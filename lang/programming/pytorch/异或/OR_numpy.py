import numpy as np
import itertools

"""
doc\lang\programming\algo\梯度下降公式详细推导.md

与门的脑补参数实现
    《深度学习入门：基于Python的理论与实现》 p.28
"""
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 仅权重和偏置与AND不同！
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

"""
与门单层神经网络实现
    神经网络实现的是向量x 到向量 h的仿射变换
    仿射变换相比线性变换多了一个平移，原点变了  
    线性变换保证几何体的形状和比例不变  
    平移是通过加上一个常量既偏置完成的

输入信号矩阵左乘权重矩阵，求出输入信号的加权和，激活函数把若干个加权和压缩到0 和1 之间，这就是隐层的单元
    隐层单元又作为输入信号开始新一轮的计算，最后在输出层得到前向传播的最终结果，这就是预测值
        利用梯度下降或反向传播算法不断的更新权重，从而减小预测值和期望值之间的误差
        当误差小到一定范围时神经网络就训练好了

矩阵中的元素
    上标是行，下标是列

维度
    行向量是多维空间的一个点由不同维度的坐标组成的向量
    列向量是多维空间的多个点的同一维度的坐标组成的向量

网络结构
    输入层2 结点，没有隐层，输出层1 结点

输入矩阵
    X 维度是 4*3 （四组输入，每一组是 1*3）
    输入矩阵要左乘权重矩阵，既X点乘W： X.W
        W 右乘X，X 的列降维到和W 一至，降维的方法是矩阵所有的列加权求和
            左乘是行变换，右乘是列变换
            列向量右乘一个矩阵，左边的矩阵行数没变列数被降维了（被降到和列向量对齐）

权重矩阵
    第一层3 输入对应1 输出，共有三条边，所以需要3 权重
    W 维度是 3*1

输出矩阵
    Y 4*1（四组输入，对应四个输出，四个标量组成的列向量）

梯度下降过程向量化 - Logistic回归总结 洞庭之子
    https://www.cnblogs.com/earendil/p/8268757.html
    doc\lang\programming\梯度下降过程向量化
"""

import numpy as np

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
             ], np.float)

# 输入矩阵，维度4*3。注意偏置作为列向量添加进来了

Y = np.array([
                [0],
                [1],
                [1],
                [1]
             ], np.float)
# 4*1 输出

W = np.random.uniform(size=(3, 1))   # 3*1 权重
#W = W * 0.1 # 据说对于sigmoid 激活函数，更小的权重更容易收敛
"""
观察输入输出的维度，可以看出需要对X 的列进行压缩，既把列从维度3 降维到1
    右乘是列变换，应该让权重矩阵W 右乘X，既 X.W
    矩阵点乘的维度变化
        (4*3).(3*1) = 4*1
"""

for k in range(maxIter): 

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