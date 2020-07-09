# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:59:16 2018

@author: zhangjuefei
"""

from book_draw_util import *


xrange = [-4.01, 4]
yrange = [-4.01, 4]
step = 80
number_of_points= 60


mu1 = [1, 1]
sigma1 = [[1,0.2], [0.2,0.6]]

mu2 = [-.5, -.5]
sigma2 = [[1,-0.2], [-0.2,0.4]]


fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

# two distributions
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
ax.grid(True)
    
ax.text(-0.8, 4.4, "混合正态分布",fontsize=AXIS_LABEL_FONT_SIZE , fontproperties=myfont)

# confour
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = normal_density_2([x1, x2], mu1, sigma1) + normal_density_2([x1, x2], mu2, sigma2)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)
    
points = np.concatenate([np.random.multivariate_normal(mu1, sigma1, number_of_points // 2), np.random.multivariate_normal(mu2, sigma2, number_of_points // 2)])
ax.scatter(points[:,0], points[:,1], color="k", s=BIG_POINT_SIZE, alpha=DARK_ALPHA)



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
ax.grid(True)
  
ax.text(-0.8, 4.4, "单一正态分布",fontsize=AXIS_LABEL_FONT_SIZE , fontproperties=myfont)

mu = np.mean(points, axis=0)
sigma = np.cov(points.transpose())

# confour
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = normal_density_2([x1, x2], mu, sigma)
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)
ax.scatter(points[:,0], points[:,1], color="k", s=BIG_POINT_SIZE, alpha=DARK_ALPHA)

 
plt.savefig(os.path.join(all_pic_path, '5-14.png'), format='png')