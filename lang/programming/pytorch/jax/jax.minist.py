
# https://docs.python.org/3/library/array.html

import imp
import jax
import jax.numpy as jnp
import jax.random as jr
import numpy as onp

import flax.linen as nn

import gzip
import struct

import array

import matplotlib.pyplot as plt
import cv2

X = jnp.array([
               [[0, 0]],  # (1*2) 的输入  
               [[0, 1]],
               [[1, 0]],
               [[1, 1]]
             ], jnp.float32)

Y = jnp.array([
                [[0]],    # (1*1) 的输出
                [[1]],
                [[1]],
                [[0]]
             ], jnp.float32)

def mnist(fname):
    with gzip.open(fname, "rb") as fh:
        _, batch, rows, cols = struct.unpack(">IIII", fh.read(16))
        shape = (batch, 1, rows, cols)
        return jnp.array(array.array("B", fh.read()), dtype=jnp.uint8).reshape(shape)


class CNN(nn.Module):
    @nn.compact
    def __call__(self, x):
        x = nn.Dense(features=2)(x)
        x = nn.sigmoid(x)
        return x

model = CNN()

batch = X  # (N, H, W, C) format
variables = model.init(jax.random.PRNGKey(0), batch)
output = model.apply(variables, batch)

def main():
    fname = 'train-images-idx3-ubyte.gz'
    data = mnist(fname)
    data_mean = jnp.mean(data)
    data_std = jnp.std(data)
    data_max = jnp.max(data)
    data_min = jnp.min(data)
    data_shape = data.shape[1:]
    # data = (data - data_mean) / data_std

    img = data[0][0].__array__()  # jax 数组转 numpy 数组

    # plt.imshow(img)
    # plt.show()

    img2 = cv2.resize(img, (800, 800), cv2.INTER_NEAREST)  # 放大一百倍，原来的图太小了
    cv2.imshow("result", img2)
    cv2.waitKey(0)

    cv2.imwrite('img.jpg', img)

    print('hi,,')

main()




