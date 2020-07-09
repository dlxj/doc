# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:46:54 2019

@author: zhangjuefei
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tensorflow.examples.tutorials.mnist import input_data

from node import *
from optimizer import *

mnist = input_data.read_data_sets("E:/train_pic/mnist_dataset/", one_hot=True)
train_x = mnist.train.images
train_y = mnist.train.labels

test_x = mnist.test.images
test_y = mnist.test.labels

hidden_layer_neuro = 90
output_layer_neuro = 10

# 构造多分类逻辑回归计算图，输入变量
X = Variable(784, trainable=False)

# 隐藏层神经元
layer = []
for i in range(hidden_layer_neuro):
    layer.append(Add(Dot(Variable(784, True), X), Variable(1, True)))

# 隐藏层的输出
hidden_output = ReLU(Vectorize(*layer))

# 输出层神经元
layer = []
for i in range(output_layer_neuro):
    layer.append(Add(Dot(Variable(hidden_layer_neuro, True), hidden_output), Variable(1, True)))

# 输出层仿射值施加SoftMax后的概率值
o = Vectorize(*layer)
prob = SoftMax(o)

# 训练标签
label = Variable(output_layer_neuro, trainable=False)

# 交叉熵损失
loss = CrossEntropyWithSoftMax(o, label)

# Adam优化器
optimizer = Adam(default_graph, loss, 0.01, batch_size=32)

# 训练
for e in range(6):

    # 每个epoch在测试集上评估模型正确率
    probs = []
    losses = []
    for i in range(len(test_x)):
        X.set_value(np.mat(test_x[i, :]).T)
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

    print("Epoch: {:d}，测试集损失值：{:.3f}，测试集正确率：{:.2f}%".format(e + 1, np.mean(losses), accuracy * 100))

    for i in range(len(train_x)):
        X.set_value(np.mat(train_x[i, :]).T)
        label.set_value(np.mat(train_y[i, :]).T)

        # 执行一步优化
        optimizer.one_step()

        # 计算Mini Batch上的损失
        if i % 100 == 0:
            loss.forward()
            print("Iteration: {:d}, Mini Batch损失值：{:.3f}".format(i + 1, loss.value[0, 0]))

# 训练结束后打印最终评价
print("验证集正确率：{:.3f}".format(accuracy_score(truth, pred)))
print(classification_report(truth, pred))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
_ = sns.heatmap(
    confusion_matrix(truth, pred),
    square=True,
    xticklabels=np.arange(10),
    annot=True,
    annot_kws={"fontsize": 8},
    yticklabels=np.arange(10),
    cbar=False,
    cmap=sns.light_palette("#00304e", as_cmap=True),
    ax=ax
)
plt.savefig("Confusion_Matrix.png")
