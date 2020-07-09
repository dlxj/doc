# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:18:09 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

vrange = (-6, 6)
minv, maxv = vrange
step = 60

mus = [[0, 0], [0, 0]]
sigmas = [[[3, 2], [2, 3]], [[6, -1.2], [-1.2, 2]]]

for c, mu, sigma in zip(np.arange(2), mus, sigmas):
    ax = fig.add_subplot(1, 2, c+1, projection="3d")
    ax.clear() 
    # ax.set_title(r"$Lorenz\ Attractor$")
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$p\left(x_1,x_2\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
    
    # surface
    x1 = np.linspace(minv, maxv, endpoint=True, num=step)
    x2 = np.linspace(minv, maxv, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = normal_density_2([x1, x2], mu, sigma)
    ax.set_zlim([0, 0.08])

    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                        rstride=6, cstride=6, 
                        color="k", alpha=LIGHT_ALPHA)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=0, cmap=plt.cm.Greys, alpha=ALPHA)
    ax.set_title(r"$\delta_1^2={:.3f},\ \delta_2^2={:.3f},$".format(sigma[0][0] ** 0.5, sigma[1][1] ** 0.5) + "协方差：{:.2f}".format(sigma[0][1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '5-8.png'), format='png')