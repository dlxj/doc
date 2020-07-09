# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:56:29 2018

@author: zhangjuefei
"""

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.axisartist as axisartist
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.axis3d import Axis
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
import matplotlib.tri as mtri
import  matplotlib.font_manager as fm
import seaborn as sns
from skimage import data, img_as_float, color
from skimage import io
from scipy.ndimage.filters import convolve
myfont=fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=16)
timesfont=fm.FontProperties(fname="C:\Windows\Fonts\Times New Roman\times.ttc", size=16)

all_pic_path = "D:/develop/project/book/neural_network_book/图片/高品质图片"

plt.rcParams["savefig.dpi"] = 600

SQUARE_FIG_SIZE = (10 ,10)
RECTANGLE_FIG_SIZE = (10, 6)
TWO_FIG_SIZE = (20, 10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
LEGEND_FONT_SIZE = 14
ARROW_HEAD_WIDTH = 0.12
ALPHA = 0.3
DARK_ALPHA = 0.7
LIGHT_ALPHA = 0.1
POINT_SIZE = 12
BIG_POINT_SIZE = 30
SMALL_POINT_SIZE = 8

params = {'axes.labelsize': AXIS_LABEL_FONT_SIZE,'axes.titlesize':AXIS_LABEL_FONT_SIZE, 'legend.fontsize': LEGEND_FONT_SIZE}
matplotlib.rcParams.update(params)

# np.random.seed(66)
logistic = np.vectorize(lambda x: 1 / (1 + np.e ** (-x)))

def csurface(p):
    x1, x2 = p[0], p[1]
    return 2 + 1 / np.e ** ((x1 + 2) ** 2 + (x2 - 2) ** 2) - 1 / np.e ** ((x1 - 2) ** 2 + (x2 + 2) ** 2) - 0.5 / np.e ** ((x1 + 2) ** 2 + (x2 + 2) ** 2) + 0.5 / np.e ** ((x1 - 2) ** 2 + (x2 - 2) ** 2)

def csurface_2peaks(p):
    x1, x2 = p[0], p[1]
    d = 4
    dn1 = np.e ** (((x1 + 2) / d) ** 2 + ((x2 - 2) / d) ** 2)
    dn2 = np.e ** (((x1 - 2) / d) ** 2 + ((x2 + 2) / d) ** 2)
    return 2 - 0.02 * x1 + 0.02 * x2 + 1 / dn1 - 0.5 / dn2

def csurface_2peaks_de(p):
    x1, x2 = p[0], p[1]
    d = 4
    dn1 = np.e ** (((x1 + 2) / d) ** 2 + ((x2 - 2) / d) ** 2)
    dn2 = np.e ** (((x1 - 2) / d) ** 2 + ((x2 + 2) / d) ** 2)
    return  -0.02 - 2 * (x1 + 2) / (d**2 * dn1) + (x1 - 2) / (d**2 * dn2),  0.02 - 2 * (x2 - 2) / (d**2 * dn1) +  (x2 + 2) / (d**2 * dn2)


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

def plane(x, p, b, g):
    x = np.mat(x)
    p = np.mat(p).T
    g = np.mat(g)
    return np.array(b + np.matmul(p - x, g.T)).flatten()

def non_convex_fun_1d(x):
    
    return 0.5 + 1 / np.e ** (((x - 2)) ** 2) + 0.5 / np.e ** (((x + 2) / 2) ** 2)

def non_convex_fun_1d_de(x):
    
    return - 2 * (x - 2) / np.e ** (((x - 2)) ** 2) - (x + 2)  / (4 * np.e ** (((x + 2) / 2) ** 2))

def single_peak_2d(p):
    x1, x2 = p[0], p[1]
    return 3 / np.e ** (((x1) ** 2 + (x2) ** 2) / 2)

def single_peak_2d_de(p):
    x1, x2 = p[0], p[1]
    return - 3 * (x1) / np.e ** (((x1) ** 2 + (x2) ** 2) / 2), - 3 * (x2) / np.e ** (((x1) ** 2 + (x2) ** 2) / 2)


def saddle(x1, x2):
    return x1 ** 2 - 0.6 * x2 ** 2


v1 = 1
v2 = 0.1
m = 0.01
def valley(p):
    x1, x2 = p[0], p[1]
    return v1 * x1 ** 2 + v2 * x2 ** 2 - m * x1 * x2

def valley_de(p):
    x1, x2 = p[0], p[1]
    return 2 * v1 * x1- m * x2, 2 * v2 * x2 - m * x1

slope = 0.0001
def plateau(p):
    x1, x2 = p[0], p[1]
    return 0.5 + slope * x1 ** 2 + slope / 2 * x2 ** 2

def plateau_de(p):
    x1, x2 = p[0], p[1]
    return 2 * slope * x1, slope * x2


def normal_density(x, mu, delta):
    return 1 / ((2 * np.pi) ** 0.5 * delta) * np.e ** (-(x - mu) ** 2 / (2 * delta ** 2))

def normal_density_2(x, mu, sigma):
    x = np.mat(x)
    n = x.shape[0]
    mu = np.mat(mu).T
    sigma = np.mat(sigma)
    
    return 1 / ((2 * np.pi) ** (n / 2) * np.linalg.det(sigma) ** 0.5) * np.e ** np.diag((-(x - mu).T * sigma.I * (x-mu) / 2))

def logistic_map(r, x):
    return r * x * (1 - x)