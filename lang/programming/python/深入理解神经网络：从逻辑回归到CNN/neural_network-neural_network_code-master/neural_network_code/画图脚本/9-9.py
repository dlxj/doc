# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:55:56 2018

@author: zhangjuefei
"""

from book_draw_util import *

vrange = (-3, 4)
minv, maxv = vrange
x1 = np.arange(minv, maxv)
x2 = np.arange(minv, maxv)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()

fig = plt.figure(figsize=(18, 6), facecolor='white')


for c, d in zip(np.arange(3),[0.3, 1.2, 3.0]):
    ax = fig.add_subplot(1, 3, c+1)
    ax.clear() 
    
    sigma = [[d, 0], [0, d]]
    x3 = normal_density_2([x1, x2], [0, 0], sigma).reshape(7, 7)
    sns.heatmap(x3, cmap=plt.cm.Greys, annot=True, fmt=".3f", linewidths=0.05, 
            linecolor="k", cbar=False, square=True, xticklabels=False, yticklabels=False,
            ax=ax, annot_kws={"size": TEXT_FONT_SIZE * 0.6})
    ax.set_title(r"$\delta^2={:.1f}$".format(d), fontsize=AXIS_LABEL_FONT_SIZE)
    

plt.savefig(os.path.join(all_pic_path, '9-9.png'), format='png')