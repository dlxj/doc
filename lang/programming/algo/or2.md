[TOC]



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
X = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])   # 4*3
```

> OR 门四组输入，也就是要有四组坐标，所以行数是4  
> 每组输入有两个维度，再把偏置项1 加进来，共三个维度，所以列数是3



对于OR 问题，上述公式中：m = 4, n = 2。有：
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


  $x^{(1)}$ 读作第一行，$x^{(1)}_{0}$ 读作第一行的第一维，$x^{(1)}_{1}$ 读作第一行的第二维。

> 既 X 的维度是：m * (n+1)






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



对于OR 问题 n = 2, 有：

$$
W =
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
w_{2}  \\
\end{bmatrix}
=
\begin{bmatrix}
rand  \\
rand  \\
rand  \\
\end{bmatrix}
$$



```python
W = np.random.uniform(size=(3,1))         # 3*1
```



## Activation Function



### Sigmoid Function



$$
h(x) = \frac{1}{1 + e^{-x}}
$$



> e 是欧拉数（Euler’s number），近似数值 2.718281，是一个无理数
>
> Sigmoid 意为“S形的”



```python
def sigmoid (x):
    return 1 / (1 + np.exp(-x))
```

```python
def sigmoid_derivative(x):
    return x * (1 - x)
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
\end{bmatrix}
$$


$$
h(A) = \frac{1}{1 + e^{-A}}=\frac{1}{1 + e^{-X \cdot W}}
$$




## Cost function



[Derivative of a cost function (Andrew NG machine learning course)](https://math.stackexchange.com/questions/3581373/derivative-of-a-cost-function-andrew-ng-machine-learning-course)

[Partial derivative in gradient descent for two variables](https://math.stackexchange.com/questions/70728/partial-derivative-in-gradient-descent-for-two-variables)

$$
J(W) = \frac{1}{2 m} \sum^{m}_{i=1}(h_{W}(x^{(i)})-y^{(i)})^2
$$


其中hypothesis (预测) $h_{W}$ 为：


$$
h_{W}(x^{(i)}) = \frac{1}{1 + e^{-x^{(i)} \cdot W}}
$$


W 是待求的变量，X 和Y 看成常量，目标是求使**均方代价函数**$J(W)$ 值最小的W。





### partial derivatives



#### 偏导数的计算方法



> 偏的意思是“偏心”，只把你关心的参数看成是变量，其他参数全部认为是常量
>



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
h_{W}(x^{(i)}) = \frac{1}{1 + e^{-x^{(i)} \cdot W}}  \\
f(w_{0},w_{1},w_{2})^{i} = h_{W}(x^{(i)}) - y^{i} = \frac{1}{1 + e^{-x^{(i)} \cdot W}} - y^{(i)} \\
= \frac{1}{1 + e^{- (w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2})}} - y^{(i)}
$$


整个损失函数求偏导：
$$
J(W) = \frac{1}{2 m} \sum^{m}_{i=1}(h_{W}(x^{(i)})-y^{(i)})^2 \\
J(w_{0}, w_{1}, w_{2}) = \frac{1}{2 m} \sum^{m}_{i=1}(h_{W}(x^{(i)})-y^{(i)})^2 \\
\frac{\partial}{\partial w_{0}} J(w_{0}, w_{1}, w_{2}) = \frac{\partial}{\partial w_{0}} \frac{1}{2m} \sum ^{m}_{i=1}(f(w_{0},w_{1},w_{2})^{i})^2 \\
= \frac{1}{m} \sum ^{m}_{i=1}f(w_{0},w_{1},w_{2})^{i}
$$















$$
J(f(w_{0},w_{1},w_{2})^{i}) = \frac{1}{2 m} \sum^{m}_{i=1}(f(w_{0},w_{1},w_{2})^{i})^2 \\
\frac{\partial}{\partial w_{0}} J(f(w_{0},w_{1},w_{2})^{i}) = 
\frac{1}{m} \sum^{m}_{i=1}(f(w_{0},w_{1},w_{2})^{i}) \\
= \frac{1}{m} \sum^{m}_{i=1} \frac{1}{1 + e^{- (w_{0} x^{(i)}_{0} + w_{1} x^{(i)}_{1} + w_{2} x^{(i)}_{2})}} - y^{(i)}
$$







## Gradient descent




$$
w_{j} := w_{j} - \alpha \frac{1}{m} \sum^{m}_{i=1}(h_{W}(x^{(i)}-y^{(i)}) x^{(i)}_{j}
$$




### 















