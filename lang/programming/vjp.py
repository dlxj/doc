
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md

import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

# F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)

# dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I

# dF / dX = I 克罗内克积符号 A^T

A = jnp.array( [[2,3]] , jnp.float16 )

X = jnp.array( [[1,2],[3,4]] , jnp.float16 )

F = jnp.dot( A, X )



# jax.numpy.kron(a, b)


a = 1

