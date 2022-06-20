
# OR_JAX_vmap.py
# 或运算的 JAX.vmap 向量化实现
# reference:
#   doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md   JAX section
import numpy as onp
import jax
import jax.numpy as np


X = np.array([
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]
             ], onp.float)
# 注意第一列是偏置， 把它作为输入向量的一部分添加进来了

Y = np.array([
                [0],
                [1],
                [1],
                [1]
             ], onp.float)


W = onp.random.uniform(size=(3, 1))   # 3*1 权重
#W = W * 0.1 # 据说对于sigmoid 激活函数，更小的权重更容易收敛

# 以同样的顺序随机化两个数组
def shuffle(X, Y):
    randomize = onp.arange(len(X))
    onp.random.shuffle(randomize)

    X = X[ randomize ]
    Y = Y[ randomize ]

    return X, Y

X, Y = shuffle(X, Y)

print( X )
print( Y )


# 生成一批数据
def batch_data(X, Y):
    X_batch = []
    Y_batch = []

    for i in range(4):

        X, Y = shuffle(X, Y)

        for j in range( len(X) ):
            X_batch.append( X[j].copy().reshape(1, 3) )
            Y_batch.append( Y[j].copy().reshape(1, 1) )

    X_batch = np.array( X_batch, np.float32 )  # (16*1*3)  # 批量输入 16 个 X，同时进行训练，输出 16 个结果
    Y_batch = np.array( Y_batch, np.float32 )

    return X_batch, Y_batch


# X_batch, Y_batch = batch_data(X, Y)

# print( X_batch[0:5, :] )
# print( Y_batch[0:5, :] )


# batch_size = len(X_batch)
epoch = 12000
alpha = 0.1 # 学习率

# m = batch_size # 样本数
# n = 3 # 列数
# alpha = 0.5 # 学习率
# maxIter = 50000 # 最大迭代次数


# f = lambda X, W : np.dot(X, W)
# # X = jax.random.normal(jax.random.PRNGKey(55), (1, 3))
# # W = jax.random.normal(jax.random.PRNGKey(77), (3, 1))
# # (1*3) . (3*1) = (1*1)

# a = f( X, W )
# b = f( X_batch[0], W )  # (3*1) . (3*1) = (1*1)
# c = f( X_batch, W )     # (16*3*1) . (3*1) = (16*1*1)


# 此激活函数设计为可以接受列向量
# 返回结果也是列向量
# np.exp 的实现可以接受向量作为参数，所以代码很简洁
def sigmoid (x):
    return 1/(1 + np.exp(-x))



# X = np.array([
#                 [1, 0, 0],
#                 [1, 0, 1],
#                 [1, 1, 0],
#                 [1, 1, 1]
#              ], onp.float)

# # 输入矩阵，维度4*3。注意偏置作为列向量添加进来了

# Y = np.array([
#                 [0],
#                 [1],
#                 [1],
#                 [1]
#              ], onp.float)
# # 4*1 输出


"""
观察输入输出的维度，可以看出需要对X 的列进行压缩，既把列从维度3 降维到1
    右乘是列变换，应该让权重矩阵W 右乘X，既 X.W
    矩阵点乘的维度变化
        (4*3).(3*1) = 4*1
"""


# 求前向传播的均方误差
def loss(W, X, Y, m):
    A = np.dot(X, W)  # 前向传播
    H = sigmoid(A)    # 预测结果
    E = H - Y         # 误差值
    E2 = E ** 2
    
    errs = np.sum( E2, axis=0 )[0] # 按列求和

    lss = 1 / (2 * m) * errs  # 均方误差值

    return lss[0]


for k in range(epoch): 

    X_batch, Y_batch = batch_data(X, Y)

    if (k == 0):
        print( X_batch[0:5, :] )
        print( Y_batch[0:5, :] )


    batch_size = len(X_batch)

    lss = loss(W, X_batch, Y_batch, batch_size) 

    # grads = jax.grad(loss, argnums=(1,))(X, W, m)
    
    [ lss, grads ] = jax.value_and_grad(loss, argnums=(0,))(W, X_batch, Y_batch, batch_size)  # 表示对 第0 个参数进行求导 (索引从0 开始，这里的第一个参数是 W)

    lss = float(lss)  # lss 是 0 维数组，不能用下标去索引

    W = W - alpha * grads[0]


    if lss < 0.001: 

        A = np.dot(X, W)  # 前向传播
        H = sigmoid(A)    # 预测结果
        E = H - Y         # 误差值

        print(f"loss is: {lss}, curr iter num: {k}")
        print(H) 
        
        break

    if k % 10 == 0:
        print(f"loss is: {lss}, curr iter num: {k}")
