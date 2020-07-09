# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:04:31 2018

@author: chaos
"""

from book_draw_util import *

def identity(x):
    return x

def identity_d(x):
    return 1

fun = np.vectorize(identity)
derivative = np.vectorize(identity_d)

xrange = [-6.02, 6.02]
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
ax.margins(0)


x = np.arange(xrange[0], xrange[1], 0.01)
ax.plot(x, fun(x), "k")
ax.plot(x, derivative(x), "k--")
ax.legend([r"$f\left(x\right)$", r"$f^{'}\left(x\right)$"], fontsize=LEGEND_FONT_SIZE)

ax.grid(True)
ax.set_ylim(xrange)
ax.set_ylim(xrange)

plt.savefig(os.path.join(all_pic_path, '6-9.png'), format='png')
