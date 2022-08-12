
import torch

def j3():
 x = torch.ones(3, requires_grad=True)

 y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))

 v = torch.tensor([3, 5, 7])

 y.backward(v)
 print(x.grad)
 """
 The Jacobian seems correct and if it multiplies on vector (3, 5, 7) I would expect result to be (11, 17, 14).
 Got it! We should transpose Jacobian before multiplication. Then everything matches.
 """

 print( torch.matmul(  torch.tensor([ [2, 0, 0], [1, 2 , 0], [0, 1, 2] ]),  torch.tensor([ [3], [5], [7] ]) ) )       # J.t() @ v  结果是列向量
 print( torch.matmul(  torch.tensor([ [3], [5], [7] ]).t(), torch.tensor([ [2, 1, 0], [0, 2 , 1], [0, 0, 2] ])  ) )   # v.t() @ J  结果是行向量

j3()