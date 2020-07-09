# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:44:00 2018

@author: chaos
"""

from book_draw_util import *

xrange = [-10, 10]
step = 80

w1 = np.mat([-1, -1])
b1 = -1
    
w2 = np.mat([1, -1])
b2 = -1
    
w3 = np.mat([0,1])
b3 = 2

wo = np.mat([1,-1, 1])
bo = 2

cm = plt.cm.Greys

def logistic(w, b, x, y):
    s = -(w * np.mat([[x], [y]]) + bo)
    return 1/(1+np.power(np.e, s))
    # return s

def mlp(x, y):
    s = np.mat([logistic(w1, b1, x, y)[0,0], logistic(w2, b2, x, y)[0,0], logistic(w3, b3, x, y)[0,0]]).T
    s = -(wo * s + bo)
    return  1/(1+np.power(np.e, s))


mlp = np.vectorize(mlp)

x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = mlp(x1, x2)
bottom = np.min(x3)

fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)

ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=bottom, cmap=cm, alpha=ALPHA)
             
# ax.set_zlim([np.min(x3)-0.01, np.max(x3)+0.01])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$f\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
# ax.view_init(40, 60)

plt.savefig(os.path.join(all_pic_path, '6-7.png'), format='png')