
"""
功能：XOR 算法神经网络实现
    向量x 到向量 h的仿射变换，仿射变换相比线性变换多了一个平移，原点变了。线性变换保证几何体的形状和比例不变
        平移是通过加上一个常量，既偏置完成的
        输入信号作为列向量左乘权重矩阵，求出输入信号的加权和，激活函数把若干个加权和压缩到0 和1 之间，这就是隐层的单元了，隐层单元又作为输入信号开始新一轮的计算，
            最后在输出层得到前向传播的最终结果，这就是预测值


梯度是偏导数的向量
    但是仍然使用：“x上的梯度” 这样的术语，因为简单
    函数关于每个变量的偏导数指明了整个表达式对于该变量的敏感程度
    反向传播，可以计算各个节点的导数
    通过比较数值微分和误差反向传播法的结果，可以确认误差反向传播法的实现是否正确（梯度确认）


《深度学习入门：基于Python的理论与实现》

梯度下降过程向量化 - Logistic回归总结 洞庭之子
https://www.cnblogs.com/earendil/p/8268757.html
doc\lang\programming\梯度下降过程向量化

CS231n课程笔记翻译：反向传播笔记
https://zhuanlan.zhihu.com/p/21407711

神经网络求解异或问题
https://towardsdatascience.com/implementing-the-xor-gate-using-backpropagation-in-neural-networks-c1f255b4f20d

神经网络中的偏置项b到底是什么？
https://www.jiqizhixin.com/articles/2018-07-05-18
https://www.jiqizhixin.com/articles/2018-12-24-19

浅层神经网络
https://redstonewill.github.io/2018/03/26/37/

"""

import numpy as np


inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_output = np.array([[0],[1],[1],[0]])

inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2,2,1

hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
"""
  一边一权重，算看有多少条边
    二输入每对应一隐层单元就是2 条边，所以“第一间”边上的权重是2*2（间的说法对比五线谱的线间关系，  \
    输入层和隐层[也可以认为是中间输出层]分别是第一线，第二线，那么连接它们的边所在位置就是第一间）
    线是line, 间是space， 所以第一间可以用 1th_space 表示
"""

hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))  # 一线一偏置，1th线偏置1，对应2th线的2 单元，两条边。所以维度是 1*2
"""
严格说来这是偏置1 乘以它的权重的结果，因为这样方便，之后直接加到结果上就可以了，不用再把它添加到输入矩阵里了
从数学公式上来看，偏置也不在输入矩阵里，而是作为方程组的常数项
"""

output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))  # 2th 间权重，维度 2*1
output_bias = np.random.uniform(size=(1,outputLayerNeurons))  # 2th 线偏置，维度1*1

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

hidden_layer_activation = np.dot(inputs,hidden_weights)  # 输入信号的加权和，
hidden_layer_activation += hidden_bias # 加上偏置这个常量，实际上是数学上的平移
hidden_layer_output = sigmoid(hidden_layer_activation)
output_layer_activation = np.dot(hidden_layer_output,output_weights)
output_layer_activation += output_bias
predicted_output = sigmoid(output_layer_activation)
"""
输入信号的前向传播(forward propagation)，经过隐层和输出层的计算，得到一组预测输出
backpropagation
"""


lr = 0.01

#Backpropagation
error = expected_output - predicted_output
d_predicted_output = error * sigmoid_derivative(predicted_output)
 
error_hidden_layer = d_predicted_output.dot(output_weights.T)
d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
#Updating Weights and Biases
output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
hidden_weights += inputs.T.dot(d_hidden_layer) * lr
hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr


print("hi,,,")

print(hidden_weights)







