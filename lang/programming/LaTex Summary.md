[TOC]

# LaTex Summary



## mathjax



**首先斜体加粗是这个\boldsymbol**

例如\boldsymbol{x}

和\mathbf{x}有区别



**正体** \mathrm{}

$\mathrm{Logistic}\left(a\right)$





**另外在任意Markdown的编辑器中：**

自己设置一下就好：找到mathjax 配置文件写入如下定义tex的代码中的Macros即可定义简写：

```html
<script type="text/x-mathjax-config">
       MathJax.Hub.Config({
        tex2jax: {
          inlineMath: [ ['$','$'], ["\\(","\\)"] ],
          displayMath: [ ['$$', '$$'], ["\\[", "\\]"] ],
          processEscapes: true
        },
        TeX: {
          equationNumbers: {autoNumber: 'AMS'},
          Macros: {bm: "\\boldsymbol"}
        },
        'HTML-CSS': {
          imageFont: null
        }
      });
  </script>
```



```
 \left\langle ... \middle| ... \right\rangle
```

$ \left\langle ... \middle| ... \right\rangle$





一个简单的办法：
chrome打开知乎页面，按顺序 F12 - F1 - 在General 里面点选 Disable JavaScript。就可以复制了。



## 二级下标



向量的长度是向量与原点之间的欧式距离。 3 维乃至更高维向量的长度也是它们与原点之间的 欧氏距离一一各分量平方和的平方根。 


$$
length(\textbf{x}) = \sqrt{x_{_1}^2 + x_{_2}^2}
$$



向量的模定义为**与自身内积的平方根** ： 
$$
\|\boldsymbol{x}\| = \sqrt{\left < \boldsymbol{x},\boldsymbol{x} \right>} 
= \sqrt{\sum^n_{i=1}\boldsymbol{x}_{_i}^2}
$$






## align

$$
\begin{align}
\frac{d \ e^x}{d x} &= \lim \limits_{\Delta x \rightarrow 0} \frac{e^x - e^{x - \Delta x}}{\Delta x} \\
&= e^x \lim \limits_{\Delta x \rightarrow 0} \frac{1 - e^{- \Delta x}}{\Delta x} \\
&= e^x
\end{align}
$$



## tag

$$
\begin{align}
a &= b + c \tag{1} \\
  &= d + e + f \tag{2}
\end{align}
$$







$$
X=
\begin{bmatrix}
0 & 0  \\
0 & 1  \\
1 & 0  \\
1 & 1  \\
\end{bmatrix}
$$


$$
Y=
\begin{bmatrix}
0 \\
1 \\
1 \\
0 \\
\end{bmatrix}
$$





## bigg Big Bigg parentheses 


$$
\frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) = 
\frac{\partial}{\partial w_{j}} \bigg [ \frac{1}{2m} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2 \bigg ] \\
= \frac{1}{2m} \frac{\partial}{\partial w_{j}} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2   \text by linearity of the derivative
$$





## top arrow



$A \overrightarrow{V} = \lambda \overrightarrow{V}$





## 斜体小写字母



黑斜体小写字母表示向量 $\textbf{x}$

斜体小写字母表示标量  $\textit{x}$

矩阵表示一组向量 $X$

上标



## 花体

> $\mathcal{R}(h)$





## 集合符号

### 属于

$$
\vec{y} \in \mathbb{R}^n, \ \vec{y} = (y_1,y_2,\cdots,y_n)
$$


















