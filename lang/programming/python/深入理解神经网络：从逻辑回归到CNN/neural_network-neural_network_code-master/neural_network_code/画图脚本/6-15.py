# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:34:43 2018

@author: chaos
"""

from book_draw_util import *

leaky_alpha=0.1
def leaky_relu(x):
    
    if x >= 0:
        result = x
    else:
        result = leaky_alpha * x

    return result

def leaky_relu_d(x):
    return 1 if x >= 0 else leaky_alpha

fun = np.vectorize(leaky_relu)
derivative = np.vectorize(leaky_relu_d)

xrange = [-1, 1.01]
yrange = [-0.1, 1.01]
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


x = np.arange(xrange[0], xrange[1], 0.0001)
ax.plot(x, fun(x), "k")
ax.plot(x, derivative(x), "k--")
ax.legend([r"$f\left(x\right)$", r"$f^{'}\left(x\right)$"], fontsize=LEGEND_FONT_SIZE)

ax.grid(True)
ax.set_ylim(xrange)
ax.set_ylim(yrange)
ax.margins(0)

plt.savefig(os.path.join(all_pic_path, '6-15.png'), format='png')