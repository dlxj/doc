



# 反向传播算法(Backpropagation)





## 前向传播(Forward propagation)



上标是行，下标是列。**上下标带括号的是向量**，否则是标量

> 行向量是多维空间的一个点由不同维度的坐标组成的向量。  
> 列向量是多维空间的多个点的同一维度的坐标组成的向量。

矩阵用大写字母表示，矩阵里的向量用小写字母加上下标表示




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
w^{1}_{1} & w^{1}_{2} & \cdots & w^{1}_{n-1}  \\
w^{2}_{1} & w^{2}_{2} & \cdots & w^{2}_{n-1} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{n}_{1} & w^{n}_{2} & \cdots & w^{n}_{n-1} \\
\end{bmatrix}
$$



$$
h_{W}(X) =
X \cdot W + c
=
\begin{bmatrix}
h_{w_{(1)}}(X) \quad h_{w_{(2)}}(X) \ ...  \ h_{w_{(n-1)}}(X) 
\end{bmatrix}
+ c
$$



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
g^0 = g(h^0) =
\begin{bmatrix}
g( h_{W^{0}}(x^0_{^{(1)}}) ) \\
g( h_{W^{0}}(x^0_{^{(2)}}) )  \\
...  \\
g( h_{W^{0}}(x^0_{^{(m)}}) ) \\
\end{bmatrix}
$$

$$
(g^0)^T = 
\begin{bmatrix}
g( h_{W^{0}}(x^0_{^{(1)}}) ) \quad 
g( h_{W^{0}}(x^0_{^{(2)}}) ) \quad  
... \quad 
g( h_{W^{0}}(x^0_{^{(m)}}) )
\end{bmatrix}
$$


$$
W^{1} =
\begin{bmatrix}
w^{1}_{0}  \\
w^{1}_{1}  \\
\vdots \\
w^{1}_{n}  \\
\end{bmatrix}
$$

$$
h^1 = (g^0)^T \cdot W^1 
=
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























