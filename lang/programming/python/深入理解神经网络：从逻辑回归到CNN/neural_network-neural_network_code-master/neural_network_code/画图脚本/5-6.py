# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:44:42 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=(10, 6))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
ax.margins(0,0)

rx = np.arange(-6, 6.02, 0.01)
x = 1.5
dx = 0.8
rt = np.arange(x - 1, x + 1, 0.01)

# plt.xlim(-12,12)
plt.ylim(0, 0.7)
ax.grid(True)
ax.text(x=6.3, y=-0.005, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.3, y=0.75, s=r"$p\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.plot(rx, normal_density(rx, 2, 0.6), "k")
ax.plot(rx, normal_density(rx, -2, 1.2), "k--")
ax.text(1.92, -0.06, s=r"$\mu^1$", fontsize=TEXT_FONT_SIZE)
ax.text(-2.08, -0.06, s=r"$\mu^2$", fontsize=TEXT_FONT_SIZE)
ax.text(-3.5, 0.62, s=r"$\delta^2>\delta^1$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '5-6.png'), format='png')