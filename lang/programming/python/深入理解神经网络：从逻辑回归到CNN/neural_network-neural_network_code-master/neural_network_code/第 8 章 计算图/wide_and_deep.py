from node import *


def wide_and_deep(n, classes=2, hiddens=(12,)):
    """
    构造一个Wide & Deep模型的计算图，特征数量为 n 。 n 个特征能产生
    C(n, 2) 个二次交互项 xi * xj 。
    """

    # x 是一个 n 维向量变量，不初始化，不参与训练
    x = Variable(n, init=False, trainable=False)

    # 二次特征，共C(n, 2)=n * (n-1) / 2个
    assert n > 1
    power2_n = int(n * (n - 1) / 2)
    x_2 = Variable(power2_n, init=False, trainable=False)

    # Wide部分
    wide = []
    for i in range(classes):
        wide.append(Add(Dot(Variable(power2_n, True), x_2), Variable(1, True)))
    wide = Vectorize(*wide)

    # Deep部分
    output_size = n
    output = x
    for h_size in hiddens:
        hidden = []
        for i in range(h_size):
            hidden.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))

        # 隐藏层的输出
        output = ReLU(Vectorize(*hidden))
        output_size = h_size

    # 输出层的神经元
    deep = []
    for i in range(classes):
        deep.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))
    deep = Vectorize(*deep)

    # 将Wide部分和Deep部分的输出相加，得到logits
    logits = Add(wide, deep)

    # 返回输入和logits
    return x, x_2, logits
