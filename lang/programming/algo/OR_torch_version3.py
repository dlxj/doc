import torch
import torch.nn as nn
import torch.optim as optim


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = torch.nn.Linear(2, 8)
        self.fc2 = torch.nn.Linear(8, 8)
        self.fc3 = torch.nn.Linear(8, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.sigmoid(x)
        return x


def main():

    import numpy as np
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    num_epochs = 10000

    # convert numpy array to tensor
    x_tensor = torch.from_numpy(x).float()
    y_tensor = torch.from_numpy(y).float()

    # crate instance
    net = Net()

    # set training mode
    net.train()

    # set training parameters
    optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
    criterion = torch.nn.MSELoss()

    # start to train
    epoch_loss = []
    for epoch in range(num_epochs):
        print(epoch)
        # forward
        outputs = net(x_tensor)

        # calculate loss
        loss = criterion(outputs, y_tensor)

        # update weights
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # save loss of this epoch
        epoch_loss.append(loss.data.numpy().tolist())

    print(net(torch.from_numpy(np.array([[0, 0]])).float()))
    print(net(torch.from_numpy(np.array([[1, 0]])).float()))
    print(net(torch.from_numpy(np.array([[0, 1]])).float()))
    print(net(torch.from_numpy(np.array([[1, 1]])).float()))

if __name__ == "__main__":
    main()