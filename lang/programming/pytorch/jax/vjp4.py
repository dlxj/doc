
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md
# https://zhuanlan.zhihu.com/p/144756543 让向量、矩阵和张量的求导更简洁些吧
# https://www.cnblogs.com/pinard/p/10825264.html
    # 矩阵对矩阵的求导是比较复杂的定义
# https://www.zhihu.com/question/52399883
    # 矩阵求导不能直接使用链式法则，即将中间导数矩阵乘起来。使用链式法则归根结底还是要考虑矩阵元素对元素的求导，即标量对标量求导。

# https://rogerluo.dev/Brochure.jl/dev/automatic-differentiation/
    # julia 实现自动微分

# https://segmentfault.com/a/1190000042199820 
    # OneFlow源码阅读6：自动微分机制

# https://zhuanlan.zhihu.com/p/25063314 机器学习中的矩阵/向量求导
    


import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

import numpy as np

import torch

A = jnp.array( [[1,2], [3, 4]] , jnp.float32 )

X = jnp.array( [[5, 6],[7, 8]] , jnp.float32 )

B = jnp.array( [[9],[10]] , jnp.float32 )

def f(a, b):
 return jnp.dot( a, b )

def c(A, X, B):
    return f( f(A, X), B)

ax = f(A, X)

axb = f(ax, B)

C = c(A, X, B)

( grad_C, ) = jax.jacfwd(c, argnums=(0,))( A, X, B )

( grad_axb_ax, ) = jax.jacfwd(f, argnums=(0,))( ax, B )  # (A.X).B 对 A.X 求导

( grad_ax_a, ) = jax.jacfwd(f, argnums=(0,))( A, X )  # A.X 对 A 求导

g_axb_a = jnp.matmul( grad_axb_ax, grad_ax_a )


"""


    A       X         B       C
( (2*2) . (2*2) ) . (2*1) = (2*1)

d c / d A = d c / d A.X  *  d A.X / d A
2*1*2*2 = 2*1*2*2 * 2*2*2*2


梯度 grad_C 的维度是 (2, 1, 2, 2)
    它是这样构造的：先是有一个正常的 2*1 的矩阵，矩阵的每一个元素都是标量，然后把这些标量全部用 2*2 的矩阵替换，就得到 (2, 1, 2, 2) 的矩阵


[
    [ b00 * x00 + b10 *x01, b00 * x10 + b10 * x11],
    [ 0, 0 ]
]

[
    [ 0, 0 ],
    [ b00 * x00 + b10 *x01, b00 * x10 + b10 * x11]
]

"""

gc00 = jnp.array(
        [
            [ B[0][0] * X[0][0] + B[1][0] * X[0][1], B[0][0] * X[1][0] + B[1][0] * X[1][1] ], 
            [ 0, 0 ]
        ], 
        jnp.float32 )

gc10 = jnp.array(
        [
            [ 0, 0 ],
            [ B[0][0] * X[0][0] + B[1][0] * X[0][1], B[0][0] * X[1][0] + B[1][0] * X[1][1] ]

        ], 
        jnp.float32 )


gc = jnp.stack([gc00, gc10 ], axis=0).reshape((2, 1, 2, 2))


# F= AX   # 求 df / dA   # (2*2) . (2*2) => (2*2)

# F = AX = IAX # 注意在 A 的左边添加了一个单位阵 I (3*3)

# dF = IdAX 

# vec(dF) = vec(IdAX) = (X^T \otimes I) vec(dA)  # \otimes 表示克罗内克积

# vec(dF) = \frac{\partial F^T}{\partial X}  vec(dX)  # 导数与微分的联系

# dF / d A = X^T \otimes I^T

pi = jnp.pi
e = jnp.e


A = jnp.array( [[1,3], [2, 4]] , jnp.float32 )

X = jnp.array( [[5, 7],[6, 8]] , jnp.float32 )

def f(A, X):
 return jnp.dot( A, X )

F = f( A, X )

( grad_A, ) = jax.jacfwd(f, argnums=(0,))( A, X )  # jax 自动微分求出的梯度 dF / dA   (3, 2, 3, 2)

def y(A, X):
    y00 = jnp.dot( A[:1, :],  X[:,:1]).__array__()[0][0]
    y01 = jnp.dot( A[:1, :],  X[:, 1:2]).__array__()[0][0]
    y10 = jnp.dot( A[1:2, :],  X[:,:1]).__array__()[0][0]
    y11 = jnp.dot( A[1:2, :],  X[:,1:2]).__array__()[0][0]

    Y = jnp

    return y00

y(A, X)

I = jnp.eye( 3 ) # I 的转置还是 I，这里就省掉了

X_T =  jnp.transpose(X)

kr = jax.numpy.kron(X_T, I) # (6*6)  # 求 dF / dX
 # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 6 个元素，参数总共 6 个元素，求导结果总共应该是 6*6 = 36 个元素
     # df_1(x) .. df_n(x) 横向展开， dx 纵向展开
     # kr 的转置应该就是雅可比，它是 dx 横向展开, df(x) 纵向展开

# grad_A_reshape = torch.reshape( torch.tensor(grad_A.__array__()), (6, 6))

grad_A_reshape = jnp.reshape(grad_A, (6, 6))  # 经观察，它和前面的 kr 排序顺序不一样，数值似乎是一样的



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