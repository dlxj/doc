
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md

import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

import numpy as np

import torch

# F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)

# dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I

# dF / dX = I 克罗内克积符号 A^T    dX 形状是 (4*2) ，所以 I 是 (2*2)。单位阵必是方阵

# G = FV # (1*2) . (2*1) => (1*1)
    # 

A = jnp.array( [[1,2]] , jnp.float32 )

X = jnp.array( [[3,4],[5,6]] , jnp.float32 )

V = jnp.array( [[7],[8]] , jnp.float32 )

def f(A, X):
    return jnp.dot( A, X )

F = f( A, X )
G = f( F, V )

l = lambda A, X, V: f( f(A, X), V )
L = l(A, X, V)
( grad_X, grad_V) = jax.jacfwd(l, argnums=(1,2))( A, X, V )  # dG / dX 和  dG / dV
    # 为了和后面分步计算的雅克比乘积结果对比 (链式法则求各层的梯度)

I = jnp.eye( 2 )

A_T = jnp.transpose(A)

kr = jax.numpy.kron(I, A_T) # (4*2)  # 求 dF / dX
    # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 2 个元素，参数总共 4 个元素，求导结果总共应该是 8 个元素
        # df_1(x) .. df_n(x) 横向展开， dx 纵向展开
        # kr 的转置应该就是雅可比，它是 dx 横向展开, df(x) 纵向展开

kr2 = jnp.transpose(F) # (2*1)  # 求 dG / dV



a = 1

# 下面用 jax 自动微分验证

( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
    # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样

grad_42 = jnp.reshape(grad, (4, 2)) # 和前面 kr 一样了


( grad2, ) = jax.jacfwd(f, argnums=(1,))( F, V )

grad2_21 = jnp.reshape(grad2, (2, 1))

a = 1


y, vjp_fn = jax.vjp(f, A, X) # 返回函数的计算结果，还有用于计算 vjp 的函数 vjp_fn，它需要一个向量作为参数
    # 你传一个向量进去，vjp_fn 就会给你一个 v * 雅可比 的结果


AA = torch.tensor(A.__array__())
XX = x = torch.tensor(X.__array__())

def ff(AA, XX):
    return torch.mm(AA, XX) # 数学里的矩阵乘法，要求两个Tensor的维度满足矩阵乘法的要求

FF = ff(AA, XX)

jacobians = torch.autograd.functional.jacobian(ff, (AA, XX))
jacobian_XX = jacobians[1]  # (1, 2, 2, 2)  和 jax 算出来的 grad 是一样的

jacobian_XX_42 = torch.reshape(jacobian_XX, (4, 2)) # 和前面 kr 一样了

a = 1

# def g(F):
#     return jnp.sum(F)
#     # return jax.nn.sigmoid(F)



a = 1



