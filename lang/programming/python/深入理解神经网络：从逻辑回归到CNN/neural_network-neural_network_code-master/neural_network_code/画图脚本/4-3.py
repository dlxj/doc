# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:48:07 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

points = [(-np.pi/2, np.pi/2), (np.pi/2, np.pi/2), (-np.pi/2, -np.pi/2), (np.pi/2, -np.pi/2)]
point = None

def fun(p):
    x1, x2 = p
    return np.sin(x1) + np.sin(x2)

def gradient(p):
    x1, x2 = p
    return np.array([np.cos(x1), np.cos(x2)])

def hessian(p):
    x1, x2 = p
    return np.mat([[-np.sin(x1), 0], [0, -np.sin(x2)]])

def tyler(p):
    
    
    global point
    p = np.mat(p).T # 6400x2
    fx = fun(point) # 1x1
    g = np.mat(gradient(point)) # 1x2
    
    h = np.mat(p - np.array(point)) # 1x2
    H = hessian(point)
    return fx + h * g.T + 0.5 * h * H * h.T

xrange = [-np.pi, np.pi]
step = 80
minx, maxx = xrange

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"
idx = 0
titles = ["鞍点", "局部极大点", "局部极小点", "鞍点"]
for p, title in zip(points, titles):
    
    idx += 1
    ax = fig.add_subplot(2, 2, idx, projection="3d")
    ax.clear()

    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
    # ax.set_zlim([0, 3])
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
    
    x1 = np.linspace(minx, maxx, endpoint=True, num=step)
    x2 = np.linspace(minx, maxx, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = fun([x1, x2])
    minv = np.min(x3) - 1.5
    tri = mtri.Triangulation(x1, x2)
    
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), rstride=8, cstride=8, color="k", alpha=LIGHT_ALPHA)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=minv, cmap=plt.cm.Greys, alpha=ALPHA)



    
    point = p
    # tyler expansion
    step_t = 40
    span = 1.5
    t1 = np.linspace(point[0]-span, point[0] + span, endpoint=True, num=step_t)
    t2 = np.linspace(point[1]-span, point[1] + span, endpoint=True, num=step_t)
    t1, t2 = np.meshgrid(t1, t2)
    t1, t2 = t1.flatten(), t2.flatten()
    ft = tyler([t1, t2])
    tri = mtri.Triangulation(t1, t2)
    ax.plot_trisurf(t1, t2, np.diag(ft), antialiased=True, alpha=ALPHA, color="k")
    # ax.contourf(t1.reshape(step_t,-1), t2.reshape(step_t,-1), ft.reshape(step_t,-1), zdir='z', offset=minv, cmap=plt.cm.Greys, alpha=ALPHA)
    ax.scatter(point[0], point[1], minv, color="k", s=BIG_POINT_SIZE)
    ax.scatter(point[0], point[1], fun(point), color="k", s=BIG_POINT_SIZE)
    ax.scatter(point[0], point[1], minv, color="k", s=BIG_POINT_SIZE)
    ax.plot([point[0]] * 2, [point[1]] * 2, [minv, fun(point)], "k--", alpha=ALPHA)
    # ax.text(point[0] - 1.3, point[1], minv - 1.4,, fontsize=TEXT_FONT_SIZE)
    # ax.text(point[0]-2, point[1], 3, "在x的二阶泰勒展开：" + r"$f\left(x^{'}\right)=f\left(x\right)+\triangledown f_x^T\left(x^{'}-x\right)+\frac{\left(x^{'}-x\right)^TH\left(x\right)\left(x^{'}-x\right)}{2}$", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    # ax.text(np.pi/2 - 1, np.pi/2, fun([np.pi/2, np.pi/2]) + .1, r"$f\left(x\right)=sin\left(x_1\right)+sin\left(x_2\right)$", fontsize=TEXT_FONT_SIZE)
    # Hessian
    H = hessian(point)
    eigvalues,  eigvectors = np.linalg.eig(H)
    eigvectors = np.array(eigvectors)
    labels = [r"$v^1$",
              r"$v^2$"
            ]
    c = 1
    for va, ve, label in zip(eigvalues, eigvectors, labels):
        arrow = Arrow3D([point[0], point[0] +ve[0]],[point[1], point[1] + ve[1]],[minv, minv], arrowstyle="-|>", lw=1,mutation_scale=10, color="black")
        ax.add_artist(arrow)
        ax.text( point[0] +ve[0],  point[1] +ve[1], minv, label, fontsize=TEXT_FONT_SIZE)
        c += 1
    
    ax.set_title(title +  r"$\ \left({:.1f},{:.1f}\right)^{:s}$".format(point[0], point[1], T) + "，特征值：" + r"$\lambda^1={:.1f}\quad \lambda^2={:.1f}$".format(eigvalues[0], eigvalues[1]), fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

        
plt.savefig(os.path.join(all_pic_path, '4-3.png'), format='png')