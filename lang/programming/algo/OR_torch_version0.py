
"""
OR 的pytorch 实现

reference:
    doc\lang\programming\pytorch\李宏毅2020机器翻译\iAttention.py
    doc\lang\programming\pytorch\数字识别\ihandwritten_digit_recognition_GPU.ipynb
    https://gist.github.com/user01/68514db1127eb007f24d28bfd11dd60e

"""
import torch
import torch.utils.data as torch_data
from torch import nn
from torch import optim

from time import time

def Data(type='training'):
    data = [
        [ torch.Tensor([0, 0]), torch.Tensor([0]) ],
        [ torch.Tensor([0, 1]), torch.Tensor([1]) ],
        [ torch.Tensor([1, 0]), torch.Tensor([1]) ],
        [ torch.Tensor([1, 1]), torch.Tensor([1]) ]
    ]

    return data

class TorchDataset(torch_data.Dataset):
  def __init__(self, data):
    self.data = data
        
  def __len__(self):
    return len(self.data)
  def __getitem__(self, Index):
    item = self.data[Index]

    return item[0], item[1]

def infinite_iter(data_loader):
  it = iter(data_loader)
  while True:
    try:
      item_in , item_out = next(it)
      yield item_in, item_out
    except StopIteration:
      it = iter(data_loader)

# Layer details for the neural network
input_size = 2 # 输入层两个神经元
# hidden_sizes = [128, 64] # 没有隐层
output_size = 1 # 输出一个值

# Build a feed-forward network
model = nn.Sequential(
  nn.Linear(2, 3),
  nn.ReLU(),
  nn.Linear(3, 1)
)
print(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
model.to(device)



train_dataset = TorchDataset(Data(type='training'))
train_loader = torch_data.DataLoader(train_dataset, batch_size = 2, shuffle=True)  # 每个输入是维度是(2) 的一维数组，每一批输入2 组 来训练
train_iter = infinite_iter(train_loader)

sources, targets = next(train_iter)

print( sources, targets )


optimizer = optim.SGD(model.parameters(), lr=0.01) # momentum=0.05
criterion = nn.MSELoss() #nn.NLLLoss()  # https://zhuanlan.zhihu.com/p/264366034
  # NLLloss 和交叉熵一样只适用于分类任务， NLLLoss是基于softmax，softmax得到结果向量的概率分布，是离散值。回归任务建议MSE或MAE等损失函数
  # 否则提示多个target报错

time0 = time()
epochs = 50000

# 训练模型
for e in range(epochs):
    running_loss = 0
    sources, targets = next(train_iter)

    #targets = targets.squeeze(1) # 降维
    #targets = targets.to(device=device, dtype=torch.long)
    #targets =torch.tensor(targets, dtype=torch.long) # 类型转换

    # Training pass
    optimizer.zero_grad()
        
    output = model( sources.cuda() if torch.cuda.is_available() else sources.cpu() )
    loss = criterion(output,  targets.cuda() if torch.cuda.is_available() else targets.cpu() )
    #This is where the model learns by backpropagating
    loss.backward()
        
    #And optimizes its weights here
    optimizer.step()
        
    running_loss += loss.item()
    
    print("Epoch {} - Training loss: {}".format(e, running_loss/4)) # 4 是总样本数

print("\nTraining Time (in minutes) =",(time()-time0)/60)


# 保存训练好的参数
torch.save(model.state_dict(), "save_OR_torch.pt")

# 验证训练出的模型是否正确
sources, targets = next(train_iter)
with torch.no_grad():
    
    # 加载训练好的参数
    model.load_state_dict(torch.load("save_OR_torch.pt"))
    model.eval()

    output = model( sources.cuda() if torch.cuda.is_available() else sources.cpu() )
    print( sources, output )
