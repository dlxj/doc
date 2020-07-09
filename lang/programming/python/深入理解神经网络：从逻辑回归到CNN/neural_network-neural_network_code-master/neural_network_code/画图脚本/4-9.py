# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:40:39 2018

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=(10, 10))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

w1 = 0.3
w2 = 1
m = 0.5
def valley(p):
    x1, x2 = p[0], p[1]
    return w1 * x1 ** 2 + w2 * x2 ** 2 + m * x1 * x2
    
def valley_de(p):
    x1, x2 = p[0], p[1]
    return 2 * w1 * x1 + m * x2, 2 * w2 * x2 + m * x1
    
def valley_hessian(p):
    x1, x2 = p[0], p[1]
    return np.mat([[2 * w1, m], [m, 2 * w2]])

xrange = [-10, 10]
yrange = [-10.1, 10]
step = 80
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
p = np.array([8, 5])



# Hession
H = valley_hessian(p)
eigvalues, eigvectors = np.linalg.eig(H)
    
for i in range(2):
    
    ax.scatter(p[0], p[1], s=BIG_POINT_SIZE, c="k")
    ax.text(p[0], p[1] + 0.5, r"$x^{:d}$".format(i), fontsize=TEXT_FONT_SIZE)
    
    g = np.mat(valley_de(p)).T
    v = eigvectors[:, i]
    
    p_next = p - (v * g.T * v / (v.T * H * v)).T
    ax.arrow(p[0], p[1], (p_next.A1-p)[0], (p_next.A1-p)[1], head_width=0.3, length_includes_head=True, color="k", linestyle="--", alpha=DARK_ALPHA)
    ax.arrow(p[0], p[1], v.A1[0], v.A1[1], head_width=0.3, length_includes_head=True, color="k")
    ax.text(p[0]+v.A1[0] - 0.5, p[1] + v.A1[1] + 0.5, r"$v^{:d}$".format(i), fontsize=TEXT_FONT_SIZE)
    p = p_next.A1
    
plt.savefig(os.path.join(all_pic_path, '4-9.png'), format='png')