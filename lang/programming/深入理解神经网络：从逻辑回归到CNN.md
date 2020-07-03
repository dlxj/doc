

[TOC]



# 深入理解神经网络：从逻辑回归到CNN





## affine function



关于$x_1, x_2,\dots,x_n$ 的**仿射函数**(affine function)


$$
a = b + \sum^n_{i=1} w_i x_i
$$


## multilayer perceptron

多层感知机(**MLP**)，也称**多层全连接神经网络**





神经元的能力和极限



## 向量



**黑斜体小写字母**表示向量 $\boldsymbol{x}$ 

> $\mathbf{x}$ 黑非斜

斜体小写字母表示标量  $\textit{x}$ 

矩阵表示一组向量 $X$

上标$\textbf{x}^3$ 表示一组向量中的第3 个



### 维数

向量分量的个数称为向量的维数

向量可以表示坐标系上的一个点，也可以看作**从原点指向这个点的一个有长度和方向的“箭头”**

点和箭头都是向量的几何表现形式



### 向量差



其中一个向量取反方向再求和





### 模长



向量的长度是向量与原点之间的欧式距离。 3 维乃至更高维向量的长度也是它们与原点之间的 欧氏距离一一各分量平方和的平方根。 


$$
length(\textbf{x}) = \sqrt{x_{_1}^2 + x_{_2}^2}
$$



向量的模定义为**与自身内积的平方根** ： 
$$
\|\boldsymbol{x}\| = \sqrt{\left < \boldsymbol{x},\boldsymbol{x} \right>} 
= \sqrt{\sum^n_{i=1}\boldsymbol{x}_{_i}^2}
$$
方向不变，长度缩放到1

$$
\frac{\boldsymbol{x}}{\|\boldsymbol{x}\|}
$$

#### 模长和分量的长度成正比



## 数乘



### 数乘是缩放每一个分量

$$
\|k\boldsymbol{x}\| = 
\sqrt{\sum^n_{i=1}(k\boldsymbol{x_{_i}})^2} \\
= 
\sqrt{\sum^n_{i=1}k^2\boldsymbol{x_{_i}}^2} \\
= 
\sqrt{k^2\sum^n_{i=1}\boldsymbol{x_{_i}}^2} \\
= 
k  \sqrt{\sum^n_{i=1}\boldsymbol{x_{_i}}^2} \\
= 
|k| \ \|\boldsymbol{x}\|
$$





## 内积



### 三角形三边关系

$$
c^2 = a^2+b^2-2ab \  cos\theta \\
2ab \  cos\theta = 0 \quad \text{when $\theta=\frac{\pi}{2}, cos\theta=0$}
$$
> $cos\theta = \frac{斜边的投影}{斜边}$, 90度的时侯斜边的投影是0



### $\|\boldsymbol{x}\|cos\theta=\frac{\left<\boldsymbol{x},\boldsymbol{y}\right>}{\|\boldsymbol{y}\|}$ 是 $\boldsymbol{x}$向 $\boldsymbol{y}$  的投影的长度

如果$\boldsymbol{x}$和 $\boldsymbol{y}$ 之间的夹角为$\theta$，那么$\|\boldsymbol{x}\|cos\theta$ 是向 $\boldsymbol{x}$向 $\boldsymbol{y}$  的投影的长度。投影长度等 于鬻，如果 y 是单位向量，则向 y 的投影的长度就等于 y 〉 。 



### 内积定义为各分量的乘积和


$$
\left< x,y \right> = \sum_{i=1}^n x_i y_i
$$

### 内积是模长乘积再乘夹角余弦

$$
\left< x,y \right> = \|\boldsymbol{x}\| \ \|\boldsymbol{y}\| \ cos \theta
$$

> 在更高维的情况下，向量的夹角反过来由这个式子定义



#### 内积是0则向量正交













![image-20200703130605379](深入理解神经网络：从逻辑回归到CNN.assets/image-20200703130605379.png)

[【直观详解】线性代数的本质](https://charlesliuyx.github.io/2017/10/06/%E3%80%90%E7%9B%B4%E8%A7%82%E8%AF%A6%E8%A7%A3%E3%80%91%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0%E7%9A%84%E6%9C%AC%E8%B4%A8/)



## 线性独立



如果**一组向量中的任何一个都不能被组内其他向量线性表出**，则称这组向量是 线性独立的 (lmearmdependent ） 。如果一组向量不是线性独立的，则称它们线性相关。



如果存在非全零$\boldsymbol{w}$ 满足 $\sum^n_{i=1}w^iV^i=0$  则$V$ 是线性相关的

> w是向量，V 是一组向量  $V \cdot \boldsymbol{w}$ = 0



- 关于什么是线性相关，有两种表达

- - 【表达一】你有多个向量，并且可以**移除其中一个而不减小张成的空间**（即2D共线或3D共面），我们称**它们（这些向量）线性相关**
  - 【表达二】其中一个向量，可以**表示为其他向量的线性组合**，因为这个向量已经落在其他向量张成的空间之中

- 如果从统计学角度来说，这些向量之中有**冗余**。这一堆向量中，我们只需要其中几个（取决于维度）就可以表示其他所有的向量














从信号处理的角度来说，内积是两个信号的相似性

$$
||x(t)-y(t)||^2=||x(t)||^2+||y(t)||^2-2Re{<x(t),y(t)>}
$$
> 
> 等式左边是两个信号的差别，右边前两项是信号的能量。可见对于能量相同（一般通过能量归一化实现）的若干信号来说，内积越大的两个信号差别越小。



解释物理现象：力的做功，当力的向量和移动距离向量有夹角时，力的功就是力向量与距离向量的点积

> 外积出来的量还是矢量，内积出来的量才是标量。功，是标量，这是内积没错



方便复杂计算： 例如，向量的点积为零，意味着垂直，这在证明垂直问题上有很大作用



引入内积的目的时为了定义内积空间





一个简单的办法：
chrome打开知乎页面，按顺序 F12 - F1 - 在General 里面点选 Disable JavaScript。就可以复制了。



