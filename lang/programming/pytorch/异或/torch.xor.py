import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


EPOCHS_TO_TRAIN = 50000


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, 3, True)   # (1*2) . (2*3) = (1*3)
        self.fc2 = nn.Linear(3, 1, True)   # (1*3) . (3*1) = (1*1)

    def forward(self, x):
        # x = F.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return x

net = Net()
inputs = list(map(lambda s: (torch.Tensor([s])), [  # Variable  # Variable 是可以自动微分的 Tensor，Varibale 默认不求梯度 # doc\lang\programming\pytorch summary.md
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]))
targets = list(map(lambda s: (torch.Tensor([s])), [  # Variable
    [0],
    [1],
    [1],
    [0]
]))


criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

print("Training loop:")
for idx in range(0, EPOCHS_TO_TRAIN):
    for input, target in zip(inputs, targets):
        optimizer.zero_grad()   # zero the gradient buffers
        output = net(input)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()    # Does the update
    if idx % 500 == 0:
        print("Epoch {: >8} Loss: {}".format(idx, loss.data.numpy()))



print("")
print("Final results:")
for input, target in zip(inputs, targets):
    output = net(input)
    print("Input:[{},{}] Target:[{}] Predicted:[{}] Error:[{}]".format(
        int(input.data.numpy()[0][0]),
        int(input.data.numpy()[0][1]),
        int(target.data.numpy()[0]),
        round(float(output.data.numpy()[0]), 4),
        round(float(abs(target.data.numpy()[0] - output.data.numpy()[0])), 4)
    ))
