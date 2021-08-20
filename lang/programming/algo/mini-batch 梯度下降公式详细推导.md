

## mini-batch



对于给定输入：

​	[ [0, 0], [0,1], [1,0], [1,1]]

 XOR 的结果是：

​	[ [1,0], [0,1], [0,1], [1,0] ]

> [ [1, 0] ... ] 里的1 表示对于输入 [0, 0]，分类为0 的概率为100%；0 表示分类为1 的概率为0%
>
> [...,[0,1],... ]  里的0 表示对于输入[0,1]，分类为0 的概率为0%；1表示分类为1 的概率为100%



对于分类问题，神经网络的输出结果是一组概率分布。监督学习的标签是真实概率分布 $p$，训练给出的预测结果是近似概率分布 $q$ 。 训练的过程就是是让 $q$ 不断地逼近 $p$。衡量两个分布的接近程度是用KL散度，又由于最小化KL 散度等价于最小化交叉熵，所以用交叉熵作为损失函数。





样本是随机变量$X$（一个骰子）的取值$x$，概率分布 $p$ 给出了随机变量所有取值的概率




## Softmax 函数



https://charlee.li/how-to-compute-the-derivative-of-softmax-and-cross-entropy/

https://deepnotes.io/softmax-crossentropy

- 数值技巧

https://aimatters.wordpress.com/2019/06/17/the-softmax-function-derivative/



softmax 把向量$z$  变成概率
$$
\sigma(z) = (\sigma_1(z), \cdots,\sigma_k(z))
$$

$$
\sigma_i(z) = \frac{e^{z_{i}}}{\sum^k_{j=1} e^{z_{j}}}, \ i \in 1 \cdots k
$$


- 总共有 $k$ 类，样本被分为第 $i$ 类的概率是 $\sigma_i(z)$

  求 $z$ 的任意一个分量对概率 $\sigma_i(z)$ 的偏导


$$
\frac{\partial}{\partial z_{s}} \sigma_i(z) = \frac{\partial}{\partial z_{s}} \bigg ( \frac{e^{z_{i}}}{\sum^k_{j=1} e^{z_{j}}} \bigg ) \ for \ 

\ i \in 1 \cdots k, \ s \in 1 \cdots k \\

=   \frac{ \frac{\partial}{\partial z_{s}} e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - \frac{\partial}{\partial z_{s}} (\sum^k_{j=1} e^{z_{j}}) * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\
$$

$$
if \  s = i,  \\

=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - \frac{\partial}{\partial z_{s}} ( e^{z_{i}}) * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\

=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}}) - e^{z_{i}} * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\


