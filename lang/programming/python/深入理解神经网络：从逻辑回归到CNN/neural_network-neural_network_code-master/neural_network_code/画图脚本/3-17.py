# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:16:40 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=(16, 8))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

v1 = 0.05
v2 = 1
m = 0
def valley(p):
    x1, x2 = p[0], p[1]
    return v1 * x1 ** 2 + v2 * x2 ** 2 - m * x1 * x2

def valley_de(p):
    x1, x2 = p[0], p[1]
    return 2 * v1 * x1 - m * x2, 2 * v2 * x2 - m * x1

xrange = [-20, 20]
yrange = [-10.1, 10]
step = 80
ax.set_xlim(xrange)
ax.set_ylim(yrange)
# ax.grid(True)
# ax.set_zlim([0, 6])
    
# confour
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = valley([x1, x2])
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)

# point
p = (10, 5)
ax.scatter(p[0], p[1], s=BIG_POINT_SIZE, c="k")
ax.text(p[0] + .2, p[1] + .2, r"$x$", fontsize=TEXT_FONT_SIZE)

# gradient
g = valley_de(p)
ax.arrow(p[0], p[1], -g[0], -g[1], 
         head_width=0.3, 
         length_includes_head=True, color="k")

ax.text(p[0] - g[0] - 0.5, p[1] - g[1] - 1 , r"$-\triangledown f$", fontsize=TEXT_FONT_SIZE)
ax.plot([p[0], p[0]], [p[1], p[1] -g[1]], "k--", alpha=ALPHA, linewidth=1.2)
ax.plot([p[0], p[0] - g[0]], [p[1], p[1]], "k--", alpha=ALPHA, linewidth=1.2)
ax.plot([p[0]-g[0], p[0]-g[0]], [p[1], p[1] - g[1]], "k--", alpha=ALPHA, linewidth=1.2)
ax.plot([p[0], p[0]-g[0]], [p[1] - g[1], p[1] - g[1]], "k--", alpha=ALPHA, linewidth=1.2)
ax.plot([p[0], p[0]-g[0]], [p[1] - 0.4 * g[1], p[1] - 0.4 * g[1]], "k--", alpha=ALPHA, linewidth=1.2)


# shrink

ax.arrow(p[0], p[1], 0, -0.4 * g[1], head_width=0.3, length_includes_head=True, color="k", alpha=ALPHA)
ax.text(p[0] + .5, p[1] - 0.4 * g[1] , "反梯度较大的分量收缩", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
# new gradient
ax.arrow(p[0], p[1], -g[0], -0.4 * g[1], head_width=0.3, length_includes_head=True, color="k")

ax.annotate(s="调整后的方向", 
        xy=(p[0] - g[0] - 0.5, p[1] - 0.4 * g[1] + 0.5), xytext=(2, 5), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-17.png'), format='png')