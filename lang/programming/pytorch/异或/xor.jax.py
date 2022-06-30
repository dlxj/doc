

import imp
import jax
import jax.lax as lax
import jax.numpy as jnp
import jax.random as jrandom
import optax  # https://github.com/deepmind/optax

import functools

X = jnp.array([
                [0, 0],
                [0, 1],
                [1, 0],
                [1, 1]
             ], jnp.float32)

# 输入矩阵，维度4*2。

Y = jnp.array([
                [0],
                [1],
                [1],
                [0]
             ], jnp.float32)
# 4*1 输出


# (4*4) . (4*2) = (4*2)
# (4*2) . (2*1) = (4*1) 


key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)

W1 = jrandom.normal(key1, (4, 4) )  # 第一层权重
W2 = jrandom.normal(key1, (2, 1))   # 第二层权重

b1 = jrandom.normal(key1, (4, 2))   # 第一层偏置
b2 = jrandom.normal(key1, (4, 1))   # 第二层偏置

def value_and_jacfwd(f, x):
  pushfwd = functools.partial(jax.jvp, f, (x,))
  basis = jnp.eye(x.size, dtype=x.dtype)
  y, jac = jax.vmap(pushfwd, out_axes=(None, 1))((basis,))
  return y, jac

def value_and_jacrev(f, x):
  y, pullback = jax.vjp(f, x)
  basis = jnp.eye(y.size, dtype=y.dtype)
  jac = jax.vmap(pullback)(basis)
  return y, jac

[ A1, grads1 ] = jax.jacfwd (jnp.dot, argnums=(0,))(W1, X) # 同时返回函数值和梯度

print( A1 )
print( grads1 )