=   \frac{ e^{z_{i}} * (\sum^k_{j=1} e^{z_{j}} - e^{z_{i}} )  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\


=   \frac{ e^{z_{i}}   }{\sum^k_{j=1} e^{z_{j}}} * \frac{  \sum^k_{j=1} e^{z_{j}} - e^{z_{i}} }{\sum^k_{j=1} e^{z_{j}}}  \\ 

= \sigma_i(z) * (1 - \sigma_i(z))
$$


$$
if \  s \neq i,  \\

=   \frac{ 0 -  e^{z_{s}} * e^{z_{i}}  }{(\sum^k_{j=1} e^{z_{j}})^2}  \\

=   - \ \frac{ e^{z_{s}} }{\sum^k_{j=1} e^{z_{j}}} * \frac{  e^{z_{i}} }{\sum^k_{j=1} e^{z_{j}}}  \\

= - \sigma_s(z) \sigma_i(z)  \\
$$





$$
h(x) = f(x) g(x) \\
h'(x) = f'(x)g(x) + f(x)g'(x)
$$

$$
h(x) = \frac{f(x)}{g(x)}  \\
令：\frac{1}{g(x)} = z(x)，则：
h(x) = f(x) z(x) \\
h'(x) = f'(x)z(x) + f(x)z'(x) \\
= f'(x)\frac{1}{g(x)} + f(x) ( - \frac{ \frac{d}{d x}g(x) }{g(x)^{2}} ) \\

= \frac{f'(x)g(x)}{g(x)^2} - \frac{g'(x)f(x)}{g(x)^2} \\

=  \frac{f'(x)g(x) - g'(x)f(x)}{g(x)^2} 
$$


$$
E = y_1 + y_2 \\
y_1 = s_1 s_2, \ y_2 = s_1^2
$$

$$
\frac{\partial}{\partial s_{1}} E = \frac{\partial}{\partial s_{1}} y_1 + \frac{\partial} {\partial s_{1}} y_2 \\
= s_2 + 2s_1
$$

$$
\frac{\partial E}{\partial s_{1}} = \frac{\partial E}{\partial y_{1}} \frac{\partial y_1}{\partial s_{1}} +\frac{\partial E}{\partial y_{2}} \frac{\partial y_2}{\partial s_{1}}
$$

- 两种方法都对

  > 多元复合函数求导法则，后一种方法更通用。其中：
  >
  > $\frac{\partial E}{\partial y_{1}}$ = 1


$$
(f \circ g)'(x) = f'\big( g(x) \big ) g'(x)
$$





$$
y_i = \frac{e^{s_i}}{\sum^{nclass}_{c} e^{s_c}}
$$

$$
E = - \sum^{nclass}_k t_k \ log (y_k)
$$


$$
E = X_1 + \cdots + X_n \\

X_k = - t_k log(y_k) \\ 

\frac{\partial{E}}{\partial{s_i}} = \frac{\partial{E}}{\partial{X_1}} \frac{\partial{X_1}}{\partial{y_1}} \frac{\partial{y_1}}{\partial{s_i}} + \cdots +

\frac{\partial{E}}{\partial{X_n}} \frac{\partial{X_n}}{\partial{y_n}} \frac{\partial{y_n}}{\partial{s_i}} \\

= \frac{\partial{E}}{\partial{y_1}}  \frac{\partial{y_1}}{\partial{s_i}} + \dots +

\frac{\partial{E}}{\partial{y_n}} \frac{\partial{y_n}}{\partial{s_i}} \\

= \sum_k^{nclass} \frac{\partial{E}}{\partial{y_k}}  \frac{\partial{y_k}}{\partial{s_i}} \\


= \frac{\partial{E}}{\partial{y_i}}  \frac{\partial{y_i}}{\partial{s_i}} + \sum_{k \neq i}^{nclass} \frac{\partial{E}}{\partial{y_k}}  \frac{\partial{y_k}}{\partial{s_i}}  \\
$$




$$
\frac{\partial{E}}{\partial{X_1}} \frac{\partial{X_1}}{\partial{y_1}} \frac{\partial{y_1}}{\partial{s_i}} = \frac{\partial{E}}{\partial{y_1}}  \frac{\partial{y_1}}{\partial{s_i}}
$$






$$
y_i = \frac{e^{s_i}}{\sum^{nclass}_{c} e^{s_c}}
$$

$$
E = - \sum^{nclass}_k t_k \ log (y_k)
$$

$$
E = - t_1 log(y_1) - t_2 log(y_2) \cdots - t_n log(y_n) \\

\frac{\partial{E}}{\partial{s_i}} = \frac{\partial}{\partial s_i} (- t_1 log(y_1)) + \frac{\partial}{\partial s_i} (- t_2 log(y_2)) \cdots + \frac{\partial}{\partial s_i} (- t_n log(y_n)) \\

= -t_1 \frac{\partial}{\partial s_i} log(y_1)  \cdots  -t_n \frac{\partial}{\partial s_i} log(y_n) \\

= -t_1 \frac{1}{y_1} \frac{\partial}{\partial s_i} y_1 \cdots -t_n \frac{1}{y_n} \frac{\partial}{\partial s_i} y_n \\

= -t_i \frac{1}{y_i} \frac{\partial}{\partial s_i} y_i - \sum_{k \neq i} t_k \frac{1}{y_k} \frac{\partial}{\partial s_i} y_k \\

= -t_i \frac{1}{y_i} y_i (1 - y_i) - \sum_{k \neq i} t_k \frac{1}{y_k} ( - y_i y_k  ) \\

= -t_i (1 - y_i) + \sum_{k \neq i} t_k y_i \\

= -t_i + t_i y_i + \sum_{k \neq i} t_k y_i \\

= -t_i + \sum_{k } t_k y_i  \\

= -t_i + y_i  \sum_{k } t_k \\

= y_i - t_i
$$









### 自信息量


$$
I(x) = log_2(\frac{1}{p(x)}) = - log_{2}(p(x))
$$

> 事件$x$ 出现的概率是$p(x)$，则它的信息量是$I(x)$ ，$2$ 为底单位是比特, $e$ 为底单位是奈特。



## 信息熵


$$
H(\mathbf{x}) = \mathbb{E}_{x \sim \small{P}} \big[I(x) \big] \\
= \sum^{N}_{i=1} P(x) I(x)
$$

> 信息熵是随机变量（信息源）的所有事件信息量的均值(数学期望)



- 一个事件$x$ 的自信息量的度量是$I(x)$
- 一个随机变量（信息源）的自信息量的度量（熵）是其所有事件自信息量的数学期望（均值）
  - 熵代表随机变量的平均信息量
  - 随机变量$X \sim p(X)$的熵$H(p)$即是编码随机变量$X$ 的最优平均编码长度





## 交叉熵



监督学习的标签是真实概率分布 $p$，训练给出的预测结果是近似概率分布 $q$ 。

> 本来分布 $q$ 自已就可以计算一个信息熵， 交叉的意思就是在计算$q$ 的平均信息量时，用实概率分布 $p$ 得到的概率来进行概率平均（注意它和算术平均的区别）



$q$ 的信息熵是：
$$
- \sum^{N}_{i=1} q(x)  log \ q(x)
$$
$q$ 的交叉熵是：
$$
- \sum^{N}_{i=1} p(x)  log \ q(x)
$$

- 注意其中一个$q$ 是如何被替换成$p$ 的



> 不要盲目地使用交叉熵！你要注意的是你的数据分布，如果它不符合正态分布假设，那么你很可能就需要重新设计Loss Function了



## KL 散度



KL 散度是真实概率分布 $p$ 信息熵与近似概率分布 $q$ 交叉熵之差。因为 $p$ 信息熵是常量，所以**最小化KL 散度等价于最小化 $q$ 交叉熵**。


$$
D(P \ || \ Q) = E(P,Q) - E(P) = \sum P(i) \ log \frac{P(i)}{Q(i)}
$$


假设$P$ 为真实分布(狗=0，猫=1), $Q$ 为模型预测的分布（狗=0.4，猫=0.6）

- 注意到 $E(P)$ 恒为零（因为百分百确定的事件没有信息量，平均信息量熵自然也是零） 
- 所以有：KL 散度 = 交叉熵





## 交叉熵-Softmax求导 

（Cross Entropy Loss with Softmax）


$$
L = - \sum^{k}_{i=1} p(x_i)  log \ q(x_i)
$$

> $x_i$ 代表输入被分类为第$i$ 类的事件，$p(x_i)$ 是这个事件发生的真实概率，$q(x_i)$ 是预测得到的近似概率
>
> $log$ 不标明底数的时侯，默认以 $e$ 为底



把前面的$\sigma_i(z)$ 代入交叉熵损失函数：
$$
L = - \sum^{k}_{i=1} p(x_i)  log \ \sigma_i(z)
$$


$$
\frac{\partial}{\partial z_{s}} L = - \sum^{k}_{i=1} p(x_i) \frac{\partial}{\partial z_{s}} \big( log \ \sigma_i(z) \big ) \\ 

= - \sum^{k}_{i=1} p(x_i) \frac{1}{\sigma_i(z)} 

\frac{\partial}{\partial z_{s}} \sigma_i(z) \\
$$

$$
\ if \ s = i \\

= - \sum^{k}_{i=1} p(x_i) \frac{1}{\sigma_i(z)}  \sigma_i(z) * (1 - \sigma_i(z)) \\ 

= - \sum^{k}_{i=1} p(x_i)  (1 - \sigma_i(z)) \\
$$




$$
\frac{\partial}{\partial z_{s}} \big( log \ \sigma_i(z) \big ) 

= \frac{1}{\sigma_i(z)} 

\frac{\partial}{\partial z_{s}} \sigma_i(z)
$$








$p(x_i)$代表真实标签，在真实标签中，除了对应类别其它类别的概率都为0，实际上，交叉熵可以简写为：


$$
L = -log \ \sigma_i(z)
$$

> 求和符号被去掉了，因为真实标签中只有一项为1，其他都为0
>
> $p(x_i)$ 也不见了，因为它的值是1


$$
L' = -log' \big( \sigma_i(z) \big) \ \sigma_i(z)'  \\
= - \frac{1}{\sigma_i(z)} \sigma_i(z)'
$$





$$
\begin{eqnarray*} y = \ln(x) &\Longleftrightarrow & x =
      e^y \cr y = \log_a(x) & \Longleftrightarrow & x = a^y
      \end{eqnarray*}
$$

$$
\frac{d}{dx}
            \ln(x) = \frac{1}{x}, \qquad \frac{d}{dx}\log_a(x) =
            \frac{1}{x \ln(a)}
$$





## 激活函数-ReLU



```
# https://zhuanlan.zhihu.com/p/92412922

激活函数为什么是非线性的？如果使用线性激活函数，那么输入跟输出之间的关系为线性的，无论神经网络有多少层都是线性组合。输出层可能会使用线性激活函数，但在隐含层都使用非线性激活函数。

常用的激活函数：sigmoid，Tanh，ReLU，Leaky ReLU，PReLU，ELU，Maxout


```



```
# https://oldpan.me/archives/non-linear-activation-relu-or-lrelu
RELU的优点即计算特别简单，高度非线性，但是RELU的缺点也很明显：

因为其将所有的输入负数变为0，在训练中可能很脆弱，很容易导致神经元失活，使其不会在任何数据点上再次激活。简单地说，ReLu可能导致神经元死亡。
对于ReLu中(x<0)的激活，此时梯度为0，因此在下降过程中权重不会被调整。这意味着进入这种状态的神经元将停止对错误/输入的变化做出反应(仅仅因为梯度为0，没有任何变化)。这就是所谓的dying ReLu problem.
平时使用的时候RELU的缺点并不是特别明显，只有在学习率设置不恰当(较大)的时候，会加快神经网络中神经元的“死亡”。

而LeakyRelu是RELU的变体，对输入小于0部分的反应有所变化，减轻了RELU的稀疏性，因为我们可以设置negative_slop这个系数保证在输入小于0的时候有微弱的输出。

LeakyReLU的优点是什么，就是缓解一些RELU导致神经元死亡的问题，但是缺点也很明显，因为有了负数的输出，导致其非线性程度没有RELU强大，在一些分类任务中效果还没有Sigmoid好，更不要提RELU。

自己在尝试生成类的时候，使用自编码器生成图像，上述这两个激活函数的时候并没有发现明显的差别。可能LRELU稍好一些，总结一下就是RELU适合分类，LRELU适合生成类的任务。

```



```

# https://zhuanlan.zhihu.com/p/73214810

ReLU的有效导数是常数1，解决了深层网络中出现的梯度消失问题，也就使得深层网络可训练。同时ReLU又是非线性函数，所谓非线性，就是一阶导数不为常数；对ReLU求导，在输入值分别为正和为负的情况下，导数是不同的，即ReLU的导数不是常数，所以ReLU是非线性的（只是不同于Sigmoid和tanh，relu的非线性不是光滑的）。

ReLU在x>0下，导数为常数1的特点：

导数为常数1的好处就是在“链式反应”中不会出现梯度消失，但梯度下降的强度就完全取决于权值的乘积，这样就可能会出现梯度爆炸问题。解决这类问题：一是控制权值，让它们在（0，1）范围内；二是做梯度裁剪，控制梯度下降强度，如ReLU(x)=min(6, max(0,x))

ReLU在x<0下，输出置为0的特点：

描述该特征前，需要明确深度学习的目标：深度学习是根据大批量样本数据，从错综复杂的数据关系中，找到关键信息（关键特征）。换句话说，就是把密集矩阵转化为稀疏矩阵，保留数据的关键信息，去除噪音，这样的模型就有了鲁棒性。ReLU将x<0的输出置为0，就是一个去噪音，稀疏矩阵的过程。而且在训练过程中，这种稀疏性是动态调节的，网络会自动调整稀疏比例，保证矩阵有最优的有效特征。

但是ReLU 强制将x<0部分的输出置为0（置为0就是屏蔽该特征），可能会导致模型无法学习到有效特征，所以如果学习率设置的太大，就可能会导致网络的大部分神经元处于‘dead’状态，所以使用ReLU的网络，学习率不能设置太大。

ReLU作为激活函数的特点：

相比Sigmoid和tanh，ReLU摒弃了复杂的计算，提高了运算速度。
解决了梯度消失问题，收敛速度快于Sigmoid和tanh函数，但要防范ReLU的梯度爆炸
容易得到更好的模型，但也要防止训练中出现模型‘Dead’情况。
```



```
梯度剪切。另外一种解决梯度爆炸的手段是采用权重正则化（weithts regularization）。
```




$$
\mathrm{ReLU}(x) = \mathrm{max}(0, x)
$$

> relu函数仅仅在0点处不可导，因为左导数不等于右导数。一般这个间断点处的导数认为是0







## mini-batch 交叉熵



就是多个交叉熵损失的算术平均

mini batch的平均loss



## 矩阵求导



```
# https://zhuanlan.zhihu.com/p/24709748
# https://wzbtech.com/tech/matrix-derivatives1.html
# https://zhuanlan.zhihu.com/p/83859554
# https://zhuanlan.zhihu.com/p/50319086
	全微分 是梯度向量 (nx1)与微分向量  (nx1)的内积）

# https://www.cnblogs.com/hechangchun/p/11087943.html
	hadamard product（哈达玛积）、kronecker product（克罗内克积）
```







## 交叉熵 pytorch 计算

```python
import torch
import torch.nn as nn

input = torch.tensor([[ 0.8082,  1.3686, -0.6107],
        [ 1.2787,  0.1579,  0.6178],
        [-0.6033, -1.1306,  0.0672],
        [-0.7814,  0.1185, -0.2945]])
target = torch.tensor([1,0,2,1])

loss = nn.CrossEntropyLoss()
output = loss(input, target)
output.backward()
```


> **当使用交叉熵作为损失函数的时候，标签不能为onehot形式，只能是一维的向量**，例如，当batch size是5时，这一个batch的标签只能时[0,1,4,2,6]这样的形式。








**概率**是已知参数求**结果的可能性**

**似然**是已知结果求**参数的可能性**

- Likelihood
- 最大似然是求最大可能性的参数（**最大似然**估计(MLE)）



**最大似然原理**



给定一个概率分布$D$，已知其概率密度函数（连续分布）或概率质量函数（离散分布）为$f_D$，以及一个分布参数 $\theta$ ，我们可以从这个分布中抽出一个具有 $n$ 个值的采样$X_{1},X_{2},\ldots ,X_{n}$，利用$f_{D}$ 计算出其似然函数：

$$
L(\theta \ | \ x_1, \cdots, x_n) = f_{\theta}(x_1, \cdots, x_n) 
$$


若$D$ 是离散分布，$f_\theta$ 即是在参数为 $\theta$ 时观测到这一采样的概率。





```
用随机选择的小批量数据（mini-batch）作为全体训练数据的近似值，损失函数要计算这一批数据的总体损失

Xor 问题的每一个输入维度是 (2,) , batch 大小设为3，既每次训练三组输入数据，作为全体训练数据的近似

使用双隐层网络结构，矩阵的维度变化：
	(3,2).(2,5) = (3,5)
	(3,5).(5,5) = (3,5)
	(3,5).(5,2) = (3,2)
```



$m=3, n=2, c=5, nclass=2$
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
a^1_{*,j} = X^0 \cdot w^1_{*,j} + b^1_{*,j}
$$


$$
L = g(x^0 w^1 + b^1)
$$


> Matrix Differentiation  






$$
g \bigg (
\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,c}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,c} \\
\end{bmatrix}
\bigg )

