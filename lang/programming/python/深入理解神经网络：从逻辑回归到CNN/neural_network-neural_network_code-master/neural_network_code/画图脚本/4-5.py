# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:07:27 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

point = (-np.pi/2 + .95, -np.pi/2 + .95)

def fun(p):
    x1, x2 = p
    return np.sin(x1) + np.sin(x2)

def gradient(p):
    # print(p)
    x1, x2 = p
    return np.mat([np.cos(x1), np.cos(x2)])

def hessian(p):
    x1, x2 = p
    return np.mat([[-np.sin(x1), 0], [0, -np.sin(x2)]])

def tyler(p):
    
    
    global point
    p = np.mat(p).T # 6400x2
    fx = fun(point) # 1x1
    g = gradient(point) # 1x2
    
    h = np.mat(p - np.array(point)) # 1x2
    H = hessian(point)
    return fx + h * g.T + 0.5 * h * H * h.T

xrange = [-np.pi, np.pi]
step = 80
minx, maxx = xrange

p = np.array(point)

fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

labels = [r"$x^0$", r"$x^1$", r"$x^2$", r"$x^3$", r"$x^4$"]
for i, label in zip(np.arange(4), labels):
    ax = fig.add_subplot(2, 2, i + 1, projection="3d")
    ax.clear()
    
    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

    x1 = np.linspace(minx, maxx, endpoint=True, num=step)
    x2 = np.linspace(minx, maxx, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = fun([x1, x2])
    minv = np.min(x3) - 0.5
    maxv = np.max(x3) + 0.5
    tri = mtri.Triangulation(x1, x2)
    
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), rstride=8, cstride=8, color="k", alpha=LIGHT_ALPHA)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=minv, cmap=plt.cm.Greys, alpha=ALPHA)



    # tyler expansion
    step_t = 40
    span = 2
    t1 = np.linspace(p[0]-span, p[0] + span, endpoint=True, num=step_t)
    t2 = np.linspace(p[1]-span, p[1] + span, endpoint=True, num=step_t)
    t1, t2 = np.meshgrid(t1, t2)
    t1, t2 = t1.flatten(), t2.flatten()
    ft = tyler([t1, t2])
    tri = mtri.Triangulation(t1, t2)
    ax.plot_trisurf(t1, t2, np.diag(ft), antialiased=True, alpha=ALPHA, color="k")
    ax.scatter(p[0], p[1], minv, color="k", s=BIG_POINT_SIZE)
    ax.scatter(p[0], p[1], fun(p), color="k", s=BIG_POINT_SIZE)
    ax.plot([p[0]] * 2, [p[1]] * 2, [minv, fun(p)], "k--", alpha=ALPHA)
    ax.text(p[0], p[1], minv-0.5, label, fontsize=TEXT_FONT_SIZE)
    
    H = hessian(p)
    g = gradient(p)
    p_next = (np.mat(p).T-H.I*(g.T)).A1
    ax.scatter(p_next[0], p_next[1], minv, color="k", facecolors="none", s=BIG_POINT_SIZE)
    arrow = Arrow3D([p[0], p_next[0]],[p[1], p_next[1]],[minv, minv], arrowstyle="-|>", lw=1,mutation_scale=10, color="black")
    ax.add_artist(arrow)
    # ax.text(p_next[0], p_next[1], minv-0.5, labels[i + 1], fontsize=TEXT_FONT_SIZE)
        
    point = tuple(p_next)
    p = point
    ax.set_title("第 {:d} 步迭代".format(i + 1),  fontproperties=myfont)
    ax.set_zlim([minv, maxv])
    
plt.savefig(os.path.join(all_pic_path, '4-5.png'), format='png')