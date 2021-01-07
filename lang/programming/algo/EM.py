
"""
EM 算法估计IRT 题目参数，注意他的公式定义和书上的有差异
https://zhuanlan.zhihu.com/p/29887184
"""

import numpy as np
import warnings


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

def _lik(scores, p_val):
    # 似然函数
    loglik_val = np.dot(np.log(p_val + 1e-200), scores.transpose()) + \
                    np.dot(np.log(1 - p_val + 1e-200), (1 - scores).transpose())
    return np.exp(loglik_val)

def _e_step(scores, p_val, weights):
    # EM算法E步
    # 计算theta的分布人数
    lik_wt = _lik(scores, p_val) * weights
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

def _newton(p_val, full_dis, right_dis, slop, threshold, theta):
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


if __name__ == "__main__":

    init_slop=None; init_threshold=None; max_iter=10000; tol=1e-5; gp_size=11; m_step_method='newton'
    
    """
    先模似答题数据
    阀值 = -1 * ( 难度 * 区分度 )
    难度 = -1 * ( 阀值 / 区分度 )
    """
    # n_persons = 10
    # n_questions = 5
    n_persons = 1000
    n_questions = 5
    
    np.random.seed(543678)
    true_theta = np.random.normal(loc=0, scale=1, size=(n_persons,1))   # 能力 (10*1)
    true_theta = np.tile(true_theta, n_questions)                       # 每道题的能力都一样，列复制10次 (10*1) -> (10*5)
    true_beta = np.random.normal(loc=0, scale=1, size=(1,n_questions))  # 5个问题的难度 (1*5)

    true_alpha = np.random.uniform(1, 3, (1,n_questions) ) # 区分度 (1*10)
    true_threshold = -1 * ( true_beta * true_alpha )

    z = Z(true_alpha, true_threshold, true_theta) # slop, threshold, theta (_z = slop * theta + threshold )
    likelihood = P(z)  # 每个人，每道题，回答正确的概率
    
    scores = np.random.binomial(size=(n_persons, n_questions), p=likelihood, n=1)  # (10*5) 二值分布，1 的概率由p 给出

    """
    先求11 个积分点
    """
    x_nodes, x_weights = np.polynomial.hermite.hermgauss(gp_size)  # Gauss–Hermite积分点数
    x_nodes = x_nodes * 2 ** 0.5
    x_nodes.shape = x_nodes.shape[0], 1
    x_weights = x_weights / np.pi ** 0.5
    x_weights.shape = x_weights.shape[0], 1
    

    slop = np.ones(scores.shape[1])
    threshold = np.zeros(scores.shape[1])

    convergenceQ = False

    for i in range(max_iter):
        z = Z(slop, threshold, x_nodes)
        p_val = P(z)
        full_dis, right_dis = _e_step(scores, p_val, x_weights)
        slop, threshold, delta_list = _newton(p_val, full_dis, right_dis, slop, threshold, x_nodes) # _m_step  x_nodes 作为theta(能力)
        if np.max(np.abs(delta_list)) < tol:
            print(i)
            convergenceQ = True
    
    if convergenceQ:
        # 正常收敛
        # 区分度(斜率) slop
        # 阀值 threshold
        # print( slop, threshold )
        beta = -1 * (threshold / slop)  # 难度
        
        # 难度的均方误差
        print('difficulty mse: {}'.format(np.mean((beta - true_beta) ** 2)))

        # 区分度的均方误差
        print('slop mse: {}'.format(np.mean((slop - true_alpha) ** 2)))
    else:
        warnings.warn("no convergence")
        print(slop, threshold)




