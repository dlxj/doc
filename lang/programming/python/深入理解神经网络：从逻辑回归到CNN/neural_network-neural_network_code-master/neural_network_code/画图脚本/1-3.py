# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:12:44 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")



plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.arrow(0,0,4,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")
ax.arrow(0,0,-2,4, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")

ax.text(x=4.1, y=2.1, s=r"$\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=-2.5, y=4.1, s=r"$\left(-2,4\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-3.png'), format='png', dpi=600) 