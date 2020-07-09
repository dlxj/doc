# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:15:44 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.axis("off")
ax.grid(False)
ax.clear()

xrange = [-1, 1]
ax.set_xlim(xrange)
ax.set_ylim(xrange)
# ax.set_zlim([0, 3])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

x1 = np.linspace(-1, 1, endpoint=True, num=80)
x2 = np.linspace(-1, 1, endpoint=True, num=80)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = saddle(x1, x2)
bottom = np.min(x3)
tri = mtri.Triangulation(x1, x2)
# cmap=plt.cm.Greys
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
ax.contourf(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)
ax.plot_wireframe(x1.reshape(80,-1), x2.reshape(80,-1), x3.reshape(80,-1), 
                   rstride=8, cstride=8, 
                   color="k", alpha=LIGHT_ALPHA)
ax.scatter(0, 0, bottom, color="k", s=BIG_POINT_SIZE)
ax.scatter(0, 0, saddle(0, 0), color="k", s=BIG_POINT_SIZE)
ax.plot([0,0], [0,0], [bottom, saddle(0, 0)], "k--", alpha=ALPHA)
ax.text(-0.1, 0, bottom + 0.05, "鞍点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-8.png'), format='png')