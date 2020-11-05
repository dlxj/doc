
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

def XOR():
    X = torch.tensor([
            [0,0],
            [0,1],
            [1,0],
            [1,1]
        ], dtype=torch.float32)

    Y = torch.tensor([
            [0],
            [1],
            [1],
            [0]
        ], dtype=torch.float32)

    """
    定义线性模型，自动生成并初始化所需权重和偏置
    y = x w^T + b --> x @ w.t() + b
    nn.Linear
        第一参：一条输入样本的维数(行向量)
        第二参：一条输出样本的维数(行向量)
    """

    seq_model = nn.Sequential( # 双隐层模型
        nn.Linear(2, 2),
        nn.Sigmoid(),
        # nn.Linear(2, 2),
        # nn.Sigmoid(),
        nn.Linear(2, 1),
    )

    # seq_model = nn.Sequential(OrderedDict([
    #     ('hidden_linear', nn.Linear(1, 8)),
    #     ('hidden_activation', nn.Tanh()),
    #     ('output_linear', nn.Linear(8, 1))
    # ]))


    #model = nn.Linear(2, 1)  # X 第一行维度是2， Y 第一行的维度是1
    model = seq_model

    # print(model.weight)
    # print(model.bias)
    list(model.parameters()) # 返回模型中的所有权重和偏置

    # Define dataset
    train_ds = TensorDataset(X, Y)  # 生成训练样本  (  tensor(输入), tensor(输出)  )
    print( train_ds[0:2] )          # 查看前两条样本

    # Define data loader
    batch_size = 4
    train_dl = DataLoader(train_ds, batch_size, shuffle=True)  # 样本分组(batches)，2 条样本一组 # shuffle 重新洗牌，既乱序

    opt = torch.optim.SGD(model.parameters(), lr=0.1)  # 定义优化方法：随机梯度下降 # 1e-5

    # Define loss function
    loss_fn = F.mse_loss  # 定义损失函数：均方误差损失函数

    num_epochs = 15000

    # Repeat for given number of epochs
    for epoch in range(num_epochs):
        
        # Train with batches of data
        for xb,yb in train_dl:
            
            # 1. Generate predictions
            pred = model(xb)
            
            # 2. Calculate loss
            loss = loss_fn(pred, yb)
            
            # 3. Compute gradients
            loss.backward()
            
            # 4. Update parameters using gradients
            opt.step()
            
            # 5. Reset the gradients to zero
            opt.zero_grad()
        
        # Print the progress
        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

if __name__ == "__main__":
    print( torch.cuda.is_available() )
    XOR()
    print('hi,,,')



