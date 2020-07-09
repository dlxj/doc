# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:34:08 2019

@author: zhangjuefei
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:23:14 2018

@author: zhangjuefei
"""


from book_draw_util import *
from scipy.optimize import fmin



def wierd(p):
    x1, x2 = p[0], p[1]
    return np.sin(0.2 * x1) + np.cos(0.4 * x2)

def wierd_de(p):
    x1, x2 = p[0], p[1]
    return 0.2 * np.cos(0.2 * x1), -0.4 * np.sin(0.4 * x2)


fig = plt.figure(figsize=(20, 30), facecolor='white')

xrange = [-12, 12]
step = 80

def gd(p, g, eta):
    return tuple(np.array(p) - eta * np.array(g))
    
momentum_v = np.array((0, 0))
momentum_beta = 0.8
def momentum(p, g, eta):
    global momentum_v, momentum_beta
    momentum_v = momentum_beta * momentum_v + eta * np.array(g)
    return tuple(np.array(p) - momentum_v)


adagrad_s = np.array((0, 0))
def adagrad(p, g, eta):
    global adagrad_s
    g = np.array(g)
    adagrad_s = adagrad_s + g ** 2
    return tuple(np.array(p) - eta * g / (adagrad_s + 1e-8) ** 0.5)

rmsprop_s = np.array((0, 0))
rmsprop_beta = 0.9
def rmsprop(p, g, eta):
    global rmsprop_s
    g = np.array(g)
    rmsprop_s = rmsprop_beta * rmsprop_s + (1- rmsprop_beta) * g ** 2
    return tuple(np.array(p) - eta * g / (rmsprop_s + 1e-8) ** 0.5)

adam_s = np.array((0, 0))
adam_v = np.array((0, 0))
adam_beta_1 = 0.6
adam_beta_2 = 0.9
global_step = 0
def adam(p, g, eta):
    global adam_s, adam_v, adam_beta_1, adam_beta_2
    g = np.array(g)
    adam_v = adam_beta_1 * adam_v + (1 - adam_beta_1) * g
    adam_s = adam_beta_2 * adam_s + (1 - adam_beta_2) * (g ** 2)
    adam_v = adam_v / (1 - adam_beta_1 ** (global_step))
    adam_s = adam_s / (1 - adam_beta_2 ** (global_step))
    return tuple(np.array(p) - eta * adam_v / (adam_s + 1e-8) ** 0.5)


etas = [0.2, 0.9, 0.2 ,0.2, 0.2, 0.2]
names = ["原始梯度下降", "原始梯度下降", "冲量法", "AdaGrad", "RMSProp", "Adam"] # 原始梯度下降
params = ["", "", r"$\beta={:.2f}$".format(momentum_beta), "", r"$\beta={:.2f}$".format(rmsprop_beta), r"$\beta^1={:.2f}\ ,\beta^2={:.2f}$".format(adam_beta_1, adam_beta_2)]

algos = [gd, gd, momentum, adagrad, rmsprop, adam] # gd
for c,eta, param, name, algo in zip(np.arange(len(names)), etas, params, names, algos):
    ax = fig.add_subplot(3, 2, c+1, projection="3d")
    ax.clear()
    
    
    ax.set_xlim(xrange)
    ax.set_ylim(xrange)
    
    ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
    ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)
           
    # surface
    x1 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x2 = np.linspace(xrange[0], xrange[1], endpoint=True, num=step)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = wierd([x1, x2])
    bottom = np.min(x3)
    
    tri = mtri.Triangulation(x1, x2)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, cmap = plt.cm.Greys)
    ax.contourf(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), zdir='z', offset=bottom, cmap=plt.cm.Greys, alpha=ALPHA)
    ax.plot_wireframe(x1.reshape(step,-1), x2.reshape(step,-1), x3.reshape(step,-1), 
                            rstride=6, cstride=6, 
                            color="k", alpha=LIGHT_ALPHA)
    

    p = (5 / 2 * np.pi - 1e-3, -1)
    ax.scatter(p[0], p[1], bottom, s=POINT_SIZE, c="k")
    ax.scatter(p[0], p[1], wierd(p), s=POINT_SIZE, c="k")
    ax.text(p[0], p[1] , bottom + 0.1, r"$x^{\mathrm{start}}$", fontsize=TEXT_FONT_SIZE)
    tr1 = [p[0]]
    tr2 = [p[1]]
    
    global_step = 1
    while True:
        g = wierd_de(p)
        p2 = algo(p, g, eta)
        tr1.append(p2[0])
        tr2.append(p2[1])
        p = p2
        global_step += 1
        
        if np.linalg.norm(g) < 1e-6 or global_step > 20000:
            break;
    

    print("{} {:.5f} {:d}".format(name, np.linalg.norm(g), global_step - 1))
    ax.plot(tr1, tr2, [bottom] * len(tr1),"k", linewidth=0.8)
    # ax.plot(tr1, tr2, wierd([np.array(tr1), np.array(tr2)]), "k--", linewidth=0.8)
    ax.scatter(tr1, tr2, wierd([np.array(tr1), np.array(tr2)]), s=POINT_SIZE * 0.2, c="k", alpha=ALPHA)
    ax.scatter(p[0], p[1], bottom, s=POINT_SIZE, c="k")
    ax.scatter(p[0], p[1], wierd(p), s=POINT_SIZE, c="k")
    ax.text(p[0], p[1] , bottom + 0.1, r"$x^{\mathrm{end}}$", fontsize=TEXT_FONT_SIZE)
    
    ax.set_title("{:s}，学习率：{:.2f}，迭代次数：{:d}".format(name, eta, global_step) + (("，超参数：" + param) if param else "") , fontsize=TEXT_FONT_SIZE, fontproperties=myfont)

plt.savefig(os.path.join(all_pic_path, '3-18.png'), format='png')