# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:06:36 2018

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

arrow = Arrow3D([0,3],[0,-1.5],[0,3], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(3, -1.5, 3, r"$w$", fontsize=TEXT_FONT_SIZE)


x1 = np.linspace(-0.6, 2, endpoint=True, num=2)
x2 = np.linspace(-2, 0.8, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = 2 - x1 + 0.5 * x2
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")


arrow = Arrow3D([0,0],[0,0],[0,2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 0, 2, r"$x_a$", fontsize=TEXT_FONT_SIZE)
ax.text(-0.05, 0.2, 0.1, r"$\theta_a$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,2],[0,0],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(2, 0, 0, r"$x_b$", fontsize=TEXT_FONT_SIZE)
ax.text(0.2, 0, .05, r"$\theta_b$", fontsize=TEXT_FONT_SIZE)

arrow = Arrow3D([0,0],[0,2],[0,1], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(0, 2, 1, r"$x_c$", fontsize=TEXT_FONT_SIZE)
ax.text(0, 0.6, 0.12, r"$\theta_c$", fontsize=TEXT_FONT_SIZE)


ax.plot((8/7, 0), (-4/7, 0), (8/7, 2), "k--", alpha=ALPHA)
ax.plot((8/7, 2), (-4/7, 0), (8/7, 0), "k--", alpha=ALPHA)
ax.plot((8/7, 0), (-4/7, 2), (8/7, 1), "k--", alpha=ALPHA)
ax.scatter(8/7, -4/7, 8/7, s=POINT_SIZE, c="k")
ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")

ax.set_title(r"$||x_a||\mathrm{cos}\theta_a=||x_b||\mathrm{cos}\theta_b=||x_c||\mathrm{cos}\theta_c=\frac{x_a^\mathrm{T}w}{||w||}=\frac{x_b^\mathrm{T}w}{||w||}=\frac{x_c^\mathrm{T}w}{||w||}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-10.png'), format='png', dpi=600) 