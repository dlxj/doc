
"""
EAP（expected a posteriori）期望后验参数估计算法中的高斯-埃尔米特(Gauss-Hermite) 积分数值计算方法研究
    用于实时估计考生能力，　
    应用场景在于考生在线实时答题过程中快速实时调整对该考生的能力估计，
    要求计算要快，消耗资源要少
    EAP（expected a posteriori）算法是唯一不需要迭代的算法，所以它的计算速度是最快的，常用于在线测验的参数估计，其理论依据是贝叶斯法则。


あき時間 vacant hours 空闲时间 あき〔明き〕

双参数二级计分模型进行参数估计：https://zhuanlan.zhihu.com/p/29887184
注意这公式和书上的有点不同
# https://github.com/17zuoye/pyirt/blob/master/pyirt/util/tools.py 
# 另一个参考项目，基于论文的实现 IRT Parameter Estimation using the EM Algorithm By Brad Hanson 2000


高斯求积简介 https://discourse.juliacn.com/t/topic/1024

高斯厄米特积分点的数量，影响积分计算的精度
    肯定是越大越好，但也没太多必要，6个积分点就够了

参见:Gauss–Hermite积分 in 深入理解神经网络：从逻辑回归到CNN.md

"""

import numpy as np

def Z(slop, threshold, theta):
    # z函数
    _z = slop * theta + threshold
    _z[_z > 35] = 35
    _z[_z < -35] = -35
    return _z

def P(z):
    # 回答正确的概率函数
    e = np.exp(z)
    p = e / (1.0 + e)
    return p

def get_gh_point(gp_size):
    x_nodes, x_weights = np.polynomial.hermite.hermgauss(gp_size)  # Gauss–Hermite积分点数
    x_nodes = x_nodes * 2 ** 0.5
    x_nodes.shape = x_nodes.shape[0], 1
    x_weights = x_weights / np.pi ** 0.5
    x_weights.shape = x_weights.shape[0], 1
    return x_nodes, x_weights


"""
阀值 = -1 * ( 难度 * 区分度 )
难度 = -1 * ( 阀值 / 区分度 )
"""
if __name__ == "__main__":

    """
    一个人的真实能力是1，他答了3 道题，使用EAP 算法估计他的能力
    """
    num = 5 # 题数
    slop = np.random.uniform(1, 3, num)            # 1000 道题的区分度  # 均匀分布
    threshold = np.random.normal(0, 1, size=num)   # 1000 个阀值        # 正态分存
    z = Z(slop, threshold, 1) # 区分度，阀值，能力
    p = P(z)
    score = np.random.binomial(1, p, num)

    """
    先求21 个积分点
    """
    x_nodes, x_weights = np.polynomial.hermite.hermgauss(21)  # Gauss–Hermite积分点数
    x_nodes = x_nodes * 2 ** 0.5
    x_nodes.shape = x_nodes.shape[0], 1
    x_weights = x_weights / np.pi ** 0.5
    x_weights.shape = x_weights.shape[0], 1

    z = Z(slop, threshold, x_nodes)  # x_nodes是21 个theta 采样值
    p = P(z)                         # (21 * 5) 的正确率
    tmp1 = p**score # p 被按列乘方，p 的列数要等于score 的列数
    tmp2 = (1.0 - p)**(1-score)

    lik_values = np.prod(tmp1*tmp2, axis=1)

    # lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1)
    """
    计算所有元素的乘积，按行连乘(维度变成n*1)。
    如果不指定轴，则不管是几维都展平成一维然后连乘
    """

    x = x_nodes[:, 0]
    weight = x_weights[:, 0]
    g = np.sum(x * weight * lik_values)


    weight = x_weights[:, 0]
    h = np.sum(weight * lik_values)

    """
    估计的能力值
    """
    theta = round(g / h, 3)
    print(theta)


"""
SELECT t.Alpha, t.Beta FROM testirt t ORDER BY RAND() LIMIT 1000;
"""





