# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:06:26 2018

@author: zhangjuefei
"""

from book_draw_util import *

# sobel filter
sobelh = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
sobelv = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

x1 = np.linspace(0, 512, endpoint=True, num=512)
x2 = np.linspace(0, 512, endpoint=True, num=512)
x1, x2 = np.meshgrid(x1, x2)
img = img_as_float(color.rgb2grey(io.imread("ping.png")))
bottom = -3
top = 2


# chart
fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2)

for c, f, t in zip(np.arange(2),[sobelv, sobelh], ["纵向 Sobel 滤波器", "横向 Sobel 滤波器"]):

    x3 = np.abs(convolve(img, f))
    # x3 /= x3.max()
    
    ax = fig.add_subplot(2, 2, 2 * c + 1)
    ax.imshow(x3, cmap="gray")
    ax.set_title(t, fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

    ax = fig.add_subplot(2, 2, 2 * c + 2, projection="3d")

    ax.plot_trisurf(x1.flatten(), x2.flatten(), x3.flatten(), antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.contourf(x1, x2, x3, zdir='z', offset=bottom, cmap=plt.cm.gray, antialiased=True)
    ax.view_init(35, 60)
    ax.set_zlim((bottom, top))
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_title(t, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '9-16.png'), format='png')