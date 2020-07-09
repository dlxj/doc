# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:26:12 2018

@author: zhangjuefei
"""

from book_draw_util import *


def f(t):
    return np.e ** (-t ** 2 / 2) / (2 * np.pi) ** 0.5

f = np.vectorize(f)

xrange = (-6, 6)
xdelta = 0.05
x = np.arange(xrange[0], xrange[1], xdelta)
y = f(x) * xdelta
signal = np.sin(x) + np.random.normal(0, 0.6, len(x))
blurred = np.convolve(signal, y, "same")


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

ax.plot(x, signal, "k-", alpha=ALPHA)
ax.plot(x, blurred, "k--")
# ax.plot(x, y) 
ax.grid()
ax.set_xlim(xrange)
ax.set_ylim([-4.01, 4])
ax.legend(["$g$", "$f*g$"], fontsize=LEGEND_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '9-2.png'), format='png')