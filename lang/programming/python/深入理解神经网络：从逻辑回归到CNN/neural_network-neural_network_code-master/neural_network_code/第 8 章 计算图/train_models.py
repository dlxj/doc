import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import sys

from optimizer import *
from util import get_data, construct_pow2
from graph import default_graph
from node import *

algo = sys.argv[1]
print("model: {:s}".format(algo))
n = 5  # 特征数
classes = 2
epoches = 20

# 构造训练数据
train_x, train_y, test_x, test_y = get_data(number_of_classes=classes, number_of_features=n)

if algo == "lr":
    from lr import logistic_regression

    X, logit = logistic_regression(n)

    X_2 = None  # 简单逻辑回归模型没有二次特征

    # 由于我们只有 SoftMax 节点（包括后续损失的那个），对于二分类问题，我们也得要求
    # 模型的输出是 2 分类概率，所以我们构造一个常量 0 ，当作第 2 个 logit ，LR 模
    # 型输出的值作为第一个 logit ，构造 2 维 logit 向量。
    c = Variable(1, init=False, trainable=False)
    c.set_value(np.mat([[0]]))
    logits = Vectorize(logit, c)

elif algo == "neural network":
    from nn import neural_network
    X, logits = neural_network(n, classes, (6, 6), "ReLU")
    X_2 = None  # 多层全连接神经网络不用二次特征

elif algo == "wide & deep":
    from wide_and_deep import wide_and_deep
    X, X_2, logits = wide_and_deep(n, classes)

elif algo == "fm":
    from fm import factorization_machine
    X, X_2, logits = factorization_machine(n, classes)

elif algo == "ffm":
    from ffm import field_aware_factorization_machine
    fields = [(0, 1, 3), (2, 4)]
    X, X_2, logits = field_aware_factorization_machine(n, fields, classes, latent_dim=6)

elif algo == "deepfm":
    from deepfm import deepfm
    X, X_2, logits = deepfm(n, classes, latent_dim=6)

# 绘制计算图（不包括损失）
default_graph.draw()

# 对模型输出的 logits 施加 SoftMax 得到多分类概率
prob = SoftMax(logits)

# 训练标签
label = Variable(classes, trainable=False)

# 交叉熵损失
loss = CrossEntropyWithSoftMax(logits, label)  # 注意第一个父节点是 logits

# Adam 优化器
optimizer = Adam(default_graph, loss, 0.02, batch_size=32)

# 训练
for e in range(epoches):

    # 每个 epoch 开始时在测试集上评估模型正确率
    probs = []
    losses = []
    for i in range(len(test_x)):
        X.set_value(np.mat(test_x[i, :]).T)

        if X_2 is not None:
            X_2.set_value(construct_pow2(np.mat(test_x[i, :]).T))

        label.set_value(np.mat(test_y[i, :]).T)

        # 前向传播计算概率
        prob.forward()
        probs.append(prob.value.A1)

        # 计算损失值
        loss.forward()
        losses.append(loss.value[0, 0])

    # 取概率最大的类别为预测类别
    pred = np.argmax(np.array(probs), axis=1)
    truth = np.argmax(test_y, axis=1)
    accuracy = accuracy_score(truth, pred)

    print("Epoch: {:d}，损失值：{:.3f}，正确率：{:.2f}%".format(e + 1, np.mean(losses), accuracy * 100))

    for i in range(len(train_x)):
        X.set_value(np.mat(train_x[i, :]).T)

        if X_2 is not None:
            X_2.set_value(construct_pow2(np.mat(train_x[i, :]).T))

        label.set_value(np.mat(train_y[i, :]).T)

        # 执行一步优化
        optimizer.one_step()

        # print("Epoch: {:d}，Iteration：{:d}".format(e + 1, i + 1))

# 训练结束后打印最终评价
print("\n测试集最终正确率：{:.3f}".format(accuracy_score(truth, pred)))
print(classification_report(truth, pred))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
_ = sns.heatmap(
    confusion_matrix(truth, pred),
    square=True,
    annot=True,
    annot_kws={"fontsize": 8},
    cbar=False,
    cmap=sns.light_palette("#00304e", as_cmap=True),
    ax=ax
)
