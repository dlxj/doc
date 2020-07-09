# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 17:29:28 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.optimize import fmin

w1 = 0.1
w2 = 1
m = 0
center = (10, 7)
l = 0.5

def valley(p):
    x1, x2 = p[0] - center[0], p[1] - center[1]
    return w1 * x1 ** 2 + w2 * x2 ** 2 + m * x1 * x2
    
def valley_de(p):
    x1, x2 = p[0] - center[0], p[1] - center[1]
    return np.array([2 * w1 * x1 + m * x2, 2 * w2 * x2 + m * x1])

def l2(p):
    x1, x2 = p[0], p[1]
    return l * (x1 ** 2 + x2 ** 2)

def l2_de(p):
    x1, x2 = p[0], p[1]
    return np.array([2 * l * x1, 2 * l * x2])

def valley_l2(p):
    return valley(p) + l * l2(p)
    
def valley_l2_de(p):
    x1, x2 = p[0] - center[0], p[1] - center[1]
    return valley_de(p) + l * l2_de(p)
    
    
fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

xrange = [-5, 15]
yrange = [-5, 15]
step = 80
p = (3, 2)

params = [(0.8, 0.8, 0.0), (0.8, 1.6, 0.2), (0.8, 2.4, 0.3), (0.8,3.0, 0.1)]

ax = axisartist.Subplot(fig, 121)
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
# minium point
ax.scatter(center[0], center[1], s=BIG_POINT_SIZE, c="k")

# gradient descent
p = np.array((0, 0))
track = []
for i in range(20):
    track.append(p)
    g = valley_de(p)
    p = p - 0.1 * np.array(g)

track = np.array(track)
ax.plot(track[:, 0], track[:, 1],"k--", alpha=ALPHA)
ax.scatter(track[-1, 0], track[-1, 1], s=BIG_POINT_SIZE, c="k", alpha=ALPHA)
ax.text(track[-1, 0] + .1, track[-1, 1] + .1, r"$x^{20}$",  fontsize=TEXT_FONT_SIZE)
ax.text(-1.2, 16, "提前停止", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)


# L2 Regularization
ax = axisartist.Subplot(fig, 122)
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
# x3 = valley([x1, x2])
x4 = valley_l2([x1, x2])
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x4.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)
cs = ax.contour(x1.reshape(step,-1), x2.reshape(step,-1), x4.reshape(step,-1), colors="k", alpha=ALPHA)
ax.clabel(cs, inline=1, fontsize=8)

# minium point
minimum = fmin(valley_l2, (0, 0))
ax.scatter(minimum[0], minimum[1], s=BIG_POINT_SIZE, c="k")
# gradient descent
p = np.array((0, 0))
track = []
for i in range(2000):
    track.append(p)
    g = valley_l2_de(p)
    p = p - 0.1 * np.array(g)

track = np.array(track)
ax.plot(track[:, 0], track[:, 1],"k--", alpha=ALPHA)
ax.scatter(track[-1, 0], track[-1, 1], s=BIG_POINT_SIZE, c="k", alpha=ALPHA)
ax.text(track[-1, 0] + .1, track[-1, 1] + .1, r"$x^{2000}$",  fontsize=TEXT_FONT_SIZE)
ax.text(-1.2, 16, r"$L_2$" + "正则化", fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '7-4.png'), format='png')