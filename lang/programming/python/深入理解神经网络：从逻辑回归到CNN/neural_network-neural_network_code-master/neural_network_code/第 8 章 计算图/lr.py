from node import *


def logistic_regression(n):
    """
    构造一个逻辑回归模型的计算图，特征数量为 n 。
    """

    # x 是一个 n 维向量变量，不初始化，不参与训练
    x = Variable(n, init=False, trainable=False)

    # w 是一个 n 维向量变量，随机初始化，参与训练
    w = Variable(n, init=True, trainable=True)

    # b 是一个 1 维向量（标量）变量，随机初始化，参与训练
    b = Variable(1, init=True, trainable=True)

    # 求 w 和 x 的内积，加上偏置，施加 Logistic 函数
    logit = Add(Dot(w, x), b)

    # 返回输入和未施加 Logistic 的 logit ，至于为什么不施加 Logistic ，看训练代码
    return x, logit
