# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:22:34 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

xrange = (-3, 3)

def q1(p):
    x1, x2 = p[0], p[1]
    return x1**2 + x2**2

def q2(p):
    return -q1(p)

def q3(p):
    x1, x2 = p[0], p[1]
    return x1**2 + 0.5 * x2**2 - 0.6 * x1 * x2

def q4(p):
    x1, x2 = p[0], p[1]
    return x1**2 - x2**2 

c = 0
funs = [q1, q2, q3, q4]
eqs = [r"$f\left(x\right)=x_1^2+x_2^2$", 
       r"$f\left(x\right)=-x_1^2-x_2^2$", 
       r"$f\left(x\right)=x_1^2+0.5x_2^2-0.6x_1x_2$", 
       r"$f\left(x\right)=x_1^2-x_2^2$"]

for fun, eq in zip(funs, eqs):
    
    c+=1
    ax = fig.add_subplot(2, 2, c, projection="3d")
    ax.clear()
    
    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
        
    # ax.set_title(r"$Lorenz\ Attractor$")
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
        
    # surface
    minv, maxv = xrange
    step = 40
    x1 = np.linspace(minv, maxv, endpoint=True, num=step)
    x2 = np.linspace(minv, maxv, endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = fun([x1, x2])
    bottom = np.min(x3)
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                            rstride=6, cstride=6, 
                            color="k", alpha=LIGHT_ALPHA)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)
    # ax.set_title(eq, fontsize=TEXT_FONT_SIZE)
    ax.set_title("二次函数：" + eq , fontsize=TEXT_FONT_SIZE, fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '4-1.png'), format='png')