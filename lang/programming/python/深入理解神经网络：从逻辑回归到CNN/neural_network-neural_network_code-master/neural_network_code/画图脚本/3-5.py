# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:19:06 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
    
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
ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
ax.plot_wireframe(x1.reshape(40,-1), x2.reshape(40,-1), x3.reshape(40,-1), 
                        rstride=6, cstride=6, 
                        color="k", alpha=LIGHT_ALPHA)

# point
p = (0.5, -.5)
ax.scatter(p[0], p[1], 0, s=BIG_POINT_SIZE, c="k")
ax.scatter(p[0], p[1], single_peak_2d(p), s=BIG_POINT_SIZE, c="k")
fp = single_peak_2d(p)
ax.plot((p[0], p[0]), (p[1], p[1]), (0, fp), "k--", alpha=ALPHA)
ax.text(p[0], p[1] , -0.3, r"$x$", fontsize=TEXT_FONT_SIZE)

# direction
d = (-0.2, 0.05)
d /= np.linalg.norm(d)
arrow = Arrow3D([p[0],p[0] + d[0]],[p[1],p[1] + d[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10, color="black")
ax.add_artist(arrow)
ax.text(p[0] + d[0], p[1] + d[1], 0.05, r"$d$".format(d[0], d[1]), fontsize=TEXT_FONT_SIZE)
rt = np.arange(-2.6, 3.6, 0.01)
track = np.array([np.array(p) + t * np.array(d) for t in rt])
ax.plot(track[:,0], track[:,1], [0] * len(track), "k--", alpha=ALPHA)
ax.plot(track[:,0], track[:,1], single_peak_2d([track[:,0], track[:,1]]), "k--", alpha=DARK_ALPHA)

# gradient
g = single_peak_2d_de(p)
arrow = Arrow3D([p[0],p[0] + g[0]],[p[1],p[1] + g[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(p[0] + g[0], p[1] + g[1], 0, r"$\triangledown f$".format(g[0], g[1]), fontsize=TEXT_FONT_SIZE)

# tangent line
dd = np.inner(g, d)
rtl = np.arange(-1.2, 1.2, 0.01)
rtv = fp + dd * rtl
track = np.array([np.array(p) + t * np.array(d) for t in rtl])
# ax.plot(track[:,0], track[:,1], [0] * len(track), "k--", alpha=ALPHA)
ax.plot(track[:,0], track[:,1], rtv, "k", alpha = DARK_ALPHA)
ax.text(p[0], p[1], fp + 0.5, "切线", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

# projection
proj = p + dd * d
ax.plot([p[0] + g[0], proj[0]], [p[1] + g[1], proj[1]], [0, 0], "k--", alpha=ALPHA)
ax.text(p[0]-0.2, p[1]-0.2, -0.15, r"$\theta$", fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '3-5.png'), format='png')