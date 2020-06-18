
"""
深度学习之单层感知器（一）
https://zhuanlan.zhihu.com/p/28929620
"""

import numpy as np
#建立数据集
x = np.mat([[1,0,0],[1,0,1],[1,1,0],[1,1,1],[0,0,1],[0,1,0],[0,1,1],[0,0,0]])
y = np.mat([[-1],[1],[1],[1],[-1],[-1],[1],[-1],])

#设置初始权值和偏置值
w = np.mat([0.3,0.3,0.3])
baise = 0.4

#学习率
rate = 0.01

#激活函数
def sgn(x):
  return np.where(x >= 0.0, 1, -1)

#通过学习规则，进行迭代
for i in range(1000):
  #误差计算
  errors = 0
  for j in range(len(x)):
    #误差计算
    r = rate*(y[j] - sgn(x[j]*w.T+baise))
    #r = rate*(y[j] - (x[j]*w.T+baise))
    #调整权值
    w += r*x[j]
    baise += r
    #误差计算
    errors += abs(r)
  print(i,' iter :error is ', errors)
  if errors ==0:
    break





