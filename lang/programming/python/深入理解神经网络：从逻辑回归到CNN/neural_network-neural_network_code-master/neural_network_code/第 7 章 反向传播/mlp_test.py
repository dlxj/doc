import pandas as pd
import numpy as np
from mlp import NeuralNetwork
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler


bird = pd.read_csv("bird.csv").dropna().drop("id", axis=1)

# 先将6个类别的字符串名称编码成整数编号，再转化成6个1/0值的one hot编码
label_encoder = LabelEncoder()
one_hot_label = OneHotEncoder(sparse=False).fit_transform(label_encoder.fit_transform(bird.type).reshape(-1, 1))

# 去掉类别的字符串名称列
bird.drop("type", axis=1, inplace=True)

# 将10个数值型特征列与6个类别标签one hot编码列合并起来
data = np.c_[bird.values, one_hot_label]

# 将样本随机洗牌
np.random.shuffle(data)

# 前300个样本作为训练集，将特征与one hot编码分开
ss = StandardScaler()
train_x = ss.fit_transform(np.mat(data[:300,:-6]))
train_y = np.mat(data[:300,-6:])

# 其余样本作为测试集，将特征与one hot编码分开
test_x = ss.transform(np.mat(data[300:,:-6]))
test_y = np.mat(data[300:,-6:])

# 构造2隐藏层，每个隐藏层包含20个神经元的全连接神经网络，隐藏层的激活函数为ReLU
lr = NeuralNetwork([20, 20, 6], ["relu", "relu", "identity"])

# 在训练集上训练网络
lr.train(train_x, train_y)

# 预测测试集样本的分类概率
p = lr.predict(test_x) # 模型对6个类别预测的概率

# 取概率最大的类别为预测类别
pred = [label_encoder.classes_[idx] for idx in np.argmax(p, axis=1)]
truth = [label_encoder.classes_[idx] for idx in np.argmax(test_y, axis=1).A1]
accuracy = accuracy_score(truth, pred)

print("正确率：{:.2f}%".format(accuracy * 100))
print(classification_report(truth, pred))
