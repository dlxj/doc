# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:27:32 2018

@author: zhangjuefei
"""

from book_draw_util import *
from sklearn.linear_model import LogisticRegression


fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
ax.margins(0)


plt.xlim(-4, 4)
plt.ylim(-4.01, 4)
ax.grid(True)
ax.text(x=4.2, y=-0.05, s=r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.text(x=-0.06, y=4.2, s=r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)

class1 = np.random.multivariate_normal((1.5, 0.5), [[0.3,0],[0,0.3]], 20)
ax.scatter(class1[:,0],class1[:,1], color="k", s=BIG_POINT_SIZE)

class2 = np.random.multivariate_normal((-1, 1.5), [[0.3,0],[0,0.3]], 20)
ax.scatter(class2[:,0],class2[:,1], color="k", marker="^",  s=BIG_POINT_SIZE)

class3 = np.random.multivariate_normal((0,-1.5), [[0.3,0],[0,0.3]], 20)
ax.scatter(class3[:,0],class3[:,1], color="k", facecolors='none', s=BIG_POINT_SIZE)

data = np.concatenate([class1, class2, class3], axis=0)
label = np.array([0] * 20 + [1] * 20 + [2] * 20)

lr = LogisticRegression(multi_class="multinomial", solver="lbfgs").fit(data, label)

w = lr.coef_[1] - lr.coef_[0]
b = lr.intercept_[1] - lr.intercept_[0]
x1 = np.arange(-4, 4, 0.1)
x2 = -w[0] * x1 / w[1] - b / w[1]
ax.plot(x1, x2, "k-")

w = lr.coef_[2] - lr.coef_[0]
b = lr.intercept_[2] - lr.intercept_[0]
x1 = np.arange(-4, 4, 0.1)
x2 = -w[0] * x1 / w[1] - b / w[1]
ax.plot(x1, x2, "k--")

w = lr.coef_[2] - lr.coef_[1]
b = lr.intercept_[2] - lr.intercept_[1]
x1 = np.arange(-4, 4, 0.1)
x2 = -w[0] * x1 / w[1] - b / w[1]
ax.plot(x1, x2, "k-.")

ax.legend(["1-2 类分界线", "1-3 类分界线", "2-3 类分界线", "第 1 类样本", "第 2 类样本", "第 3 类样本"], prop=myfont)

plt.savefig(os.path.join(all_pic_path, '11-1.png'), format='png')
