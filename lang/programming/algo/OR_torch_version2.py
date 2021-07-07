import torch as pt
from torch.nn.functional import mse_loss
pt.manual_seed(33);

model = pt.nn.Sequential(
    pt.nn.Linear(2, 5),
    pt.nn.ReLU(),
    pt.nn.Linear(5, 1)
)

X = pt.tensor([[0, 0],
               [0, 1],
               [1, 0],
               [1, 1]], dtype=pt.float32)

y = pt.tensor([0, 1, 1, 0], dtype=pt.float32).reshape(X.shape[0], 1)

EPOCHS = 100

optimizer = pt.optim.Adam(model.parameters(), lr = 0.03)

for epoch in range(EPOCHS):
  #forward
  y_est = model(X)
  
  #compute mean squared error loss
  loss = mse_loss(y_est, y)

  #backprop the loss gradients
  loss.backward()

  #update the model weights using the gradients
  optimizer.step()

  #empty the gradients for the next iteration
  optimizer.zero_grad()

  
