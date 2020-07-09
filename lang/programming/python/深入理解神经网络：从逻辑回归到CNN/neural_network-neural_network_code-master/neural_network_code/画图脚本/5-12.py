# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:24:02 2018

@author: zhangjuefei
"""

from book_draw_util import *


xrange = [-2.01, 2.01]
yrange = [-2.01, 2.01]
step = 80
number_of_points= 30

true_mu = [.8, .8]

mu1 = [.7, .7]
sigma1 = [[0.8, 0], [0, 0.8]]

mu2 = [.4, .4]
sigma2 = [[0.2, 0], [0, 0.2]]


fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

# two distributions

for c, mu, sigma, title in zip(np.arange(2), [mu1, mu2], [sigma1, sigma2], ["低偏置-高方差", "高偏置-低方差"]):
    ax = axisartist.Subplot(fig, 121 + c)
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
        
    ax.text(-0.4, 2.2, title, fontproperties=myfont)
    
    # confour
    x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = normal_density_2([x1, x2], mu, sigma)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)
    points = np.random.multivariate_normal(mu, sigma, number_of_points)
    ax.scatter(points[:,0], points[:,1], color="k", facecolors="none", s=BIG_POINT_SIZE, alpha=DARK_ALPHA)
    ax.scatter(true_mu[0], true_mu[1], color="k", s=BIG_POINT_SIZE * 1.5)
    ax.annotate(s="真实值", 
            xy=(true_mu[0], true_mu[1]), xytext=(true_mu[0] + .2, true_mu[1] + .2), arrowprops=dict
            (width=0.1, 
            facecolor='black',
            headwidth=6,
            shrink=0.05), fontproperties=myfont)
    
    ax.scatter(mu[0], mu[1], color="k", s=BIG_POINT_SIZE * 1.5)
    
    ax.annotate(s="预测值期望", 
            xy=(mu[0], mu[1]), xytext=(mu[0] - .6, mu[1] - .3), arrowprops=dict
            (width=0.1, 
            facecolor='black',
            headwidth=6,
            shrink=0.05), fontproperties=myfont)
    
plt.savefig(os.path.join(all_pic_path, '5-12.png'), format='png')

 