= 

\begin{bmatrix}
x^{1}_{1,1} & x^{1}_{1,2} & \cdots & x^{1}_{1,c}  \\
x^{1}_{2,1} & x^{1}_{2,2} & \cdots & x^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{1}_{m,1} & x^{1}_{m,2} & \cdots & x^{1}_{m,c} \\
\end{bmatrix}
$$



$$
\begin{bmatrix}
x^{1}_{1,1} & x^{1}_{1,2} & \cdots & x^{1}_{1,c}  \\
x^{1}_{2,1} & x^{1}_{2,2} & \cdots & x^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{1}_{m,1} & x^{1}_{m,2} & \cdots & x^{1}_{m,c} \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
w^{2}_{1,1} & w^{2}_{1,2} & \cdots & w^{2}_{1,c}  \\
w^{2}_{2,1} & w^{2}_{2,2} & \cdots & w^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{2}_{c,1} & w^{2}_{c,2} & \cdots & w^{2}_{c,c} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{2}_{1,1} & b^{2}_{1,2} & \cdots & b^{2}_{1,c}  \\
b^{2}_{2,1} & b^{2}_{2,2} & \cdots & b^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
b^{2}_{m,1} & b^{2}_{m,2} & \cdots & b^{2}_{m,c} \\
\end{bmatrix}

