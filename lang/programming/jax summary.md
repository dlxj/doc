# rwkv_jax

```python

# see huggingface/rwkv_numpy/rwkv.py

# pip install tokenizers
# pip install -U "jax[cpu]"

# Taken from https://johanwind.github.io/2023/03/23/rwkv_details.html. 
# I've added additional comments restructured it a tiny bit, which makes it clearer for me.


""""
probs
    shape:
        (50277,)
    # RWKV 函数输出下一个 token 的概率分布,  总 token 数为 50277
    
"""

# import numpy as np
import jax.numpy as np
from torch import load as torch_load  # Only for loading the model weights
from torch import save as torch_save
from tokenizers import Tokenizer
import base64
from collections import OrderedDict
import json
import jax
import jax.numpy as jnp
import jax.random as jrandom

exp = np.exp
layer_norm = lambda x, w, b : (x - np.mean(x)) / np.std(x) * w + b
sigmoid = lambda x : 1/(1 + exp(-x))


def RWKV(model, token, state):
    keys = model.keys()
    emb = [key for key in model.keys() if key.startswith('emb')]
    blocks_0_ln0 = [key for key in model.keys() if key.startswith('blocks.0.ln0')]
    blocks_0_att = [key for key in model.keys() if key.startswith('blocks.0.att')]
    blocks_0_ffn = [key for key in model.keys() if key.startswith('blocks.0.ffn')]
    ln_out = [key for key in model.keys() if key.startswith('ln_out')]
    head = [key for key in model.keys() if key.startswith('head')]
    
    params = lambda prefix: [model[key] for key in model.keys() if key.startswith(prefix)]
    
    emb_weight = model['emb.weight']
    
    x = emb_weight[token]
    
    # b64 = base64.b64encode(x)
    # bytes = base64.decodebytes(b64)
    # x__ = np.frombuffer(bytes, dtype=np.float32)
    
    blocks_0_ln0_weight = model['blocks.0.ln0.weight']
    blocks_0_ln0_bias = model['blocks.0.ln0.bias']
    
    x = layer_norm(x, blocks_0_ln0_weight, blocks_0_ln0_bias)

    #x = params('emb')[0][token]
    #x = layer_norm(x, *params('blocks.0.ln0'))

    for i in range(N_LAYER):
        blocks_i_ln1_weight = model[f'blocks.{i}.ln1.weight']
        blocks_i_ln1_bias = model[f'blocks.{i}.ln1.bias']
        x_ = layer_norm(x, blocks_i_ln1_weight, blocks_i_ln1_bias)
        
        blocks_i_att_time_decay = model[f'blocks.{i}.att.time_decay']
        blocks_i_att_time_first = model[f'blocks.{i}.att.time_first']
        blocks_i_att_time_mix_k = model[f'blocks.{i}.att.time_mix_k']
        blocks_i_att_time_mix_v = model[f'blocks.{i}.att.time_mix_v']
        blocks_i_att_time_mix_r = model[f'blocks.{i}.att.time_mix_r']
        blocks_i_att_key_weight = model[f'blocks.{i}.att.key.weight']
        blocks_i_att_value_weight = model[f'blocks.{i}.att.value.weight']
        blocks_i_att_receptance_weight = model[f'blocks.{i}.att.receptance.weight']
        blocks_i_att_output_weight = model[f'blocks.{i}.att.output.weight']
        
                
        last_x, last_num, last_den = state[i][:3]
        dx, x_num_den = time_mixing(x_, last_x, last_num, last_den, 
                                blocks_i_att_time_decay,
                                blocks_i_att_time_first,
                                blocks_i_att_time_mix_k,
                                blocks_i_att_time_mix_v,
                                blocks_i_att_time_mix_r,
                                blocks_i_att_key_weight,
                                blocks_i_att_value_weight,
                                blocks_i_att_receptance_weight,
                                blocks_i_att_output_weight
                            )

        # state[i][:3] = x_num_den  # just for numpy
        state = state.at[i, :3].set( x_num_den )

        x = x + dx


        blocks_i_ln2_weight = model[f'blocks.{i}.ln2.weight']
        blocks_i_ln2_bias = model[f'blocks.{i}.ln2.bias']

        blocks_i_ffn_time_mix_k = model[f'blocks.{i}.ffn.time_mix_k']
        blocks_i_ffn_time_mix_r = model[f'blocks.{i}.ffn.time_mix_r']
        blocks_i_ffn_key_weight = model[f'blocks.{i}.ffn.key.weight']
        blocks_i_ffn_receptance_weight = model[f'blocks.{i}.ffn.receptance.weight']
        blocks_i_ffn_value_weight = model[f'blocks.{i}.ffn.value.weight']


        x_ = layer_norm(x, blocks_i_ln2_weight, blocks_i_ln2_bias)
        dx, tmp_x = channel_mixing(x_, state[i][3], 
                            blocks_i_ffn_time_mix_k,
                            blocks_i_ffn_time_mix_r,
                            blocks_i_ffn_key_weight,
                            blocks_i_ffn_receptance_weight,
                            blocks_i_ffn_value_weight
                        )

        # state[i][3] = tmp_x  # just for numpy
        state = state.at[i, 3].set( tmp_x )

        x = x + dx
        

    
    ln_out_weight = model[f'ln_out.weight']
    ln_out_bias = model[f'ln_out.bias']
    head_weight = model[f'head.weight']

    x = layer_norm(x, ln_out_weight, ln_out_bias)
    x = head_weight @ x


    e_x = exp(x - np.max(x))
    probs = e_x / e_x.sum() # Softmax of x

    return probs, state


def save_model(model, pth):
    ml = OrderedDict()
    for k, v in model.items():
        ml[k] = base64.b64encode(v).decode('ascii')  # bytes to asscii
        a = 1
    ml_str = json.dumps(ml)
    # ml_ = json.loads(ml_str, object_pairs_hook=OrderedDict)
    with open(pth, 'w', encoding='utf-8') as f:
	    f.write(ml_str)
    

def time_mixing(x, last_x, last_num, last_den, decay, bonus, mix_k, mix_v, mix_r, Wk, Wv, Wr, Wout):
    # Part of the state tensor
    #   - last_x  - previous time step embedding (input / prev layer's emb) (1024,)
    #   - last_num - numerator, or "weighted sum of past values" (1024,)
    #   - last_den - denominator, "sum of weights of past values" (1024,)
    # Learnable parameters
    #   - decay (1024,)
    #   - bonus (1024,)
    #   - mix_k - mixing ratio for key (1024,)
    #   - mix_v - mixing ratio for value (1024,)
    #   - mix_r - mixing ratio for receptance (1024,)
    #   - Wk - affine transformation for key (1024, 1024)
    #   - Wv - affine transformation for value (1024, 1024)
    #   - Wr - affine transformation for receptance (1024, 1024)
    #   - Wout - affine transformation for output (1024, 1024)

    # In a typical transformer, the “time mixing” would be done by multi head attention.
    # However, in the RWKV model, the time mixing is done at each time step when
    # num(erator) and den(ominator) are updated. This is similar to how RNNs work.

    # Linear interpolation below between x and last_x uses element-wise mixing ratios
    # mix_*, which are learned weights (of same size as x, last_x).
    # W* are 1024x1024 matrices; matmul with these are most time-consuming.
    k = Wk @ (x * mix_k + last_x * (1 - mix_k))
    v = Wv @ (x * mix_v + last_x * (1 - mix_v))
    r = Wr @ (x * mix_r + last_x * (1 - mix_r))

    # num / den ~= Weighted average of past values
    # wkv ~= Also weighted average of past values, 
    #        but we are adding a "bonus" weight to the current value `v`.
    #        Previous weights get exponentially smaller weight, which is
    #        already captured in the last_num and last_den variables.
    #        However the weight doesn't decay the same for each dimension,
    #        but is determined on each time step based on the decay vector 
    #        (see num and den updates below)
    wkv = (
        (last_num + exp(bonus + k) * v) /
        (last_den + exp(bonus + k))
    )
    # Multiplying the wkv (weighted average of past values) with sigmoid(r) is similar
    # to a "gate" in RNNs that controls how much of the past values to use, since
    # sigmoid(r) is a value between 0 and 1.
    rwkv = sigmoid(r) * wkv
    # Final linear (affine) transformation to get the output embedding.
    time_mixed = Wout @ rwkv

    # Below we set the numerator and denominator for the next time step.
    #   num - numerator, or "weighted sum of past values"
    #   den - denominator, "sum of weights of past values"
    # Can be seen as interpolate between previous step num (or den) and a new value,
    # where element-wise decay vector determines the amount of decay per dimension.
    num = exp(-exp(decay)) * last_num + exp(k) * v
    den = exp(-exp(decay)) * last_den + exp(k)

    return time_mixed, (x, num, den)


def channel_mixing(x, last_x, mix_k, mix_r, Wk, Wr, Wv):
    # Wk - (4096, 1024)
    # Wr - (1024, 1024)
    # Wv - (1024, 4096)
    
    # In a typical transformer, the “channel mixing” is done by a simple FF NN.
    # By contrast, we use two separate fully connected layers on the input
    # (where input linearly interpolates between the current input and 
    # previous time step input) and then multiply them element-wise.

    # Linear interpolation (below) between x and last_x uses an element-wise mixing ratio
    # mix_k and mix_r, which are learned weights (of same size as x, last_x).
    # Wk, Wr, Wv are 1024x1024 matrices; matmul with these are most time-consuming.

    # x and last_x is linearly interpolated with mixing ratio mix_k,
    # then passed through a FC layer with squared relu activation
    k = Wk @ (x * mix_k + last_x * (1 - mix_k)) # @ is matrix multiplication
    k = np.maximum(k, 0) ** 2 # squared relu activation

    # x and last_x is linearly interpolated with mixing ratio mix_r,
    # then passed through a FC layer with sigmoid activation
    r = Wr @ (x * mix_r + last_x * (1 - mix_r))
    r = sigmoid(r)

    # K-mixed input is passed through affine transformation (without activation, 
    # so not quite a FC layer) before being multiplied to r-mixed input element-wise.
    vk = Wv @ k
    channel_mixed = r * vk

    return channel_mixed, x # pass x along unchanged, will be last_x in the next step


def sample_probs(probs, temperature=1.0, top_p=0.85):
    sorted_probs = np.sort(probs)[::-1]
    cumulative_probs = np.cumsum(sorted_probs)
    cutoff = sorted_probs[np.argmax(cumulative_probs > top_p)]
    idx = probs < cutoff
    # probs[probs < cutoff] = 0
    probs = probs.at[idx].set(0)
    probs = probs ** (1 / temperature)
    # return np.random.choice(a=len(probs), p=probs / np.sum(probs))
    key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)
    return jax.random.choice(key=key4, a=len(probs), p=probs / np.sum(probs))


# Available at https://huggingface.co/BlinkDL/rwkv-4-pile-430m/resolve/main/RWKV-4-Pile-430M-20220808-8066.pth
MODEL_FILE = 'RWKV-4-Pile-430M-20220808-8066.pth'
N_LAYER = 24
N_EMBD = 1024

print(f'\nLoading {MODEL_FILE}')
weights = torch_load(MODEL_FILE, map_location='cpu')
for k in weights.keys():
    if '.time_' in k:
        weights[k] = weights[k].squeeze()
    weights[k] = weights[k].float().numpy() # convert to f32 type


# import pickle
# with open("new.pkl", "wb") as f:
#     pickle.dump(weights, f)


emb_weight = weights['emb.weight']

# weights['emb.weight'] = np.random.uniform(size=(50277, 1024))
    # 只替换嵌入向量成随机数, 后面再自已训练？

# key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)
# weights['emb.weight'] = jax.random.normal(key1, shape=(50277, 1024), dtype=jnp.float32)   

# Available at https://github.com/BlinkDL/ChatRWKV/blob/main/20B_tokenizer.json
tokenizer = Tokenizer.from_file("20B_tokenizer.json")

print(f'\nPreprocessing context')
context = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."

# The 4 dimensions are 
#     [last_x, last_num, last_den] (after time mixing) - used by time mixing
#     last_x (after channel mixing) - used by channel mixing
state = np.zeros((N_LAYER, 4, N_EMBD), dtype=np.float32)
for token in tokenizer.encode(context).ids:
    probs, state = RWKV(weights, token, state)

print(context, end="")
for i in range(100):
    token = sample_probs(probs)
    print(tokenizer.decode([token]), end="", flush=True)
    probs, state = RWKV(weights, token, state)

```







