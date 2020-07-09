# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:03:34 2018

@author: zhangjuefei
"""

from book_draw_util import *
from scipy.integrate import odeint


def lorenz(w, t, p, r, b):
    x, y, z = w
    return np.array([p * (y - x), x * (r - z) - y, x * y - b * z])


t = 0.0
step = 0.005
span = 40000
max_steps = 600
trail = 0

points = 1
tracks = []

for i in range(points):
    tracks.append(np.array([[0.0 + np.random.normal(0, 0.001), 1.0 + np.random.normal(0, 0.001), 0.0 + np.random.normal(0, 0.001)]]))


fig = plt.figure(figsize=SQUARE_FIG_SIZE, facecolor='white')
ax = Axes3D(fig)
ax.clear()
# plt.axis('off')
# ax.grid(False)

trange = np.arange(0, span * step, step)

# for i, track in zip(range(len(tracks)), tracks):
track = tracks[0]
track_step = odeint(lorenz, track[-1], trange, args=(10.0, 28.0, 3.0))
# tracks[i] = np.concatenate((track, track_step))[-trail:]
ax.scatter(track_step[:, 0], track_step[:, 1], track_step[:, 2], linewidth=.3, c="k", s=1, alpha=0.3)
# ax.scatter(track[-1, 0], track[-1, 1], track[-1, 2], s=6)

ax.set_xlim([-30, 30])
ax.set_ylim([-30, 30])
ax.set_zlim([0, 50])

# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$z$", fontsize=AXIS_LABEL_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, 'A-14.png'), format='png')