\\ = 

\begin{bmatrix}
a^{2}_{1,1} & a^{2}_{1,2} & \cdots & a^{2}_{1,c}  \\
a^{2}_{2,1} & a^{2}_{2,2} & \cdots & a^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{2}_{m,1} & a^{2}_{m,2} & \cdots & a^{2}_{m,c} \\
\end{bmatrix}
$$

$$
g \bigg (
\begin{bmatrix}
a^{2}_{1,1} & a^{2}_{1,2} & \cdots & a^{2}_{1,c}  \\
a^{2}_{2,1} & a^{2}_{2,2} & \cdots & a^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{2}_{m,1} & a^{2}_{m,2} & \cdots & a^{2}_{m,c} \\
\end{bmatrix}
\bigg )

= 

\begin{bmatrix}
x^{2}_{1,1} & x^{2}_{1,2} & \cdots & x^{2}_{1,c}  \\
x^{2}_{2,1} & x^{2}_{2,2} & \cdots & x^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{2}_{m,1} & x^{2}_{m,2} & \cdots & x^{2}_{m,c} \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
x^{2}_{1,1} & x^{2}_{1,2} & \cdots & x^{2}_{1,c}  \\
x^{2}_{2,1} & x^{2}_{2,2} & \cdots & x^{2}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{2}_{m,1} & x^{2}_{m,2} & \cdots & x^{2}_{m,c} \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
w^{3}_{1,1} & w^{3}_{1,2} & \cdots & w^{3}_{1,nclass}  \\
w^{3}_{2,1} & w^{3}_{2,2} & \cdots & w^{3}_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{3}_{c,1} & w^{3}_{c,2} & \cdots & w^{3}_{c,nclass} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{3}_{1,1} & b^{3}_{1,2} & \cdots & b^{3}_{1,nclass}  \\
b^{3}_{2,1} & b^{3}_{2,2} & \cdots & b^{3}_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
b^{3}_{m,1} & b^{3}_{m,2} & \cdots & b^{3}_{m,nclass} \\
\end{bmatrix}

