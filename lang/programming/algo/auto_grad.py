

import numpy as np
import torch
from torch import tensor

from torch.autograd.functional import jacobian
from torch.functional import Tensor

import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random

key = random.PRNGKey(0)


# def exp_reducer(x):
#     return x.exp() # .sum(dim=1)

# inputs =  Tensor( [ [1, 2], [3, 4] ] ) # torch.rand(2, 2)
# outputs = exp_reducer(inputs)

# ja = jacobian(exp_reducer, inputs)


w = tensor( np.random.uniform(size=(2, 2)) )   # 2*2 权重

x = tensor(
    [ [0, 0], 
      [0, 1] ]
    ) 

b = tensor( np.random.uniform(size=(2, 2)) )   # 2*2 偏置

def forword(w):

    # 前向传播 (2,2) . (2,2) = (2,2)

    a = x.dot( w ) + b

    #a = np.dot(x, w) + b 

    return a

ja = jacobian(forword, w)

print(ja)

