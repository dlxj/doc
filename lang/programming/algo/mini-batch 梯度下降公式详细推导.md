

## mini-batch



对于给定输入：

​	[ [0, 0], [0,1], [1,0], [1,1]]

 XOR 的结果是：

​	[ [1,0], [0,1], [0,1], [1,0] ]

> [ [1, 0] ... ] 里的1 表示对于输入 [0, 0]，分类为0 的概率为100%；0 表示分类为1 的概率为0%
>
> [...,[0,1],... ]  里的0 表示对于输入[0,1]，分类为0 的概率为0%；1表示分类为1 的概率为100%



对于分类问题，神经网络的输出结果是一组概率分布。监督学习的标签是真实概率分布 $p$，训练给出的预测结果是近似概率分布 $q$ 。 训练的过程就是是让 $q$ 不断地逼近 $p$。衡量两个分布的接近程度是用KL散度，又由于最小化KL 散度等价于最小化交叉熵，所以用交叉熵作为损失函数。





样本是随机变量$X$（一个骰子）的取值$x$，概率分布 $p$ 给出了随机变量所有取值的概率




## Softmax 函数



https://deepnotes.io/softmax-crossentropy

https://aimatters.wordpress.com/2019/06/17/the-softmax-function-derivative/



softmax 把向量$z$  变成概率
$$
\sigma(z) = (\sigma_1(z), \cdots,\sigma_k(z))
$$

$$
\sigma_i(z) = \frac{e^{z_{i}}}{\sum^k_{j=1} e^{z_{j}}}, \ i \in 1 \cdots k
$$


- 总共有 $k$ 类，样本被分为第 $i$ 类的概率是 $\sigma_i(z)$

  求 $z$ 的任意一个分量对概率 $\sigma_i(z)$ 的偏导


$$
\frac{\partial}{\partial z_{s}} \sigma_i(z) = \frac{\partial}{\partial z_{s}} \bigg ( \frac{e^{z_{i}}}{\sum^k_{j=1} e^{z_{j}}} \bigg ) \ for \ 

\ i \in 1 \cdots k, \ s \in 1 \cdots k \\

=   \frac{ \frac{\partial}{\partial z_{s}} e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - \frac{\partial}{\partial z_{s}} (\sum^k_{j=1} e^{z_{j}}) * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\
$$

$$
if \  s = i,  \\

=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - \frac{\partial}{\partial z_{s}} ( e^{z_{i}}) * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\

=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - e^{z_{i}} * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\


=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}} - e^{z_{i}} )  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\


=   \frac{ e^{z_{i}}   }{\sum^k_{j=1} e^{z_{j}}} * \frac{  \sum^k_{j=1} e^{z_{j}} - e^{z_{i}} }{\sum^k_{j=1} e^{z_{j}}}  \\ 

= \sigma_i(z) * (1 - \sigma_i(z))
$$


$$
if \  s \neq i,  \\

