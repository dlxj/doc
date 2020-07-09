import numpy as np


class Gradient:
    """
    原始梯度下降
    """
    def __init__(self, learning_rate = 0.001):
        self.learning_rate = learning_rate
    
    def delta(self, gradient):
        """
        接受当前点的梯度，给出前进向量：学习率乘以梯度反方向
        """
        return -self.learning_rate * gradient


class Decay:
    """
    学习率衰减
    """
    def __init__(self, learning_rate = 0.001, r = 500):
        self.learning_rate = learning_rate
        self.r = r
        self.global_steps = 0
        
    
    def delta(self, gradient):
        """
        接受当前点的梯度，给出前进向量。根据学习率衰减公式调整学习率
        """
        eta = self.learning_rate * 10 ** (-self.global_steps / self.r)
        self.global_steps += 1
        return -eta * gradient


class Momentum:
    """
    冲量梯度下降。
    """
    def __init__(self, learning_rate = 0.001, beta = 0.9):
        self.learning_rate = learning_rate
        self.v = None
        self.beta = beta
    
    def delta(self, gradient):
        """
        接受当前点的梯度，给出前进向量。加入冲量机制
        """
        if self.v is None:
            # 将v初始化为与梯度同维数的全零向量
            self.v = np.mat(np.zeros(gradient.shape[0])).T
            
        self.v = self.beta * self.v - self.learning_rate * gradient
        return self.v


class AdaGrad:
    """
    AdaGrad
    """
    def __init__(self, learning_rate = 0.001):
        self.learning_rate = learning_rate
        self.s = None
    
    def delta(self, gradient):
        """
        接受当前点的梯度，根据AdaGrad算法得到前进向量
        """
        if self.s is None:
            # 将s初始化为与梯度同维数的全零向量
            self.s = np.mat(np.zeros(gradient.shape[0])).T
            
        self.s = self.s + np.power(gradient, 2)
        return -self.learning_rate * gradient / np.sqrt(self.s + 1e-10)


class RMSProp:
    """
    RMSProp
    """
    def __init__(self, learning_rate = 0.001, beta = 0.9):
        self.learning_rate = learning_rate
        self.s = None
        self.beta = beta
    
    def delta(self, gradient):
        """
        接受当前点的梯度，根据RMSProp算法得到前进向量
        """
        if self.s is None:
            # 将s初始化为与梯度同维数的全零向量
            self.s = np.mat(np.zeros(gradient.shape[0])).T
            
        self.s = self.beta * self.s + (1 - self.beta) * np.power(gradient, 2)
        return -self.learning_rate * gradient / np.sqrt(self.s + 1e-10)


class Adam:
    """
    Adam
    """
    def __init__(self, learning_rate = 0.001, beta_1 = 0.9, beta_2 = 0.99):
        self.learning_rate = learning_rate
        self.s = None
        self.v = None
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.global_steps = 0
    
    def delta(self, gradient):
        """
        接受当前点的梯度，根据Adam算法得到前进向量
        """
        if self.s is None or self.v is None:
            # 将s初始化为与梯度同维数的全零向量
            self.s = np.mat(np.zeros(gradient.shape[0])).T
            # 将v初始化为与梯度同维数的全零向量
            self.v = np.mat(np.zeros(gradient.shape[0])).T
        
        self.v = self.beta_1 * self.v + (1 - self.beta_1) * gradient
        self.s = self.beta_2 * self.s + (1 - self.beta_2) * np.power(gradient, 2)
        
        self.v = self.v / (1 - self.beta_1 ** (self.global_steps + 1))
        self.s = self.s / (1 - self.beta_2 ** (self.global_steps + 1))
        self.global_steps += 1
        
        return -self.learning_rate * self.v / np.sqrt(self.s + 1e-10)
