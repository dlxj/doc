[TOC]



# TextRank Summary

[z](https://zhuanlan.zhihu.com/p/126733456) [g](https://ansvver.github.io/pagerank_and_textrank.html) [g](https://zouzhitao.github.io/posts/pagerank/) [j](https://www.jianshu.com/p/f6d66ab97332)

[The Google Pagerank Algorithm and How It Works](https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm)



### PageRank的目的

- **判断网页的重要性**
  
  > 在已知网页互相链接方式的情况下**判断网页的重要性**。如果A和B中含有相同的关键字，而A的重要性高于B，那么搜索这个关键字的结果中网页A应该放在网页B之前

- 重要的网页，搜索结果排名靠前，优先展示



## 有向图

![image-20200422151310667](TextRank Summary.assets/image-20200422151310667.png)

- node 节点，一个节点是一个网页

- edge 边，一条边是一个网页链接

- 箭头方向表示网页链接的方向





## Adjacency Matrix 邻接矩阵

> 邻接矩阵是**有向图的数学表示**



![image-20200422153814830](TextRank Summary.assets/image-20200422153814830.png)



- **G(i,j) = 1 表示有箭头从第i 个结点指向第j 个结点，既网页i 链接到网页j** 

- G中的1表示无权重的图，如果是有权图，则这里的1可以替换为相应权重





## 概率转移矩阵（只是近似）

![image-20200422162911198](TextRank Summary.assets/image-20200422162911198.png)



- 通过标准化邻接矩阵得到概率转移矩阵

- **W并不真正满足概率转移矩阵的定义**：

  矩阵各元素都是非负的，并且各行（列）元素之和等于1，各元素用概率表示，在一定条件下是互相转移的。

- **W(i,j) = 1/3 表示网页i "转移"到网页j 的概率是1/3**  ???





## 随机向量



![image-20200422165942195](TextRank Summary.assets/image-20200422165942195.png)



- 随机向量是一个列向量
- 这个随机向量表示五个节点的初始概率





### 随机向量的概率转移

![image-20200422170205225](TextRank Summary.assets/image-20200422170205225.png)

- **随机变量s 右乘（因为s 在右边）概率转移矩阵W 得到新的随机变量**，这就是概率转移
  - W 在左边，所以它是左概率转移矩阵(也叫**随机矩阵**)





### 马尔科夫收敛过程

> 马尔可夫收敛，也需要满足一定的条件，首先必须满足转移矩阵的定义，其次转移矩阵不可约，且非周期。转移矩阵不可约指的是每一个状态都可来自任意的其它状态，也就是任意两个网页都可以通过若干中间网页链接。周期指的是存在一个最小的正整数 k，使得从某状态 i 出发又回到状态 i 的所有路径的长度都是 k 的整数倍，也就是Dead Ends问题，这里由于d(**阻尼因子**)的存在，也使得非周期性得到满足





### 阻尼因子

- 当加入了阻尼因子后，可以认为用户浏览到任何一个页面，都**有可能以一个极小的概率转移到另外一个页面**







# The Google Pagerank Algorithm and How It Works

[o](https://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm)



## Definitions

-  **PR = PageRank**



## So what is PageRank?

- In short **PageRank is a “vote”**











