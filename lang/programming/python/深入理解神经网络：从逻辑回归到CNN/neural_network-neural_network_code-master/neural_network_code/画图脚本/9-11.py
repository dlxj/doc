# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:33:29 2018

@author: zhangjuefei
"""

from book_draw_util import *

vrange = (-1, 2)
minv, maxv = vrange
mus = [0, 0]
sigma = [[0.5, 0], [0, 0.5]]

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = fig.add_subplot(1, 1, 1)
ax.clear() 
    
    # surface
f = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

sns.heatmap(f, cmap=plt.cm.Greys, annot=True, fmt="d", linewidths=0.05, 
            linecolor="k", cbar=False, square=True, xticklabels=False, yticklabels=False,
            ax=ax, annot_kws={"size": 1.5 * TEXT_FONT_SIZE})

plt.savefig(os.path.join(all_pic_path, '9-11.png'), format='png')