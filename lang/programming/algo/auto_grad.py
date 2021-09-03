

import numpy as np
import torch

from torch.autograd.functional import jacobian


def exp_reducer(x):
    return x.exp().sum(dim=1)

inputs = torch.rand(2, 2)
jacobian(exp_reducer, inputs)

print(1)

