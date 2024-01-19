

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







