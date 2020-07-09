# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:09:11 2018

@author: zhangjuefei
"""

from book_draw_util import *

def f1(t):
    sigma = 0.06
    return np.e**(-t**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

def f2(t):
    sigma=0.1
    return np.e**(-t**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

def f3(t):
    sigma=0.6
    return np.e**(-t**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

def f4(t):
    sigma=1.6
    return np.e**(-t**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)

fv1 = np.vectorize(f1)
fv2 = np.vectorize(f2)
fv3 = np.vectorize(f3)
fv4 = np.vectorize(f4)

xrange = (-6.01, 6)
xdelta = 0.05
x = np.arange(xrange[0], xrange[1], xdelta)
signal = np.sin(x) + np.random.normal(0, 0.6, len(x))


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2)

for idx, f, s in zip(np.arange(4), [fv1, fv2, fv3, fv4], [0.06, 0.1, 0.6, 1.6]):
    sigma = s
    ax = axisartist.Subplot(fig, 221 + idx)
    fig.add_axes(ax)
    
    y = f(x) * xdelta
    blurred = np.convolve(signal, y, "same")
    
    ax.axis[:].set_visible(False)
    ax.axis["x"] = ax.new_floating_axis(0,0)
    ax.axis["x"].set_axisline_style("-|>", size = 1.0)
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax.axis["x"].set_axis_direction("bottom")
    ax.axis["y"].set_axis_direction("right")
    
    ax.plot(x, signal, "k-", alpha=ALPHA)
    ax.plot(x, blurred, "k--")
    # ax.plot(x, y) 
    ax.grid()
    ax.set_xlim(xrange)
    ax.set_ylim([-4, 4])
    ax.legend(["$g$", "$f*g$"], fontsize=LEGEND_FONT_SIZE)
    ax.text(-0.7, 4.4, r"$\sigma={:.2f}$".format(s), fontsize=TEXT_FONT_SIZE)

plt.savefig(os.path.join(all_pic_path, '9-3.png'), format='png')