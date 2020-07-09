# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:18:52 2018

@author: chaos
"""

from book_draw_util import *

def logistic(x):
    return 1 / (1 + np.e ** (-x))

def logistic_d(x):
    return logistic(x) * (1 - logistic(x))

fun = np.vectorize(logistic)
derivative = np.vectorize(logistic_d)

xrange = [-6, 6.02]
yrange = [0, 1]
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


x = np.arange(xrange[0], xrange[1], 0.01)
ax.plot(x, fun(x), "k")
ax.plot(x, derivative(x), "k--")
ax.legend([r"$f\left(x\right)$", r"$f^{'}\left(x\right)$"], fontsize=LEGEND_FONT_SIZE)

ax.grid(True)
ax.set_ylim(xrange)
ax.set_ylim(yrange)
ax.margins(0)

plt.savefig(os.path.join(all_pic_path, '6-10.png'), format='png')