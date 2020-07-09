# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:02:32 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE)

c = 30
data = [np.random.multivariate_normal((0, 0), [[0.8, 0.6], [0.6, 0.7]], c)]

for idx, d in zip(np.arange(len(data)), data):

    ax = axisartist.Subplot(fig, 111 + idx)
    ax.grid(True)
    fig.add_axes(ax)
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["x"].set_axisline_style("-|>", size = 1.0)
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax.axis["x"].set_axis_direction("bottom")
    ax.axis["y"].set_axis_direction("right")
        
    
   
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3.01, 3])
    # ax.grid(True)
    # ax.set_zlim([0, 6])
        
    # ax.set_title(r"$Lorenz\ Attractor$")
        
    x1, x2 = d[:,0], d[:,1]
    ax.scatter(x1, x2, c="k", s=BIG_POINT_SIZE)
    ax.text(1.5, 2.5, "协方差：{:.3f}".format(np.cov(x1, x2)[0, 1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '5-2.png'), format='png')