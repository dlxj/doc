# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:40:36 2018

@author: zhangjuefei
"""

from book_draw_util import *

vrange = (-2, 3)
minv, maxv = vrange
mus = [0, 0]
sigma = [[0.5, 0], [0, 0.5]]

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = fig.add_subplot(1, 1, 1)
ax.clear() 
    
    # surface
f = np.array([0.04] * 25).reshape(5, 5)
annot = np.array([r"$\frac{1}{25}$"] * 25).reshape(5, 5)

sns.heatmap(f, cmap=plt.cm.Greys, annot=annot, fmt="s", linewidths=0.05, 
            linecolor="k", cbar=False, square=True, xticklabels=False, yticklabels=False,
            ax=ax, annot_kws={"size": 1.5 * TEXT_FONT_SIZE})

plt.savefig(os.path.join(all_pic_path, '9-13.png'), format='png')