# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:47:39 2018

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

w = np.array([2, -0.2, 2])
wws = [np.array([0, 0, 1]), np.array([2, 0, 0]), np.array([2.3, -2.3, 1])]
b = -4

def plane(x1, x2):
    global w, b
    return(-b - w[0] * x1 -w[1] * x2) / w[2]
    
arrow = Arrow3D([0, w[0]],[0, w[1]],[0, w[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
T = "\mathrm{T}"
ax.text(w[0] - 1, w[1], w[2] - 0.2, r"$w=\left({:.1f},{:.1f},{:.1f}\right)^{:s}$".format(w[0], w[1], w[2], T), fontsize=TEXT_FONT_SIZE)


x1 = np.linspace(-.4, 2, endpoint=True, num=2)
x2 = np.linspace(-2, 1.5, endpoint=True, num=2)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = plane(x1, x2)
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=ALPHA, color="black")


for idx, ww in zip(np.arange(len(wws)), wws):
    arrow = Arrow3D([0, ww[0]],[0, ww[1]],[0, ww[2]], arrowstyle="-|>", lw=1, mutation_scale=10, color="black")
    ax.add_artist(arrow)
    
    wwp = np.inner(ww, w) * w / np.linalg.norm(w) ** 2
    ax.text(ww[0], ww[1], ww[2], ("正侧" if np.inner(ww, w) > -b else "负侧" if np.inner(ww, w) < -b else "在平面上"), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
    ax.scatter(wwp[0], wwp[1], wwp[2], s=POINT_SIZE, c="k")
    ax.plot((ww[0], wwp[0]), (ww[1], wwp[1]), (ww[2], wwp[2]), "k--", alpha=ALPHA)


ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")
ax.text(0, 0, 2, "平面：" + r"$\frac{w^\mathrm{T}x}{||w||}=-\frac{b}{||w||}$", fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '2-3.png'), format='png')