\\ = 

\begin{bmatrix}
a^{3}_{1,1} & a^{3}_{1,2} & \cdots & a^{3}_{1,nclass}  \\
a^{3}_{2,1} & a^{3}_{2,2} & \cdots & a^{3}_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{3}_{m,1} & a^{3}_{m,2} & \cdots & a^{3}_{m,ncalss} \\
\end{bmatrix}
$$

$$
Softmax \bigg (

\begin{bmatrix}
a^{3}_{1,1} & a^{3}_{1,2} & \cdots & a^{3}_{1,nclass}  \\
a^{3}_{2,1} & a^{3}_{2,2} & \cdots & a^{3}_{2,nclass} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{3}_{m,1} & a^{3}_{m,2} & \cdots & a^{3}_{m,ncalss} \\
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

> CE 代表求交叉熵


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

> L 代表求损失




$$
\frac{\partial}{\partial w^1_{i,j}} L,   \  for \ i \in 1 \cdots n; \ j \in 1 \cdots c
$$










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
a^2_{s,1} = x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}
$$

$$
x^{1}_{s,*} \cdot w^2_{*,1} = x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1}
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



### 第二层偏导



#### 权重偏导


$$
\\

\ for \ s \in 1 \cdots m; \ (x^{1}_{s,*} 代表行向量) \\
a^2_{s,1} = x^{1}_{s,*} \cdot w^2_{*,1}
$$

