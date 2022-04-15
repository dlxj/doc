

"""
EM算法(期望最大化算法)简介 http://blog.sciencenet.cn/blog-2970729-1191928.html
Think Bayes - 我所理解的贝叶斯定理 https://zhuanlan.zhihu.com/p/22467549

"""

import numpy as np


# n 选k 的组合数
def C(n, k):
    return np.math.factorial(n) / ( np.math.factorial(k) * np.math.factorial(n - k) ) # factorial 是阶乘的意思


def _lik(array, thetas):
    # 似然函数
    thetaA = thetas[0]
    thetaB = thetas[1]
    
    """
    k 这个结果出现了，它是由A 抛出来的概率就是似然。既似然其实就是一个条件概率
    表示这个结果是A 抛出来的可能性有多大
    """
    n = len(array)    # 总共抛n 次
    k = np.sum(array) # 正面向上的次数是k
    
    
    c = C(n, k) # 二项系数

    H_A = c * ( thetaA ** k ) * ( 1 - thetaA ) ** (n - k)  # 由A 来抛，出现这个结果的概率
    H_B = c * ( thetaB ** k ) * ( 1 - thetaB ) ** (n - k)  # 由B 来抛，出现这个结果的概率

    """
    用贝叶斯定理算出似然值
    """
    lik_A = H_A / ( H_A + H_B )  # 这个结果是A 抛的概率
    lik_B = H_B / ( H_A + H_B )  # 这个结果是B 抛的概率
    
    return lik_A, lik_B, n, k


"""
真实概率是true_thetas，目标是用EM 算法估计出这个真实概率
"""
true_thetas = [ 0.7, 0.3 ]  # A，B 两枚硬币正面向上的概率
#true_thetas = [ 0.5, 0.5 ]

"""
总共进行5 次实验，每次实验随机选一枚硬币抛10 次
"""
arrays = [] # 所有实验结果

"""
自已生成模似数据的方法
"""
# for i in range(5):
#     theta = true_thetas[ np.random.binomial(size=1, p=0.5, n=1)[0] ]  # 随机选一枚硬币
#     array = np.random.binomial(size=10, p=theta, n=1)  # 抛10 次。二项分布，值为1 的概率由p 给出
#     arrays.append(array)

# k = np.sum(array) # 正面向上的次数 


if __name__ == "__main__":

    """
    论文里面的真实数据，用于验证算法正确性
    """
    arrays = [
        [1,0,0,0,1,1,0,1,0,1],
        [1,1,1,1,0,1,1,1,1,1],
        [1,0,1,1,1,1,1,0,1,1],
        [1,0,1,0,0,0,1,1,0,0],
        [0,1,1,1,0,1,1,1,0,1]
    ]

    max_iter=100

    thetas = [ 0.6, 0.5 ]  # 未知参数开始时先随便估计一个值 

    for _ in range(max_iter):
        
        E_A = []; E_B = []
        for i in range(len(arrays)):
            lik_A, lik_B, n, k = _lik( arrays[i], thetas  ) # 这个结果是A 抛的概率、B 抛的概率、总共抛n 次、结果是k 次正面向上
            E_A.append( [ round(lik_A * k, 1), round(lik_A  * ( n - k ), 1) ] )  # k 次正面的单次期望，n - k 次反面的单次期望
            E_B.append( [ round(lik_B * k, 1), round(lik_B  * ( n - k ), 1) ] )
        
        E_A = np.sum(E_A, axis=0) # 按列连加
        E_B = np.sum(E_B, axis=0)

        # 更新参数（用期望来算概率）

        thetas[0] = E_A[0] / (E_A[0] + E_A[1])
        thetas[1] = E_B[0] / (E_B[0] + E_B[1])
    
    print( thetas )  # 最终估计值




