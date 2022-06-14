from __future__ import print_function
import random
import itertools

import jax
import jax.numpy as np
# Current convention is to import original numpy as "onp"
import numpy as onp



# Sigmoid nonlinearity
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Computes our network's output
def net(params, x):
    w1, b1, w2, b2 = params
    hidden = np.tanh(np.dot(w1, x) + b1)
    return sigmoid(np.dot(w2, hidden) + b2)

# Cross-entropy loss
def loss(params, x, y):
    out = net(params, x)
    cross_entropy = -y * np.log(out) - (1 - y)*np.log(1 - out)
    return cross_entropy

# Utility function for testing whether the net produces the correct
# output for all possible inputs
def test_all_inputs(inputs, params):
    predictions = [int(net(params, inp) > 0.5) for inp in inputs]
    for inp, out in zip(inputs, predictions):
        print(inp, '->', out)
    return (predictions == [onp.bitwise_xor(*inp) for inp in inputs])



def initial_params():
    return [
        onp.random.randn(3, 2),  # w1
        onp.random.randn(3),  # b1
        onp.random.randn(3),  # w2
        onp.random.randn(),  #b2
    ]

loss_grad = jax.grad(loss)

# Stochastic gradient descent learning rate
learning_rate = 1.
# All possible inputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Initialize parameters randomly
params = initial_params()

for n in itertools.count():
    # Grab a single random input
    x = inputs[onp.random.choice(inputs.shape[0])]
    # Compute the target output
    y = onp.bitwise_xor(*x)
    # Get the gradient of the loss for this input/output pair
    grads = loss_grad(params, x, y)
    # Update parameters via gradient descent
    params = [param - learning_rate * grad
              for param, grad in zip(params, grads)]
    # Every 100 iterations, check whether we've solved XOR
    if not n % 100:
        print('Iteration {}'.format(n))
        if test_all_inputs(inputs, params):
            break