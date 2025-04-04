# import torch
# from torch.autograd import Variable
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim


import jax
import jax.numpy as np
import numpy as onp
import jax.random as jrandom


# 此激活函数设计为可以接受列向量
# 返回结果也是列向量
# np.exp 的实现可以接受向量作为参数，所以代码很简洁
def sigmoid (x):
    return 1/(1 + np.exp(-x))

X = np.array([
               [[0, 0]],  # (1*2) 的输入  
               [[0, 1]],
               [[1, 0]],
               [[1, 1]]
             ], onp.float)

Y = np.array([
                [[0]],    # (1*1) 的输出
                [[1]],
                [[1]],
                [[0]]
             ], onp.float)

key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)

W1 = jax.random.normal(key1, shape=(2, 3), dtype=np.float32)   # (2*1) 权重

W2 = jax.random.normal(key2, shape=(3, 1), dtype=np.float32)   # (3*1) 权重


b1 = jax.random.normal(key3, shape=(1, 3), dtype=np.float32)   # (1*3) 偏置

b2 = jax.random.normal(key4, shape=(1, 1), dtype=np.float32)   # (1*1) 偏置


alpha = 0.5 # 学习率
maxIter = 50000 # 最大迭代次数

# 求前向传播的均方误差
def loss(X, W1, b1, W2, b2):
    A1 = np.dot(X, W1) + b1  
    # H1 = sigmoid(A1)
    H1 = jax.nn.sigmoid(A1)

    A2 = np.dot(H1, W2) + b2  
    H2 = jax.nn.sigmoid(A2)

    E = H2 - Y             # 误差值
    E2 = E ** 2
    
    errs = np.sum( E2, axis=0 )[0] # 按列求和

    lss = 1 / 2 * errs  # 均方误差值

    return lss[0]


loss_jit = jax.jit(loss)

for k in range(maxIter): 

    # grads = jax.grad(loss, argnums=(1,))(X, W, m)
    
    [ lss, grads ] = jax.value_and_grad(loss_jit, argnums=(1,2,3,4,))(X, W1, b1, W2, b2)  # 表示对 第1,2,3,4 个参数进行求导 (索引从0 开始，这里的第一个参数是 W1)

    lss = float(lss)  # lss 是 0 维数组，不能用下标去索引

    W1 = W1 - alpha * grads[0]
    b1 = b1 - alpha * grads[1]
    W2 = W2 - alpha * grads[2]
    b2 = b2 - alpha * grads[3]

    if lss < 0.001: 

        print(f"loss is: {lss}, curr iter num: {k}")

        print('final results: ')

        for input, target in zip(X, Y):
            A1 = np.dot(input, W1) + b1  
            H1 = sigmoid(A1)

            A2 = np.dot(H1, W2) + b2  
            H2 = jax.nn.sigmoid(A2)

            print("Input:[{}] Target:[{}] Predicted:[{}]".format(
                input, target, H2, input - target
            ))
       
        break

    if k % 100 == 0:
        print(f"loss is: {lss}, curr iter num: {k}")


# EPOCHS_TO_TRAIN = 20000

# class Net(nn.Module):

#     def __init__(self):
#         super(Net, self).__init__()
#         self.fc1 = nn.Linear(2, 3, True)   # (1*2) . (2*3) = (1*3)
#         self.fc2 = nn.Linear(3, 1, True)   # (1*3) . (3*1) = (1*1)

#     def forward(self, x):

#         tmp = self.fc1(x)
        
#         x = F.sigmoid(tmp)


#         x = self.fc2(x)
#         return x

# net = Net()
# inputs = list(map(lambda s: (torch.Tensor([s])), [  # Variable  # Variable 是可以自动微分的 Tensor，Varibale 默认不求梯度 # doc\lang\programming\pytorch summary.md
#     [0, 0],
#     [0, 1],
#     [1, 0],
#     [1, 1]
# ]))
# targets = list(map(lambda s: (torch.Tensor([s])), [  # Variable
#     [0],
#     [1],
#     [1],
#     [0]
# ]))


# criterion = nn.MSELoss()
# optimizer = optim.SGD(net.parameters(), lr=0.01)

# print("Training loop:")
# for idx in range(0, EPOCHS_TO_TRAIN):
#     for input, target in zip(inputs, targets):
#         optimizer.zero_grad()   # zero the gradient buffers
#         output = net(input)
#         loss = criterion(output, target)
#         loss.backward()
#         optimizer.step()    # Does the update
#     if idx % 5000 == 0:
#         print("Epoch {: >8} Loss: {}".format(idx, loss.data.numpy()))



# print("")
# print("Final results:")
# for input, target in zip(inputs, targets):
#     output = net(input)
#     print("Input:[{},{}] Target:[{}] Predicted:[{}] Error:[{}]".format(
#         int(input.data.numpy()[0][0]),
#         int(input.data.numpy()[0][1]),
#         int(target.data.numpy()[0]),
#         round(float(output.data.numpy()[0]), 4),
#         round(float(abs(target.data.numpy()[0] - output.data.numpy()[0])), 4)
#     ))
