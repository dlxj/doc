# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:08:34 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
# ax = Axes3D(fig)
# ax.axis("off")
# ax.clear()

xrange = [-20, 20]
step = 80

lr = [0.95, 0.8, 0.6, 0.4]
for c in range(4):
    ax = fig.add_subplot(2, 2, c+1, projection="3d")
    ax.clear()
    
    
    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
    
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
        
    # surface
    x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = valley([x1, x2])
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=0, cmap=plt.cm.Greys, alpha=ALPHA)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                            rstride=6, cstride=6, 
                            color="k", alpha=LIGHT_ALPHA)
    
    
    
    # gd track
    p = (15, 15)
    ax.scatter(p[0], p[1], 0, s=POINT_SIZE, c="k")
    ax.text(p[0], p[1] , -40, r"$x^{\mathrm{start}}$", fontsize=TEXT_FONT_SIZE)
    
    tr1 = [p[0]]
    tr2 = [p[1]]
    global_step = 0
    while True:
        g = valley_de(p)
        p2 = tuple(np.array(p) - lr[c] * np.array(g))
        tr1.append(p2[0])
        tr2.append(p2[1])
        p = p2
        
        global_step += 1
        if np.linalg.norm(g) < 1e-7:
            break;
            
    ax.scatter(p[0], p[1], 0, s=POINT_SIZE, c="k")
    ax.plot(tr1, tr2, [0] * len(tr1),"k", linewidth=0.8)
    # ax.plot(tr1, tr2, valley([np.array(tr1), np.array(tr2)]), "k--", linewidth=0.8)
    ax.text(p[0], p[1] , -40, r"$x^{\mathrm{end}}$", fontsize=TEXT_FONT_SIZE)
    ax.set_title("学习率：{:.2f}，迭代次数：{:d}".format(lr[c], global_step) , fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '3-15.png'), format='png')