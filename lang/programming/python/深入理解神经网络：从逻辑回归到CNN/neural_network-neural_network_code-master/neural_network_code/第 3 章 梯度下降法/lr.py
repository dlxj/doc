from optimizer import *
import numpy as np


class LogisticRegression:

    def __init__(self, optimizer, iterations = 100000):
        
        assert(optimizer is not None)
        
        self.optimizer = optimizer
        self.iterations = iterations # 迭代次数

    def train(self, x, y):
        """
        x为矩阵，形状是n_samples * n_features ，每一行为一个样本
        y为矩阵，形状是n_samples * 1，元素为样本的标签，正类为1， 负类为0
        """
        
        # 在x最前面添加一列常数1，作为偏置值的输入，以简化公式
        x = np.mat(np.c_[[1.0] * x.shape[0], x])
        
        # 根据x的列数（特征数）随机初始化权值，此时偏置值纳入了权值向量，相当于第一个权值
        # 权值向量为n_features + 1维向量，每个分量以0均值、0.01标准差的正态分布初始化
        self.weights = np.mat(np.random.normal(0, 0.01, size=x.shape[1])).T

        for i in range(self.iterations):

            # 计算当前模型对训练集样本的输出
            p = self.predict(x, False)

            gradient = -x.T * (y - p) / x.shape[0] # 交叉熵损失对模型参数的梯度
            self.weights += self.optimizer.delta(gradient) # 更新模型参数
           
            # 评估当前模型并打印训练信息
            if i % 100 == 0:
                # 交叉熵损失
                cross_entropy = (-y.T * np.log(p) - (1.0 - y).T * np.log(1 - p)) / y.shape[0]
                
                # 正确率
                accuracy = np.sum(((p > 0.5).astype(np.int) == y).
                                  astype(np.int)) / y.shape[0]
                
                print("迭代: {:d}，交叉熵: {:.6f}，正确率：{:.2f}%".format(
                        i + 1, cross_entropy[0, 0], accuracy * 100))


    def predict(self, x, augment = True):
        """
        预测函数。x为矩阵，形状是n_samples * n_features，每一行为一个样本
        augment参数指示是否要在特征矩阵前添加一列常量1
        """
        # 在x最前面添加一列常数1，作为偏置值的输入
        if augment:
            x = np.mat(np.c_[[1.0] * x.shape[0], x])

        a = -np.matmul(x, self.weights)
        a[a > 1e2] = 1e2  # 防止数值过大
        p = 1.0 / (1.0 + np.power(np.e, a))
        
        # 剪裁概率值，保证其为合法的概率值
        p[p >= 1.0] = 1.0 - 1e-10
        p[p <= 0.0] = 1e-10
        
        return p
