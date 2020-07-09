# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:11:13 2019

@author: zhangjuefei
"""

bird = pd.read_csv("E://train_pic/bird.csv").dropna()
feature_columns = ['huml', 'humw', 'ulnal', 'ulnaw', 'feml', 'femw', 'tibl', 'tibw', 'tarl', 'tarw']
bird["type"] = bird.type.apply(lambda t: t in ["SW", "W", "R"]).astype(np.int)

feature_columns = ['huml', 'ulnal', 'feml', 'tibl', 'tarl']

fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = fig.add_subplot()

_ = sns.pairplot(
    data=bird, 
    kind="scatter", 
    vars=feature_columns, 
    hue="type", 
    markers=["o", "s"],
    diag_kind="hist", 
    palette=sns.color_palette("Greys", n_colors=2, desat=1.),
)

plt.savefig(os.path.join(all_pic_path, '1-20.png'), format='png', dpi=600) 