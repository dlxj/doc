# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:45:04 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=(18, 6))

c = 40
x = np.random.uniform(-6, 6, c)
y1 = 0.6 * x + np.random.normal(0, 0.5, c)
y2 = 0.6 * x + np.random.normal(0, 1.5, c)
y3 = 2 * np.sin(x) + np.random.normal(0, 2, c) * 0.2

for idx, y in zip(np.arange(3), [y1, y2, y3]):

    ax = axisartist.Subplot(fig, 131 + idx)
    ax.grid(True)
    fig.add_axes(ax)
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["x"].set_axisline_style("-|>", size = 1.0)
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax.axis["x"].set_axis_direction("bottom")
    ax.axis["y"].set_axis_direction("right")
        
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6.1, 6])
        
    ax.scatter(x, y, c="k", s=BIG_POINT_SIZE)
    ax.text(1.2, 4.5, "相关系数：{:.3f}".format(np.corrcoef(x, y)[0, 1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '5-1.png'), format='png') 