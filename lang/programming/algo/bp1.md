



# 反向传播算法(Backpropagation)





## 前向传播(Forward propagation)



上标是行，下标是列。**上下标带括号的是向量**，否则是标量

> 行向量是多维空间的一个点由不同维度的坐标组成的向量。  
> 列向量是多维空间的多个点的同一维度的坐标组成的向量。

矩阵用大写字母表示，矩阵里的向量用小写字母加上下标表示



W的维度变化见： 《DeepLearningBook-chinese》p.151



$$
X = 
\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{n}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{1} & x^{m}_{2} & \cdots & x^{m}_{n} \\
\end{bmatrix}
$$



$$
W = 
\begin{bmatrix}
w^{1}_{1} & w^{1}_{2} & \cdots & w^{1}_{n}  \\
w^{2}_{1} & w^{2}_{2} & \cdots & w^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{n}_{1} & w^{n}_{2} & \cdots & w^{n}_{n} \\
\end{bmatrix}
$$



$$
V = 
\begin{bmatrix}
v^{1} \\
v^{2} \\
\vdots    \\
v^{n} \\
\end{bmatrix}
$$




$$
X \cdot W = 
\begin{bmatrix}
x^{(1)} \cdot w_{(1)} & x^{(1)} \cdot w_{(2)} & \cdots & x^{(1)} \cdot w_{(n)}  \\
x^{(2)} \cdot w_{(1)} & x^{(2)} \cdot w_{(2)} & \cdots & x^{(2)} \cdot w_{(n)}  \\
\vdots & \vdots & \ddots & \vdots & \\
x^{(m)} \cdot w_{(1)} & x^{(m)} \cdot w_{(2)} & \cdots & x^{(m)} \cdot w_{(n)}  \\
\end{bmatrix}
$$




$$
H(X,W,C) = X \cdot W + C= 
\begin{bmatrix}
x^{(1)} \cdot w_{(1)} + c & x^{(1)} \cdot w_{(2)} + c & \cdots & x^{(1)} \cdot w_{(n)} + c  \\
x^{(2)} \cdot w_{(1)} + c & x^{(2)} \cdot w_{(2)} + c & \cdots & x^{(2)} \cdot w_{(n)} + c  \\
\vdots & \vdots & \ddots & \vdots & \\
x^{(m)} \cdot w_{(1)} + c & x^{(m)} \cdot w_{(2)} + c & \cdots & x^{(m)} \cdot w_{(n)} + c  \\
\end{bmatrix}
\\
=
\begin{bmatrix}
h^{(1)} \\
h^{(2)}   \\
\vdots  \\
h^{(m)}  \\
\end{bmatrix}
$$


$$
g( H(X,W,C) ) = 
\begin{bmatrix}
g(h^{(1)}) \\
g(h^{(2)})   \\
\vdots  \\
g(h^{(m)})  \\
\end{bmatrix}
\\
= 
\begin{bmatrix}
g( x^{(1)} \cdot w_{(1)} + c ) & g( x^{(1)} \cdot w_{(2)} + c ) & \cdots & g ( x^{(1)} \cdot w_{(n)} + c )  \\
g( x^{(2)} \cdot w_{(1)} + c ) & g( x^{(2)} \cdot w_{(2)} + c ) & \cdots & g( x^{(2)} \cdot w_{(n)} + c )  \\
\vdots & \vdots & \ddots & \vdots & \\
g( x^{(m)} \cdot w_{(1)} + c ) & g( x^{(m)} \cdot w_{(2)} + c ) & \cdots & g( x^{(m)} \cdot w_{(n)} + c ) \\
\end{bmatrix}
$$




$$
O = 
g( H(X,W,C) ) \ \cdot \ V + B= 
\begin{bmatrix}
g(h^{(1)}) \\
g(h^{(2)})   \\
\vdots  \\
g(h^{(m)})  \\
\end{bmatrix} 

\cdot

\begin{bmatrix}
v^{1} \\
v^{2} \\
\vdots    \\
v^{n} \\
\end{bmatrix}
+ B
\\
= 
\begin{bmatrix}
g(h^{(1)}) \cdot V \\
g(h^{(2)}) \cdot V  \\
\vdots  \\
g(h^{(m)}) \cdot V \\
\end{bmatrix}
+ B
\\
=
\begin{bmatrix}
( v^{1} g( x^{(1)} \cdot w_{(1)} + c ) ) + ( v^{2} g( x^{(1)} \cdot w_{(2)} + c ) ) + \cdots + ( v^{n} g ( x^{(1)} \cdot w_{(n)} + c ) ) + b \\
( v^{1} g( x^{(2)} \cdot w_{(1)} + c ) ) + ( v^{2} g( x^{(2)} \cdot w_{(2)} + c ) ) + \cdots + ( v^{n} g( x^{(2)} \cdot w_{(n)} + c ) ) + b\\
\vdots \\
( v^{1} g( x^{(m)} \cdot w_{(1)} + c ) ) + ( v^{2} g( x^{(m)} \cdot w_{(2)} + c ) ) + \cdots + ( v^{n} g( x^{(m)} \cdot w_{(n)} + c ) ) + b\\
\end{bmatrix}
$$