$$
\ for \ j \in 1 \cdots m; \  s \in 1 \cdots m; \\

\frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) = \frac{\partial}{\partial w^2_{j,1}} g( x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}) \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} a^2_{s,1}  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1})  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial w^2_{j,1}} ( x^1_{s,j} w^2_{j,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j} \  \frac{\partial}{\partial w^2_{j,1}} (  w^2_{j,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j}
$$

#### 偏置偏导


$$
\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^2_{j,1}} g( x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1}) \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial b^2_{j,1}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\


= g(a^2_{s,1})(1 - g(a^2_{s,1})) \frac{\partial}{\partial b^2_{j,1}} (b^2_{s,1})  \\
$$

$$
\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) =  0, if \ j \neq s  \\

\frac{\partial}{\partial b^2_{j,1}} g( a^2_{s,1} ) = g(a^2_{s,1})(1 - g(a^2_{s,1})) , if \ j = s  \\ 
$$










$$
\frac{\partial}{\partial w^2_{j,1}} \mathcal{L} = \frac{\partial}{\partial w^2_{j,1}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ j \in 1 \cdots m  \\
\\

= \frac{1}{2m} \sum^{m}_{s=1}\frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})^2   \quad \text{(by linearity of the derivative)} \\


= \frac{1}{2m} \sum^{m}_{s=1} 

