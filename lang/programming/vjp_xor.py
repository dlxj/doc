
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md

import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

# F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)

# dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I

# dF / dX = I 克罗内克积符号 A^T    dX 形状是 (4*2) ，所以 I 是 (2*2)。单位阵必是方阵

A = jnp.array( [[2,3]] , jnp.float32 )

X = jnp.array( [[1,2],[3,4]] , jnp.float32 )

def f(A, X):
    return jnp.dot( A, X )
F = f( A, X )

I = jnp.eye( 2 )

A_T = jnp.transpose(A)

kr = jax.numpy.kron(I, A_T) # (4*2) 
    # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 2 个元素，参数总共 4 个元素，求导结果总共应该是 8 个元素
        # df_1(x) .. df_n(x) 横向展开， dx 纵向展开

a = 1

# 下面用 jax 自动微分验证

( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
    # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样

a = 1



