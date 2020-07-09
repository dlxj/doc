# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:06:15 2018

@author: zhangjuefei
"""


from book_draw_util import *
from scipy.optimize import fmin

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.axis("off")
ax.grid(False)
ax.clear()

xrange = [-4, 4]
ax.set_xlim(xrange)
ax.set_ylim(xrange)
ax.set_zlim([0, 3])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

x1 = np.linspace(-4, 4, endpoint=True, num=80)
x2 = np.linspace(-4, 4, endpoint=True, num=80)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = csurface([x1, x2])
tri = mtri.Triangulation(x1, x2)
# cmap=plt.cm.Greys
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
ax.contourf(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), zdir='z', offset=-0.1, cmap=plt.cm.Greys, alpha=ALPHA)
ax.plot_wireframe(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), 
                   rstride=8, cstride=8, 
                   color="k", alpha=LIGHT_ALPHA)

T = "\mathrm{T}"
# stationary points
for t, sp in zip(["局部极小点", "全局最小点"], [(-2,-2),(2,-2)]):
    p = fmin(csurface, sp)
    fp = csurface(p)
    ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
    ax.scatter(p[0], p[1], csurface(p), s=BIG_POINT_SIZE, c="k")
    ax.plot([p[0], p[0]], [p[1], p[1]], (0, fp), "k--", alpha=ALPHA)
    ax.text(p[0] - 1, p[1], 0.05, t, fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    ax.text(p[0] - 0.6, p[1], -0.35, r"$\left({:.0f}, {:.0f}\right)^{:s}$".format(p[0], p[1], T), fontsize=TEXT_FONT_SIZE)


def csurface_reverse(p):
    return - csurface(p)

for t, sp in zip(["全局最大点", "局部极大点"], [(-2,2),(2,2)]):
    p = fmin(csurface_reverse, sp)
    fp = csurface(p)
    ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
    ax.scatter(p[0], p[1], csurface(p), s=BIG_POINT_SIZE, c="k")
    ax.plot([p[0], p[0]], [p[1], p[1]], (0, fp), "k--", alpha=ALPHA)
    ax.text(p[0] - 1, p[1], 0.05, t, fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    ax.text(p[0] - 0.6, p[1], -0.35, r"$\left({:.0f}, {:.0f}\right)^{:s}$".format(p[0], p[1], T), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '3-7.png'), format='png')