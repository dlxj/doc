# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:05:33 2018

@author: zhangjuefei
"""


from book_draw_util import *

fig = plt.figure(figsize=(10, 6))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)



p = np.arange(0, 1, 0.001)[1:-1]
ax.plot(p, -np.log2(p), "k")
ax.set_xlabel(r"$p\left(X=x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$I\left(X=x\right)$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.grid(True)
ax.margins(0,0)

plt.savefig(os.path.join(all_pic_path, '2-2.png'), format='png')
