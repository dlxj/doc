# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:53:47 2018

@author: zhangjuefei
"""

from book_draw_util import *
fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"
c = 0
for p in [(-.4, -.4), (-.2, -.2), (-.1, -.1), (-.05, -.05)]:
    c+=1
    ax = fig.add_subplot(2, 2, c, projection="3d")
    # ax = Axes3D(fig)
    # ax.axis("off")
    ax.clear()
    
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([0, 6])
    
    # ax.set_title(r"$Lorenz\ Attractor$")
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
    # surface
    x1 = np.linspace(-3, 3, endpoint=True, num=40)
    x2 = np.linspace(-3, 3, endpoint=True, num=40)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = single_peak_2d([x1, x2])
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(40,-1), x2.reshape(40,-1), x3.reshape(40,-1), 
                       rstride=6, cstride=6, 
                       color="k", alpha=LIGHT_ALPHA)
    
    # point
    ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
    ax.scatter(p[0], p[1], single_peak_2d(p), s=BIG_POINT_SIZE, c="k")
    fp = single_peak_2d(p)
    ax.plot((p[0], p[0]), (p[1], p[1]), (0, fp), "k--", alpha=ALPHA)
    ax.text(p[0], p[1] , -0.5, r"$x$", fontsize=TEXT_FONT_SIZE)
    
    
    # gradient
    g = single_peak_2d_de(p)
    arrow = Arrow3D([p[0],p[0] + g[0]],[p[1],p[1] + g[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(p[0] + g[0], p[1] + g[1], 0, r"$\triangledown f=\left({:.2f},{:.2f}\right)^{:s}$".format(g[0], g[1], T), fontsize=TEXT_FONT_SIZE)
    
    # norm
    n = (p[0] + g[0], p[1] + g[1], fp-1)
    arrow = Arrow3D([p[0],n[0]],[p[1], n[1]],[fp, n[2]], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(n[0], n[1], n[2], "法向量" + r"$=\left({:.2f},{:.2f},{:.2f}\right)^{:s}$".format(g[0], g[1], -1, T), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
    # tangent plane
    t1 = np.linspace(p[0]-1.2, p[0]+1.2, endpoint=True, num=40)
    t2 = np.linspace(p[1]-1.2, p[1]+1.2, endpoint=True, num=40)
    t1, t2 = np.meshgrid(t1, t2)
    t1, t2 = t1.flatten(), t2.flatten()
    ft = plane(p, (t1, t2), fp, g)
    tri = mtri.Triangulation(t1, t2)
    ax.plot_trisurf(t1, t2, ft, antialiased=True, alpha=ALPHA, color="k")
    ax.text(p[0], p[1], fp + 0.2, r"切平面".format(g[0], g[1], -1), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
    ax.set_title(r"$x=\left({:.2f},{:.2f}\right)^{:s}$".format(p[0], p[1], T) + " 处的切平面和梯度", fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-3.png'), format='png')