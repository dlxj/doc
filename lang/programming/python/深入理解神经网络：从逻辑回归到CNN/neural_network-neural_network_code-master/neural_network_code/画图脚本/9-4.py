# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:46:09 2018

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
ax.margins(0)


rx = np.arange(-6, 6, 0.01)
rt = np.arange(-6, 5, 1)
x = 2
d = 0.8

# plt.xlim(-12,12)
plt.ylim(-0.81, 0.81)
ax.grid(True)
ax.text(x=6.2, y=-0.03, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)

# ax.plot(rx, non_convex_fun_1d_de(rx), "k")
# ax.plot(rx, normal_density(rx, x, d), "k--")

ax.scatter(x + rt, non_convex_fun_1d_de(x + rt), s=BIG_POINT_SIZE, color="k")
ax.scatter(x + rt, normal_density(x + rt, x, d), s=BIG_POINT_SIZE, color="k", facecolors="none")
ax.legend([r"$g$", r"$f$"], fontsize=LEGEND_FONT_SIZE)

for p in rt:
    g = non_convex_fun_1d_de(x + p)
    f = normal_density(x + p, x, d)
    f_offset, g_offset = (0.15, -0.15) if f >= g else (-0.15, 0.15)
    # ax.text(x + p, g + g_offset, r"$g\left({:d}\right)$".format(x + p), fontsize=TEXT_FONT_SIZE * 0.6)
    # ax.text(x + p, f + f_offset, r"$f\left({:d}\right)$".format(-p), fontsize=TEXT_FONT_SIZE * 0.6)
    
    if np.abs(f-g) > 0.15:
        ax.plot([x + p, x + p], [g, f], "k--", alpha=ALPHA)
        ax.text(x + p - 0.08, (g + f) / 2 - 0.02, r"$\times$", fontsize=TEXT_FONT_SIZE * 0.6)
        
plt.savefig(os.path.join(all_pic_path, '9-4.png'), format='png')