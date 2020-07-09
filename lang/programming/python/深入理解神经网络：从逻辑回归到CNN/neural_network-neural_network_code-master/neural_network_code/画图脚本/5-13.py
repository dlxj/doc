# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:22:00 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

xrange = [-0.5, 1.5]
step = 80
g_step = 20
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()

l = 0.15
def l1_q(p):
    return .05 * (p[0] - 0.5) ** 2 + .1 * (p[1] - 1)**2 + l * (np.abs(p[0]) + np.abs(p[1]))

def l2_q(p):
    return .05 * (p[0] - 0.5) ** 2 + .1 * (p[1] - 1)**2 + l * (np.abs(p[0]) ** 2 + np.abs(p[1]) ** 2)

fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

T = "\mathrm{T}"
funs = [l1_q, l2_q]
titles = ["带" + r"$L_1$" + "正则项的二次函数", "带" + r"$L_2$" + "正则项的二次函数"]
for c, fun, title in zip(np.arange(len(funs)), funs, titles):
    ax = fig.add_subplot(1, 2, c+1, projection="3d")
    ax.clear() 

    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
    x3 = fun([x1, x2]) 
    bottom = np.min(x3)

    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step, -1), x2.reshape(step, -1), x3.reshape(step, -1), 
                   rstride=8, cstride=8, 
                   color="k", alpha=LIGHT_ALPHA)

    # contour
    ax.contourf(x1.reshape(step, -1), x2.reshape(step, -1), x3.reshape(step, -1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)

    # minima
    p = fmin(fun, (2, -2))
    ax.scatter(p[0], p[1], bottom, c="k", s=BIG_POINT_SIZE)
    ax.text(p[0] - 0.25, p[1], bottom - 0.1, "全局最小点：" + r"$\left({:.2f},{:.2f}\right)^{:s}$".format(p[0], p[1], T), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

    ax.set_title(title, fontsize=AXIS_LABEL_FONT_SIZE, fontproperties=myfont)
    ax.set_zlim([bottom, 0.8])
    
plt.savefig(os.path.join(all_pic_path, '5-13.png'), format='png')