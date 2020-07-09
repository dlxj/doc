# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:35:51 2018

@author: zhangjuefei
"""


from book_draw_util import *

iterations = 3000

fig = plt.figure(figsize=(20, 12))
ax = fig.add_subplot(1, 1, 1)

for r in np.arange(3.83, 3.9, 0.00005):
    p = []
    x = 0.5
    for i in range(iterations):
        x = logistic_map(r, x)
        p.append([r, x])
        
    p = np.array(p)
    ax.scatter(p[2800:,0], p[2800:,1],s=1, c="k", alpha=0.2, marker=",")

ax.set_xlabel(r"$r$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)

ax.annotate("倍周期分岔", xy=(3.845, 0.52), xytext=(3.842, 0.62), 
              arrowprops=dict(facecolor='black', arrowstyle="->"),
              fontproperties=myfont)
ax.grid(True)

plt.savefig(os.path.join(all_pic_path, 'A-21.png'), format='png')
