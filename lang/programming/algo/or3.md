



[Partial derivative in gradient descent for two variables](https://math.stackexchange.com/questions/70728/partial-derivative-in-gradient-descent-for-two-variables)

[How is the cost function from Logistic Regression derivated](https://stats.stackexchange.com/questions/278771/how-is-the-cost-function-from-logistic-regression-derivated)

[Derivative of Cost Function for Logistic Regression](https://medium.com/analytics-vidhya/derivative-of-log-loss-function-for-logistic-regression-9b832f025c2d)

[复合函数求导方法](https://www.jianshu.com/p/29a9c2c424e5)

[小时物理 - 复合函数的偏导 链式法则](http://wuli.wiki/online/PChain.html)

[梯度下降法的推导（非常详细、易懂的推导）](https://blog.csdn.net/pengchengliu/article/details/80932232)

[梯度下降法 —— 经典的优化方法](https://zhuanlan.zhihu.com/p/36564434)

- 泰勒公式给出了函数最小化的方法

[怎样更好地理解并记忆泰勒展开式](https://www.zhihu.com/question/25627482)

- 拉格朗日中值定理

  柯西中值定理

欧拉-拉格朗日方程(Euler -Lagrange equation)





函数的微分与自变量的微分之商等于该函数的导数。因此，导数也叫做微商

可微的函数，其微分等于导数乘以自变量的微分













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
\frac{d}{dx} c = 0, \ \frac{d}{dx} x = 1, \\
\frac{d}{dx} [c\cdot f(x)] = c\cdot\frac{df}{dx} \ \ \ \text{(linearity)}, \\
\frac{d}{dx}[f(x)+g(x)] = \frac{df}{dx} + \frac{dg}{dx} \ \ \ \text{(linearity)},  \\
\frac{d}{dx}[f(x)]^2 = 2f(x)\cdot\frac{df}{dx} \ \ \ \text{(chain rule)}.
$$




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

so:



for j=0, 1, 2；i = 1,2,3,4:

$$
\frac{\partial}{\partial w_{j}} h_{W}(x^{i}) = x^{i}_{j}
$$






which we will use later. 



for j=0, 1, 2 :
$$
\frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) = 
\frac{\partial}{\partial w_{j}} \bigg [ \frac{1}{2m} \sum^{m}_{i=1}(h_{W}(x^{i}) - y^{i})^2 \bigg ] \\
= \frac{1}{2m} \sum^{m}_{i=1}\frac{\partial}{\partial w_{j}} (h_{W}(x^{i}) - y^{i})^2   \quad \text{(by linearity of the derivative)} \\
= \frac{1}{2m} \cdot 2 \sum^{m}_{i=1} (h_{W}(x^{i}) - y^{i}) \frac{\partial}{\partial w_{j}} (h_{W}(x^{i}) - y^{i}) \quad \text{(by chain rule)} \\
= \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{i}) - y^{i}) 
\bigg [ \frac{\partial}{\partial w_{j}} h_{W}(x^{i}) - 0 \bigg ] \\
= \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{i}) - y^{i}) \frac{\partial}{\partial w_{j}} h_{W}(x^{i}) \\
= \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{i}) - y^{i}) x^{i}_{j}
$$

​										



Lagrange's Mean Value Theorem （拉格朗日中值定理）


$$
f(x + \Delta x) = f(x) + f'(x + \theta \Delta x) \Delta x, 0 < \theta < 1
$$
so:
$$
f(x + \Delta x ) \simeq f(x) + \Delta x \nabla f(x)
$$

> 也可以从泰勒公式的一阶展开推导



从微商的定义推导

> $$
> \Delta x = x_{0} - x_{1} \quad \text{and} \quad \Delta x \rightarrow 0 \\
> 
> \nabla f(x) = \frac{f(x + \Delta x) - f(x)}{ \Delta x } \\
> \Delta x \nabla f(x) = f(x + \Delta x) - f(x) \\
> f(x + \Delta x) = f(x) + \Delta x \nabla f(x)
> $$



我们是想要x 移动一小步后函数值变小，既：
$$
f(x + \Delta x) < f(x)
$$
只需：$\Delta x \nabla f(x) < 0$，令 $ \Delta x = - \alpha \nabla f(x), \quad (\alpha > 0) $


$$
\Delta x \nabla f(x) = - \alpha (\nabla f(x))^{2}
$$


so:
$$
f(x + \Delta x) = f(x - \alpha \Delta f(x)) < f(x)
$$


所以，要让函数变小，x 的更新方法是：
$$
x' \leftarrow x - \alpha \Delta f(x)
$$

$$
w_{j} := w_{j} - \alpha \frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) \\
= w_{j} - \alpha \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{i}) - y^{i}) x^{i}_{j}
$$



## OR Gate



