# import torch
# from torch.autograd import Variable
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim


import jax
import jax.numpy as jnp
import numpy as onp
import jax.random as jrandom
from optax import chain


X = jnp.array([
               [0, 0],  # (4*2) 的输入  
               [0, 1],
               [1, 0],
               [1, 1]
             ], jnp.float32)

Y = jnp.array([
                [0],    # (4*1) 的输出
                [1],
                [1],
                [0]
             ], jnp.float32)

# (4*2) . (2*2) + (4*2) = (4*2)  
# (4*2) . (2*1) + (4*1) = (4*1)

key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)

W1 = jax.random.normal(key1, shape=(2, 2), dtype=jnp.float32)   # (2*2) 权重

W2 = jax.random.normal(key2, shape=(2, 1), dtype=jnp.float32)   # (2*1) 权重


b1 = jax.random.normal(key3, shape=(4, 2), dtype=jnp.float32)   # (1*3) 偏置

b2 = jax.random.normal(key4, shape=(4, 1), dtype=jnp.float32)   # (1*1) 偏置


f1 = lambda X, W1, b1 : jax.nn.sigmoid( jnp.dot( X, W1 ) + b1 )

f2 = lambda A1, W2, b2 : jax.nn.sigmoid( jnp.dot( A1, W2 ) + b2 )

f3 = lambda X, W1, b1, W2, b2 : f2( f1(X, W1, b1), W2, b2 )

def loss( X, W1, b1, W2, b2 ):
    
    A1 = f1( X, W1, b1  )

    (jacobian10, jacobian11) = jax.jacfwd(f1, argnums=(1, 2))( X, W1, b1 )
    # print(jacobian10)

    # (4, 2, 2, 2)  (4, 1, 4, 2)

    A2 = f2( A1, W2, b2  )
    (jacobian20, jacobian21, jacobian22) = jax.jacfwd(f2, argnums=(0, 1, 2))( A1, W2, b2 )
    # print(jacobian20)

    """
    
    d f2 / d W1 = d f2 / d A1 * d A1 / d W1 
    
    """

    # (4, 1, 2, 2)
    A3 = f3( X, W1, b1, W2, b2 )
    (jacobian30, jacobian31, jacobian32, jacobian33) = jax.jacfwd(f3, argnums=(1, 2, 3, 4))(  X, W1, b1, W2, b2  )

    chain = jacobian20 * jacobian10

    E = A2 - Y

    lss = jnp.sum( E ** 2 )

    return lss

loss_jit = jax.jit(loss)

# lss = loss( X, W1, b1, W2, b2 )

t = 1

# lss = loss(A2)
# (jacobian30, ) = jax.jacrev(loss, argnums=(0, ))( A2 )

# """

# 链式法则求损失函数对网络参数 W1 的偏导

# d loss / d W1 =   d loss / d A2 *    d A2 / d A1  *    d A1 / d W1

#               =  jacobian30  . jacobian20 . jacobian10
#               (4*1) . (4*1*4*2) . (4*2*2*2)
# """

# t1 = jnp.dot( jacobian30, jacobian20 )

# # t1 = jnp.dot( jnp.array( jacobian30, jnp.float32), jnp.array( c, jnp.float32) )

alpha = 0.3 # 学习率
maxIter = 50000 # 最大迭代次数

for k in range(maxIter): 

    ( lss, grads ) = jax.value_and_grad(loss_jit, argnums=(1,2,3,4,))( X, W1, b1, W2, b2 )  # 表示对 第1,2,3,4 个参数进行求导 (索引从0 开始，这里的第一个参数是 W1)

    W1 = W1 - alpha * grads[0]
    b1 = b1 - alpha * grads[1]
    W2 = W2 - alpha * grads[2]
    b2 = b2 - alpha * grads[3]

    if lss < 0.001: 

        print(f"loss is: {lss}, curr iter num: {k}")

        print('final results: ')

        A1 = f1( X, W1, b1  )
 
        A2 = f2( A1, W2, b2  )
        
        E = A2 - Y

        lss = jnp.sum( E ** 2 )

        print( A2 )
       
        break

    if k % 100 == 0:
        print(f"loss is: {lss}, curr iter num: {k}")

# # 求前向传播的均方误差
# def loss(X, W1, b1, W2, b2):
#     A1 = np.dot(X, W1) + b1  
#     # H1 = sigmoid(A1)
#     H1 = jax.nn.sigmoid(A1)

#     A2 = np.dot(H1, W2) + b2  
#     H2 = jax.nn.sigmoid(A2)

#     E = H2 - Y             # 误差值
#     E2 = E ** 2
    
#     errs = np.sum( E2, axis=0 )[0] # 按列求和

#     lss = 1 / 2 * errs  # 均方误差值

#     return lss[0]


# loss_jit = jax.jit(loss)

# for k in range(maxIter): 

#     # grads = jax.grad(loss, argnums=(1,))(X, W, m)
    
#     [ lss, grads ] = jax.value_and_grad(loss_jit, argnums=(1,2,3,4,))(X, W1, b1, W2, b2)  # 表示对 第1,2,3,4 个参数进行求导 (索引从0 开始，这里的第一个参数是 W1)

#     lss = float(lss)  # lss 是 0 维数组，不能用下标去索引

#     W1 = W1 - alpha * grads[0]
#     b1 = b1 - alpha * grads[1]
#     W2 = W2 - alpha * grads[2]
#     b2 = b2 - alpha * grads[3]

#     if lss < 0.001: 

#         print(f"loss is: {lss}, curr iter num: {k}")

#         print('final results: ')

#         for input, target in zip(X, Y):
#             A1 = np.dot(input, W1) + b1  
#             H1 = sigmoid(A1)

#             A2 = np.dot(H1, W2) + b2  
#             H2 = jax.nn.sigmoid(A2)

#             print("Input:[{}] Target:[{}] Predicted:[{}]".format(
#                 input, target, H2, input - target
#             ))
       
#         break

#     if k % 100 == 0:
#         print(f"loss is: {lss}, curr iter num: {k}")

