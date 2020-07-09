from node import *


def factorization_machine(n, classes=2, latent_dim=6):
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

    # 将多个 logit 组装成 logits 向量
    logits = Vectorize(*logits)

    # 返回输入和logits
    return x, x_2, logits
