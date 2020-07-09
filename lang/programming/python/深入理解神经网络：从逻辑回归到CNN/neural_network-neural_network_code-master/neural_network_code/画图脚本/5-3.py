# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:23:56 2018

@author: zhangjuefei
"""

from book_draw_util import *
from sklearn.decomposition import PCA

fig = plt.figure(figsize=SQUARE_FIG_SIZE)

c = 60
data = np.random.multivariate_normal((0, 0), [[0.8, 0.6], [0.6, 0.7]], c)


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
ax.text(1.5, 2.5, "总方差：{:.3f}".format(np.cov(x1, x2)[0, 0] + np.cov(x1, x2)[1, 1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

pca = PCA().fit(data)
pc1, pc2 = pca.components_[:,0], pca.components_[:,1]
ax.arrow(0, 0, pc1[0], pc1[1], head_width=0.08, length_includes_head=True, color="k")

pax1 = 2 * pc1
# ax.arrow(-pax1[0], -pax1[1], 4 * pc1[0], 4 * pc1[1], head_width=0.08, length_includes_head=True, color="k", alpha=ALPHA, linestyle="dashed")
ax.text(pc1[0], pc1[1], "第一主成分方向，方差：{:.3f}".format(pca.explained_variance_[0]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)


pax2 = 2 * pc2
# ax.arrow(-pax2[0], -pax2[1], 4 * pc2[0], 4 * pc2[1], head_width=0.08, length_includes_head=True, color="k", alpha=ALPHA, linestyle="dashed")
ax.arrow(0, 0, pc2[0], pc2[1], head_width=0.08, length_includes_head=True, color="k")
ax.text(pc2[0], pc2[1], "第二主成分方向，方差：{:.3f}".format(pca.explained_variance_[1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '5-3.png'), format='png')