# cuda 多版本切换

```
/usr/local/cuda/bin/nvcc --version

ldconfig -p | grep cuda

wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda_11.7.1_515.65.01_linux.run
sudo sh cuda_11.7.1_515.65.01_linux.run

update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.7 117
ln -sfT /usr/local/cuda-11.7 /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda

```







```
jax.device_get(logits) # 得到普通 array
```



# 概率输出

```
# see echodict\transformer\t.py

labels_out = logits.argmax(axis=-1)   # 模型输出的分类
acc = (labels_out == labels).mean()   # 正确率
```

- `.argmax(axis=-1)` 它沿着最后一个轴（通常是特征或类别的轴）查找最大值的索引。在分类任务中，此操作可以找出模型认为最可能的类别。
- `(labels_out == labels)` 比较预测标签`labels_out`与真实标签`labels`是否相等，返回一个布尔数组。
- `.mean()` 计算布尔数组中`True`值的平均值，因为在Python中`True`可被视为`1`，`False`可被视为`0`。因此，这个方法会得到分类正确的样本占总样本的比例，即模型的准确率`acc`。



# bf16

```
# https://github.com/google/jax/issues/8044 bfloat16 pmap cuda11.1 results in error

import jax
import numpy as np
import jax.numpy as jnp
jax.devices()

from typing import NamedTuple, Tuple
import functools

class Params(NamedTuple):
    weight: jnp.ndarray
    bias: jnp.ndarray


def init(rng) -> Params:
    """Returns the initial model params."""
    weights_key, bias_key = jax.random.split(rng)
    weight = jax.random.normal(weights_key, (), dtype=D_TYPE)
    bias = jax.random.normal(bias_key, (), dtype=D_TYPE)
    return Params(weight, bias)


def loss_fn(params: Params, xs: jnp.ndarray, ys: jnp.ndarray) -> jnp.ndarray:
    """Computes the least squares error of the model's predictions on x against y."""
    pred = params.weight * xs + params.bias
    return jnp.mean((pred - ys) ** 2)

LEARNING_RATE = 0.005

# So far, the code is identical to the single-device case. Here's what's new:


# Remember that the `axis_name` is just an arbitrary string label used
# to later tell `jax.lax.pmean` which axis to reduce over. Here, we call it
# 'num_devices', but could have used anything, so long as `pmean` used the same.
@functools.partial(jax.pmap, axis_name='num_devices')
def update(params: Params, xs: jnp.ndarray, ys: jnp.ndarray) -> Tuple[Params, jnp.ndarray]:
    """Performs one SGD update step on params using the given data."""

    # Compute the gradients on the given minibatch (individually on each device).
    loss, grads = jax.value_and_grad(loss_fn)(params, xs, ys)

    # Combine the gradient across all devices (by taking their mean).
    grads = jax.lax.pmean(grads, axis_name='num_devices')

    # Also combine the loss. Unnecessary for the update, but useful for logging.
    loss = jax.lax.pmean(loss, axis_name='num_devices')

    # Each device performs its own update, but since we start with the same params
    # and synchronise gradients, the params stay in sync.
    new_params = jax.tree_multimap(
        lambda param, g: param - g * LEARNING_RATE, params, grads)

    return new_params, loss

# Generate true data from y = w*x + b + noise
true_w, true_b = 2, -1
xs = np.random.normal(size=(128, 1))
noise = 0.5 * np.random.normal(size=(128, 1))
ys = xs * true_w + true_b + noise

# Initialise parameters and replicate across devices.
D_TYPE = jnp.bfloat16
params = init(jax.random.PRNGKey(123))
n_devices = jax.local_device_count()
replicated_params = jax.tree_map(lambda x: jnp.array([x] * n_devices), params)

def split(arr):
    """Splits the first axis of `arr` evenly across the number of devices."""
    return arr.reshape(n_devices, arr.shape[0] // n_devices, *arr.shape[1:])

# Reshape xs and ys for the pmapped `update()`.
x_split = split(xs)
y_split = split(ys)

type(x_split)

def type_after_update(name, obj):
    print(f"after first `update()`, `{name}` is a", type(obj))

# Actual training loop.
for i in range(1000):

    # This is where the params and data gets communicated to devices:
    replicated_params, loss = update(replicated_params, x_split, y_split)

    # The returned `replicated_params` and `loss` are now both ShardedDeviceArrays,
    # indicating that they're on the devices.
    # `x_split`, of course, remains a NumPy array on the host.
    if i == 0:
        type_after_update('replicated_params.weight', replicated_params.weight)
        type_after_update('loss', loss)
        type_after_update('x_split', x_split)

    if i % 100 == 0:
        # Note that loss is actually an array of shape [num_devices], with identical
        # entries, because each device returns its copy of the loss.
        # So, we take the first element to print it.
        print(f"Step {i:3d}, loss: {loss[0]:.3f}")


# Plot results.

# Like the loss, the leaves of params have an extra leading dimension,
# so we take the params from the first device.
params = jax.device_get(jax.tree_map(lambda x: x[0], replicated_params))
```





# purejaxrl

[purejaxrl](https://github.com/luchris429/purejaxrl)







