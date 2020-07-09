# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:08:20 2018

@author: zhangjuefei
"""


from book_draw_util import *


fig = plt.figure(figsize=RECTANGLE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")


rx = np.arange(-6, 6.02, 0.01)
x = 1.5
dx = 0.8
rt = np.arange(x - 1, x + 1, 0.01)

# plt.xlim(-12,12)
plt.ylim(-1, 2)
ax.grid(True)
ax.margins(0,0)
ax.text(x=6.3, y=-0.04, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=2.2, s=r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.plot(rx, non_convex_fun_1d(rx), c="k")
ax.plot(rx, non_convex_fun_1d_de(rx), "k--")
# ax.legend([r"$f\left(x\right)$", r"$f^'\left(x\right)$"])
ax.legend([r"$f\left(x\right)$", r"$f^{'}\left(x\right)$"], loc="upper left", fontsize=LEGEND_FONT_SIZE)

fx = non_convex_fun_1d(x)
ax.scatter(x, 0, s=POINT_SIZE, c="k")
ax.scatter(x, fx, s=POINT_SIZE, c="k")
ax.plot([x, x], [0, fx], "k--", alpha=ALPHA)
ax.text(x - 0.1, -0.15, s=r"$x$", fontsize=TEXT_FONT_SIZE)

xdx = x + dx
fxdx = non_convex_fun_1d(xdx)
ax.scatter(xdx, 0, s=POINT_SIZE, c="k")
ax.scatter(xdx, fxdx, s=POINT_SIZE, c="k")
ax.plot([xdx, xdx], [0, fxdx], "k--", alpha=ALPHA)
ax.text(xdx - 0.1, -0.15, s=r"$x+h$", fontsize=TEXT_FONT_SIZE)

ax.plot([x, xdx], [fx, fxdx], "k", alpha=DARK_ALPHA)
ax.plot([x, xdx], [fx, fx], "k--", alpha=ALPHA)
ax.text((x+xdx)/2 - 0.1, fx - 0.1, s=r"$h$", fontsize=TEXT_FONT_SIZE)

ax.annotate(s=r"$f\left(x+h\right)-f\left(x\right)$", 
        xy=(xdx, (fx+fxdx)/2), xytext=(xdx + 1, (fx+fxdx)/2), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontsize=TEXT_FONT_SIZE)

ax.plot(rt, (rt - x) * non_convex_fun_1d_de(x) + fx, "k", alpha=DARK_ALPHA)
# ax.text(x - 0.1, fx + 0.1, s="x 处的切线", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
ax.annotate(s="x 处的切线", 
        xy=(x, fx), xytext=(x - 1.2, fx + 0.5), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-1.png'), format='png')

