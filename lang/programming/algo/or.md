# 与门单层神经网络实现



## 神经网络实现的是向量x 到向量 h的仿射变换



> 仿射变换相比线性变换多了一个平移，原点变了  
> 线性变换保证几何体的形状和比例不变  
> 平移是通过加上一个常量既偏置完成的  



输入信号矩阵左乘权重矩阵，求出输入信号的加权和，激活函数把若干个加权和压缩到0 和1 之间，这就是隐层的单元了，隐层单元又作为输入信号开始新一轮的计算，最后在输出层得到前向传播的最终结果，这就是预测值

> 利用梯度下降或反向传播算法不断的更新权重，从而减小预测值和期望值之间的误差  
> 当误差小到一定范围时神经网络就训练好了



## 梯度是偏导数的向量

> 但是仍然使用：“x上的梯度” 这样的术语，因为简单  
>
> 梯度指示的方向是各点处的函数值减小最多的方向
>
> 函数关于每个变量的偏导数指明了整个表达式对于该变量的敏感程度  
>
> 反向传播，可以计算各个节点的导数  
>
> 通过比较数值微分和误差反向传播法的结果，可以确认误差反向传播法的实现是否正确（梯度确认）



## 有向无环图

> 有向无环图未必能转化成树，但任何有向树均为有向无环图



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
W := W - \alpha X^{T} \cdot E
$$






