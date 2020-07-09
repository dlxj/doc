# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:41:48 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()


ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$x_3$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")

# vector 1
v1 = (1,0,0.3)
arrow = Arrow3D([0, v1[0]],[0, v1[1]],[0, v1[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(v1[0], v1[1], v1[2], r"$X_{*,1}$", fontsize=TEXT_FONT_SIZE)


# vector 2
v2 = (0,1,0.3)
arrow = Arrow3D([0, v2[0]],[0, v2[1]],[0, v2[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(v2[0], v2[1], v2[2], r"$X_{*,2}$", fontsize=TEXT_FONT_SIZE)

# norm
n = np.cross(v1, v2)

# surface
x1 = np.linspace(-1.6, 1.6, endpoint=True, num=2)
x2 = np.linspace(-1.6, 1.6, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = -n[0] / n[2] * x1 - n[0] / n[2] * x2
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
ax.text(-2.5, 0, -2.0, "设计矩阵" + R"$X$" + "的列张成的子空间：平面", zdir=(1, 1, -0.22), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

# y
y = (0.5, 0.5, 1.5)
arrow = Arrow3D([0, y[0]],[0, y[1]],[0, y[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(y[0], y[1], y[2], r"$y$", fontsize=TEXT_FONT_SIZE)

# y hat
X = np.mat([v1, v2]).T
y_hat = tuple((X * (X.T * X).I * X.T * np.mat(y).T).A1)
arrow = Arrow3D([0, y_hat[0]],[0, y_hat[1]],[0, y_hat[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(y_hat[0], y_hat[1], y_hat[2], r"$\hat{y}$", fontsize=TEXT_FONT_SIZE)
ax.plot([y[0], y_hat[0]], [y[1], y_hat[1]], [y[2], y_hat[2]], "k--", alpha=ALPHA)

plt.savefig(os.path.join(all_pic_path, '5-10.png'), format='png')