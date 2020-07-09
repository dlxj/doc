import numpy as np


class NeuralNetwork:

    def __init__(self, shape, activations, learning_rate = 0.005, iterations = 8000, 
                 minibatch_size = 32, beta_1 = 0.9, beta_2 = 0.99):
        
        if not len(shape) == len(activations):
            raise Exception("激活函数名称数组必须等于层数。")

        # shape数组是每层的神经元数量，最后一层是输出层，其神经元数量必须与问题类别数一致
        self.shape = shape
        # shape数组的长度为神经网络的深度
        self.depth = len(self.shape)
        
        # 保存各层的输出值以及局部误差的数组
        self.outputs = [0] * (self.depth + 1)
        self.deltas = [0] * self.depth

        self.learning_rate = learning_rate # 学习率
        self.iterations = iterations # 迭代数量

        # 每次迭代取minibatch_size个样本为一批（mini batch）
        # 计算这批样本的平均交叉熵的梯度。顺序取完所有训练样本后，从头再来
        self.minibatch_size = minibatch_size
        
        # Adam算法的两个超参
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        
        # activations数组包含各层激活函数的名称
        # 输出层直接连SoftMax，所以最后一层的激活函数应设为恒等函数"idendity"
        self.activations = activations
        self.activation_func = []
        self.activation_func_diff = []
        
        for f in activations:

            f = f.lower()
            if f == "logistic":
                self.activation_func.append(self.logistic)
                self.activation_func_diff.append(self.logistic_diff)
            elif f == "identity":
                self.activation_func.append(self.identity)
                self.activation_func_diff.append(self.identity_diff)
            elif f == "relu":
                self.activation_func.append(self.relu)
                self.activation_func_diff.append(self.relu_diff)
            elif f == "tanh":
                self.activation_func.append(self.tanh)
                self.activation_func_diff.append(self.tanh_diff)
            else:
                raise Exception("不支持的激活函数：{:s}".format(f))

        # 保存各层权值矩阵和偏置向量的数组
        self.weights = [0] * self.depth
        self.biases = [0] * self.depth
        
        # 在未提供训练数据时，输入层的权值矩阵的尺寸未知
        # 故在这里只初始化非输入层的权值矩阵和偏置向量
        self.input_weights_initialized = False
        for idx in np.arange(1, self.depth):
            # 权值以0均值、0.001标准差的正态分布初始化
            self.weights[idx] = np.mat(np.random.normal(0, 0.001,
                        size=(self.shape[idx], self.shape[idx - 1])))
            # 偏置向量以0值初始化
            self.biases[idx] = np.mat(np.zeros((self.shape[idx], 1)))
        
        # 保存Adam算法用到的累积梯度一阶矩和二阶矩的数组
        self.weights_v = [0] * self.depth
        self.weights_s = [0] * self.depth
        
        self.biases_v = [0] * self.depth
        self.biases_s = [0] * self.depth


    def compute(self, x):
        """
        x为n_features * n_samples矩阵，每列为一个样本
        本函数计算神经网络对这批样本的输出
        """
        result = x
        for idx in np.arange(0, self.depth):
            self.outputs[idx] = result
            # 对上一层的输出计算仿射值
            al = self.weights[idx] * result + self.biases[idx]

            # 对仿射值施加激活函数
            result = np.mat(self.activation_func[idx](al))

        self.outputs[self.depth] = result
        return self.softmax(result)


    def predict(self, x):
        """
        x为n_samples * n_features矩阵，每行为一个样本
        本函数仅仅是对compute函数的简单封装，供使用者执行预测之用
        """

        if not x.shape[0] or not x.shape[1]:
            raise Exception("数据为空。")

        return self.compute(x.T).T.A


    def bp(self, d):
        """
        反向传播
        """
        tmp = d.T

        for idx in np.arange(0, self.depth)[::-1]:
            delta = np.multiply(tmp, self.activation_func_diff[idx](self.outputs[idx + 1]).T)
            self.deltas[idx] = delta
            tmp = delta * self.weights[idx]


    def update(self):
        """
        运用Adam算法更新权值矩阵和偏置向量
        """

        for idx in np.arange(0, self.depth):

            weights_grad = self.deltas[idx].T * self.outputs[idx].T / self.deltas[idx].shape[0]
            biases_grad = np.mean(self.deltas[idx].T, axis=1)

            # 累积权值矩阵的梯度的一阶和二阶矩
            self.weights_v[idx] = self.beta_1 * self.weights_v[idx] + (1 - self.beta_1) * weights_grad
            self.weights_s[idx] = self.beta_2 * self.weights_s[idx] + (1 - self.beta_2) * np.power(weights_grad, 2)
            
            # 累积偏置向量的梯度的一阶和二阶矩
            self.biases_v[idx] = self.beta_1 * self.biases_v[idx] + (1 - self.beta_1) * biases_grad
            self.biases_s[idx] = self.beta_2 * self.biases_s[idx] + (1 - self.beta_2) * np.power(biases_grad, 2)

            # 更新权值矩阵和偏置向量，在此我们省略了Adam中对一阶和二阶矩的微小调整
            self.weights[idx] = self.weights[idx] - self.learning_rate * self.weights_v[idx] / np.sqrt(self.weights_s[idx] + 1e-10)
            self.biases[idx] = self.biases[idx] - self.learning_rate * self.biases_v[idx] / np.sqrt(self.biases_s[idx] + 1e-10)


    def train(self, x, y):

        if not x.shape[0] or not x.shape[1] or x.shape[0] != y.shape[0] or not y.shape[1]:
            raise Exception("特征矩阵与one hot标签矩阵的样本数不相同，或数据为空。")

        # 根据输入向量的维数初始化输入层权值矩阵和偏置向量
        if not self.input_weights_initialized:
            self.weights[0] = np.mat(np.random.normal(0, 0.001, size=(self.shape[0], x.shape[1])))
            self.biases[0] = np.mat(np.zeros((self.shape[0], 1)))
            self.input_weights_initialized = True

        start = 0
        for i in range(self.iterations):

            # 从全体训练样本中取下一批
            end = start + self.minibatch_size
            minibatch_x = x[start:end].T
            minibatch_y = y[start:end].T
            start = (start + self.minibatch_size) % x.shape[0]

            # 计算当前网络对这批样本的预测概率
            yp = self.compute(minibatch_x)
            
            # 计算当前模型对这批样本的正确率
            loss = np.mean(-np.sum(np.multiply(minibatch_y, np.log(yp + 1e-300)), axis=0))
            pred = np.argmax(yp, axis=0) # 取概率最大的类别为预测类别
            truth = np.argmax(minibatch_y, axis=0)
            accuracy = (pred == truth).astype(np.int).sum() / self.minibatch_size
            print("迭代:{:d}，损失值:{:.6f}，正确率：{:.2f}%".format(i, loss, accuracy * 100))
            
            # 误差
            d = yp - minibatch_y

            # 误差的反向传播
            self.bp(d)
            
            # 更新模型参数
            self.update()
            

    """
    几种激活函数。在本实现中，激活函数的导函数接受的是神经元的输出，
    因为logistic、tanh和relu可以用输出计算导数，而且还更节省计算量。
    但是并非所有激活函数都可以用输出计算导数。
    """
    @staticmethod
    def logistic(x):
        return 1.0 / (1.0 + np.power(np.e, np.where(-x > 1e2, 1e2, -x)))

    @staticmethod
    def logistic_diff(x):
        return np.multiply(x, (1 - x))

    @staticmethod
    def relu(x):
        return np.where(x > 0, x, 0.0)

    @staticmethod
    def relu_diff(x):
        return np.where(x > 0, 1.0, 0.0)

    @staticmethod
    def identity(x):
        return x

    @staticmethod
    def identity_diff(x):
        return np.ones(x.shape)

    @staticmethod
    def tanh(x):
        exp = 2 * np.where(x > 1e2, 1e2, x)
        return (np.power(np.e, exp) - 1) / (np.power(np.e, exp) + 1)

    @staticmethod
    def tanh_diff(x):
        return 1 - np.multiply(x, x)

    @staticmethod
    def softmax(x):
        x[x > 1e2] = 1e2
        ep = np.power(np.e, x)
        return ep / np.sum(ep, axis=0)