2 \cdot (g( a^2_{s,1} ) - y_{s,1}) \frac{\partial}{\partial w^2_{j,1}} (g( a^2_{s,1} ) - y_{s,1})   \quad \text{(by chain rule)} \\


= \frac{1}{2m} \cdot 2 \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - \frac{\partial}{\partial w^2_{j,1}} y_{s,1} \bigg ]  \quad \text{(by linearity of the derivative)}  \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \bigg [ \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} ) - 0 \bigg ]   \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial w^2_{j,1}} g( a^2_{s,1} )  \\


= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) \ g(a^2_{s,1})(1 - g(a^2_{s,1})) \  x^1_{s,j} \\
$$





### 第一层偏导



#### 权重偏导


$$
\frac{\partial}{\partial w^1_{i,j}} g( a^2_{s,1} ) = g(a^2_{s,1})(1 - g(a^2_{s,1})) \ \frac{\partial}{\partial w^1_{i,j}} (  a^2_{s,1} )  \\

= g(a^2_{s,1})(1 - g(a^2_{s,1})) w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i} \\
$$

$$
\frac{\partial}{\partial w^1_{i,j}} (  a^2_{s,1} ) = \frac{\partial}{\partial w^1_{i,j}} (x^{1}_{s,*} \cdot w^2_{*,1} + b^2_{s,1})  \\

= \frac{\partial}{\partial w^1_{i,j}} (x^{1}_{s,*} \cdot w^2_{*,1})  \\

