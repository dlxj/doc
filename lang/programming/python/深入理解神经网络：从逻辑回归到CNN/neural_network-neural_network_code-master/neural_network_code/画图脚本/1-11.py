# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:04:47 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

c = 0

T = "\mathrm{T}"
ws = [[0.1, -0.2], [0.4, -0.2], [1.2, -0.2], [1.6, -0.2]]
for w in ws:

    c+=1
    ax = fig.add_subplot(2, 2, c, projection="3d")

    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    
    # ax.set_title(r"$Lorenz\ Attractor$")
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
    arrow = Arrow3D([0, w[0]],[0, w[1]],[0, -1], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(w[0] - 1.6, w[1], -2, r"$w=\left({:.1f},{:.1f},-1\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)
    
    arrow = Arrow3D([0, w[0]],[0, w[1]],[0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(w[0] - 1, w[1], 0.1, r"$\left({:.1f},{:.1f},0\right)^{:s}$".format(w[0], w[1], T), fontsize=TEXT_FONT_SIZE)
    
    ax.plot((w[0], w[0]), (w[1], w[1]), (-1, 0), "k--", alpha=ALPHA)
    
    
    x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = w[0] * x1 + w[1] * x2
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")
    ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")
    ax.set_title("法向量: " + r"$\left({:.1f},{:.1f},{:.1f}\right)^{:s}$".format(w[0], w[1], -1, T), fontproperties=myfont)


plt.savefig(os.path.join(all_pic_path, '1-11.png'), format='png', dpi=600) 
