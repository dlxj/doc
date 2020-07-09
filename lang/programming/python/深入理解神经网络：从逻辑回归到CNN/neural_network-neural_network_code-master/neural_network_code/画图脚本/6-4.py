# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:22:51 2018

@author: chaos
"""
from book_draw_util import *

xrange = [-6, 6]
step = 80

w1 = np.mat([2, 2])
b1 = -1
    
w2 = np.mat([-2, 2])
b2 = -1
    
w3 = np.mat([1, -2])
b3 = 2

cm = plt.cm.Greys

def affine(w, b, x, y):
    s = w * np.mat([[x], [y]]) + b
    # return 1/(1+np.power(np.e, s))
    return s

def sum_of_affine(x, y):
    s = affine(w1, b1, x, y)+affine(w2, b2, x, y)+affine(w3, b3, x, y)
    return s


sum_of_affine_v = np.vectorize(sum_of_affine)
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
tri = mtri.Triangulation(x1, x2)
x3 = sum_of_affine_v(x1, x2)
bottom = np.min(x3)

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)

ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=bottom, cmap=cm, alpha=ALPHA)
ax.scatter(0, 0, bottom, s=POINT_SIZE, c="k")
      
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$f\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)


for idx, w in zip(np.arange(3), [w1, w2, w3]):
    arrow = Arrow3D([0, w[0, 0]], [0, w[0, 1]], [bottom, bottom], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)
    ax.text(w[0, 0] + 0.1, w[0, 1] + 0.1, bottom - 0.02, r"$w_{:d}$".format(idx + 1), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '6-4.png'), format='png')