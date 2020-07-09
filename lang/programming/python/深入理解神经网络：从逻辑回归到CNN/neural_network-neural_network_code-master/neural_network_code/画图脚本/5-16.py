# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:06:53 2018

@author: zhangjuefei
"""

from book_draw_util import *
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


xrange = [-4.01, 4]
yrange = [-4.01, 4]
step = 80
number_of_points= 60


mu1 = [.6, .6]
sigma1 = [[1,0.2], [0.2,0.6]]

mu2 = [-.6, -.6]
sigma2 = [[1,-0.2], [-0.2,0.4]]


fig = plt.figure(figsize=TWO_FIG_SIZE, facecolor='white')

# two model
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
    
ax.text(-0.5, 4.4, "线性模型",fontsize=AXIS_LABEL_FONT_SIZE , fontproperties=myfont)
 
points1 = np.random.multivariate_normal(mu1, sigma1, number_of_points // 2)
points2 = np.random.multivariate_normal(mu2, sigma2, number_of_points // 2)
ax.scatter(points1[:,0], points1[:,1], color="k", s=BIG_POINT_SIZE, alpha=DARK_ALPHA)
ax.scatter(points2[:,0], points2[:,1], color="k", facecolors='none', s=BIG_POINT_SIZE, alpha=DARK_ALPHA)
ax.legend(["第 1 类样本", "第 2 类样本"], prop=myfont, loc="upper right")

data = np.concatenate([points1, points2])
label = [0] * (number_of_points // 2) + [1] * (number_of_points // 2)
lr = LogisticRegression().fit(data, label)

# confour
x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
x2 = np.linspace(yrange[0], yrange[1], endpoint=True, num=step)
x1, x2 = np.meshgrid(x1, x2)
x1, x2 = x1.flatten(), x2.flatten()
x3 = lr.predict_proba(np.array([x1,x2]).transpose())[:,1]
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)

# two model
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

ax.text(-0.6, 4.4, "过于复杂的模型",fontsize=AXIS_LABEL_FONT_SIZE , fontproperties=myfont)
 
points1 = np.random.multivariate_normal(mu1, sigma1, number_of_points // 2)
points2 = np.random.multivariate_normal(mu2, sigma2, number_of_points // 2)
ax.scatter(points1[:,0], points1[:,1], color="k", s=BIG_POINT_SIZE, alpha=DARK_ALPHA)
ax.scatter(points2[:,0], points2[:,1], color="k", facecolors='none', s=BIG_POINT_SIZE, alpha=DARK_ALPHA)
ax.legend(["第 1 类样本", "第 2 类样本"], prop=myfont, loc="upper right")


lr = KNeighborsClassifier(n_neighbors = 5).fit(data, label)

# confour
x3 = lr.predict_proba(np.array([x1, x2]).transpose())[:,1]
ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), cmap=plt.cm.Greys, alpha=ALPHA)

plt.savefig(os.path.join(all_pic_path, '5-16.png'), format='png')