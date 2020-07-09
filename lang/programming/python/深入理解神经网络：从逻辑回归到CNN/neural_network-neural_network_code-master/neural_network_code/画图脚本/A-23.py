# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:44:21 2018

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


plt.xlim(-6, 6)
plt.ylim(-4, 4)
ax.grid(True)
ax.text(x=6.3, y=-0.06, s=r"$\alpha$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=4.5, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.scatter(-4, 0, s=BIG_POINT_SIZE * 2, c="k")
ax.scatter(2, 0, s=BIG_POINT_SIZE * 2, color="k", facecolor="none")
ax.legend(["吸引子", "排斥子"], loc="upper left", prop=myfont)

ax.scatter(-2, 0, s=BIG_POINT_SIZE * 2, c="k")
ax.scatter(0, 0, s=BIG_POINT_SIZE * 2, c="k")

ax.scatter(4, 0, s=BIG_POINT_SIZE * 2, color="k", facecolor="none")
ax.scatter([2, 2, 4, 4], [np.sqrt(2), -np.sqrt(2), np.sqrt(4), -np.sqrt(4)], s=BIG_POINT_SIZE * 2, c="k")

ax.plot([-5.2, 0], [0, 0], c="k", linewidth=2)
ax.plot([0, 5.2], [0, 0], "k--", linewidth=2)

x = np.arange(0, 5.2, 0.01)
y_plus = np.sqrt(x)
y_minus = -np.sqrt(x)
ax.plot(x, y_plus, "k", linewidth=2)
ax.plot(x, y_minus, "k", linewidth=2)

ax.arrow(-4, 3.2, 0, -2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([-4, -4], [3.2, 0], c="k", linewidth=2)

ax.arrow(-4, -3.2, 0, 2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([-4, -4], [-3.2, 0], c="k", linewidth=2)

ax.arrow(-2, 3.2, 0, -2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([-2, -2], [3.2, 0], c="k", linewidth=2)

ax.arrow(-2, -3.2, 0, 2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([-2, -2], [-3.2, 0], c="k", linewidth=2)

ax.arrow(0, 3.2, 0, -2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([0, 0], [3.2, 0], c="k", linewidth=2)

ax.arrow(0, -3.2, 0, 2, head_width=0.2, length_includes_head=True, color="k")
ax.plot([0, 0], [-3.2, 0], c="k", linewidth=2)

ax.arrow(2, 3.2, 0, np.sqrt(2) - 2.4, head_width=0.2, length_includes_head=True, color="k")
ax.arrow(2, 0, 0, 1, head_width=0.2, length_includes_head=True, color="k")
ax.plot([2, 2], [3.2, 0.08], c="k", linewidth=2)

ax.arrow(2, -3.2, 0, -np.sqrt(2) + 2.4, head_width=0.2, length_includes_head=True, color="k")
ax.arrow(2, 0, 0, -1, head_width=0.2, length_includes_head=True, color="k")
ax.plot([2, 2], [-3.2, -0.08], c="k", linewidth=2)


ax.arrow(4, 3.2, 0, np.sqrt(2) - 2.4, head_width=0.2, length_includes_head=True, color="k")
ax.arrow(4, 0, 0, 1, head_width=0.2, length_includes_head=True, color="k")
ax.plot([4, 4], [3.2, 0.08], c="k", linewidth=2)

ax.arrow(4, -3.2, 0, -np.sqrt(2) + 2.4, head_width=0.2, length_includes_head=True, color="k")
ax.arrow(4, 0, 0, -1, head_width=0.2, length_includes_head=True, color="k")
ax.plot([4, 4], [-3.2, -0.08], c="k", linewidth=2)

ax.text(4.2, -1.8, r"$\alpha^2=x$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, 'A-23.png'), format='png')