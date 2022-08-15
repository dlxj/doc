

import jax.numpy as jnp
import jax
from jax import random, jacfwd, vjp

X = jnp.array([[0,1]], jnp.float16) # (1*2)

# W = jnp.array([[0],[1]], jnp.float16) # (2*2)

key = random.PRNGKey(0)
key, W_key, b_key = random.split(key, 3)
W = random.normal(W_key, (2, 2))
b = random.normal(b_key, (1, 2))


def forward(X, W, b):
    return jax.nn.sigmoid(jnp.dot(X, W) + b)

def vgrad(f, x, w, b): # 输出 x 的梯度
  y, vjp_fn = vjp(f, x, w, b)
  return vjp_fn(jnp.ones(y.shape))

A = forward(X, W, b)

(grad_x, grad_w, grad_b) = vgrad( forward, X, W, b )

(grads, ) = jax.jacfwd(forward, argnums=(1,))(X, W, b)


# vgrad(forward, )


# jax.nn.sigmoid

a = 1

X = jnp.array([[2],[3]], jnp.float16) # (2*1) -> (2*1) -> (1,)

f = lambda X: X ** 2

Y = f(X)

( grad10, ) = jax.jacfwd(f, argnums=(0,))( X )

s = jax.numpy.sum( Y )

( grad20, ) = jax.jacfwd(jax.numpy.sum, argnums=(0,))( Y )

y, vjp_fun = jax.vjp(jax.numpy.sum, Y)

a = 1


# import jax.numpy as jnp
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

print('Jacobian using vjp and stacking:')
print(jnp.vstack([vjp_fun(mi) for mi in M]))

# computing directly using jacrev function
print('Jacobian using jacrev directly:')
print(jacrev(f)(W))


import torch

def j3():
 x = torch.ones(3, requires_grad=True)

 y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))

 v = torch.tensor([3, 5, 7])

 y.backward(v)
 print(x.grad)
 """
 The Jacobian seems correct and if it multiplies on vector (3, 5, 7) I would expect result to be (11, 17, 14).
 Got it! We should transpose Jacobian before multiplication. Then everything matches.
 """

 print( torch.matmul(  torch.tensor([ [2, 0, 0], [1, 2 , 0], [0, 1, 2] ]),  torch.tensor([ [3], [5], [7] ]) ) )       # J.t() @ v  结果是列向量
 print( torch.matmul(  torch.tensor([ [3], [5], [7] ]).t(), torch.tensor([ [2, 1, 0], [0, 2 , 1], [0, 0, 2] ])  ) )   # v.t() @ J  结果是行向量

j3()