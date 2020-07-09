# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:19:42 2018

@author: zhangjuefei
"""

from book_draw_util import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

data = make_moons(1000, noise=0.3)
train_x, test_x, train_y, test_y = train_test_split(data[0], data[1])


train_acc = []
test_acc = []

for deep in range(1, 40):
   dt = DecisionTreeClassifier(max_depth=deep).fit(train_x, train_y) 
   train_acc.append(accuracy_score(train_y, dt.predict(train_x)))
   test_acc.append(accuracy_score(test_y, dt.predict(test_x)))


fig = plt.figure(figsize=(10, 6))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

ax.margins(0,0)
ax.plot(train_acc, "k")
ax.plot(test_acc, "k--")
ax.grid(True)
ax.legend(["训练集准确率", "测试集准确率"], loc="lower right", prop=myfont)
ax.set_ylim([0.75, 1.1])
ax.set_xlim([0, 40])

ax.annotate(s="欠拟合", 
        xy=(1, 0.825), xytext=(4, 0.83), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontproperties=myfont)

ax.annotate(s="过拟合", 
        xy=(38, .999), xytext=(30, 0.975), arrowprops=dict
        (width=0.1, 
        facecolor='black',
        headwidth=6,
        shrink=0.05), fontproperties=myfont)

ax.text(0, 0.70, "自由度低：高偏置/低方差", fontproperties=myfont)
ax.text(27, 0.70, "自由度高：低偏置/高方差", fontproperties=myfont)
ax.set_ylabel("Accuracy", fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '5-17.png'), format='png')