= \frac{\partial}{\partial w^1_{i,j}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\


= \frac{\partial}{\partial w^1_{i,j}} ( x^1_{s,j} w^2_{j,1} )  \\

= \frac{\partial}{\partial w^1_{i,j}} ( g(a^{1}_{s,j}) w^2_{j,1} )  \\

= w^2_{j,1} \frac{\partial}{\partial w^1_{i,j}} ( g(a^{1}_{s,j})  )  \\

=  w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) \frac{\partial}{\partial w^1_{i,j}} a^{1}_{s,j} \\

= w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i} \\
$$

$$
\frac{\partial}{\partial w^1_{i,j}} a^{1}_{s,j} = \frac{\partial}{\partial w^1_{i,j}}(x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j}) \\

= \frac{\partial}{\partial w^1_{i,j}}(x^{0}_{s,i} w^{1}_{i,j} ) \\

= x^{0}_{s,i} \frac{\partial}{\partial w^1_{i,j}}( w^{1}_{i,j} ) \\

= x^{0}_{s,i}
$$






$$
x^{1}_{s,*} \cdot w^2_{*,1} = x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1}
$$

$$
x^{1}_{s,j} = g(a^{1}_{s,j}) \\
= g(x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j})
$$

$$
a^{1}_{s,j} = x^{0}_{s,*} \cdot w^{1}_{*,j} \\
=
x^{0}_{s,1} w^{1}_{1,j} + x^{0}_{s,2} w^{1}_{2,j} + \cdots + x^{0}_{s,n} w^{1}_{n,j}  \\
$$





$$
\frac{\partial}{\partial w^1_{i,j}} \mathcal{L} = \frac{\partial}{\partial w^1_{i,j}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ i \in 1 \cdots n; \ j \in 1 \cdots m  \\
\\


= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial w^1_{i,j}} g( a^2_{s,1} )  \\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1}) g(a^2_{s,1})(1 - g(a^2_{s,1})) w^1_{i,j} g(a^{1}_{s,j}) (1 -  g(a^{1}_{s,j})) x^{0}_{s,i}  \\
$$




#### 偏置偏导


$$
\frac{\partial}{\partial b^1_{k,j}} \mathcal{L} = \frac{\partial}{\partial b^1_{k,j}} 
\bigg [
\frac{1}{2m} \sum^{m}_{s=1}(h^{2}_{s,1} - y_{s,1})^2 
\bigg ]
, \ for \ k \in 1 \cdots m; \ j \in 1 \cdots m  \\
\\

= \frac{1}{m} \sum^{m}_{s=1} 

(g( a^2_{s,1} ) - y_{s,1})  \frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} )  \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,1} w^2_{1,1} + x^1_{s,2} w^2_{2,1} + \cdots + x^1_{s,m} w^2_{m,1} )  \\

= \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,j} w^2_{j,1} )  \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = \frac{\partial}{\partial b^1_{k,j}} ( x^1_{s,j} w^2_{j,1} ),  if \ k = s \\
= \frac{\partial}{\partial b^1_{k,j}} ( g(a^1_{s,j}) w^2_{j,1} ) \\

= \frac{\partial}{\partial b^1_{k,j}} ( g(a^1_{s,j}) w^2_{j,1} ) \\

= w^2_{j,1} \frac{\partial}{\partial b^1_{k,j}} g(a^1_{s,j})  \\


= w^2_{j,1} g(a^1_{s,j}) (1-g(a^1_{s,j}) ) \frac{\partial}{\partial b^1_{k,j}} (a^1_{s,j})  \\

= w^2_{j,1} g(a^1_{s,j}) (1-g(a^1_{s,j}) )
$$

$$
\frac{\partial}{\partial b^1_{s,j}} (a^1_{s,j}) = \frac{\partial}{\partial b^1_{s,j}} (  x^{0}_{s,*} \cdot  w^{1}_{*,j} + b^1_{s,j}) \\
= 1 \\
$$

$$
\frac{\partial}{\partial b^1_{k,j}} g( a^2_{s,1} ) = 0,  if \ k \neq s \\
$$

































