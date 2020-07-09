import pandas as pd
import numpy as np
from optimizer import *
from lr import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score 

# 读入数据
bird = pd.read_csv("bird.csv").dropna().drop("id", axis=1)

# 根据标签是否属于"SW", "W", "R"三类，构造二分类1/0标签
bird["type"] = bird.type.apply(lambda t: t in ["SW", "W", "R"]).astype(np.int)

data = bird.values
# 将样本随机洗牌
np.random.shuffle(data)

# 前300个样本作为训练集
train_x = np.mat(data[:300,:-1])
train_y = np.mat(data[:300,-1]).T

# 其余样本作为测试集
test_x = np.mat(data[300:,:-1])
test_y = np.mat(data[300:,-1]).T

# 构造逻辑回归对象，优化器为Adam，各超参数取默认值
lr = LogisticRegression(Adam())

# 在训练集上训练
lr.train(train_x, train_y)

# 对测试集进行预测
p = lr.predict(test_x) # 模型预测的正类概率
pred = (p > 0.5).astype(np.int) # 以 0.5 为阈值时，模型预测的类别

print("正确率：{:.2f}%，查准率：{:.2f}%，查全率：{:.2f}%，ROC 曲线下面积:{:.3f}".format(
        accuracy_score(test_y, pred) * 100,
        precision_score(test_y, pred) * 100,
        recall_score(test_y, pred) * 100,
        roc_auc_score(test_y.A, p)))
