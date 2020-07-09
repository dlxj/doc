# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:46:54 2019

@author: zhangjuefei
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

from node import *
from optimizer import *

# 构造二次项
def construct_pow2(x):
    m = x*x.T
    x_2 = []
    for i in range(len(x)):
        for j in range(i):
            x_2.append(m[i, j])

    return np.mat(x_2).T

bird = pd.read_csv("bird.csv").dropna().drop("id", axis=1)

# 先将6个类别的字符串名称编码成整数编号，再转化成6个1/0值的one hot编码
label_encoder = LabelEncoder()
one_hot_label = OneHotEncoder(sparse=False, categories="auto").fit_transform(
    label_encoder.fit_transform(bird.type).reshape(-1, 1))

# 去掉类别的字符串名称列
bird.drop("type", axis=1, inplace=True)

# 将10个数值型特征列与6个类别标签one hot编码列合并起来
data = np.c_[bird.values, one_hot_label]

# 将样本随机洗牌
np.random.shuffle(data)

# 前300个样本作为训练集，将特征与one hot编码分开
ss = StandardScaler()
train_x = ss.fit_transform(np.mat(data[:300, :-6]))
train_y = np.mat(data[:300, -6:])

# 其余样本作为测试集，将特征与one hot编码分开
test_x = ss.transform(np.mat(data[300:, :-6]))
test_y = np.mat(data[300:, -6:])

# 输入向量：一次特征
X = Variable(10, trainable=False)  # 10维特征变量

# 输入向量：二次特征，共C(10,2)=45个
X_2 = Variable(45, trainable=False)

# Wide部分
wide = []
for i in range(6):
    wide.append(Add(Dot(Variable(45, True), X_2), Variable(1, True)))
wide = Vectorize(*wide)

# Deep部分
hidden1_size = 12
hidden2_size = 12

# 第1隐藏层的神经元
hidden1 = []
for i in range(hidden1_size):
    hidden1.append(Add(Dot(Variable(10, True), X), Variable(1, True)))

# 第1隐藏层的输出
hidden1 = ReLU(Vectorize(*hidden1))

# 第2隐藏层的神经元
hidden2 = []
for i in range(hidden2_size):
    hidden2.append(Add(Dot(Variable(hidden1_size, True), hidden1), Variable(1, True)))

# 第2隐藏层的输出
hidden2 = ReLU(Vectorize(*hidden2))

# 输出层的6个神经元
deep = []
for i in range(6):
    deep.append(Add(Dot(Variable(hidden2_size, True), hidden2), Variable(1, True)))
deep = Vectorize(*deep)

# 输出层的仿射值以及施加SoftMax后的概率值
logits = Add(wide, deep)
prob = SoftMax(logits)

# 训练标签
label = Variable(6, trainable=False)

# 交叉熵损失
loss = CrossEntropyWithSoftMax(logits, label)  # 注意第一个父节点是输出层的仿射值

# Adam优化器
optimizer = Adam(default_graph, loss, 0.01, batch_size=32)

# 训练
for e in range(300):

    # 每个epoch开始时在测试集上评估模型正确率
    probs = []
    losses = []
    for i in range(len(test_x)):
        x = np.mat(test_x[i, :]).T
        x_2 = construct_pow2(x)
        X.set_value(x)
        X_2.set_value(x_2)
        label.set_value(np.mat(test_y[i, :]).T)

        # 前向传播计算概率
        prob.forward()
        probs.append(prob.value.A1)

        # 计算损失值
        loss.forward()
        losses.append(loss.value[0, 0])

    # 取概率最大的类别为预测类别
    pred = [label_encoder.classes_[idx] for idx in np.argmax(np.array(probs), axis=1)]
    truth = [label_encoder.classes_[idx] for idx in np.argmax(test_y, axis=1).A1]
    accuracy = accuracy_score(truth, pred)

    print("Epoch: {:d}，损失值：{:.3f}，正确率：{:.2f}%".format(e + 1, np.mean(losses), accuracy * 100))

    for i in range(len(train_x)):
        x = np.mat(train_x[i, :]).T
        x_2 = construct_pow2(x)
        X.set_value(x)
        X_2.set_value(x_2)
        label.set_value(np.mat(train_y[i, :]).T)

        # 执行一步优化
        optimizer.one_step()

# 训练结束后打印最终评价
print("测试集正确率：{:.3f}".format(accuracy_score(truth, pred)))
print(classification_report(truth, pred))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
_ = sns.heatmap(
    confusion_matrix(truth, pred),
    square=True,
    xticklabels=label_encoder.classes_,
    annot=True,
    annot_kws={"fontsize": 8},
    yticklabels=label_encoder.classes_,
    cbar=False,
    cmap=sns.light_palette("#00304e", as_cmap=True),
    ax=ax
)

plt.savefig("Confusion_Matrix.png")
