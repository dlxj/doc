# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:42:13 2018

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

points = np.random.multivariate_normal((0,0), [[0.3,0],[0,0.3]], 30)
ax.scatter(points[:,0],points[:,1], color="k", s=BIG_POINT_SIZE)

r = np.random.normal(3, 0.2, 30)
t = np.random.uniform(0, 2 * np.pi, 30)
# points = np.random.multivariate_normal((-3,3), [[0.5,0],[0,0.5]], 30)
ax.scatter(r * np.cos(t), r * np.sin(t), color="k", facecolors="none", s=BIG_POINT_SIZE)
ax.legend(["正类样本", "负类样本"], prop=myfont)

plt.savefig(os.path.join(all_pic_path, '1-15.png'), format='png', dpi=600) 