=   \frac{ 0 -  e^{z_{s}} * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\

=   - \ \frac{ e^{z_{s}} }{\sum^k_{j=1} e^{z_{j}}} * \frac{  e^{z_{i}} }{\sum^k_{j=1} e^{z_{j}}}  \\

= - \sigma_s(z) \sigma_i(z)  \\
$$

$$
h(x) = f(x) g(x) \\
h'(x) = f'(x)g(x) + f(x)g'(x)
$$

$$
h(x) = \frac{f(x)}{g(x)}  \\
令：\frac{1}{g(x)} = z(x)，则：
h(x) = f(x) z(x) \\
h'(x) = f'(x)z(x) + f(x)z'(x) \\
= f'(x)\frac{1}{g(x)} + f(x) ( - \frac{ \frac{d}{d x}g(x) }{g(x)^{2}} ) \\

= \frac{f'(x)g(x)}{g(x)^2} - \frac{g'(x)f(x)}{g(x)^2} \\

=  \frac{f'(x)g(x) - g'(x)f(x)}{g(x)^2} 
$$






**概率**是已知参数求**结果的可能性**

**似然**是已知结果求**参数的可能性**

- Likelihood
- 最大似然是求最大可能性的参数（**最大似然**估计(MLE)）



**最大似然原理**



给定一个概率分布$D$，已知其概率密度函数（连续分布）或概率质量函数（离散分布）为$f_D$，以及一个分布参数 $\theta$ ，我们可以从这个分布中抽出一个具有 $n$ 个值的采样$X_{1},X_{2},\ldots ,X_{n}$，利用$f_{D}$ 计算出其似然函数：

$$
L(\theta \ | \ x_1, \cdots, x_n) = f_{\theta}(x_1, \cdots, x_n) 
$$


若$D$ 是离散分布，$f_\theta$ 即是在参数为 $\theta$ 时观测到这一采样的概率。











```

用随机选择的小批量数据（mini-batch）作为全体训练数据的近似值，损失函数要计算这一批数据的总体损失

Xor 问题的每一个输入维度是 (2,) ,  batch 大小设为3，既每次训练三组输入数据，作为全体训练数据的近似

矩阵的维度变化：
	(3,2).(2,3) = (3,3)
	(3,3).(3,1) = (3,1)
```


$$
\begin{bmatrix}
x^{0}_{1,1} & x^{0}_{1,2} & \cdots & x^{0}_{1,n}  \\
x^{0}_{2,1} & x^{0}_{2,2} & \cdots & x^{0}_{2,n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{0}_{m,1} & x^{0}_{m,2} & \cdots & x^{0}_{m,n} \\
\end{bmatrix}

\cdot

\begin{bmatrix}
w^{1}_{1,1} & w^{1}_{1,2} & \cdots & w^{1}_{1,m}  \\
w^{1}_{2,1} & w^{1}_{2,2} & \cdots & w^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{1}_{n,1} & w^{1}_{n,2} & \cdots & w^{1}_{n,m} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{1}_{1,1} & b^{1}_{1,2} & \cdots & b^{1}_{1,m}  \\
b^{1}_{2,1} & b^{1}_{2,2} & \cdots & b^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
b^{1}_{m,1} & b^{1}_{m,2} & \cdots & b^{1}_{m,m} \\
\end{bmatrix}

\\

= 

\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,m}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,m} \\
\end{bmatrix}
$$

$$
g \bigg (
\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,m}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,m} \\
\end{bmatrix}
\bigg )

= 

\begin{bmatrix}
x^{1}_{1,1} & x^{1}_{1,2} & \cdots & x^{1}_{1,m}  \\
x^{1}_{2,1} & x^{1}_{2,2} & \cdots & x^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{1}_{m,1} & x^{1}_{m,2} & \cdots & x^{1}_{m,m} \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
x^{1}_{1,1} & x^{1}_{1,2} & \cdots & x^{1}_{1,m}  \\
x^{1}_{2,1} & x^{1}_{2,2} & \cdots & x^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{1}_{m,1} & x^{1}_{m,2} & \cdots & x^{1}_{m,m} \\
\end{bmatrix}


\cdot

\begin{bmatrix}
w^{2}_{1,1}  \\
w^{2}_{2,1}  \\
\vdots  \\
w^{2}_{m,1}  \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{2}_{1,1} \\
b^{2}_{2,1} \\
\vdots \\
b^{2}_{m,1}  \\
\end{bmatrix}

= 

\begin{bmatrix}
a^{2}_{1,1} \\
a^{2}_{2,1} \\ 
\vdots \\
a^{2}_{m,1}  \\
\end{bmatrix}
$$


$$
a^2_{s,1} = x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}
$$

$$
x^{1}_{s,*} \cdot w^2_{*,1} = x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1}
$$






$$
g \bigg (
\begin{bmatrix}
a^{2}_{1,1} \\
a^{2}_{2,1} \\ 
\vdots \\
a^{2}_{m,1}  \\
\end{bmatrix}
\bigg )

= 

\begin{bmatrix}
h^{2}_{1,1} \\
h^{2}_{2,1} \\ 
\vdots \\
h^{2}_{m,1}  \\
\end{bmatrix}
$$



### 第二层偏导



#### 权重偏导


$$
\\

\ for \ s \in 1 \cdots m; \ (x^{1}_{s,*} 代表行向量) \\
a^2_{s,1} = x^{1}_{s,*} \cdot w^2_{*,1}
$$

$$
\ for \ j \in 1 \cdots m; \  s \in 1 \cdots m; \\

\frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) = \frac{\partial}{\partial w^2_{j,1}} g( x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}) \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} a^2_{s,1}  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1})  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} ( x^1_{s,j} w^2_{j,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j} \  \frac{\partial}{\partial w^2_{j,1}} (  w^2_{j,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j}
$$

#### 偏置偏导


$$
\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^2_{j,1}} g( x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}) \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial b^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial b^2_{j,1}} (b^2_{s,1})  \\
$$

$$
\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) =  0, if \ j \neq s  \\

\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) = g(a^2_{s,1})(1 - g(a^2_{s,1})) , if \ j = s  \\ 
$$










