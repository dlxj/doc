# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:05:53 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

xrange = (-3, 3)

w1 = 1
w2 = 1
def q(p):
    global w1, w2
    x1, x2 = p[0], p[1]
    return w1 * x1 ** 2 + w2 * x2 ** 2 - 0 * x1 * x2

def hessian(p):
    global w1, w2
    x1, x2 = p
    return np.mat([[2 * w1, -0], [-0, 2 * w2]])



idx = 0
ws = [(1, 1), (1, 2), (1, 4), (1, 8)]

for w in ws:
    
    idx += 1
    w1 = w[0]
    w2 = w[1]
    ax = fig.add_subplot(2, 2, idx, projection="3d")
    ax.clear()
    
    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
        
    # ax.set_title(r"$Lorenz\ Attractor$")
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
        
    # surface
    minx, maxx = xrange
    step = 40
    x1 = np.linspace(minx, maxx, endpoint=True, num=step)
    x2 = np.linspace(minx, maxx, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = q([x1, x2])
    bottom = np.min(x3)
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                            rstride=6, cstride=6, 
                            color="k", alpha=LIGHT_ALPHA)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)
    
    # Hessian
    point = (0, 0)
    ax.scatter(point[0], point[1], bottom, color="k", s=BIG_POINT_SIZE)
    H = hessian(point)
    eigvalues,  eigvectors = np.linalg.eig(H)
    eigvectors = np.array(eigvectors)
    labels = [r"$v^1$",
              r"$v^2$"
            ]
    c = 1
    for va, ve, label in zip(eigvalues, eigvectors, labels):
        arrow = Arrow3D([point[0], point[0] +ve[0]],[point[1], point[1] + ve[1]],[bottom, bottom], arrowstyle="-|>", lw=1,mutation_scale=10, color="black")
        ax.add_artist(arrow)
        ax.text( point[0] +ve[0],  point[1] +ve[1], bottom + 1, label.format(va), fontsize=TEXT_FONT_SIZE)
        c += 1
    
    condition_number = eigvalues[1] / eigvalues[0] if eigvalues[1] / eigvalues[0] >= 1 else eigvalues[0] / eigvalues[1]
    ax.set_title("特征值：" + r"$\lambda^1={:.2f}\ \lambda^2={:.2f}\ $".format(eigvalues[0], eigvalues[1]) + ",条件数：" r"$\frac{\lambda^{\mathrm{max}}}{\lambda^{\mathrm{min}}}=$" + "{:.2f}".format(condition_number), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '4-4.png'), format='png')