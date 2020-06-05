# 与门单层神经网络实现



## Input Matrix



上标是行，下标是列

> 行向量是多维空间的一个点由不同维度的坐标组成的向量。
> 列向量是多维空间的多个点的同一维度的坐标组成的向量。



矩阵用大写字母表示，矩阵里的向量用小写字母加上下标表示


$$
X =
\begin{bmatrix}
x^{(1)}  \\
x^{(2)}  \\
...  \\
x^{(m)}  \\
\end{bmatrix}
=
\begin{bmatrix}
x^{(1)}_{0} & x^{(1)}_{1} & ... & x^{(1)}_{n}  \\
x^{(2)}_{0} & x^{(2)}_{1} & ... & x^{(2)}_{n}  \\
... & ... & ... & ...  \\
x^{(m)}_{0} & x^{(m)}_{1} & ... & x^{(m)}_{n}  \\
\end{bmatrix}
$$



```python
X = np.array([[0,0],[0,1],[1,0],[1,1]])   # 4*2
```

> OR 门四组输入，也就是要有四组坐标，所以行数是4
> 每组输入有两个维度，所以列数是2



对于OR 问题，上述公式中：m = 4, n = 1。有：


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
x^{(1)}_{0} & x^{(1)}_{1}  \\
x^{(2)}_{0} & x^{(2)}_{1}  \\
... & ... & \\
x^{(4)}_{0} & x^{(4)}_{1}  \\
\end{bmatrix}
=
\begin{bmatrix}
0 & 0  \\
0 & 1  \\
1 & 0 \\
1 & 1  \\
\end{bmatrix}
$$



  $x^{(1)}$ 读作第一行，$x^{(1)}_{0}$ 读作第一行的第一维。






## Output Matrix


$$
Y =
\begin{bmatrix}
y^{(1)}  \\
y^{(2)}  \\
...  \\
y^{(m)}  \\
\end{bmatrix}
$$

对于OR 问题 m = 4, 有：

$$
Y =
\begin{bmatrix}
y^{(1)}  \\
y^{(2)}  \\
...  \\
y^{(4)}  \\
\end{bmatrix}
=
\begin{bmatrix}
0  \\
1  \\
1  \\
1  \\
\end{bmatrix}
$$


```python
Y = np.array([[0],[1],[1],[1]]) # 4*1
```





## Weight Matrix

$$
W =
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
...  \\
w_{n}  \\
\end{bmatrix}
$$



对于OR 问题 n = 1, 有：

$$
W =
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
\end{bmatrix}
=
\begin{bmatrix}
rand  \\
rand  \\
\end{bmatrix}
$$



```python
W = np.random.uniform(size=(2,1))         # 2*1
```



## Forward propagation


$$
A =
X.W
=
\begin{bmatrix}
x^{(1)}_{0} & x^{(1)}_{1} & ... & x^{(1)}_{n}  \\
x^{(2)}_{0} & x^{(2)}_{1} & ... & x^{(2)}_{n}  \\
... & ... & ... & ...  \\
x^{(m)}_{0} & x^{(m)}_{1} & ... & x^{(m)}_{n}  \\
\end{bmatrix}
\cdot
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
...  \\
w_{n}  \\
\end{bmatrix}
$$


对于OR 问题，m = 4, n = 1。有：


$$
A =
X \cdot W
=
\begin{bmatrix}
x^{(1)}_{0} & x^{(1)}_{1}  \\
x^{(2)}_{0} & x^{(2)}_{1}  \\
... & ... & \\
x^{(4)}_{0} & x^{(4)}_{1}  \\
\end{bmatrix}
\cdot
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
\end{bmatrix}
=
\begin{bmatrix}
w_{0} x^{(1)}_{0} + w_{1} x^{(1)}_{1}  \\
w_{0} x^{(2)}_{0} + w_{1} x^{(2)}_{1}  \\
...  \\
w_{0} x^{(4)}_{0} + w_{1} x^{(4)}_{1}  \\
\end{bmatrix}
$$



## Error Loss


$$
E =
h_{w}(X) - Y
=
g(A) - Y
=
\begin{bmatrix}
g(A^{1}) - y^{(1)}  \\
g(A^{2}) - y^{(2)}  \\
...  \\
g(A^{m}) - y^{(m)}  \\
\end{bmatrix}
=
\begin{bmatrix}
e^{1}  \\
e^{2}  \\
...  \\
e^{m}  \\
\end{bmatrix}
$$


g 是激活函数，$g(A^{1})$ 是第一组输入的输出结果，这里没有考虑偏置项b

- 完整形式应该是$g(A + b)$

  > 其中A 是1列向量，b 也是1 列向量





## Weight Update


$$
w_{0} := w_{0} - \alpha \sum^{m}_{j=1} ( h_{w}(x^{i}) - y^{i} ) x^{i}_{0} \\
= w_{0} - \alpha \sum^{m}_{j=1} e^{i} x^{i}_{0}  \\
= w_{0} - \alpha ( x^{1}_{0} , x^{2}_{0} , ... , x^{m}_{0} ) \cdot E
$$


更一般地有：
$$
w_{j} := w_{j} - \alpha ( x^{1}_{j} , x^{2}_{j} , ... , x^{m}_{j} ) \cdot E
$$
所以有：


$$
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
...  \\
w_{n}  \\
\end{bmatrix}
:=
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
...  \\
w_{n}  \\
\end{bmatrix}
-
\alpha 
\begin{bmatrix}
x^{(1)}_{0} & x^{(2)}_{0} & ... & x^{(m)}_{0}  \\
x^{(1)}_{1} & x^{(2)}_{1} & ... & x^{(m)}_{1}  \\
... & ... & ... & ...  \\
x^{(1)}_{n} & x^{(2)}_{n} & ... & x^{(m)}_{n}  \\
\end{bmatrix}
\cdot
E
$$



既：


$$
W := W - \alpha  X^{T} \cdot E
$$






