
import numpy as np
import itertools


# 此激活函数设计为可以接受列向量
# 返回结果也是列向量
# np.exp 的实现可以接受向量作为参数，所以代码很简洁
def sigmoid (x):
    return 1/(1 + np.exp(-x))




if __name__ == "__main__":
    """
    异或问题，双隐层神经网络算法
    """
    m = 4 # 样本数
    n = 2 # 每个样本的维度

    alpha = 0.5 # 学习率
    maxIter = 50000 # 最大迭代次数

    x_0 = np.array([
                [0, 0, 1, 1],
                [0, 1, 0, 1]
            ], np.float)
    # (2 * 4) 输入

    Y = np.array([
                [0, 1, 1, 0]
            ], np.float)
    # (1 * 4) 输出

    W_1 = np.random.uniform(size=(2, 2))   # 隐层一权重
    # (2 * 2) (2 * 4) -> (2 * 4)

    b_1 = np.random.uniform(size=(2, 4))   # 隐层一偏置


    W_2 = np.random.uniform(size=(1, 2))   # 隐层二权重
    # (1 * 2) (2 * 4) -> (1 * 4)

    b_2 = np.random.uniform(size=(1, 4))   # 隐层二偏置

    for k in range(50000):
        """
        前向传播
        """
        a_1 = np.dot(W_1, x_0) + b_1
        x_1 = sigmoid(a_1)          
        
        a_2 = np.dot(W_2, x_1) + b_2
        h_2 = sigmoid(a_2)                  # 预测结果

        E = h_2 - Y                         # 误差值

        # H = sigmoid(A)    # 预测结果
        # E = H - Y         # 误差值

    



