# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:21:23 2018

@author: zhangjuefei
"""

from book_draw_util import *


# filter
vrange = (-3, 4)
minv, maxv = vrange
mu = [0, 0]
sigma = [[1.0, 0], [0, 1.0]]
fx1 = np.arange(minv, maxv)
fx2 = np.arange(minv, maxv)
fx1, fx2 = np.meshgrid(fx1, fx2)
fx1, fx2 = fx1.flatten(), fx2.flatten()


# image 
# image
x1 = np.linspace(0, 512, endpoint=True, num=512)
x2 = np.linspace(0, 512, endpoint=True, num=512)
x1, x2 = np.meshgrid(x1, x2)
img = img_as_float(color.rgb2grey(io.imread("ping.png")))
bottom = -3
top = 2


# chart
fig = plt.figure(figsize=(20, 30), facecolor='white')

for c, d in zip(np.arange(3), [0.3, 1.2, 3.0]):
    
    sigma = [[d, 0], [0, d]]
    gaussian_filter = normal_density_2([fx1, fx2], mu, sigma).reshape(7, 7)
    x3 = convolve(img, gaussian_filter)

    ax = fig.add_subplot(3, 2, 2 * c + 1)
    ax.imshow(x3, cmap="gray")
    ax.set_title(r"$\delta^2={:.1f}$".format(d), fontsize=AXIS_LABEL_FONT_SIZE)
    
    ax = fig.add_subplot(3, 2, 2 * c + 2, projection="3d")
    ax.plot_trisurf(x1.flatten(), x2.flatten(), x3.flatten(), antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.contourf(x1, x2, x3, zdir='z', offset=bottom, cmap=plt.cm.gray, antialiased=True)
    ax.view_init(35, 60)
    ax.set_zlim((bottom, top))
    
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_title(r"$\delta^2={:.1f}$".format(d), fontsize=AXIS_LABEL_FONT_SIZE)
    
plt.savefig(os.path.join(all_pic_path, '9-10.png'), format='png')