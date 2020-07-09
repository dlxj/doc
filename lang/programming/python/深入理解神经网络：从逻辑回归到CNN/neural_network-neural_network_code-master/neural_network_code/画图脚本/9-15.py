# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:55:56 2018

@author: zhangjuefei
"""

from book_draw_util import *

vrange = (-1, 3)
minv, maxv = vrange

f1 = np.array([[1,0,-1], [2,0,-2], [1,0,-1]])

fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')


for c, f, t in zip(np.arange(2),[f1, f1.transpose()], ["纵向 Sobel 滤波器", "横向 Sobel 滤波器"]):
    ax = fig.add_subplot(1, 2, c+1)
    ax.clear() 
    
    sns.heatmap(f, cmap=plt.cm.Greys, annot=True, fmt="d", linewidths=0.05, 
            linecolor="k", cbar=False, square=True, xticklabels=False, yticklabels=False,
            ax=ax, annot_kws={"size": TEXT_FONT_SIZE})
    ax.set_title(t, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '9-15.png'), format='png')