[Partial derivative in gradient descent for two variables](https://math.stackexchange.com/questions/70728/partial-derivative-in-gradient-descent-for-two-variables)

[小时物理 - 复合函数的偏导 链式法则](http://wuli.wiki/online/PChain.html)

[梯度下降法的推导（非常详细、易懂的推导）](https://blog.csdn.net/pengchengliu/article/details/80932232)



求导方法：

  1.
$$
f(x) = cx^{n} \\
f(x)'= cn \ast x^{n -1}
$$

2. 常量的导数是0

3. 求和符号不影响求导，原来在哪求导完还在哪

4. 应用了链式法则

   $g(f(x))$ 求$g'$ 把$f(x)$ 看成变量


$$
X =
\begin{bmatrix}
x^{(1)}  \\
x^{(2)}  \\
...  \\
x^{(4)}  \\
\end{bmatrix}
=
\begin{bmatrix}
x^{(1)}_{0} & x^{(1)}_{1} & x^{(1)}_{2}  \\
x^{(2)}_{0} & x^{(2)}_{1} & x^{(2)}_{2} \\
... & ... & ... & \\
x^{(4)}_{0} & x^{(4)}_{1} & x^{(4)}_{2} \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0  \\
1 & 0 & 1  \\
1 & 1 & 0 \\
1 & 1 & 1  \\
\end{bmatrix}
$$


$$
h_{W}(X) =
X \cdot W
=
\begin{bmatrix}
x^{(1)}_{0} & x^{(1)}_{1} & x^{(1)}_{2}  \\
x^{(2)}_{0} & x^{(2)}_{1} & x^{(2)}_{2} \\
... & ... & ... & \\
x^{(4)}_{0} & x^{(4)}_{1} & x^{(4)}_{2} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
w_{2}  \\
\end{bmatrix}
=
\begin{bmatrix}
w_{0} x^{(1)}_{0} + w_{1} x^{(1)}_{1} + w_{2} x^{(1)}_{2}  \\
w_{0} x^{(2)}_{0} + w_{1} x^{(2)}_{1} + w_{2} x^{(2)}_{2}  \\
...  \\
w_{0} x^{(4)}_{0} + w_{1} x^{(4)}_{1} + w_{2} x^{(4)}_{2}  \\
\end{bmatrix}  \\
=
\begin{bmatrix}
h_{W}(x^{^{(1)}}) \\
h_{W}(x^{^{(2)}})  \\
...  \\
h_{W}(x^{^{(4)}}) \\
\end{bmatrix}
$$


We have
$$
h_{W}(x^{i}) = w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2}
$$
and
$$
J(w_{0},w_{1},w_{2}) = \frac{1}{2m} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2
$$
We first compute
$$
\frac{\partial}{\partial w_{0}} h_{W}(x^{i}) = \frac{\partial}{\partial w_{0}}(w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2}) \\
= \frac{\partial}{\partial w_{0}} w_{0}x^{i}_{0} + 
\frac{\partial}{\partial w_{0}} w_{1}x^{i}_{1} + 
\frac{\partial}{\partial w_{0}} w_{2}x^{i}_{2} \\
= x^{i}_{0} + 0 + 0 = x^{i}_{0}
$$

$$
\frac{\partial}{\partial w_{1}} h_{W}(x^{i}) = \frac{\partial}{\partial w_{1}}(w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2}) \\
= \frac{\partial}{\partial w_{1}} w_{0}x^{i}_{0} + 
\frac{\partial}{\partial w_{1}} w_{1}x^{i}_{1} + 
\frac{\partial}{\partial w_{1}} w_{2}x^{i}_{2} \\
= 0 + x^{i}_{1} + 0 = x^{i}_{1}
$$

$$
\frac{\partial}{\partial w_{2}} h_{W}(x^{i}) = \frac{\partial}{\partial w_{2}}(w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2}) \\
= \frac{\partial}{\partial w_{2}} w_{0}x^{i}_{0} + 
\frac{\partial}{\partial w_{2}} w_{1}x^{i}_{1} + 
\frac{\partial}{\partial w_{2}} w_{2}x^{i}_{2} \\
= 0 + 0 + x^{i}_{2} = x^{i}_{2}
$$

which we will use later. 



for j=0, 1, 2 :
$$
\frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) = 
\frac{\partial}{\partial w_{j}} \bigg [ \frac{1}{2m} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2 \bigg ] \\
= \frac{1}{2m} \frac{\partial}{\partial w_{j}} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2   \text (by linearity of the derivative)
$$













维度

  列是多维空间的不同维度

​    1列是多维空间中N个点的同一维度坐标组成的向量

  行是多维空间的一组坐标

​    1行是多维空间的一个点



左乘是行变换，右乘是列变换

列向量右乘一个矩阵，左边的矩阵行数没变列数被降维了（被降到和列向量对齐）

> 一列向量作为系数右乘一个矩阵，矩阵降维到一列。降维的方法是矩阵所有的列加仅求和
>
> N列向量右乘一个矩阵，矩阵降维到N列

*2 加倍 *1/2减倍



 一边一权重，算看有多少条边

  二输入每对应一隐层单元就是2 条边，所以“第一间”边上的权重是2*2（间的说法对比五线谱的线间关系， \

  输入层和隐层[也可以认为是中间输出层]分别是第一线，第二线，那么连接它们的边所在位置就是第一间）

  线是line, 间是space， 所以第一间可以用 1th_space 表示



  向量x 到向量 h的仿射变换，仿射变换相比线性变换多了一个平移，原点变了。线性变换保证几何体的形状和比例不变

​    平移是通过加上一个常量，既偏置完成的

​    输入信号作为列向量左乘权重矩阵，求出输入信号的加权和，激活函数把若干个加权和压缩到0 和1 之间，这就是隐层的单元了，隐层单元又作为输入信号开始新一轮的计算，

​      最后在输出层得到前向传播的最终结果，这就是预测值



梯度是偏导数的向量

  但是仍然使用：“x上的梯度” 这样的术语，因为简单

  函数关于每个变量的偏导数指明了整个表达式对于该变量的敏感程度

  反向传播，可以计算各个节点的导数

  通过比较数值微分和误差反向传播法的结果，可以确认误差反向传播法的实现是否正确（梯度确认）



有向无环图

  有向无环图未必能转化成树，但任何有向树均为有向无环图



**随机矩阵**（Stochastic matrix），**所有元素不小于0，每一列的和为1**，状态转移矩阵的最大特征值为1