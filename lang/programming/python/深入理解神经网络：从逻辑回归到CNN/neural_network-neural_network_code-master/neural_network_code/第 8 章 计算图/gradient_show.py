import matplotlib.pyplot as plt
from matplotlib import animation
from sklearn.metrics import accuracy_score

from nn import neural_network
from optimizer import *
from util import get_data, construct_pow2

n = 5  # 特征数
classes = 2
epoches = 3

# 构造训练数据
train_x, train_y, test_x, test_y = get_data(number_of_classes=classes, number_of_features=n)

# 算法
algo = "fm"

# 构造神经网络计算图
if algo == "neural network":
    X, logits = neural_network(n, classes, (6, 6, 6, 6), "ReLU")
    X_2 = None  # 多层全连接神经网络不用二次特征

elif algo == "fm":
    from fm import factorization_machine

    X, X_2, logits = factorization_machine(n, classes)

# 绘制计算图（不包括损失）
# default_graph.draw()
fig = plt.figure(figsize=(11, 6))
ax = fig.add_subplot(1, 1, 1)

# 对模型输出的 logits 施加 SoftMax 得到多分类概率
prob = SoftMax(logits)

# 训练标签
label = Variable(classes, trainable=False)

# 交叉熵损失
loss = CrossEntropyWithSoftMax(logits, label)  # 注意第一个父节点是 logits

# Adam 优化器
optimizer = Adam(default_graph, loss, 0.02, batch_size=32)


# 动画初始化函数
def init():
    global ax
    default_graph.draw(ax)


# 动画更新函数
c = 0
e = 0
val_acc = 0


def update(idx):
    global c, e, loss, ax, val_acc
    X.set_value(np.mat(train_x[c, :]).T)
    if X_2 is not None:
        X_2.set_value(construct_pow2(np.mat(test_x[c, :]).T))
    label.set_value(np.mat(train_y[c, :]).T)

    # 执行一步优化
    optimizer.one_step()

    # 训练样本上的 loss
    if loss.value is None:
        loss.forward()
    train_loss = loss.value[0, 0]

    probs = []
    for i in range(len(test_x)):
        X.set_value(np.mat(test_x[i, :]).T)
        if X_2 is not None:
            X_2.set_value(construct_pow2(np.mat(test_x[i, :]).T))
        label.set_value(np.mat(test_y[i, :]).T)

        # 前向传播计算概率
        prob.forward()
        probs.append(prob.value.A1)

    # 取概率最大的类别为预测类别
    pred = np.argmax(np.array(probs), axis=1)
    truth = np.argmax(test_y, axis=1)
    val_acc = accuracy_score(truth, pred)

    default_graph.draw(ax)

    msg = "epoches:{:d}, iteration:{:d}, loss:{:.8f}, validation accuracy:{:.3f}%".format(e + 1, c + 1, train_loss,
                                                                                          val_acc * 100)
    ax.set_title(msg)
    print(msg)

    c = (c + 1) % len(train_x)
    if c % len(train_x) == 0:
        e += 1


anim = animation.FuncAnimation(fig, update, init_func=init, frames=epoches * len(train_x), interval=50, blit=False)
anim.save('gradient_show.mp4')
# plt.show()
