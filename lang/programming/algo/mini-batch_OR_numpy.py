
"""
或问题的纯 numpy，mini-bach 实现
"""

import numpy as np




g_batch_size = 2 # 批大小
g_alpha = 0.1 # 学习率
maxIter = 10000 # 最大迭代次数


"""
    M: 批大小
    N: 每个样本的属性数
    C: 隐层结点数
    NClass: 分类数 

"""
M=2; N=2; C=2; NClass=2




def sigmoid (x):
    return 1/(1 + np.exp(-x))

def stable_softmax(X):
    exps = np.exp(X - np.max(X))
    return exps / np.sum(exps)


def Data():
    data = [
        [ [0, 0], [1, 0] ], # 对于给定输入[0, 0]， 分类为0 的概率是1， 1 的概率是0
        [ [0, 1], [0, 1] ],
        [ [1, 0], [0, 1] ],
        [ [1, 1], [0, 1] ]
    ]

    return data


class DataLoader():
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, Index):
        np.random.shuffle(self.data) # 乱序
        #item = self.data[Index]
        item = self.data[0]
        return item[0], item[1]

def infinite_iter(data_loader, batch_size):
  it = iter(data_loader)
  while True:
    try:
      arr1 = []
      arr2 = []
      for i in range(batch_size):
        source , target = next(it)
        arr1.append( source )
        arr2.append( target )
      
      yield arr1, arr2
    except StopIteration:
      it = iter(data_loader)

train_loader = DataLoader(Data())

train_iter = infinite_iter(train_loader, M)

X_0, Y = next(train_iter) # 随机得到三个样本，作为一个mini-batch 输入

print(X_0, Y)



w = np.random.uniform(size=(N, C))   # 2*2 权重

b = np.random.uniform(size=(M, C))   # 2*2 偏置




epoch = 3

for _ in range(epoch):

    x, p = next(train_iter)
    """
        X_0: (4,2)
        Y:   (4,1)
    """

    for iter in range(maxIter):


        # 前向传播

        A = np.dot(x, w)  # 前向传播 (2,2) . (2,2) = (2,2)
        a = A + b 

        q = stable_softmax(a)


        c = np.zeros( (M,1) )  # 存交叉熵

        # 交叉熵
        for i in range(M):

            ce_i_1 = 0.0

            for j in range(NClass):

                q_i_j = q[i][j]

                p_i_j = p[i][j]


                ce_i_1 += p_i_j * np.log( q_i_j )

            ce_i_1 = -1 * ce_i_1

            c[i][0] = ce_i_1


        L = (1.0 / M) * np.sum(c)  # 损失


        


            


        # E = h_2 - Y



        # # 反向传播


        # n = 2  # 这是个输入的列数
        # m = g_batch_size  # 这就是批大小


        # loss = (1.0 / 2 * m ) * np.sum( E ** 2 )

        # print("Losss: ", loss, " -- ",epoch, '/', maxIter )

        # #if (loss <= 0.001):
        # #    break


        # """
        # 第一层权重更新
        # """
        # for i in range(n):

        #     for j in range(m):
    
        #         S = 0 # 累加求和结果
        
        #         for s in range(m):
        #             h_2_s_1 = h_2[s][0]
        #             y_s_1 = Y[s][0]
        #             g_a_1_s_j = X_1[s][j]
        #             x_0_s_i = X_0[s][i]

        #             S += ( h_2_s_1 - y_s_1 ) *  h_2_s_1 * ( 1 - h_2_s_1 ) * W_1[i][j] * g_a_1_s_j * ( 1 - g_a_1_s_j ) * x_0_s_i

        #         w_1_i_j_derivative = ( 1.0 / m ) * S  # 权重的导数

        #         W_1[i][j] = W_1[i][j] - g_alpha * w_1_i_j_derivative # 权重更新


        # """
        # 第一层偏置更新
        # """
        # for j in range(m):

        #     S = 0

        #     for s in range(m):

        #         #b_1_s_j = b_1[s][j]

        #         h_2_s_1 = h_2[s][0]
        
        #         y_s_1 = Y[s][0]

        #         g_a_1_s_j = X_1[s][j]

        #         S += ( h_2_s_1 - y_s_1 ) * W_2[j][0] * g_a_1_s_j * (1 - g_a_1_s_j)


        #     b_1_s_j_derivative = (1.0 / m) * S

        #     b_1[s][j] =  b_1[s][j] - g_alpha * b_1_s_j_derivative   # 偏置更新 



        # """
        # 第二层权重更新
        # """
        # for j in range(m):

        #     S = 0

        #     for s in range(m):
        
        #         h_2_s_1 = h_2[s][0]
        #         y_s_1 = Y[s][0]
        #         x_1_s_j = X_1[s][j]

        #         S += ( h_2_s_1 - y_s_1 ) * h_2_s_1 * ( 1 -  h_2_s_1) * x_1_s_j


        #     w_2_j_1_derivative = (1.0 / m) * s

        #     W_2[j][0] = W_2[j][0] - g_alpha * w_2_j_1_derivative  # 权重更新



        # """
        # 第二层偏置更新
        # """
        # S = 0

        # for s in range(m):
        
        #     h_2_s_1 = h_2[s][0]
        #     y_s_1 = Y[s][0]

        #     S += (h_2_s_1 - y_s_1) * h_2_s_1 * ( 1 - h_2_s_1 )

        #     b_2_j_1_derivative = (1.0 / m) * S

        #     b_2[s][0] = b_2[s][0] - g_alpha * b_2_j_1_derivative


    print('hi,,,')







