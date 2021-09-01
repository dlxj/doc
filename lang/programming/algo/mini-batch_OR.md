

```
用随机选择的小批量数据（mini-batch）作为全体训练数据的近似值，损失函数要计算这一批数据的总体损失

OR 问题的每一个输入维度是 (2,) , batch 大小设为3，既每次训练三组输入数据，作为全体训练数据的近似


使用双隐层网络结构，矩阵的维度变化：
	(3,2).(2,2) = (3,2)
```



$m=3, n=2, c=2, nclass=2$


$$
\begin{bmatrix}
x^{0}_{1,1} & x^{0}_{1,2} & \cdots & x^{0}_{1,n}  \\
x^{0}_{2,1} & x^{0}_{2,2} & \cdots & x^{0}_{2,n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{0}_{m,1} & x^{0}_{m,2} & \cdots & x^{0}_{m,n} \\
\end{bmatrix}

\cdot

\begin{bmatrix}
w^{1}_{1,1} & w^{1}_{1,2} & \cdots & w^{1}_{1,c}  \\
w^{1}_{2,1} & w^{1}_{2,2} & \cdots & w^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{1}_{n,1} & w^{1}_{n,2} & \cdots & w^{1}_{n,c} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{1}_{1,1} & b^{1}_{1,2} & \cdots & b^{1}_{1,c}  \\
b^{1}_{2,1} & b^{1}_{2,2} & \cdots & b^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
b^{1}_{m,1} & b^{1}_{m,2} & \cdots & b^{1}_{m,c} \\
\end{bmatrix}

\\

= 

\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,c}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,c} \\
\end{bmatrix}
$$

$$
a^{1}_{1,1} = x^0_{1,*} \cdot w^1_{*,1} \\
= x^0_{1,1} w^1_{1,1} + x^0_{1,2} w^1_{2,1} + \cdots + x^0_{1,n} w^1_{n,1}
$$

$$
a^{1}_{1,c} = x^0_{1,*} \cdot w^1_{*,c} \\
= x^0_{1,1} w^1_{1,c} + x^0_{1,2} w^1_{2,c} + \cdots + x^0_{1,n} w^1_{n,c}
$$

$$
a^{1}_{m,c} = x^0_{m,*} \cdot w^1_{*,c} \\
= x^0_{m,1} w^1_{1,c} + x^0_{m,2} w^1_{2,c} + \cdots + x^0_{m,n} w^1_{n,c}
$$


$$
\frac{ \partial }{ \partial w^1_{s,r} } a^1_{i,j} = 0, if \ r  \neq j
$$

$$
\frac{ \partial }{ \partial w^1_{s,r} } a^1_{i,j} = x^0_{i,s} \ , if \ r  = j
$$






$$
Softmax \bigg (

\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,c}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,c} \\
\end{bmatrix}

\bigg ) 


\\ =

\begin{bmatrix}
p_{1,1} & p_{1,2} & \cdots & p_{1,nclass}  \\
p_{2,1} & p_{2,2} & \cdots & p_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
p_{m,1} & p_{m,2} & \cdots & p_{m,ncalss} \\
\end{bmatrix}
$$

$$
CE \bigg (

\begin{bmatrix}
p_{1,1} & p_{1,2} & \cdots & p_{1,nclass}  \\
p_{2,1} & p_{2,2} & \cdots & p_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
p_{m,1} & p_{m,2} & \cdots & p_{m,ncalss} \\
\end{bmatrix}

\bigg ) 


\\ =

\begin{bmatrix}
ce_{1,1} \\
ce_{2,1}  \\
\vdots  \\
ce_{m,1} \\
\end{bmatrix}
$$

$$
L \bigg (

\begin{bmatrix}
ce_{1,1} \\
ce_{2,1}  \\
\vdots  \\
ce_{m,1} \\
\end{bmatrix}

\bigg ) 


= 

\frac{1}{m} \sum^{m}_{i=1} ce_{i,1}
$$