$$
\frac{\partial}{\partial w^2_{j,1}} \mathcal{L} = \frac{\partial}{\partial w^2_{j,1}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ j \in 1 \cdots m  \\
\\

= \frac{1}{2m} \sum^{m}_{s=1}\frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})^2   \quad \text{(by linearity of the derivative)} \\


= \frac{1}{2m} \sum^{m}_{s=1} 

2 \cdot (g( a^2_{s,1} ) - y_{s,1}) \frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})   \quad \text{(by chain rule)} \\


= \frac{1}{2m} \cdot 2 \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - \frac{\partial}{\partial w^2_{j,1}} y_{s,1} \bigg ]  \quad \text{(by linearity of the derivative)}  \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - 0 \bigg ]   \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} )  \\


= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \ g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j} \\
$$





### 第一层偏导



#### 权重偏导


$$
\frac{\partial}{\partial w^1_{i,j}} g( a^2_{s,1} ) = g(a^2_{s,1})(1 - g(a^2_{s,1})) \ \frac{\partial}{\partial w^1_{i,j}} (  a^2_{s,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i} \\
$$

$$
\frac{\partial}{\partial w^1_{i,j}} (  a^2_{s,1} ) = \frac{\partial}{\partial w^1_{i,j}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\

= \frac{\partial}{\partial w^1_{i,j}} (x^{1}_{s,*} \cdot w^2_{*,1})  \\

= \frac{\partial}{\partial w^1_{i,j}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\


= \frac{\partial}{\partial w^1_{i,j}} ( x^1_{s,j} w^2_{j,1} )  \\

= \frac{\partial}{\partial w^1_{i,j}} ( g(a^{1}_{s,j}) w^2_{j,1} )  \\

= w^2_{j,1} \frac{\partial}{\partial w^1_{i,j}} ( g(a^{1}_{s,j})  )  \\

=  w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) \frac{\partial}{\partial w^1_{i,j}} a^{1}_{s,j} \\

= w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i} \\
$$

$$
\frac{\partial}{\partial w^1_{i,j}} a^{1}_{s,j} = \frac{\partial}{\partial w^1_{i,j}}(x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j}) \\

= \frac{\partial}{\partial w^1_{i,j}}(x^{0}_{s,i} w^{1}_{i,j} ) \\

= x^{0}_{s,i} \frac{\partial}{\partial w^1_{i,j}}( w^{1}_{i,j} ) \\

= x^{0}_{s,i}
$$






$$
x^{1}_{s,*} \cdot w^2_{*,1} = x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1}
$$

$$
x^{1}_{s,j} = g(a^{1}_{s,j}) \\
= g(x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j})
$$

$$
a^{1}_{s,j} = x^{0}_{s,*} \cdot w^{1}_{*,j} \\
=
x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j}  \\
$$





$$
\frac{\partial}{\partial w^1_{i,j}} \mathcal{L} = \frac{\partial}{\partial w^1_{i,j}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ i \in 1 \cdots n; \ j \in 1 \cdots m  \\
\\


= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial w^1_{i,j}} g( a^2_{s,1} )  \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) g(a^2_{s,1})(1 - g(a^2_{s,1})) w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i}  \\
$$




#### 偏置偏导


$$
\frac{\partial}{\partial b^1_{k,j}} \mathcal{L} = \frac{\partial}{\partial b^1_{k,j}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ k \in 1 \cdots m; \ j \in 1 \cdots m  \\
\\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} )  \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\

= \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,j} w^2_{j,1} )  \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,j} w^2_{j,1} ),  if \ k = s \\
= \frac{\partial}{\partial b^1_{k,j}} ( g(a^1_{s,j}) w^2_{j,1} ) \\

= \frac{\partial}{\partial b^1_{k,j}} ( g(a^1_{s,j}) w^2_{j,1} ) \\

= w^2_{j,1} \frac{\partial}{\partial b^1_{k,j}} g(a^1_{s,j})  \\


= w^2_{j,1} g(a^1_{s,j}) (1-g(a^1_{s,j}) ) \frac{\partial}{\partial b^1_{k,j}} (a^1_{s,j})  \\

= w^2_{j,1} g(a^1_{s,j}) (1-g(a^1_{s,j}) )
$$

$$
\frac{\partial}{\partial b^1_{s,j}} (a^1_{s,j}) = \frac{\partial}{\partial b^1_{s,j}} (  x^{0}_{s,*} \cdot  w^{1}_{*,j} + b^1_{s,j}) \\
= 1 \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = 0,  if \ k \neq s \\
$$

































