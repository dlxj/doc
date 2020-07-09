# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:07:31 2018

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
# plt.ylim(-0.01, 0.5)
ax.grid(True)
ax.text(x=6.3, y=-0.005, s=r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.3, y=0.43, s=r"$p\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.plot(rx, normal_density(rx, 0, 1), c="k")
ax.text(2.1, 0.37, s=r"$p\left(x\right)=\frac{1}{\left(\mathrm{2\pi}\right)^{1/2}}\mathrm{e}^{\frac{x^2}{2}}$", fontsize=TEXT_FONT_SIZE)
ax.set_ylim([-.01, .4])
plt.savefig(os.path.join(all_pic_path, '5-5.png'), format='png')