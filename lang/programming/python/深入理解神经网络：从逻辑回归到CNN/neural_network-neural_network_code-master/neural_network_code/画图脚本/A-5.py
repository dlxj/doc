# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:53:17 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
    
ax.set_xlim([0, 1.5])
ax.set_ylim([0, 1.5])
ax.set_zlim([0, 1.5])
    
# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel("第 1 元胞", fontsize=AXIS_LABEL_FONT_SIZE, fontproperties=myfont)
ax.set_ylabel("第 2 元胞", fontsize=AXIS_LABEL_FONT_SIZE, fontproperties=myfont)
ax.set_zlabel("第 3 元胞", fontsize=AXIS_LABEL_FONT_SIZE, fontproperties=myfont)
ax.view_init(30, 30)
ax.grid(False)
plt.axis('off')

points = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]


# point
for p in points:
    ax.scatter(p[0], p[1], p[2], s=BIG_POINT_SIZE * 6, c="k")
    ax.text(p[0] + 0.1, p[1] + 0.1 , p[2] + 0.1, "".join([str(i) for i in p]), fontsize=TEXT_FONT_SIZE)
    

already = []
for p1 in points:
    for p2 in points:
        
        if np.logical_xor(np.array(p1), np.array(p2)).sum() == 1 and (p1, p2) not in already:
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], "k--", alpha=ALPHA)
            already.extend([(p1, p2), (p2, p1)])

plt.savefig(os.path.join(all_pic_path, 'A-5.png'), format='png')