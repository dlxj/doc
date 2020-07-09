# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:00:01 2019

@author: zhangjuefei
"""

bird = pd.read_csv("E://train_pic/bird.csv").dropna()
feature_columns = ['huml', 'humw', 'ulnal', 'ulnaw', 'feml', 'femw', 'tibl', 'tibw', 'tarl', 'tarw']
# feature_columns = ['huml', 'humw', 'ulnal']

fig = plt.figure(figsize=(25, 10), facecolor='white')

for c, f in zip(np.arange(10),feature_columns):
    ax = fig.add_subplot(2, 5, c+1)
    _ = sns.boxplot(
        data=bird, 
        y=f, 
        x='type', 
        ax=ax, 
        palette=sns.color_palette("Greys", n_colors=6, desat=.5)
    )
    
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title(f)
    ax.grid(True)
    

plt.savefig(os.path.join(all_pic_path, '1-19.png'), format='png', dpi=600) 