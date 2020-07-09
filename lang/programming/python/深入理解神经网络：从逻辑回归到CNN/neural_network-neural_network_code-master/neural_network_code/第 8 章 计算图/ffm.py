from node import *


def field_aware_factorization_machine(n, fields, classes=2, latent_dim=6):
    """
    构造一个FFM模型的计算图，特征数量为 n 。 n 个特征能产生
    C(n, 2) 个二次交互项 xi * xj 。fields 说明特征如何归入 field
    """
    assert n == sum([len(f) for f in fields])

    # x 是一个 n 维向量变量，不初始化，不参与训练
    x = Variable(n, init=False, trainable=False)

    # 二次特征，共C(n, 2)=n * (n-1) / 2个
    assert n > 1
    power2_n = int(n * (n - 1) / 2)
    x_2 = Variable(power2_n, init=False, trainable=False)

    # 域数量
    number_of_fields = len(fields)
    assert number_of_fields >= 1

    # 有多少类别，就有多少 logit
    logits = []
    for c in range(classes):

        # 一次部分，简单的将特征加权相加（求输入向量与权值向量的内积）
        order_1 = Dot(Variable(n, True, trainable=False), x)

        # 二次隐藏向量部分，首先为每个特征对每个 field 构造一个隐藏向量， latent_vectors 的
        # 第 i,k 元素是第 i 个特征对第 k 个 field 的隐藏向量
        latent_vectors = np.array([None] * n * number_of_fields).reshape(n, number_of_fields)
        for i in range(n):
            for j in range(len(fields)):
                latent_vectors[i, j] = Variable(latent_dim, True, trainable=True)

        # 每个二次交互项的权重是两个原始特征的隐藏向量的内积
        latent_weights = []
        for i in range(n):
            for j in range(i):

                # 寻找第 i 特征和第 j 特征所在的 field
                left_field = right_field = None
                for f in fields:
                    if i in f:
                        left_field = fields.index(f)
                    if j in f:
                        right_field = fields.index(f)

                latent_weights.append(Dot(latent_vectors[i, right_field], latent_vectors[j, left_field]))

        # 全部二次交互项的加权和
        order_2 = Dot(Vectorize(*latent_weights), x_2)

        # 偏置
        bias = Variable(1, True, trainable=False)

        # 将一次部分、二次部分和偏置相加
        logits.append(Add(Add(order_1, order_2), bias))

    # 将多个 logit 组装成 logits 向量
    logits = Vectorize(*logits)

    # 返回输入和logits
    return x, x_2, logits
