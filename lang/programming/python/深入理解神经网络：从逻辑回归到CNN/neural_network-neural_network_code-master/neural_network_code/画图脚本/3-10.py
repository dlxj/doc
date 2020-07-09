# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:04:05 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.axis("off")
ax.grid(False)
ax.clear()

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 6])

ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

# surface
x1 = np.linspace(-3, 3, endpoint=True, num=40)
x2 = np.linspace(-3, 3, endpoint=True, num=40)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = single_peak_2d([x1, x2])
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
ax.plot_wireframe(x1.reshape(40,-1), x2.reshape(40,-1), x3.reshape(40,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)

# point
p = (0.5, 0)
ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
ax.scatter(p[0], p[1], single_peak_2d(p), s=BIG_POINT_SIZE, c="k")
fp = single_peak_2d(p)
ax.plot((p[0], p[0]), (p[1], p[1]), (0, fp), "k--", alpha=ALPHA)
ax.text(p[0], p[1] , -0.3, r"$x$", fontsize=TEXT_FONT_SIZE)


# gradient
g = single_peak_2d_de(p)
arrow = Arrow3D([p[0],p[0] - g[0]],[p[1],p[1] - g[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(p[0] - g[0], p[1] - g[1], 0-0.1, r"$-\triangledown f$".format(g[0], g[1]), fontsize=TEXT_FONT_SIZE)

# Force
n = (p[0] - g[0], p[1] - g[1], fp+1)
arrow = Arrow3D([p[0],n[0]],[p[1], n[1]],[fp, n[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(n[0], n[1], n[2], r"$F=\left(-\triangledown f^\mathrm{T},1\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

# support
arrow = Arrow3D([p[0],p[0]],[p[1], n[1]],[fp, n[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(p[0] - 0.2, p[1], n[2], r"$m\mathrm{g}$", fontsize=TEXT_FONT_SIZE)

# push
arrow = Arrow3D([p[0],n[0]],[p[1], n[1]],[fp, fp], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(n[0], n[1], fp, r"$\frac{m\mathrm{g}}{\mathrm{tan}\theta}$", fontsize=TEXT_FONT_SIZE)
ax.text(n[0], n[1], fp, r"$\frac{m\mathrm{g}}{\mathrm{tan}\theta}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '3-10.png'), format='png')