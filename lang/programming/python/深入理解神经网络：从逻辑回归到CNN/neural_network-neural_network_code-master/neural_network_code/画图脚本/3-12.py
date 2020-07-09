# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:51:57 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
# ax.set_zlim([0, 1])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

xrange = (-6, 6)
step = 80
w = (1.5, 1.5)
alpha = 2
s = 0.01

def f(p):
    x1, x2 = p[0], p[1]
    global w, alpha
    return s * (x1**2+x2**2) + 1 / (1 + np.e ** - (alpha * (w[0] * x1 + w[1] * x2)))

def g(p):
    x1, x2 = p[0], p[1]
    global w, alpha
    return 2*s*x1 + alpha * w[0] * np.e ** - (alpha * (w[0] * x1 + w[1] * x2)) / (1 + np.e ** - (alpha * (w[0] * x1 + w[1] * x2))) ** 2,  2*s*x2 + alpha * w[0] * np.e ** - (alpha * (w[0] * x1 + w[1] * x2)) / (1 + np.e ** - (alpha * (w[0] * x1 + w[1] * x2))) ** 2



x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = f([x1, x2])
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=0, cmap=plt.cm.Greys, alpha=ALPHA)

p_start = [-4, -2]
p = fmin(f, p_start)
ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
ax.text(p[0] - 0.8, p[1], -0.18, r"极小点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)


x0 = (-1.6, 1.6)
g0 = g(x0)
ax.scatter(x0[0], x0[1], 0, s=BIG_POINT_SIZE, c="k")
ax.text(x0[0], x0[1], -0.1, r"$x^0$", fontsize=TEXT_FONT_SIZE)
arrow = Arrow3D([x0[0], x0[0] - g0[0]],[x0[1], x0[1] - g0[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(x0[0] - g0[0] - 0.2, x0[1] - g0[1], 0.04, r"$-\triangledown f$", fontsize=TEXT_FONT_SIZE)

# gd track
p = x0
tr1 = [p[0]]
tr2 = [p[1]]
for i in range(100000):
    gradient = g(p)
    p2 = tuple(np.array(p) - 4 * np.array(gradient))
    tr1.append(p2[0])
    tr2.append(p2[1])
    p = p2

ax.plot(tr1, tr2, [0] * len(tr1), "k", linewidth=0.8)\

"""
# gradient field
g1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=25)
g2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=25)
g1, g2 = np.meshgrid(g1, g2)
g1, g2 = g1.flatten(), g2.flatten()
gf = g([g1, g2])
ax.quiver(g1, g2, [0] * len(g1), -gf[0], -gf[1], [0] * len(g1), arrow_length_ratio=0.08, color="k", alpha=ALPHA)
"""

plt.savefig(os.path.join(all_pic_path, '3-12.png'), format='png')


