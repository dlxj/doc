[TOC]



# TextRank Summary

[z](https://zhuanlan.zhihu.com/p/126733456) 

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





## 概率转移矩阵

![image-20200422162911198](TextRank Summary.assets/image-20200422162911198.png)







