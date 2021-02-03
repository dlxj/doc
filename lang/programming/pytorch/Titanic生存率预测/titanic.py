
"""
https://zhuanlan.zhihu.com/p/53176091
"""
#导入包
import numpy as np
import pandas as pd
import os

#导入数据
train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

# 训练数据集大小： (891, 12)
# 测试数据集大小： (418, 11)
print('训练数据大小:',train.shape)
print('测试数据大小:',test.shape)

# 训练数据比预测数据多了一列：即标签"result"
print( train.columns )
print( test.columns )


#训练数据集比测试数据集多一列结果列
#现在将数据集进行合并，方便进行数据清洗和特征提取
full = pd.DataFrame()
full = pd.concat([train,test],ignore_index=True)  # 列数不一至的数据帧合并，缺失列的一方会添加空列(所有数据为空白)
print(full.columns)

full.head()
#查看描述统计和信息
full.describe()
#根据描述统计没有观察到异常值
full.info()
'''
通过info可以看出总共有1309条数据，其中Age，Cabin，Embarked，Fare，Survived均有不同程度的数据缺失，包含数值型数据（Age，Fare和Survived）
和字符型数值（Cabin和Embarked），这就需要我们根据不同的数据类型进行相应的数据预处理。
'''


currDir = os.path.dirname(os.path.abspath(__file__))
fname_full = os.path.join(currDir, 'full.csv')
full.to_csv(fname_full, index=False ,encoding="utf-8")


"""
数据清洗（Data Preparaion） 这一步我们主要对缺失数据进行补充，并对数据进行特征工程
"""


