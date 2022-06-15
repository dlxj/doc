
# OR_JAX.py
import numpy as onp
import jax
import jax.numpy as np

"""
OR 运算, JAX 自动微分实现
"""

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
    
    errs = np.sum( E2, axis=0 )[0] # 按列求和

    lss = 1 / (2 * m) * errs  # 均方误差值

    return lss


loss_grad = jax.grad(loss)  # 自动求梯度


for k in range(maxIter): 

    # grads = jax.grad(loss, argnums=(1,))(X, W, m)
    
    [ lss, grads ] = jax.value_and_grad(loss, argnums=(1,))(X, W, m)  # 表示对 第1 个参数进行求导 (索引从0 开始，这里的第一个参数是 W)

    lss = float(lss)  # lss 是 0 维数组，不能用下标去索引

    W = W - alpha * grads[0]


    if lss < 0.001: 

        A = np.dot(X, W)  # 前向传播
        H = sigmoid(A)    # 预测结果
        E = H - Y         # 误差值

        print(f"loss is: {lss}, curr iter num: {k}")
        print(H) 
        
        break

    if k % 100 == 0:
        print(f"loss is: {lss}, curr iter num: {k}")
