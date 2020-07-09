# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:06:20 2018

@author: zhangjuefei
"""

from book_draw_util import *


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)


trange = np.arange(0, 3000)

r1 = 1000
r2 = 500
r3 = 100

lr = 0.1
def decay(r):
    global lr
    return lr * np.power(10, -trange / r)


ax.plot(trange, decay(r1), "k")
ax.plot(trange, decay(r2), "k--")
ax.plot(trange, decay(r3), "k-.")
ax.set_xlabel("$t$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel("$\eta^t$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.legend([r"$r={:d}$".format(r1), r"$r={:d}$".format(r2), r"$r={:d}$".format(r3)])
ax.grid(True)

plt.savefig(os.path.join(all_pic_path, '3-16.png'), format='png')

