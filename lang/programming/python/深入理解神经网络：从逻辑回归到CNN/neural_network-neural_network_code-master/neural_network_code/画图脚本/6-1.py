# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:42:34 2018

@author: chaos
"""

from book_draw_util import *

step = 80
def logistic(x1, x2):
    return 1 / (1 + np.e ** -(w[0] * x1 + w[1] * x2))

fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

T = "\mathrm{T}"
for idx, w in zip(np.arange(2), [(.4, .9), (.9, .3)]):

    w /= np.linalg.norm(w)
    ax = fig.add_subplot(121+idx, projection="3d")
    ax.clear()
    
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])

    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE) 
    
    # w
    arrow = Arrow3D([0,w[0]],[0,w[1]],[0,0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(w[0], w[1], 0.05, r"$w$", fontsize=TEXT_FONT_SIZE)
    
    # line
    l = np.array([[t * w[0], t * w[1]] for t in np.arange(-10, 10, 0.01) if -6 < t * w[0] < 6 and -6 < t * w[1] < 6]).transpose()
    ax.plot(l[0], l[1], [0] * l.shape[1], "k--", alpha=ALPHA)
    ax.plot(l[0], l[1], logistic(l[0], l[1]), "k", alpha=ALPHA)
    
    # x
    x = (4, 0)
    arrow = Arrow3D([0, x[0]], [0, x[1]], [0, 0], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(x[0], x[1], 0, r"$x$", fontsize=TEXT_FONT_SIZE)
    
    # surface
    x1 = np.linspace(-6, 6, endpoint=True, num=step)
    x2 = np.linspace(-6, 6, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = logistic(x1, x2)
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    # ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
    #                rstride=12, cstride=12, 
    #                color="k", alpha=LIGHT_ALPHA)
    
    ax.scatter(0, 0, 0, s=POINT_SIZE, c="k")
    
    
    # projection
    pj = np.inner(x, w) * np.array(w)
    ax.scatter(pj[0], pj[1], 0, s=POINT_SIZE, c="k")
    ax.plot([x[0], pj[0]], [x[1], pj[1]], [0] * 2, "k--", alpha=ALPHA)
    ax.scatter(pj[0], pj[1], logistic(pj[0], pj[1]), s=POINT_SIZE, c="k")
    ax.text(pj[0] - 0.1, pj[1], logistic(pj[0], pj[1]) + 0.05, "{:.2f}".format(logistic(pj[0], pj[1])), fontsize=TEXT_FONT_SIZE)
    ax.plot([pj[0], pj[0]], [pj[1], pj[1]], [0, logistic(pj[0], pj[1])], "k--", alpha=ALPHA)
    ax.set_title("单位权值向量: " + r"$w=\left({:.2f},{:.2f}\right)^{:s}$".format(w[0], w[1], T), fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '6-1.png'), format='png')