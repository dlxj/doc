# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:30:30 2018

@author: zhangjuefei
"""

from book_draw_util import *

iterations = 3000

fig = plt.figure(figsize=(20, 12))
ax = fig.add_subplot(1, 1, 1)

for r in np.arange(0.0, 4.0, 0.001):
    p = []
    x = 0.5
    for i in range(iterations):
        x = logistic_map(r, x)
        p.append([r, x])
        
    p = np.array(p)
    ax.scatter(p[2800:,0], p[2800:,1],s=1, c="k", alpha=0.2, marker=",")

ax.set_xlabel(r"$r$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.plot([3.0,3.0], [0.0,1.0], "k--")
ax.plot([3.45,3.45], [0.0,1.0], "k--")
ax.plot([3.57,3.57], [0.0,1.0], "k--")
ax.text(1.15, 0.95, "1-周期", fontproperties=myfont)
ax.text(3.15, 0.95, "2-周期", fontproperties=myfont)
ax.text(3.5, 0.95, "4", fontproperties=myfont)
ax.text(3.65, 0.95, "混沌", fontproperties=myfont)
ax.annotate("3周期窗口", xy=(3.85, 0.2), xytext=(3.6, 0.05), 
             arrowprops=dict(facecolor='black', arrowstyle="->"),
             fontproperties=myfont)
ax.grid(True)

plt.savefig(os.path.join(all_pic_path, 'A-20.png'), format='png')
