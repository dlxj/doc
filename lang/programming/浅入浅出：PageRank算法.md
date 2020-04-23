# 浅入浅出：PageRank算法



网络上将pagerank的博文已经很多了，一般的数据挖掘相关的书籍中也会有介绍。本文只是粗略的讲一下笔者对pagerank的理解，以及如何放在真实场景中使用pagerank。

下图显示了某一时刻网页A、B、C的链接情况，网页A中存在到网页B、C中的链接，网页B存在到网页C的链接，网页C存在到网页A的链接。

![图 01](https://www.letianbiji.com/machine-learning/img/pagerank-03.png)

图 01



PageRank的目的就是在已知这种链接方式的情况下判断三个网页的重要性。如果A和B中含有相同的关键字，而A的重要性高于B，那么搜索这个关键字的结果中网页A应该放在网页B之前。

### 最简单的PageRank

一个网页本身具有一定的重要性，我们认为一个网页的链接会把该网页的重要性传递到链接的网页中，而一个网页的重要性又必须通过链接它的网页来确定。公平起见，一个网页X若链接了m个网页，那么这m个网页的每个网页接收到的来自网页X的重要性是PR(X)/m。设A、B、C的重要性，也就是PageRank值分别是PR(A)、PR(B)、PR(C)。

于是由图01，可得以下方程组：

```plain
PR(A) = PR(C)
PR(B) = PR(A)/2
PR(C) = PR(A)/2 + PR(B)
```

Copy

计算可得：

```plain
PR(A) = PR(C) = 2*PR(B)
```

Copy

上面的结果已经大致能看出A、B、C各自的重要性。不过有一个问题是，没有把重要程度量化。下面，通过迭代的方式将其量化。

设A、B、C的初始的重要性均为1，通过上面的方程组进行迭代，每次迭代后会更新A、B、C的重要性。为了方面，先把方程组转换为矩阵运算。

```plain
PR(A) = 0*PR(A) + 0*PR(B) + PR(C)
PR(B) = 0.5*PR(A) + 0*PR(B) + 0*PR(C)
PR(C) = 0.5*PR(A) + PR(B) + 0*PR(C)
```

Copy

下面是MATLAB版本的代码：

```plain
M = [0 0 1 
    0.5 0 0
    0.5 1 0];
PR = [1; 1 ; 1];

for iter = 1:100
    PR = M*PR;
    disp(iter);
    disp(PR);
end
```

Copy

| 第几次迭代 | A的重要性 | B的重要性 | C的重要性 |
| :--------- | :-------- | :-------- | :-------- |
| 0          | 1         | 1         | 1         |
| 1          | 1         | 0.5       | 1.5       |
| 2          | 1.5       | 0.5       | 1.0       |
| 3          | 1         | 0.75      | 1.25      |
| 4          | 1.25      | 0.5       | 1.25      |
| ...        | ...       | ...       | ...       |
| 20         | 1.2002    | 0.5996    | 1.2002    |
| 27         | 1.2000    | 0.6000    | 1.2000    |
| 100        | 1.2000    | 0.6000    | 1.2000    |

但是，上面的方法是有问题的。先看下图：

![图 02](https://www.letianbiji.com/machine-learning/img/pagerank-04.png)

图 02



从上图，得到的方程组如下：

```plain
PR(A) = PR(B) + PR(C)
```

Copy

这种情况下，网页之间的重要性无法比较。

而通过迭代的方法求重要性：

```plain
M = [0 1 1 
    0 0 0
    0 0 0];

PR = [1; 1 ; 1];

for iter = 1:100
    PR = M*PR;
    disp(iter);
    disp(PR);
end
```

Copy

最终收敛的结果是：

```plain
PR(A) = PR(B) = PR(C) = 0
```

Copy

于是，修正是有必要的。

### 修正版本的PageRank

第一种修正方式是网页通过链接传递的重要性乘以一个在0和1之间的阻尼系数d：

PR(A)=(1−d)+d∗∑i=1mPR(Ti)C(Ti)

上式是计算网页A的重要性的式子。Ti是存在到A的链接的网页。C(Ti)是网页Ti中的存在的链接的数量。d是阻尼系数，一般定义为用户随机点击链接的概率，常取值0.85。而`(1-d)`代表着不考虑入站链接的情况下随机进入一个页面的概率。

另一种修正方式和第一种很像，如下：

PR(A)=(1−d)N+d∗∑i=1mPR(Ti)C(Ti)

`N`是网页的总数。

本文只讨论第一种修正方式。

首先，取阻尼系数为0.85，解决图02中的问题，方程组如下：

```plain
A = 0.15 + 0.85*(B+C)
B = 0.15
C = 0.15
```

Copy

解得：

```plain
A = 0.4050
B = 0.15
C = 0.15
```

Copy

通过迭代的方法计算：

```plain
M = [0 1 1 
    0 0 0
    0 0 0];

PR = [1; 1 ; 1];

for iter = 1:100
    PR = 0.15 + 0.85*M*PR;
    disp(iter);
    disp(PR);
end
```

Copy

最终收敛到：

```plain
A = 0.4050
B = 0.15
C = 0.15
```

Copy

### 与特征值的关系

使用迭代的方法处理`图01`中的链接关系的时候，使用的矩阵是：

```plain
M = [0 0 1 
    0.5 0 0
    0.5 1 0];
```

Copy

这是一个典型的状态转移矩阵（所有元素不小于0，每一列的和为1），也可以叫做随机矩阵（Stochastic matrix），状态转移矩阵的最大特征值为1。在迭代的每一步，进行了下面的运算：

```plain
PR = M*PR;
```

Copy

由于图01中的迭代是能够收敛的，所以对于最终的向量PR，肯定会满足上式。这也就意味着PR是矩阵M的特征值1对应的特征向量。

这里只说到这儿，详细可以参考[How Google Finds Your Needle in the Web's Haystack](http://www.ams.org/samplings/feature-column/fcarc-pagerank)。

### MapReduce实现

矩阵与向量的乘法很容易用MapReduce编程模型实现，不讨论。

### 相关资料

- [PageRank 维基百科](http://zh.wikipedia.org/wiki/PageRank)

- [深入探讨PageRank（一）：PageRank算法原理入门](http://blog.csdn.net/monkey_d_meng/article/details/6554518)

- [深入探讨PageRank（二）：PageRank原理剖析](http://blog.csdn.net/monkey_d_meng/article/details/6556295)

- [深入探讨PageRank（四）：PageRank的危机及搜索引擎的未来](http://blog.csdn.net/monkey_d_meng/article/details/6558100)

- [The PageRank Citation Ranking: Bringing Order to the Web](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)

- [谷歌背后的数学](http://www.changhai.org/articles/technology/misc/google_math.php)

- [PageRank算法](http://blog.csdn.net/hguisu/article/details/7996185)

- [Google PageRank算法](http://www.charlesgao.com/?p=157)

- [浅析PageRank算法](http://blog.codinglabs.org/articles/intro-to-pagerank.html)

  

- [随机矩阵的最大特征值](http://whzecomjm.wordpress.com/2013/04/13/随机矩阵的最大特征值/)

- [How Google Finds Your Needle in the Web's Haystack](http://www.ams.org/samplings/feature-column/fcarc-pagerank)

- [Lecture #3: PageRank Algorithm - The Mathematics of Google Search](http://www.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html)

- [Stochastic matrix](http://en.wikipedia.org/wiki/Stochastic_matrix)

