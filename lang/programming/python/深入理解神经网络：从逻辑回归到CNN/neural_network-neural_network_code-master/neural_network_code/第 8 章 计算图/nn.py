from node import *


def neural_network(n, classes=2, hiddens=(12,), activation="ReLU"):
    """
    构造一个多层全连接神经网络的计算图。
    """

    # x 是一个 n 维向量变量，不初始化，不参与训练
    x = Variable(n, init=False, trainable=False)

    # 构造全连接层
    output_size = n
    output = x
    for l, h_size in zip(np.arange(len(hiddens)), hiddens):

        hidden = []
        for i in range(h_size):
            hidden.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))

        hidden = Vectorize(*hidden)
        # 隐藏层的输出
        if activation == "ReLU":
            output = ReLU(hidden)
        elif activation == "Logistic":
            output = Logistic(hidden)
        else:
            output = hidden

        output_size = h_size

    # 输出层的神经元
    logits = []
    for i in range(classes):
        logits.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))

    logits = Vectorize(*logits)

    # 返回输入和 logits
    return x, logits
