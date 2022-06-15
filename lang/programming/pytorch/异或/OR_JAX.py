import numpy as onp

import jax
import jax.numpy as np
import itertools

"""
异或问题, JAX 自动微分实现
"""

# import numpy as np

# 此激活函数设计为可以接受列向量
# 返回结果也是列向量
# np.exp 的实现可以接受向量作为参数，所以代码很简洁
def sigmoid (x):
    return 1/(1 + np.exp(-x))

m = 4 # 样本数
n = 3 # 列数
alpha = 0.5 # 学习率
maxIter = 50000 # 最大迭代次数

X = np.array([
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]
             ], onp.float)

# 输入矩阵，维度4*3。注意偏置作为列向量添加进来了

Y = np.array([
                [0],
                [1],
                [1],
                [1]
             ], onp.float)
# 4*1 输出

W = onp.random.uniform(size=(3, 1))   # 3*1 权重
#W = W * 0.1 # 据说对于sigmoid 激活函数，更小的权重更容易收敛
"""
观察输入输出的维度，可以看出需要对X 的列进行压缩，既把列从维度3 降维到1
    右乘是列变换，应该让权重矩阵W 右乘X，既 X.W
    矩阵点乘的维度变化
        (4*3).(3*1) = 4*1
"""


# 求前向传播的均方误差
def loss(X, W, m):
    A = np.dot(X, W)  # 前向传播
    H = sigmoid(A)    # 预测结果
    E = H - Y         # 误差值
    E2 = E ** 2
    
    totalErrs = np.sum( E2, axis=0 )[0] # 按列求和

    lss = 1 / (2 * m) * totalErrs  # 均方误差值

    return lss


loss_grad = jax.grad(loss)  # 自动求梯度


for k in range(maxIter): 

    lss = loss(X, W, m)

    grads = jax.grad(loss, argnums=(1,))(X, W, m)  # 表示对 第1 个参数进行求导 (索引从0 开始，这里的第一个参数是 W)

    grads = loss_grad(X, W, m)

    A = np.dot(X, W)  # 前向传播
    H = sigmoid(A)    # 预测结果
    E = H - Y         # 误差值

    errs = sum( list(itertools.chain(*abs(E))) )  # 误差总和
    """
    注意这里算的不是均方误差，但是下面的权重更新是用了均方误差函数的导数来算的
    这里的errs 只是用来衡量预测结果有多接近期望结果，以便提前结速迭代
    """
    if errs < 0.05:
        print(f'stop at {k}')
        print("Weight: ")
        print(W)
        break

    """
    权重更新
    """
    for j in range(n):
        s = 0
        for i in range(m):
            s += E[i] * H[i] * (1 - H[i]) * X[i][j]  # W_{j} 的梯度
            W[j] = W[j] - alpha * 1/m * s # 更新权重

    print(f"err sum is: {errs}, curr iter num: {k}")
    print(H)