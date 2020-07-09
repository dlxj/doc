# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:41:53 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.axis("off")
ax.grid(False)
ax.clear()

xrange = [-8, 8]
ax.set_xlim(xrange)
ax.set_ylim(xrange)
ax.set_zlim([0, 3])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=80)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=80)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = csurface_2peaks([x1, x2])
bottom = 0
tri = mtri.Triangulation(x1, x2)
# cmap=plt.cm.Greys
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
ax.contourf(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)
ax.plot_wireframe(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), 
                   rstride=8, cstride=8, 
                   color="k", alpha=LIGHT_ALPHA)

# gradient field
g1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=30)
g2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=30)
g1, g2 = np.meshgrid(g1, g2)
g1, g2 = g1.flatten(), g2.flatten()
gf = csurface_2peaks_de([g1, g2])
ax.quiver(g1, g2, [0] * len(g1), -gf[0], -gf[1], [0] * len(g1), arrow_length_ratio=0.08, color="k", alpha=ALPHA)


p = fmin(csurface_2peaks, (2, -2))
fp =  csurface_2peaks(p)
ax.scatter(p[0], p[1], 0, color="k", s=BIG_POINT_SIZE)
ax.scatter(p[0], p[1], fp, color="k", s=BIG_POINT_SIZE)
ax.plot([p[0],p[0]], [p[1],p[1]], [0, fp], "k--", alpha=ALPHA)
ax.text(p[0] - 2.6, p[1], 0.02, "驻点：局部极小点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
def csurface_2peaks_reverse(p):
    return -csurface_2peaks(p)

p = fmin(csurface_2peaks_reverse, (-2, 2))
fp =  csurface_2peaks(p)
ax.scatter(p[0], p[1], 0, color="k", s=BIG_POINT_SIZE)
ax.scatter(p[0], p[1], fp, color="k", s=BIG_POINT_SIZE)
ax.plot([p[0],p[0]], [p[1],p[1]], [0, fp], "k--", alpha=ALPHA)
ax.text(p[0] - 2.6, p[1], 0.02, "驻点：局部极大点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-9.png'), format='png')