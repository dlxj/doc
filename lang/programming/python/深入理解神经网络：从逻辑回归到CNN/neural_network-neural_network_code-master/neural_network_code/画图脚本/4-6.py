# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:57:31 2018

@author: zhangjuefei
"""

from book_draw_util import *

w1 = 1
w2 = 1
m = 0
def valley(p):
    x1, x2 = p[0], p[1]
    return w1 * x1 ** 2 + w2 * x2 ** 2 + m * x1 * x2
    
def valley_de(p):
    x1, x2 = p[0], p[1]
    return 2 * w1 * x1 + m * x2, 2 * w2 * x2 + m * x1
    
def valley_hessian(p):
    x1, x2 = p[0], p[1]
    return np.mat([[2 * w1, m], [m, 2 * w2]])
    
fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')
# ax = Axes3D(fig)
# ax.axis("off")
# ax.clear()

xrange = [-12.01, 12.01]
yrange = [-12.01, 12.01]
step = 80
p = (3, 2)

params = [(0.8, 0.8, 0.0), (0.8, 1.6, 0.2), (0.8, 2.4, 0.3), (0.8,3.0, 0.1)]
for idx, param in zip(np.arange(4), params):

    w1, w2, m = param
    ax = axisartist.Subplot(fig, 221 + idx)
    fig.add_axes(ax)
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["x"].set_axisline_style("-|>", size = 1.0)
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax.axis["x"].set_axis_direction("bottom")
    ax.axis["y"].set_axis_direction("right")
        
    
   
    ax.set_xlim(xrange)
    ax.set_ylim(yrange)
        
    # confour
    x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = valley([x1, x2])
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)
    cs = ax.contour(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), colors="k", alpha=ALPHA)
    ax.clabel(cs, inline=1, fontsize=8)

    # point
    ax.scatter(p[0], p[1], s=BIG_POINT_SIZE, c="k")
    # ax.text(p[0], p[1], r"$x$", fontsize=TEXT_FONT_SIZE)
    
    # gradient
    g = valley_de(p)
    ax.arrow(p[0], p[1], -g[0], -g[1], 
             head_width=0.3, 
             length_includes_head=True, color="k")
    
    ax.text(p[0] - g[0] - 0.8, p[1] - g[1] - 1 , r"$-\triangledown f$", fontsize=TEXT_FONT_SIZE)
    
    
    # hessian and eigvectors
    H = valley_hessian(p)
    eigvalues, eigvectors = np.linalg.eig(H.I)
    
    v1,v2 = eigvectors[:,0], eigvectors[:,1]
    ax.arrow(p[0], p[1], v1.A1[0], v1.A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0] + v1.A1[0], p[1] + v1.A1[1] , r"$v^1,\ \lambda^1={:.2f}$".format(1 / eigvalues[0]), fontsize=TEXT_FONT_SIZE)
    ax.arrow(p[0], p[1], v2.A1[0], v2.A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0] + v2.A1[0], p[1] + v2.A1[1] , r"$v^2,\ \lambda^2={:.2f}$".format(1 / eigvalues[1]), fontsize=TEXT_FONT_SIZE)
    
    
    # projection
    g = np.array(g)
    pj1 = np.inner(v1.A1, -g) * v1
    pj2 = np.inner(v2.A1, -g) * v2
    ax.arrow(p[0], p[1], pj1.A1[0], pj1.A1[1], head_width=0.3, length_includes_head=True, color="k", alpha=ALPHA)
    ax.text(p[0] + pj1.A1[0] - 1.5, p[1] + pj1.A1[1] + 0.2 , r"$-\triangledown f^\mathrm{T}v^1$", fontsize=TEXT_FONT_SIZE)
    ax.arrow(p[0], p[1], pj2.A1[0], pj2.A1[1], head_width=0.3, length_includes_head=True, color="k", alpha=ALPHA)
    ax.text(p[0] + pj2.A1[0] - 0.8, p[1] + pj2.A1[1] - 1.2 , r"$-\triangledown f^\mathrm{T}v^2$", fontsize=TEXT_FONT_SIZE)
    
    shrink1 = pj1 * eigvalues[0]
    shrink2 = pj2 * eigvalues[1]
    ax.arrow(p[0], p[1], shrink1.A1[0], shrink1.A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0] + shrink1.A1[0], p[1] + shrink1.A1[1] + 0.6 , r"$\frac{-\triangledown f^\mathrm{T}v^1}{\lambda^1}$", fontsize=TEXT_FONT_SIZE)
    ax.arrow(p[0], p[1], shrink2.A1[0], shrink2.A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0] + shrink2.A1[0] + 0.4, p[1] + shrink2.A1[1] + 0.7 , r"$\frac{-\triangledown f^\mathrm{T}v^2}{\lambda^2}$", fontsize=TEXT_FONT_SIZE)
    
    ax.arrow(p[0], p[1], (shrink1 + shrink2).A1[0], (shrink1 + shrink2).A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0] + (shrink1 + shrink2).A1[0] - 4.8, p[1] + (shrink1 + shrink2).A1[1] + 0.2 , "修正后的方向", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    ax.text(-8, 13, "二次函数：" + r"$f\left(x\right)={:.1f}x^1+{:.1f}x^2+{:.1f}x^1x^2$".format(w1, w2, m), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '4-6.png'), format='png')