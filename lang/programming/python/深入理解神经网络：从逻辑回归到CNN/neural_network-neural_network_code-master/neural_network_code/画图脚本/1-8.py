# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:05:09 2018

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
ax.arrow(0,0,1,2, head_width=ARROW_HEAD_WIDTH, length_includes_head=True, color="k")


ax.arrow(1.6,0.8,-0.6,1.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.4,0.7,-0.1,0.2, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)
ax.arrow(1.3,0.9,0.2,0.1, head_width=0, length_includes_head=True, color="k", linestyle="dashed", alpha=ALPHA)

ax.text(x=4.1, y=2.1, s=r"$y=\left(4,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=1.1, y=2.1, s=r"$x=\left(1,2\right)^\mathrm{T}$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.2, y=0.2, s=r"$\theta$", fontsize=TEXT_FONT_SIZE)
ax.text(x=0.05, y=1.6, s=r"$\left||x\right||$", fontsize=TEXT_FONT_SIZE)
ax.annotate(s=r"$\left||x\right||\mathrm{cos}\theta=\frac{\left<x,y\right>}{\left||y\right||}$", 
        xy=(0.7,0.3), xytext=(2,0.25), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '1-8.png'), format='png', dpi=600) 