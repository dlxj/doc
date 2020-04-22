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



- 通过标准化邻接矩阵得到概率转移矩阵

- **W(i,j) = 1/3 表示网页i "转移"到网页j 的概率是1/3**  ???



## 随机向量



![image-20200422165942195](TextRank Summary.assets/image-20200422165942195.png)



- 随机向量是一个列向量
- 这个随机向量表示五个节点的初始概率



### 随机向量的概率转移

![image-20200422170205225](TextRank Summary.assets/image-20200422170205225.png)

- **随机变量s 右乘（因为s 在右边）概率转移矩阵W 得到新的随机变量**，这就是概率转移
  - W 在左边，所以它是左概率转移矩阵(也叫**随机矩阵**)















