# 与门单层神经网络实现



## Input Matrix



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






