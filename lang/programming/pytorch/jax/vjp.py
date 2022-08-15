
import jax.numpy as jnp
from jax import random, jacrev, vjp

key = random.PRNGKey(0)


def sigmoid(x):
    return 0.5 * (jnp.tanh(x / 2) + 1)


def predict(W, b, inputs):
    return sigmoid(jnp.dot(inputs, W) + b)


key, W_key, b_key = random.split(key, 3)
W = random.normal(W_key, (3,))
b = random.normal(b_key, ())

inputs = jnp.array([[0.52, 1.12,  0.77],
                    [0.88, -1.08, 0.15],
                    [0.52, 0.06, -1.30],
                    [0.74, -2.49, 1.39]])

# (4,3) . (3,) + () = (4,) 

t1 = sigmoid(jnp.dot(inputs, W) + b)

def f(W):
    return predict(W, b, inputs)


def basis(size, index):
    a = [0.0] * size
    a[index] = 1.0
    return jnp.array(a)


M = [basis(4, i) for i in range(0, 4)]

# computing by stacking VJPs of basis vectors
y, vjp_fun = vjp(f, W)

def vgrad(f, W): # 输出 x 的梯度
  y, vjp_fn = vjp(f, W)
  return vjp_fn(jnp.ones(y.shape))

r = vgrad(f, W)

print('Jacobian using vjp and stacking:')
print(jnp.vstack([vjp_fun(mi) for mi in M]))

# computing directly using jacrev function
print('Jacobian using jacrev directly:')
print(jacrev(f)(W))