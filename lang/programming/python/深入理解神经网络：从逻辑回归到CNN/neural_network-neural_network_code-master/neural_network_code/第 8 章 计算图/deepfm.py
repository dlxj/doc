from node import *


def deepfm(n, classes=2, hiddens=(12,), latent_dim=6):
    """
    构造一个FM模型的计算图，特征数量为 n 。 n 个特征能产生
    C(n, 2) 个二次交互项 xi * xj 。
    """

    # x 是一个 n 维向量变量，不初始化，不参与训练
    x = Variable(n, init=False, trainable=False)

    # 二次特征，共C(n, 2)=n * (n-1) / 2个
    assert n > 1
    power2_n = int(n * (n - 1) / 2)
    x_2 = Variable(power2_n, init=False, trainable=False)

    # 有多少类别，就有多少 logit
    logits = []
    for c in range(classes):

        # FM 部分
        # 一次部分，简单的将特征加权相加（求输入向量与权值向量的内积）
        order_1 = Dot(Variable(n, True), x)

        # 二次隐藏向量部分，首先为每个特征构造一个隐藏向量
        latent_vectors = []
        for i in range(n):
            latent_vectors.append(Variable(latent_dim, True))

        # 每个二次交互项的权重是两个原始特征的隐藏向量的内积
        latent_weights = []
        for i in range(n):
            for j in range(i):
                latent_weights.append(Dot(latent_vectors[i], latent_vectors[j]))

        # 全部二次交互项的加权和
        order_2 = Dot(Vectorize(*latent_weights), x_2)

        # 偏置
        bias = Variable(1, True)

        # 将一次部分、二次部分和偏置相加
        logits.append(Add(Add(order_1, order_2), bias))

    # 将多个 logit 组装成 wide 向量
    wide = Vectorize(*logits)

    # Deep 部分，以所有隐藏向量为输入的层，神经元个数为 hiddens[0]
    l = []
    for n in range(hiddens[0]):
        temp = []
        for v in latent_vectors:
            temp.append(Dot(Variable(latent_dim, True), v))

        w = Variable(len(latent_vectors), False, False)
        w.set_value(np.mat([1.0] * len(latent_vectors)).T)
        l.append(Dot(w, Vectorize(*temp)))

    output_size = hiddens[0]
    output = ReLU(Vectorize(*l))

    # 其余各层
    for h_size in hiddens[1:]:
        hidden = []
        for i in range(h_size):
            hidden.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))

        # 隐藏层的输出
        output = ReLU(Vectorize(*hidden))
        output_size = h_size

    # 输出层，包含 classes 个神经元
    deep = []
    for i in range(classes):
        deep.append(Add(Dot(Variable(output_size, True), output), Variable(1, True)))
    deep = Vectorize(*deep)

    # 将Wide部分和Deep部分的输出相加，得到logits
    logits = Add(wide, deep)

    # 返回输入和logits
    return x, x_2, logits
