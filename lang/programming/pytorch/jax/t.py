
import math

import jax
import jax.lax as lax
import jax.numpy as jnp
import jax.random as jrandom
import optax  # https://github.com/deepmind/optax

import equinox as eqx


f1 = lambda x : x ** 2

f2 = lambda x : 2 * x

f3 = lambda x : f2( f1(x) )

x = 2.

X = jnp.array( [2 , 2], jnp.float32 )

( A1, (grad, ) ) = jax.value_and_grad(f1, argnums=(0,))( x )

( A2, (grad2, ) ) = jax.value_and_grad(f2, argnums=(0,))( A1 )

( A3, (grad3, ) ) = jax.value_and_grad(f3, argnums=(0,))( x )


chain = grad2 * grad  # 复合函数求导的链式法则

assert ( chain == grad3 )



( grad11, ) = jax.jacfwd(f1, argnums=(0,))( X )


a = 1

"""

d f1 = 2 * x

d f2 = 2


d f3 = d f2 ( f1(x)  ) * d f1 ( x )

     = 2 * 2 * x

     = 4 * x

"""

a = 1

@jax.jit
@jax.grad
def loss_fn(model, x, y):
    pred_y = jax.vmap(model)(x)
    return jax.numpy.mean((y - pred_y) ** 2)

batch_size, in_size, out_size = 32, 2,  3
model = eqx.nn.Linear(in_size, out_size, key=jax.random.PRNGKey(0))
x = jax.numpy.zeros((batch_size, in_size))
y = jax.numpy.zeros((batch_size, out_size))
grads = loss_fn(model, x, y)

a = 1