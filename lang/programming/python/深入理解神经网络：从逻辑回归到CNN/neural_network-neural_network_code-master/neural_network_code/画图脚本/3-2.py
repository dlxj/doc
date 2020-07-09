# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:42:21 2018

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

plt.ylim(-1, 2)
ax.grid(True)
ax.margins(0,0)
ax.text(x=6.3, y=-0.04, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=2.2, s=r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.plot(rx, non_convex_fun_1d(rx), c="k")

fx = non_convex_fun_1d(x)
ax.scatter(x, 0, s=POINT_SIZE, c="k")
ax.scatter(x, fx, s=POINT_SIZE, c="k")
ax.plot([x, x], [0, fx], "k--", alpha=ALPHA)
ax.text(x - 0.1, -0.15, s=r"$x$", fontsize=TEXT_FONT_SIZE)

xdx = x + dx
fxdx = non_convex_fun_1d(xdx)
ax.scatter(xdx, 0, s=POINT_SIZE, c="k")
ax.scatter(xdx, fxdx, s=POINT_SIZE, c="k")

ldx = fx + non_convex_fun_1d_de(x) * dx
ax.plot([xdx, xdx], [0, fxdx], "k--", alpha=ALPHA)
ax.plot([xdx, xdx], [fxdx, ldx], "k", alpha=DARK_ALPHA)
ax.scatter(xdx, ldx, s=POINT_SIZE, c="k")
ax.plot([0, xdx], [fxdx, fxdx], "k--", alpha=ALPHA)
ax.plot([0, x], [fx, fx], "k--", alpha=ALPHA)
ax.plot([0, xdx], [ldx, ldx], "k--", alpha=ALPHA)
ax.text(xdx - 0.1, -0.15, s=r"$x+h$", fontsize=TEXT_FONT_SIZE)
ax.text(-1, fx-0.05, s=r"$f\left(x\right)$", fontsize=TEXT_FONT_SIZE)
ax.text(-1.3, fxdx-0.03, s=r"$f\left(x+h\right)$", fontsize=TEXT_FONT_SIZE)
ax.text(-2, ldx-0.05, s=r"$f\left(x\right)+hf^{'}\left(x\right)$", fontsize=TEXT_FONT_SIZE)


ax.annotate(s=r"$\mathcal{R}\left(h\right)=f\left(x\right)+hf^{'}\left(x\right)-f\left(x+h\right)$", 
        xy=(xdx, (ldx+fxdx)/2), xytext=(xdx + 0.4, (ldx+fxdx)/2), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontsize=TEXT_FONT_SIZE)

ax.plot(rt, (rt - x) * non_convex_fun_1d_de(x) + fx, "k", alpha=DARK_ALPHA)
# ax.text(x - 0.1, fx + 0.1, s="x 处的切线", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
# ax.annotate(s="x 处的切线", 
#         xy=(x, fx), xytext=(x - 0.8, fx + 0.4), arrowprops=dict
#         (width=0.1, 
#         facecolor='black',
#         headwidth=6,
#         shrink=0.05), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-2.png'), format='png')