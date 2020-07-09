# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 14:33:52 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.axis("off")
ax.grid(False)
ax.clear()

np.random.seed(5)
xrange = [-6, 6]
step = 1
minx, maxx = xrange
e = int((maxx - minx) / step + 1)
# ax.set_xlim(xrange)

def fun(p):
    x1, x2 = p
    return 0.1 * (np.sin(x1) + np.sin(x2))


x1 = np.arange(minx, maxx + 1, step)
x2 = np.arange(minx, maxx + 1, step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = fun([x1, x2])
bottom = np.min(x3)
ax.set_zlim([bottom, 3])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.scatter(x1, x2, x3, s=POINT_SIZE, c="k", alpha=ALPHA)
# ax.contourf(x1.reshape(e, e), x2.reshape(e, e), x3.reshape(e, e), zdir='z', offset=0, cmap=plt.cm.Greys, alpha=ALPHA)
# ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="k")


point = [2, 2]
step_t = 40
span = 2
t1 = np.linspace(point[0]-span, point[0] + span, endpoint=True, num=step_t)
t2 = np.linspace(point[1]-span, point[1] + span, endpoint=True, num=step_t)
t1, t2 = np.meshgrid(t1, t2)
t1, t2 = t1.flatten(), t2.flatten()
t3 = normal_density_2([t1, t2], point, [[0.6, 0], [0, 0.6]]) + 2
ax.plot_trisurf(t1, t2, t3, antialiased=True, alpha=ALPHA, cmap=plt.cm.Greys)

p1 = np.arange(point[0] - span, point[0] + span + 1)
p2 = np.arange(point[1] - span, point[1] + span + 1)
p1, p2 = np.meshgrid(p1, p2)
p1, p2 = p1.flatten(), p2.flatten()
p3 = normal_density_2([p1, p2], point, [[0.6, 0], [0, 0.6]]) + 2

ax.scatter(p1, p2, p3, s=POINT_SIZE, color="k", facecolor="none")

ax.plot([1, 1], [1, 1], [fun([1, 1]), normal_density_2([[1], [1]], point, [[0.6, 0], [0, 0.6]]) + 2], "k--", alpha=ALPHA)

ax.text(-3, 0, 1.0, r"$f\left(1,1\right)\times g\left(x^*_1-1, x^*_2-1\right)$", fontsize=TEXT_FONT_SIZE)
ax.text(1.8, 2, -0.2, r"$x^*$", fontsize=TEXT_FONT_SIZE)
ax.scatter(2, 2, 0, s=POINT_SIZE * 2, c="k")

ax.text(-2, 1, -0.5, r"$\left(x^*_1-1,x^*_2-1\right)$", fontsize=TEXT_FONT_SIZE)
ax.scatter(1, 1, 0, s=POINT_SIZE * 2, c="k")

ax.text(-1.5, 2, 2.4, "翻转(且被抬高)的 " + r"$f$" + " 图像", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
ax.set_title(r"$f*g\left(x^*\right)=\Sigma_{t\in R^2}f\left(t\right)\times g\left(x^*-t\right)$")


plt.savefig(os.path.join(all_pic_path, '9-7.png'), format='png')