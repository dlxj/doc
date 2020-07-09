# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 20:18:41 2018

@author: zhangjuefei
"""

from book_draw_util import *


# gaussian filter
vrange = (-2, 3)
minv, maxv = vrange
mu = [0, 0]
sigma = [[1.0, 0], [0, 1.0]]
x1 = np.arange(minv, maxv)
x2 = np.arange(minv, maxv)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
gaussian_filter = normal_density_2([x1, x2], mu, sigma).reshape(5, 5)


# image
x1 = np.linspace(0, 512, endpoint=True, num=512)
x2 = np.linspace(0, 512, endpoint=True, num=512)
x1, x2 = np.meshgrid(x1, x2)
img = img_as_float(color.rgb2grey(io.imread("ping.png")))
x3 = convolve(img, gaussian_filter)
bottom = -3
top = 2


# chart
fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')
ax = fig.add_subplot(1, 2, 1)
ax.imshow(x3, cmap="gray")

ax = fig.add_subplot(1, 2, 2, projection="3d")
ax.plot_trisurf(x1.flatten(), x2.flatten(), x3.flatten(), antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.gray_r)
ax.contourf(x1, x2, x3, zdir='z', offset=bottom, cmap=plt.cm.gray, antialiased=True)
ax.view_init(35, 60)
ax.set_zlim((bottom, top))
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '9-8.png'), format='png')