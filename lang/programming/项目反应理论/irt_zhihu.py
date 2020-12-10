

from __future__ import print_function, division
import numpy as np
import warnings

"""
双参数二级计分模型进行参数估计：https://zhuanlan.zhihu.com/p/29887184
注意这公式和书上的有点不同
# https://github.com/17zuoye/pyirt/blob/master/pyirt/util/tools.py 
# 另一个参考项目，基于论文的实现 IRT Parameter Estimation using the EM Algorithm By Brad Hanson 2000
"""

class BaseIrt(object):

    def __init__(self, scores=None):
        self.scores = scores

    @staticmethod
    def p(z):
        # 回答正确的概率函数
        e = np.exp(z)
        p = e / (1.0 + e)
        return p

class Irt2PL(BaseIrt):

    @staticmethod
    def z(slop, threshold, theta):
        # z函数
        _z = slop * theta + threshold
        _z[_z > 35] = 35
        _z[_z < -35] = -35
        return _z

   # EM算法求解
    def __init__(self, init_slop=None, init_threshold=None, max_iter=10000, tol=1e-5, gp_size=11,
                 m_step_method='newton', *args, **kwargs):
        """
        :param init_slop: 斜率初值
        :param init_threshold: 阈值初值
        :param max_iter: EM算法最大迭代次数
        :param tol: 精度
        :param gp_size: Gauss–Hermite积分点数
        """
        super(Irt2PL, self).__init__(*args, **kwargs)
        # 斜率初值
        if init_slop is not None:
            self._init_slop = init_slop
        else:
            self._init_slop = np.ones(self.scores.shape[1])
        # 阈值初值
        if init_threshold is not None:
            self._init_threshold = init_threshold
        else:
            self._init_threshold = np.zeros(self.scores.shape[1])
        self._max_iter = max_iter
        self._tol = tol
        self._m_step_method = '_{0}'.format(m_step_method)
        self.x_nodes, self.x_weights = self.get_gh_point(gp_size)

    @staticmethod
    def get_gh_point(gp_size):
        x_nodes, x_weights = np.polynomial.hermite.hermgauss(gp_size)
        x_nodes = x_nodes * 2 ** 0.5
        x_nodes.shape = x_nodes.shape[0], 1
        x_weights = x_weights / np.pi ** 0.5
        x_weights.shape = x_weights.shape[0], 1
        return x_nodes, x_weights

    def _lik(self, p_val):
        # 似然函数
        scores = self.scores
        loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                     np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
        return np.exp(loglik_val)

    def _e_step(self, p_val, weights):
        # EM算法E步
        # 计算theta的分布人数
        scores = self.scores
        lik_wt = self._lik(p_val) * weights
        # 归一化
        lik_wt_sum = np.sum(lik_wt, axis=0)
        _temp = lik_wt / lik_wt_sum
        # theta的人数分布
        full_dis = np.sum(_temp, axis=1)
        # theta下回答正确的人数分布
        right_dis = np.dot(_temp, scores)
        full_dis.shape = full_dis.shape[0], 1
        # 对数似然值
        print(np.sum(np.log(lik_wt_sum)))
        return full_dis, right_dis

    def _irls(self, p_val, full_dis, right_dis, slop, threshold, theta):
        # 所有题目误差列表
        e_list = (right_dis - full_dis * p_val) / full_dis * (p_val * (1 - p_val))
        # 所有题目权重列表
        _w_list = full_dis * p_val * (1 - p_val)
        # z函数列表
        z_list = self.z(slop, threshold, theta)
        # 加上了阈值哑变量的数据
        x_list = np.vstack((threshold, slop))
        # 精度
        delta_list = np.zeros((len(slop), 2))
        for i in range(len(slop)):
            e = e_list[:, i]
            _w = _w_list[:, i]
            w = np.diag(_w ** 0.5)
            wa = np.dot(w, np.hstack((np.ones((self.x_nodes.shape[0], 1)), theta)))
            temp1 = np.dot(wa.transpose(), w)
            temp2 = np.linalg.inv(np.dot(wa.transpose(), wa))
            x0_temp = np.dot(np.dot(temp2, temp1), (z_list[:, i] + e))
            delta_list[i] = x_list[:, i] - x0_temp
            slop[i], threshold[i] = x0_temp[1], x0_temp[0]
        return slop, threshold, delta_list


    def _newton(self, p_val, full_dis, right_dis, slop, threshold, theta):
        # 一阶导数
        dp = right_dis - full_dis * p_val
        # 二阶导数
        ddp = full_dis * p_val * (1 - p_val)
        # jac矩阵和hess矩阵
        jac1 = np.sum(dp, axis=0)
        jac2 = np.sum(dp * theta, axis=0)
        hess11 = -1 * np.sum(ddp, axis=0)
        hess12 = hess21 = -1 * np.sum(ddp * theta, axis=0)
        hess22 = -1 * np.sum(ddp * theta ** 2, axis=0)
        delta_list = np.zeros((len(slop), 2))
        # 把求稀疏矩阵的逆转化成求每个题目的小矩阵的逆
        for i in range(len(slop)):
            jac = np.array([jac1[i], jac2[i]])
            hess = np.array(
                [[hess11[i], hess12[i]],
                 [hess21[i], hess22[i]]]
            )
            delta = np.linalg.solve(hess, jac)
            slop[i], threshold[i] = slop[i] - delta[1], threshold[i] - delta[0]
            delta_list[i] = delta
        return slop, threshold, delta_list

    def _est_item_parameter(self, slop, threshold, theta, p_val):
        full_dis, right_dis = self._e_step(p_val, self.x_weights)
        return self._m_step(p_val, full_dis, right_dis, slop, threshold, theta)

    def _m_step(self, p_val, full_dis, right_dis, slop, threshold, theta):
        # EM算法M步
        m_step_method = getattr(self, self._m_step_method)
        return m_step_method(p_val, full_dis, right_dis, slop, threshold, theta)

    def em(self):
        max_iter = self._max_iter
        tol = self._tol
        slop = self._init_slop
        threshold = self._init_threshold
        for i in range(max_iter):
            z = self.z(slop, threshold, self.x_nodes)
            p_val = self.p(z)
            slop, threshold, delta_list = self._est_item_parameter(slop, threshold, self.x_nodes, p_val)
            if np.max(np.abs(delta_list)) < tol:
                print(i)
                return slop, threshold
        warnings.warn("no convergence")
        return slop, threshold