$$
V = 
\begin{bmatrix}
v^{1} \\
v^{2} \\
\vdots    \\
v^{n} \\
\end{bmatrix}
$$


> 隐层的权重行列数都等于X 的列数，所以隐层的维度和X 相同，在最后一层权重的列数设为1，既可将最终输出变成1列




$$
h_{W}(X) + C =
X \cdot W + C
=
\begin{bmatrix}
h_{w_{(1)}}(X) \quad h_{w_{(2)}}(X) \ \ ...  \ \ h_{w_{(n)}}(X) 
\end{bmatrix}
+ C
\\
= 
\begin{bmatrix}
h_{w_{(1)}}(X) + c \quad h_{w_{(2)}}(X) + c \ \ ...  \ \ h_{w_{(n)}}(X) + c 
\end{bmatrix}
$$

> C 的维度和X 一至


$$
h_{w_{(1)}}(X) = X \cdot w_{(1)} = 
\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{n}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{1} & x^{m}_{2} & \cdots & x^{m}_{n} \\
\end{bmatrix}

\cdot

\begin{bmatrix}
w^{1}_{1} \\
w^{2}_{1} \\
\vdots \\
w^{n}_{1}
\end{bmatrix}
=
\begin{bmatrix}
w^{1}_{1} x^{1}_{1} + w^{2}_{1} x^{1}_{2} + \cdots + w^{n}_{1} x^{1}_{n}  \\
w^{1}_{1} x^{2}_{1} + w^{2}_{1} x^{2}_{2} + \cdots + w^{n}_{1} x^{2}_{n} \\
\vdots  \\
w^{1}_{1} x^{m}_{1} + w^{2}_{1} x^{m}_{2} + \cdots + w^{n}_{1} x^{m}_{n} \\
\end{bmatrix}
$$



$$
g( h_{W}(X) + C) =
\begin{bmatrix}
g(h_{w_{(1)}}(X) + c) \quad g(h_{w_{(2)}}(X) + c) \ \ ...  \ \ g(h_{w_{(n)}}(X) + c) 
\end{bmatrix}
$$



$$
H = g ( g( h_{W}(X) + C) \cdot V ) + B
$$



$$
J(X,W,C,V,B) = 
 \frac{1}{2m} \sum^{m}_{i=1}(h^i - y^{i})^2 \\
 =
 \frac{1}{2m} \sum^{m}_{i=1}( g ( g( h_{W}(X) + C) \cdot V ) + B - y^i )^2
\\
$$










上标是行，下标是列。**上标带括号的是行向量**，否则是标量

> 行向量是多维空间的一个点由不同维度的坐标组成的向量。  
> 列向量是多维空间的多个点的同一维度的坐标组成的向量。

矩阵用大写字母表示，矩阵里的向量用小写字母加上下标表示



k = 0，则$X^k$ 是原始输入

k > 0,  则$X^k$ 是前一层($X^{k-1}$)的输出，后一层的输入


$$
X^k = 
\begin{bmatrix}
x^{k}_{1,0} & x^{k}_{1,1} & \cdots & x^{k}_{1,n}  \\
x^{k}_{2,0} & x^{k}_{2,1} & \cdots & x^{k}_{2,n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{k}_{m,0} & x^{k}_{m,1} & \cdots & x^{k}_{m,n} \\
\end{bmatrix}
$$


$$
W^{k} =
\begin{bmatrix}
w^{k}_{0}  \\
w^{k}_{1}  \\
\vdots \\
w^{k}_{n}  \\
\end{bmatrix}
$$


$$
Y =
\begin{bmatrix}
y^{1}  \\
y^{2}  \\
...  \\
y^{m}  \\
\end{bmatrix}
$$





$$
h_{W}(X) =
X \cdot W
=
\begin{bmatrix}
x^{1}_{0} & x^{1}_{1} & \cdots & x^{1}_{n}  \\
x^{2}_{0} & x^{2}_{1} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{0} & x^{m}_{1} & \cdots & x^{m}_{n} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
\vdots \\
w_{n}  \\
\end{bmatrix}
=
\begin{bmatrix}
w_{0} x^{1}_{0} + w_{1} x^{1}_{1} + \ \cdots \  + w_{n} x^{1}_{n}  \\
w_{0} x^{2}_{0} + w_{1} x^{2}_{1} +\ \cdots \  + w_{n} x^{2}_{n}  \\
\vdots \\
w_{0} x^{m}_{0} + w_{1} x^{m}_{1} + \ \cdots \  + w_{n} x^{m}_{n}  \\
\end{bmatrix}  \\
=
\begin{bmatrix}
h_{W}(x^{^{(1)}}) \\
h_{W}(x^{^{(2)}})  \\
...  \\
h_{W}(x^{^{(m)}}) \\
\end{bmatrix}
$$



$$
g(h_{W}(X)) = 
\begin{bmatrix}
g( h_{W}(x^{^{(1)}}) ) \\
g( h_{W}(x^{^{(2)}}) ) \\
... \\
g( h_{W}(x^{^{(m)}}) ) \\
\end{bmatrix}
$$























