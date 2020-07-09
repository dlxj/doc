# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:05:13 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
# ax.axis("off")
ax.clear()

xrange = [-20, 20]
step = 80
ax.set_xlim(xrange)
ax.set_ylim(xrange)
# ax.set_zlim([0, 6])
    
# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
# surface
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = valley([x1, x2])
tri = mtri.Triangulation(x1, x2)
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=0, cmap=plt.cm.Greys, alpha=ALPHA)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                        rstride=6, cstride=6, 
                        color="k", alpha=LIGHT_ALPHA)


# gd track
p = (15, 15)
ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
ax.text(p[0] - 1, p[1] , -36, r"$x^0$", fontsize=TEXT_FONT_SIZE)
for i in range(1000):
    g = valley_de(p)
    p2 = tuple(np.array(p) - 0.95 * np.array(g))
    ax.plot([p[0], p2[0]], [p[1], p2[1]], [0, 0],"k", linewidth=0.8)
    p = p2

ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
ax.text(p[0] - 1, p[1] , -36, r"$x^{1000}$", fontsize=TEXT_FONT_SIZE)

"""
# gradient field
g1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=10)
g2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=10)
g1, g2 = np.meshgrid(g1, g2)
g1, g2 = g1.flatten(), g2.flatten()
gf = valley_de([g1, g2])
ax.quiver(g1, g2, [0] * len(g1), -gf[0], -gf[1], [0] * len(g1), arrow_length_ratio=0.08, color="k", alpha=ALPHA)
"""
plt.savefig(os.path.join(all_pic_path, '3-13.png'), format='png')