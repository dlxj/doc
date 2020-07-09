# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:31:56 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin


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


xrange = (-6, 6)
plt.xlim(-6.01, 6.02)
plt.ylim(-6.02, 6.01)
ax.grid(True)
ax.text(x=6.3, y=-0.08, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.1, y=6.3, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)

# gradient field
xrange = (-5.6, 5.6)
g1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=30)
g2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=30)
g1, g2 = np.meshgrid(g1, g2)
g1, g2 = g1.flatten(), g2.flatten()
gf = csurface_2peaks_de([g1, g2])
ax.quiver(g1, g2, -gf[0], -gf[1], color="k", width=0.002, alpha=ALPHA)

p = fmin(csurface_2peaks, (2, -2))
fp =  csurface_2peaks(p)
ax.scatter(p[0], p[1], color="k", s=BIG_POINT_SIZE)
ax.text(p[0] + 0.1, p[1] + 0.1, "吸引子", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
def csurface_2peaks_reverse(p):
    return -csurface_2peaks(p)

p = fmin(csurface_2peaks_reverse, (-2, 2))
fp =  csurface_2peaks(p)
ax.scatter(p[0], p[1], color="k", s=BIG_POINT_SIZE)
ax.text(p[0] + 0.1, p[1] + 0.1, "排斥子", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-11.png'), format='png')