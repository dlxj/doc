# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:53:33 2018

@author: zhangjuefei
"""

from book_draw_util import *
from sklearn.decomposition import PCA

fig = plt.figure(figsize=SQUARE_FIG_SIZE)

c = 80
data = np.random.multivariate_normal((0, 0), [[1, 0.6], [0.6, 0.7]], c)


ax = axisartist.Subplot(fig, 111)
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
        
x1, x2 = data[:,0], data[:,1]
ax.scatter(x1, x2, c="k", s=BIG_POINT_SIZE, alpha=ALPHA)

pca = PCA().fit(data)
pc1, pc2 = pca.components_[:,0], pca.components_[:,1]
ax.arrow(0, 0, pc1[0], pc1[1], head_width=0.08, length_includes_head=True, color="k")
ax.arrow(0, 0, pc2[0], pc2[1], head_width=0.08, length_includes_head=True, color="k")

# normal point
normal_point  = np.random.multivariate_normal((0, 0), [[0.8, 0.6], [0.6, 0.7]], 1)[0]
ax.scatter(normal_point[0], normal_point[1], c="k", s=3 * POINT_SIZE)
ax.text(normal_point[0], normal_point[1] + .1, "正常点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)


# outlier
outlier = (-.8, 2.2)
ax.scatter(outlier[0], outlier[1], marker="^", c="k", s=3 * POINT_SIZE)
ax.text(outlier[0], outlier[1] + .1, "离群点", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

# projection
pj1 = np.inner(outlier, pc1) * pc1
pj2 = np.inner(outlier, pc2) * pc2
# ax.arrow(0, 0, pj1[0], pj1[1], head_width=0.08, length_includes_head=True, color="k", alpha=ALPHA)
# ax.arrow(0, 0, pj2[0], pj2[1], head_width=0.08, length_includes_head=True, color="k", alpha=ALPHA)

# ax.plot([outlier[0], pj1[0]], [outlier[1], pj1[1]], "k--", alpha=ALPHA)
# ax.plot([outlier[0], pj2[0]], [outlier[1], pj2[1]], "k--", alpha=ALPHA)

plt.savefig(os.path.join(all_pic_path, '5-11.png'), format='png')