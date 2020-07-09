# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:31:52 2018

@author: zhangjuefei
"""

from book_draw_util import *

vrange = (-2, 3)
minv, maxv = vrange
mu = [0, 0]
sigma = [[1, 0], [0, 1]]

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = fig.add_subplot(1, 1, 1)
ax.clear() 
    
# surface
x1 = np.arange(minv, maxv)
x2 = np.arange(minv, maxv)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = normal_density_2([x1, x2], mu, sigma).reshape(5, 5)
    

sns.heatmap(x3, cmap=plt.cm.Greys, annot=True, fmt=".3f", linewidths=0.05, 
            linecolor="k", cbar=False, square=True, xticklabels=False, yticklabels=False,
            ax=ax,  annot_kws={"size": TEXT_FONT_SIZE})

plt.savefig(os.path.join(all_pic_path, '9-5.png'), format='png')