class EAPIrt2PLModel(object):

    def __init__(self, score, slop, threshold, model=Irt2PL):
        self.x_nodes, self.x_weights = model.get_gh_point(21)
        z = model.z(slop, threshold, self.x_nodes)
        p = model.p(z)
        self.lik_values = np.prod(p**score*(1.0 - p)**(1-score), axis=1)

    @property
    def g(self):
        x = self.x_nodes[:, 0]
        weight = self.x_weights[:, 0]
        return np.sum(x * weight * self.lik_values)

    @property
    def h(self):
        weight = self.x_weights[:, 0]
        return np.sum(weight * self.lik_values)

    @property
    def res(self):
        return round(self.g / self.h, 3)


f = 'lsat.csv'
score = np.loadtxt(f, delimiter=",")
res = Irt2PL(scores=score).em()
alpha = res[0]                  # 区分度(斜率) slop
beta = -1 * (res[1] / alpha)    # 难度
"""
结果和R语言ltm 包算出来的一致
ltm 用法参考这本书：《Using R for Item Response Theory Model Applications by Insu Paek, Ki Cole (z-lib.org)》

#detach("package:eRm")
#install.packages("ltm")
library("ltm")
setwd("D:\\workcode\\algo")
getwd()
#answers <- read.csv("answers_2PL.csv")

#ddd<- read.csv("answers_2PL.csv")
ddd<- read.csv('lsat.csv')

#ddd<-read.fwf("c2_2pl.dat", widths=c(10,rep(1,20)))  # read fixed width data format
# 前10 列是person identification
dim(ddd) #2.2_2
#数据维度是：(1000*21)，默认列名是：V1 到V21
#第一列是person index

#ddd <- ddd[,-1] # 2.2_3 
#去掉第一列，只取 V2到V21
#用head(ddd) 或 names(ddd) 来验证这一点

#names(ddd) <- paste("It",1:20, sep="") #2.2_4
#列名重命名为：It1 到It20

mod.2pl <- ltm(ddd~z1, IRT.param=T) #2. 2_5
mod.2pl$conv #2. 2_6

summary(mod.2pl) #2.2_7
co <- coef(mod.2pl) #2.2_8
co
"""


# 模拟参数
a = np.random.uniform(1, 3, 1000)
b = np.random.normal(0, 1, size=1000)
z = Irt2PL.z(a, b, 1)
p = Irt2PL.p(z)
score = np.random.binomial(1, p, 1000)
# 计算并打印潜在特质估计值
eap = EAPIrt2PLModel(score, a, b)
print(eap.res)

print('hi,,,')

