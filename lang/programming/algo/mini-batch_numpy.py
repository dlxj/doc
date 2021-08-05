
"""
异或问题的纯 numpy，mini-bach 实现
"""

import numpy as np


g_batch_size = 4 # 批大小
g_alpha = 0.8# 学习率
maxIter = 50000 # 最大迭代次数



def sigmoid (x):
    return 1/(1 + np.exp(-x))

def Data():
    data = [
        [ [0, 0], [0] ],
        [ [0, 1], [1] ],
        [ [1, 0], [1] ],
        [ [1, 1], [0] ]
    ]

    return data


class DataLoader():
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, Index):
        #np.random.shuffle(self.data) # 乱序
        item = self.data[Index]
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

train_iter = infinite_iter(train_loader, g_batch_size)


W_1 = np.random.uniform(size=(2, 4))   # 2*3 权重
#W_1 = W_1 * 0.1 # 据说对于sigmoid 激活函数，更小的权重更容易收敛

W_2 = np.random.uniform(size=(4, 1))   # 3*1 权重


b_1 = np.random.uniform(size=(4, 4))   # 3*3 偏置

b_2 = np.random.uniform(size=(4, 1))   # 3*1 偏置



for kk in range(15):

    X_0, Y = next(train_iter)
    """
        X_0: (4,2)
        Y:   (4,1)
    """

    for epoch in range(maxIter):


        # 前向传播



        A_1 = np.dot(X_0, W_1)  # 前向传播 (4,2) . (2,4) = (4,4)
        a_1 = A_1 + b_1 


        X_1 = sigmoid(a_1)

        A_2 = np.dot(X_1, W_2)  # (3,3) . (3,1) = (3,1)
        a_2 = A_2 + b_2


        h_2 = sigmoid(a_2) # (3*1)


        E = h_2 - Y



        # 反向传播


        n = 2  # 这是个输入的列数
        m = g_batch_size  # 这就是批大小


        loss = (1.0 / 2 * m ) * np.sum( E ** 2 )

        print("Losss: ", loss, " -- ",epoch, '/', maxIter )

        #if (loss <= 0.001):
        #    break


        """
        第一层权重更新
        """
        for i in range(n):

            for j in range(m):
    
                S = 0 # 累加求和结果
        
                for s in range(m):
                    h_2_s_1 = h_2[s][0]
                    y_s_1 = Y[s][0]
                    g_a_1_s_j = X_1[s][j]
                    x_0_s_i = X_0[s][i]

                    S += ( h_2_s_1 - y_s_1 ) *  h_2_s_1 * ( 1 - h_2_s_1 ) * W_1[i][j] * g_a_1_s_j * ( 1 - g_a_1_s_j ) * x_0_s_i

                w_1_i_j_derivative = ( 1.0 / m ) * S  # 权重的导数

                W_1[i][j] = W_1[i][j] - g_alpha * w_1_i_j_derivative # 权重更新


        """
        第一层偏置更新
        """
        for j in range(m):

            S = 0

            for s in range(m):

                #b_1_s_j = b_1[s][j]

                h_2_s_1 = h_2[s][0]
        
                y_s_1 = Y[s][0]

                g_a_1_s_j = X_1[s][j]

                S += ( h_2_s_1 - y_s_1 ) * W_2[j][0] * g_a_1_s_j * (1 - g_a_1_s_j)


            b_1_s_j_derivative = (1.0 / m) * S

            b_1[s][j] =  b_1[s][j] - g_alpha * b_1_s_j_derivative   # 偏置更新 



        """
        第二层权重更新
        """
        for j in range(m):

            S = 0

            for s in range(m):
        
                h_2_s_1 = h_2[s][0]
                y_s_1 = Y[s][0]
                x_1_s_j = X_1[s][j]

                S += ( h_2_s_1 - y_s_1 ) * h_2_s_1 * ( 1 -  h_2_s_1) * x_1_s_j


            w_2_j_1_derivative = (1.0 / m) * s

            W_2[j][0] = W_2[j][0] - g_alpha * w_2_j_1_derivative  # 权重更新



        """
        第二层偏置更新
        """
        S = 0

        for s in range(m):
        
            h_2_s_1 = h_2[s][0]
            y_s_1 = Y[s][0]

            S += (h_2_s_1 - y_s_1) * h_2_s_1 * ( 1 - h_2_s_1 )

            b_2_j_1_derivative = (1.0 / m) * S

            b_2[s][0] = b_2[s][0] - g_alpha * b_2_j_1_derivative


    print(X_0, Y)







