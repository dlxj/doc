import pandas as pd
import numpy as np
from mlp import NeuralNetwork
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from tensorflow.examples.tutorials.mnist import input_data
import seaborn as sns
import matplotlib.pyplot as plt


mnist = input_data.read_data_sets("E:/train_pic/mnist_dataset/", one_hot=True)
train_x = mnist.train.images
train_y = mnist.train.labels

test_x = mnist.test.images
test_y = mnist.test.labels

# 构造 2 隐藏层，每个隐藏层包含 40 个神经元的全连接神经网络，隐藏层的激活函数为 ReLU
lr = NeuralNetwork([40, 40, 10], ["relu", "relu", "identity"],
                   learning_rate = 0.001, iterations = 8000, beta_1=0.9, beta_2=0.99, minibatch_size = 2000)

# 在训练集上训练网络
lr.train(train_x, train_y)

# 预测测试集样本的分类概率
p = lr.predict(test_x) # 模型对 6 个类别预测的概率

# 取概率最大的类别为预测类别
pred = np.argmax(p, axis=1)
truth = np.argmax(test_y, axis=1)
accuracy = accuracy_score(truth, pred)

print("正确率：{:.2f}%".format(accuracy * 100))
print(classification_report(truth, pred))
print()

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
