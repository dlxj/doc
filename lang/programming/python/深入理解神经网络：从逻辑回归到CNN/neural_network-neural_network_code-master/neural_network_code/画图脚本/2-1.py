# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:42:11 2018

@author: zhangjuefei
"""

from book_draw_util import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

v = 5
number_points = 20000
a = np.random.multivariate_normal([1, 1, 1], [[v, 0, 0], [0, v, 0], [0, 0, v]], number_points)
b = np.random.multivariate_normal([-1, -1, -1], [[v, 0, 0], [0, v, 0], [0, 0, v]], number_points)

data = np.concatenate([a, b], axis=0)
label = np.array([0] * number_points + [1] * number_points)


train_data, test_data, train_label, test_label = train_test_split(data, label)
lr = LogisticRegression().fit(train_data, train_label)

prob = lr.predict_proba(test_data)
fpr, tpr, th = roc_curve(test_label, prob[:, 1])


fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)


ax.margins(0,0)
ax.plot(fpr, tpr, c="k")
ax.plot([0, 1], [0, 1], "k--", alpha=ALPHA)
ax.set_xlabel(r"$\mathrm{FPR}$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$\mathrm{TPR}$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_title(r"$\mathrm{ROC}$" + "曲线", fontsize=AXIS_LABEL_FONT_SIZE, fontproperties=myfont)
ax.text(x=0.81, y=0.05, s=r"$\mathrm{AUC}$" + "={:.3f}".format(roc_auc_score(test_label, prob[:, 1])), fontsize=TEXT_FONT_SIZE)
# plt.ylim(-.1, 1.1)
ax.grid(True)
# ax.text(x=13, y=-0.02, s=r"$a$", fontsize=AXIS_LABEL_FONT_SIZE)
# ax.text(x=-1.3, y=1.2, s=r"$Logistic\left(a\right)$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '2-1.png'), format='png')