# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:54:14 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-6, 6], emit=False)
ax.set_ylim([-6, 6])
# ax.set_zlim([0, 1])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

def f(x1, x2):
    global w
    return 0.02 * (w[0] * x1 + w[1] * x2) ** 2

w = (1.5, 1.5)
w /= np.linalg.norm(w)
arrow = Arrow3D([0, w[0]],[0, w[1]],[0,0], arrowstyle="-|>", lw=1, mutation_scale=10, color="black")
ax.add_artist(arrow)
ax.text(w[0], w[1], 0.05, r"$w$", fontsize=TEXT_FONT_SIZE)
ax.plot((-6, 6), (-6, 6), (0, 0), "k--", alpha=ALPHA)

arrow = Arrow3D([0,4],[0,0],[0,0], arrowstyle="-|>", lw=1, mutation_scale=10, color="black")
ax.add_artist(arrow)
ax.text(4.1, 0, 0, r"$x_a$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,6],[0,-2],[0,0], arrowstyle="-|>", lw=1, mutation_scale=10, color="black")
ax.add_artist(arrow)
ax.text(5.9, -1.9, 0, r"$x_b$", fontsize=TEXT_FONT_SIZE)

ax.plot((6.5, -1.5), (-2.5, 5.5), (0, 0), "k--", alpha=ALPHA)

ax.text(2, 2, 1.5 * f(2,2), r"$f\left(x\right)=0.02\times\left(w^\mathrm{T}x\right)^2$", fontsize=TEXT_FONT_SIZE)

x1 = np.linspace(-6, 6, endpoint=True, num=40)
x2 = np.linspace(-6, 6, endpoint=True, num=40)
x3 = f(x1, x2)
ax.plot(x1, x2, x3, "k", alpha=ALPHA)

x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = f(x1, x2)
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

ax.scatter(0, 0, 0, s=SMALL_POINT_SIZE, c="k")
ax.scatter(2, 2,0 , s=SMALL_POINT_SIZE, c="k")
ax.scatter(2, 2,f(2, 2) , s=SMALL_POINT_SIZE, c="k")
ax.plot(np.linspace(2, 2, endpoint=True, num=40)
, np.linspace(2, 2, endpoint=True, num=40), np.linspace(0, f(2, 2), endpoint=True, num=40), "k--", alpha=ALPHA)

points = np.random.multivariate_normal((3,3), [[0.3,0],[0,0.3]], 20)
ax.scatter(points[:,0],points[:,1],[0] * 20,  color="k", s=BIG_POINT_SIZE)

points = np.random.multivariate_normal((-3,3), [[0.3,0],[0,0.3]], 20)
ax.scatter(points[:,0],points[:,1],[0] * 20,  color="k", facecolors="none",  s=BIG_POINT_SIZE)

points = np.random.multivariate_normal((3,-3), [[0.3,0],[0,0.3]], 20)
ax.scatter(points[:,0],points[:,1],[0] * 20,  color="k", facecolors="none",  s=BIG_POINT_SIZE)

points = np.random.multivariate_normal((-3,-3), [[0.3,0],[0,0.3]], 20)
ax.scatter(points[:,0],points[:,1],[0] * 20,  color="k", s=BIG_POINT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-14.png'), format='png', dpi=600) 