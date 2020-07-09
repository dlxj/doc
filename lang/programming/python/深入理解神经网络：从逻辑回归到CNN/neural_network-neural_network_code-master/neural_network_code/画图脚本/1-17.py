# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 12:59:14 2019

@author: zhangjuefei
"""

from book_draw_util import *

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()


bird = pd.read_csv("E://train_pic/bird.csv").dropna()


size_of_each_group = bird.groupby("type").size().sort_values(ascending=False)

ax = size_of_each_group.plot(
    kind="bar", 
    color="#555555",
    rot=0
)

ax.set_xlabel("")
ax.grid(True)

for x, y in zip(np.arange(0, len(size_of_each_group)), size_of_each_group):
    ax.annotate("{:d}".format(y), xy=(x-(0.14 if len(str(y)) == 3 else 0.1), y-8), color="#ffffff", fontproperties=myfont)
                
plt.savefig(os.path.join(all_pic_path, '1-17.png'), format='png', dpi=600) 