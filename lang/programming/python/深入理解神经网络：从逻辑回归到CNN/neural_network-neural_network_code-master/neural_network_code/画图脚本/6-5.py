# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:34:26 2018

@author: chaos
"""

from book_draw_util import *

xrange = [-6, 6]
step = 80

w1 = np.mat([1,1])
b1 = -6
    
w2 = np.mat([-1,-1])
b2 = -6

cm = plt.cm.Greys
with_logistic = True

def logistic_1(x, y):
    s = -(w1*np.mat([[x], [y]])+b1)
    return 1/(1+np.power(np.e, s)) if with_logistic else -s

def logistic_2(x, y):
    s = -(w2*np.mat([[x], [y]])+b2)
    return 1/(1+np.power(np.e, s)) if with_logistic else -s

def sum_of_logistic(x, y):
    s = logistic_1(x, y)+logistic_2(x, y)#+logistic(w3, b3, x, y)
    return s


sum_of_logistic_v = np.vectorize(sum_of_logistic)
logistic_1_v = np.vectorize(logistic_1)
logistic_2_v = np.vectorize(logistic_2)

x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
# x1, x2 = np.meshgrid(np.arange(-10, 10, .2), np.arange(-10, 10, .2))

x3 = np.round(sum_of_logistic_v(x1, x2), 5)
bottom = np.min(x3)

fig = plt.figure(figsize=TWO_FIG_SIZE)
ax = fig.add_subplot(1, 2, 1, projection="3d")
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=-0.2, cmap=cm, alpha=ALPHA)
ax.plot_trisurf(x1, x2, logistic_1_v(x1, x2), antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), logistic_1_v(x1, x2).reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
ax.plot_trisurf(x1, x2, logistic_2_v(x1, x2), antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), logistic_2_v(x1, x2).reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
             
ax.set_zlim([-0.2, 1.2])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$f\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

arrow = Arrow3D([0,w1[0,0]],[0,w1[0,1]],[-0.2,-0.2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w1[0,0], w1[0,1], -0.2, r"$w^1$", fontsize=TEXT_FONT_SIZE)
arrow = Arrow3D([0,w2[0,0]],[0,w2[0,1]],[-0.2,-0.2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w2[0,0]-0.6, w2[0,1]-0.6, -0.2, r"$w^2$", fontsize=TEXT_FONT_SIZE)
ax.scatter(0,0,-0.2, s=POINT_SIZE, c="k")
ax.set_title("带" + r"$\mathrm{Logistic}$" + "函数", fontproperties=myfont)

ax = fig.add_subplot(1, 2, 2, projection="3d")
with_logistic=False
x3 = np.round(sum_of_logistic_v(x1, x2), 5)
bottom = np.min(x3)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=-16, cmap=cm, alpha=ALPHA)
ax.plot_trisurf(x1, x2, logistic_1_v(x1, x2), antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), logistic_1_v(x1, x2).reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
ax.plot_trisurf(x1, x2, logistic_2_v(x1, x2), antialiased=True, alpha=LIGHT_ALPHA, cmap=cm)
ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), logistic_2_v(x1, x2).reshape(step,-1), 
                   rstride=6, cstride=6, 
                   color="k", alpha=LIGHT_ALPHA)
             
ax.set_zlim([-16, 10])
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$f\left(x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

arrow = Arrow3D([0,w1[0,0]],[0,w1[0,1]],[-16,-16], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w1[0,0], w1[0,1], -16, r"$w^1$", fontsize=TEXT_FONT_SIZE)
arrow = Arrow3D([0,w2[0,0]],[0,w2[0,1]],[-16,-16], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
ax.add_artist(arrow)
ax.text(w2[0,0]-0.6, w2[0,1]-0.6, -16, r"$w^2$", fontsize=TEXT_FONT_SIZE)
ax.scatter(0,0,-16, s=POINT_SIZE, c="k")
ax.set_title("不带" + r"$\mathrm{Logistic}$" + "函数", fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '6-5.png'), format='png')