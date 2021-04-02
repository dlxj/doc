
#导入包
import numpy as np
import pandas as pd
import os

#导入数据
train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

train_row = train.shape[0]  # 训练数据 1460 行
test_row = test.shape[0]    # 测试数据 1459 行

print(train.info)

print('hi,,,')



