
# https://docs.python.org/3/library/array.html

import jax
import jax.numpy as jnp
import jax.random as jr

import gzip
import struct

import array

def mnist(fname):
    with gzip.open(fname, "rb") as fh:
        _, batch, rows, cols = struct.unpack(">IIII", fh.read(16))
        shape = (batch, 1, rows, cols)
        return jnp.array(array.array("B", fh.read()), dtype=jnp.uint8).reshape(shape)


def main():
    fname = 'train-images-idx3-ubyte.gz'
    data = mnist(fname)
    data_mean = jnp.mean(data)
    data_std = jnp.std(data)
    data_max = jnp.max(data)
    data_min = jnp.min(data)
    data_shape = data.shape[1:]
    data = (data - data_mean) / data_std

    print('hi,,')

main()