上标是行，下标是列。**上标带括号的是行向量**，否则是标量

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
x^{1}_{0} & x^{1}_{1} & ... & x^{1}_{n}  \\
x^{2}_{0} & x^{2}_{1} & ... & x^{2}_{n}  \\
... & ... & ... & ...  \\
x^{m}_{0} & x^{m}_{1} & ... & x^{m}_{n}  \\
\end{bmatrix}
$$


for m = 4, n = 1 ：


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
x^{1}_{0} & x^{1}_{1} & x^{1}_{2}  \\
x^{2}_{0} & x^{2}_{1} & x^{2}_{2} \\
... & ... & ... & \\
x^{4}_{0} & x^{4}_{1} & x^{4}_{2} \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0  \\
1 & 0 & 1  \\
1 & 1 & 0 \\
1 & 1 & 1  \\
\end{bmatrix}
$$



  $x^{(1)}$ 读作第一行，$x^{1}_{0}$ 读作第一行的第一维。



### Output Matrix


$$
Y =
\begin{bmatrix}
y^{1}  \\
y^{2}  \\
...  \\
y^{m}  \\
\end{bmatrix}
$$

for m = 4 ：

$$
Y =
\begin{bmatrix}
y^{1}  \\
y^{2}  \\
...  \\
y^{4}  \\
\end{bmatrix}
=
\begin{bmatrix}
0  \\
1  \\
1  \\
1  \\
\end{bmatrix}
$$



### Weight Matrix

$$
W =
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
...  \\
w_{n}  \\
\end{bmatrix}
$$



for n = 2 ：

$$
W =
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
w_{2}  \\
\end{bmatrix}
$$





### Forward propagation



$$
h_{W}(X) =
X \cdot W
=
\begin{bmatrix}
x^{1}_{0} & x^{1}_{1} & x^{1}_{2}  \\
x^{2}_{0} & x^{2}_{1} & x^{2}_{2} \\
... & ... & ... & \\
x^{4}_{0} & x^{4}_{1} & x^{4}_{2} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
w_{0}  \\
w_{1}  \\
w_{2}  \\
\end{bmatrix}
=
\begin{bmatrix}
w_{0} x^{1}_{0} + w_{1} x^{1}_{1} + w_{2} x^{1}_{2}  \\
w_{0} x^{2}_{0} + w_{1} x^{2}_{1} + w_{2} x^{2}_{2}  \\
...  \\
w_{0} x^{4}_{0} + w_{1} x^{4}_{1} + w_{2} x^{4}_{2}  \\
\end{bmatrix} \\
= \begin{bmatrix}
h_{W}(x^{(1)})  \\
h_{W}(x^{(2)})  \\
...  \\
h_{W}(x^{(m)})  \\
\end{bmatrix}
$$



### Errors


$$
E =
h_{w}(X) - Y
=
\begin{bmatrix}
h_{W}(x^{1}) - y^{1}  \\
h_{W}(x^{2}) - y^{2}  \\
...  \\
h_{W}(x^{m}) - y^{m}  \\
\end{bmatrix}
=
\begin{bmatrix}
e^{1}  \\
e^{2}  \\
...  \\
e^{m}  \\
\end{bmatrix}
$$


### Cost function




$$
\frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) = 
\frac{\partial}{\partial w_{j}} \bigg [ \frac{1}{2m} \sum^{m}_{i=1}(h_{W}(x^{(i)}) - y^{i})^2 \bigg ] \\
= \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{(i)}) - y^{i}) x^{i}_{j} \\
= \frac{1}{m} \sum^{m}_{i=1} e^{i} x^{i}_{j}
$$

### Weight update


$$
w_{j} := w_{j} - \alpha \frac{\partial}{\partial w_{j}} J(w_{0},w_{1},w_{2}) \\
= w_{j} - \alpha \frac{1}{m} \sum^{m}_{i=1} (h_{W}(x^{(i)}) - y^{i}) x^{i}_{j} \\
= w_{j} - \alpha \frac{1}{m} \sum^{m}_{i=1} e^{i} x^{i}_{j} \\
= w_{j} - \alpha \frac{1}{m} ( e^{1} x^{1}_{j} + e^{2} x^{2}_{j} + ... + e^{m} x^{m}_{j} ) \\
= w_{j} - \alpha \frac{1}{m} ( x^{1}_{j}, x^{2}_{j}, ... , x^{m}_{j} )^{T} \cdot E
$$



So:


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
\alpha \frac{1}{m}
\begin{bmatrix}
(x^{1}_{0} & x^{2}_{0} & ... & x^{m}_{0})^{T}  \\
(x^{1}_{1} & x^{2}_{1} & ... & x^{m}_{1})^T  \\
... & ... & ... & ...  \\
(x^{1}_{n} & x^{2}_{n} & ... & x^{m}_{n})^T  \\
\end{bmatrix}
\cdot
E
$$


Finally:


$$
W := W - \alpha \frac{1}{m} X^{T} \cdot E
$$










