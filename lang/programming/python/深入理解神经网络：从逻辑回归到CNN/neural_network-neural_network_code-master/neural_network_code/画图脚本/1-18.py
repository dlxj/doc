# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:13:19 2019

@author: zhangjuefei
"""



fig = plt.figure(figsize=SQUARE_FIG_SIZE)
ax = fig.add_subplot()


bird = pd.read_csv("E://train_pic/bird.csv").dropna()
feature_columns = ['huml', 'humw', 'ulnal', 'ulnaw', 'feml', 'femw', 'tibl', 'tibw', 'tarl', 'tarw']
# feature_columns = ['huml', 'humw', 'ulnal']

_ = sns.pairplot(
    data=bird, 
    kind="scatter", 
    vars=feature_columns, 
    hue="type", 
    markers=["o", "s", "D", "^", "p", "*"],
    diag_kind="hist", 
    palette=sns.color_palette("Greys", n_colors=6, desat=1.),
)

plt.savefig(os.path.join(all_pic_path, '1-18.png'), format='png', dpi=600) 