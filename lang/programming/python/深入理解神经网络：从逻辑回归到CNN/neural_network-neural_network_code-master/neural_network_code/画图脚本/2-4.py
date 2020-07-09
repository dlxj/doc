# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:17:44 2018

@author: zhangjuefei
"""


from book_draw_util import *

fig = plt.figure(figsize=(10, 6))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)

x = np.arange(-6, 6, 0.01)
y = np.log(1+np.e ** -x)
ax.margins(0,0)
ax.plot(x, y, "k")
ax.plot([-6, 0], [np.log(2), np.log(2)], "k--", alpha=ALPHA)
ax.plot([0, 0], [0, np.log(2)], "k--", alpha=ALPHA)
ax.plot(x, y, "k--", alpha=ALPHA)
ax.set_xlabel(r"$\widetilde{y}^i\left(b+w^\mathrm{T}x^i\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$\mathrm{loss}\left(w ,b|x^i,\widetilde{y}^i\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
# ax.text(x=0.85, y=0.05, s="AUC={:.3f}".format(roc_auc_score(test_label, prob[:, 1])), fontsize=TEXT_FONT_SIZE)
# plt.ylim(-.1, 1.1)
ax.grid(True)

plt.savefig(os.path.join(all_pic_path, '2-4.png'), format='png')
