
"""
OR 的pytorch 实现

reference:
    doc\lang\programming\pytorch\李宏毅2020机器翻译\iAttention.py
    doc\lang\programming\pytorch\数字识别\ihandwritten_digit_recognition_GPU.ipynb

"""
import torch
import torch.utils.data as torch_data
from torch import nn

def Data(type='training'):
    data = [
        [ [0, 0], [0] ],
        [ [0, 1], [1] ],
        [ [1, 0], [1] ],
        [ [1, 1], [1] ]
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


# Layer details for the neural network
input_size = 2 # 输入层两个神经元
# hidden_sizes = [128, 64] # 没有隐层
output_size = 1 # 输出一个值

# Build a feed-forward network
model = nn.Sequential(nn.Linear(input_size, output_size))
print(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
model.to(device)


train_dataset = TorchDataset(Data(type='training'))
trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=1, shuffle=True)




