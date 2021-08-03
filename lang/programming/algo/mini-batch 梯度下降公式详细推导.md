

## mini-batch



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

$$
for \ i,j \in 1 \cdots n; \\

\begin{bmatrix}
x^{0}_{i,1} & x^{0}_{i,2} & \cdots & x^{0}_{i,m}  \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
w^{1}_{1,j}  \\
w^{1}_{2,j}  \\
\vdots  \\
w^{1}_{m,j}  \\
\end{bmatrix}

+  b^1_{i,j}

 =
 
 a^1_{i,j} \\
$$

$$
for \ i \in 1 \cdots n; \\

\begin{bmatrix}
x^{1}_{i,1} & x^{1}_{i,2} & \cdots & x^{1}_{i,n}  \\
\end{bmatrix}


\cdot

\begin{bmatrix}
w^{2}_{1,1}  \\
w^{2}_{2,1}  \\
\vdots  \\
w^{2}_{n,1}  \\
\end{bmatrix}

+ 


b^{2}_{i,1} 

= 

a^{2}_{i,1}
$$



### 第二层偏导


$$
\\

\ for s \in 1 \cdots m; \ (x^{1}_{s,} 代表行向量) \\
a^2_{s,1} = x^{1}_{s,} \cdot w^2
$$

$$
\ for \ j \in 1 \cdots m; \  s \in 1 \cdots m; \\

\frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) = \frac{\partial}{\partial w^2_{j,1}} g( x^{1}_{s,} \cdot w^2 ) \\
$$






$$
\frac{\partial}{\partial w^2_{j,1}} \mathcal{L} = \frac{\partial}{\partial w^2_{j,1}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ j \in 1 \cdots m  \\
\\

= \frac{1}{2m} \sum^{m}_{i=1}\frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})^2   \quad \text{(by linearity of the derivative)} \\


= \frac{1}{2m} \sum^{m}_{i=1} 

2 \cdot (g( a^2_{s,1} ) - y_{s,1}) \frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})   \quad \text{(by chain rule)} \\


= \frac{1}{2m} \cdot 2 \sum^{m}_{i=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - \frac{\partial}{\partial w^2_{j,1}} y_{s,1} \bigg ]  \quad \text{(by linearity of the derivative)}  \\

= \frac{1}{m} \sum^{m}_{i=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - 0 \bigg ]   \\
$$







