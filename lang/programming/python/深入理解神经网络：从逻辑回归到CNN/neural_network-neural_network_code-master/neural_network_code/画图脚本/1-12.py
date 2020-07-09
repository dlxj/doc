# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:44:44 2018

@author: zhangjuefei
"""

from book_draw_util import *

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

w = (1.5, 1.5)
w /= np.linalg.norm(w)
def f(x1, x2):
    global w
    return 1 / (1 + np.e ** -(w[0] * x1 + w[1] * x2))

arrow = Arrow3D([0,w[0]],[0,w[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w[0], w[1], 0.05, r"$w$", fontsize=TEXT_FONT_SIZE)
ax.plot((-6, 6), (-6, 6), (0, 0), "k--", alpha=ALPHA)


arrow = Arrow3D([0,4],[0,0],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(4.1, 0, 0, r"$x_a$", fontsize=TEXT_FONT_SIZE)
ax.plot((6.5, -1.5), (-2.5, 5.5), (0, 0), "k--", alpha=ALPHA)

arrow = Arrow3D([0,6],[0,-2],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(5.9, -1.9, 0, r"$x_b$", fontsize=TEXT_FONT_SIZE)

ax.text(2, 2, 1.1 * f(2, 2), r"$y=\frac{1}{1+\mathrm{e}^{-w^\mathrm{T}x}}$", fontsize=TEXT_FONT_SIZE)

x1 = np.linspace(-6, 6, endpoint=True, num=40)
x2 = np.linspace(-6, 6, endpoint=True, num=40)
x3 = f(x1, x2)
ax.plot(x1, x2, x3, "k", alpha=ALPHA)

x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = f(x1, x2)
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")
ax.scatter(2, 2,0 , s=POINT_SIZE, c="k")
ax.scatter(2, 2, f(2, 2) , s=POINT_SIZE, c="k")
ax.plot(np.linspace(2, 2, endpoint=True, num=40)
, np.linspace(2, 2, endpoint=True, num=40), np.linspace(0, f(2, 2), endpoint=True, num=40), "k--", alpha=ALPHA)

plt.savefig(os.path.join(all_pic_path, '1-12.png'), format='png', dpi=600) 