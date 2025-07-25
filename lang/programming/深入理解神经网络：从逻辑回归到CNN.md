

[TOC]



# 深入理解神经网络：从逻辑回归到CNN



What I cannot create I do not understand

Things Happen for A Reason



### install cuda 11.8

```
install cuda 11.8

update-alternatives --remove cuda /usr/local/cuda-12.2
update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-11.8 118
ln -sfT /usr/local/cuda-11.8 /etc/alternatives/cuda
ln -sfT /etc/alternatives/cuda /usr/local/cuda


vi ~/.bashrc 

if [ -z $LD_LIBRARY_PATH ]; then
  LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64
else
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.8/lib64
fi
export LD_LIBRARY_PATH

export PATH=/usr/local/cuda/bin:$PATH


source ~/.bashrc 

nvcc --version
```





### 极好的

https://xiaosheng.run/2022/03/24/transformers-note-7.html

> Hugging Face 的 Transformers 库快速入门（七）：翻译任务

[MicroTokenizer](https://github.com/howl-anderson/MicroTokenizer) 面向教育的中文分词



### 多维矩阵乘法

- https://pytorch.org/docs/stable/notes/broadcasting.html

```

前面的维度要满足broadcast才行，就是要么有一个维度为1，要么维度相等
最后的两个维度要满足矩阵乘法


结果：前面的维度保留最大的，后面的维度由矩阵乘法给出


a和b除了最后两个维度可以不一致，其他维度要相同(比如上面代码第一维和第二维分别都是1,2)
a和b最后两维的维度要符合矩阵乘法的要求（比如a的(3,4)能和b的(4,6)进行矩阵乘法）

(1,2) . (1,2,2,2) => (1,1,2,2)

```



- https://itewqq.cn/%E6%95%B0%E5%AD%A6-%E5%90%91%E9%87%8F%E5%87%BD%E6%95%B0%E7%9A%84%E9%9B%85%E5%8F%AF%E6%AF%94%E7%9F%A9%E9%98%B5%E4%B8%8E%E9%93%BE%E5%BC%8F%E6%B3%95%E5%88%99/



多元函数$f:\mathbb{R}^{n}\rightarrow \mathbb{R}^{1}$，我们可以把他的输入当作一个向量 $\bf{x}\in \mathbb{R}^{n}$，输出 $y=f(\bf{x})\in \mathbb{R}^{1}$ 是一个数字。那么 $f$ 的梯度定义为：
$$
\nabla f_{\boldsymbol{x}} \overset{\underset{\mathrm{def}}{}}{=} \left[ \frac{\partial f }{\partial x_1}, \frac{\partial f }{\partial x_2},\cdots,\frac{\partial f }{\partial x_n} \right]=\frac{\partial f }{\partial \boldsymbol{x}}
$$
全微分的向量化表示为：
$$
\begin{aligned} 
df &= \frac{\partial f}{\partial x_1}dx_1+\frac{\partial f}{\partial x_2}dx_2+\cdots+\frac{\partial f}{\partial x_n}dx_n \\ 
   &=\left[ \frac{\partial f }{\partial x_1}, \frac{\partial f }{\partial x_2},\cdots,\frac{\partial f }{\partial x_n} \right] \left[dx_1, dx_2,\cdots,dx_n \right]^T \\ 
   &=\frac{\partial f }{\partial \boldsymbol{x}} d\boldsymbol{x} 
\end{aligned}
$$


映射 $f:\mathbb{R}^{n}\rightarrow \mathbb{R}^{m}$ 的输入是向量 $\bf{x}\in \mathbb{R}^{n}$，输出是向量 $\bf{y}=f(\bf{x})\in \mathbb{R}^{m}$

如果我们将输出向量 $y$ 的每个分量 $y_i$ 看作一个独立的多元函数，那么我们可以写出每个 $y_i$ 对每个 $x_i$  的偏导数（也就是梯度）
$$
\left[ \frac{\partial y_i }{\partial x_1}, \frac{\partial y_i }{\partial x_2},\cdots,\frac{\partial y_i }{\partial x_n} \right]
$$
将每个 $y_i$ 的梯度组合起来就得到了雅可比矩阵
$$
\begin{aligned}J=\left(\begin{array}{ccc} 
   \frac{\partial y_{1}}{\partial x_{1}} & \cdots & \frac{\partial y_{1}}{\partial x_{n}}\\ 
   \vdots & \ddots & \vdots\\ 
   \frac{\partial y_{m}}{\partial x_{1}} & \cdots & \frac{\partial y_{m}}{\partial x_{n}} 
   \end{array}\right)\end{aligned}
$$
也常写作
$$
J=\frac{\partial(y_1,…,y_m)}{\partial(x_1,…,x_n)}
$$



雅可比矩阵表示了函数 $f$ 在每一处可导点的导数。具体地说，设 $\Delta \bf{x}$ 为一在 $x$ 处的位移向量(假设为列向量)，则 $J(\bf{x}) \cdot \Delta \bf{x}$ 就是函数值的位移向量（类似一元数值函数里 $\Delta y=y'(x)*\Delta x$, 该函数值的位移向量即为 $x$ 处的 $f(x)$ 增量的最佳线性逼近(更熟悉点的词叫全微分)。类似于导数，雅可比矩阵是函数局部的线性化，使用矩阵形式来表示微分(线性逼近)这个线性变换。



提一点雅可比行列式有关的：当上述 $m=n$ 时，$f$ 是一个从 $R^n$ 到 $R^n$  的映射，因此雅可比矩阵是一个方阵，我们可以求出来这个方阵的行列式，常称雅可比行列式。对高等数学(下)有印象的人应该可以记得起这个名字，雅可比行列式常用在多元微积分中，尤其是在在换元积分时，需要用它作为乘子。为什么要作为乘子出现？感性的理解，这还是因为在积分中空间转换带来的面积/体积变化，而众所周知行列式就是体积/面积，雅可比矩阵作为导数就表现了局部的线性变化比例。



设 $f$ 和 $g$ 为两个关于 $x$ 可导函数，则复合函数 $(f∘g)(x)$ 的导数 $(f∘g)′(x)$ 为：$(f∘g)′(x)=f′(g(x))g′(x)$ .

考虑可微函数 $f:R^m→R^k$ 和 $g:R^n→R^m$，以及 $R^n$ 上一点  $x$ 。令 $D_xg$ 表示 $g$ 在 $x$ 处的全微分，$D_g(x)f$ 表示 $f$ 在 $g(x)$ 处的全微分，则复合函数 $(f∘g)(x)$ 的全微分可表示为：


$$
D_{\bf{x}}(f\circ g)(\bf{x})=D_{g(\bf{x})}f\circ D_{\bf{x}}g
$$
相应的，用雅可比矩阵表示的形式为：
$$
J_{f \circ g}=(J_f \circ g)J_{g}
$$


或者用变量名表示的话写成
$$
\frac{\partial(y_1,…,y_k)}{\partial(x_1,…,x_n)}=\frac{\partial(y_1,…,y_k)}{\partial(u_1,…,u_m)}\frac{\partial(u_1,…,u_m)}{\partial(x_1,…,x_n)}
$$


上式中右边意为两个矩阵相乘。

我们来从直观上理解一下这个等式。首先，我们知道雅可比矩阵的“成因”是用**矩阵**来表示一阶微分的，也就是把一阶微分的算子当成一个**线性变换**，而复合函数等于是一个嵌套，也就是函数的函数，对应到线性变换里，也就是**线性变换的线性变换**，而我们又知道用矩阵表示线性变换时这种“**线性变换的线性变换**”，就是相当于两个矩阵的**乘积**。到这里。我们把微积分和线性代数两种工具结合到了一起，就得到了这个结果。



设有函数 $g:R→R^3$ 为
$$
g(t)=(t\ t2 \ t3)
$$





### 雅克比的乘积注意不！是！矩阵乘法！ 

```python
import math

import jax
import jax.lax as lax
import jax.numpy as jnp
import jax.random as jrandom
import optax  # https://github.com/deepmind/optax

import equinox as eqx


f1 = lambda x : x ** 2

f2 = lambda x : 2 * x

f3 = lambda x : f2( f1(x) )

x = 2.

X = jnp.array( [ [2 , 2] ], jnp.float32 )

( A1, (grad, ) ) = jax.value_and_grad(f1, argnums=(0,))( x )

( A2, (grad2, ) ) = jax.value_and_grad(f2, argnums=(0,))( A1 )

( A3, (grad3, ) ) = jax.value_and_grad(f3, argnums=(0,))( x )


chain = grad2 * grad  # 复合函数求导的链式法则

assert ( chain == grad3 )


A11 = f1(X) # X 是 (1,2)   f1 的输出是 (1,2)  d f1 / d X 是 (1,2,1,2) 
( grad11, ) = jax.jacfwd(f1, argnums=(0,))( X )

A22 = f2(A11)
( grad22, ) = jax.jacfwd(f2, argnums=(0,))( A11 )

A33 = f3(X)
( grad33, ) = jax.jacfwd(f3, argnums=(0,))( X )


chain2 = grad22 * grad11 # 雅克比的乘积，注意不！是！矩阵乘法！ 

assert ( chain2 == grad33 )

a = 1

"""

d f1 = 2 * x

d f2 = 2


d f3 = d f2 ( f1(x)  ) * d f1 ( x )

     = 2 * 2 * x

     = 4 * x

"""
```



### chain rule in multiple dimensions

- https://math.stackexchange.com/questions/2888293/multidimensional-chain-rule-example

  > multidimensional chain rule, example



### NLLloss 损失函数

> **NLLLoss**的全称是Negative Log Likelihood Loss,中文名称是最大似然或者log似然代价函数
>
> 似然函数就是我们有一堆观察所得得结果，然后我们用这堆观察结果对模型的参数进行估计

> doc\lang\programming\pytorch\异或\OR_torch_version0.py
>
> criterion = nn.MSELoss() #nn.NLLLoss()  # https://zhuanlan.zhihu.com/p/264366034
>
>  \# NLLloss 和交叉熵一样只适用于分类任务， NLLLoss是基于softmax，softmax得到结果向量的概率分布，是离散值。回归任务建议MSE或MAE等损失函数
>
>  \# 否则提示多个target报错



### 常用Loss总结

#### 1. BCELoss

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824091538443.png" alt="image-20220824091538443" style="zoom: 67%;" />

#### 2. CELoss

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824091656783.png" alt="image-20220824091656783" style="zoom:67%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824091725867.png" alt="image-20220824091725867" style="zoom:67%;" />

#### 3. MSELoss

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824091824389.png" alt="image-20220824091824389" style="zoom:67%;" />

#### 4. FocalLoss

类别极度不均衡情况

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824092112912.png" alt="image-20220824092112912" style="zoom:67%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824092214029.png" alt="image-20220824092214029" style="zoom:67%;" />

画图所用到的代码：



```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y1, y2, y3, y4, y5 = (1-x)**0, (1-x)**0.5, (1-x)**1, (1-x)**2, (1-x)**5
plt.plot(x, y1, 'red')
plt.plot(x, y2, 'green')
plt.plot(x, y3, 'blue')
plt.plot(x, y4, 'yellow')
plt.plot(x, y5, 'purple')
# plt.title('line chart')
plt.xlabel('probability of ground truth class')
plt.ylabel('Weight Value') 
plt.show()
```

注意：用权重函数，加权BCELoss，则生成论文中的函数图像。由上图可知，其中gamma=2时，权重函数是个单调下降函数，预测的概率值较小时（即为难样本），Focal Loss所加的权重较大，使得整体loss变大，突出难样本；预测值概率值较大时（即为易样本），Focal Loss所加的权重较小，使得整体loss变小，这不要紧，因为预测值概率值较大（注意，此时y=1），我们就是希望loss较小。

```
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y1, y2, y3, y4, y5 = (1-x)**0 * (-np.log(x)), (1-x)**0.5 * (-np.log(x)), (1-x)**1 * (-np.log(x)), (1-x)**2 * (-np.log(x)), (1-x)**5 * (-np.log(x))
plt.plot(x, y1, 'red')
plt.plot(x, y2, 'green')
plt.plot(x, y3, 'blue')
plt.plot(x, y4, 'yellow')
plt.plot(x, y5, 'purple')
# plt.title('line chart')
plt.xlabel('probability of ground truth class')
plt.ylabel('Focal loss') 
plt.show()
```

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824092414759.png" alt="image-20220824092414759" style="zoom:67%;" />

```
# focal实现，引自：Focal Loss 分类问题 pytorch实现代码（简单实现）_镜中隐

import torch
import torch.nn as nn
 
#二分类
class FocalLoss(nn.Module):
 
    def __init__(self, gamma=2,alpha=0.25):
        super(FocalLoss, self).__init__()
        self.gamma = gamma
        self.alpha=alpha
    def forward(self, input, target):
        # input:size is M*2. M　is the batch　number
        # target:size is M.
        pt=torch.softmax(input,dim=1)
        p=pt[:,1]
        loss = -self.alpha*(1-p)**self.gamma*(target*torch.log(p))-\
               (1-self.alpha)*p**self.gamma*((1-target)*torch.log(1-p))
        return loss.mean()
```



#### 5. DiceLoss

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220824093332262.png" alt="image-20220824093332262" style="zoom:67%;" />

```
import torch.nn as nn
import torch.nn.functional as F
 
class SoftDiceLoss(nn.Module):
    def __init__(self, weight=None, size_average=True):
        super(SoftDiceLoss, self).__init__()
 
    def forward(self, logits, targets):
        num = targets.size(0)
        smooth = 1
        
        probs = F.sigmoid(logits)  # to (0, 1)
        m1 = probs.view(num, -1)  # (b,c,h,w)  -- (n, )
        m2 = targets.view(num, -1)  # (b,c,h,w)  -- (n, )
        intersection = (m1 * m2)  # A * B
 
        score = 2. * (intersection.sum(1) + smooth) / (m1.sum(1) + m2.sum(1) + smooth)
        score = 1 - score.sum() / num
        return score
```





### 分量是高维点在低维的投影



**向量的分量 = 高维空间的点（向量），在低维空间中的投影（分量，坐标轴上的坐标）**

**（向量内积，一行和一列的内积）影子（投影）是凸透镜和凹透镜，把低维向是量（点）放大或缩小，透镜的倍分是影子的长度**





**强化学习** ，是一种通过教会智能体（agents）**反复试错从而完成任务的机器学习方法**。深度强化学习指的是强化学习和 深度学习的结合。—— **OpenAI — Spinning Up** [u](https://spinningup.readthedocs.io/zh_CN/latest/user/introduction.html)



选择 **PyTorch** 的重要原因是：**用它来实现各种新的想法特别容易**，特别是在 GPU 集群上。







**A MATLAB Package for Markov Chain Monte Carlo with a Multi-Unidimensional IRT Model** [u](https://www.jstatsoft.org/article/view/v028i10)

- **此网站论文+代码 全开放下载，概率统计专题**



```
Kaggle 是一个数据科学竞赛的平台，很多公司会发布一些接近真实业务的问题，吸引爱好数据科学的人来一起解决。
可以锻炼数据挖掘和机器学习技能
```



PyTorch入门: Kaggle 泰坦尼克幸存者预测 [u](https://magolor.cn/2020/01/12/2020-01-12-blog-01/)

- 入门很细致 [u](https://zhuanlan.zhihu.com/p/53176091)

- top 3% [u](https://zhuanlan.zhihu.com/p/50194676)



线代笔记 jupyter

https://github.com/MacroAnalyst/Linear_Algebra_With_Python



**OpenAI — Spinning Up** [u](https://spinningup.readthedocs.io/zh_CN/latest/user/introduction.html)

**Udacity — deep-learning**-v2-pytorch [u](https://github.com/udacity/deep-learning-v2-pytorch)

**Open AI Five Dota2** [u](https://aistudio.baidu.com/aistudio/projectdetail/632270)

DearPyGui 基础 [u](https://blog.csdn.net/hekaiyou/article/details/109386393)

DearPyGui 实现队列模型仿真[u](https://www.zhihu.com/zvideo/1307375212308856832)

**清华大学学位论文模板** [u](https://github.com/tuna/thuthesis)



**How Pytorch Backward() function works**



### 优化方法

> Diagonal Gaussian Likelihood 对角高斯似然







[PyTorch for Deep Learning - Full Course / Tutorial](https://www.youtube.com/watch?v=GIsg-ZUy0MY&ab_channel=freeCodeCamp.org)

> [Linear Regression with PyTorch](https://jovian.ai/aakashns/02-linear-regression)

李宏毅2020机器学习深度学习(完整版)国语

> [课程主页](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html)
>
> [B站视频](https://www.bilibili.com/video/av94519857/)


[Pytorch autograd,backward详解](https://zhuanlan.zhihu.com/p/83172023)

[pytorch-tutorial-for-deep-learning-lovers](https://www.kaggle.com/kanncaa1/pytorch-tutorial-for-deep-learning-lovers)

[Yann LeCun 深度学习（Pytorch）2020 春季课程【官方字幕】](https://www.bilibili.com/video/av796677275/)

> [讲义](https://atcold.github.io/pytorch-Deep-Learning/)

[全-中英字幕-吴恩达 深度学习_Deep Learning_Pytorch特别制作版](https://www.bilibili.com/video/BV1BZ4y1M7hF/)

> [代码](https://gitee.com/inkCode/pytorch_tutorial)



SVD分解(一)：自编码器与人工智能 [u](https://kexue.fm/archives/4208)





深度神经网络（Deep Neural Networks， 简称DNN）是深度学习的基础

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20201106102822241.png" alt="image-20201106102822241" style="zoom: 67%;" />







**算子就是变换的别名，而变换又是函数的花俏说法。**



函数是一种向量

函数可进行加和与数乘运算，而因为向量也不过只有相加和数乘两种运算，所以最初以空间中箭头为背景来建立的线性代数的合理概念和解决问题的手段，例如：**线性变换，列空间、点积、特征值、特征向量等，都能够直接应用于函数**。



<img src="math summary.assets/image-20200820082343457.png" alt="image-20200820082343457" style="zoom: 67%;" />



映射是函数的推广，**雅可比是梯度的推广**

> 梯度是偏导的向量，雅可比是梯度的向量



一个多元函数求偏导，每一元就得到一个偏导，n元偏导组成一个向量，这就是梯度。

m个多元函数求偏导，每一函数得到一个梯度，m个梯度组成一个矩阵，这就是雅可比矩阵。



二阶导数是自变量与一阶导微小变化比

> 海森矩阵，是一个多元函数的二阶偏导数构成的方阵，描述了函数的局部曲率。



一阶优化算法

> 梯度下降仅使用一阶导的信息，所以它是一阶优化算法 
> 如果使用二阶导数的信息去指导优化时，这就是二阶优化算法 



一般是使用泰勒级数来对函数进行近似，通过二阶导数预期一个梯度下降步骤表现的多好
$$
f(x) \approx  f(x^0) + (x - x^0)^T g + \frac{1}{2} (x - x^0)\ H\ (x-x^0) \\

其中 g 是梯度， H 是 x^0 点的 海森矩阵。
$$




函数的输出是标量，映射的输入输出都是向量

> 单个神经元就是一个函数，神经网络的执行就是一个映射
>
> > m 组输入构成的**向量**是**神经网络(映射)**的输入，m个预测构成的**向量**是**神经网络(映射)**的输出



应用链式法则求**某节点对其他节点的雅可比矩阵**，它**从结果节点开始**，沿着计算路径向前追溯，**逐节点计算雅可比**。将神经网络和损失函数连接成一个计算图，则它的输入、输出和参数都是节点，可利用自动求导**求损失值对网络参数的雅可比**，从而得到梯度。



逻辑回归计算图，预测时将 $w$和$b$ 视为常量，将 $x$ 视为变量；训练时则将$x$ 视为常量，将 $w$ 和$b$ 视为变量。



梯度、散度、旋度、Jacobian、Hessian、Laplacian 的关系图 [u](https://zhuanlan.zhihu.com/p/35323714) [微分算子](https://zh.wikipedia.org/wiki/%E5%BE%AE%E5%88%86%E7%AE%97%E5%AD%90)

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20201029122824914.png" alt="image-20201029122824914" style="zoom:50%;" />

> 连续群是否一定是可微群，历史上是希尔伯特第五问题。答案是连续群一定是可微群
>
> **连续不一定可微，但连续群一定可微**，因为群的封闭性是一个特别强的要求，封闭性使群的连续性保可微性



$X$ 是神经网络的输入，总共$m$ 组，每一组是一个$n$ 维向量



$$
X = 
\begin{bmatrix}
x^{1}_{1} & x^{1}_{1} & \cdots & x^{1}_{m}  \\
x^{2}_{1} & x^{2}_{1} & \cdots & x^{2}_{m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{n}_{1} & x^{n}_{1} & \cdots & x^{n}_{m} \\
\end{bmatrix}
$$



例如，与门(OR Gate) 的全部参数为：

$$
X = \begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
\end{bmatrix}
\text {（与门的输入）}
$$

$$
Y =
\begin{bmatrix}
0 & 1 & 1 & 1 \\
\end{bmatrix}
\text{（与门的输出）}
$$

$$
W =
\begin{bmatrix}
w_1 & w_2  \\
\end{bmatrix}
\text{（线性变换，也就是权重）}
$$

$$
B =
\begin{bmatrix}
b_1 & b_2 & b_3 & b_4  \\
\end{bmatrix}
\text{（偏置）}
$$

维度检查：$(1 \times 2) (2 \times 4) \rightarrow (1 \times 4)$ 



前向传播的过程：

$$
f(W,X,B) = W \cdot X + B =

\begin{bmatrix}
w_1 & \cdots & w_n  \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{m}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{n}_{1} & x^{n}_{2} & \cdots & x^{n}_{m} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b_1 & \cdots & b_m  \\
\end{bmatrix}

\\

= 

\begin{bmatrix}
W \cdot x_1 + b_1 & \cdots & W \cdot x_m + b_m \\
\end{bmatrix} \\
= 
\begin{bmatrix}
f'_1(W, x_1, b_1) & \cdots & f'_m(W, x_m, b_m) \\
\end{bmatrix}
$$

维度检查：$(1 \times n) (n \times m) \rightarrow (1 \times m)$ 





激活
$$
g(x) = \frac{1}{1 + e^{-x}}
$$

$$
g( f(W,X) ) = 
\begin{bmatrix}
g(f'_1(W, x_1)) & \cdots & g(f'_m(W, x_m)) \\
\end{bmatrix}
$$


$$
E =
g( f(W,X) ) - Y
=
\begin{bmatrix}
g(f'_1(W, x_1)) - y_1 & \cdots & g(f'_m(W, x_m)) - y_m \\
\end{bmatrix}
=
\begin{bmatrix}
e_{1} & \cdots & e_{m}
\end{bmatrix}
$$


均方误差代价函数
$$
J(W) = 
 \frac{1}{2m} \sum^{m}_{i=1}( g(f'(W, x_i, b_i)) - y_i )^2
$$

$$
f'(W, x_i, b_i) = W \cdot x_i + b_i \ , i \in 1 \cdots m \\
=
\begin{bmatrix}
w_1 & \cdots & w_n  \\
\end{bmatrix}

\cdot

\begin{bmatrix}
x^{1}_{i}   \\
x^{2}_{i}  \\
\vdots \\
x^{n}_{i} \\
\end{bmatrix}

+ b_i  \\

= w_1  x^1_i + w_2  x^2_i + \cdots + w_n  x^n_i + b_i
$$

$$
\frac{\partial}{\partial w_{j}} f'(W, x_i, b_i) = x^j_i \ , (j \in 1 \cdots n, i \in 1 \cdots m)
$$

$$
\frac{d}{d x} g(x) = \frac{d}{d x} (\frac{1}{1 + e^{-x}}) =  \frac{ - \frac{d}{d x} (1 + e^{-x}) }{(1 + e^{-x})^{2}} \\
= \frac{ - \frac{d}{dx} e^{-x} }{(1 + e^{-x})^{2}} = \frac{ - \frac{d}{dx} \frac{1}{e^{x}} }{(1 + e^{-x})^{2}} = \frac{ - (\frac{- \frac{d}{dx} e^x}{(e^x)^2}) }{(1 + e^{-x})^{2}} = \frac{e^{-x}}{(1 + e^{-x})^2} \\
= (\frac{1}{1+e^{-x}}) (\frac{e^{-x}}{1 + e^{-x}}) \\
= (\frac{1}{1+e^{-x}}) (\frac{1 + e^{-x}}{1 + e^{-x}} -\frac{1}{1 + e^{-x}}) \\
= g(x)(1 - g(x))
$$

$$
(f \circ g)'(x) = f'(g(x))g'(x)
$$


$$
\frac{\partial}{\partial w_j} J(W) =  \frac{1}{2m} \sum^{m}_{i=1}( g(f'(W, x_i, b_i)) - y_i )^2
$$






#### 计算图雅可比

[计算图反向传播的原理及实现](https://zhuanlan.zhihu.com/p/69175484)

[常见激活函数优缺点与dead relu problem](https://zhuanlan.zhihu.com/p/92412922)



反向传播的含义：被传播的是损失值对仿射值的偏导数

> 偏导从后往前乘，进而计算每一个权值和偏置的偏导，这就是反向传播



计算图中的一条有向路径表示一个映射



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200927083845923.png" alt="image-20200927083845923" style="zoom: 50%;" />

由 $x$计算 $y$ 是一个多重复合映射。如果$x$ 是 $n$ 维向量， $y$是$m$ 维向量，则该计算图表示的计算是一个$\mathbb{R}^n \rightarrow \mathbb{R}^m$ 的映射。这个映射的“导数”是一个 $m \times n$的矩阵，即雅可比矩阵。根据链式法则， $y$对$x$的雅可比矩阵是：
$$
\frac{\partial y}{\partial x} = \frac{\partial y}{\partial u^k} \frac{\partial u^k}{\partial u^{k-1}} \cdots \frac{\partial u^2}{\partial u^1} \frac{\partial u^1}{\partial x}
$$




上标表示层，输入是第$0$ 层，输出是第$K$ 层

第$1$ 到$K-1$ 层是隐层

$x^0_i$ 第$0$ 层输入向量的第$i$ 分量

$n_0$ 第$0$ 层总共有$n_0$ 个分量

$a^k_i$ 第$k$ 层第$i$ 个神经元的仿射值

$x^k_i$ 第$k$ 层第$i$ 个神经元的激活值

第$k$ 层有$n_k$ 个神经元，所以该层有$n_k$ 个输出


$$
x^k_i = f(a^k_i) = f(\sum^{n_{k-1}}_{s=1} w^k_{i,s} x^{k-1}_s + b^k_i)
$$

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200927112132641.png" alt="image-20200927112132641" style="zoom:50%;" />




$$
a^k_i = \sum^{n_{k-1}}_{j=1} w^k_{i,j} x^{k-1}_j + b^k_i
$$

$$
\frac{\partial a^k_i}{\partial w^k_{i,j}} = x^{k-1}_j
$$
损失值$\mathcal{L}$  对$w^k_{i,j}$ 的偏导数由链式法则给出：
$$
\frac{ \partial{\mathcal{L}} } { \partial w^k_{i,j} } = 
\frac{ \partial{\mathcal{L}} } { \partial a^k_i }
\cdot
\frac{\partial a^k_i}{\partial w^k_{i,j}}
$$
既，损失值对某个权值的偏导，等于损失对映射值的偏导乘以映射值对权值的偏导

后偏导  * 前偏导 * 前前偏导 * ... 一直乘到要求的那个偏导

p.164 	



损失值对某个偏置的偏导
$$
\frac{ \partial{\mathcal{L}} } { \partial b^k_{i} } = 
\frac{ \partial{\mathcal{L}} } { \partial a^k_i }
\cdot
\frac{\partial a^k_i}{\partial b^k_{i}}
= \frac{ \partial{\mathcal{L}} } { \partial a^k_i }
$$



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200927155441465.png" alt="image-20200927155441465" style="zoom: 50%;"/>



将激活值$x^k_i$ 看成是变量，同层的其他激活值是常量，则下一层神经元的仿射值由映射$g:\mathbb{R} \rightarrow \mathbb{R}^{n_{k+1}}$ 给出：


$$
g(x^k_i) = \begin{pmatrix}
a^{k+1}_1 \\
a^{k+1}_2 \\
\vdots \\
a^{k+1}_{n_{k+1}} \\
\end{pmatrix} 
= 
\begin{pmatrix}
\sum^{n_k}_{j=1} w^{k+1}_{1,j} x^k_j + b^{k+1}_1  \\
\sum^{n_k}_{j=1} w^{k+1}_{2,j} x^k_j + b^{k+1}_2  \\
\vdots \\
\sum^{n_k}_{j=1} w^{k+1}_{{n_{k+1}}, j} x^k_j + b^{k+1}_{n_{k+1}}  \\
\end{pmatrix}
$$


最后，映射$h:\mathbb{R}^{n_{k+1}} \rightarrow \mathbb{R}$ 将第$k+1$ 层的仿射值映射到损失值$\mathcal{L}$，若将损失值$\mathcal{L}$ 视作$a^k_i$ 的函数，则它是三个映射的复合： 


$$
\mathcal{L}(a^k_i) = (h \circ g \circ f)(a^k_i)
$$


$\mathcal{L}$ 对$a^k_i$ 的雅可比（导数）是这三个映射在相应位置的雅可比之积：


$$
\frac{\partial \mathcal{L}}{\partial a^k_i} = A_h \cdot A_g \cdot A_f
$$









向量导数的链式法则
$$
\vec{x} \in \mathbb{R}^m \ , \vec{y} \in \mathbb{R}^n  \\

g:\mathbb{R}^m \rightarrow \mathbb{R}^n， g(\vec{x}) = \vec{y}  \\
f:\mathbb{R}^n \rightarrow \mathbb{R}， f(\vec{y}) = z
$$



[详解Pytorch 自动微分里的（vector-Jacobian product）](https://zhuanlan.zhihu.com/p/65609544)

[带你少走弯路：强烈推荐的Pytorch快速入门资料和翻译](https://zhuanlan.zhihu.com/p/87263048)

[AI算法工程师手册](http://www.huaxiaozhuan.com/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/chapters/2_bp.html)

[向量、矩阵和张量的导数](https://zhuanlan.zhihu.com/p/29502026)

[多元复合函数求导法则的教学思考](https://image.hanspub.org/Html/2-1250530_21119.htm)



### 多元复合函数求导法则

#### 导数是自变量因变量微小变化比

> 偏导数必须要先选取坐标（选取所有待求偏导的变量）以后，才有意义

[微积分本质](https://zhuanlan.zhihu.com/p/141064528)

 

##### Pytorch 计算雅可比

```python
x = torch.ones(3, requires_grad=True)
def calc(x):
	return torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))
jacobian = torch.autograd.functional.jacobian(calc, x)
```

```python
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md

import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

import numpy as np

import torch

# F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)

# dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I

# dF / dX = I 克罗内克积符号 A^T    dX 形状是 (4*2) ，所以 I 是 (2*2)。单位阵必是方阵

# G = FV # (1*2) . (2*1) => (1*1)
    # [ [f00, f01]  ] . [ [v00], [v10]  ]
    # 

A = jnp.array( [[1,2]] , jnp.float32 )

X = jnp.array( [[3,4],[5,6]] , jnp.float32 )

V = jnp.array( [[7],[8]] , jnp.float32 )

def f(A, X):
    return jnp.dot( A, X )

F = f( A, X )
G = f( F, V )

l = lambda A, X, V: f( f(A, X), V )
L = l(A, X, V)
( grad_X, grad_V) = jax.jacfwd(l, argnums=(1,2))( A, X, V )  # dG / dX 和  dG / dV
    # 为了和后面分步计算的雅克比乘积结果对比 (链式法则求各层的梯度)

I = jnp.eye( 2 )

A_T = jnp.transpose(A)

kr = jax.numpy.kron(I, A_T) # (4*2)  # 求 dF / dX
    # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 2 个元素，参数总共 4 个元素，求导结果总共应该是 8 个元素
        # df_1(x) .. df_n(x) 横向展开， dx 纵向展开
        # kr 的转置应该就是雅可比，它是 dx 横向展开, df(x) 纵向展开

kr2 = jnp.transpose(F) # (2*1)  # 求 dG / dV



a = 1

# 下面用 jax 自动微分验证

( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
    # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样

grad_42 = jnp.reshape(grad, (4, 2)) # 和前面 kr 一样了


( grad2, ) = jax.jacfwd(f, argnums=(1,))( F, V )

grad2_21 = jnp.reshape(grad2, (2, 1))

a = 1


y, vjp_fn = jax.vjp(f, A, X) # 返回函数的计算结果，还有用于计算 vjp 的函数 vjp_fn，它需要一个向量作为参数
    # 你传一个向量进去，vjp_fn 就会给你一个 v * 雅可比 的结果


AA = torch.tensor(A.__array__())
XX = x = torch.tensor(X.__array__())

def ff(AA, XX):
    return torch.mm(AA, XX) # 数学里的矩阵乘法，要求两个Tensor的维度满足矩阵乘法的要求

FF = ff(AA, XX)

jacobians = torch.autograd.functional.jacobian(ff, (AA, XX))
jacobian_XX = jacobians[1]  # (1, 2, 2, 2)  和 jax 算出来的 grad 是一样的

jacobian_XX_42 = torch.reshape(jacobian_XX, (4, 2)) # 和前面 kr 一样了
```



##### vector-Jacobian product 

- $J \cdot v$ 中的v 是人为的给各**微量变化比加权重**，调大调小变化影响力

  > $J^T \cdot v$ 是列向量 [CSC321 Lecture 10：Automatic Differentiation]()
  >
  > $v^T \cdot J$ 是行向量

```python
x = torch.ones(3, requires_grad=True)
y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))
v = torch.tensor([3, 5, 7])
y.backward(v)
print(x.grad)
```





一个函数的变换是线性的是什么意思?

> Additivity: $L(\overrightarrow{v}+\overrightarrow{w}) = L(\overrightarrow{v})+L(\overrightarrow{w})$
> Scaling: $L(c \overrightarrow{v}) = c L(\overrightarrow{v})$



#### 求导就是一种线性运算，它将一个函数变成另一个函数

他符合以上两个条件

<img src="math summary.assets/image-20200718160301631.png" alt="image-20200718160301631" style="zoom:67%;" />



**将曲的函数图像掰直**，掰直的图像就是导函数

> 导数是函数的局部性质，对函数进行局部的线性逼近，在局部 "以直代曲"，
>
> 一个函数在某一点的导数描述了这个函数在这一点附近的变化率。





**梯度属于向量分析（或向量微積分）的范畴**



$$
A_{g} = \begin{pmatrix} 
\nabla y_1(X)^T \\

\vdots \\

\nabla y_n(X)^T \\
\end{pmatrix}

= 

\begin{pmatrix} 
\frac{\partial y_1}{\partial x_1} & \cdots & \frac{\partial y_1}{\partial x_m}\\


\vdots & \ddots & \vdots \\ 

\frac{\partial y_n}{\partial x_1} & \cdots & \frac{\partial y_n}{\partial x_m}\\

\end{pmatrix}
$$


$$
g:\mathbb{R}^m \rightarrow \mathbb{R}^n
$$


$$
g \bigg (
\begin{bmatrix}
x_{1}  \\
x_{2}  \\
\vdots  \\
x_{m} \\
\end{bmatrix}
\bigg ) 
=
\begin{bmatrix}
y_{1}  \\
y_{2}  \\
\vdots  \\
y_{n} \\
\end{bmatrix}
$$




$$
A_{f} = \nabla z(Y)^T =

\begin{pmatrix} 
\frac{\partial z}{\partial y_1} & \cdots & \frac{\partial z}{\partial y_n}\\
\end{pmatrix}
$$

$$
f:\mathbb{R}^n \rightarrow \mathbb{R}
$$

$$
f \bigg (
\begin{bmatrix}
y_{1}  \\
y_{2}  \\
\vdots  \\
y_{n} \\
\end{bmatrix}
\bigg ) 
= z
$$


$$
Jacobi(f \oplus g)_{(1 \times m)} = A_f \cdot A_g = \begin{pmatrix} 
\frac{\partial z}{\partial y_1} & \cdots & \frac{\partial z}{\partial y_n}\\
\end{pmatrix}

\begin{pmatrix} 
\frac{\partial y_1}{\partial x_1} & \cdots & \frac{\partial y_1}{\partial x_m}\\


\vdots & \ddots & \vdots \\ 

\frac{\partial y_n}{\partial x_1} & \cdots & \frac{\partial y_n}{\partial x_m}\\

\end{pmatrix}
$$

$$
Jacobi(f \oplus g)_{1,j} = \frac{\partial z}{\partial x_j}  = \sum^n_{s=1} \frac{\partial z}{\partial y_s} \frac{\partial y_s}{\partial x_j} , \ for \ j \in 1 ... m
$$

​	


$$
a^1_{i,*}:\mathbb{R}^{(1 \times n)} \rightarrow \mathbb{R}^{1 \times m}, for \ i \in 1...n
$$

$$
A_{a^1_{i,*}} = \begin{pmatrix} 
\nabla a^1_{i,1}(W^1_{i,*})^T \\

\vdots \\

\nabla a^1_{i,m}(W^1_{i,*})^T \\
\end{pmatrix}

=

\begin{pmatrix} 
\frac{\partial a^1_{i,1}}{\partial w_{i,1}} & \cdots & \frac{\partial a^1_{i,1}}{\partial w_{i,n}} \\


\vdots & \ddots & \vdots \\ 

\frac{\partial a^1_{i,m}}{\partial w_{i,1}} & \cdots & \frac{\partial a^1_{i,m}}{\partial w_{1,n}} \\

\end{pmatrix}
$$

$$
\begin{bmatrix}
w^{1}_{1,1} & w^{1}_{1,2} & \cdots & w^{1}_{1,n}  \\
w^{1}_{2,1} & w^{1}_{2,2} & \cdots & w^{1}_{2,n} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{1}_{n,1} & w^{1}_{n,2} & \cdots & w^{1}_{n,n} \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
x^{0}_{1,1} & x^{0}_{1,2} & \cdots & x^{0}_{1,m}  \\
x^{0}_{2,1} & x^{0}_{2,2} & \cdots & x^{0}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{0}_{n,1} & x^{0}_{n,2} & \cdots & x^{0}_{n,m} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b^{1}_{1,1} & b^{1}_{1,2} & \cdots & b^{1}_{1,m}  \\
b^{1}_{2,1} & b^{1}_{2,2} & \cdots & b^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
b^{1}_{n,1} & b^{1}_{n,2} & \cdots & b^{1}_{n,m} \\
\end{bmatrix}

\\

= 

\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,m}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{n,1} & a^{1}_{n,2} & \cdots & a^{1}_{n,m} \\
\end{bmatrix}
$$

$$
A_{x^1_{i,*}} = \begin{pmatrix} 
\nabla x^1_{i,1}(a^1_{i,*})^T \\

\vdots \\

\nabla x ^1_{i,m}(a^1_{i,*})^T \\
\end{pmatrix}

=

\begin{pmatrix} 
\frac{\partial x^1_{i,1}}{\partial a^1_{i,1}} \\


\vdots \\

\frac{\partial x^1_{i,m}}{\partial a^1_{i,1}} \\

\end{pmatrix}
$$

$$
g \bigg (
\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,m}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{n,1} & a^{1}_{n,2} & \cdots & a^{1}_{n,m} \\
\end{bmatrix}
\bigg )

= 

\begin{bmatrix}
x^{1}_{1,1} & x^{1}_{1,2} & \cdots & x^{1}_{1,m}  \\
x^{1}_{2,1} & x^{1}_{2,2} & \cdots & x^{1}_{2,m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{1}_{n,1} & x^{1}_{n,2} & \cdots & x^{1}_{n,m} \\
\end{bmatrix}
$$






$$
\frac{\mathrm{d} z}{ \mathrm{d} X } = \frac{\mathrm{d} z}{ \mathrm{d} Y } \frac{\mathrm{d} Y}{ \mathrm{d}X }
$$

$$
\frac{\mathrm{d} z}{ \mathrm{d} Y } =

\begin{bmatrix}
\frac{\partial z}{\partial y_{1}}  \\
\frac{\partial z}{\partial y_{2}}  \\
\vdots  \\
\frac{\partial z}{\partial y_{n}} \\
\end{bmatrix}
$$

$$
\frac{\mathrm{d} Y}{ \mathrm{d} X } =

\begin{bmatrix}
\frac{\partial Y}{\partial x_{1}}  &
\frac{\partial Y}{\partial x_{2}}  &
\cdots  
\frac{\partial Y}{\partial x_{m}} &
\end{bmatrix} 
=

\begin{bmatrix}
\frac{\partial y_1}{\partial x_{1}} & \frac{\partial y_2}{\partial x_{1}} & \cdots & \frac{\partial y_n}{\partial x_{1}} \\

\frac{\partial y_1}{\partial x_{2}} & \frac{\partial y_2}{\partial x_{2}} & \cdots & \frac{\partial y_n}{\partial x_{2}} \\

\vdots  & \vdots & \ddots & \vdots\\

\frac{\partial y_1}{\partial x_{m}} & \frac{\partial y_2}{\partial x_{m}} & \cdots & \frac{\partial y_n}{\partial x_{m}} \\

\end{bmatrix}
$$

(1,n)(n,m)->(1,m)

(m,n)(n,1)->(m,1)

$$
\frac{\partial z}{\partial x_i} = \sum^n_{j=1} \frac{\partial z}{\partial y_j} \frac{\partial y_j}{\partial x_i} , \ i = 1, 2, \cdots ,m
$$




映射是函数的推广，**雅可比是梯度的推广**

> 梯度是偏导的向量，雅可比是梯度的向量
>
> 有些教材认为，实值函数对列向量求导的结果是**列向量**，有些教材认为上述结果需要再做一次转置，即梯度是**行向量**



一个多元函数求偏导，每一元就得到一个偏导，n元偏导组成一个向量，这就是梯度。

m个多元函数求偏导，每一函数得到一个梯度，m个梯度组成一个矩阵，这就是雅可比矩阵。





![image-20200925164844085](深入理解神经网络：从逻辑回归到CNN.assets/image-20200925164844085.png)


$$
\frac{\partial}{\partial w_{j}}
J(W) = 
 \frac{\partial}{\partial w_{j}} \bigg [ \frac{1}{2m} \sum^{m}_{i=1}( g(f'(W, x_i)) - y_i )^2
 
 \bigg ] \\
 
 = \frac{1}{2m} \sum^{m}_{i=1}\frac{\partial}{\partial w_{j}} ( g(f'(W, x_i)) - y_i )^2   \quad \text{(by linearity of the derivative)} \\
= \frac{1}{2m} \sum^{m}_{i=1} 

2 \cdot ( g(f'(W, x_i)) - y_i ) \frac{\partial}{\partial w_{j}} ( g(f'(W, x_i)) - y_i )   \quad \text{(by chain rule)} \\
= \frac{1}{2m} \cdot 2 \sum^{m}_{i=1} 

( g(f'(W, x_i)) - y_i ) \bigg [ \frac{\partial}{\partial w_{j}} g(f'(W, x_i)) - \frac{\partial}{\partial w_{j}} y_{i} \bigg ]  \quad \text{(by linearity of the derivative)}  \\
= \frac{1}{m} \sum^{m}_{i=1} 

(g(f'(W, x_i)) - y_{i}) \bigg [ \frac{\partial}{\partial w_{j}} g(f'(W, x_i)) - 0 \bigg ]   \\

= \frac{1}{m} \sum^{m}_{i=1} 

(g(f'(W, x_i)) - y_{i}) \frac{\partial}{\partial w_{j}} g(f'(W, x_i))     \\
= \frac{1}{m} \sum^{m}_{i=1} 

(g(f'(W, x_i)) - y_{i}) g(f'(W, x_i))(1 - g(f'(W, x_i))) x^{i}_{j}
$$










梯度是偏导的向量，雅可比是梯度的向量

$$
a_i = \nabla f'_i(W, x_i) = \begin{pmatrix} \frac{\partial{f'_i(W, x_i)}}{\partial{w_1}} \\ \vdots \\ \frac{\partial{f'_i(W, x_i)}}{\partial{w_n}}  \end{pmatrix}
, i \in 1 \cdots m
$$

$$
A_{m \times n} = \begin{pmatrix}
(a_{1})^{T} \\
\vdots \\
(a_{m})^{T}
\end{pmatrix}
$$










$A$ 就是$f(W,X)$ 的雅可比矩阵
$$
f(W+h,X) = f(W, X) + A h
$$



$f(W+h, X)$ 可被**$f(W, X) + A h$** 近似，近似误差随$h$ 趋于零向量而**迅速消失**





#### 神经网络雅可比


$$
a=\left(
\begin{array}{c}
 x_1^3+2x_2^2 \\
 3x_1^4+7x_2
\end{array}
\right);b=\left(
\begin{array}{c}
 x_1 \\
 x_2
\end{array}
\right);J=\left(
\begin{array}{cc}
 \frac{\partial \left(x_1^3+2x_2^2\right)}{\partial x_1} & \frac{\partial \left(x_1^3+2x_2^2\right)}{\partial x_2} \\
 \frac{\partial \left(3x_1^4+7x_2\right)}{\partial x_1} & \frac{\partial \left(3x_1^4+7x_2\right)}{\partial x_2}
\end{array}
\right);
$$




$f(x+h) = f(x) + A h$

> $A$ 是$f$ 的雅可比





$(a_{i,*})^T$ 是矩阵A 的第$i$ 行，$a_{i,*}$ 是函数$f^i(x)$ 在$x$ 的梯度：
$$
a_{i,*} = \nabla f^i(x) = \begin{pmatrix} \frac{\partial{f^i(x)}}{\partial{x_1}} \\ \vdots \\ \frac{\partial{f^i(x)}}{\partial{x_n}}  \end{pmatrix}
$$

$$
A_{m \times n} = \begin{pmatrix} \frac{\partial{f^i(x)}}{\partial{x_1}} & \cdots & \frac{\partial{f^i(x)}}{\partial{x_n}} \\
\vdots & \ddots & \vdots \\
\frac{\partial{f^m(x)}}{\partial{x_1}} & \cdots & \frac{\partial{f^m(x)}}{\partial{x_n}}
\end{pmatrix}
$$





$f'':\mathbb{R}^n \rightarrow \mathbb{R}^1$ 是一个线性函数

$$
f''(x_i) = W \cdot \ x_i \ , i \in 1 \cdots m
$$

> 线性函数，等同于线性变换，函数又可以认为是一种向量
>
> 所以这里的指的线性变换就是权重向量$W$，$W$对$x_i$ 进行了线性变换
>
> 维度变化：$(1 \times n) (n \times 1) \rightarrow (1 \times 1)$ ，所以线性变换$W$ **的维度是$(1 \times n)$**
>
> > 读作：线性变换将$1$ 个$n$ 维向量变换成$1$ 个 $1$ 维向量 





$f'$ 是一个仿射函数
$$
f'(x_i) = W \cdot \ x_i + b_i \ , i \in 1 \cdots m
$$

> 仿射函数是一个线性函数加上一个常量
>
> $b_i$ 的维度是$(1 \times 1)$ ，$B$ 的维度是$(1 \times m)$ 





$f$ 是一个仿射映射
$$
f(X) = \begin{bmatrix} f'_1(x_{1}) & \cdots &  f'_m(x_{m}) \end{bmatrix} = W \cdot X + B \\
=
\begin{bmatrix}
w_1 & \cdots & w_n  \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{m}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{n}_{1} & x^{n}_{2} & \cdots & x^{n}_{m} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b_1 & \cdots & b_m  \\
\end{bmatrix}
$$

> 仿射映射可以看作由若干个仿射函数组成
>
> 大写的$X$ 表示这是一个矩阵
>
> 小写的$x$ 表示这是一个向量，$x$ 的下标表示这是一个列向量，下标的数字指出它是矩阵中的第几列










$$
\begin{bmatrix}
w_1 & \cdots & w_n  \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{m}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{m} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{n}_{1} & x^{n}_{2} & \cdots & x^{n}_{m} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b_1 & \cdots & b_m  \\
\end{bmatrix}
$$












如果映射$f:\mathbb{R}^{n \times m} \rightarrow \mathbb{R}^m$ 在自变量$x$ 附近可以写成：
$$
f(x+h) = f(x) + A h + \mathcal{R}(h)
$$


$A$ 由$x$ 决定，余项$\mathcal{R}(h)$ 是$m$ 维向量，满足：





其中：
$$
X = 
\begin{bmatrix}
x^{1}_{0} & x^{1}_{1} & \cdots & x^{1}_{n}  \\
x^{2}_{0} & x^{2}_{1} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{0} & x^{m}_{1} & \cdots & x^{m}_{n} \\
\end{bmatrix}
$$


与门(OR) 运算实际上就是一个仿射映射


$$
X = \begin{bmatrix}
0 & 0 \\
0 & 1 \\
1 & 0 \\
1 & 1 \\
\end{bmatrix}
\text {（与门的输入）}
$$

$$
Y =
\begin{bmatrix}
0  \\
1  \\
1  \\
1  \\
\end{bmatrix}
\text{（与门的输出）}
$$

如何找到从$x$ 到$y$ 的线性变换（也就是w）？

> 既找到一个线性函数，将$X$ 中的行向量$x$ 变换到$Y$ 中的行向量$y$ 



$f:\mathbb{R}^n \rightarrow \mathbb{R}^m$ 是线性映射，必然存在一个$m \times n$ 的矩阵A，对任意$\vec{x} \in \mathbb{R}^n$ 满足：
$$
f(\vec{x}) = A \vec{x}
$$

> $A$ 是一个$m \times n$ 的矩阵，这个矩阵本身就是线性变换
>
> - 注意前面函数就是向量这个事实，$f$ 就是线性变换，$f$ 和$A$ 是同一个东西
>
> 为什么从$n$ 维到$m$ 维向量的线性映射的维度是$m \times n$ ?
>
> > **一个矩阵代表一个线性变换，矩阵的列是变换后的新空间的基向量**
> >
> > > 新基向量的线性组合构成了新向量
> > >
> > > 实际上是整个空间被变换了，原基向量被变换成了新基向量，原空间里的所有向量也跟着被变换了
> > > $m \times n$ 的含义是$n$ 个$m$ 维基向量，也就是说这个新空间是$m$ 维的（如果每个基向量都能贡献新维度的话，也就是说它们是线性独立的）
> > >
> > > **原向量所有维度上的点作为数乘，数乘$n$ 个$m$ 维基向量，就得到了新空间的向量。这就是线性组合**
> > >
> > > > **数乘本身在变换中保持不变，变化的实际上是基向量**。因为原向量可以表示成原基向量的数乘，新向量也可以表示成新基向量的数乘，而这两者的数乘是完全一样的
>
> 维度检查：$(m \times n) (n \times 1) \rightarrow (m \times 1)$ 
>
> > **读作：$n$ 个$m$ 维向量将$1$ 个$n$ 维向量线性变换成$1$ 个$m$ 维向量**



与门(OR) 运算的仿性映射$f$ 表示为：
$$
f(X) = W \cdot X + B = Y
$$
其中$X$ 的维度是$(2 \times 4)$，$Y$ 的维度是$(1 \times 4)$

> 将4 个2 维向量，线性变换成4个1 维向量
>
> 这个变换$W$ 的维度是$(1 \times 2)$
>
> 维度检查：$(1 \times 2) (2 \times 4) \rightarrow (1 \times 4)$ 


$$
X = \begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
\end{bmatrix}
\text {（与门的输入）}
$$

$$
Y =
\begin{bmatrix}
0 & 1 & 1 & 1 \\
\end{bmatrix}
\text{（与门的输出）}
$$

$$
W =
\begin{bmatrix}
w_1 & w_2  \\
\end{bmatrix}
\text{（线性变换）}
$$

$$
B =
\begin{bmatrix}
b_1 & b_2 & b_3 & b_4  \\
\end{bmatrix}
\text{（偏置）}
$$



前向


$$
h_{W}(X) =
W \cdot X
=
\begin{bmatrix}
w_1 & w_2  \\
\end{bmatrix}

\cdot

\begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
\end{bmatrix}
$$










**w 是一个法向量(一根掍)，同时也是一个线性变换**。它将垂直于w 的平面上的所有点全部变换成自身的某一点（既棍上的一点）（这是**投影变换**？对应的应该还有一个**内积变换**？）

投影是线性变换的同义词，投影向量的模长是垂直法向量的平面的截距

- 这个截距就是仿射变换中的常数b


















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


















仿射映射可以看作由若干个仿射函数组成







## 反向传播

若要透彻理解反向传播算法的原理，需要掌握**映射、仿射映射、雅可比矩阵，以及映射求导的链式法则**。

映射是函数的推广，雅可比矩阵是梯度的推广



反向传播是**计算损失函数对**神经网络**权值和偏置的偏导数**的算法。有了偏导数也就有了**梯度**，然后利用**梯度下降算法更新权值和偏置**



**狭义的反向传播只适用于多层全连接神经网络**，它是计算图自动求导的一个特例



### 映射(map)

**函数的输出是标量**，既实数。映射是函数的推广，**映射的输入输出都是向量**。函数是映射的特例，因为**标量是一维向量**。

单个神经元就是一个函数，神经网络的执行就是一个映射。



#### 线性映射

$\vec{x}, \vec{y}$ 是任意向量，$a, b$ 是任意实数，如果映射$f:\mathbb{R}^n \rightarrow \mathbb{R}^m$满足：
$$
f(a \vec{x}+b\vec{y}) = af(\vec{x}) + bf(\vec{y})
$$

**则称$f$ 是线性映射**(linear map)

> 可以将$f$ 看成一个变换矩阵，$\vec{x}, \vec{y}$ 看成基向量，$a \vec{x}+b\vec{y}$ 是基向量的线性组合得到的一个新向量，
>
> 整个操作是：对向量进行变换，等同于先分别对向量的分量中的基向量进行变换，然后再把数乘(模长的缩放)放进来



$f:\mathbb{R}^n \rightarrow \mathbb{R}^m$ 是线性映射，必然存在一个$m \times n$ 的矩阵A，对任意$\vec{x} \in \mathbb{R}^n$ 满足：
$$
f(\vec{x}) = A \vec{x}
$$

> 维度检查：$(m \times n) (n \times 1) \rightarrow (m \times 1)$ 



证明：

任意 $\vec{x} \in \mathbb{R}^n$ 必然能够以**标准正交基**的线性组合表示：
$$
\vec{x} = \sum^n_{i=1} x_i e^i
$$

因为$f$ 是线性映射，所以：

$$
f(\vec{x}) = f(\sum^n_{i=1} x_i e^i ) = \sum^n_{i=1} x_i f(e^i) = (f(e^1)\  \cdots \ f(e^n)) \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = A \ \vec{x}
$$

> 整个操作是：对向量进行变换，等同于先分别对向量的分量中的基向量进行变换，然后再把数乘(模长的缩放)放进来

$f:\mathbb{R}^n \rightarrow \mathbb{R}^m$ ，所以$e^i$ 是n 维列向量，$f(e^i)$ 是m 维列向量，$
A$ 是 $m \times n$ 矩阵(**$n$ 个$m$ 维向量** )。

 

线性映射必将$\mathbb{R^n}$ 中的零向量映射到$\mathbb{R^m}$  中的零向量，因为：

$$
f(0) = A \ 0 = 0
$$



#### 仿射映射



仿射映射(affine map)是线性映射加上一个常向量，b：
$$
f(x) = A \ x + b
$$


如果b 不是零向量，则仿射映射不保持零向量。仿射映射可以看作由若干个仿射函数组成：
$$
f(x) = \begin{pmatrix} f^1(x) \\ \vdots \\ f^m(x) \end{pmatrix} = A \ x + b = \begin{pmatrix} (a_{1, \ *})^T x + b_1 \\ \vdots \\ (a_{m, \ *})^T x + b_m \end{pmatrix}
$$




$f$ 的第$i$ 分量用$f^i$ 表示，$(a_{i,*})^T$ 是矩阵A 的第$i$ 行。$f^i$ **是输出为标量的函数。**





#### 雅可比矩阵

[计算图反向传播的原理及实现](https://zhuanlan.zhihu.com/p/69175484)

[“瞬时运动学”——还是从关节空间到操作空间（雅可比矩阵上篇）](https://www.guyuehome.com/5627)

你还需要懂得简单的**向量求导运算**——其实很简单啦，如果你不知道怎么对向量求导，那就把它当一列标量一个一个写出来，比如这样：



<img src="深入理解神经网络：从逻辑回归到CNN.assets/1-13.jpg" alt="干货 | “瞬时运动学”——还是从关节空间到操作空间（雅可比矩阵上篇）插图" style="zoom: 67%;" />



 

不知道行列怎么分布？把分母乘到右边，算一下**左边是3×1向量，右边是3×2矩阵乘以2×1向量 = 3×1向量**，左右相等，搞定！简单粗暴，方便有效。哎呀，一不小心，把**雅可比矩阵（Jacobian Matrix）**都给写出来了呢。（想要知道数学上是怎么定义推导出向量求导方法的请去上数学课，我只负责教你记住啦:p）



如果映射$f:\mathbb{R}^n \rightarrow \mathbb{R}^m$ 在自变量$x$ 附近可以写成：
$$
f(x+h) = f(x) + A h + \mathcal{R}(h)
$$


$A$ 由$x$ 决定，余项$\mathcal{R}(h)$ 是$m$ 维向量，满足：
$$
lim_{\|\boldsymbol{h}\| \rightarrow 0} \frac{\mathcal{R}(h)}{\|\boldsymbol{h}\|} = 0
$$

则称映射$f$ 在$x$ 可导。**$A$ 是$f$ 在$x$ 的雅可比矩阵( Jacobian matrix )**，简称雅可比。

这种情况意味着，$f(x+h)$ 可被**仿射映射$f(x) + A h$** 近似，近似误差随$h$ 趋于零向量而**迅速消失**——误差的每个分量都是$\|\boldsymbol{h}\|$ 的**高阶无穷小**。

> **大家都是无穷小，都趋向于零，谁跑得快谁就是高阶**
>
> 高阶无穷小是一个比较，即在两个无穷小之间的比较一个相对于另一个是高阶。
> 那么什么是高阶呢，无穷小都趋向于零，一个无穷小**比另一个趋向于0的速度更快**，那就是高阶无穷小。
>
> 一条直线上的点的数量是无穷多个，记为n。
> 两条直线上的点的数量也是无穷多个，记为m。
> 一个平面上的点的数量也是无穷多个，记为l。
>
> 有以下几个结论：
> l>>m
> l >>n
> m~n
> 所以l就是m和n的高阶无穷大。
> 在以上空间任选某点选中任意点的概率就是1/n,1/m,1/l，其中1/l就是1/n,1/m的高阶无穷小。



$(a_{i,*})^T$ 是矩阵A 的第$i$ 行，$a_{i,*}$ 是函数$f^i(x)$ 在$x$ 的梯度：
$$
a_{i,*} = \nabla f^i(x) = \begin{pmatrix} \frac{\partial{f^i(x)}}{\partial{x_1}} \\ \vdots \\ \frac{\partial{f^i(x)}}{\partial{x_n}}  \end{pmatrix}
$$

$$
A_{m \times n} = \begin{pmatrix} \frac{\partial{f^i(x)}}{\partial{x_1}} & \cdots & \frac{\partial{f^i(x)}}{\partial{x_n}} \\
\vdots & \ddots & \vdots \\
\frac{\partial{f^m(x)}}{\partial{x_1}} & \cdots & \frac{\partial{f^m(x)}}{\partial{x_n}}
\end{pmatrix}
$$



映射是函数的推广，**雅可比是梯度的推广**

https://blog.csdn.net/m0_46510245/article/details/108614235

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200923155803237.png" alt="image-20200923155803237" style="zoom:50%;" />








#### 平面的倾斜程度与法向量的模长有关

#### 平面的朝向由法向量在平面上的投影决定



仿射函数
$$
y = b + \sum^{n}_{i=1} w_i x_i
$$

$$
w_1 x_1 + w_2 x_2 - y = (w_1, w_2, -1) \begin{pmatrix} x_1 \\ x_2 \\ y \end{pmatrix} = -b
$$

内积为常数，也就是说**仿射变换的图像是3维空间中的一张平面**。

> **点积是把向量从二维变换到一维，然后缩放**
>
> - 缩放的数乘就是另一个向量的模长



变换前是
$$
\begin{bmatrix}
x_1 \ \text{i-hat} \\
x_2 \ \text{j-hat} \\
y \ \ \text{k-hat} \\
\end{bmatrix}
$$
也就是
$$
\begin{bmatrix}
 1 \ \text{i-hat} * x_1 \\
1 \ \text{j-hat} * x_2 \\
1 \ \ \text{k-hat} * y \\
\end{bmatrix}
$$


首先把基向量 $(1 \ \text{i-hat}, 1 \ \text{j-hat}, 1 \ \ \text{k-hat} )^T$ 变换成新的基向量：
$$
\begin{bmatrix}
w_1 \ \text{i-hat} & w_2 \ \text{i-hat} & -1\ \ \text{i-hat}
\end{bmatrix}
$$
所以，**三个不同维度的向量(共同构成原空间的基)线性变换成同一维度的三个向量(构成新空间的基)**：

- $1 \ \text{i-hat} \rightarrow w_1 \ \text{i-hat}$
- $1 \ \text{j-hat} \rightarrow w_2 \ \text{i-hat}$
- $1 \ \text{k-hat} \rightarrow -1 \ \text{i-hat}$

三个相同维度的向量，其中只有一个能贡献新的维度，所以它们是**线性相关的**



然后，把原来的数乘（缩放）放进来就得到**真实变换后的向量**：

- $w_1 \ \text{i-hat} \rightarrow w_1 * x_1 \ \text{i-hat}$ 
- $w_2 \ \text{j-hat} \rightarrow w_2 * x_2 \ \text{i-hat}$
- $-1 \ \text{k-hat} \rightarrow -1 * y \ \text{i-hat}$



#### 内积就是线性变换

[一个向量点乘它的微分量等于什么?](https://www.zhihu.com/question/567982061)

##### 变换后的向量等于它在各数轴上（或者说各基向量）的投影向量之和

##### 所有投影向量的和等于本体

所以，

> 就是说，你看到的变换结果是一个**标量**，实际上**它还有一个隐藏的量纲**：i-hat j-hat k-hat 之类的，指出它是属于哪个数轴。
>
> 而且这个标量实际上是若干个分向量的和，这些分向量加起来等于这个标量



# 内积是线性变换，变换的结果是"本体"在数轴上（或者说基向量上）所有投影的和

$$
\begin{align}
(w_1, w_2, -1) \begin{pmatrix} x_1 \\ x_2 \\ y \end{pmatrix} &=
w_1 * x_1 \ \text{i-hat} + w_2 * x_2 \ \text{i-hat} + -1 * y \ \text{i-hat}
\\
&= -b 
\end{align}
$$

## 所有投影(所有到基向量的投影之和等于它自身)都变换到同一个数轴上了，这使得内积的值是一个常量



w 是法向量，-b 的绝对值是平面的截距

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200814095743943.png" alt="image-20200814095743943" style="zoom:50%;" />
$$
w = (0.1, -0.2, -1)^T \\
w' = (0.1, -0.2, 0)^T \\
$$

$$
向量可以看成一个点，也可以看成\textbf{从原点指向这个点的箭头} \\
\\
w' 是w 在x_1x_2 平面上的投影，它决定了平面的朝向(我觉得是决定了平面的斜率？) \\
w_1 \ w_2 绝对值的大小决定了平面的倾斜程度
$$



所有与w 的内积为常数的向量组成一个**垂直于w 的平面**

> 内积是投影乘棍长，内积是常数棍长也是长数(w的模长)，所以**投影也是常数**(准确的说是**投影向量的模长**)
>
> **w 是一个法向量(一根掍)，同时也是一个线性变换**。它将平面上的所有点全部变换成自身的某一点（既棍上的一点）
>
> 投影是线性变换的同义词，投影向量的模长是垂直法向量的平面的截距
>
> - 这个截距就是仿射变换中的常数b



```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

    # 画简头，从p1 指向p2        
def drawArrow(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T  
    arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)

    # 画虚线 p1 [x, y, z] 坐标 p2 [x, y, z] 坐标 
def drawDashe(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T
    ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

    # 画平面 corner4hight: 4 个角的高度
def drawPlane(ax, w, DrawScatter=False):
    x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = w[0] * x1 + w[1] * x2
    print("----->x3:", x3)
    if DrawScatter:
        #ax.scatter(x1, x2, x3, c=[0, 2.7, -2.7,  2.1], cmap='viridis', linewidth=0.5)
        ax.scatter(x1, x2, x3, c=['g', 'r', 'g',  'g'], linewidth=0.5)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

    
# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

w = [1.6, -0.2]
drawArrow([0,0,0], [w[0], w[1], 0], ax)
drawArrow([0,0,0], [w[0], w[1], -1], ax)
drawDashe([w[0], w[1], 0], [w[0], w[1], -1], ax)
#drawPlane(ax, [0,0])                # 四个角高度为0 的平面
drawPlane(ax, w, DrawScatter=True)   # 大概是垂直于法向量的平面？
plt.show()                           # .py 需要, .ipynb 不需要

```

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200814151110692.png" alt="image-20200814151110692" style="zoom:50%;" />


```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D

SQUARE_FIG_SIZE = (10 ,10)
AXIS_LABEL_FONT_SIZE = 16
TEXT_FONT_SIZE = 16
ALPHA = 0.3
LIGHT_ALPHA = 0.1


fig = plt.figure(figsize=np.array(SQUARE_FIG_SIZE) * 2, facecolor='white')

T = "\mathrm{T}"

ax = fig.add_subplot(2, 2, 1, projection="3d")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
 
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
 
    def set_data(self, xs, ys, zs):
        self._verts3d = xs, ys, zs

    # 画简头，从p1 指向p2        
def drawArrow(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T  
    arrow = Arrow3D(pts[0], pts[1], pts[2], arrowstyle="-|>", lw=1,mutation_scale=10,color="black")
    ax.add_artist(arrow)

    # 画虚线 p1 [x, y, z] 坐标 p2 [x, y, z] 坐标 
def drawDashe(p1, p2, ax):
    pts = np.array([ p1, p2 ], np.float).T
    ax.plot((pts[0][0], pts[0][1]), (pts[1][0], pts[1][1]), (pts[2][0], pts[2][1]), "k--", alpha=ALPHA)

    # 画平面 corner4hight: 4 个角的高度
def drawPlane(ax, w, DrawScatter=False):
    x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = w[0] * x1 + w[1] * x2
    print("----->x1:\n", x1)
    print("----->x2:\n", x2)
    print("----->x3:\n", x3)
    if DrawScatter:
        #ax.scatter(x1, x2, x3, c=[0, 2.7, -2.7,  2.1], cmap='viridis', linewidth=0.5)
        ax.scatter(x1, x2, [-2.1, 2.7, -2.7, 2.1], c=['g', 'r', 'g',  'g'], linewidth=0.5)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

    
# ax.set_title(r"$Lorenz\ Attractor$")
ax.set_xlabel(r"$x_1$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_ylabel(r"$x_2$", fontsize=AXIS_LABEL_FONT_SIZE)
ax.set_zlabel(r"$y$", fontsize=AXIS_LABEL_FONT_SIZE)

w = [1.6, -0.2]
"""
W
    [1.6 -0.2 -1]           # 仿射变换中的法向量
x1
    [-1.5  1.5 -1.5  1.5]
x2
    [-1.5 -1.5  1.5  1.5]
x3
    [-2.1 2.7 -2.7 2.1]
         # 这是四个角的高度  2.7 是图中红色那个点的高度
         # c=['g', 'r', 'g',  'g'] 既是画散点时指定了红色 'r' 的那一个
         # 我们的目标是绘制从这个角点到法向量W 的投影
    
    x1, x2, x3 如果构成一个矩阵，矩阵的列向量就是四个角点的坐标
    
"""
drawArrow([0,0,0], [w[0], w[1], 0], ax)
drawArrow([0,0,0], [w[0], w[1], -1], ax)
drawDashe([w[0], w[1], 0], [w[0], w[1], -1], ax)
#drawPlane(ax, [0,0])                # 四个角高度为0 的平面
drawPlane(ax, w, DrawScatter=True)   # 大概是垂直于法向量的平面？
drawDashe([1.5, -1.5, 2.7], [w[0], w[1], -1], ax)  # 红色角点到法向量W 的线段
drawArrow([0,0,0], [1.5, -1.5, 2.7], ax) # 红点向量
plt.show()                           # .py 需要, .ipynb 不需要


```



**法向量穿过平面的那个点刚好是原点，这时平面所有的点(向量)都和w 垂直**

> 如果穿过点不是原点，则平面的点向量就不与w 垂直了。此时平面与w 有截距



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200817090603504.png" alt="image-20200817090603504" style="zoom: 50%;" />

```mathematica
v= {{1.5,-1.5,2.7}}^\[Transpose] ;v//MatrixForm (* 红点向量 *)
w={{1.6,-0.2,-1}};w//MatrixForm  (* 法向量 *)
w.v
--> {{0.}}  (* 内积为零，所以平面和w 是垂直的 *)
```

#### 你点乘别人，你就是变换矩阵，你就是新空间的基

> 参见 math summary.md

#### 你点乘别人是别人向你投影，内积等于你长乘投影长

> 内积为0，棍长不为0，所以**投影长一定是零**




#### 一个矩阵代表一个线性变换，矩阵的列是新空间的基向量

> 如果网格线保持平行且等距分布，并且原点映射为自身，就称它是线性的







## 绘制垂直于法向量的平面，截距是b

```python
    # 画垂直于法向量W 的平面，平面的截距是b（原点到平面与W 的交点）
def drawPlaneVerticalWithW(ax, w, b, DrawScatter=False):
    """
    参见：张觉非《深入理解神经网络》 p.15
    代码：https://gitee.com/neural_network/neural_network_code
    mma： ParametricPlot3D[{x1, x2, 1.6 x1 - 0.2 x2 +1},{x1,-2,2}, {x2,-2,2}]
    """
    x1 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x2 = np.linspace(-1.5, 1.5, endpoint=True, num=2)
    x1, x2 = np.meshgrid(x1, x2)
    x1, x2 = x1.flatten(), x2.flatten()
    x3 = w[0] * x1 + w[1] * x2 + b
    print("----->x1:\n", x1)
    print("----->x2:\n", x2)
    print("----->x3:\n", x3)
    if DrawScatter:
        #ax.scatter(x1, x2, x3, c=[0, 2.7, -2.7,  2.1], cmap='viridis', linewidth=0.5)
        ax.scatter(x1, x2, [-2.1, 2.7, -2.7, 2.1], c=['g', 'r', 'g',  'g'], linewidth=0.5)
    ax.plot_trisurf(x1, x2, x3, antialiased=True, alpha=LIGHT_ALPHA, color="black")

drawPlaneVerticalWithW(ax, w, -1, DrawScatter=False)

```



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200817141114424.png" alt="image-20200817141114424" style="zoom:50%;" />

## affine function



关于$x_1, x_2,\dots,x_n$ 的**仿射函数**(affine function)


$$
a = b + \sum^n_{i=1} w_i x_i
$$

## multilayer perceptron



多层感知机(**MLP**)，也称**多层全连接神经网络**





神经元的能力和极限



## 向量



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210518172728970.png" alt="image-20210518172728970" style="zoom:50%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210519081406409.png" alt="image-20210519081406409" style="zoom:50%;" />




$$
\begin{bmatrix}
3 & 1 \\
2 & 4 \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
1 \\
0 \\
\end{bmatrix}

= 

\begin{bmatrix}
3 \\
2 \\
\end{bmatrix}
$$

- $A$ 将$x$ 轴的单位向量变换到$(3,2)^T$ 

$$
\begin{bmatrix}
3 & 1 \\
2 & 4 \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
0 \\
1 \\
\end{bmatrix}

= 

\begin{bmatrix}
1 \\
4 \\
\end{bmatrix}
$$

- $A$ 将$y$ 轴的单位向量变换到$(1,4)^T$ 


$$
A^{\ } = 
\begin{bmatrix}
3 & 1 \\
2 & 4 \\
\end{bmatrix}

\ \text{（列空间）}

\\

A^T = 
\begin{bmatrix}
3 & 2 \\
1 & 4 \\
\end{bmatrix}

\ \text{（行空间）}
$$

- 列空间和行空间

$$
\begin{bmatrix}
3 & 1 \\
2 & 4 \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
3 \\
1 \\
\end{bmatrix}

= 

\begin{bmatrix}
10 \\
10 \\
\end{bmatrix}
$$

- $A$ 把行空间变换到列空间


$$
\begin{bmatrix}
3 & 2 \\
1 & 4 \\
\end{bmatrix}

\cdot 

\begin{bmatrix}
3 \\
2 \\
\end{bmatrix}

= 

\begin{bmatrix}
13 \\
11 \\
\end{bmatrix}
$$

- $A^T$ 把列空间变换到行空间







### 四个基本子空间

 https://zhuanlan.zhihu.com/p/34056351

GitHub\doc\lang\programming\矩阵的四个子空间及其联系 - 知乎.pdf

- 严格地说, 线性变换一般是指 R^n 到R^n 的线性映射。R^n 到R^m（m≠n）叫线性映射或者线性算子，不叫线性变换。

#### 阶梯形矩阵（或行阶梯型）

> 1. 非零行必在零行之上
> 2. 后一行第一个非零值（按维度从小到大数，既行的左边数到右边。注意，行向量本质是列向量的转置。做转置只是为了适应运算规则而已）所在的维度必大于前一行的第一个非零值  
> 3. 第一个非零值后面所有维度的值必为零
> 4. 梯形阵可以通过高斯消元得到（高斯消元可求出可逆方阵的逆矩阵）



#### 主元

> 梯形阵每一行的第一个非零值既是主元
>
> 主元数目在取值上与矩阵的秩相等（**主元数=秩=维数**）

##### 主元列

> 主元所在的列，也称为**pivot columns**主元所在的列，所有主元列构成空间的一组基
>
> 主元所在的列，对应的系数（被变换的向量的分量就是系数，用来对列做线性组合的），称为**主元变量**（pivot variables），不含主元的列，对应系数称为**自由变量**（free variables）





列空间（column space）

行空间（row space）

- **行空间的维度 = 秩**，也就是说：**列空间维度 = 行空间维度= 秩**

- 虽然行向量有5个元素，看似是在一个5维的空间中，但实际上因为我们的基向量只有两个，它们只能张成一个嵌套在5维空间中的2维子空间。（5维空间的两个点）
- 我们选的基向量实际上是主元所在的行，这样的行称为pivot rows

零（核）空间（nullspace or kernel space）

- AX = 0，所有被A 变换后位于0 点的向量（点）构成零空间

- **零空间的维度 = 列数减列空间维度（n-r）= 没有贡献新维度的列数** 

- 如何求零空间的基向量？（特解）

  1. 消元，把A 变成梯形矩阵
  2. **自由变量**（free variables）尝试在0和1之间自由取值
  3. 得到方程的一组特解，这组特解就是零空间的基向量
- **零空间是列空间的一个子空间**

  

左零空间（left nullspace）
- $A^T X = 0$，所有被$A^T$ 变换后位于0 点的向量（点）构成左零空间
- **左零空间的维度 = 行数减行空间维度（m-r）= 没有贡献新维度的行数**

- **左零空间是行空间的一个子空间**





**向量的分量 = 高维空间的点（向量），在低维空间中的投影（分量，坐标轴上的坐标）**

**（向量内积，一行和一列的内积）影子（投影）是凸透镜和凹透镜，把低维向是量（点）放大或缩小，透镜的倍分是影子的长度**

夹角的余弦是另一只凹透镜，将一行向量缩小$Cos\theta$ 倍，得到投影，而投影又将一列向量放大或缩小。



**向量的内积 = $\|$投影向量 * 被变换向量$\|$（投影后它们的夹解是0）**

> 但是为什么结果是标量？因为夹解的关系？



[投影矩阵与最小二乘法](https://zhuanlan.zhihu.com/p/34208141) D:\GitHub\doc\lang\programming\投影矩阵与最小二乘法 - 知乎.pdf

**最小二乘方法用于求投影矩阵**



https://cloud.tencent.com/developer/article/1402805

https://zhuanlan.zhihu.com/p/37236365



- 其中行空间和零空间彼此*正交*；列空间和*左零空间*彼此*正交*。

  > AX = 0，所有被A 变换后位于0 点的向量（点）构成零空间
  >
  > A 的所有行向量（点，把它作转置变成我们熟悉的列向量）选取线性无关的一组作为基，这些基向量张成行空间（一个向量可以写成行向量也可以写成列向量，这是我们的自由，但是它们都代表同一个点）
  >
  > 正交向量的内积为0
  >
  > 矩阵乘可以看作是A 的每一行与X 的每一列作内积运算，AX = 0 要求所有这样的内积运算结果为0，
  >
  > 所以A 中的每一行必须与X 中的每一列正交





### 矩阵分析 哈工大严质彬

看完Gilbert Strang教授的线性代数后，我推荐可以继续看看国内哈工大严质彬老师的《矩阵分析》(矩阵分析_严质彬_哈尔滨工业大学-超星学术视频 1122)，同样是循序渐进通俗易通。特别是在描叙矩阵本质的时候非常精彩，把握住了思想要领，在回头来看基，相似相合，不变子空间，特征值时又会有更深的认识。视频后面部分用Gram矩阵描述最小二乘问题和李雅普夫稳定性理论的推导证明直观给力！



线代笔记 jupyter

https://github.com/MacroAnalyst/Linear_Algebra_With_Python



### 余弦相似度



直角三角形中，∠A的余弦是它的邻边比三角形的斜边



余弦相似度指的就是夹角的余弦值



```mathematica
(* 正交的两向量内积是0 *)
x ={{0,1}}; x//MatrixForm
y={{1},{0}};y//MatrixForm
x.y
```



```mathematica
(* 两向量的余弦 *)
x = {{1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1}};
y = {{1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1}};
x.Transpose[y] / ( Norm[x] * Norm[y] ) // N
-> {{0.829515}}
```





```python
# 两编语言
# https://blog.csdn.net/tszupup/article/details/107942261
# http://lazycece.com/2019/07/28/%E8%AF%8D%E5%90%91%E9%87%8F%E4%BD%99%E5%BC%A6%E7%AE%97%E6%B3%95%E8%AE%A1%E7%AE%97%E6%96%87%E6%9C%AC%E7%9B%B8%E4%BC%BC%E5%BA%A6/
# https://www.cnblogs.com/abella/p/11170592.html

"""
余弦相似度的假设
https://kexue.fm/archives/8069
最小熵原理（四）：“物以类聚”之从图书馆到词向量
https://kexue.fm/archives/6191
"""


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, paired_distances
 
x = np.array([[1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]])
print(x)
y = np.array([[1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1]])
print(y)
# 余弦相似度
simi = cosine_similarity(x, y)
print('cosine similarity:', simi)
# 余弦距离 = 1 - 余弦相似度
dist = paired_distances(x, y, metric='cosine')
print('cosine distance:', dist)
```







**黑斜体小写字母**表示向量 $\boldsymbol{x}$ 

> $\mathbf{x}$ 黑非斜

斜体小写字母表示标量  $\textit{x}$ 

矩阵表示一组向量 $X$

上标$\textbf{x}^3$ 表示一组向量中的第3 个



### 维数

向量分量的个数称为向量的维数

向量可以表示坐标系上的一个点，也可以看作**从原点指向这个点的一个有长度和方向的“箭头”**

点和箭头都是向量的几何表现形式



### 向量差



其中一个向量取反方向再求和





### 模长



向量的长度是向量与原点之间的欧式距离。 3 维乃至更高维向量的长度也是它们与原点之间的 欧氏距离一一各分量平方和的平方根。 


$$
length(\textbf{x}) = \sqrt{x_{_1}^2 + x_{_2}^2}
$$



向量的模定义为**与自身内积的平方根** ： 
$$
\|\boldsymbol{x}\| = \sqrt{\left < \boldsymbol{x},\boldsymbol{x} \right>} 
= \sqrt{\sum^n_{i=1}\boldsymbol{x}_{_i}^2}
$$
方向不变，长度缩放到1

$$
\frac{\boldsymbol{x}}{\|\boldsymbol{x}\|}
$$

#### 模长和分量的长度成正比



### 范数



距离的定义是一个宽泛的概念，只要满足非负、自反、三角不等式就可以称之为距离。**范数是一种强化了的距离**概念，它在定义上比距离多了一条数乘的运算法则。有时候为了便于理解，我们可以把范数当作距离来理解。

在数学上，范数包括向量范数和矩阵范数，向量范数表征向量空间中向量的大小，矩阵范数表征矩阵引起变化的大小。一种非严密的解释就是，对应向量范数，向量空间中的向量都是有大小的，这个大小如何度量，就是用范数来度量的，不同的范数都可以来度量这个大小，就好比米和尺都可以来度量远近一样；对于矩阵范数，学过线性代数，我们知道，通过运算A X = B AX=BAX=B，可以将向量X变化为B，矩阵范数就是来度量这个变化大小的。





## 数乘



### 数乘是缩放每一个分量

$$
\|k\boldsymbol{x}\| = 
\sqrt{\sum^n_{i=1}(k\boldsymbol{x_{_i}})^2} \\
= 
\sqrt{\sum^n_{i=1}k^2\boldsymbol{x_{_i}}^2} \\
= 
\sqrt{k^2\sum^n_{i=1}\boldsymbol{x_{_i}}^2} \\
= 
k  \sqrt{\sum^n_{i=1}\boldsymbol{x_{_i}}^2} \\
= 
|k| \ \|\boldsymbol{x}\|
$$





## 内积

dot product

> product 是积，积量的积累



# 内积是投影乘棍长

> 棍长不为0, 投影为0, 则内积是0,则**两向量正交**
> 余弦是投影的长度比自已的模长, 90度时余弦是0
> 投影是自已的模长乘余弦

#### 投影是内积比棍长(法向量的模长) 

> 棍子是竹签



### 内积空间

内积空间是数学中的线性代数里的基本概念，是增添了一个额外的结构的向量空间。这个额外的结构叫做内积或标量积。**内积将一对向量与一个标量连接起来**，允许我们严格地谈论向量的“夹角”和“长度”，并进一步谈论**向量的正交性**。内积空间由欧几里得空间抽象而来（内积是点积的抽象），这是泛函分析讨论的课题。

内积空间有时也叫做**准希尔伯特空间**（pre-Hilbert space），因为由内积定义的距离完备化之后就会得到一个希尔伯特空间。



### 三角形三边关系

$$
c^2 = a^2+b^2-2ab \  cos\theta \\
2ab \  cos\theta = 0 \quad \text{when $\theta=\frac{\pi}{2}, cos\theta=0$}
$$
> $cos\theta = \frac{斜边的投影}{斜边}$, 90度的时侯斜边的投影是0

# 余弦是投影的长度比自已的模长



### $\|\boldsymbol{x}\|cos\theta=\frac{\left<\boldsymbol{x},\boldsymbol{y}\right>}{\|\boldsymbol{y}\|}$ 是 $\boldsymbol{x}$向 $\boldsymbol{y}$  的投影的长度

如果$\boldsymbol{x}$和 $\boldsymbol{y}$ 之间的夹角为$\theta$，那么$\|\boldsymbol{x}\|cos\theta$ 是向 $\boldsymbol{x}$向 $\boldsymbol{y}$  的投影的长度。如果 $\boldsymbol{y}$是单位向量，则$\boldsymbol{x}$向 $\boldsymbol{y}$ 的投影的长度就等于 $\left<\boldsymbol{x},\boldsymbol{y}\right>$ 。 



#### 投影到一个单位向量，投影长度就是内积

![image-20200703170620803](深入理解神经网络：从逻辑回归到CNN.assets/image-20200703170620803.png)



所以最好把**法向量**的长度定为1，作为单位向量



# 法向量所有垂线上的点与法向量的内积都相同



#### 想到内积就要想到投影和法向量模长




$$
\left<\boldsymbol{w},\boldsymbol{x}\right> = \|\boldsymbol{w}\| \|\boldsymbol{x}\| cos\theta 
= c
$$
$\|\boldsymbol{x}\|cos\theta=\frac{\left<\boldsymbol{w},\boldsymbol{x}\right>}{\|\boldsymbol{w}\|}\text{（projection $\boldsymbol{x}$ to $\boldsymbol{w}$）}$ 

> 想到内积就要想就投影和法向量模长



#### 法向量是烤肉串的那根棍，肉上的所有点向量在棍上的投影相同

> 投影就是从棍尾到肉块的长度
>
> 内积就是投影乘以棍长



#### 和法向量内积相同的所有点构成一条直线
> 二维点构成直线
>  三维点构成平面
> N维点构成超平面



### 内积定义为各分量的乘积和


$$
\left< x,y \right> = \sum_{i=1}^n x_i y_i
$$

### 内积是模长乘积再乘夹角余弦

$$
\left< x,y \right> = \|\boldsymbol{x}\| \ \|\boldsymbol{y}\| \ cos \theta
$$

> 在更高维的情况下，向量的夹角反过来由这个式子定义



#### 内积是0则向量正交





### 垂线上的点内积都相同



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200703185257579.png" alt="image-20200703185257579" style="zoom: 67%;" />



**2 维空间中与非零向量内积相同的点构成垂直于该向量的直线** 

$$\|\boldsymbol{x_{_a}}\|cos\theta=\frac{\left<\boldsymbol{x_{_a}},\boldsymbol{w}\right>}{\|\boldsymbol{w}\|}$$  and  $$\|\boldsymbol{x_{_b}}\|cos\theta=\frac{\left<\boldsymbol{x_{_b}},\boldsymbol{w}\right>}{\|\boldsymbol{w}\|}$$



**3 维空间中与非零向量内积相同的点构成垂直于该向量的平面** 



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20200706085636145.png" alt="image-20200706085636145" style="zoom:50%;" />







![image-20200703130605379](深入理解神经网络：从逻辑回归到CNN.assets/image-20200703130605379.png)

[【直观详解】线性代数的本质](https://charlesliuyx.github.io/2017/10/06/%E3%80%90%E7%9B%B4%E8%A7%82%E8%AF%A6%E8%A7%A3%E3%80%91%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0%E7%9A%84%E6%9C%AC%E8%B4%A8/)



## 线性独立



线性变换

线性函数满足分配律 $f(x+y)=f(x)+f(y)$

线性函数一定可以表示为两个向量的内积 $f(x)=w^T x$

线性函数一定过原点

线性变换原点不变



如果高维被低维线性表出，则高维是线性相关的。（高维信息有冗余，可以被压缩。它们中有基本粒子的组合）



#### 如果一组向量$v^1,v^2,\dots ,v^s$可以被另一组向量$u^1,u^2,\dots ,u^r$线性表出,并且$r<s$,那么向量组$V$ 是线性相关的





如果**一组向量中的任何一个都不能被组内其他向量线性表出**，则称这组向量是 线性独立的 (lmearmdependent ） 。如果一组向量不是线性独立的，则称它们线性相关。



如果存在非全零$\boldsymbol{w}$ 满足 $\sum^n_{i=1}w^iV^i=0$  则$V$ 是线性相关的

> w是向量，V 是一组向量  $V \cdot \boldsymbol{w}$ = 0



- 关于什么是线性相关，有两种表达

  - 【表达一】你有多个向量，并且可以**移除其中一个而不减小张成的空间**（即2D共线或3D共面），我们称**它们（这些向量）线性相关**

  - 【表达二】其中一个向量，可以**表示为其他向量的线性组合**，因为这个向量已经落在其他向量张成的空间之中

- 如果从统计学角度来说，这些向量之中有**冗余**。这一堆向量中，我们只需要其中几个（取决于维度）就可以表示其他所有的向量



### 仿射函数

仿射函数是线性函数加上一个常量 b 

仿射函数是一类最简单的函数，它的图像在自变量为 1 维的情况下是直线，在自变量为 2 维 的情况下是平面，在更高维情况下是高维超平面。超平面在任意位置的性质都相同，例如 2 维平面任意位置的朝向和倾斜程度都相同。 














从信号处理的角度来说，内积是两个信号的相似性

$$
||x(t)-y(t)||^2=||x(t)||^2+||y(t)||^2-2Re{<x(t),y(t)>}
$$
> 
> 等式左边是两个信号的差别，右边前两项是信号的能量。可见对于能量相同（一般通过能量归一化实现）的若干信号来说，内积越大的两个信号差别越小。



解释物理现象：力的做功，当力的向量和移动距离向量有夹角时，力的功就是力向量与距离向量的点积

> 外积出来的量还是矢量，内积出来的量才是标量。功，是标量，这是内积没错



方便复杂计算： 例如，向量的点积为零，意味着垂直，这在证明垂直问题上有很大作用



引入内积的目的时为了定义内积空间





## 集合



一组集合称为集合$S$ 的**分割**，如果这组集合互不相交且并为$S$ 

$R^2$ 表示实数对的集合





## 香农信息量



熵（英語：entropy）是接收的每条消息中包含的信息的平均量，又被稱為信息熵、信源熵、**平均自信息量**

- 1948年，克劳德·艾尔伍德·**香农將熱力學的熵，引入到信息论**，因此它又被稱為香农熵(Shannon entropy)



熱力学中所谓熵（英語：entropy），是一種測量在動力學方面**不能做功的能量總數**，也就是當總體的熵增加，其做功能力也下降，熵的量度正是能量退化的指標



热力学中，**熵是不能做功的能量总和**

> 熵是热量(Q)除以温度(T)的**商数**
>
> **熵是热量温度比**

熵用于衡量系统的混乱程度



熵是不确定性的测度，对某件事情知道得越多，熵越小

 

熵是**未知平均信息量**（**平均自信息量**）

> 平均信息量是指观察到一个事件发生(接收到一条消息)，平均能获得的信息量

事件的概率分布和每个事件的信息量构成了一个随机变量，这个随机变量的均值（即期望）就是这个**分布产生的信息量的平均值（即熵）**



```python
"""
“熵”不起：从熵、最大熵原理到最大熵模型（二）
https://kexue.fm/archives/3552
"""
# 计算随机变量的信息熵
# lp 是离散随机变量, 概率的列表
def entropy(lp):
    return int( np.sum( list(map(lambda p: -p * np.log2(p), lp)) ) )

assert( entropy([0.5, 0.5]), 1 ) # 一枚均匀的硬币信量量是1 比特
```



比特（bit）竟测量的是什么呢？香农的回答是：用于测量信息的单位。在香农眼里，**信息是和长度、重量这些物理量一样，是一种可以测量和规范的东西**。由于对于通信系统而言，其传递的信息具有随机性，所以定量描述信息应基于随机事件。香农认为，任何信息都存在冗余，冗余的大小与信息中每个符号（数字、字母或者单词）的出现概率或者不确定性相关。

- 信息论的创始人



### 相对熵（KL散度）

在机器学习中，P往往用来表示样本的真实分布，Q用来表示模型所预测的分布，那么KL散度就可以计算两个分布的差异，也就是Loss损失值。

- 从KL散度公式中可以看到Q的分布越接近P（Q分布越拟合P），那么散度值越小，即损失值越小。



### 信息量


$$
log_2(\frac{1}{p(x)}) = - log2(p(x))
$$

> 出现负号是因为对数的性质，$\log_b(a^c) = c \cdot \log_b(a) $, $\frac{1}{p(x)}=p(x)^{-1}$




### 熵(entropy)  是所有事件的概率及其信息量之积的总和


$$
I(X=x^i) = log\frac{1}{p(x^i)} = - log\ p(x^i), \ i = 1,...,k
$$

如果**以2 为底，信息量的单位是比特**(bit)。$I(X=x^i)$ 中的$X=x^i$ 是一条信息，$I$ 是这条信息的**自信息量**(self-information)。$X$ 是信息源。

> 信息量是信息多少的量度
>
> 信息量越大，事件越稀有。你获得了这条信息，相当于得到了一件稀有物品。

> 熵代表随机变量的平均信息量

信息量是单个事件的稀有度（单位比特），熵是所有子事件的平均稀有度（单位比特）

> 这里的稀有度 =  信息量
>
> 这里的平均 = 数学期望（均值）
>
> 这里的熵 = 编码随机变量所需平均比特位个数的下界（所有事件比特位个数的平均）



- 一个事件$x$ 的自信息量的度量是$I(x)$
- 一个随机变量（信息源）的自信息量的度量（熵）是其所有事件自信息量的数学期望（均值）
  - 熵代表随机变量的平均信息量
  - 随机变量$X \sim p(X)$的熵$H(p)$即是编码随机变量$X$ 的最优平均编码长度



为什么要让偏差符合正态分布呢？

- 同分布中心极限定理：n个独立同分布的随机变量之和，服从正态分布。
- 非同分布的李雅普诺夫定理：大量随机因素叠加的结果，近似服从正态分布。

有了这已经证明的两条理论，才可以基于正态分布，得出MSE的标准形式。





信息中的事件发生的概率越小，信息量越大。



信息源$X$ 的**熵(entropy)** 是**所有事件的概率及其自信息量之积的总和**



离散情况
$$
H(X) = \sum^k_{i=1} p(x^i) \ log \frac{1}{p(x^i)} = - \sum^k_{i=1} p(x^i) \ log \ p(x^i)
$$

连续情况
$$
H(X) = - \int^{+\infty}_{\infty} p(x)log(p(x))dx
$$
期望形式
$$
H(X) = E_{x\sim p(x)}[-log(p(x))]
$$


熵可以理解为依据概率分布  $p(x)$ 生成的符号进行编码所需要的最小平均比特数



- 所有事件的集合是一个信息源，可以对它计算一个信息熵，**信息熵描述了发生一个事件，平均可以获得多少信息量**







如昨天下雨这个已知事件，因为**已经发生，既定事实，那么它的信息量就为0**。如明天会下雨这个事件，因为未有发生，那么这个事件的信息量就大。



### 交叉熵

[PyTorch中的CrossEntropyLoss与交叉熵计算不一致](https://kezhi.tech/e295e676.html)

随机变量

- 样本是随机变量$X$（一个骰子）的取值$x$，概率分布 $P$ 给出了随机变量所有取值的概率
  > 随机变量是一颗筛子，随机变量的取值是筛子的点数
  



分布列

- 分布列是随机变量的取值概率函数

- $\scriptsize{X} \sim P(\scriptsize{X})$ 读作随机变量$\scriptsize{X}$ 遵循分布$P$  [u](DeepLearningBook-chinese.pdf) 
  > $\sim$ 读作采样，$P(X)$ 读作随机变量$X$ 的概率分布
  > **采样随机变量$X$ 的概率分布$P(X)$ 得到样本$x$**
  > $p(X=x)$(简写$p(x)$) 表示在特定值 $x$ 处的**密度函数值**



期望

- 变量以一定概率出现不同的取值，函数将给出怎样的均值？
  
> 这个均值不是用算术平均计算的

- 离散随机变量的期望可以通过求和得到：
  > $E_{\scriptsize{X} \sim P}[f(x)] = \sum_x P(x) f(x)$
  > $P$ 是关于随机变量 $X$ 的概率分布, $x$ 是随机变量 $X$ 的某个可能的取值(样本)。$P(x)$ 是样本$x$ 出现的概率。  $E$ 是函数 $f$ 在这个分布下给出的均值，既数学期望。



信息量（也称为自信息）

- 它是一个事件发生时所带来的不确定性的减少量，单位是比特。如果你获得了一比特的信息，那么不确定性(或着说无序性、系统的混乱程度)就减少一比特。
  
  > $I(x) = log_2(\frac{1}{P(x)}) = - log_{2}[P(x)]$  单位比特
  >
  > 出现负号是因为对数的性质，$\log_b(a^c) = c \cdot \log_b(a) $, $\frac{1}{p(x)}=p(x)^{-1}$



信息熵（Entropy）

- 熵是分布产生的信息量的均值
  > 事件的概率分布和每个事件的信息量构成了一个随机变量，这个**随机变量的均值**（即期望）就是这个分布产生的信息量的平均值（即熵）。
  > $ H(X) = E_{\scriptsize{X} \sim P}[I(x)] = \sum_x P(x) I(x) = -\sum_x P(x) log[P(x)]$



交叉熵

- 计算公式和信息熵的形式是一样的，只是原来是两个真 $P$, 后一个真 $P$ 被替换成了近似分布 $Q$ (大模预测出来的分布)

  > $H(X) = -\sum_x P(x) log[Q(x)]$ 

- 最小化交叉熵是一种使模型预测分布 $Q$ 尽可能接近真实分布 $P$ 的方法。



相对熵（KL散度）

在机器学习中，P往往用来表示样本的真实分布，Q用来表示模型所预测的分布，那么KL散度就可以计算两个分布的差异，也就是Loss损失值。

- 从KL散度公式中可以看到Q的分布越接近P（Q分布越拟合P），那么散度值越小，即损失值越小。



```python

# https://github.com/google/flax/issues/2051
# https://editor.mdnice.com/
# see doc\lang\programming\深入理解神经网络：从逻辑回归到CNN.md -> 香农信息量 -> 交叉熵
# https://kezhi.tech/e295e676.html
# https://spaces.ac.cn/archives/6620
    # https://blog.51cto.com/u_14300986/5467002

import jax
from jax import nn
import jax.numpy as np
jnp = np
import jax.random as rand
import numpy as onp
from operator import getitem
import torch
import torch.nn.functional as F
import optax

jax.config.update('jax_platform_name', 'cpu')

key = rand.PRNGKey(42)

x = rand.normal(key, (16, 10))
y = rand.randint(key, (16,), 0, 10) # [0, 10) 的整数, 包含0 不包含 10
    # 下一个 token 的概率分布,  总 token 数为 10
    # x 是预测的概率分布, 16 个 token ，在总数为 10 的 token 字表里每一个 token 的概率值, 所以维度是 (16, 10)
    # y 是真实token, 16 个整数, 代表 16 个 token,  维度是 (16, ) 的一维数组
    # y 后面会被弄成　one hot 的形式，　维度变成　(16, 10), 其中 0 代表这个 token 的概率是　0,  1 代表百分百 

x_ = torch.from_numpy(onp.asarray(x))
y_ = torch.from_numpy(onp.asarray(y)).long()

print(F.cross_entropy(x_, y_, reduction="none").mean().numpy())  #  print(F.cross_entropy(x_, y_).numpy())  PyTorch implementation: 2.888901
    # 16 个预测得到的交叉熵求均值？

tt = y_.view(-1,1) # 最后一维是 1, 前面的一维自适应

loss_1 = -torch.log(F.softmax(x_, dim=-1).gather(1, y_.view(-1,1)))
"""
gather
    在dim维度上，按照indexs所给的坐标选择元素，返回一个和indexs维度相同大小的tensor
    这里indexs必须也是Tensor，并且维度数与input相同（len(input.shape)=len(indexs.shape)）

精髓：不被选择的本就不需要参与计算 例: token 索引为 6 的拿来计算

"""

def cross_entropy_loss_naive(x_, y_):
    x_ = F.softmax(x_, dim=-1) 
        # -1 表示最后一维
        # 最后一维这个数组做一次 softmax, 使得它的所有元素总和为 1, 也就是总概率为 100%
        # 相当于对数据做了一次规范化
    
    n_classes = x_.shape[-1]
    y_ = F.one_hot(y_, n_classes)
        # 现在 x_  y_ 的 shape 一致了
        # y_ 是真实概率分布 P, x_ 是模型预测的概率分布 Q
        # one_hot 中的 0 表示这个token 的概率为0, 1 表示概率 100% 
    
    
    # 现在计算 Q 的信息量
    I_x = -torch.log(x_)
    
    P_x_Q_x = y_ * I_x 
        # P(x) * I(x)
    
    # 沿最后一个维度数组做一次求和，结果就是 16 个交叉熵
    H_P_Q = P_x_Q_x.sum(dim=-1)
    
    H_P_Q_mean = H_P_Q.mean().numpy()
        # 16 个交叉熵的均值
    
    return H_P_Q_mean

print( cross_entropy_loss_naive(x_, y_) )

def cross_entropy_loss(*, logits, labels):
    n_classes = logits.shape[-1]
    loss = optax.softmax_cross_entropy(logits, jax.nn.one_hot(labels, n_classes)).mean()
    return loss
    # one_hot_labels = jax.nn.one_hot(labels, num_classes=10)
    # return -jnp.mean(jnp.sum(one_hot_labels * logits, axis=-1))

print(cross_entropy_loss(logits=x, labels=y))  # Current implementation: -0.0056607425

@jax.jit
def cross_entropy_loss(logits, labels):
    logits = nn.log_softmax(logits)
    loss = jax.vmap(getitem)(logits, labels)
    loss = -loss.mean()
    return loss

print(cross_entropy_loss(x, y))  # Correct implementation: 2.8889012


def cross_entropy_loss_naive_jax(logits, labels):

    n_classes = logits.shape[-1]
    P = jax.nn.one_hot(labels, n_classes)
    
    Q = logits
    Q = jax.nn.softmax(Q, axis=-1) 
        # -1 表示最后一维
        # 最后一维这个数组做一次 softmax, 使得它的所有元素总和为 1, 也就是总概率为 100%
        # 相当于对数据做了一次规范化


    # 现在计算 Q 的信息量
    I_x = -jax.numpy.log(Q)
    
    P_x_Q_x = P * I_x 
        # P(x) * I(x)

    # 沿最后一个维度数组做一次求和，结果就是 16 个交叉熵
    H_P_Q = P_x_Q_x.sum(axis=-1)
    
    H_P_Q_mean = H_P_Q.mean()
        # 16 个交叉熵的均值
    
    return H_P_Q_mean


print( cross_entropy_loss_naive_jax(x, y) )

```







## 概率论



## 独立实验和二项概率  p.37



### 独立试验序列

试验有一系列独立并且相同的小试验组成，称这种试验为独立试验序列。



单次抛掷硬币有两种可能结果：“**正面（H）**”，“**反面（T）**”



多单次抛掷硬币：

**结果**：抛$n$ 次硬币的结果（$2^n$ 种可能，长度为$n$ 的正反序列）

**事件**： 结果里有$k$ 个正面

**结果里有$k$ 个正面这个单个事件的概率为**：$p^k (1-p)^{n-k}$，$p$ = 正面的概率

**样本空间里总共有 $35$ 个这样的事件**（等于3正4反的排列数）

> 样本空间是事件的集合，当你谈论概率的时侯一定要知道样本空间是多少，
>
> 符合条件的事件是多少；前面的$p$ = 正面的概率 是一个先验概率，或着是实验得到的，
>
> 但过程已省略

所以样本空间里符合“结果里有$k$ 个正面” 这个条件的事件的概率是：$\frac{35}{2^n}$ ？（**这样求得的只是占比，并没有考虑到单个事件的概率**）

有点问题？应该这样考虑：**单个事件的概率为是$p^k (1-p)^{n-k}$，总共有$35$ 个这样的事件，**

**所以总概率应该是它的$35$ 倍**，既：$35 * p^k (1-p)^{n-k}$



简单的理解：框里总共有$2^7$个球，其中你想要的球有35个，经过大量的重复实验表明你想要的球它们每一个单独出现的概率都是$p^k (1-p)^{n-k}$，问：现在你从框里面随意抽一个球，抽到那$35$ 个的其中一个的概率是多少？





《程序员的数学2概率统计》平冈和幸 p.82 ：

> 假设硬币正面向上的概率为$p$，抛掷$n=7$ 次后正面向上的个数为$3$ 这个事件的概率是 $P(X=3)$  
>
> > **随机变量$X$ 是事件的集合，$X=3$ 代表一个具体事件**
>
> 样本空间总共$2^7$ 个样本，其中符合$k $ 个正面的样本有 $35$ 个（等于3正4反的排列数）
>
> ```mathematica
> Permutations[{0, 0, 0, 0, 1, 1, 1}]//Length 
> -> 35
> ```
>
>  



> n+1 n+2 ... n+k
>
> n+k n+k-1 ... n+1
>
> (2n+k+1)*k/2













事件$A_i = \{ \ i 次抛掷结果为“正面” \  \}$



每个试验结果（长度为3 的正面和反面的序列）的概率只与序列中的正面出现次数有关。
$$
结果_{k个正面，3-k个反面} 的概率 = p^k (1-p)^{3-k}
$$


#### 在长度为$n$ 的独立伯努立试验序列中，任意一个实验结果有$k$ 个正面这个事件的概率为：$p^k (1-p)^{n-k}$


$$
p^k (1-p)^{n-k} \\
p(k) = \begin{pmatrix} n \\ k \end{pmatrix} p^k (1-p)^{n-k}
$$


$\begin{pmatrix} n \\ k \end{pmatrix}$ 表示 $n$ 次试验中出现$k$ 次正面的结果数



> **结果**：抛三次硬币的结果（8 个可能）
>
> **事件**： 结果里有两个正面" （3个可能）
>
>  [随机变量](https://www.shuxuele.com/data/random-variables.html) X = "结果里正面的个数"：
>
> - P(X = 3) = 1/8
> - P(X = 2) = 3/8
> - P(X = 1) = 3/8
> - P(X = 0) = 1/8



$P(X)$ 就是二项分布，它给出结果中所有可能的正面个数出现的概率  






### 二项分布

- https://leondong1993.github.io/2017/05/binomial-expectation/

  > 二项分布的期望

- https://leondong1993.github.io/2017/05/alibaba-date-problem/

  > 相亲次数问题







**伯努利分布**（Bernoulli Distribution），「只有两种可能，试验结果相互独立且对立」的随机变量通常称为伯努利随机变量。

- 从伯努利分布**采样得到的结果只有两种可能，结果之间互相独立**

**贝塔分布**（Beta Distribution），也称Β分布，是指一组定义在(0,1) 区间的连续概率分布。



二项分布 = 重复N次独立的伯努利试验



$arg \ max$ 的意思是求使后面的值最大的参数 





**The Probability Lifesaver** All the Tools You Need to Understand Chance by Steven J. Miller (z-lib.org).pdf

- 二项定理和二项分布 p.330

随机变量 $X$ 为正面向上的次数，它的均值（期望）是$np$

$$
\begin{align}
\mu \mathbf{x} &= E[X] \\
&= E[X_1 + \cdots + X_n] \\
&= E[X_1] + \cdots + E[X_n] \\
&= p + \cdots + p = np
\end{align}
$$

- ？？





**Gaussian Processes for Machine Learning** (Adaptive Computation and Machine Learning) by Carl Edward Rasmussen, Christopher K. I. Williams (z-lib.org).pdf



```python
np.random.binomial(p=0.5, n=1)
```



### EM 算法

因为log函数是单调递增的，所以求p(x, z)的最大值，即求log(p(x, z))的最大值。[u](http://blog.sciencenet.cn/blog-2970729-1191928.html)



(**讲得最清楚**)**EM算法(期望最大化算法)简介** [u](http://blog.sciencenet.cn/blog-2970729-1191928.html)

- $P(A \cap H) + P(B \cap H) = P(H) ？$ **AB是空间的分割就成立，且不要求H 也在同一空间**
  - **Think Bayes - 我所理解的贝叶斯定理** [u](https://zhuanlan.zhihu.com/p/22467549)
  - **全概率公式**

- 二项系数刚好等于$n$ 选$k$ 的组合数

$$
\begin{pmatrix}
n \\
k
\end{pmatrix}
= C^k_n = \frac{n!}{k!(n-k)!}
$$

**(也很清楚)EM Algorithm 从直观到数学理解** [u](https://hanspond.github.io/2018/09/02/EM%20Algorithm%20%E4%BB%8E%E7%9B%B4%E8%A7%82%E5%88%B0%E6%95%B0%E5%AD%A6%E7%90%86%E8%A7%A3/)

**(提高编)EM算法的九層境界：Hinton和Jordan理解的EM算法** [u](https://www.luoow.com/dc_hk/108333860)





**概率**是特定参数下**结果的可能性**

**似然**是特定结果下**参数的可能性**

- Likelihood



**条件概率 = 后验概率**

**边缘概率 = 先验概率**

**似然函数 = 可能性函数**
$$
P(A|B) = P(A) * \frac{P(B|A)}{P(B)}
$$
$P(A|B)$ 先验概率

$P(A)$ 后验概率

$\frac{P(B|A)}{P(B)}$ 可能性函数(**likelyhood**)

> 可能性函数>1，意味着先验概率被增强，事件A的发生可能性变大；可能性函数=1,意味着B事件无助于判断事件A的可能性；可能性函数<1，意味着先验概率被削弱，事件A的可能性变小





**初识贝叶斯** [u](https://www.jianshu.com/p/b984617c6d3c)





$arg \ max$ 的意思是求使后面的值最大的参数 



**伯努利分布**（Bernoulli Distribution），「只有两种可能，试验结果相互独立且对立」的随机变量通常称为伯努利随机变量。

- 从伯努利分布**采样得到的结果只有两种可能，结果之间互相独立**



**贝塔分布**（Beta Distribution），也称Β分布，是指一组定义在(0,1) 区间的连续概率分布。

> 随机函数被叫做模型，表达模型的方法，和正常的Python方法没有区别
> 模型（model）和变分分布（guide）的参数。【注：**所谓变分就是将原始函数换作另一（易处理的）函数的数学技巧**】
> 最大化证据（evidence）  证据下限”ELBO（evidence lower bound）



### 条件概率



(a) 在连续两次抛掷骰子的试验中，已知两粒骰子的点数的总和为 9 ，第一粒骰子的点数为 6 的可能性有多大？



条件概率是在小样本空间里算概率 概率导论p.17
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

- 分子是同时发生的概率



Think Bayes Bayesian Statistics in Python by Allen B. Downey (z-lib.org).pdf
$$
P(A\ and\ B) = P(A)P(B|A) \\
P(B\ and\ A) = P(B)P(A|B)
$$

- The cookie problem p.3

  > 贝叶斯定理把两个对立的条件概率联系起来了 $P(A|B)和P(B|A)$
  >
  > - **贝叶斯定理通过上面那两个等式导出**







### 随机变量



样本是随机变量$X$（一个骰子）的取值$x$，概率分布 $P$ 给出了随机变量所有取值的概率



随机变量是一颗筛子，随机变量的取值是筛子的点数

$\scriptsize{X} \sim P(\scriptsize{X})$ 读作随机变量$\scriptsize{X}$ 遵循分布 [u](DeepLearningBook-chinese.pdf) 

> $\sim$ 读作采样，$P(X)$ 读作随机变量$X$ 的概率分布
>
> **采样随机变量$X$ 的概率分布$P(X)$ 得到$x$**

$p(X=x)$(简写$p(x)$) 表示在特定值 $x$ 处的**密度函数值**

- **变分贝叶斯初探** [u](https://www.jianshu.com/p/86c5d1e1ef93)



连续随机变量$X$ 有 **概率密度函数**（probability density function, PDF）有时简称为**密度**函数
$$
f\scriptsize{X}(x)
$$


离散随机变量$X$ 有**概率质量函数**（probability mass function, PMF），有时简称为**分布律**函数
$$
p\scriptsize{X}(x)
$$


**联合概率分布**（joint probability distribution）
$$
P(\scriptsize{X} = x, \scriptsize{Y}=y) \\
P(x, y)
$$
表示 $x,y$ 同时发生的概率



观察到随机变量中的一个事件相当于**收到了一条消息** [u](p.30)



### 分布列 [u](概率导论,2ed,Dimitri Bertsekas,John N图灵图书中文版.pdf)

分布列是**随机变量的取值概率**
$$
p\scriptsize{X}(x) = p(\{X=x\})
$$
<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20201118181329071.png" alt="image-20201118181329071" style="zoom:50%;" />



用记号 $P_\theta(A)$ 表示一个事件的概率。注意$P_\theta(A)$ **对于$\theta$ 的依赖性仅仅是函数上的依赖性**，**而不是**像贝叶斯分析中那样， $\theta$ 的出现意味着相应的概率是**条件概率** ·



### 期望



- **变量以一定概率出现不同的取值，函数将给出怎样的均值**？

  > 这个均值不是算术平均，从计算方法上看可以认为是**概率平均**？



函数$f(x)$ 关于某分布$P(\scriptsize{X})$ 的期望(expectation) 是指，当$x$ 由$P$ 产生时，$f$ 作用于$x$ 的平均值。



离散随机变量的期望可以通过求和得到：


$$
E_{\scriptsize{X} \sim P}[f(x)] = \sum_x P(x) f(x)
$$
连续随机变量的期望可以通过积分得到：


$$
E_{\scriptsize{X} \sim P}[f(x)] = \int P(x) f(x) dx
$$










设随机变量$X$ 的分布列为 $p\scriptsize{X}$. $X$ 的**期望值 （ 也称期望或均值 ）** 由下式给出
$$
E[X] = \sum_x x \ p\scriptsize{X}(x)
$$



信息源$X$ 的**熵(entropy)** 是**所有事件的概率及其信息量之积的总和**



$$
H(p) = \sum^k_{i=1} p(x^i) \ log \frac{1}{p(x^i)} = - \sum^k_{i=1} p(x^i) \ log \ p(x^i)
$$





### 方差



方差（variance）衡量的是当我们对$x$ 依据它的概率分布**进行采样时**，随机变量$x$ 的函数值**会呈现多大的差异**：


$$
Var(f(x)) = E [( f(x) - E[f(x)] )^2]
$$



**方差是期望离散度**
$$
var(X) = E[(X - E[X])^2] \\
var(X) = \sum_{x} (X - E[X])^2 p\scriptsize{X}(x)
$$

- 方差非负，提供了$X$ 在期望周围分散程度的一个测度





K-L 散度可以用来衡量两个分布之间的差异程度



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210508164935854.png" alt="image-20210508164935854" style="zoom:50%;" />

[方差的计算](https://zh.wikihow.com/%E8%AE%A1%E7%AE%97%E6%A0%87%E5%87%86%E5%B7%AE)

1. 求平均数

2. 求方差 （方差是数据偏离平均数的程度）

   > 每一项都减去平均数，然后全部求平方，再然后全部加起来，最后除以总个数（或者总个数 - 1）

3. 求标准差

   > 方差开平方既可

 



### 正态分布


$$
N(\mu, \sigma^2)
$$
期望为$\mu$，方差为$\sigma^2$



#### 独立同分布(iid)

- independent and identically distributed (**i.i.d**.)

随机变量**具有相同的概率分布，并且互相独立**

> 概率论里是这样的概念：X1,X2,…,Xn是独立同分布的n个随机变量，当n很大时，它们的和X=X1+X2+…+Xn可以近似看作服从正态分布的。
> **中心极限定理**就是说的这个概念，定理证明了X的标准化以后的随机变量，当n→∞时趋向于标准正态分布。实际应用时，n应该至少等于几十才不至于有太大的误差。
> 独立同分布independent and identically distributed (i.i.d.)
>
> 　　在概率统计理论中，如果变量序列或者其他随机变量有相同的概率分布，并且互相独立，那么这些随机变量是独立同分布。(independent and identically distributed )
>
> 　　随机变量X1和X2独立,是指X1的取值不影响X2的取值,X2的取值也不影响X1的取值.随机变量X1和X2同分布,意味着X1和X2具有相同的分布形状和相同的分布参数,对离散随机变量具有相同的分布律,对连续随机变量具有相同的概率密度函数,有着相同的分布函数,相同的期望、方差。反之，若随机变量X1和X2是同类型分布，且分布参数完全相同，则X1和X2完全一定同分布！
>
> 　　英文资料中写成i.i.d，iid或者IID。
>
> 　　如实验条件保持不变，一系列的抛硬币的正反面结果是独立同分布







### 后验概率
#### 后验概率 = 条件概率


$$
p(X=x|Y=y) = \frac{p(Y=y|X=x) \ p(X=x)}{p(Y=y)}
$$
后验概率是观察到一个事件$Y=y$ 后，另一个事件的$X=x$ 的概率





一个简单的办法：
chrome打开知乎页面，按顺序 F12 - F1 - 在General 里面点选 Disable JavaScript。就可以复制了。





## 经典参数估计 [u](概率导论p.391)



### 最大化似然 = 最小化交叉熵



**最大似然函数**
$$
\sum_{x,y} \tilde{p}(x,y) log\ p(x,y;\theta)
$$
**交叉熵函数**
$$
- \sum_{x,y} \tilde{p}(x,y) log\ p(x,y;\theta)
$$

> 两个的函数图像关于$X$ 轴对称，最大最小值正好反过来了





### 联合概率导出似然函数，似然函数导出对数似然函数(为了求导方便)



**人人都懂EM算法** [u](https://zhuanlan.zhihu.com/p/36331115)

> 概率统计的思想，根据样本估算总体
>
> 正态分布(normal distribution) = 高斯分布(Gaussian distribution)



样本集 $X = x_1, x_2, \cdots, x_N$ 表示200 个人的身高

- 假设学校**所有学生的身高服从正态分布** $N(μ, \sigma^2)$
- 期望$μ$，方差$\sigma^2$ 未知
- 目标是：**从样本估算出未知的期望和方差**



**概率密度$p(x|\theta)$ 服从高斯分布$N(μ, \sigma^2)$** 

- 未知参数是 $\theta = [\mu, \sigma]^T$
- **目标是：估算 $\theta$**

每个样本都是独立地从$p(x|\theta)$中抽取的



**正好抽到这特定的 200 个身高的概率是一个联合概率**
$$
L(\theta) = L(x_1, x_2, \cdots , x_n; \theta) = \prod^n_{i=1} p(x_i|\theta), \theta \in \Theta
$$
**当概率密度函数的参数是$\theta$ 时，得到$X$ 这组样本的概率是$L(\theta)$**



**联合概率$L(\theta)$ 表示**在不同参数$\theta$ 取值下，**正好抽到$X $ 这组样本的概率**



**联合概率$L(\theta)$** **又称为**参数$\theta$ 相对于样本集$X$ 的**似然函数**(likehood function)



为了求导方便，**对似然函数取对数**，使连乘变成连加，**就得到对数似然函数**：
$$
H(\theta) = \ln L(\theta) = \ln \prod^n_{i=1} p(x_i|\theta) = \sum^n_{i=1} p(x_i|\theta)
$$

**什么样的参数能使联合概率出现最大值？这就是最大似然要研究的问题。既我们观察(或抽样)到这一组结果，使它出现的可能性(概率)最大的模型(公式)参数(未知量;隐变量)是什么？**



#### 最大似然估计量 $\hat{\theta}$ 

$$
\hat{\theta} = arg max\ L(\theta)
$$

- arg 表示参数
- max 表示似然函数得到极大值

> **表示使似然函数得到极大值的参数**





**求极大似然函数估计值的一般步骤**

1. 写出似然函数
2. 对似然函数取对数，并整理
3. 求导数，令导数为 0，得到似然方程
4. 解似然方程，得到的参数









**梯度下降和EM算法：系出同源，一脉相承** [u](https://kexue.fm/archives/4277/comment-page-1)

> EM算法，也就是**最大期望算法**，一般**用于**复杂的**最大似然问题的求解**。
>
> **求最大似然函数的最大值，等价于求交叉熵的最小值**。

**从最大似然到EM算法：一致的理解方式** [u](https://kexue.fm/archives/5239)



**EM 用于含有未知变量的概率模型的极大似然估计，或者说是极大后验概率估计**

> 只要有一些训练数据，再定义一个最大化函数，采用**EM算法**，利用计算机经过若干次迭代，就可以得到所要的模型。这实在是太美妙了，这也许是我们的造物主刻意安排的。所以我把它称作为**上帝的算法**。——吴军



**K-means与EM其实是有关联的**或者说k-means算法也是EM算法思想的一种体现



**交叉熵函数**
$$
S = - \sum_{x,y} \tilde{p}(x,y) log\ p(x,y;\theta)
$$

$$
\tilde{p}(x,y) = \frac{\#(x,y)}{N}
$$

> $\#(x,y)$ 是共现次数，$\tilde{p}(x,y)$ 是共现概率





经典的方法就是将参数$\theta$ 看作未知常数，而不是随机变量。

**最大似然估计量**，它**可以看作是**经典统计中与**贝叶斯最大后验概率估计量相对应**的部分

>  这是一种**适用范围较广的估计方法**，与贝叶斯推断中的**最大后验概率估计有很多相似之处**



**置信区间**：一个有很大概率包含未知参数的区间 

最后关注简单但是重要的**估计未知均值**的例子，如果可能的话**估计未知的方差**

> 这里用到的很重要的方法是**大数定律和中心极限定理**



**概率（probabilty）和统计（statistics）研究的问题刚好相反**

- **概率是已经方程和参数，求结果**
- **统计是已知结果，求方程和参数**



对于概率看法不同的两大派别频率学派与贝叶斯派。他们看待世界的视角不同，导致他们对于产生数据的模型参数的理解也不同

**频率学派**

- **他们认为世界是确定的**。他们直接为事件本身建模，也就是说事件在多次重复实验中趋于一个稳定的值p，那么这个值就是该事件的概率

- **极大似然估计（MLE）**

  - 最大化可能性

    > **已知输入数据是方程的结果，求方程最有可能的参数**



**贝叶斯派**

- **他们认为世界是不确定的**，因获取的信息不同而异。假设对世界先有一个预先的估计，然后通过获取的信息来不断调整之前的预估计。 他们不试图对事件本身进行建模，而是从旁观者的角度来说。因此对于同一个事件，不同的人掌握的先验不同的话，那么他们所认为的事件状态也会不同。

- **最大后验概率估计（MAP）**



**详解最大似然估计（MLE）、最大后验概率估计（MAP），以及贝叶斯公式的理解** [u](https://blog.csdn.net/u011508640/article/details/72815981)





### 估计量



$\hat{\Theta}_{n}$ 是未知参数 $\theta$ 的一个**估计量**，**是**关于$n$ 个的**观测** $X_1, \cdots，X_n $ 的一个函数（服从依赖参数$\theta$ 的分布）



- 估计误差
  $$
  \tilde{\Theta}_{n} = \hat{\Theta}_{n} - \theta
  $$

- 估计量的偏差
  $$
  b_{\theta}(\hat{\Theta}_{n}) = E_{\theta}[\hat{\Theta}_{n}] - \theta
  $$
  
- **均方误差**

$$
E_{\theta}[\tilde{\Theta}^2_{n}] = b^2_{\theta}(\hat{\Theta}_{n}) + \scriptsize{V}ar_{\theta}(\hat{\Theta}_{n})
$$

  > 这个公式很重要，**方差的减少总是伴随着偏差的增大**
  >
  > 一个好的估计量会让两项的取值都比较小





### 极大似然和极大期望



**参数估计**

- **最大似然估计和线性回归方法**



**最大似然估计** ： 选择参数使得**被观测到的数据“最有可能 ' 出现**





**极大似然** MLE (maximum likelihood estimation)，**极大期望** EM(Expectation Maximization)

> **必须假设数据总体的分布**，否则不能使用
>
> 利用已知的样本结果，去反推最有可能（最大概率）导致这样结果的参数值
>
> EM算法是**一种迭代算法**，用于含有隐变量的概率模型的极大似然估计，或者说是**极大后验概率估计**
>
> EM 分为两步：Expection-Step 和 Maximization-Step。E-Step 主要通过观察数据和现有模型来估计参数，然后用这个估计的参数值来计算似然函数的期望值；而 M-Step 是寻找似然函数最大化时对应的参数。由于算法会保证在每次迭代之后似然函数都会增加，所以函数最终会收敛
>
> - **EM 是梯度上升算法，最大化似然函数**



极大似然和EM算法更加抽象，与其说是一种算法，不如说是一种解决问题的思想，解决一类问题的框架



### EM算法

- https://blog.sciencenet.cn/blog-2970729-1191928.html

  > EM算法(期望最大化算法)简介



A、B 两枚硬币，假设它们抛出正面向上的真实概率分别为$\theta_A$ 和$\theta_B$ ，写成向量形式为：

$$
\theta = (\theta_A, \theta_B)
$$

总共进行五次实验，其中第$i$ 次实验过程为：以50% 的概率随机从硬币A、B中挑一个，挑选的结果记为$z_i$，$z_i \in \{A, B\}$然后用它抛5 次，出现正面的次数记为$x_i$ ，$x_i \in \{ 0,1,\cdots, 5\}$ 



五次实验结果写成向量形式为：
$$
z = (z_1,z_2,z_3,z_4,z_5) \\
x = (x_1,x_2,x_3,x_4,x_5)
$$

可以近似的认为在整个实验中（五次实验一起）：
$$
\theta_A = \frac{A硬币出现正面次数}{A硬币抛掷总次数}
$$


得出$\theta_A$ 的方法就叫做**极大似然估计**(Maximum likelihood estimation)



现在假设，$z$ 是未知的，目标还是要算出$\theta_A$，这就是**EM算法** 要解决的问题





**在长度为$n$ 的独立伯努立试验序列中，任何实验结果为$k$ 次正面的概率为：**$p^k (1-p)^{n-k}$

$$
p(k) = \begin{pmatrix} n \\ k \end{pmatrix} p^k (1-p)^{n-k}
$$


$\begin{pmatrix} n \\ k \end{pmatrix}$ 表示 $n$ 次试验中出现$k$ 次正面的结果数



结果A出现0次、1次、……、10次的概率各是多少呢？这样的概率分布呈现出什么特征呢？这就是二项分布所研究的内容



> **结果**：抛三次硬币的结果（8 个可能）
>
> **事件**： 结果里有"两个正面" （3个可能）
>
>  [随机变量](https://www.shuxuele.com/data/random-variables.html) X = "结果里正面的个数"：
>
> - P(X = 3) = 1/8
> - P(X = 2) = 3/8
> - P(X = 1) = 3/8
> - P(X = 0) = 1/8



$P(X)$ 就是二项分布，它给出结果中所有可能的正面个数出现的概率  





## 三角函数

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210618114742424.png" alt="image-20210618114742424" style="zoom:50%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210618114812409.png" alt="image-20210618114812409" style="zoom:50%;" />



## 数值积分



**高斯求积简介** [u](https://discourse.juliacn.com/t/topic/1024) [u2](GitHub\doc\lang\programming\高斯求积简介.pdf)

**Gauss quadrature nodes and weights** [u](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/23972/versions/22/previews/chebfun/examples/quad/html/GaussQuad.html)

```matlab
% Golub-Welsch algorithm
% The classical method for computing the Gauss nodes and weights is the Golub-Welsch algorithm [2], which reduces the problem to a symmetric tridiagonal eigenvalue problem. We refrain from deriving this relation, but give a small snippet of the code (borrowed from [3, p. 129]).

n = 5; format short

    beta = .5./sqrt(1-(2*(1:n-1)).^(-2)); % 3-term recurrence coeffs
    T = diag(beta,1) + diag(beta,-1)      % Jacobi matrix
    [V,D] = eig(T);                       % Eigenvalue decomposition
    x = diag(D); [x,i] = sort(x);         % Legendre points
    w = 2*V(1,i).^2;                      % Quadrature weights
```





函数$f(x)$ 的积分可以用n 个矩形的面积来逼近，一般会在函数上等间距采 n个点的值 $f(x_1),f(x_2),\cdots,f(x_n)$，然后分别乘以间隔（权重）得到面积，再累加求和得到积分

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210107110026248.png" alt="image-20210107110026248" style="zoom:50%;" />

- node 是函数值$f(x_i)$ ，是小矩形的长
- weight 是小矩形的宽

$$
\int^{1}_{-1} f(x)dx \approx  w_1 f(x_1) + w_2 f(x_2) 
+ w_3 f(x_3) + w_4 f(x_4)
$$

> 随机选4 个点对$f(x)$ 都成立

目标是用**n 个点可以完美积分n-1 阶多项式**。可以分别令$f(x)$ 为张成多项式空间的一组基$(1,x,x^2,x^3)$
$$
\begin{array}{c}
2=\int_{-1}^{1} 1 d x \approx w_{1}+w_{2}+w_{3}+w_{4} \\
0=\int_{-1}^{1} x d x \approx w_{1} x_{1}+w_{2} x_{2}+w_{3} x_{3}+w_{4} x_{4} \\
\frac{2}{3}=\int_{-1}^{1} x^{2} d x \approx w_{1} x_{1}^{2}+w_{2} x_{2}^{2}+w_{3} x_{3}^{2}+w_{4} x_{4}^{2} \\
0=\int_{-1}^{1} x^{3} d x \approx w_{1} x_{1}^{3}+w_{2} x_{2}^{3}+w_{3} x_{3}^{3}+w_{4} x_{4}^{3}
\end{array}
$$
这样就得到了一个线性方程组，4 个方程 4个权重未知数，正好可以解出。如果我们选择$x_i$在$[-1,1]$上均匀分布，那么这就是牛顿-柯特斯积分。



```python
>pip3 install pycall # for julia to using sympy package

from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y

print( integrate(sin(x)/x,(x,-float("inf"),float("inf"))) ) # 积分结果是pi
print( integrate(1+15*x+2*x**2+12*x**3,(x,float(-1),float(1))) ) # 3.333
```



```julia
# 全程开全局代理 Proxifier
julia>import Pkg; Pkg.add("SymPy")
julia>using SymPy
julia>sympy.sqrt(3)

# vscode
using SymPy
x = symbols("x")
println( integrate(sin(x)/x, (x, -oo, oo)) )
println( integrate(1+15*x+2*x^2+12*x^3, (x, -1.0, 1.0)) )

```





SymTridiagonal  对称三对角矩阵



@. 的作用是同时向量向化函数调用和赋值

```
f(x) to f.(x)
+= to .+=
```



https://www.zhihu.com/column/p/22141637

同时，我们可以通过求解一个三对角对称矩阵的本征值和本征向量来得到所需的零点位置和积分权值（这可以通过QR分解来快速精确求解），事实上这就是实际计算中所采用的办法。

上面的Golub-Welsch算法里得到点和权重的方法就是利用Jacobi矩阵的特征多项式的三项递归特性。



定义内积和系统问题本身其实关系极大，而内积也不一定要这么定义，例如在Hermite多项式中，其内积就加上一个权重函数：
$$
<H_M,H_n> = \int^{\infty}_{-\infty} dx \cdot H_m(x)H_n(x) e^{-x^2}
$$

这种连续函数的内积的定义，我是这样看的：每一个函数都是一个矢量，而矢量中每一值是在不同的x的值，即
$$
f(x) = [f(x_0),f(x_1),f(x_2)]^T
$$


内积就是两普通矢量的内积，即

把这转成积分，加上权重，就成了一般所见的函数的内积定义。



![image-20210115145527050](深入理解神经网络：从逻辑回归到CNN.assets/image-20210115145527050.png)

![image-20210115145540640](深入理解神经网络：从逻辑回归到CNN.assets/image-20210115145540640.png)





**政治大學 數值分析Numerical Analysis** [u](http://moocs.nccu.edu.tw/course/132/intro)
$$
\int^b_a f(x)dx = \sum^n_{i=0} w_i f(x_i) \\
for f \in \mathbb{P}_{2n+1}
$$

- $f$ 的阶数是$2n+1$ 时左右相等，而不是近似



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210108084947579.png" alt="image-20210108084947579" style="zoom: 33%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210108090152548.png" alt="image-20210108090152548" style="zoom: 50%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210108100114400.png" alt="image-20210108100114400" style="zoom:50%;" />



勒让德多项式





数值积分和高斯点简介 [u](https://cn.comsol.com/blogs/introduction-to-numerical-integration-and-gauss-points/)

数值积分也称为*数值求积*，其本质是**用求和代替积分**，其中**被积函数在多个离散点被采样**



其中 $x_i$ 是积分点的位置，$w_i$ 是相应的权重因子。积分点通常称为高斯点，但是严格来说，这种命名法仅适用于高斯求积 法定义的积分点。



在高斯求积算法中，需要选择积分点的位置及其权重，以便精确地对阶次尽可能高的多项式进行积分。由于 N 次多项式包含 N + 1 个系数，而具有 M 个点的高斯点规则包含 2M 个参数（位置+权重），因此可以精确积分的多项式的最高阶次是 N = 2M-1。

高斯求积对于可由一定程度的多项式很好地进行近似的积分场非常有效





### Gauss–Hermite积分 [u](https://zhuanlan.zhihu.com/p/29887184)


$$
\int e^{-x^2} f(x)dx \approx \sum w_i f(x_i)
$$
假设$\theta$ 服从正态分布 $\theta \sim N(0,1)$，于是有：
$$
\sum \frac{w_i}{\sqrt\pi}f(\sqrt2 x_i)
$$

```python
class Irt2PL(BaseIrt):
    ''
    @staticmethod
    def get_gh_point(gp_size):
        x_nodes, x_weights = np.polynomial.hermite.hermgauss(gp_size)
        x_nodes = x_nodes * 2 ** 0.5
        x_nodes.shape = x_nodes.shape[0], 1
        x_weights = x_weights / np.pi ** 0.5
        x_weights.shape = x_weights.shape[0], 1
        return x_nodes, x_weights
```





MLE, MAP and Bayesian Inference [u](https://towardsdatascience.com/mle-map-and-bayesian-inference-3407b2d6d4d9)

A Gentle Introduction to Maximum Likelihood Estimation and Maximum A Posteriori Estimation [u](https://towardsdatascience.com/a-gentle-introduction-to-maximum-likelihood-estimation-and-maximum-a-posteriori-estimation-d7c318f9d22d)



在统计计算中经常需要计算积分。比如，从密度$p(x)$**计算分布函数**$F(x)$，如果**没有解析表达式**和精确的计算公式， **需要用积分来计算**



从联合密度**计算边缘密度**， 要用积分计算



贝叶斯分析中从先验密度$\pi(\theta)$ 和似然函数$p(x|\theta)$，**计算后验密度**
$$
p(\theta|x) = \frac{p(\theta,x)}{p(x)} = \frac{\pi(\theta)p(x|\theta)}{\int \pi(u)p(x|u)du}
$$

 不能得到后验密度 $p(\theta|x)$ 的解析表达式时，需要计算积分，**用后验密度求期望、平均损失函数**也需要计算积分



## 数论



[中英字幕] 科普：**费马大定理的证明** | 椭圆曲线与模形式 [u](https://www.bilibili.com/video/BV1ut4y1C7Z1?t=41)

- **sage 库**,python

**vscode+jupyternotebook+sagemath配置** [u]()





## 雅可比矩阵



[雅可比矩阵和雅可比行列式](https://zhuanlan.zhihu.com/p/39762178)

[The Jacobian matrix Video](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/jacobian/v/the-jacobian-matrix)





## TextRank



```python

import math
import numpy as np

"""
功能：文本摘要算法实现(TextRank for Text Summarization)
TextRank 从PageRank 发展而来，PageRank 是计算网站重要性的算法，这里将用一个通俗的比喻来解释它的含义： 极简“个人价值模型” 
	在这个模型里面，PageRank 是说：个人价值与自身努力无关，也不靠拼爹，完全由你的朋友数量决定。朋友越多你的价值越高，
		价值计算过程很简单，假设你有N 个朋友，那么你要把自身价值均分给你的每一个朋友，既你的每一个朋友都得到你个人价值的 1/N，并且所有人都要这么做，均分自已的价值，所以这是一个循环计算的过程。
		细节：
			1. 所有人的价值都初始化为0.15
			2. 每个人都有一个基础价值0.15，如果一个人完全没有朋友，那么他的价值就是0.15
			3. 所有均分出去的价值都要抽税，既对方能得到的值是：  0.85 * 1/N * 你的价值
			4. 所以你对你的每一个朋友的贡献值都是： 0.85 * 1/N * 你的价值
			5. 你的价值等于所有朋友对你的贡献总和再加上基础价值0.15
			6. 循环计算所有人的价值，经过若干次计算以后结果会收敛到稳定值
	
	TextRank 是说：朋友里面也还分好朋友和一般的朋友，关系好的就要多分一点。 
		对应文本摘要算法，“关系好”就是句子之间的相似度高，把相似度作为边的权重
		TextRank 和PangeRank 的唯一差别就在那个 1/N 上面，TextRank 用某种方法替换了 1/N,
			1/N 的替换方法是： 你和某个朋友的相似度  /  你和所有朋友之间的相似度总和 
		细节：
			替换了那个1/N 以后，所有计算过程和PageRank 相同
"""

# 相似度计算公式参见原始论文：《TextRank: Bringing Order into Texts》by: Rada Mihalcea and Paul Tarau
# https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf

def similarOfSents(words1, words2):
	"""
	words1:句子1的词list
	words2:句子2的词list
	"""
	intersects = [] # 两个词集合words1，words2 的交集
	for w in words1:
		if w in words2:
			if w not in intersects:
				intersects.append(w)
	numerator = len(intersects)  # 分子是交集的元素个数
	if numerator == 0:
		return 0.0
	denominator = math.log(len(words1)) + math.log(len(words2))  # 分母是句子对应的词集长度分别求对数，然后相加
	if denominator < 1e-12:
		return 0.0

	return numerator / denominator

# 构造相似度邻接矩阵
# wordsList: 句子词向量列表 example: [ ['a', 'b', 'c'], ['a', 'b', 'f'], ['a', 'h', 'i'] ]
def similarMatrix(wordsList):
	n = len(wordsList)
	adjacentMatrix = np.zeros((n, n))
	"""
	邻接矩阵，里面存的是相似度，相似度可以用作graph 边的权值
	"""
	for i in range(0, n):
		for j in range(i+1, n):
			sim = similarOfSents(wordsList[i], wordsList[j])
			adjacentMatrix[i, j] = sim
			adjacentMatrix[j, i] = sim
	return adjacentMatrix


# 构造权值邻接矩阵
# simMatrix: 相似度邻接矩阵
def weightMatrix(simMatrix):
	"""
	graph 是一个有向图，结点是句子， \
		边的意义是两句子相似，箭头指向的意义是价值传递的方向，  \
		权值的意义是你愿意把自已价值的百分之几传递给箭头指向的那个结点。 \
		计算A -> B 的权值的方法是：  \
			先算A 和所有结点相似度的总和，这是分母  \
			再算A 和B 的相似度，这是分子  \
			两者的比值既是A -> B的边的权值
		注意：严格说来，这里的相似度才是论文中所指的权重， \
			而这里的权值实际上是论文公式后半段带小求和的分子除以分母的部分，  \
			但考虑到权值的意义这么定义更清晰，所以是值得的
	"""
	n = len(simMatrix)
	weightMtrx = np.zeros((n, n))
	
	for i in range(0, n):
		sumsim = sum( simMatrix[i] )  # 句子i 和其他所有结点相似度的总和
		for j in range(0, n):
			if i != j and simMatrix[i][j] > 0.001 and sumsim > 1e-12:  # 相似度小于一定值，认为结点之间没有边
				weightMtrx[i][j] = simMatrix[i][j] / sumsim
	
	return weightMtrx			

# 计算句子textrank 值(价值，或者说“重要性”)
# wordsList: 句子词向量列表 example: [ ['a', 'b', 'c'], ['a', 'b', 'f'], ['a', 'h', 'i'] ]
def textrank2(wordsList):
	"""
	这个版本的实现是networkx 库的实现，和Matlab 中内置的算法实现结果是一至的，  \
		但是和论文公式的计算过程有差异，严格按照论文的实现在textSummarization 函数
	"""
	N = len(wordsList)

	simMatrix = similarMatrix(wordsList) # 相似度邻接矩阵
	print("similary matrix:\n ", simMatrix, "\n\n")

	W = weightMatrix(simMatrix)  # 权值邻接矩阵
	print("weight matrix:\n ", W, "\n\n")

	WS = np.full(N, 1/N) # TextRank 初始值  list ，1*N 维，初值1/N
	for _ in range(0, 100):
		WS_last = WS
		WS = [0, 0, 0]
		for i in range(0, N):
			for j in range(0, N):
				if i != j and W[i][j] > 0:
					WS[j] += 0.85 * WS_last[i] * W[i][j]  # 先算i 为别人做了多少贡献
			WS[i] += 0.15 * 1 / N  # 再算别人为i 做了多少贡献
	
	print ("textrank值：\n", WS, "\n", sum(WS))
	return WS

"""
# 严格按照论文公式计算
# 计算句子textrank 值(价值，或者说“重要性”)
# wordsList: 句子词向量列表 example: [ ['a', 'b', 'c'], ['a', 'b', 'f'], ['a', 'h', 'i'] ]
# MaxIter 最大迭代次数, 默认值100
"""
def textSummarization(wordsList, MaxIter = 200):

	N = len(wordsList)

	simMatrix = similarMatrix(wordsList) # 相似度邻接矩阵
	#print("similary matrix:\n ", simMatrix, "\n\n")

	W = weightMatrix(simMatrix)  # 权值邻接矩阵
	#print("weight matrix:\n ", W, "\n\n")

	WS = np.full(N, 0.15) # TextRank 初始值  list ，1*N 维，初值0.15
	
	for k in range(MaxIter):
		last_WS = WS.copy()
		for i in range(0, N):
			s = 0 # 其他结点给句子i 的贡献总和
			for j in range(0, N):
				if i != j and W[i][j] > 0:
					s += W[j][i] * WS[j]  # 句子j 的价值是WS[j]，把自已的价值按百分比贡献给句子i，这个比值是边的权值 W[j][i] (j -> i)
			WS[i] = 0.15 + 0.85 * s
		
		if sum( WS - last_WS ) < 1e-12:  # 提前结束计算，如果误差值小于一定值（ 算法保证了新值一定不小于旧值，所以不需要求绝对值 ）
			print('break loop now. current iterate num: ', k+1, 'deviation sum is:', sum( WS - last_WS ))
			break

	"""
	评论：得到的结果和networkx 库的实现实现有差异，Matlab 原生实现和前一个实现版本是一至的，  \
		因为其他实现相当于对结果作了归一化，使得所有句子TextRank 值的总和为1，也就是百分百。  \
		如果我们也对最后的结果WS 作一次归一化就会发现和它们的结果是一模一样的,  \
			归一化的方法是：所有TextRank 值分别除以TextRank 总和
	"""

	return WS


if __name__ == "__main__":

	"""
	textrank.m
str = [
    "a b c"
    "a b f"
    "a h i"
];
documents = tokenizedDocument(str);

scores = textrankScores(documents);

figure
bar(scores)
xlabel("Document")
ylabel("Score")
title("TextRank Scores")

	"""

	# textrank2( [ ['a', 'b', 'c'],
	# 			 ['a', 'b', 'f'],
	# 			 ['a', 'h', 'i']
	# 	  	  ])

	ts = textSummarization( [ 
		                      ['a', 'b', 'c'],
					          ['a', 'b', 'f'],
				 	          ['a', 'h', 'i']
		  	   		        ])
	print ( ts )
	
	# print ( 1.11038961 / (1.11038961 + 1.11038961 + 0.77922078), 0.77922078 / (1.11038961 + 1.11038961 + 0.77922078) )  # 比较归一化后的结果
	
	total = sum(ts)
	ts2 = list( map(lambda n : n/total,ts) )

	print(ts2)

```



### 最大边界相关算法(MMR)

https://github.com/fajri91/Text-Summarization-MMR  能跑

https://blog.csdn.net/Eliza1130/article/details/24033161  解释得很清楚

https://blog.csdn.net/ZJRN1027/article/details/81136761

https://zhuanlan.zhihu.com/p/83596443



```
抽取式摘要的模式主要是使用算法从源文档中提取现成的句子作为摘要
生成式摘要比较接近于我们先理解文本内容，然后再自己写出一段话来对给定的文本进行概括的一种方式
    https://kexue.fm/archives/8046


TextRank的优点在于不需要标注数据，不需要进行预训练，效果尚可。但是缺点也很明显。从其核心思想可以看出来，它挑选摘要句时会侧重于挑选那些与很多句子相似度高的句子。
    https://zhuanlan.zhihu.com/p/83596443


摘要抽取算法——最大边界相关算法MMR(Maximal Marginal Relevance) 实践
    https://www.jianshu.com/p/4a2f7e5d45da
    生成式一般采用的是监督式学习算法，最常见的就是sequence2sequence模型，需要大量的训练数据。生成式的优点是模型可以学会自己总结文章的内容，而它的缺点是生成的摘要可能会出现语句不通顺的情况。
    抽取式指的摘要是从文章中抽出一些重要的句子，代表整篇文章的内容。抽取式的优点是生成的摘要不会出现语句不通顺的情况，而它的缺点是缺乏文本总结能力，生成的摘要可能出现信息丢失的情况。


利用最大边缘相关改进一个简单的文本摘要程序
    https://www.cnblogs.com/little-horse/p/7191287.html
    具体地说，在MMR模型中，同时将相关性和多样性进行衡量。因此，可以方便的调节相关性和多样性的权重来满足偏向“需要相似的内容”或者偏向“需要不同方面的内容”的要求。摘要的核心便是要从原文句子中选一个句子集合，使得该集合在相关性与多样性的评测标准下，得分最高。


《自动文摘研究进展与趋势》
    最大边缘相关法(Maximal Marginal Relevance – MMR)(Carbonell and Goldstein, 1998)，即在每次选取过程中，贪心选择与查询最相关或内容最重要、同时和已选择信息重叠性最小的结果。


《基于分层最大边缘相关的柬语多文档抽取式摘要方法》
    最大边缘相关算法MMR(maximalmarginalrelevance),是一种用于实现文档摘要的方法。新闻文本    
    中包含许多重复的背景信息。MMR的主要思想是使所选的摘要句与文档主旨高度相关,在确保摘要多样
    性的同时,使候选摘要句与已选摘要句之间的差异性尽可能大,最终摘要结果仅有较低冗余信息,达到平衡
    摘要句之间多样性和差异性的目的。

    https://blog.csdn.net/qq_25222361/article/details/78694617
        自动文摘评测方法：Rouge-1、Rouge-2、Rouge-L、Rouge-S


算法的思想：
    与总体相关性越高越好（相关性），与已抽出部分相关性越低越好（冗余性）
```





### 遗忘曲线

#### 曲线拟合

```python
import numpy as np
import matplotlib.pyplot as plt
import torch as t
from torch.autograd import Variable as var


def get_data(x,w,b,d):
    c,r = x.shape
    #y = (w * x * x + b*x + d) #+ (0.1*(2*np.random.rand(c,r)-1))
    y = x * x
    return(y)

xs = np.arange(-3,3,0.01).reshape(-1,1)
ys = get_data(xs,1,-2,3)

xs = var(t.Tensor(xs))
ys = var(t.Tensor(ys))

class Fit_model(t.nn.Module):
    def __init__(self):
        super(Fit_model,self).__init__()
        self.linear1 = t.nn.Linear(1,16)
        self.relu = t.nn.ReLU()
        self.linear2 = t.nn.Linear(16,1)

        self.criterion = t.nn.MSELoss()
        self.opt = t.optim.SGD(self.parameters(),lr=0.01)
    def forward(self, input):
        y = self.linear1(input)
        y = self.relu(y)
        y = self.linear2(y)
        return y
        
model = Fit_model()
for e in range(4001):
    y_pre = model(xs)

    loss = model.criterion(y_pre,ys)
    if(e%200==0):
        print(e,loss.data)
    
    # Zero gradients
    model.opt.zero_grad()
    # perform backward pass
    loss.backward()
    # update weights
    model.opt.step()

ys_pre = model(xs)

plt.title("curve")
plt.plot(xs.data.numpy(),ys.data.numpy())
plt.plot(xs.data.numpy(),ys_pre.data.numpy())
plt.legend("ys","ys_pre")
plt.show()
```



```python
import numpy as np
import matplotlib.pyplot as plt
import torch as t
from torch.autograd import Variable as var

"""
20分钟后，42%被遗忘掉，58%被记住。
1小时后，56%被遗忘掉，44%被记住。
1天后，74%被遗忘掉，26%被记住。
1周后，77%被遗忘掉，23%被记住。
1个月后，79%被遗忘掉，21%被记住。

但是，艾宾浩斯的实验中使用的是毫无意义的字母组合，因此，相对于有意义的词汇而言，其实验没有可比性和参照性的指责也同时存在。并且，再认知可能的遗忘与完全遗忘也没有被区分开来
"""


def get_data(x,w,b,d):
    c,r = x.shape
    #y = (w * x * x + b*x + d) #+ (0.1*(2*np.random.rand(c,r)-1))
    y = x * x
    return(y)

# xs = np.arange(-3,3,0.01).reshape(-1,1)
# ys = get_data(xs,1,-2,3)

# 单位统一成天
xs = np.array( [
    0,
    20/60/24,
    1/24,
    1,
    1*7,
    1*30
] ).reshape(-1,1)

ys = np.array( [
    1.0,
    1-0.42,
    1-0.56,
    1-0.74,
    1-0.77,
    1-0.79
] ).reshape(-1,1)


xs = var(t.Tensor(xs))
ys = var(t.Tensor(ys))

class Fit_model(t.nn.Module):
    def __init__(self):
        super(Fit_model,self).__init__()
        self.linear1 = t.nn.Linear(1,16)
        self.relu = t.nn.ReLU()
        self.linear2 = t.nn.Linear(16,1)

        self.criterion = t.nn.MSELoss()
        self.opt = t.optim.SGD(self.parameters(),lr=0.01)
    def forward(self, input):
        y = self.linear1(input)
        y = self.relu(y)
        y = self.linear2(y)
        return y
        
model = Fit_model()
for e in range(4001):
    y_pre = model(xs)

    loss = model.criterion(y_pre,ys)
    if(e%200==0):
        print(e,loss.data)
    
    # Zero gradients
    model.opt.zero_grad()
    # perform backward pass
    loss.backward()
    # update weights
    model.opt.step()

ys_pre = model(xs)

plt.title("curve")
plt.plot(xs.data.numpy(),ys.data.numpy())
plt.plot(xs.data.numpy(),ys_pre.data.numpy())
plt.legend("ys","ys_pre")
plt.show()

```





```
20分钟后，42%被遗忘掉，58%被记住。
1小时后，56%被遗忘掉，44%被记住。
1天后，74%被遗忘掉，26%被记住。
1周后，77%被遗忘掉，23%被记住。
1个月后，79%被遗忘掉，21%被记住。

但是，艾宾浩斯的实验中使用的是毫无意义的字母组合，因此，相对于有意义的词汇而言，其实验没有可比性和参照性的指责也同时存在。并且，再认知可能的遗忘与完全遗忘也没有被区分开来

```

20分钟后用户在其中一个记忆对象上点了一下“我认识”，这一结果如何影响原来的遗忘曲线？



考虑对象的记忆难度来修正原始曲线

考虑用户在复习时点“认识”或“不认识”的行为来修正原始曲线

20分钟后，42% 的内容将被遗忘，假设这时用户在其中一个记忆对象上点了一下“我认识”，这一结果如何影响原来的遗忘曲线？



近似公式
$$
R = e^{-\frac{t}{s}}
$$

- $R$ 记忆对象

- $t$ 时间
- $s$ 相对记忆强度

> 对于群体而言，S 的值是相对稳定的；而放在个体上来看， S 的值则会因人而异。




多邻国的实现

https://github.com/duolingo/halflife-regression



```
难道good 和superlative 需要以相同的频率复习吗

熟悉度分级
	重点复习不认识的，已认识的会插空巩固
	在每日学习单词的例句中，会包含你不久前刚学过的词，也可能包含你未来需要学的词
	
会根据大家的“认识” 与否，智能调节复习的间隔与频率

扇贝学习记忆曲线
	结合你自身的学习情况，给出更精准的记忆预测结果与建议

	“我认识”或“提示一下”
		积累每日学习行为，智能推测出你的记忆效果，绘制成图中“你的记忆曲线”，预测N 日是后单词的认识率
		


```



```
记忆难度
	第一个是记忆的复杂性（比如单词 good 就比单词 wonderful 容易记很多




```



曲线绘制

频率复习



## 高端玩法：标题生成

[李宏毅2020作业](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html)

- [作业答案 NTU_MachineLearning](https://github.com/IPINGCHOU/NTU_MachineLearning)

  - [Scheduled Sampling](https://zhuanlan.zhihu.com/p/374340958)

  - > 工行纯visa卡（不要限联）可以，刚刚买了，邮编填了蒙大洲的59601，似乎免税了，9.9刀
    >
    > 以上卡的特点就是都只能在境外消费使用，在国内无法使用，这就是为什么国内很多人用信用卡申请失败的原因，失败的往往是那些用了VISA双币卡的信用卡，不是所有中国发行的信用卡都是被拒绝的。
    >
    > 招行的VISA全币卡，中国银行长城跨境通国际借记卡(VISA版)，交通银行信用卡(Master Card)，建设银行信用卡（Master Card）

- [cs224n lec08](https://blog.csdn.net/weixin_41332009/article/details/114129748?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-18.control&dist_request_id=1332049.21748.16195148309019773&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-18.control)

- [cs224 Neural-Machine-Translation-with-Attention](https://github.com/dlxj/DeepNLP-models-Pytorch)

[李宏毅2021作业](https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html)

- [李宏毅机器学习2021笔记—self-attention（上）](https://blog.csdn.net/zghnwsc/article/details/115982794)
- [浅谈Attention-based Model【原理篇】](https://blog.csdn.net/wuzqChom/article/details/75792501)
- [Attention-based Model](https://mmchiou.gitbooks.io/ai_gc_methodology_2018_v1-private/content/attention-based-model-li-hong-yi-jiao-638829/attention-based-model-prof-li-hong-6bc529.html)
- [Attention手写字符识别（有论文）](https://github.com/omni-us/research-seq2seq-HTR)
- [Attention手写公式识别](https://github.com/whywhs/Pytorch-Handwritten-Mathematical-Expression-Recognition)
- [编写高效的PyTorch代码技巧](https://zhuanlan.zhihu.com/p/137965337)
  - 高效DataLoad
- [7 个有用的 PyTorch 技巧](https://zhuanlan.zhihu.com/p/372733826)
- [Kaggle竞赛实战系列：手写数字识别器](https://zhuanlan.zhihu.com/p/101810169)



[《机器翻译：基础与模型》肖桐 朱靖波](https://github.com/NiuTrans/MTBook)

- 束搜索（Beam Search）p.73 （又称束剪枝（Beam Pruning））

  - “<eos>”（end of sequence）

    "<bos>"（beginning of sequence）
- Scheduled Sampling
  - 改善RNN模型在生成任务中的错误累积问题
  - 主要应用在序列到序列模型的训练阶段，而生成阶段则不需要使用



[英中文本机器翻译源码](https://github.com/foamliu/Transformer-v2)

> AI Challenger 2017中的英中机器文本翻译数据集，超过1000万的英中对照的句子对作为数据集合。其中，训练集合占据绝大部分，为12904955对，验证集合8000对，测试集A 8000条，测试集B 8000条。

- 这个是真大佬  机翻、语音识别、图像识别

[AI Challenger 2018 中的阅读理解数据集](https://github.com/foamliu/Reading-Comprehension)

[边做边学深度强化学习：PyTorch程序设计实践 源码](https://github.com/YutaroOgawa/Deep-Reinforcement-Learning-Book)

- **pytorch 实现打砖块**

[seq2seq pytorch 机器翻译源码](https://github.com/SamLynnEvans/Transformer)

[教育目的的GPT](https://github.com/karpathy/minGPT)

[numpy 手写所有主流ML](https://github.com/ddbourgin/numpy-ml)



[循环神经网络 RNN-算法工程师手册](http://www.huaxiaozhuan.com/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/chapters/6_RNN.html)

[手写实现李航《统计学习方法》书中全部算法](https://github.com/Dod-o/Statistical-Learning-Method_Code)

[GitHub中文排行榜](https://github.com/kon9chunkit/GitHub-Chinese-Top-Charts)

[西瓜书公式推导](https://datawhalechina.github.io/pumpkin-book/#/)

[(花书) 数学推导](https://github.com/MingchaoZhu/DeepLearning)

[动手深度学习——编码器—解码器（seq2seq）](https://tangshusen.me/Dive-into-DL-PyTorch/#/chapter10_natural-language-processing/10.9_seq2seq)

[一文看懂 NLP 里的模型框架 Encoder-Decoder 和 Seq2Seq](https://easyaitech.medium.com/%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82-nlp-%E9%87%8C%E7%9A%84%E6%A8%A1%E5%9E%8B%E6%A1%86%E6%9E%B6-encoder-decoder-%E5%92%8C-seq2seq-1012abf88572)

[《百面机器学习》]()





[从语言模型到Seq2Seq：Transformer如戏，全靠Mask](https://kexue.fm/archives/6933)

[万创杯 中医药天池大数据竞赛](https://github.com/kangyishuai/CHINESE-MEDICINE-QUESTION-GENERATION)

[SPACES：“抽取-生成”式长文本摘要（法研杯总结）](https://github.com/bojone/SPACES)

[](https://github.com/bojone/SimCSE)

> ```
> ”代码唯一修改的地方就是在运行extract_convert.py文件的时候报错，TypeError: Object of type int64 is not JSON serializable“该问题我也遇到过，在写入文档前，即 f.write(json.dumps(d, ensure_ascii=False) + '\n')前，加入两行代码
> d = repr(d)
> d = eval(d)就可以正常运行了，不太明白什么原因，转换数据类型再转回来就可以存储了，确实很奇怪
> ```
>
> ```
> import os
> #os.environ["TF_KERAS"] = '1'  # 关键配配，出错的时侯切换试试
> %tensorflow_version 1.14
> ```
>
> ```
> # ! git clone https://github.com/bojone/SPACES.git
> ! git clone https://github.com/dlxj/SPACES.git 
> ```
> ```
> # 授权要点出来的url ，然后复制key 回来，输入，回车
> from google.colab import drive
> drive.mount('/gdrive')
> ! ln -s "/gdrive/My Drive/BERT" "/content/"
> ! unzip ./BERT/chinese_roberta_wwm_ext_L-12_H-768_A-12.zip # -d ./BERT/chinese_roberta_wwm_ext_L-12_H-768_A-12
> ```
>
> ```
> https://drive.google.com/drive/folders/1tFs-wMoXIY8zganI2hQgDBoDPqA8pSmh
> ```

[提速不掉点：基于词颗粒度的中文WoBERT](https://kexue.fm/archives/7758)



[BERT多分类：你还要我怎样？----bert源码使用](https://blog.csdn.net/sjyttkl/article/details/104767467)

[手写Transformer以及思考](http://www.sniper97.cn/index.php/note/deep-learning/note-deep-learning/3620/)



[NLP实战：使用Bert4Keras工具包+Colab实现命名实体识别NER任务](https://www.jianshu.com/p/4254053ff601)

- https://github.com/bojone/bert4keras/blob/master/examples/task_sequence_labeling_ner_crf.py
- https://colab.research.google.com/drive/1p53J9wH5PI5Fb7vhRCexTSot1TShIOxA#scrollTo=_lPjP3oURiRX

> NER（named entity recognition）的本质其实就是从文本识别某些特定实体指称的边界和类别。这些特定的实体可以是：人名、地名、组织机构名、时间和数字表达（包括时间、日期、货币量和百分数等）。

[Google Colab 的正确使用姿势](https://zhuanlan.zhihu.com/p/218133131)

[How To Run CUDA C or C++ on Google Colab or Azure Notebook](https://harshityadav95.medium.com/how-to-run-cuda-c-or-c-on-google-colab-or-azure-notebook-ea75a23a5962)

[CS224N: PyTorch Tutorial (Winter '21)](http://web.stanford.edu/class/cs224n/materials/CS224N_PyTorch_Tutorial.html)

[图解 BERT 预训练模型](https://zhuanlan.zhihu.com/p/279452588)

[当Bert遇上Keras：这可能是Bert最简单的打开姿势](https://kexue.fm/archives/6736)

[《Attention is All You Need》浅读（简介+代码）](https://kexue.fm/archives/4765)

[Attention Is All You Need | 源码解析（pytorch）](https://zhuanlan.zhihu.com/p/126671976)



```
Google Colab可直接从github打开Jupyter notebooks，

只需将“http:// github.com/”替换为“https:// colab.research.google.com/github/”，就会直接加载到Colab中 

```

```
https://colab.research.google.com/github/bojone/SPACES
```

```python
import os
os.chdir("/content/gdrive/MyDrive")

import pdb; pdb.set_trace() # 调试， exit 退出
```





```

抽取式摘要的模式主要是使用算法从源文档中提取现成的句子作为摘要
生成式摘要比较接近于我们先理解文本内容，然后再自己写出一段话来对给定的文本进行概括的一种方式
    https://kexue.fm/archives/8046


TextRank的优点在于不需要标注数据，不需要进行预训练，效果尚可。但是缺点也很明显。从其核心思想可以看出来，它挑选摘要句时会侧重于挑选那些与很多句子相似度高的句子。
    https://zhuanlan.zhihu.com/p/83596443


摘要抽取算法——最大边界相关算法MMR(Maximal Marginal Relevance) 实践
    https://www.jianshu.com/p/4a2f7e5d45da
    生成式一般采用的是监督式学习算法，最常见的就是sequence2sequence模型，需要大量的训练数据。生成式的优点是模型可以学会自己总结文章的内容，而它的缺点是生成的摘要可能会出现语句不通顺的情况。
    抽取式指的摘要是从文章中抽出一些重要的句子，代表整篇文章的内容。抽取式的优点是生成的摘要不会出现语句不通顺的情况，而它的缺点是缺乏文本总结能力，生成的摘要可能出现信息丢失的情况。


利用最大边缘相关改进一个简单的文本摘要程序
    https://www.cnblogs.com/little-horse/p/7191287.html
    具体地说，在MMR模型中，同时将相关性和多样性进行衡量。因此，可以方便的调节相关性和多样性的权重来满足偏向“需要相似的内容”或者偏向“需要不同方面的内容”的要求。摘要的核心便是要从原文句子中选一个句子集合，使得该集合在相关性与多样性的评测标准下，得分最高。
```



### BERT

#### MASK

```
https://github.com/JunnYu/WoBERT_pytorch

import torch
from transformers import BertForMaskedLM as WoBertForMaskedLM
from wobert import WoBertTokenizer
pretrained_model_or_path_list = [
    "junnyu/wobert_chinese_plus_base", "junnyu/wobert_chinese_base"
]
for path in pretrained_model_or_path_list:
    text = "今天[MASK]很好，我[MASK]去公园玩。"
    tokenizer = WoBertTokenizer.from_pretrained(path)
    model = WoBertForMaskedLM.from_pretrained(path)
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs).logits[0]
    outputs_sentence = ""
    for i, id in enumerate(tokenizer.encode(text)):
        if id == tokenizer.mask_token_id:
            tokens = tokenizer.convert_ids_to_tokens(outputs[i].topk(k=5)[1])
            outputs_sentence += "[" + "||".join(tokens) + "]"
        else:
            outputs_sentence += "".join(
                tokenizer.convert_ids_to_tokens([id],
                                                skip_special_tokens=True))
    print(outputs_sentence)
# PLUS WoBERT 今天[天气||阳光||天||心情||空气]很好，我[想||要||打算||准备||就]去公园玩。
# WoBERT 今天[天气||阳光||天||心情||空气]很好，我[想||要||就||准备||也]去公园玩。

```





```
# https://github.com/ymcui/Chinese-BERT-wwm#%E7%AE%80%E4%BB%8B
简介
Whole Word Masking (wwm)，暂翻译为全词Mask或整词Mask，是谷歌在2019年5月31日发布的一项BERT的升级版本，主要更改了原预训练阶段的训练样本生成策略。 简单来说，原有基于WordPiece的分词方式会把一个完整的词切分成若干个子词，在生成训练样本时，这些被分开的子词会随机被mask。 在全词Mask中，如果一个完整的词的部分WordPiece子词被mask，则同属该词的其他部分也会被mask，即全词Mask。

需要注意的是，这里的mask指的是广义的mask（替换成[MASK]；保持原词汇；随机替换成另外一个词），并非只局限于单词替换成[MASK]标签的情况。 更详细的说明及样例请参考：#4

同理，由于谷歌官方发布的BERT-base, Chinese中，中文是以字为粒度进行切分，没有考虑到传统NLP中的中文分词（CWS）。 我们将全词Mask的方法应用在了中文中，使用了中文维基百科（包括简体和繁体）进行训练，并且使用了哈工大LTP作为分词工具，即对组成同一个词的汉字全部进行Mask。

下述文本展示了全词Mask的生成样例。 注意：为了方便理解，下述例子中只考虑替换成[MASK]标签的情况。

说明	样例
原始文本	使用语言模型来预测下一个词的probability。
分词文本	使用 语言 模型 来 预测 下 一个 词 的 probability 。
原始Mask输入	使 用 语 言 [MASK] 型 来 [MASK] 测 下 一 个 词 的 pro [MASK] ##lity 。
全词Mask输入	使 用 语 言 [MASK] [MASK] 来 [MASK] [MASK] 下 一 个 词 的 [MASK] [MASK] [MASK] 。
```



## 生成模型

- https://blog.csdn.net/g11d111/article/details/118026427

  > doc\lang\programming\pytorch\jax\jax_MNIST.ipynb
  >
  > **score-based generative models** 
  >
  > 在图像生成，音频合成(WaveGrad, DiffWave)，形状生成，音乐生成都有着良好表现，甚至音频合成领域的效果优于GAN



## BERT


```
# # http://www.sniper97.cn/index.php/note/deep-learning/traslation/3509/
2018年是机器学习模型处理文本（更准确的说是自然语言处理，NLP）的转折点。我们对于如何以最佳方式表达单词和句子的概念理解正在迅速发展，这种理解能够更好的捕捉句子的潜在含义和关系。
```

```
最近的里程碑式发展是BERT的发布，该事件被描述为NLP新时代的开始。BERT模型在多个基于语言处理的任务中都打破了记录。
```

> BERT**是一个经过训练的Transformer编码器，它是BERT的基础**



```
BERT 模型的训练分为预训练（Pre-training）和微调（Fine-tunning）两步。预训练和下游任务无关，却是一个非常耗时耗钱的过程。Google 坦言，对 BERT 的预训练一般需要 4 到 16 块 TPU 和一周的时间，才可以训练完成。

庆幸的是，大部分 NLP 研究者只需使用 Google 发布的预训练模型，而不需要重复这一过程。你可以把预训练模型想象成一个 Prior，是对语言的先验知识，一旦拥有就不需要重复构造。

微调取决于下游的具体任务。不同的下游任务意味着不同的网络扩展结构：比如一个对句子进行情感分类的任务，只需要在 BERT 的输出层句向量上接入几个 Dense 层，走个 softmax。而对于 SQuAD 上的阅读理解任务，需要对 BERT 输出的词向量增加 match 层和 softmax。

总体来说，对 BERT 的微调是一个轻量级任务，微调主要调整的是扩展网络而非 BERT 本身。换句话说，我们完全可以固定住 BERT 的参数，把 BERT 输出的向量编码当做一个特征（feature）信息，用于各种下游任务。

无论下游是什么任务，对于 NLP 研究者来说，最重要的就是获取一段文字或一个句子的定长向量表示，而将变长的句子编码成定长向量的这一过程叫做 sentence encoding/embedding。

bert-as-service 正是出于此设计理念，将预训练好的 BERT 模型作为一个服务独立运行，客户端仅需通过简单的 API 即可调用服务获取句子、词级别上的向量。在实现下游任务时，无需将整个 BERT 加载到 tf.graph 中，甚至不需要 TensorFlow 也不需要 GPU，就可以在 scikit-learn, PyTorch, Numpy 中直接使用 BERT。
```



```
在实际业务中，对给定Query检索特定范围内的词是十分常见的需求。

对于字面上的匹配总体来说并不复杂，但实际效果就仅限于有字符交集的词语，若是想要上升到语义之间有相关度，就可以化归为学术界常见的语义匹配的问题。

它们给句子的向量编码已经包含足够多的信息了，若是再辅以和业务相关的语料微调，就更好了，这也是最近大家实际应用时的做法。

既然BERT是由多个transformer堆叠而成，而每层transformer都会输出【batch size sequence length hidden size】的向量，那么我们拿其中某层transformer的输出再改造改造作为输入句子的语义编码就好了。

Query通过transformer拿到向量表示，那么词也以此拿到向量表示，而后将query和所有词语的表示计算相似度，按照阈值或者最大n个取出相似的词。
```



```
transfomer的本质是喂入n个token， 输出n个token。当你输入的token不一样时输出的向量也不一样。 比如当你喂入我爱吃苹果， 在pooling_strategy设置为NONE的情况下， 你得到的output的第5和第6（[cls, 我， 爱 ， 吃， 苹， 果]）的代表苹和果的向量， 与你喂入苹果手机真好看的第1， 2的苹和果的向量是不同的。

获得词的向量表示
https://bert-as-service.readthedocs.io/en/latest/tutorial/token-embed.html
	#　Getting ELMo-like contextual word embedding
```



```
但是，当前开源的各类中文领域的深度预训练模型，多是面向通用领域的应用需求，在包括金融在内的多个垂直领域均没有看到相关开源模型。熵简科技希望通过本次开源，推动 NLP技术在金融领域的应用发展，欢迎学术界和工业界各位同仁下载使用，我们也将在时机合适的时候推出性能更好的 FinBERT 2.0 & 3.0。
```



```
Soft-Masked BERT：文本纠错与BERT的最新结合
	# https://zhuanlan.zhihu.com/p/144995580
```



```
在专有领域如何训练自己的BERT？
	# https://www.zhihu.com/question/434726886/answer/1644141072
```



```
https://zhuanlan.zhihu.com/p/110655509
	使用bert-serving生成词向量并聚类可视化
	
bert学习的是字与字之间的关系，你给它一句话，它通过字与字之间的联系输出句向量，你给它一个词语，她就输出这两个字之间的联系输出向量，因为同一个词在不同的语句里，所以它的上下文也不同，向量也不一样	
	
```



```
pytorch+huggingface实现基于bert模型的文本分类（附代码）
	# https://www.cnblogs.com/tangjianwei/p/13334327.html
	
如果你熟悉transformer，相信理解bert对你来说没有任何难度。bert就是encoder的堆叠。

如果你不熟悉transformer，这篇文章是我见过的最棒的transformer图解，可以帮助你理解：http://jalammar.github.io/illustrated-transformer/ 

当然这个作者也做出了很棒的bert图解，链接在此：http://jalammar.github.io/illustrated-bert/
```







#### 从零开始训练

https://huggingface.co/blog/how-to-train



#### 两种大小的BERT：

- BERT BASE 和OpenAI Transformer大小差不多，目的是比较性能。
- BERT LARGE 一个巨大的模型，它达到了论文中提出的SOTA。

```
两种BERT模型都有大量的编码层（论文中称作Transformer块）——BASE版有12层，LARGE版有24层。他们也有一个前馈神经网络（BASE有768个隐藏单元，而LARGE有1024个）和多头注意力机制（BASE有12个，LARGE有16个），而不是Transformer中默认的6个编码层、512个隐藏单元和8头。
```



#### Encoder-Decoder

```
https://easyaitech.medium.com/%E4%B8%80%E6%96%87%E7%9C%8B%E6%87%82-nlp-%E9%87%8C%E7%9A%84%E6%A8%A1%E5%9E%8B%E6%A1%86%E6%9E%B6-encoder-decoder-%E5%92%8C-seq2seq-1012abf88572

Encoder-Decoder 是一类算法的统称，是一个通用的框架，在这个框架下可以使用不同的算法来解决不同的任务

```



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210427095256319.png" alt="image-20210427095256319" style="zoom:50%;" />

1. 不论输入和输出的长度是什么，中间的「向量 c」 长度都是固定的（这也是它的缺陷，下文会详细说明）
2. 根据不同的任务可以选择不同的编码器和解码器（可以是一个 [*RNN*](https://easyai.tech/ai-definition/rnn/) ，但通常是其变种 [*LSTM*](https://easyai.tech/ai-definition/lstm/) 或者 *GRU* ）

只要是符合上面的框架，都可以统称为 Encoder-Decoder 模型。说到 Encoder-Decoder 模型就经常提到一个名词 — — Seq2Seq。



**Encoder-Decoder 强调的是方法，既把输入编码成定长的向量，然后生成人类可以理解的输入**

应用：**机器翻译、对话机器人、诗词生成、代码补全、文章摘要（文本 — 文本）**





#### Seq2Seq

Seq2Seq（是 Sequence-to-sequence 的缩写），就如字面意思，输入一个序列，输出另一个序列。这种结构最重要的地方在于输入序列和输出序列的长度是可变的。

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210427095816591.png" alt="image-20210427095816591" style="zoom:50%;" />

如上图：输入了 6 个汉字，输出了 3 个英文单词。输入和输出的长度不同。



在 Seq2Seq 框架提出之前，深度神经网络在图像分类等问题上取得了非常好的效果。在其擅长解决的问题中，输入和输出通常都可以表示为固定长度的向量，如果长度稍有变化，会使用补零等操作。
然而许多重要的问题，例如机器翻译、语音识别、自动对话等，表示成序列后，其长度事先并不知道。因此如何突破先前深度神经网络的局限，使其可以适应这些场景，成为了13年以来的研究热点，Seq2Seq框架应运而生。



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210427110249918.png" alt="image-20210427110249918" style="zoom: 67%;" />

“<eos>”（end of sequence）

"<bos>"（beginning of sequence）

https://tangshusen.me/Dive-into-DL-PyTorch/#/chapter10_natural-language-processing/10.9_seq2seq





**Seq2Seq 强调的是目的，既满足输入序列、输出序列的都可称为Seq2Seq**







#### Attention 解决信息丢失问题

**Attention 机制就是为了解决「信息过长，信息丢失」的问题。**

Encoder-Decoder 因为中间是定长向量，当输入信息太长时，会丢失掉一些信息。



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210427104701228.png" alt="image-20210427104701228" style="zoom:50%;" />

*Ａttention* 模型的特点是 Eecoder 不再将整个输入序列编码为固定长度的「中间向量 Ｃ」 ，而是编码成一个向量的序列。



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210429141931516.png" alt="image-20210429141931516" style="zoom:50%;" />

p.353《机器翻译：基础与模型》肖桐 朱靖波



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210429143540051.png" alt="image-20210429143540051" style="zoom: 67%;" />

p.355



#### 过拟合

验证集在训练过程中还可以用来监控模型是否发生过拟合，一般来说验证集表现稳定后，若继续训练，训练集表现还会继续上升，但是验证集会出现不升反降的情况，这样一般就发生了过拟合。



## huggingface 企业级bert



```
# https://zhuanlan.zhihu.com/p/358525654
这段时间疯狂用了一些huggingface来打比赛，大概是把整个huggingface的api摸得差不多了，后面分不同的块来记录一下常见的用法。

transformers的前身是pytorch-transformers和pytorch-pretrained-bert，主要提供了自然语言理解（NLU）和自然语言生成（NLG）的通用体系结构（BERT，GPT-2，RoBERTa，XLM，DistilBert，XLNet等） ）包含超过32种以100多种语言编写的预训练模型，以及TensorFlow 2.0和PyTorch之间的深度互操作性。

不过就上手而言，torch还是更顺滑一些（因为很多非官方例子都是用torch来撸的），顺便让我熟悉一下torch的使用。

整体上调研了github上的多个相关的项目，包括huggingface transformer，谷歌开源的bert，bert4keras，tensorflow hub，以及其它的一些个人的keras-bert之类的实现，总的来说，huggingface的优点在于：

1、企业级维护，可靠性高，生产上用起来放心；

2、star多，issues多，网上能够找到的各种各样对应不同需求的demo代码多；

3、适配tf.keras和torch，一次性可以撸两个框架；

4、官方的tutorial是真的太特么全了

5、在PyTorch和TensorFlow 2.0之间轻松切换，从而允许使用一种框架进行训练，而使用另一种框架进行推理。非常灵活，当然其实torch和tf之间框架互相转换的功能的library挺多的；
```



### 情感二分类

```
# https://github.com/karlhl/Bert-classification-pytorch
```





## 深度文本匹配



```
1、背景介绍
文本匹配是自然语言处理中的一个核心问题，很多自然语言处理的任务都可以抽象成文本匹配问题，例如信息检索可以归结成查询项和文档的匹配，问答系统可以归结为问题和候选答案的匹配，对话系统可以归结为对话和回复的匹配。针对不同的任务选取合适的匹配模型，提高匹配的准确率成为自然语言处理任务的重要挑战。

2、数据集介绍
论文中经常用到的数据集：

SNLI：570K条人工标注的英文句子对，label有三个：矛盾、中立和支持
MultiNLI：433K个句子对，与SNLI相似，但是SNLI中对应的句子都用同一种表达方式，但是MultiNLI涵盖了口头和书面语表达，可能表示形式会不同(Mismatched)
Quora 400k个问题对，每个问题和答案有一个二值的label表示他们是否匹配
WikiQA
是问题是相对应的句子的数据集，相对比较小。
```



### pairwise、pointwise 、 listwise



```
# pairwise、pointwise 、 listwise算法是什么?怎么理解？主要区别是什么？
https://blog.csdn.net/pearl8899/article/details/102920628
```

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210702091101111.png" alt="image-20210702091101111" style="zoom:50%;" />

```
# https://zhuanlan.zhihu.com/p/111636490
Learning to Rank： pointwise 、 pairwise 、 listwise
```

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210702091438189.png" alt="image-20210702091438189" style="zoom: 80%;" />





## 深度信息检索



```
https://www.cnblogs.com/zhangxianrong/p/14793120.html

Sentence Transformers + Faiss
```



## 激活函数



```
Softmax与交叉熵损失的实现及求导
	https://zhuanlan.zhihu.com/p/67759205
	einsum 爱因斯坦求和约定（极大简化代码）
		https://zhuanlan.zhihu.com/p/71639781
	

Softmax（归一化指数函数，sigmoid函数就是其输入数为2时的特例）
	dim=0：对每一列的所有元素进行softmax运算，并使得每一列所有元素和为1。
	dim=1：对每一行的所有元素进行softmax运算，并使得每一行所有元素和为1。
	

LogSoftmax其实就是对softmax的结果进行log，即Log(Softmax(x))


Softmax将多个神经元的输出，映射到（0,1）区间内,并且做了归一化，所有元素的和累加起来等于1。可以直接当作概率对待

Softmax中使用了指数，这样可以让大的值更大，让小的更小，增加了区分对比度，学习效率更高。第二个是因为softmax是连续可导的，消除了拐点，这个特性在机器学习的梯度下降法等地方非常必要。


# https://zhuanlan.zhihu.com/p/48776056
	也谈激活函数Sigmoid,Tanh,ReLu,softplus,softmax

建议使用ReLU函数，但是要注意初始化和learning rate的设置；可以尝试使用Leaky ReLU或ELU函数；不建议使用tanh，尤其是sigmoid函数。

```



```python
# 问题：数值溢出
def softmax(X):
    exps = np.exp(X)
    return exps / np.sum(exps)
```



```python
# 改进
def stable_softmax(X):
    exps = np.exp(X - np.max(X))
    return exps / np.sum(exps)
```

![image-20210806114907337](深入理解神经网络：从逻辑回归到CNN.assets/image-20210806114907337.png)







## 损失函数



```
交叉熵（cross entropy）是一个常用的衡量两个概率分布差异的测量函数

KL散度可以被用于计算代价，而在特定情况下最小化KL散度等价于最小化交叉熵。而交叉熵的运算更简单，所以用交叉熵来当做代价。

# https://zhuanlan.zhihu.com/p/86184547
	神经网络多分类中softmax+cross-entropy的前向传播和反向传播过程

# https://stats.stackexchange.com/questions/235528/backpropagation-with-softmax-cross-entropy

# https://zhuanlan.zhihu.com/p/86787709

# https://gombru.github.io/2018/05/23/cross_entropy_loss/

# https://stats.stackexchange.com/questions/235528/backpropagation-with-softmax-cross-entropy
# doc\lang\programming\Notes on Backpropagation.pdf

# https://deepnotes.io/softmax-crossentropy
	Classification and Loss Evaluation - Softmax and Cross Entropy Loss
#  http://blog.prince2015.club/2020/03/27/softmax/
	Softmax函数求导详解
		Softmax函数有和Sigmoid函数类似的功能，Sigmoid常常被用于二分类问题的顶层，作为类标为   1的概率。当问题被推广为多分类问题时，Sigmoid函数就不能使用了，此时往往使用Softmax函数。


# https://blog.csdn.net/xg123321123/article/details/80781611

分类问题和回归问题是监督学习的两大种类：分类问题的目标变量是离散的；回归问题的目标变量是连续的数值。神经网络模型的效果及优化的目标是通过损失函数来定义的。

回归问题解决的是对具体数值的预测。比如房价预测、销量预测等都是回归问题。这些问题需要预测的不是一个事先定义好的类别，而是一个任意实数。解决回顾问题的神经网络一般只有一个输出节点，这个节点的输出值就是预测值。对于回归问题，常用的损失函数是均方误差( MSE，mean squared error )。


https://freemind.pluskid.org/machine-learning/softmax-vs-softmax-loss-numerical-stability/
	Softmax vs. Softmax-Loss: Numerical Stability


Softmax loss是由softmax和交叉熵(cross-entropy loss)loss组合而成，所以全称是softmax with cross-entropy loss，在caffe，tensorflow等开源框架的实现中，直接将两者放在一个层中，而不是分开不同层，可以让数值计算更加稳定，因为正指数概率可能会有非常大的值。

# https://deepnotes.io/softmax-crossentropy
	Classification and Loss Evaluation - Softmax and Cross Entropy Loss

```





```
# https://zhuanlan.zhihu.com/p/61944055
均方误差（mse）实际就是高斯分布的最大似然，交叉熵（crossEntropy）是多项式分布的最大似然，分类问题当然得用多项式分布

# https://segmentfault.com/a/1190000018510069
北大旁听 - 深入Loss Function的来源

其实目前大部分使用的损失函数都是以最大似然原理为核心而设计的。

深度学习的核心问题就是让网络产生的数据分布尽可能贴近样本分布，所以极大似然原理就很自然的用在了深度学习上。

而要评判分布的“差别”，首先需要可以评判分布的指标，而这个指标就是香农的信息熵。

为什么要让偏差符合正态分布呢？D

其实这是由以下两条理论得出的：

同分布中心极限定理：n个独立同分布的随机变量之和，服从正态分布。
非同分布的李雅普诺夫定理：大量随机因素叠加的结果，近似服从正态分布。
有了这已经证明的两条理论，才可以基于正态分布，得出MSE的标准形式。

二项分布的典型例子是抛硬币，每次试验有正反两种对立的可能，多项分布的例子是扔骰子，每次试验有多种可能，进行多次试验，多项分布描述的是每种可能发生次数的联合概率分布。

# https://deepnotes.io/softmax-crossentropy
	Classification and Loss Evaluation - Softmax and Cross Entropy Loss

# https://zhuanlan.zhihu.com/p/345025351
	机器学习理论—信息论：自信息、熵、交叉熵与KL散度

# https://mathpretty.com/12068.html
PyTorch中交叉熵的计算-CrossEntropyLoss介绍
	# https://muyuuuu.github.io/2021/04/02/cross-entropy/
		交叉熵优缺点分析
			# https://blog.csdn.net/tsyccnh/article/details/79163834
				一文搞懂交叉熵在机器学习中的使用，透彻理解交叉熵背后的直觉
		
		

# https://www.cnblogs.com/shine-lee/p/12032066.html
损失函数是网络学习的指挥棒，它引导着网络学习的方向——能让损失函数变小的参数就是好参数。

在这个前提下，均方误差损失可能会给出错误的指示，比如猫、老虎、狗的3分类问题，label为[1,0,0]，在均方误差看来，预测为[0.8,0.1,0.1]要比[0.8,0.15,0.05]要好，即认为平均总比有倾向性要好，但这有悖我们的常识。

而对交叉熵损失，既然类别间复杂的相似度矩阵是难以量化的，索性只能关注样本所属的类别，只要y^p越接近于1就好，这显示是更合理的。

# https://www.cnblogs.com/tornadomeet/archive/2013/03/23/2977621.html
Softmax Regression 练习


```





```
# mnist手写数字识别之损失函数精讲(百度架构师手把手带你零基础实践深度学习原版笔记系列)
https://blog.csdn.net/coolyoung520/article/details/109015443

```





### BP Cross Entropy



```
# https://stats.stackexchange.com/questions/235528/backpropagation-with-softmax-cross-entropy

# https://zhuanlan.zhihu.com/p/86184547
```








## mini-batch 学习



```
# 《深度学习入门：基于Python的理论与实现》 p.90
和收视率一样，mini-batch 的损失函数也是利用
一部分样本数据来近似地计算整体。也就是说，用随机选择的小批
量数据（mini-batch）作为全体训练数据的近似值。
```





## OCR

##### manga-ocr

- https://github.com/kha-white/manga-ocr

  - https://github.com/kha-white/mokuro

    - https://github.com/dmMaze/comic-text-detector

      - https://github.com/juvian/Manga-Text-Segmentation

      - https://t.me/SugarPic

- https://github.com/dmMaze/BallonsTranslator  漫画自动翻译

- https://github.com/PaddlePaddle/PaddleOCR/issues/10815  返回单个字坐标

- https://github.com/demuxin/pytorch_tricks

- https://github.com/ZER-0-NE/EAST-Detector-for-text-detection-using-OpenCV

- https://github.com/demuxin/OpenCV_project/blob/master/EAST_Text_Detection/text_detection.py

  - 完整的文本检测代码

  > OpenCV EAST 文本检测

- https://developer.aliyun.com/article/807683

- https://cloud.tencent.com/developer/article/1542875

  > OCR学习路径之文本检测（下）EAST算法简介

- https://www.jianshu.com/p/34b73ca276fc

- https://blog.csdn.net/u011046017/article/details/93392862

  > EAST结构分析+pytorch源码实现

- https://blog.csdn.net/haeasringnar/article/details/122936537

  > 飞桨OCR打标、训练、预测、部署全流程

- https://github.com/microsoft/unilm/tree/master/trocr
  
  - https://www.jianshu.com/p/3a054054f6f1
  
  > TrOCR

- https://github.com/chineseocr/trocr-chinese
  
> trocr-chinese 

- https://github.com/chineseocr/chineseocr/tree/master
  
  > chineseocr

- https://github.com/BADBADBADBOY/pytorchOCR

  > **dbnet 检测， 识别 都有**

- https://github.com/tommyMessi/crnn_ctc-centerloss

  > **ctcloss + centerloss crnn 解决形近字**

- https://github.com/open-mmlab/mmocr

  > **mmocr**

  - https://github.com/open-mmlab/mmocr/issues/992

    > 中文识别
  >
    > ```
  > python mmocr/utils/ocr.py t.jpg --det None --recog SAR_CN --output out.jpg
    > 
    >  wget "https://download.openmmlab.com/mmocr/textrecog/sar/dict_printed_chinese_english_digits.txt"   put it to folder /data/chineseocr/labels/
    > 
    > Yes, since your input is a cropped image, it is unnecessary to use a detection model; if the det model is not specified to None here, it will use PANet_IC15 as the detector by default.
    > MMOCR currently does not provide a Chinese-specific pre-trained model for the detector, however, you may try the model pre-trained on ICDAR2017 (such as MaskRCNN_IC17), since this is a multilingual dataset containing Chinese training samples.
    > 
    > 
    > python demo/ocr_image_demo.py t.jpg out.jpg --recog-config configs/textrecog/sar/sar_r31_parallel_decoder_chinese.py --recog-ckpt https://download.openmmlab.com/mmocr/textrecog/sar/sar_r31_parallel_decoder_chineseocr_20210507-b4be8214.pth
    > 
    > wget "https://download.openmmlab.com/mmocr/textrecog/sar/dict_printed_chinese_english_digits.txt"
    > 
    > put it to folder data/chineseocr/labels/
    > ```
    >
    > 
  
  - https://github.com/open-mmlab/mmocr/issues/1161
  
    > 中文训练集

- https://blog.csdn.net/jizhidexiaoming/article/details/80345832

  > 论文复现，很多 **matlab 代码**

- https://github.com/Huntersdeng/abinet-paddle

  > 论文复现 ABINet

- https://itcn.blog/p/1400806914.html

  > MMOCR之多模态融合ABINET文字识别  **宝藏解读**




```
    # Output of the network are log-probabilities, need to take exponential for probabilities
    ps = torch.exp(logps)

    import pdb; pdb.set_trace() # 调试， exit 退出

    probab = list(ps.cpu().numpy()[0])
    pred_label = probab.index(max(probab))  # 这一句特别精髓
    	# 先求list 里的最大值，再求最大值在list 里的索引，索引既是手写数字的以预测值
    
    
```



### lmdb

```
LMDB全称Lightning Memory-Mapped Database,是内存映射型数据库，这意味着它返回指向键和值的内存地址的指针，而不需要像大多数其他数据库那样复制内存中的任何内容，使用内存映射文件，可以提供更好的输入/输出性能，对于神经网络的的大型数据集可以将其存储到LMDB中

LMDB属于key-value数据库，而不是关系型数据库( 比如 MySQL )，LMDB提供 key-value 存储，其中每个键值对都是我们数据集中的一个样本。LMDB的主要作用是提供数据管理，可以将各种各样的原始数据转换为统一的key-value存储。

LMDB不仅可以用来存放训练和测试用的数据集，还可以存放神经网络提取出的特征数据。如果数据的结构很简单，就是大量的矩阵和向量，而且数据之间没有什么关联，数据内没有复杂的对象结构，那么就可以选择LMDB这个简单的数据库来存放数据。

用LMDB数据库来存放图像数据，而不是直接读取原始图像数据的原因：

数据类型多种多样，比如：二进制文件、文本文件、编码后的图像文件jpeg、png等，不可能用一套代码实现所有类型的输入数据读取，因此通过LMDB数据库，转换为统一数据格式可以简化数据读取层的实现。
lmdb具有极高的存取速度，大大减少了系统访问大量小文件时的磁盘IO的时间开销。LMDB将整个数据集都放在一个文件里，避免了文件系统寻址的开销，你的存储介质有多快，就能访问多快，不会因为文件多而导致时间长。LMDB使用了内存映射的方式访问文件，这使得文件内寻址的开销大幅度降低。
```





### tesseract nodejs

```javascript
# https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件
# 自动安装的语言模型很小，不准确

先安装c++17
yum install centos-release-scl
yu install devtoolset-7-gcc-c++ --enablerepo='centos-sclo-rh'
scl enable devtoolset-7 'bash' # 切换编译器
which gccc


// https://thelinuxcluster.com/2020/02/04/compiling-tesseract-5-0-on-centos-7/
> yum install autoconf automake libtool pkgconfig.x86_64 libpng12-devel.x86_64 libjpeg-devel libtiff-devel.x86_64 zlib-devel.x86_64
# wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz .
# tar -zxvf leptonica-1.79.0.tar.gz
# cd leptonica-1.79.0
# ./configure --prefix=/usr/local/leptonica-1.79.0
# make
# make install

> export PKG_CONFIG_PATH=/usr/local/leptonica-1.79.0/lib/pkgconfig
$ git clone https://github.com/tesseract-ocr/tesseract.git
$ cd tesseract
$ ./autogen.sh
$ ./configure --prefix=/usr/local/tesseract-5.0 
$ make
$ make install
$ ln -s /usr/local/tesseract-5.0/bin/tesseract /usr/local/bin/
$ tesseract  --version #  成功


// https://github.com/schwarzkopfb/tesseract-ocr/blob/master/docs.md
// npm install tesseractocr
(async()=>{

    let tesseract = require('tesseractocr')
    let recognize = tesseract.withOptions({
        psm: 4,
        language: [ 'chi_sim', 'eng' ],
        config: ['tessedit_do_invert=0']
    })

    let recognize2 = tesseract.withOptions({
        psm: 4,
        language: [ 'eng' ],
        config: ['tessedit_do_invert=0']
    })

    // const text = await recognize('t.jpg')
    // console.log('Yay! Text recognized:', text)

    const text = await recognize('7001.jpg')
    console.log('Yay! Text recognized:', text)

    // const text2 = await recognize2('t.jpg')
    // console.log('Yay! Text recognized:', text2)

    let a = 1

})()

recognize(`${__dirname}/image.png`, (err, text) => { /* ... */ })
recognize(Buffer.from(/* ... */), (err, text) => { /* ... */ })
recognize(fs.createReadStream(/* ... */), (err, text) => { /* ... */ })
recognize('image.jpeg', (err, text) => { /* ... */ })
recognize('image.tiff').then(console.log, console.error)
```



### tesseract 大佬

- https://fancyerii.github.io/2019/03/12/3_tesseract/

```

# https://fancyerii.github.io/2019/03/12/3_tesseract/
	# tesseract 很深入
	> tesseract --version
	> tesseract test.png test -l chi_sim
	> tesseract t3.jpg stdout -l chi_sim # 标准输出
# https://github.com/yizt/crnn.pytorch
	# 很好
# https://github.com/xiaofengShi/CHINESE-OCR
	ctpn是一种基于目标检测方法的文本检测模型
	# 也很好
	
	理解文本检测网络CTPN
		https://zhuanlan.zhihu.com/p/77883736

# http://xiaofengshi.com/2019/01/23/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0-TextDetection/
	# 全是干货

# https://github.com/wangqingbaidu/Dr.Sure/blob/master/Algorithm/Attention-based_Extraction_of_Structured_Information_from_Street_View_Imagery.md

	一般来说，OCR过程包括两个部分，一个是检测，一个是识别，这个pipeline与人脸识别类似。

	检测，就是把包括文字的区域检测出来，但是与人脸检测不同的是，文字识别不像人脸识别那样包括一些特别通用的pattern，这个检测的难度还是不小。

	识别，就是把检测输出的包括文字的图像块里面的具体文字识别出来，这个地方与人脸识别也有所不同，通常来说人脸识别的识别阶段不是一个分类任务，而是一个最近邻匹配任务，但是OCR的识别则是一个文字的分类任务，而且是sequence的分类任务。

# https://blog.csdn.net/u014453898/article/details/104784212
	加入attention的crnn ---- ocr之pytorch代码解释(带代码)
# https://zhuanlan.zhihu.com/p/142886134
	基于transformer的文本识别方法
# https://zhuanlan.zhihu.com/p/141389516
	文本识别中的注意力机制

# https://github.com/chenjun2hao/Attention_ocr.pytorch


# https://blog.csdn.net/Vermont_/article/details/108424547?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-19.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-19.control

# https://github.com/YCG09/chinese_ocr
# https://mp.weixin.qq.com/s/jWo8cdbnM-bO3ImTi4gZLg

【OCR学习笔记】9、OCR中文项目综合实践（CTPN+CRNN+CTC Loss原理讲解）


```



- 开运算：先腐蚀后膨胀，用于移除由图像噪音形成的斑点
- 闭运算：先膨胀后腐蚀，用来连接被误分为许多小块的对象



### tesseract 自已训练

- https://zhuanlan.zhihu.com/p/58366201

  > Tesseract 4.0 LSTM训练超详细教程



- https://www.jianshu.com/p/a7bf361cd70a

  ```
  官方训练教程：https://github.com/tesseract-ocr/tessdoc/blob/master/TrainingTesseract-4.00.md
  语言包地址：https://github.com/tesseract-ocr/tessdata_best
  
  4.0 LSTM的训练流程和3.0版本有点像，如下：
  
  准备培训文字（txt）。
  将文本转换为 图像和box文件。
  制作unicharset文件。
  根据unicharset和可选的词典数据制作入门级训练数据。
  运行tesseract以处理图像和 box文件以创建训练数据集。
  对训练数据集进行训练。
  合并数据文件。
  其区别在于：
  1、 3.0版本训练图像文字，需要知道每个要训练的字在其图像中的具体坐标，而4.0版本训练仅需要知道这个字所在行的坐标即可（即不需要逐个字去调试坐标）。
  2、3.0版本训练过程中的 .tr文件在4.0版本的训练过程中被替换为.lstmf数据文件。（其他训练教程里面如果出现了.tr文件，那就可以肯定他的教程是3.0版本）
  3、 字体可以并且应该自由混合而不是分开。（这段话我看不懂）
  4、 3.0版本的聚类步骤（mftraining，cntraining，shapeclustering）在4.0中被替换为一个缓慢的lstmtraining步骤。（即3.0的多个合并步骤在4.0这里只需要一个步骤完成）
  5、 4.0的训练需要一气呵成，如果训练中断，重启后很难自动结束。
  6、 4.0使用的语言模型、unicharset和3.0版本所使用的语言模型和unicharset不一样（所以不要拿3.0的数据来4.0里面训练）。
  
  
  
  ```

  

### tesseract 文字坐标

- https://localcoder.org/getting-the-bounding-box-of-the-recognized-words-using-python-tesseract

- https://github.com/tesseract-ocr/tesseract/issues/2879

  > **Tesseract**'s recognizer just finds words, and **doesn't tell us anything about spaces**. 
  
- https://github.com/tesseract-ocr/tesseract/issues/3105
  
  > if you need **accurate bounding boxes** (on character level), you need **to use legacy engine**
  > (e.g. `tesseract INPUT.jpg OUTPUT -l nor --oem 0 makebox`).
  >
  > \# ! tesseract --help-extra  # 查看额外参数

```python
import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('7001.jpg')
height = img.shape[0]
width = img.shape[1]

# ! tesseract --help-extra  # 查看额外参数
config = '--oem 0'  # tesseract 命令行的传参

texts = []

d = pytesseract.image_to_boxes(img, output_type=Output.DICT, config=config)  # '--psm 6 --oem 1'
n_boxes = len(d['char'])
for i in range(n_boxes):
    (text,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
    cv2.rectangle(img, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)
    texts.append(text)
cv2.imshow('img',img)
cv2.waitKey(0)
```


```
# tesseract ocr 文字坐标
import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('7001.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
```



```
import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('7001.jpg')
height = img.shape[0]
width = img.shape[1]

d = pytesseract.image_to_boxes(img, output_type=Output.DICT)
n_boxes = len(d['char'])
for i in range(n_boxes):
    (text,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
    cv2.rectangle(img, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)
```



```
import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('7001.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (text,x,y,w,h) = (d['text'][i],d['left'][i],d['top'][i],d['width'][i],d['height'][i])
    cv2.rectangle(img, (x,y), (x+w,y+h) , (0,255,0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)
```





#### 命令行

```
# https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件

tesseract .\billion.png out -l eng -c hocr_char_boxes=1 makebox hocr pdf
```



```
tesseract t3.jpg stdout -l chi_sim 
--oem 0 # Legacy engine only.  文字定位更准确
```

```
四。命令行介绍 
tesseract test.jpg test.txt -l chi_sim+eng -psm 7 --oem 1 

-l chi_sim+eng 指定中文字库和英文字库

-psm 7 表示告诉tesseract code.jpg图片是一行文本这个参数可以减少识别错误率. 默认为 3。自己测试好像是一样的

             默认的tesseract将一个图片当成一个文档来看。如果只需要指定的区域可以使用不同的分割模式，使用psm参数

            参考：https://blog.csdn.net/claroja/article/details/82992643

--oem 1 --oem 后面的参数 1代表用lstm引擎识别, 0表示用传统引擎识别

configfile 参数值为tessdata\configs 和 tessdata\tessconfigs 目录下的文件名.

```









### pytesseract

```
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt  
%matplotlib inline

path="9450.jpg"

"""
🐬指明tesseract命令位置
"""

tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd =tesseract_cmd

"""
 👻基础的图片转换为文字
"""

# 显示
image=Image.open(path)
plt.figure(figsize=(2,2))
plt.axis('off')
plt.imshow(image)

print(pytesseract.image_to_string(image))


"""
🤠当前支持的语言 osd On Screen Display 屏幕显示字符
"""
print(pytesseract.get_languages(config=''))

"""
🤓尝试修改语言参数
"""
print(pytesseract.image_to_string(image, lang='osd'))

"""
🐱‍👓识别超时就停止
"""
try:
    print(pytesseract.image_to_string(image, timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string(image, timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

"""
🎅将识别结果导出成文字可选的pdf
这个达成的效果，就是会把图片转成pdf，同时其中的文字会是可编辑/可选的
"""
pdf = pytesseract.image_to_pdf_or_hocr(Image.open("1.png"), extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

"""
💌修改参数
"""
configdigit='--psm 6 --oem 1'
print(pytesseract.image_to_string(img_cv,config=configdigit))

configdigit='--psm 6 --oem 3  -c tessedit_char_whitelist=0123456789'
print(pytesseract.image_to_string(img_cv,config=configdigit))

"""
🍳关于其中的psm参数和oem参数，可以查看帮助文档
"""
! tesseract --help-extra
> Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.

OCR Engine modes:
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.

```



### OCR 大佬

- https://zhuanlan.zhihu.com/p/448407149

  > CV预训练MAE（Masked AutoEncoder）
  >
  > 继2017年Transformer[2]被提出之后，预训练成为了NLP领域主流的研究方向，经典算法有GPT，BERT[3]等。GPT是经典的自回归（Auto-Regressive）预训练模型，而BERT是经典的掩码模型，或者说是去噪自编码（Denosing AutoEncoder）语言模型。DeepMind的image GPT（iGPT）将预训练任务迁移到了计算机视觉方向，它的预训练任务借鉴了GPT系列，即通过自回归（Auto-Regressive）的方式根据保留的图像上半部分逐像素的预测图像的下半部分的方式，并且通过微调和线性探测两个方法验证了iGPT在图像分类任务上可以起到明显的效果提升的作用。iGPT表明自回归训练任务是可以迁移计算机视觉方向的，那么自编码语言模型是否也能迁移到计算机视觉上呢？这里要介绍的Masked AutoEncoder（MAE）给出了肯定的答案。MAE的最核心的思想是通过对图片中的patch进行随机掩码，然后通过未被掩码的区域预测被掩码掉的区域，进行使得模型学习图像的语义特征。





### 文本检测 

- https://github.com/demuxin/OpenCV_project/tree/master/EAST_Text_Detection

  > EAST 算法

- https://zhuanlan.zhihu.com/p/339381734

  > 文字检测算法：PSENet

- https://blog.csdn.net/weixin_40437821/article/details/117194635

  > DBNet
  >
  > - https://blog.csdn.net/hhhhhhhhhhwwwwwwwwww/article/details/123904386
  >
  >   > pytorch 完整训练
  > - https://blog.csdn.net/nihate/article/details/115504611?spm=1001.2014.3001.5501
  >   > **DBNet车牌识别** 
  >   >
  >   > 在TensorRT或者openvino或者opencv和onnxruntime部署时，pytorch模型转onnx这一步是必不可少的
  >   >
  >   > - https://github.com/hpc203/license-plate-detect-recoginition-opencv/issues/1
  >   >
  >   >   > **一些坑**
  >   >   >
  >   >   > 较一下out1 = torch.div(out1, f.item())和out1 = torch.div(out1, f)里的除数的区别
  >   >   >
  >   >   > f = torch.mean(f)得到的，在pytorch对一个4维张量求平均值后得到的是没有形状信息的张量，其实是一个标量数值，如果想要转化成标量数值，那就需要加.item()
  >   >
  >   > - https://github.com/hpc203/dbnet-opencv-cpp-python
  >   > **OpenCV+DBNet成品**
  >   > - https://blog.csdn.net/nihate/article/details/108754622
  >   > **极简主义OCR**  



#### DBNet 可微分二值化

see doc\lang\programming\pytorch\文本检测\DBNET  **论文代码都有**

https://blog.csdn.net/weixin_43507865/article/details/136671486

> DBNet.pytorch: 训练灰度图时需要在配置里移除`dataset.args.transforms.Normalize`

- a

  > ## 实验
  >
  > **数据集**
  >
  > **SynthText**
  >
  > - https://github.com/ankush-me/SynthText  生成代码
  >
  > 人工合成的数据集，包含800k张图片，8k张背景图，作者仅仅用来预训练。
  >
  > **MLT-2017 dataset**
  >
  > 多语言的数据集，9种语言展示6种脚本。7200张训练数据，1800张验证数据，9000张测试数据。我们使用训练数据和验证数据来finetune。
  >
  > **ICDAR 2015 dataset**
  >
  > 由google glassees采集，分辨率720*1280，1000张训练数据，500张测试数据。标注是单词级别的。
  >
  > **MSRA-TD500 dataset**
  >
  > 中英文双语的数据集。300张训练数据，200张测试数据。标注是文字行级别的。跟之前的方法一样，我们把HUST-TR400中的400张训练数据也加进来了。
  >
  > **CTW1500 dataset**
  >
  > 卷曲文字数据集，1000张训练数据，500张测试数据。标注是文字行级别的。
  >
  > **Total-Text dataset**
  >
  > 包括各种形状的文字，水平的、多方向的和卷曲的。1255张训练数据和300张测试数据。标注是单词级别的。
  >
  > **实现细节**
  >
  > **先使用SynthText预训练100k次迭代，继续在真实数据上 finetune 1200个epochs。**训练batch size为16。使用poly lr，当前学习率为初始学习率乘上 (1−itermax_iter)power ，初始学习率为0.007，power为0.9。
  >
  > 数据增广用到三种方法：(1)随机在 (−10∘,10∘) 之间旋转；(2)随机裁剪；(3)随机翻转；所有图片最终都转到640*640。
  >
  > 在测试阶段，我们保持原图的比例，针对不同的数据设置一个固定的图像高度。batch size为1，单张1080ti GPU，单线程。总耗时包括模型前向和后处理，后处理耗时占总体的30%。

- https://github.com/DayBreak-u/chineseocr_lite OCR**成品**

- https://paddlepedia.readthedocs.io/en/latest/tutorials/computer_vision/OCR/OCR_Detection/DBNet.html
  
- https://blog.csdn.net/michaelshare/article/details/108811236
  
- https://github.com/yts2020/DBnet_pytorch  
  
  - https://blog.csdn.net/ytsaiztt/article/details/118090611  DBNet的简单复现  **必看 简洁的实现**
  
- https://zhuanlan.zhihu.com/p/382641896 **DBNet的简单复现**
  
- https://blog.csdn.net/u010901792/article/details/112791647  **宝藏解读**
  
  整个流程如下
  
  1. 图像经过FPN网络结构，得到四个特征图，分别为1/4,1/8,1/16,1/32大小；
  
  2. 将四个特征图分别上采样为1/4大小，再concat，得到特征图F（**特征金字塔**上采样到相同的尺寸，并进行**特征级联**得到特征F）
  
     > concat：系列**特征融合**，直接将两个特征进行连接。两个输入特征x和y的维数若为p和q，输出特征z的**维数为p+q**；
  
  3. 由F得到 probability map (P) 和 threshold map (T)
  
  4. 通过P、T计算（通过可微分二值化DB，下文介绍） approximate binary map（ 近似binary map  B-hat ）
  
  对于每个网络，一定要区分训练和推理阶段的不同：
  
  - 训练阶段：对P、T、B进行监督训练，P和B是用的相同的监督信号（label）；
  - 推理阶段：通过P或B就可以得到文本框。
  
- https://blog.csdn.net/u010901792/article/details/112791647

  > **对每一个像素点进行自适应二值化**，二值化阈值由网络学习得到，彻底将二值化这一步骤加入到网络里一起训练
  >
  > 和常规基于语义分割算法的**区别是多了一条threshold map分支**，该分支的主要目的是和分割图联合得到更接近二值化的二值图，属于辅助分支。**其余操作就没啥了**。整个核心知识就这些了。

- https://github.com/christianversloot/machine-learning-articles/blob/main/upsampling2d-how-to-use-upsampling-with-keras.md  **上采样很详细**
  
  > **网络输出：**
  >
  > 1.probability map, w\*h\*1 , 代表像素点是文本的概率
  >
  > 2.threshhold map, w\*h\*1, 每个像素点的阈值
  >
  > 3.binary map, w\*h\*1, 由1,2 计算得到，计算公式为DB公式
  >
  > ```python
  > thresh_binary = self.step_function(binary, thresh)
  > 	# binary和thresh分别为P和T
  > 	# thresh_binary 就是approximate binary map
  > 
  > def step_function(self, x, y):
  > 	return torch.reciprocal(1 + torch.exp(-self.k * (x - y)))
  > 
  > 
  > ```
  >
  > $$
  > \hat{a}_{i,j} = \frac{1}{1+e^{-k (P_{i,j} - T_{i,j})}}
  > $$
  >
  > 
  
- https://github.com/MhLiao/DB/issues/100  **官方配置问题**
  
  - https://github.com/MhLiao/DB/issues/49 **训练时间问题**
  
    > ```
    > ear author, Could you give me the information about your training time and your computing resource?
    > I found it cost about 50min with 4 Titian Xp GPUs to train one epoch. Is it normal ?
    > ```
    >
    > ```
    > The training time of one epoch is highly related to the number of training images. If the number of your training images is much larger than 1000, you should shorten the training epochs. Take Total-Text (about 1200 images) as an example, It takes about 1~2 minutes for one epoch (78 iters) with Titan Xp GPUs. Thus, the training speed is about 1~2 seconds/iter.
    > ```
  
  - https://github.com/open-mmlab/mmocr/tree/main/configs/textdet/dbnet **直接可用**
  
- https://www.cnblogs.com/yanghailin/p/12337543.html 官方实现配置过程
  
  > make_border_map.py这个是为了做threshold的标签的
  >
  > ```
  > # DB/structure/model.py 改一下
  > class BasicModel(nn.Module):
  >     def __init__(self, args):
  >         nn.Module.__init__(self)
  > 
  >         backboneName = 'deformable_resnet18' # args['backbone']
  >         backboneFunc = getattr(backbones, backboneName)
  >         backboneInstance = backboneFunc(**args.get('backbone_args', {}))
  >         self.backbone = backboneInstance
  > 
  >         decoderName = 'SegDetector' # args['decoder']
  >         decoderFunc = getattr(decoders, decoderName)
  >         decoderInstance = decoderFunc(**args.get('decoder_args', {}))
  >         self.decoder = decoderInstance
  > 
  >         # self.backbone = getattr(backbones, args['backbone'])(**args.get('backbone_args', {}))
  >         # self.decoder = getattr(decoders, args['decoder'])(**args.get('decoder_args', {}))
  > ```
  >
  > 
  
  - https://www.cnblogs.com/yanghailin/p/12209685.html 两个都有
  
- https://blog.csdn.net/weixin_43705733/article/details/123347511  **非？官方实现配置过程**
  
- https://github.com/WenmuZhou/DBNet.pytorch
  
  - https://bbs.huaweicloud.com/blogs/345205  **非官方的训练，详细！**
  
- https://lwd3-byt.github.io/2021/07/28/DBNet-%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90-%E5%AE%9E%E8%B7%B5%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE%E5%8F%8A%E8%BF%90%E8%A1%8C/  **DBNet.pytorch实现配置过程**
  
- https://blog.csdn.net/jizhidexiaoming/article/details/124342274  **网络结构大图 损失函数详细**
  
  >
  > > icdar2015 文本检测数据集
  > > 标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text
  > >
  > > 其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。 
  > >
  > > \#\#\# 表示text难以辨认。
  > >
  > > 
  > >
  > > DBNet 对每个像素点进行自适应二值化，二值化的阈值由网络学习得到，彻底将二值化这一步骤加入到网络里一起训练，这样最终的输出图对于阈值就会非常鲁棒。
  > >
  > > DB(Differentiable Binarization) **可微分二值化**[u](https://zhuanlan.zhihu.com/p/365227183)
  > >
  > > ![image-20220429172656953](深入理解神经网络：从逻辑回归到CNN.assets/image-20220429172656953.png)
  > >
  > > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220510103251330.png" alt="image-20220510103251330" style="zoom:25%;" />
  > > $$
  > > \text{人工标记的原图}
  > > $$
  > >
  > >
  > > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220510102129945.png" alt="image-20220510102129945" style="zoom: 25%;" />
  > > $$
  > > \text{多边形}
  > > $$
  > >
  > > $$
  > > G=\{S_k\}^n_{k=1} \ \ \text{，每一个多边形用线段的集合表示, 这里 } n=14 \\
  > > 注：多边形有几个点就有几条边，因为它必须是闭合的，至少三个点；\\ 
  > > 第一个点增加0条边，最后一个点增加2条边，所以平均起来就是一点一边。
  > > $$
  > >
  > > 
  > >
  > > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220510103751165.png" alt="image-20220510103751165" style="zoom:25%;" />
  > > $$
  > > \text{概率图标签}
  > > $$
  > >
  > > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220510103953497.png" alt="image-20220510103953497" style="zoom:25%;" />
  > > $$
  > > \text{阈值图标签}
  > > $$
  > >
> > 使用**概率图标签**$G_s$的计算过程中**得到的偏移量D**进行**多边形扩充**，然后计算$G_d$与$G_s$之间的**像素到原始框最近边的归一化距离**，最后将其中的值进行缩放，得到的就是最终的**阈值图标签**$G_d$。 
> >
> > backbone of **ResNet-18**, 主干网络是ResNet网络，后接**FPN**，再对不同尺寸的特征图进行concat，最终由两个不同的输出头给出结果。
> >
> > 整个流程如下 https://zhuanlan.zhihu.com/p/368035566
> >
> > DB\decoders\seg_detector.py  上采样的代码在这里
> >
> > 图像经过FPN网络结构，得到四个特征图，分别为1/4,1/8,1/16,1/32大小；
> > 将四个特征图分别上采样为1/4大小，再concat，得到特征图F
> > 由F得到 probability map (P) 和 threshold map (T)
> > 通过P、T计算（通过可微分二值化DB，下文介绍） approximate binary map（ 近似binary map [公式] ）
> > 对于每个网络，一定要区分训练和推理阶段的不同：
> >
> > 训练阶段：对P、T、B进行监督训练，P和B是用的相同的监督信号（label）；
> > 推理阶段：通过P或B就可以得到文本框。
> >
> > ```
> > # log.py 修改
> > 	if not os.path.exists(self.log_dir):
> >             # os.symlink(storage_dir, self.log_dir)
> >             os.symlink(r'D:\pytorch\DB\outputs\workspace\DB', r'D:\pytorch\DB\workspace')
> > ```
> >
> > 

- https://lwd3-byt.github.io/2021/07/28/DBNet-%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90-%E5%AE%9E%E8%B7%B5%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE%E5%8F%8A%E8%BF%90%E8%A1%8C/
> OCR-(DB+CRNN)-代码分析-实践环境配置及运行 **非常详细**

- https://github.com/open-mmlab/mmocr/blob/main/README_zh-CN.md
> 直接用的工具箱（文本检测、识别）

- https://github.com/qdd1234/Source-code-for-terminal-representation
> DBNet 车牌识别  大作业

- https://zhuanlan.zhihu.com/p/94677957
> DBNet阅读笔记

- https://blog.csdn.net/DU_YULIN/article/details/118460206
  
> DBnet源码解析
>
> ICDAR2015 数据集
>
> <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220601082231209.png" alt="image-20220601082231209" style="zoom:50%;" />
>
> ![image-20220601082133262](深入理解神经网络：从逻辑回归到CNN.assets/image-20220601082133262.png)
>
> 其中A为红色实线区域面积，L为红色实线区域周长，r表示收缩率， 一般r=0.4。
>
> <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220923181248445.png" alt="image-20220923181248445" style="zoom:50%;" />
>
> ```python
> 		# 生成概率图的类 data\processes\make_seg_detection_data.py
> 		class MakeSegDetectionData(DataProcess):
> 			...
> 			def process(self, data):
> 				...
> 				# polygon为红色实线区域，由n个顶点组成，每个顶点有x,y两个坐标值
> 				# 这里应用shapely.geometry.Polygon统计任意形状四边形面积和周长
> 				polygon_shape = Polygon(polygon)
> 
> 				# distance 即为上述公式（6）中 D的计算过程
>  distance = polygon_shape.area * \
>      (1 - np.power(self.shrink_ratio, 2)) / polygon_shape.length
>  subject = [tuple(l) for l in polygons[i]]
> 
> 				# 应用pyclipper.PyclipperOffset进行红色实线区域收缩
>  padding = pyclipper.PyclipperOffset()
>  padding.AddPath(subject, pyclipper.JT_ROUND,
>                  pyclipper.ET_CLOSEDPOLYGON)
>  shrinked = padding.Execute(-distance)
>  if shrinked == []:
>      cv2.fillPoly(mask, polygon.astype(
>          np.int32)[np.newaxis, :, :], 0)
>      ignore_tags[i] = True
>      continue
> 
> 				# shrinded即为收缩后的蓝色虚线区域
>  shrinked = np.array(shrinked[0]).reshape(-1, 2)
>  # 将概率图像中蓝色实线区域值设置为1，其它区域默认值为0
>  cv2.fillPoly(gt[0], [shrinked.astype(np.int32)], 1)
> 
> 
> 数据加载
> /root/DB/data/image_dataset.py
> class ImageDataset(data.Dataset, Configurable):
> 	self.data_dir = ['./datasets/TD_TR/TD500/', './datasets/TD_TR/TR400/']
> 	self.data_list = ['./datasets/TD_TR/TD500/train_list.txt', './datasets/TD_TR/TR400/train_list.txt']
> 
>  # 所有的数据处理都在这里
>  def __getitem__(self, index, retry=0):
>      if self.processes is not None:
>          for data_process in self.processes:
>              data = data_process(data)
> 				# 第一步做数据增强，随机透视变换、改变大小、什么的
>              	 
>              
> 
> 读人工标记(图片文本区域的多边形)
> /root/DB/data/image_dataset.py
> gt_paths=['./datasets/TD_TR/TD500//train_gts/IMG_0855.JPG.txt',
> './datasets/TD_TR/TD500//train_gts/IMG_1835.JPG.txt',
> './datasets/TD_TR/TD500//train_gts/IMG_2113.JPG.txt']
> 
> def load_ann(self):
> res = []
> for gt in self.gt_paths:
>    lines = []
>    reader = open(gt, 'r').readlines()
>    for line in reader:
>        item = {}
>        parts = line.strip().split(',')
>        label = parts[-1]
>        if 'TD' in self.data_dir[0] and label == '1':
>            label = '###'
>        line = [i.strip('\ufeff').strip('\xef\xbb\xbf') for i in parts]
>        if 'icdar' in self.data_dir[0]:
>            poly = np.array(list(map(float, line[:8]))).reshape((-1, 2)).tolist()
>        else:
>            num_points = math.floor((len(line) - 1) / 2) * 2
>            poly = np.array(list(map(float, line[:num_points]))).reshape((-1, 2)).tolist()
>        item['poly'] = poly
>        item['text'] = label
>        lines.append(item)
>    res.append(lines)
> return res
> 
> 
> 
> # 经过了数据增强
> # /root/DB/data/processes/augment_data.py
> 
> aug = self.augmenter.to_deterministic()
> 
> 	data['image'] = aug.augment_image(image)
> 
> import imgaug.augmenters as iaa
> 
> 	iaa.Fliplr(0.5)
> 
> imgaug.augmenters.geometric.Affine  'rotate':[-10, 10]
> 
> 	['Fliplr', 0.5]
> 	{'cls': 'Affine', 'rotate': [-10, 10]}
> 	['Resize', [0.5, 3.0]]
> 
> 
> # 可视化
> basename = os.path.basename(filename)
> cv2.imwrite(f'/root/{basename}_shrinked.jpg', gt[0] * 255) # 数值是 0~1.0 转灰度图
> 
> 
> 第一张图： 是随机的，没用
> DB\data\data_loader.py  这里控制是否随机加载数据 改 shuffle=False 不随机
> 	            torch.utils.data.DataLoader.__init__(
>        self, self.dataset,
>        batch_size=self.batch_size, num_workers=self.num_workers,
>        drop_last=self.drop_last, shuffle=self.shuffle,
>        pin_memory=True, collate_fn=self.collect_fn,
>        worker_init_fn=default_worker_init_fn)
> 
> 
> './datasets/TD_TR/TR400//train_images/IMG_0117.jpg'
> 
> 
> Syntax: cv2.fillpoly(Image,End_Points,Color)
> Parameter:
> Image: This is image on which we want draw filled polygon
> End_Points: Points of polygon(for triangle 3 end points, for rectangle 4 end points will be there)
> Color: It specifies the color of polygon   
> 
> points = np.array([[160, 130], [350, 130], [250, 300]])
> cv2.fillPoly(img, pts=[points], color=(255, 0, 0))
> 
> ```
>
> ```
> # 可视化
> 
> 
> 
> 
> 
> 
> 		fuse = torch.cat((p5, p4, p3, p2), 1)
> # this is the pred module, not binarization module; 
> # We do not correct the name due to the trained model.
> binary = self.binarize(fuse)
> 
> # 可视化--------
> binary_img = binary[0].permute((1, 2, 0)).cpu().data.numpy() * 255
> thresh_img = self.thresh(fuse)[0].permute((1, 2, 0)).cpu().data.numpy() * 255
> binary_img = binary_img.astype(np.uint8)
> thresh_img = thresh_img.astype(np.uint8)
> cv2.imwrite('bin.bmp', binary_img)
> binary_color_map = cv2.applyColorMap(binary_img, cv2.COLORMAP_JET)
> cv2.imwrite('cm.bmp', binary_color_map)
> 
> cv2.imwrite('thresh.bmp',thresh_img)
> thresh_color_map=cv2.applyColorMap(thresh_img, cv2.COLORMAP_JET)
> cv2.imwrite('color_thresh.bmp',thresh_color_map)
> # ------------------
> ```
>
> 

- https://zhuanlan.zhihu.com/p/368035566
  
> **手把手教你学DBNet**

- https://zhuanlan.zhihu.com/p/88645033

  > CTC算法详解

- https://github.com/MhLiao/DB/issues/223

  > **Running the code on Google Colab**

- https://blog.csdn.net/weixin_43705733/article/details/123347511

  > **DBNet训练过程笔记（超详细)** 实战级

- https://blog.csdn.net/fxwfxw7037681/article/details/112943956

  > 在实际使用中，可能存在的问题及调整
  >
  > 在config/det_DB_resnet50.yaml的postprocess中有三个参数是要根据实际来调整的，**thresh，box_thresh和unclip_ratio**。
  >
  > **发现框太大或太小，调整unclip_ratio**。
  > 发现漏检，可能是由于你的阈值设定的太高了，调整thresh和box_thresh，比如thresh=0.2，box_thresh=0.3，但是thresh变小后，unclip_ratio也要相应变小，因为thresh变小，必然导致probability map变大，所以向外扩的比例要调下，不然框就太大了。

- https://blog.csdn.net/qq_41131535/article/details/120174542

  > 数据生成很详细



##### Vatti's clipping algorithm 算法

- https://github.com/fonttools/pyclipper

  > 缩放多边形的库

  - http://www.angusj.com/delphi/clipper.php



#### FCENet

[FCENet](https://zhuanlan.zhihu.com/p/375231118)



#### mmocr

- https://zhuanlan.zhihu.com/p/484637638

  > 初尝mmocr，使用mmocr训练自定义数据集

- https://mmocr.readthedocs.io/zh_CN/latest/demo.html#id2

  > 官方文档

- https://github.com/open-mmlab/mmocr/issues/152  ICDAR 2015

- https://github.com/open-mmlab/mmocr/issues/17 ICDAR2015 数据集

  > 训练DBNet
  >
  > ICDAR2015 数据集  可以试着跑这个数据集





### 目标检测

tood detector 算法



### pytorch 实现数字识别



```
# https://zh.d2l.ai/chapter_deep-learning-basics/softmax-regression.html
动手学深度学习 -> softmax回归

其实衡量两个概率分布的差距，应该用KL散度更合理，但是在真实概率标签为one-hot的时候（即狗=0，猫=1）时，最小化KL散度等价于最小化交叉熵。
因为有如下公式：
假设p为真实分布(狗=0，猫=1), q为模型预测的分布（狗=0.4，猫=0.6）
KL(p||q) = 交叉熵H(p, q) - 熵H( p)
而由于后者 熵H( p)在one-hot定义时值恒为0，所以KL(q||p) = 交叉熵H(q,p) , 最小化KL相当于最小化熵。

# https://blog.csdn.net/Runner_of_nku/article/details/88815894
这个数据集的分布也是很有趣的，0-499都是0，然后500-999是1...一直到9，都是每500个一聚，这样也方便我们从中选取训练集和预测集
```



```
https://github.com/amitrajitbose/handwritten-digit-recognition
doc\lang\programming\pytorch\数字识别\handwritten_digit_recognition_GPU.ipynb


https://zhuanlan.zhihu.com/p/36233589
	tensor 很详细

```



```python
# [-1, 1] 的小数规范到[0, 255]
import cv2
a = ((images[0].numpy().squeeze() + 1) / 2) * 255
b = np.rint(a) # 小数变成它最接近的整数
plt.imshow(b, cmap='gray_r')
b
```





```python
输出[ 0.5 1. 1. ]，即原像素值除以102，超出1的变为1
如果一个数组里面有负数，现在想调整到正数，就使用out_range参数。如：

import numpy as np
from skimage import exposure
image = np.array([-10, 0, 10], dtype=np.int8)
mat=exposure.rescale_intensity(image, out_range=(0, 127))
print(mat)
```





```
 
 在看https://zhuanlan.zhihu.com/p/28057434这篇文章的代码时， 没明白为啥能把图片数据 转成有负数的数据.. batch_images = batch_images*2 -1 即结果在[-1,1]区间   
图片的像素 整数应该在[0,255]之间，浮点数在[0,1]之间，负数怎么能表示像素呢，负数是如何表示像素的呢?......

后来才知道，是imshow 默认做了标准化。 vmin, vmax 或noraml参数可以调节这个最大最小区间。 实际显示时，不会用到负值。

可以看到前两张图的分布是一样的，都是均匀的。由于标准化方式的不一致， 第三张图黑点更多，第四张图白点更多。
 
 
 最近在做Android上的图像处理，在Android上直接对像素操作，居然出现了意想不到的事情。Bitmap类getPixel方法获取的像素值全部是负的，本来应该是黑色的，也就是0的，全部变成了-16777216，很是奇怪。但是仔细研究研究这个16777216又比较特殊，因为16777216=256*256*256，刚好是RGB三种颜色分量最大值的乘积。其实这个值的不精确表示，我们很熟悉，手机广告中宣传屏幕的时候经常会说支持1600万色，诺基亚最喜欢这样宣传了。-16777216的补码十六进制表示就是#FF000000，刚好是加了alpha通道的不透明黑色。查了Android 的文档才知道，Android中颜色由四个分量组成，而我想当然的YY成了RGB三个分量，忽略了A这个分量，默认的A值是255。所以无A通道的图像素最高位总是1，而JAVA中又没有无符号整型，返回一个32位的int型变量，就这样出现了我遇到的各种负数。
```



### 图片相似

[video-subtitle-extractor](https://github.com/YaoFANGUK/video-subtitle-extractor)

[imagehash 各种算法都有](https://github.com/JohannesBuchner/imagehash)

[ImageHash C#实现](https://github.com/coenm/ImageHash)

[image_similarity](https://github.com/oke-aditya/image_similarity)



#### 图片搜索

[必看 openai embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

[weaviate 图像向量搜索](https://weaviate.io/blog/how-to-build-an-image-search-application-with-weaviate)



### 完全解析RNN, Seq2Seq, Attention注意力机制



https://zhuanlan.zhihu.com/p/141799551 

完全解析RNN, Seq2Seq, Attention注意力机制
https://zhuanlan.zhihu.com/p/51383402



###  三维重建 &&  Numpy && OpenCV in C# && 数据增强



```


# 三维重建



​```
https://zhuanlan.zhihu.com/p/141799551


完全解析RNN, Seq2Seq, Attention注意力机制
https://zhuanlan.zhihu.com/p/51383402
​```





# Numpy && OpenCV in C#



​```
https://www.gitmemory.com/issue/shimat/opencvsharp/1093/739471217
https://www.youtube.com/watch?v=ZZ5M7Q5ZWX4
​```



## 验证码识别（含数据增强）



​```
https://github.com/pprp/captcha.Pytorch
​```
```







### 手写数字识别



```
as title shows,datasat is MINST. but i meet the problem that the output of model is null.
the code as follows:

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.conv1=torch.nn.Sequential(
            torch.nn.Conv2d(1,64,kernel_size=3,stride=1,padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(64,128,kernel_size=3,stride=1,padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(stride=2,kernel_size=2))
        self.dense=torch.nn.Sequential(
            torch.nn.Linear(14*14*128,1024),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(1024,10))
    def forward(self,x):
            x=self.conv1(x)
            x=x.view(-1,14*14*128)
            x=self.dense(x)
            return x
model=Model()
print(model)


```





### Attention 手写数字识别



```python
https://blog.csdn.net/zgj_gutou/article/details/86558905

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
This code is a modified version of the code from this link:
https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/3_NeuralNetworks/recurrent_network.py
His code is a very good one for RNN beginners. Feel free to check it out.
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# set random seed for comparing the two result calculations
tf.set_random_seed(1)

# this is data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# hyperparameters
lr = 0.001
training_iters = 100000
# batch_size = 128
batch_size = 256

n_inputs = 28   # MNIST data input (img shape: 28*28)
n_steps = 28    # time steps
n_hidden_units = 128   # neurons in hidden layer
n_classes = 10      # MNIST classes (0-9 digits)
attention_size = 50

# tf Graph input
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])

# Define weights
weights = {   # 对权重进行随机初始化
    # (28, 128)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    # (128, 10)
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}
biases = {   # 对偏差进行随机初始化
    # (128, )
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    # (10, )
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}

def RNN(X, weights, biases):
    # transpose the inputs shape from
    # X ==> (256 batch * 28 steps, 28 inputs)
    X = tf.reshape(X, [-1, n_inputs])

    # into hidden
    # X_in = (256 batch * 28 steps, 128 hidden)
    X_in = tf.matmul(X, weights['in']) + biases['in']   # 这里的维度是（256*28,128)，输入先经过一个线性变化
    # X_in ==> (256 batch, 28 steps, 128 hidden)
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])   # 这里的维度是（256,28,128）

    # cell
    cell = tf.contrib.rnn.BasicLSTMCell(n_hidden_units)  # 一个lstm单元的输入是向量，所以有这么多隐藏单元n_hidden_units
    # lstm cell is divided into two parts (c_state, h_state)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)   # 初始状态的维度跟batch_size和隐藏单元个数有关，这里shape=(256, 128)

    outputs, final_state = tf.nn.dynamic_rnn(cell, X_in, initial_state=init_state, time_major=False)

    # unpack to list [(batch, outputs)..] * steps
    # 这里的outputs是[batch_size, max_time, cell.output_size(即hidden_units)]的形式，现在要取最后一个时间的outputs,所以要调换一下max_time和batch_size，这样就可以直接用outputs[-1]来得到最后一个的输出
    outputs = tf.unstack(tf.transpose(outputs, [1,0,2]))  # tf.unstack默认是按行分解。
    print("outputs:",outputs)

    attention_w = tf.Variable(tf.truncated_normal([n_hidden_units, attention_size], stddev=0.1), name='attention_w')
    attention_b = tf.Variable(tf.constant(0.1, shape=[attention_size]), name='attention_b')
    u_list = []
    for t in range(n_steps):
        u_t = tf.tanh(tf.matmul(outputs[t], attention_w) + attention_b)  # u_t的shape=(256,50)，output[t]表示每个时间的输出，如output[-1]表示最后一个时间的输出
        u_list.append(u_t)  # 这个u_list包含了n_steps个元素，每个元素的shape都是(256,50)
    print("u_list:",u_list)
    u_w = tf.Variable(tf.truncated_normal([attention_size, 1], stddev=0.1), name='attention_uw')
    attn_z = []
    for t in range(n_steps):
        z_t = tf.matmul(u_list[t], u_w)  # z_t的shape=(256,1),这一步线性变换其实是为了改变维度大小用的，去掉了50这个数，变成了1
        attn_z.append(z_t)   # 这个attn_z包含了28个元素，每个元素的shape都是(256, 1)
    # transform to batch_size * sequence_length
    print("attn_z:",attn_z)
    attn_zconcat = tf.concat(attn_z, axis=1)   # shape=(256,28),256是batch_size,表示样本数量
    print("attn_zconcat:",attn_zconcat)
    alpha = tf.nn.softmax(attn_zconcat)   # 得到各个权重(小数）
    # transform to sequence_length * batch_size * 1 , same rank as outputs
    alpha_trans = tf.reshape(tf.transpose(alpha, [1, 0]), [n_steps, -1, 1])  # (28,256,1)
    print("alpha_trans:",alpha_trans)
    print("outputs:",outputs)
    results = tf.reduce_sum(outputs * alpha_trans, 0)  # results的shape=(256,128)
    print("results:",results)

    fc_w = tf.Variable(tf.truncated_normal([n_hidden_units, n_classes], stddev=0.1), name='fc_w')
    fc_b = tf.Variable(tf.zeros([n_classes]), name='fc_b')
    final_output =  tf.matmul(results, fc_w) + fc_b  # shape=(256,10)

    return final_output

pred = RNN(x, weights, biases)  # 此时x还没有数值，后面用feed_dict输入
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))  # 此时y还没有数值，后面用feed_dict输入
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 0
    while step * batch_size < training_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        # print(len(batch_xs))
        # print(len(batch_xs[0]))
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])  # 把[batch_size,784]变形为[batch_size,28,28],这样才符合x的维度
        sess.run(train_op, feed_dict={x: batch_xs,y: batch_ys,})
        if step % 20 == 0:
            batch_xs, batch_ys = mnist.test.next_batch(batch_size)
            # 取batch_size大小的测试集，因为初始状态跟batch_size有关，所以这里取batch_size大小的测试集数据，否则会报错。也可以把batch_size作为一个参数来传递
            batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])
            print("time:",step," accuracy:",sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys,}))
        step += 1


```



### 验证码识别（含数据增强）



```
https://github.com/pprp/captcha.Pytorch

```



### Attention 讲原理



```

https://blog.csdn.net/zshluckydogs/article/details/88912273

摘要：
针对NLP领域的问题，谷歌创造性的提出了Attention机制，优点是可以获得较长的依赖，捕捉局部与全局的关系，并且每一步的计算都是独立的所以可以很好的并行加速，缺点是抛弃了序列的语序顺序，在NLP中是一个致命的缺点，但是研究人员通过加入position-embedding可以解决这个问题。简单点说，attention就是高端的词袋模型（BOW），给一个词根据上下文的关系赋予不同的权重，然后用这个向量表示这个词。

网络结构及其实现：
本文CRNN+Attention 的网络架构，是在CRNN网络的输出层后面加上一层attention机制，详细的说就是（这里用GRU代替LSTM）CNN+GRU（一层，hidden_units = 1024），把GRU网络的输出作为 encoder的输出，然后对其做attention得到attention输出s，假设网络上一时刻的输出 y1, 则y2时刻的输出由y1和s共同作用得到，对y1做embedding然后把（embediing(y1)+s)输入到 GRU网络中，通过softmax得到输出，在进行label转换，即可得到最后的输出序列。

input: x  gray-scale image
 
net = cnn + gru
 
Encoder = net(x)
 
Attention = BahdanauAttention(features, hidden_units)  attention的一种实现方式，更多详情可以Google，其中features是Encoder的输出，hidden_units 与gru的对齐。
 
y0 = s   假设y0时刻输出是 s, s 就代表英文字母 s
 
 
 
y1_input = embedding(s) + Attention  y1时刻的输入
 
y2 = softmax(gru(y1_input)) 对y1时刻的输入进行embedding然后输入到gru层做soft Max得到y2输出。
 
 
y2 --> e  查lable表得到标签。
大概就是上面这个过程，如果你对CRNN和Attention有一定的了解，这个实质就是对二者的一个结合而已，没有什么特别难以理解的地方。另外，本文没有提到Attention的计算方式，这个可以参考：http://jalammar.github.io/illustrated-transformer/，这篇文章讲解的非常细致，不过是英文的。

对于代码部分，只要你自己清楚的知道所设计的网络结构，根据这个去查需要的工具即可，无非是选择框架，caffe、tensorflow、keras、pytorch等，重点是你必须很清楚的知道网络是怎样的架构，然后去找相应的函数构造出来这个架构即可。所以对于研究算法的同学，写代码不是第一要务，理解算法本身才是。

参考代码：https://github.com/koibiki/CRNN-ATTENTION

我是在这个代码的基础上加了自己的东西，等有时间上传链接吧。补充，这种Attention机制的网络，在进行长文本的识别时效果比较差，而且网络的robust非常差，用训练好的CRNN网络和这个ATTENTION网络对同样的样本（来自于真实扫描版PDF截图）进行识别时两个网络的表现都很差，但是CRNN的效果却是远远优于ATTENTION的。但是Attention堆叠起来的Transformer在机器翻译任务上的表现优于传统的基于LSTM（GRU）的encoder-decoder架构，这得益于attention能够捕捉更长的时间依赖，这是机器翻领域最影响性能的因素，尤其大量的翻译样本都是长句。但是对OCR这个跟图像有着密切关联的领域，在进行Attention时由于只考虑了词间的关联性，可能会破坏词的一些可以帮助识别的视觉特征，所以性能不如经典的CRNN。

```



### 一文读懂CRNN+CTC文字识别



```
# https://zhuanlan.zhihu.com/p/43534801

```



### Subtitle extract

- https://github.com/YaoFANGUK/video-subtitle-extractor



doc\lang\programming\Python 3  Summary.md  看在这里，Extract Video Subtitle 这一节



### 别人是怎么扫书的

[别人是怎么扫书的](https://www.pdawiki.com/forum/forum.php?mod=viewthread&tid=48701&extra=)



## 词嵌入



```
Word Embedding 词嵌入
Word2Vec 
Embedding层 将词ID映射为向量
one hot 独热，是最原始的用来表示字、词的方式（每一个词分配一个基向量），有多少词就是多少维空间
```

### 为将 one-hot这个很长的向量压缩到低维


- https://samaelchen.github.io/machine_learning_step13/
  - 台大李宏毅机器学习——词向量

在很古老很古老的时候，如果我们要用向量表示一个单词，只能用一个one-hot的方法来表示，也就是一串很长很长的0-1向量。这个很长很长的向量长度跟单词的数量一样多。比如说，我们有10w个英文单词，那么这个向量就有10w维，然后给每个词在这个向量里面找个位置标记为1，其他位置标记为0，这样就得到了最原始的词向量。

但是这个向量不用想都知道，一个很突出的问题，太大了。另外有一个很大的问题就是这样的表示，没有办法表达出词语的含义。所以**word embedding做的事情就是将 one-hot这个很长很长的向量，压缩到低维。比如现在最常用的100-200维之间**。



### 为了从上下文中理解单词的意思

那word embedding实际上可以做到**通过读海量的文档内容，然后理解单词的意思**。比如 The cat sat on the pat和The dog sat on the pat这两句话，cat和dog是接近的。

那做到word embedding有两种做法。第一种是计算词语的共现次数，另一种是通过上下文的方法去做预测。



### cbow 用上下文猜中间的词 skip-gram 中间的词猜上下文



训练模型的方法一般有两种，一种是cbow，一种是skip-gram。cbow就是用上下文猜中间的词，skip-gram是按照中间的词猜上下文





### pytorch 实现cbow

- https://github.com/FraLotito/pytorch-continuous-bag-of-words
  - https://nathanrooy.github.io/posts/2018-03-22/word2vec-from-scratch-with-python-and-numpy/
    - numpy 实现
  - https://jaketae.github.io/study/word2vec/
    - numpy 实现2
- https://blog.csdn.net/weixin_43646592/article/details/119180298
  - 基于Pytorch的torch.nn.embedding()实现词嵌入层

#### NLLloss 损失函数

> doc\lang\programming\pytorch\异或\OR_torch_version0.py
>
> criterion = nn.MSELoss() #nn.NLLLoss()  # https://zhuanlan.zhihu.com/p/264366034
>
>  \# NLLloss 和交叉熵一样只适用于分类任务， NLLLoss是基于softmax，softmax得到结果向量的概率分布，是离散值。回归任务建议MSE或MAE等损失函数
>
>  \# 否则提示多个target报错



### 一切要从one hot说起

- https://spaces.ac.cn/archives/4122

one hot 独热，是最原始的用来表示字、词的方式（每一个字分配一个基向量），有多少字就是多少维空间
$$
\begin{array}{c|c}\hline\text{科} & [1, 0, 0, 0, 0, 0]\\ 
\text{学} & [0, 1, 0, 0, 0, 0]\\ 
\text{空} & [0, 0, 1, 0, 0, 0]\\ 
\text{间} & [0, 0, 0, 1, 0, 0]\\ 
\text{不} & [0, 0, 0, 0, 1, 0]\\ 
\text{错} & [0, 0, 0, 0, 0, 1]\\ 
\hline 
\end{array}
$$


“科学”这个词，的矩阵表示
$$
\begin{pmatrix}1 & 0 & 0 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 & 0 & 0 \end{pmatrix}
$$
one hot 矩阵庞大，但是好算


$$
\begin{pmatrix}1 & 0 & 0 & 0 & 0 & 0\\ 
0 & 1 & 0 & 0 & 0 & 0 \end{pmatrix}\begin{pmatrix}w_{11} & w_{12} & w_{13}\\ 
w_{21} & w_{22} & w_{23}\\ 
w_{31} & w_{32} & w_{33}\\ 
w_{41} & w_{42} & w_{43}\\ 
w_{51} & w_{52} & w_{53}\\ 
w_{61} & w_{62} & w_{63}\end{pmatrix}=\begin{pmatrix}w_{11} & w_{12} & w_{13}\\ 
w_{21} & w_{22} & w_{23}\end{pmatrix}
$$


这是一个以2x6的one hot矩阵的为输入、中间层节点数为3的**全连接神经网络层(DNN)**

- DNN 是最朴素的神经网络，它的网络参数最多，计算量最大



Embedding层就是以one hot为输入、中间层节点为字向量维数的全连接层！而这个全连接层的参数，就是一个“字向量表”



one hot型的矩阵运算简化为了查表操作



**用全连接层的参数作为字、词的表示**，从而得到了字、词向量，最后还发现了一些有趣的性质，比如向量的夹角余弦能够在某种程度上表示字、词的相似度。

对了，有人诟病，Word2Vec（**CBOW, The Continuous Bag-of-Words Model 连续词袋模型**）只是一个三层的模型，算不上“深度”学习，事实上，算上one hot的全连接层，就有4层了，也基本说得上小小的深度模型了。



- http://www.51blog.com/?p=12663
  
  - 基础讲得好
- https://zhuanlan.zhihu.com/p/68339909
  
  - 李宏毅 CBOW
- https://blog.csdn.net/weixin_29141505/article/details/112018445
  
- cbow word2vec 损失_谷歌深度学习公开课任务 5: Word2Vec&CBOW
  
- https://zhuanlan.zhihu.com/p/214127337
  
- 负采样采的究竟是什么  知识图谱的嵌入  knowledge graph（KG）
  
- https://aws.amazon.com/cn/blogs/china/training-knowledge-graph-embeddings-at-scale-with-the-deep-graph-library/

  - 使用 Deep Graph Library 训练知识图谱嵌入

    > 今天，我们很高兴与大家分享**知识图谱嵌入库（DGL-KE）**，这是一套以深度图谱库（[Deep Graph Library](https://www.dgl.ai/)，DGL）为基础构建而成的知识图谱（KG）嵌入库。**深度图谱库（DGL）**是一套易于使用、性能出色且可扩展的Python库，主要用于实现对图谱的深度学习。现在，您可以为包含数十亿个节点与边的大型知识图谱库创建嵌入，且[执行速度是其他同类手段的2到5倍](https://arxiv.org/abs/2004.08532)。
    >
    > 例如，DGL-KE在“**药物再利用知识图谱（DRKG）**”之上创建嵌入，旨在显示哪些已经批准上市的药物能够用于对抗COVID-19。这些嵌入可用于预测药物治疗疾病的可能性或药物与疾病相关蛋白质结合的可能性。
    >
    > 在本文中，我们将重点介绍如何使用[Kensho派生维基媒体数据集（KDWD）](https://blog.kensho.com/announcing-the-kensho-derived-wikimedia-dataset-5d1197d72bcf?source=collection_home---2------1-----------------------)**创建知识图谱嵌入**（KGE knowledge graph embeddings）。例如，在自然语言处理（NLP）与信息检索用例当中，大家可以**解析新查询，并将其句法转换为三元组（subject, predicate, object 即主语、谓词、宾语）**。在**将新的三元组添加至KG**之后，则可以**对节点做分类**并根据现有的KGE来**对关系作出推理**，从而**进一步扩充KG中的节点和关系**。您可以**借此指导聊天机器人发现对话意图，并为客户提供正确的FAQ**（常见问题的回答）或提示信息。





### 词向量与Embedding究竟是怎么回事？

- https://spaces.ac.cn/archives/4122
  - 词向量与Embedding究竟是怎么回事？

### 线性代数及其应用——嵌入向量_张觉非


- https://zhuanlan.zhihu.com/p/475086668?utm_source=qzone&utm_medium=social&utm_oi=937649545946140672
  - 线性代数及其应用——嵌入向量



## 中文分词

[MicroTokenizer](https://github.com/howl-anderson/MicroTokenizer) 极好的



## 机器翻译

1. 了解机器翻译的历史和发展：
   - 研究统计机器翻译（SMT）和神经机器翻译（NMT）之间的区别；
   - 了解翻译任务中的评估指标，如 BLEU、METEOR 和 ROUGE 等。
2. 学习神经机器翻译的核心技术：
   - 探索循环神经网络（RNN）、长短时记忆网络（LSTM）和门控循环单元（GRU）等模型；
   - 学习编码器-解码器（Encoder-Decoder）结构；
   - 了解注意力机制（Attention Mechanism）；
   - 研究Transformer模型。

如何生成语言模型的词表

1. 数据预处理：首先，需要对训练语料库进行预处理，包括清洗、分词、去除停用词等。
2. 统计词频：对预处理后的语料库进行词频统计，计算每个词在语料库中出现的次数。
3. 选择词表大小：确定词表的大小，这个值可以根据实际需求和计算资源来设定。较大的词表可以捕捉到更多的词汇，但计算成本也会增加。
4. 选择高频词：根据设定的词表大小，从词频统计结果中选择出现次数最多的单词作为词表的成员。
5. 添加特殊符号：在词表中添加一些特殊符号，如未知词（<UNK>）、句子起始（<SOS>）、句子结束（<EOS>）和填充符号（<PAD>）等，以处理特殊情况。
6. 生成词表：将选定的单词和特殊符号组成词表。词表可以是一个列表，也可以是一个字典，用于在训练和推理过程中将单词映射到相应的索引。

词表生成完成后，可以用于构建和训练自然语言处理模型。



### 语料

- https://www.linggle.com/
  
> 短语搜索  

- 清华HCI Lab 易搜搭ESODA
> http://www.esoda.org/

- https://opus.nlpl.eu/

  > 多国语言

- https://getyarn.io/

  > 电影


- https://xiaosheng.run/2022/03/24/transformers-note-7.html

  > Hugging Face 的 Transformers 库快速入门（七）：翻译任务
  - https://xiaosheng.run/2021/12/08/transformers-note-1.html
    
    > Hugging Face 的 Transformers 库快速入门（一）：开箱即用的 pipelines

- https://github.com/VictorZhang2014/free-google-translate
  
  >  google 免费翻译
  
- https://github.com/argosopentech/argos-translate

  - OpenNMT离线翻译

    > pip3 install argostranslategui

- https://opus.nlpl.eu/ [2](https://github.com/brightmart/nlp_chinese_corpus)

  - 平行语料

- https://colab.research.google.com/drive/1YzHT4av2SPXI_CzpX3mF9ImFv-V39n4D?usp=sharing
- https://developer.aliyun.com/article/177761?spm=5176.24320532.content1.1.5cfd3eeawKBNHD
- https://github.com/laubonghaudoi/ai_mt
  
  - OpenNMT中英

> 哈佛大学机器翻译开源项目 OpenNMT的工作原理

> ```
> # 安装虚拟环境
> conda create -n nmt pip python=3.7 PyTorch=1.6.0
> conda activate nmt # conda deactivate
> 
> # 删除虚拟环境 
> conda deactivate
> conda env remove -n nmt
> 
> # pip 安装
> pip install OpenNMT-py
> 
> # 下载英译德语料
> https://s3.amazonaws.com/opennmt-trainingdata/toy-ende.tar.gz
> 
> # 新建配置 toy_en_de.yaml
> # toy_en_de.yaml
> ## Where the samples will be written
> save_data: toy-ende/run/example
> ## Where the vocab(s) will be written
> src_vocab: toy-ende/run/example.vocab.src
> tgt_vocab: toy-ende/run/example.vocab.tgt
> # Prevent overwriting existing files in the folder
> overwrite: False
> 
> # Corpus opts:
> data:
>     corpus_1:
>         path_src: toy-ende/src-train.txt
>         path_tgt: toy-ende/tgt-train.txt
>     valid:
>         path_src: toy-ende/src-val.txt
>         path_tgt: toy-ende/tgt-val.txt
> 
> # 生成词典
> onmt_build_vocab -config toy_en_de.yaml -n_sample 10000
> 
> 
> # 在配置追加字典和训练参数 toy_en_de.yaml
> # Vocabulary files that were just created
> src_vocab: toy-ende/run/example.vocab.src
> tgt_vocab: toy-ende/run/example.vocab.tgt
> 
> # Train on a single GPU
> world_size: 1
> gpu_ranks: [0]
> 
> # Where to save the checkpoints
> save_model: toy-ende/run/model
> save_checkpoint_steps: 500
> train_steps: 1000
> valid_steps: 500
> 
> 
> # 开始训练（cpu训练删除这这两行
> world_size: 1
> gpu_ranks: [0]
> ）
> onmt_train -config toy_en_de.yaml
> 
> # 翻译
> onmt_translate -model toy-ende/run/model_step_1000.pt -src toy-ende/src-test.txt -output toy-ende/pred_1000.txt -gpu 0 -verbose
> 
> 
> 
> # 源码安装OpenNMT-py(跑不通demo)
> git clone -b 2.2.0 https://github.com/OpenNMT/OpenNMT-py.git
> cd OpenNMT-py
> git config --global url."https://".insteadOf git://  # fix github error
> pip install -e .   #python setup.py install
> pip install -r requirements.opt.txt
> 
> ```



- https://lofter.me/2020/03/22/%E4%BD%BF%E7%94%A8OpenNMT-py%E8%AE%AD%E7%BB%83%E7%BF%BB%E8%AF%91%E6%A8%A1%E5%9E%8B/

  > 使用OpenNMT-py训练翻译模型



- https://arabelatso.github.io/2021/01/03/OpenNMT-Doc/

  > OpenNMT 2.0.0rc1 使用手册



### 数据集的比例

```
数据划分的方法并没有明确的规定，不过可以参考3个原则： 对于小规模样本集（几万量级），常用的分配比例是60% 训练集、20% 验证集、20% 测试集。 对于大规模样本集（百万级以上），只要验证集和测试集的数量足够即可，例如有100w 条数据，那么留1w 验证集，1w 测试集即可。
```





## 聊天机器人

> https://fancyerii.github.io/2019/02/14/chatbot/  大佬  李理的博客

- 使用PyTorch实现Chatbot



## 语音识别系统

- https://fancyerii.github.io/2019/05/25/dev287x/

  > 微软Edx语音识别课程 大佬

- https://fancyerii.github.io/books/tf-keywords/  大佬

  > 使用Tensorflow识别语音关键词

- https://github.com/nl8590687/ASRT_SpeechRecognition
  
  - 中文语音识别系统



#### 语音识别大佬

- https://xiaodu.io/ctc-explained

  > CTC算法详解之训练篇



## katago

- https://github.com/kinfkong/katago-colab





## Deep leaning with js

- https://www.npmjs.com/package/onnxruntime-web
  - 浏览器里的 deep learning
  - https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js
    - onnxruntime-node
    - onnxruntime-react-native
  - https://juejin.cn/post/7012637429807087652
    - react 实例




## Deep leaning with Rust 

- https://github.com/arrayfire/arrayfire-rust

  - https://github.com/arrayfire/arrayfire

    - 通用GPU CPU 并行运算库

    - arrayfire底层就是cuda搭建，matmul()速度简直上天

    - https://zhuanlan.zhihu.com/p/435908830

      - 深入浅出GPU优化系列：GEMM优化（一）

## Deep learing with C++

- https://github.com/arrayfire/arrayfire/issues/3219



##       

- https://able.bio/haixuanTao/deep-learning-in-rust-with-gpu--26c53a7f

> ## My setup
>
> I am using a Hugging Face **tokenizer** and a custom **BERT** Model from Pytorch that I have converted to **ONNX** to be run with [**onnxruntime-rs**](https://github.com/nbigaouette/onnxruntime-rs)**.**
>
> I have tweaked [onnxruntime-rs](https://github.com/nbigaouette/onnxruntime-rs) to do Deep Learning on GPU with CUDA 11 and onnxruntime 1.8 You can check it out on my git: https://github.com/haixuanTao/onnxruntime-rs
>
> Hardware-side, I have a 6 cores/12 threads CPU and a GTX 1050 GPU.



# 自动微分



```
(JVP = Jacobian-vector product) ... Jacobian-vector products (JVPs) 
```



### JAX

- https://github.com/google/jax/issues/2697 **均方误差**

- https://zhuanlan.zhihu.com/p/475234869  **极好的**

- https://www.blogsaays.com/jax-neural-network-example/  XOR 例子

- https://www.radx.in/jax.htm Understanding Autodiff with JAX **计算雅可比**

- https://rogerluo.dev/Brochure.jl/dev/automatic-differentiation/ 实现你自己的自动微分  **julia**

  > 
  >
  > 自动微分的模式有两种：
  >
  > - 前向模式（Forward mode）：适合输入维度<<输出维度
  > - 反向模式（Backward mode/Reverse-mode）: 适合输入维度>>输出维度
  >
  > 在深度学习中，实际上输入的参数x维度往往大于输出y的维度，因此自动微分的计算方法中，反向模式更为常用
  >
  > 
  >
  > 自动微分是jax的核心功能之一，只要记住2个关键点：
  >
  > - **jax.grad只能对标量求导数，因此需要特别注意函数输出的shape**
  > - 进行微分的输入不能是int32类型，除非你加了 allow_int=True
  > - 小心jit的坑 ！
  >
  > 
  >
  > **jax.grad(f)(x) 等于求f(x)在x上的梯度**
  >
  > 
  >
  > **当你函数有多个输入变量时，必须明确对求导的变量的位置（argnums）, 否则默认对第一个变量进行求导。**
  >
  > 
  >
  > ```python3
  > jax.grad(f, argnums=(0,1,))(x, y)  # 表示对第0，第1 个参数进行求导
  > ```
  >
  > 
  >
  > ```python
  > [ lss, grads ] = jax.value_and_grad(loss, argnums=(1,))(X, W, m) # 同时返回损失和梯度
  > ```
  >
  > 
  >
  > **vmap**是向量化/矢量化的操作神器。**将N个具有相同维度的样本X进行堆叠(stack)后，并一次性传递给神经网络，直接得到所有或该batched样本的预测值**。
  >
  > 
  >
  > 无需再考虑batch的这个维度（batch维度在最外层即可），只需要按照无batch的输入形式去编写神经网络
  >
  > 
  >
  > ```python
  > x = jax.random.normal(jax.random.PRNGKey(55), (3, 2)) # 3*2 的随机数
  > ```
  >
  > 
  >
  > vmap有3个最重要的参数：
  >
  > - fun: 代表你需要进行向量化操作的具体函数
  > - in_axes：输入格式为元组，代表fun中每个输入参数中，使用哪一个维度进行向量化
  > - out_axes: 经过fun计算后，每组输出在哪个维度输出
  >
  > 
  >
  > **所以在矩阵运算的时候，其实最后都可以转成我们常见的二维矩阵运算，遵循的原则是：在多维矩阵相乘中，需最后两维满足shape匹配原则，最后两维才是有数据的矩阵，前面的维度只是矩阵的排列而已！**
  >
  
  
  
  

#### 雅克比的乘积注意不！是！矩阵乘法！ 

```python
import math

import jax
import jax.lax as lax
import jax.numpy as jnp
import jax.random as jrandom
import optax  # https://github.com/deepmind/optax

import equinox as eqx


f1 = lambda x : x ** 2

f2 = lambda x : 2 * x

f3 = lambda x : f2( f1(x) )

x = 2.

X = jnp.array( [ [2 , 2] ], jnp.float32 )

( A1, (grad, ) ) = jax.value_and_grad(f1, argnums=(0,))( x )

( A2, (grad2, ) ) = jax.value_and_grad(f2, argnums=(0,))( A1 )

( A3, (grad3, ) ) = jax.value_and_grad(f3, argnums=(0,))( x )


chain = grad2 * grad  # 复合函数求导的链式法则

assert ( chain == grad3 )


A11 = f1(X) # X 是 (1,2)   f1 的输出是 (1,2)  d f1 / d X 是 (1,2,1,2) 
( grad11, ) = jax.jacfwd(f1, argnums=(0,))( X )

A22 = f2(A11)
( grad22, ) = jax.jacfwd(f2, argnums=(0,))( A11 )

A33 = f3(X)
( grad33, ) = jax.jacfwd(f3, argnums=(0,))( X )


chain2 = grad22 * grad11 # 雅克比的乘积，注意不！是！矩阵乘法！ 

assert ( chain2 == grad33 )

a = 1

"""

d f1 = 2 * x

d f2 = 2


d f3 = d f2 ( f1(x)  ) * d f1 ( x )

     = 2 * 2 * x

     = 4 * x

"""
```





#### jacfwd and jacrev

- https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html

- https://github.com/google/jax/issues/2109

  > ```python
  > value, jacobian = value_and_jacfwd(my_func, 0)(x, y)
  > ```

它们功能是一样的，只是效率上有差别，如果生成的 Jacobian 是比较 “高” 的， jacfwd 前向模式比较有优势，如果生成的 Jacobian 是比较 “宽” 的，jacrev 反向模式比较有优势。如果是比较接近方阵，jacfwd 比 jacrev  更优些。



```
# torch
X = torch.tensor([3., 7.], requires_grad=True)
f = lambda x: x[0]**2 + x[1]**2 
jacobian = torch.autograd.functional.jacobian(f, X)
print( jacobian )

# jax
X = jnp.array([3., 7.], dtype=jnp.float32)
f = lambda x: x[0]**2 + x[1]**2 
jacobian = jacrev(f, argnums=(0, ))(X)
print(jacobian)
```





```python
# doc\lang\programming\pytorch\jax\JAX_From_Zero_to_Hero_1.ipynb

from jax import jacfwd, jacrev

f = lambda x, y: x**2 + y**2

# df/dx = 2x
# df/dy = 2y
# J = [df/dx, df/dy]

# d2f/dx = 2
# d2f/dy = 2
# d2f/dxdy = 0
# d2f/dydx = 0
# H = [[d2f/dx, d2f/dxdy], [d2f/dydx, d2f/dy]]

def hessian(f):
    return jit(jacfwd(jacrev(f, argnums=(0, 1)), argnums =(0, 1)))

print(f'Jacobian = {jacrev(f, argnums=(0, 1))(1., 1.)}')
print(f'Full Hessian = {hessian(f)(1., 1.)}')
```



#### value_and_grad

```
( A1, (grad, ) ) = jax.value_and_grad(f1, argnums=(0,))( x ) # 对第 0 参求导
```



```
# jacfwd 没有相应的 value_and_grad
A11 = f1(X)
( grad11, ) = jax.jacfwd(f1, argnums=(0,))( X )
```



#### 矩阵求导术

- 克罗内克积

  - https://baike.baidu.com/item/%E5%85%8B%E7%BD%97%E5%86%85%E5%85%8B%E7%A7%AF/6282573

    > vec(X)表示矩阵X的向量化，它是把X的所有列堆起来所形成的列向量。



- **矩阵求导术(下)** 
- doc\lang\programming\矩阵求导术（下） - 知乎.pdf


<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220823145345647.png" alt="image-20220823145345647" style="zoom:80%;" />



![image-20220816162311376](深入理解神经网络：从逻辑回归到CNN.assets/image-20220816162311376.png)

![image-20220816162431342](深入理解神经网络：从逻辑回归到CNN.assets/image-20220816162431342.png)



 F=AX, A 是m * n 的矩阵，求 F对A的导数。 X是 n\*p,  F 是 m\*p, dF / dA 是 m\*p\*m\*n

$F=AX=IAX$   I 是 m\*m

$vec(dF)=vec(IdAX) = (X^T \otimes I) vec(dA)$



微分与导数的联系
$$
vec(dF) = \frac{\partial F^T}{\partial X}  vec(dX)
$$


$(X^T \otimes I) = \frac{\partial F^T}{\partial A}$ 

$\frac{\partial F}{\partial A} = (X^T \otimes I^T)$   n\*p  x   m\*m ->  n\*m ,  p*m



 如果A是一个m×n的矩阵，而B是一个p×q的矩阵，克罗内克积则是 mp×nq







```
# 
# doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md

import jax
import jax.numpy as jnp
from jax import random, jacrev, vjp

# F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)

# dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I

# dF / dX = I 克罗内克积符号 A^T    dX 形状是 (4*2) ，所以 I 是 (2*2)。单位阵必是方阵

A = jnp.array( [[2,3]] , jnp.float32 )

X = jnp.array( [[1,2],[3,4]] , jnp.float32 )

def f(A, X):
    return jnp.dot( A, X )
F = f( A, X )

I = jnp.eye( 2 )

A_T = jnp.transpose(A)

kr = jax.numpy.kron(I, A_T) # (4*2) 
    # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 2 个元素，参数总共 4 个元素，求导结果总共应该是 8 个元素
        # df_1(x) .. df_n(x) 横向展开， dx 纵向展开

a = 1

# 下面用 jax 自动微分验证

( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
    # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样

a = 1
```



##### 矩阵求导术笔记

- https://hzhu212.github.io/posts/20d9a268/



小写字母如 $x$ 表示标量，粗体小写字母 $\mathbf{x}$ 表示向量，大写字母$A$表示矩阵。向量均为列向量，行向量通转置来表示，如 $\mathbf{a}^T$



导数与微分的联系
$$
\mathrm{d}y = f’(x)\mathrm{d}x = \frac{\mathrm{d}y}{\mathrm{d}x}\mathrm{d}x
$$
即：全微分 $dy$ 是导数 $\frac{\mathrm{d}y}{\mathrm{d}x}$  与微分变量 $dx$ 的积。（**推论1**）



全微分的定义

- https://math.fandom.com/zh/wiki/%E5%85%A8%E5%BE%AE%E5%88%86?variant=zh

$$
 \mathrm{d}f = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}\mathrm{d}x_i 
$$
令 $\boldsymbol{x}^T=[x_1, x_2, x_3, \dots, x_n]$ ，有：
$$
\mathrm{d}f = \frac{\partial f}{\partial \boldsymbol{x}} \cdot \mathrm{d}\boldsymbol{x}
$$
多元函数的全微分 $\mathrm{d}f$ 是导数向量  $\frac{\partial f}{\partial \boldsymbol{x}}$ 与微分变量 $\mathrm{d}\boldsymbol{x}$  的内积。（**推论2**）

> 标量的积完全可以看作向量内积的一种特殊情况，也就是说，推论2可以涵盖推论1。


$$
\mathrm{d}f = \frac{\partial f}{\partial X}\cdot \mathrm{d}X \tag{1}
$$
即：关于矩阵的函数的全微分 $\mathrm{d}f$ 是导数矩阵 $\frac{\partial f}{\partial X}$ 与微分变量 $\mathrm{d}X$ 的内积。（**推论3**）

> 标量和向量都可以看作是矩阵的特殊情况，因此推论3涵盖了推论 1、2。至此，我们得到了通用表达式





#### vjp

- https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html

- https://zhuanlan.zhihu.com/p/501451509 深度学习框架中的自动微分及高阶导数

  - https://docs.oneflow.org/master/basics/05_autograd.html 看扩展的部分，有说 vjp

    > **只需提供一个与 $y$ 大小一致的向量 $v$，即可计算 VJP**
    >
    > **若向量$v$ 是反向传播中上一层的梯度，VJP 的结果刚好是当前层要求的梯度。**

- https://blog.csdn.net/huangbx_tx/article/details/104801975

- https://github.com/google/jax/discussions/10271

- https://juejin.cn/post/6844904009841524750

- https://j-towns.github.io/2017/06/12/A-new-trick.html

- https://imrchen.wordpress.com/2021/11/15/%E5%BE%9E-jax-%E5%9B%9E%E7%9C%8B-jacobian-matrix/

  > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220817101358913.png" alt="image-20220817101358913" style="zoom:50%;" />
  >
  > ```
  > A={{a00,a01},{a10,a11}};A//MatrixForm
  > X={{5,7},{6,8}};X//MatrixForm
  > f[a_]:=a.X
  > f[A]//MatrixForm
  > D[f[A],{A}]//MatrixForm
  > 
  > # 注意看结果的维度，2*2 的结果对 A 求导，每个元素都都得一个 2*2 的导数矩阵，妙极
  > ```
  >
  > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20221009081304009.png" alt="image-20221009081304009" style="zoom:50%;" />
  >
  > <img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20221010110648236.png" alt="image-20221010110648236" style="zoom: 50%;" />
  >
  > ```
  > 
  > # doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md
  > # https://zhuanlan.zhihu.com/p/144756543 让向量、矩阵和张量的求导更简洁些吧
  > # https://www.cnblogs.com/pinard/p/10825264.html
  >     # 矩阵对矩阵的求导是比较复杂的定义
  > # https://www.zhihu.com/question/52399883
  >     # 矩阵求导不能直接使用链式法则，即将中间导数矩阵乘起来。使用链式法则归根结底还是要考虑矩阵元素对元素的求导，即标量对标量求导。
  > 
  > # https://rogerluo.dev/Brochure.jl/dev/automatic-differentiation/
  >     # julia 实现自动微分
  > 
  > # https://segmentfault.com/a/1190000042199820 
  >     # OneFlow源码阅读6：自动微分机制
  > 
  > import jax
  > import jax.numpy as jnp
  > from jax import random, jacrev, vjp
  > 
  > import numpy as np
  > 
  > import torch
  > 
  > A = jnp.array( [[1,2], [3, 4]] , jnp.float32 )
  > 
  > X = jnp.array( [[5, 6],[7, 8]] , jnp.float32 )
  > 
  > B = jnp.array( [[9],[10]] , jnp.float32 )
  > 
  > def f(a, b):
  >  return jnp.dot( a, b )
  > 
  > def c(A, X, B):
  >     return f( f(A, X), B)
  > 
  > ax = f(A, X)
  > 
  > axb = f(ax, B)
  > 
  > C = c(A, X, B)
  > 
  > ( grad_C, ) = jax.jacfwd(c, argnums=(0,))( A, X, B )
  > 
  > ( grad_axb_ax, ) = jax.jacfwd(f, argnums=(0,))( ax, B )  # (A.X).B 对 A.X 求导
  > 
  > ( grad_ax_a, ) = jax.jacfwd(f, argnums=(0,))( A, X )  # A.X 对 A 求导
  > 
  > g_axb_a = jnp.matmul( grad_axb_ax, grad_ax_a )
  > 
  > 
  > """
  > 
  > 
  >     A       X         B       C
  > ( (2*2) . (2*2) ) . (2*1) = (2*1)
  > 
  > d c / d A = d c / d A.X  *  d A.X / d A
  > 2*1*2*2 = 2*1*2*2 * 2*2*2*2
  > 
  > 
  > 梯度 grad_C 的维度是 (2, 1, 2, 2)
  >     它是这样构造的：先是有一个正常的 2*1 的矩阵，矩阵的每一个元素都是标量，然后把这些标量全部用 2*2 的矩阵替换，就得到 (2, 1, 2, 2) 的矩阵
  > 
  > 
  > [
  >     [ b00 * x00 + b10 *x01, b00 * x10 + b10 * x11],
  >     [ 0, 0 ]
  > ]
  > 
  > [
  >     [ 0, 0 ],
  >     [ b00 * x00 + b10 *x01, b00 * x10 + b10 * x11]
  > ]
  > 
  > """
  > 
  > gc00 = jnp.array(
  >         [
  >             [ B[0][0] * X[0][0] + B[1][0] * X[0][1], B[0][0] * X[1][0] + B[1][0] * X[1][1] ], 
  >             [ 0, 0 ]
  >         ], 
  >         jnp.float32 )
  > 
  > gc10 = jnp.array(
  >         [
  >             [ 0, 0 ],
  >             [ B[0][0] * X[0][0] + B[1][0] * X[0][1], B[0][0] * X[1][0] + B[1][0] * X[1][1] ]
  > 
  >         ], 
  >         jnp.float32 )
  > 
  > 
  > gc = jnp.stack([gc00, gc10 ], axis=0).reshape((2, 1, 2, 2))
  > 
  > 
  > # F= AX   # 求 df / dA   # (2*2) . (2*2) => (2*2)
  > 
  > # F = AX = IAX # 注意在 A 的左边添加了一个单位阵 I (3*3)
  > 
  > # dF = IdAX 
  > 
  > # vec(dF) = vec(IdAX) = (X^T \otimes I) vec(dA)  # \otimes 表示克罗内克积
  > 
  > # vec(dF) = \frac{\partial F^T}{\partial X}  vec(dX)  # 导数与微分的联系
  > 
  > # dF / d A = X^T \otimes I^T
  > 
  > pi = jnp.pi
  > e = jnp.e
  > 
  > 
  > A = jnp.array( [[1,3], [2, 4]] , jnp.float32 )
  > 
  > X = jnp.array( [[5, 7],[6, 8]] , jnp.float32 )
  > 
  > def f(A, X):
  >  return jnp.dot( A, X )
  > 
  > F = f( A, X )
  > 
  > ( grad_A, ) = jax.jacfwd(f, argnums=(0,))( A, X )  # jax 自动微分求出的梯度 dF / dA   (3, 2, 3, 2)
  > 
  > def y(A, X):
  >     y00 = jnp.dot( A[:1, :],  X[:,:1]).__array__()[0][0]
  >     y01 = jnp.dot( A[:1, :],  X[:, 1:2]).__array__()[0][0]
  >     y10 = jnp.dot( A[1:2, :],  X[:,:1]).__array__()[0][0]
  >     y11 = jnp.dot( A[1:2, :],  X[:,1:2]).__array__()[0][0]
  > 
  >     Y = jnp
  > 
  >     return y00
  > 
  > y(A, X)
  > 
  > I = jnp.eye( 3 ) # I 的转置还是 I，这里就省掉了
  > 
  > X_T =  jnp.transpose(X)
  > 
  > kr = jax.numpy.kron(X_T, I) # (6*6)  # 求 dF / dX
  >  # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 6 个元素，参数总共 6 个元素，求导结果总共应该是 6*6 = 36 个元素
  >      # df_1(x) .. df_n(x) 横向展开， dx 纵向展开
  >      # kr 的转置应该就是雅可比，它是 dx 横向展开, df(x) 纵向展开
  > 
  > # grad_A_reshape = torch.reshape( torch.tensor(grad_A.__array__()), (6, 6))
  > 
  > grad_A_reshape = jnp.reshape(grad_A, (6, 6))  # 经观察，它和前面的 kr 排序顺序不一样，数值似乎是一样的
  > 
  > 
  > 
  > a = 1
  > 
  > # 下面用 jax 自动微分验证
  > 
  > ( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
  >  # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样
  > 
  > grad_42 = jnp.reshape(grad, (4, 2)) # 和前面 kr 一样了
  > 
  > 
  > ( grad2, ) = jax.jacfwd(f, argnums=(1,))( F, V )
  > 
  > grad2_21 = jnp.reshape(grad2, (2, 1))
  > 
  > a = 1
  > 
  > 
  > y, vjp_fn = jax.vjp(f, A, X) # 返回函数的计算结果，还有用于计算 vjp 的函数 vjp_fn，它需要一个向量作为参数
  >  # 你传一个向量进去，vjp_fn 就会给你一个 v * 雅可比 的结果
  > 
  > 
  > AA = torch.tensor(A.__array__())
  > XX = x = torch.tensor(X.__array__())
  > 
  > def ff(AA, XX):
  >  return torch.mm(AA, XX) # 数学里的矩阵乘法，要求两个Tensor的维度满足矩阵乘法的要求
  > 
  > FF = ff(AA, XX)
  > 
  > jacobians = torch.autograd.functional.jacobian(ff, (AA, XX))
  > jacobian_XX = jacobians[1]  # (1, 2, 2, 2)  和 jax 算出来的 grad 是一样的
  > 
  > jacobian_XX_42 = torch.reshape(jacobian_XX, (4, 2)) # 和前面 kr 一样了
  > 
  > 
  > 
  > 
  > 
  > a = 1
  > 
  > 
  > import jax.numpy as jnp
  > from jax import random, jacrev, vjp
  > 
  > key = random.PRNGKey(0)
  > 
  > 
  > def sigmoid(x):
  >     return 0.5 * (jnp.tanh(x / 2) + 1)
  > 
  > 
  > def predict(W, b, inputs):
  >     return sigmoid(jnp.dot(inputs, W) + b)
  > 
  > 
  > key, W_key, b_key = random.split(key, 3)
  > W = random.normal(W_key, (3,))
  > b = random.normal(b_key, ())
  > 
  > inputs = jnp.array([[0.52, 1.12,  0.77],
  >                     [0.88, -1.08, 0.15],
  >                     [0.52, 0.06, -1.30],
  >                     [0.74, -2.49, 1.39]])
  > 
  > # (4,3) . (3,) + () = (4,) 
  > 
  > t1 = sigmoid(jnp.dot(inputs, W) + b)
  > 
  > def f(W):
  >     return predict(W, b, inputs)
  > 
  > 
  > def basis(size, index):
  >     a = [0.0] * size
  >     a[index] = 1.0
  >     return jnp.array(a)
  > 
  > 
  > M = [basis(4, i) for i in range(0, 4)]
  > 
  > # computing by stacking VJPs of basis vectors
  > y, vjp_fun = vjp(f, W)
  > 
  > def vgrad(f, W): # 输出 x 的梯度
  >   y, vjp_fn = vjp(f, W)
  >   return vjp_fn(jnp.ones(y.shape))
  > 
  > r = vgrad(f, W)
  > 
  > print('Jacobian using vjp and stacking:')
  > print(jnp.vstack([vjp_fun(mi) for mi in M]))
  > 
  > # computing directly using jacrev function
  > print('Jacobian using jacrev directly:')
  > print(jacrev(f)(W))
  > ```
  >
  > 
  >
  > ```python
  > # doc\lang\programming\CSC321 Lecture 10：Automatic Differentiation.md
  > 
  > import jax
  > import jax.numpy as jnp
  > from jax import random, jacrev, vjp
  > 
  > import numpy as np
  > 
  > import torch
  > 
  > # F= AX   # 求 df / dX   # (1*2) . (2*2) => (1*2)
  > 
  > # dF = AdX = AdXI # 注意在 dX 的右边添加了一个单位阵 I
  > 
  > # dF / dX = I 克罗内克积符号 A^T    dX 形状是 (4*2) ，所以 I 是 (2*2)。单位阵必是方阵
  > 
  > # G = FV # (1*2) . (2*1) => (1*1)
  >  # [ [f00, f01]  ] . [ [v00], [v10]  ]
  >  # 
  > 
  > A = jnp.array( [[1,2]] , jnp.float32 )
  > 
  > X = jnp.array( [[3,4],[5,6]] , jnp.float32 )
  > 
  > V = jnp.array( [[7],[8]] , jnp.float32 )
  > 
  > def f(A, X):
  >  return jnp.dot( A, X )
  > 
  > F = f( A, X )
  > G = f( F, V )
  > 
  > l = lambda A, X, V: f( f(A, X), V )
  > L = l(A, X, V)
  > ( grad_X, grad_V) = jax.jacfwd(l, argnums=(1,2))( A, X, V )  # dG / dX 和  dG / dV
  >  # 为了和后面分步计算的雅克比乘积结果对比 (链式法则求各层的梯度)
  > 
  > I = jnp.eye( 2 )
  > 
  > A_T = jnp.transpose(A)
  > 
  > kr = jax.numpy.kron(I, A_T) # (4*2)  # 求 dF / dX
  >  # 矩阵微分本质就是结果向量与参数向量逐元素求导, 结果总共 2 个元素，参数总共 4 个元素，求导结果总共应该是 8 个元素
  >      # df_1(x) .. df_n(x) 横向展开， dx 纵向展开
  >      # kr 的转置应该就是雅可比，它是 dx 横向展开, df(x) 纵向展开
  > 
  > kr2 = jnp.transpose(F) # (2*1)  # 求 dG / dV
  > 
  > 
  > 
  > a = 1
  > 
  > # 下面用 jax 自动微分验证
  > 
  > ( grad, ) = jax.jacfwd(f, argnums=(1,))( A, X ) # (1, 2, 2, 2)
  >  # 验证结果和 kr 是相同的，只是矩阵的 shape 不一样
  > 
  > grad_42 = jnp.reshape(grad, (4, 2)) # 和前面 kr 一样了
  > 
  > 
  > ( grad2, ) = jax.jacfwd(f, argnums=(1,))( F, V )
  > 
  > grad2_21 = jnp.reshape(grad2, (2, 1))
  > 
  > a = 1
  > 
  > 
  > y, vjp_fn = jax.vjp(f, A, X) # 返回函数的计算结果，还有用于计算 vjp 的函数 vjp_fn，它需要一个向量作为参数
  >  # 你传一个向量进去，vjp_fn 就会给你一个 v * 雅可比 的结果
  > 
  > 
  > AA = torch.tensor(A.__array__())
  > XX = x = torch.tensor(X.__array__())
  > 
  > def ff(AA, XX):
  >  return torch.mm(AA, XX) # 数学里的矩阵乘法，要求两个Tensor的维度满足矩阵乘法的要求
  > 
  > FF = ff(AA, XX)
  > 
  > jacobians = torch.autograd.functional.jacobian(ff, (AA, XX))
  > jacobian_XX = jacobians[1]  # (1, 2, 2, 2)  和 jax 算出来的 grad 是一样的
  > 
  > jacobian_XX_42 = torch.reshape(jacobian_XX, (4, 2)) # 和前面 kr 一样了
  > ```
  
  > Note: we **never explicitly construct the Jacobian**. It's usually simpler
  > and more efficient to **compute the VJP directly**.(CSC321 Lecture 10: Automatic Differentiation)
  >
  > <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220816091436676.png" alt="image-20220816091436676" style="zoom: 80%;" />
  >
  > ![image-20220816091749759](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220816091749759.png)
  >
  > 若一個可微分函數 𝑓 是從定義域 ℝ𝑛 映射到值域ℝ𝑚（𝑓: ℝ𝑛 → ℝ𝑚 ）， ℝ𝑛 空間中的向量 v 的梯度，可以用 vector Jacobian product J^Tv 算出來。
  >
  > ```
  > import jax.numpy as jnp
  > from jax import vjp, jvp, grad
  > from jax import jacrev, jacfwd
  >                 
  > def f(x):
  >  return 3 * x * x    # y = 3x^2
  > 
  > 
  > def vgrad(f, x): # 输出 x 的梯度
  > y, vjp_fn = vjp(f, x)
  > return vjp_fn(jnp.ones(y.shape))[0] # jax.vjp = v^T @ J
  > 
  > 
  > seed = 10
  > key = random.PRNGKey(seed)
  > 
  > x = random.normal(key, (3,), float)
  > 
  > v = jnp.array([[0.1, 1.0, 0.0001]]).T
  > 
  > # x, y, x^t @ J, dy/dx, v^t @ J,
  > x, f(x), vgrad(f, x), 6 * x, vgrad(f, v)  
  > ```



```
import jax
>>>
def f(x, y):
  return jax.numpy.sin(x), jax.numpy.cos(y)

primals, f_vjp = jax.vjp(f, 0.5, 1.0)
xbar, ybar = f_vjp((-0.7, 0.3))
print(xbar)
-0.61430776
print(ybar)
-0.2524413
```






```python
import jax.numpy as jnp
from jax import random, jacrev, vjp

key = random.PRNGKey(0)


def sigmoid(x):
    return 0.5 * (jnp.tanh(x / 2) + 1)


def predict(W, b, inputs):
    return sigmoid(jnp.dot(inputs, W) + b)


key, W_key, b_key = random.split(key, 3)
W = random.normal(W_key, (3,))
b = random.normal(b_key, ())

inputs = jnp.array([[0.52, 1.12,  0.77],
                    [0.88, -1.08, 0.15],
                    [0.52, 0.06, -1.30],
                    [0.74, -2.49, 1.39]])

# (4,3) . (3,) + () = (4,) 

t1 = sigmoid(jnp.dot(inputs, W) + b)

def f(W):
    return predict(W, b, inputs)


def basis(size, index):
    a = [0.0] * size
    a[index] = 1.0
    return jnp.array(a)


M = [basis(4, i) for i in range(0, 4)]

# computing by stacking VJPs of basis vectors
y, vjp_fun = vjp(f, W)

print('Jacobian using vjp and stacking:')
print(jnp.vstack([vjp_fun(mi) for mi in M]))

# computing directly using jacrev function
print('Jacobian using jacrev directly:')
print(jacrev(f)(W))


'''
Output:
Jacobian using vjp and stacking:
[[ 0.05981752  0.12883773  0.08857594]
 [ 0.04015911 -0.04928619  0.0068453 ]
 [ 0.12188289  0.01406341 -0.3047072 ]
 [ 0.00140426 -0.00472514  0.00263773]]
Jacobian using jacrev directly:
[[ 0.05981752  0.12883773  0.08857594]
 [ 0.04015911 -0.04928619  0.0068453 ]
 [ 0.12188289  0.01406341 -0.3047072 ]
 [ 0.00140426 -0.00472514  0.00263773]]
 ''';
```



```python
 x = torch.ones(3, requires_grad=True)

 y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))

 v = torch.tensor([3, 5, 7])

 y.backward(v)
 print(x.grad)
 """
 The Jacobian seems correct and if it multiplies on vector (3, 5, 7) I would expect result to be (11, 17, 14).
 Got it! We should transpose Jacobian before multiplication. Then everything matches.
 """

 print( torch.matmul(  torch.tensor([ [2, 0, 0], [1, 2 , 0], [0, 1, 2] ]),  torch.tensor([ [3], [5], [7] ]) ) )       # J.t() @ v  结果是列向量
 print( torch.matmul(  torch.tensor([ [3], [5], [7] ]).t(), torch.tensor([ [2, 1, 0], [0, 2 , 1], [0, 0, 2] ])  ) )   # v.t() @ J  结果是行向量
```





#### \_\_array\_\_

```
x_jnp = jnp.arange(10)
x_np = x_jnp.__array__()

print(type(x_np))
# <class 'numpy.ndarray'>
```



#### sigmoid

```
jax.nn.sigmoid(F)
```





#### OR 运算JAX实现

```

# OR_JAX.py
import numpy as onp
import jax
import jax.numpy as np

"""
OR 运算, JAX 自动微分实现
"""

# 此激活函数设计为可以接受列向量
# 返回结果也是列向量
# np.exp 的实现可以接受向量作为参数，所以代码很简洁
def sigmoid (x):
    return 1/(1 + np.exp(-x))

m = 4 # 样本数
n = 3 # 列数
alpha = 0.5 # 学习率
maxIter = 50000 # 最大迭代次数

X = np.array([
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]
             ], onp.float)

# 输入矩阵，维度4*3。注意偏置作为列向量添加进来了

Y = np.array([
                [0],
                [1],
                [1],
                [1]
             ], onp.float)
# 4*1 输出

W = onp.random.uniform(size=(3, 1))   # 3*1 权重
#W = W * 0.1 # 据说对于sigmoid 激活函数，更小的权重更容易收敛
"""
观察输入输出的维度，可以看出需要对X 的列进行压缩，既把列从维度3 降维到1
    右乘是列变换，应该让权重矩阵W 右乘X，既 X.W
    矩阵点乘的维度变化
        (4*3).(3*1) = 4*1
"""


# 求前向传播的均方误差
def loss(X, W, m):
    A = np.dot(X, W)  # 前向传播
    H = sigmoid(A)    # 预测结果
    E = H - Y         # 误差值
    E2 = E ** 2
    
    errs = np.sum( E2, axis=0 )[0] # 按列求和

    lss = 1 / (2 * m) * errs  # 均方误差值

    return lss


loss_grad = jax.grad(loss)  # 自动求梯度


for k in range(maxIter): 

    # grads = jax.grad(loss, argnums=(1,))(X, W, m)
    
    [ lss, grads ] = jax.value_and_grad(loss, argnums=(1,))(X, W, m)  # 表示对 第1 个参数进行求导 (索引从0 开始，这里的第一个参数是 W)

    lss = float(lss)  # lss 是 0 维数组，不能用下标去索引

    W = W - alpha * grads[0]


    if lss < 0.001: 

        A = np.dot(X, W)  # 前向传播
        H = sigmoid(A)    # 预测结果
        E = H - Y         # 误差值

        print(f"loss is: {lss}, curr iter num: {k}")
        print(H) 
        
        break

    if k % 100 == 0:
        print(f"loss is: {lss}, curr iter num: {k}")

```





#### windows 必须手动编译

- https://jax.readthedocs.io/en/latest/developer.html#additional-notes-for-building-jaxlib-from-source-on-windows

#### jaxlib 非官方安装

- https://github.com/cloudhan/jax-windows-builder





```
https://jax.readthedocs.io/en/latest/developer.html#additional-notes-for-building-jaxlib-from-source-on-windows
```





```python
# https://www.geeksforgeeks.org/jacobian-matrix-in-pytorch/
from torch.autograd.functional import jacobian
from torch import tensor
 
#Defining the main function
def f(x1,x2,x3):
    return (x1 + x2, x3*x1, x2**3)
 
#Defining input tensors
x1 = tensor(3.0)
x2 = tensor(4.0)
x3 = tensor(5.0)
 
#Printing the Jacobian
print(jacobian(f,(x1,x2,x3)))
```



```python
# https://github.com/google/jax/issues/47
import jax
import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random

def f(x1,x2,x3):
    return (x1 + x2, x3*x1, x2**3)

x1 = 3.
x2 = 4.
x3 = 5.

jac_x1 = jax.jacfwd(lambda x: f(x,x2,x3))(x1)
jac_x2 = jax.jacfwd(lambda x: f(x1,x,x3))(x2)
jac_x3 = jax.jacfwd(lambda x: f(x1,x2,x))(x3)

print(jac_x1)

print(jac_x2)

print(jac_x3)
```





```python

# https://github.com/google/jax/issues/47

grad 只适用于输出为标量的函数

def f(x, y):
  return 2 * x * y

grad(f)(3., 4.)  # 8.
grad(f, 0)(3., 4.)  # 8.
grad(f, 1)(3., 4.)  # 6
grad(f, (0, 1))(3., 4.)  # (8., 6.)


jacfwd 和 jacrev 当前只适用于单参的函数，所以如果需要微分多参函数时需要手动封装一下：


jacrev(lambda x: f(x, 4.))(3.)  # 8. 
jacrev(lambda y: f(3., y))(4.)  # 6.


```



```python
import jax
import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random

key = random.PRNGKey(0)


w = jax.random.uniform(key, shape=(2, 2))   # 2*2 权重

b = jax.random.uniform(key, shape=(2, 2))   # 2*2 偏置

x = jnp.array(
    [ [1, 2], 
      [3, 4] ]
    ) 

p =  jnp.array(
    [ [1, 0], 
      [0, 1] ]
    ) 

def A(w, b):
  return x.dot( w ) + b


jac_w = jax.jacfwd(lambda x: A(x, b))(w)
jac_b = jax.jacfwd(lambda x: A(w, x))(b)


print(jac_w)


print(jac_b)
```





```
# https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html
```



```python
import numpy as np
import torch

from torch.autograd.functional import jacobian


def exp_reducer(x):
    return x.exp().sum(dim=1)

inputs = torch.rand(2, 2)
jacobian(exp_reducer, inputs)
```



#### 检查cudnn版本

```
apt-cache policy libcudnn8
```



```
# Check libcudnn8 version
!apt-cache policy libcudnn8

# Install latest version
!apt install --allow-change-held-packages libcudnn8=8.0.5.39-1+cuda11.1

# Export env variables
!export PATH=/usr/local/cuda-11.1/bin${PATH:+:${PATH}}
!export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH
!export LD_LIBRARY_PATH=/usr/local/cuda-11.1/include:$LD_LIBRARY_PATH
!export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64
```





#### reduce

```python
"""
jax.lax.reduce
Parameters
    operands (Any) –  操作数

    init_values (Any) –  初值

    computation (Callable[[Any, Any], Any]) –  函数: 二进一出

    dimensions (Sequence[int]) –  维度 (0, ) 表示 0 维

Return type
    Any
"""
from jax import lax
import jax.numpy as jnp
result = lax.reduce(jnp.arange(6, dtype='uint8'), jnp.uint8(0), lax.bitwise_xor, (0,))
print(result)
```



#### linspace

```python
# 0 到 2pi 均匀的分成 16 份
jnp.linspace(0, 2 * math.pi, 16)  # shape:(16,) 16 个数的一维数组
```



#### 维度不同的加法

- doc\lang\programming\pytorch\jax\jax_train_rnn.py

```python
tmp = t + offset  # (16, ) + (10000, 1) = (10000, 16)
tmp2 = jnp.sin(tmp)  # (10000, 16)
```



#### slice



```
A[:,:1] # 行全要，列只要第0 列 
```





#### 分块操作 sousa

```python
x1 = x1.at[:half_dataset_size].multiply(-1)
y = y.at[:half_dataset_size].set(0)
x = jnp.stack([x1, x2], axis=-1)  # 堆叠在一起
```



#### stack 堆叠

```python
x = jnp.stack([x1, x2], axis=-1)   # statck (10000,16)  (10000,16)  = 10000, 16, 2  
	# stack 会增加一个新的维度, 如果 axis=0 新维度在 第 1 维, 如果 axis=-1 新维度在最后一维
```



#### 增加一个维度

```python
y = x[:,None] # 增加一个维度
```





#### assert

```python
dataset_size = arrays[0].shape[0]
assert all(array.shape[0] == dataset_size for array in arrays)
```







#### 随机数

```
(key,) = jrandom.split(key, 1)  # 逗号可能不能省略，有它才是 tuples
```



```python
import jax.random as jrandom

data_key, loader_key, model_key = jrandom.split(jrandom.PRNGKey(5678), 3)

# 均匀分布 (10000, 1) 一万个数的二维数组
offset = jrandom.uniform(data_key, (dataset_size, 1), minval=0, maxval=2 * math.pi)
```



```python
# 正态分布
key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)
W1 = jrandom.normal(key1, (4, 1) )  # 第一层权重
```





```python
def dataloader(arrays, batch_size, *, key):
    dataset_size = arrays[0].shape[0]
    assert all(array.shape[0] == dataset_size for array in arrays)
    indices = jnp.arange(dataset_size)
    while True:
        perm = jrandom.permutation(key, indices) # 随机重排，类似shuffle
        (key,) = jrandom.split(key, 1)
        start = 0
        end = batch_size
        while end < dataset_size:
            batch_perm = perm[start:end]
            yield tuple(array[batch_perm] for array in arrays)
            start = end
            end = start + batch_size
```



#### jit

```python
import jax
import jax.numpy as jnp

def selu(x, alpha=1.67, lambda_=1.05):
  return lambda_ * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)

x = jnp.arange(1000000)
%timeit selu(x).block_until_ready()


selu_jit = jax.jit(selu)

# Warm up
selu_jit(x).block_until_ready()

%timeit selu_jit(x).block_until_ready()

```









#### pytree

- https://jax.readthedocs.io/en/latest/pytrees.html

  > 是 jax 内置的数据结构



```python
pytree (nested Python tuple/list/dict) 
```



### flax

- https://github.com/gordicaleksa/get-started-with-JAX

  > **Machine Learning with JAX  From Zero to Hero**

#### @compact

- https://flax.readthedocs.io/en/latest/flax.linen.html#compact-methods

```
Without compact:

class Net(nn.Module):

  def setup(self):
    self.dense = nn.Dense(features=10)
  
  def __call__(self, x):
    x = self.dense(x)
    return x
With compact:

class Net(nn.Module):

  @nn.compact
  def __call__(self, x):
    x = nn.Dense(features=10)(x)
    return x
```



#### flax.linen.Dense

```python
import flax.linen as nn

class SimpleMLP(nn.Module):
    units: int
    
    @nn.compact
    def __call__(self, x: jnp.ndarray) -> jnp.ndarray:
        x = nn.Dense(self.units)(x)  # 线性变换
        x = nn.relu(x)
        x = nn.Dense(1)(x)
        return x
    
model=SimpleMLP(2) 

```



#### 共享参数

````python
class A(nn.Module):
  shared_param: Any

  def setup(self, is_shared=False):
     if self.shared_param is not None:
       self.param = self.shared_param
     else:
      self.param = self.variable(
        'database', 'key_db', functools.partial(jnp.zeros, dtype=jnp.float32), (4))
     
  def __call__(self, x):
    return x*self.param
````



#### torch to flax

- https://zhuanlan.zhihu.com/p/54530247

```python
import flax
import torch
import jax.numpy as jnp
import numpy as np

torch.manual_seed(0)

torch_layernorm = torch.nn.LayerNorm(12)
flax_layernorm = flax.linen.LayerNorm()
torch_state_dict = torch_layernorm.state_dict()
torch_state_dict["scale"] = jnp.array(np.array(torch_state_dict.pop("weight")))
torch_state_dict["bias"] = jnp.array(np.array(torch_state_dict.pop("bias")))

x = torch.randn((8, 12))
x_flax = jnp.array(np.array(x))

torch_out = torch_layernorm(x)
flax_out = flax_layernorm.apply(variables={"params": torch_state_dict}, x=x_flax)
np.testing.assert_allclose(torch_out.detach().numpy(), flax_out, rtol=1e-5)
```



#### SELU 激活函数


$$
f\left(x\right) = \lambda{x} \text{ if } x \geq{0} \\
f\left(x\right) = \lambda{\alpha\left(\exp\left(x\right) -1 \right)} \text{ if } x < 0
$$

```python
# doc\lang\programming\pytorch\jax\JAX_From_Zero_to_Hero_1.ipynb
# Define a function

def selu(x, alpha=1.67, lmbda=1.05):  # note: SELU is an activation function
    return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)  # 条件为true 返回第一参，否则返回第二参

selu_jit = jit(selu)  # let's jit it

# Visualize SELU (just for your understanding, it's always a good idea to visualize stuff)
visualize_fn(selu)

# Benchmark non-jit vs jit version
data = random.normal(key, (1000000,))

print('non-jit version:')
%timeit selu(data).block_until_ready()
print('jit version:')
%timeit selu_jit(data).block_until_ready()
```





### equinox

- https://github.com/patrick-kidger/equinox

  > top of jax 简单易用

- https://colab.research.google.com/drive/1xoGwp40otsZfnyAfbBtFkUrteGICJppp?usp=sharing

- https://github.com/patrick-kidger/equinox/blob/main/examples/train_rnn.ipynb

  - https://colab.research.google.com/github/patrick-kidger/equinox/blob/main/examples/train_rnn.ipynb 
  - https://colab.research.google.com/drive/17q5CGC3ZT2JNzj0v-jH8UcuhXb2kBTbC?usp=sharing

- https://colab.research.google.com/github/patrick-kidger/equinox/blob/main/examples/score_based_diffusion.ipynb

  > 数字识别

  



#### make_functional

- https://github.com/patrick-kidger/equinox/issues/112

```python
# pytorch

net = NetworkClass(*args, **kwargs)
fnet, params = functorch.make_functional(net)
y = fnet(params, x) 
```

```python
# equinox
@eqx.filter_jit
@eqx.filter_vmap(args=(None, 0, 0))
@eqx.filter_grad
def loss(model, x, y):
    return (model(x) - y) ** 2

model = eqx.nn.MLP(...)
per_sample_grads = loss(model, ...)
```



#### jax.vmap

```

import equinox as eqx
import equinox.experimental as eqxe
import jax
import jax.nn as jnn
import jax.numpy as jnp
import jax.random as jrandom
seed = 0

key = jrandom.PRNGKey(seed)
key, key_linear, key_input = jrandom.split(key, 3)
#print("key=", key)
d_in = 3
d_out = 4
x = jrandom.normal(key_input, shape=(d_in, 5))
linear = eqx.nn.Linear(d_in, d_out, use_bias=True, key=key_linear)
# fails with ValueError due to impossibility of broadcasting
res = linear(x)

# 正确做法
jax.vmap(linear, in_axes=(1,), out_axes=(1,))(x)
```



```python
`jax.vmap` 是 JAX 库中的一个函数，它用于对向量化操作进行自动批处理。简单来说，`vmap` 能够让你将操作应用于数组的批次，而无需显式编写循环。这在需要对多个输入并行执行相同操作时特别有用。

以下是 `jax.vmap` 的一些关键点：

1. **并行计算**：`vmap` 可以将任何标量函数转换为能够并行处理数组的函数。
2. **简化代码**：减少显式的循环，使代码更加简洁和易读。
3. **提高性能**：利用 JAX 的优化，能够更高效地利用硬件资源（比如 TPU/GPU）。

### 示例代码

假设我们有一个函数 `f(x, y)`，它计算两个标量的点积。我们希望对一组输入数据应用该函数，使用 `vmap` 可以非常容易地实现这一目标。

​```python
import jax.numpy as jnp
from jax import vmap

# 定义标量函数
def f(x, y):
    return x * y

# 创建输入数组
x = jnp.array([1, 2, 3])
y = jnp.array([4, 5, 6])

# 使用 vmap 将 f 向量化
vectorized_f = vmap(f)

result = vectorized_f(x, y)
print(result)  # 输出: [ 4 10 18 ]
​```

在这个例子中，`vmap` 自动将 `f(x, y)` 函数向量化，使其能够一次性处理整个数组而不是单个元素。

`jax.vmap` 在深度学习和科学计算中非常有用，能够显著简化代码并提升性能，同时保持代码清晰和可维护。
```





### mac m1

- https://github.com/google/jax/issues/12505 eig bug in M1 mac

  > ```
  > import jax.numpy as np
  > 
  > mat = np.array([
  >                     [1+1j, 3+2j, 4.0+1.1j, 11-0.00001j, 44+100j],
  >                     [22+0j, 23+2j, 0.5+0.93j, 33+12j, 0.0001+0.000001j],
  >                     [-11-1j, 23+87j, 11-0.002j, 32-0.03423j, 32+9j],
  >                     [0.0002+23j, 10+0.324j, 0.003+0.999j, 10.434+2j, 33+0j],
  >                     [3+0.9j, 12+12j, 3.22+98j, 0.024+99.123j, 0+123j]
  >                 ])
  > 
  > print(np.linalg.eig(mat[:-1, :-1]))
  > print(np.linalg.eig(mat))
  > ```



### Solving Optimization Problems with JAX



```
# Solving Optimization Problems with JAX
# https://medium.com/swlh/solving-optimization-problems-with-jax-98376508bd4f
```



```python
def f(x) : return 3*x[0]**2 
gradf = grad(f)
gradf(np.array([2.0]))
>> 12.0
```





### you-don-t-know-jax



```
# https://colinraffel.com/blog/you-don-t-know-jax.html
```



```
# https://github.com/craffel/jax-tutorial/blob/master/you-don-t-know-jax.ipynb

import random
import itertools

import jax
import jax.numpy as np
# Current convention is to import original numpy as "onp"
import numpy as onp

from __future__ import print_function


# Sigmoid nonlinearity
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Computes our network's output
def net(params, x):
    w1, b1, w2, b2 = params
    hidden = np.tanh(np.dot(w1, x) + b1)
    return sigmoid(np.dot(w2, hidden) + b2)

# Cross-entropy loss
def loss(params, x, y):
    out = net(params, x)
    cross_entropy = -y * np.log(out) - (1 - y)*np.log(1 - out)
    return cross_entropy

# Utility function for testing whether the net produces the correct
# output for all possible inputs
def test_all_inputs(inputs, params):
    predictions = [int(net(params, inp) > 0.5) for inp in inputs]
    for inp, out in zip(inputs, predictions):
        print(inp, '->', out)
    return (predictions == [onp.bitwise_xor(*inp) for inp in inputs])



def initial_params():
    return [
        onp.random.randn(3, 2),  # w1
        onp.random.randn(3),  # b1
        onp.random.randn(3),  # w2
        onp.random.randn(),  #b2
    ]

loss_grad = jax.grad(loss)

# Stochastic gradient descent learning rate
learning_rate = 1.
# All possible inputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Initialize parameters randomly
params = initial_params()

for n in itertools.count():
    # Grab a single random input
    x = inputs[onp.random.choice(inputs.shape[0])]
    # Compute the target output
    y = onp.bitwise_xor(*x)
    # Get the gradient of the loss for this input/output pair
    grads = loss_grad(params, x, y)
    # Update parameters via gradient descent
    params = [param - learning_rate * grad
              for param, grad in zip(params, grads)]
    # Every 100 iterations, check whether we've solved XOR
    if not n % 100:
        print('Iteration {}'.format(n))
        if test_all_inputs(inputs, params):
            break
```



### Getting started with JAX 



```
# https://roberttlange.github.io/posts/2020/03/blog-post-10/


```



### 初试JAX - AutoGrad与JIT

- https://zhuanlan.zhihu.com/p/111254887

```
# https://zhuanlan.zhihu.com/p/111254887
	初试JAX - AutoGrad与JIT
```



### 自动微分



```
#　http://fancyerii.github.io/books/autodiff/
	自动微分
```





### vmap 自动mini-batch



```
 While in PyTorch one always has to be careful over which dimension you want to perform computations, vmap lets you simply write your computations for a single sample case and afterwards wrap it to make it batch compatible. 
```







### Pytorch中的vector-Jacobian product



```
# https://juejin.cn/post/6844904009841524750
Pytorch中的vector-Jacobian product


```



### csc2541_2021



```
#　https://www.cs.toronto.edu/~rgrosse/courses/csc2541_2021/  
	jax colab 代码质量很高

```





### 多维矩阵乘法

- https://pytorch.org/docs/stable/notes/broadcasting.html

```

前面的维度要满足broadcast才行，就是要么有一个维度为1，要么维度相等
最后的两个维度要满足矩阵乘法


结果：前面的维度保留最大的，后面的维度由矩阵乘法给出


a和b除了最后两个维度可以不一致，其他维度要相同(比如上面代码第一维和第二维分别都是1,2)
a和b最后两维的维度要符合矩阵乘法的要求（比如a的(3,4)能和b的(4,6)进行矩阵乘法）

(1,2) . (1,2,2,2) => (1,1,2,2)

```







### 行列式



```python
import autograd.numpy as np
import autograd as ag

def f(x):
    return np.array([x[0]**2,x[1]**2])

x = np.array([3.,11.])
jac = ag.jacobian(f)(x)
result = np.linalg.det(jac)
print(result)
```

```python
import jax.numpy as np
import jax

def f(x):
    return np.array([x[0]**2,x[1]**2])

x = np.array([[3.,11.],[5.,13.],[7.,17.]])

jac = jax.jacobian(f)
vmap_jac = jax.vmap(jac)
result = np.linalg.det(vmap_jac(x))
print(result)
```







# 矩阵求导



```
# https://zhuanlan.zhihu.com/p/352215536
	绝对不会出 bug 的矩阵求导——定义，推导，动机；非交换链式法则

```







# MatrixSlow



```python
# https://gitee.com/zackchen/MatrixSlow
pip install protobuf
pip install grpcio==1.11.0
```



# C++ 并发编程

- https://github.com/parallel101/course

  > c++ 并行计算





# 装机

- https://ark.intel.com/content/www/us/en/ark/products/199331/intel-core-i910900kf-processor-20m-cache-up-to-5-30-ghz.html  10900k 是有核显的  X99平台的U都没有核显

- https://blog.csdn.net/jizhidexiaoming/article/details/114694147

  > **10900k 装机**

> 对于单路 CPU 的主板，能够同时支持四张显卡卡的神板，毫无疑问就只有 X99/X299 系列的主板了
>
> 华硕的 Prime X299-A II ，这款主板支持的CPU 包括 10900X/10920X/10940X （Intel X299/LGA 2066）
>
> 由于我选的X299 主板，CPU的插槽类型为LGA 2066，我就要选与此匹配的CPU。我选的是 i9 10900X 10核20线程，价格 3199
>
>  “海盗船 复仇者” 系列单条 16GB 最便宜的内存 3200 MHz，一共上了 4 条，总共 64GB。主板有 8 个内存插槽，先插四条构成四通道，剩余的留作扩展，不过此处一定注意， 在安装内存条的时候需要阅读主板说明书，基本每个主板都会给出推荐的插法，看好个插槽所在的通道，一定不要插错了。

- https://www.zhihu.com/question/345502563

- https://www.jianshu.com/p/a6734bb55098

  > 115 aria2

- https://github.com/acgotaku/115

- https://www.hiroom2.com/2018/05/05/ubuntu-1804-davfs2-en/

- https://wiki.archlinux.org/title/Davfs2#Installing_davfs2

- https://memorydump.eu/how-to/mount-a-webdav-resource-in-a-linux-container/

  > ```
  > for centos7
  > $ cat <<EOF | sudo debconf-set-selections
  > davfs2 davfs2/suid_file boolean false
  > EOF
  > $ sudo apt install -y davfs2
  > 
  > sudo mount -t davfs https://dav.jianguoyun.com/dav /mnt
  > 
  > https://dav.jianguoyun.com/dav/
  > 
  > 账户：cdef6xx35@qq.com
  > azf3ec5k8rqdf5wi
  > 
  > 
  > for ubuntu
  > sudo apt update
  > sudo apt install davfs2
  > 
  > apt-get install kmod
  > 
  > mkdir /mntt
  > sudo mount -t davfs https://exxxt.com/webdav /mntt
  > 
  > ```

- https://www.jianshu.com/p/fe776caafbdd

  > https://exxxt.com/webdav



# CUDA版本



CUDA8.0：

- 费米（Fermi，GTX580）
- 开普勒（Kepler，GTX680，GTX780Ti，GTX Titan，Titan Z，Tesla K80）
- 麦克斯韦（Maxwell，GTX980Ti，Titan X，Tesla M40）
- [帕斯卡](https://www.zhihu.com/search?q=帕斯卡&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A1166786819})（Pascal，GTX1080Ti，Titan Xp，Tesla P100）

CUDA9.x：

- 开普勒（Kepler，GTX680，GTX780Ti，GTX Titan，Titan Z，Tesla K80）
- 麦克斯韦（Maxwell，GTX980Ti，Titan X，Tesla M40）
- 帕斯卡（Pascal，GTX1080Ti，Titan Xp，Tesla P100）
- 伏特（Volta，Titan V，Tesla V100）

CUDA10.x：

- 开普勒（Kepler，GTX680，GTX780Ti，GTX Titan，Titan Z，Tesla K80）
- 麦克斯韦（Maxwell，GTX980Ti，Titan X，Tesla M40）
- 帕斯卡（Pascal，GTX1080Ti，Titan Xp，Tesla P100）
- 伏特（Volta，Titan V，Tesla V100）
- 图灵（Turing，RTX2080Ti，Titan RTX，Tesla T4）



# K80 矩池云

CPU 3× Xeon E5-2678 v3 + tesla k80

- https://matpool.com
  
- https://github.com/WassimBenzarti/colab-ssh
  
  > 看看能不能用vscode远程连接colab
  
- https://zhuanlan.zhihu.com/p/338507526
  
- https://zhuanlan.zhihu.com/p/279401802

- https://github.com/MhLiao/DB
  
  - https://github.com/cs-chan/Total-Text-Dataset 数据集
  
- https://univeryinli.github.io/2019/05/27/Ubuntu-k80%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA/
  
  > Ubuntu k80深度学习环境搭建
  
- https://www.guoyaohua.com/deeplearning-workstation.html
  
  > 深度学习工作站攒机指南
  >
  > ### 主板
  >
  > 有很多朋友在进行选购主机的时候认为应该先选 CPU 再选主板，个人认为配件选购的顺序和主机的用途是有关系的，对于搭建深度学习工作站而言，在正式进行硬件选购前，最重要的是需要确认一个问题，到底需要单卡（GPU）主机还是多卡主机，如果只需要搭建单显卡的主机，那么在选购主板的过程中，不需要花费太多精力，大量主板可以满足要求，如果想要搭建双卡、三卡或是四卡主机，则需要在主板上下点功夫，为了日后升级方便，我的目标是使用可支持四显卡的主机，所以在主板选择方面，会很注重 PCIE 扩展接口数量。
  >
  > 在初期选择主板时，网上各式各样型号的主板会使小萌新（我）很是懵逼，在网上查找了些资料，了解了些主板的知识。为了保证 CPU 和主板搭配合理，装到一起能正常工作，首先我们需要了解各主板芯片组和 CPU 接口的具体含义。
  >
  > 我们可以看到大多数商品名称后面都会有一个类似（AMD A320/Socket AM4）或（Intel H310/LGA 1151）的注释，其实这些就是影响你 CPU 和主板能否匹配的最重要参数了，在商品详情页，我们也可以找到这个参数，前面的 “Intel H310” 或 “AMD A320” 指的就是主板的芯片组，而后面的 “LGA 1151” 或 “Socket AM4” 指的就是主板上 CPU 插槽的类型了。
  >
  > #### 芯片组
  >
  > 芯片组示主板的核心芯片，选对芯片组，主板和 CPU 才能兼容。目前主流的主板分为 Intel 和 AMD 两个系列，分别对应不同品牌的处理器。而每个系列又按照芯片组类型的不同，分为很多子系列。以 Intel 系列主板为例，在市面上可以看到华硕、技嘉、七彩虹等近十个品牌的产品，不同品牌的主板在外观和技术上会有一些差别，但他们使用的芯片组都是由 Intel 提供的。
  >
  > 不过，虽然同属于 Intel 系列主板，但根据处理器的不同，需要搭配对应芯片组的主板才能成功组建出一台可以使用的主机。比如目前 Intel 最新的九代酷睿 i9-9900k 处理器需要搭配 Z390、Z370 或 H370 芯片组的主板来使用。而 AMD 的 Ryzen 3/5/7 系列 CPU 和 APU 产品则可以搭配 X370、B350 或 A320 芯片组的主板。
  >
  > 那么不同芯片组的主板又有什么区别呢？有的时候，多个芯片组的主板虽然可以支持同一款处理器，但在主板的规格上还是有一定区别的。这些区别包括但不限于原生 USB 及磁盘接口数量、是否支持 CPU 超频、是否支持多显卡互联等。这对于不太了解主板的用户来说确实很难选择，简单总结一下：
  >
  > B 系列（如 B360、B250）属于入门级产品，不具备超频和多卡互联的功能，同时接口及插槽数量也相对要少一些。
  >H 系列（如 H310）比 B 系列略微高端一些，可以支持多卡互联，接口及插槽数量有所增长。
  > Z 系列（如 Z390、Z370）除了具备 H 系列的特点支持，还能够对 CPU 进行超频，并且接口和插槽数量也非常丰富。
  >X 系列（如 X99、X299）可支持 Intel 至尊系列高端处理器，同时具备 Z 系列的各项特点。
  > 
  >同时，Intel 的 100 系列和 200 系列主板可以搭配 6 代及 7 代酷睿处理器，300 系列主板需要搭配 8 代酷睿处理器，X299 系列主板需要搭配 7 代至尊系列酷睿处理器。
  > 
  >对于单路 CPU 的主板，能够同时支持四张显卡卡的神板，毫无疑问就只有 X99/X299 系列的主板了，当然你也可以考虑 intel 服务器 C 系列多路 CPU 主板，可以支持两个 CPU 在一张主板上。我的目标是使用单路 CPU，所以也就没有关注 C 系列主板。
  > 
  > 对于 X299 和 X99 之间的选择，有的朋友会主张买新不买旧，我个人的建议还是性价比高才是好的，较新的 X299 板子相比 X99 主板要贵大几百甚至 1k 左右，功能上的提升并不是很大，对于我们大多数 Deep Learning 开发者而言，X99 的板子足够了，毕竟要把钱花在刀刃上，GPU 才是大手笔。X99 板子主要推荐以下三款：
  > #### 对比
  > 
  >|   型号名称   |                 MSI / 微星 X99S GAMING 7                 |                华硕 RAMPAGE V EXTREME/U3.1                |              华硕 X99-E WS/USB 3.1               |
  > | :----------: | :------------------------------------------------------: | :-------------------------------------------------------: | :----------------------------------------------: |
  >|   主芯片组   |                        Intel X99                         |                         Intel X99                         |                    Intel X99                     |
  > |   CPU 插槽   |                       LGA 2011-v3                        |                        LGA 2011-v3                        |                   LGA 2011-v3                    |
  >|   内存规格   |                    8×DDR4 DIMM 四通道                    |                    8×DDR4 DIMM 四通道                     |                8×DDR4 DIMM 四通道                |
  > | 最大内存容量 |                          128GB                           |                           128GB                           |                      128GB                       |
  > |  PCI-E 标准  |                        PCI-E 3.0                         |                         PCI-E 3.0                         |                    PCI-E 3.0                     |
  >|  PCI-E 插槽  |                     4×PCI-E X16 插槽                     |             5×PCI-E X16 插槽 1×PCI-E X1 插槽              |                 7×PCI-E X16 插槽                 |
  > |   存储接口   |        10×SATA III 1×SATA Express 1×M.2（10Gb/s）        |              1×M.2 2×SATA Express 8×SATA III              |     1×M.2 2×SATA Express 8×SATA III 2×eSATA      |
  > |   USB 接口   | 6×USB2.0（2 背板 + 4 内置） 12×USB3.0（4 背板 + 8 内置） | 14×USB3.0（4 内置 + 10 背板） 6×USB2.0（4 内置 + 2 背板） | 14×USB3.0（4 内置 + 10 背板） 4×USB2.0（4 内置） |
  > |   主板板型   |                         ATX 板型                         |                        E-ATX 板型                         |                    E-ATX 板型                    |
  > |   外形尺寸   |                       30.5×24.4cm                        |                        30.5×27.2cm                        |                   30.5×26.7cm                    |
  > |  多显卡技术  |            NVIDIA 3-Way SLI NVIDIA 3-Way SLI             |           NVIDIA 4-Way SLI AMD 4-Way CrossFireX           |       NVIDIA 4-Way SLI AMD 4-Way CrossFire       |
  > 
  > 可以看到这三款主板，均为 X99 芯片组，CPU 插槽均为 LGA 2011-v3 ，而且有 8 个内存插槽，支持四通道，最高 128G 的内存容量，内存容量这部分个人很喜欢，对于大型数据集数据预处理的过程，对内存容量和 CPU 要求都很高，而且足够的内存容量使你不用再为多开窗口卡顿现象而担忧。三者都支持多显卡扩展，华硕 R5E 和华硕 X99 E-WS 均支持 4 显卡交火，微星 X99S Gaming 7 支持 3 显卡交火，不过显卡交火，对于深度学习计算没有任何的帮助，对游戏确是有一些提升，我们日常所说的多显卡训练模型，也不是用到交火技术，而是 Data Parallel 或 Model Parallel，所以交火与否我们不需要关注，需要关注的时 PCIE ×16 扩展插槽的有效个数（有的间距太近，无法全插）。
  > 
  > 起初最想购买的是 “华硕 X99-E WS”，经典的工作站主板，很多深度学习开发者的首选，支持四路显卡交火，更为优秀的是竟然有 7 个 ×16 全速 PCIE 3.0 扩展插槽，但是对于这类主板虽然有如此强大的扩展功能，但在真正插显卡的时候，由于 PCIE 接口之间的空间限制，你是无法插满插槽的，而且现在显卡都很厚，很可能会造成接口的浪费。这个板子已经停产，不过在天猫的华硕旗舰店仍然有存货，售价 “3899 元”，还是很贵的。其中有很多功能，对于我们日常使用、训练模型来讲并不是很用得上，会造成没必要的开销。最后我选择了在淘宝购买二手的 “华硕 RAMPAGE V EXTREME”，毕竟便宜。如果经费充足的朋友，我仍然建议购买 “华硕 X99 E-WS” 这个主板。



## vscode 远程调试

```python
https://github.com/MhLiao/DB 验证可运行的环境：

tesla K80 + Ubuntu18.04 +
	+ Python 3.7 + CUDA 10.0 + cuDNN 7.6.5 + NVCC 10.0 

nvcc --version
	Cuda compilation tools, release 10.0, V10.0.130

ldconfig -p | grep cuda
	libnvrtc.so.10.0 (libc6,x86-64) => /usr/local/cuda-10.0/targets/x86_64-linux/lib/libnvrtc.so.10.0


 
conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch --yes


cp /mnt/DB.zip /mnt/TD_TR.zip . && \
unzip DB.zip && \
unzip TD_TR.zip -d DB/datasets


export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
cd ~/DB/assets/ops/dcn/ && \
python setup.py build_ext --inplace

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0


https://matpool.com/supports/doc-vscode-connect-matpool/
    Remote Development 安装插件
    VS Code 远程连接矩池云机器教程
# train.py 添加命令行参数，并用vscode 远程调试K80 服务器上的 conda 环境(ctrl+shift+p 选conda的python)，vscode 中修改train.py 在main 函数下加入：

def main():

    import sys
    sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )

修改：/root/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml    
        train: 
        class: TrainSettings
        data_loader: 
            class: DataLoader
            dataset: ^train_data
            batch_size: 16
            num_workers: 16
           
把batch_size 和 num_workers 调小一点，否则K80 顶不住会出错，这里改成12

 
vscode 中然后F5 调试远行train.py

C:\Users\i\.ssh\config
Host hz-t3.matpool.com
  HostName hz-t3.matpool.com
  Port 26517
  User root





```



```python
    args = {
        'exp': 'experiments/seg_detector/td500_resnet18_deform_thre.yaml',
        'verbose': False,
        'visualize': False,
        'force_reload': False,
        'validate': False,
        'print_config_only': False,
        'debug': False,
        'benchmark': True,
        'distributed': False,
        'local_rank': 0,
        'num_gpus': 1,
    }
```







```
wget https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run

sh cuda_10.1.105_418.39_linux.run

apt install build-essential
gcc -v #查看gcc版本


conda deactivate && \
conda update -y conda -n base && \
conda install ipython pip && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch

conda deactivate && \
conda info -e && \
conda env remove -n DB && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
python -m pip install torch==1.2.0 -f https://download.pytorch.org/whl/torch_stable.html

cp /mnt/DB.zip /mnt/TD_TR.zip . && \
unzip DB.zip && \
unzip TD_TR.zip -d DB/datasets

export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
cd ~/DB/assets/ops/dcn/ && \
python setup.py build_ext --inplace

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0 && \
CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1
```



```
cuda10需要驱动418
现在装的是pytorch 1.3.1 py3.7_cuda10.0.130_cudnn7.6.3_0 pytorch

https://github.com/facebookresearch/maskrcnn-benchmark/issues/685
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/
https://gist.github.com/bogdan-kulynych/f64eb148eeef9696c70d485a76e42c3a

https://colab.research.google.com/github/andrepereira/cuda-c--google-colab/blob/master/GPU.ipynb

https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/

https://blog.csdn.net/qq_46521210/article/details/122211173
https://developer.nvidia.com/rdp/cudnn-archive
login: cdefx9x5@qq.com
vC4
选这个：Download cuDNN v7.5.0 (Feb 21, 2019), for CUDA 10.0

%%bash
sudo dpkg -i libcudnn7_7.5.0.56-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.5.0.56-1+cuda10.0_amd64.deb
sudo dpkg -i libcudnn7-doc_7.5.0.56-1+cuda10.0_amd64.deb


apt install cuda=10.0.130-1

conda deactivate && \
conda info -e && \
conda env remove -n DB && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch
```



```
# 可视化

		fuse = torch.cat((p5, p4, p3, p2), 1)
        # this is the pred module, not binarization module; 
        # We do not correct the name due to the trained model.
        binary = self.binarize(fuse)

        # 可视化--------
        binary_img = binary[0].permute((1, 2, 0)).cpu().data.numpy() * 255
        thresh_img = self.thresh(fuse)[0].permute((1, 2, 0)).cpu().data.numpy() * 255
        binary_img = binary_img.astype(np.uint8)
        thresh_img = thresh_img.astype(np.uint8)
        cv2.imwrite('bin.bmp', binary_img)
        binary_color_map = cv2.applyColorMap(binary_img, cv2.COLORMAP_JET)
        cv2.imwrite('cm.bmp', binary_color_map)

        cv2.imwrite('thresh.bmp',thresh_img)
        thresh_color_map=cv2.applyColorMap(thresh_img, cv2.COLORMAP_JET)
        cv2.imwrite('color_thresh.bmp',thresh_color_map)
        # ------------------
```

- https://blog.csdn.net/w12567878/article/details/121196107  docker cuda

# autodl

- https://www.autodl.com/

- https://pytorch.org/get-started/previous-versions/

- https://github.com/MhLiao/DB

  > ```
  > src/deform_conv_cuda.cpp:65:3: error: ‘AT_CHECK’ was not declared in this scope
  >    AT_CHECK(weight.ndimension() == 4
  > ```

```python
C:\Users\Administrator\.ssh\config
Host region-11.autodl.com
  HostName region-11.autodl.com
  Port 16116
  User root

# 3090 + Python3.8 + torch 1.10.1 + Cuda 11.1 # 这环境 1080ti ~ 3090 都适用

- https://developer.nvidia.com/zh-cn/blog/updating-the-cuda-linux-gpg-repository-key/
    >更新 CUDA Linux GPG 存储库密钥

cat /etc/os-release    
cat /proc/version

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb

dpkg -i cuda-keyring_1.0-1_all.deb

apt-get update
apt-get -y install cuda-11-1

wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
bash Miniforge3-Linux-x86_64.sh -b && \
~/miniforge3/bin/conda init && \
ln -s ~/miniforge3/bin/conda /usr/local/bin && \
ln -s ~/miniforge3/bin/activate /usr/local/bin && \
ln -s ~/miniforge3/bin/deactivate /usr/local/bin && \
source ~/miniforge3/etc/profile.d/conda.sh


cp autodl-nas/DB.zip autodl-nas/TD_TR.zip . && \
unzip DB.zip && \
unzip TD_TR.zip -d DB/datasets


conda deactivate && \
conda update -y conda -n base && \
conda install ipython pip && \
conda create -n DB python=3.8 --yes && \
source activate DB && \
pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html


pip install torch==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
	# apt install -y libsm6 libxrender1 libxext6 libgl1-mesa-glx
    	# 实测 vgpu-32G 要装这个
        # 能正常训练

apt install build-essential  && \
export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
nvcc --version && \
ldconfig -p | grep cuda && \
cd ~/DB/assets/ops/dcn/ && \
sed -i 's/AT_CHECK/TORCH_CHECK/1' /root/DB/assets/ops/dcn/src/deform_conv_cuda.cpp && \
sed -i 's/AT_CHECK/TORCH_CHECK/1' /root/DB/assets/ops/dcn/src/deform_pool_cuda.cpp && \
python setup.py build_ext --inplace
	# python setup.py clean --all \
	    && rm -rf *.so build/
	

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0

~/DB/backbones# vi resnet.py
	# 这里可以注释掉下载预训练模型的代码

sed -i 's/batch_size\:\ 16/batch_size\:\ 10/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/num_workers\:\ 16/num_workers\:\ 10/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/save_interval\:\ 18000/save_interval\:\ 450/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/epochs\:\ 1200/epochs\:\ 30/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml

# 禁用 cudnn
torch.backends.cudnn.enabled = False


https://matpool.com/supports/doc-vscode-connect-matpool/
    Remote Development 安装插件
    VS Code 远程连接矩池云机器教程

# vscode 打开远程文件夹 DB, ctrl + x 安装 python 扩展, ctrl+shift+p 输入 Python，选择选conda的python ，vscode 中修改train.py 在main 函数下加入命令行参数：

def main():

    import sys
    sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )
    torch.backends.cudnn.enabled = False

vscode 中然后F5 调试运行train.py 


# CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1

权重转换：
Usage: python convert_to_onnx.py /path/to/exp/yaml /path/to/pretrained/weight /path/to/save/onnx.  

// 验证    
CUDA_VISIBLE_DEVICES=0 python demo.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --image_path datasets/GD500/test_images/IMG_0000.JPG --resume /root/final --polygon --box_thresh 0.7 --visualize  
```



```python
# 调试方法
/root/DB/data/data_loader.py 
        if self.shuffle is None:
            self.shuffle = self.is_train
            self.shuffle = False  # 加载图片改成不随机，这样好调试
     

# 数据加载全在这里
/root/DB/data/image_dataset.py
	'./datasets/TD_TR/TD500//train_images/IMG_0855.JPG'  # 第一张图是这个
    './datasets/TD_TR/TD500//train_gts/IMG_0855.JPG.txt' # 相应的标记
    
    
    data = data_process(data) # 这里是数据增强

# 开始增强图片
/root/DB/data/processes/augment_data.py    
	data['image'] = aug.augment_image(image)  
    
```



```
# 导出增强后的图片（准备用同一张图生成很多很多的图用于训练，看看可不可行）
# https://blog.csdn.net/xinjieyuan/article/details/105205326

		if self.processes is not None:
            for data_process in self.processes:
                data = data_process(data)
        im = data['image']
        shape = im.shape  # (3, 640, 640)
        im = torch.stack( (im[0], im[1], im[2]), 2 )  # (640, 640, 3)
        return data





        iprocesses = []
        iprocesses.append( iprocesses[0] )
        iprocesses.append( iprocesses[2] )
        iprocesses.append( iprocesses[3] )
        # for data_process in iprocesses:
        #     data = data_process(data)
        
        # im = data['image']
        # shape = im.shape
        # im = torch.stack( (im[0], im[1], im[2]), 2 )

        im = im.astype(np.uint8)

        # cv2.imwrite("/root/aug.jpg", im)


```





```
%%bash
source activate DB && \
cd ~/DB && \
CUDA_VISIBLE_DEVICES=0 python demo.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --image_path ~/DB/datasets/TD_TR/TD500/train_images/IMG_0855.JPG --resume ~/td500_resnet18 --polygon --box_thresh 0.7 --visualize
```





```
train.py

#!python3
import argparse
from asyncio.windows_events import NULL
import time

import torch
import yaml

from trainer import Trainer
# tagged yaml objects
from experiment import Structure, TrainSettings, ValidationSettings, Experiment
from concern.log import Logger
from data.data_loader import DataLoader
from data.image_dataset import ImageDataset
from training.checkpoint import Checkpoint
from training.model_saver import ModelSaver
from training.optimizer_scheduler import OptimizerScheduler
from concern.config import Configurable, Config

import json
import decimal
import datetime


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def main():

    import sys
    sys.argv.append('experiments/seg_detector/td500_resnet18_deform_thre.yaml')
    sys.argv.append('--num_gpus')
    sys.argv.append('1')
    # torch.backends.cudnn.enabled = False

    parser = argparse.ArgumentParser(description='Text Recognition Training')
    parser.add_argument('exp', type=str)
    parser.add_argument('--name', type=str)
    parser.add_argument('--batch_size', type=int,
                        help='Batch size for training')
    parser.add_argument('--resume', type=str, help='Resume from checkpoint')
    parser.add_argument('--epochs', type=int, help='Number of training epochs')
    parser.add_argument('--num_workers', type=int,
                        help='Number of dataloader workers')
    parser.add_argument('--start_iter', type=int,
                        help='Begin counting iterations starting from this value (should be used with resume)')
    parser.add_argument('--start_epoch', type=int,
                        help='Begin counting epoch starting from this value (should be used with resume)')
    parser.add_argument('--max_size', type=int, help='max length of label')
    parser.add_argument('--lr', type=float, help='initial learning rate')
    parser.add_argument('--optimizer', type=str,
                        help='The optimizer want to use')
    parser.add_argument('--thresh', type=float,
                        help='The threshold to replace it in the representers')
    parser.add_argument('--verbose', action='store_true',
                        help='show verbose info')
    parser.add_argument('--visualize', action='store_true',
                        help='visualize maps in tensorboard')
    parser.add_argument('--force_reload', action='store_true',
                        dest='force_reload', help='Force reload data meta')
    parser.add_argument('--no-force_reload', action='store_false',
                        dest='force_reload', help='Force reload data meta')
    parser.add_argument('--validate', action='store_true',
                        dest='validate', help='Validate during training')
    parser.add_argument('--no-validate', action='store_false',
                        dest='validate', help='Validate during training')
    parser.add_argument('--print-config-only', action='store_true',
                        help='print config without actual training')
    parser.add_argument('--debug', action='store_true', dest='debug',
                        help='Run with debug mode, which hacks dataset num_samples to toy number')
    parser.add_argument('--no-debug', action='store_false',
                        dest='debug', help='Run without debug mode')
    parser.add_argument('--benchmark', action='store_true',
                        dest='benchmark', help='Open cudnn benchmark mode')
    parser.add_argument('--no-benchmark', action='store_false',
                        dest='benchmark', help='Turn cudnn benchmark mode off')
    parser.add_argument('-d', '--distributed', action='store_true',
                        dest='distributed', help='Use distributed training')
    parser.add_argument('--local_rank', dest='local_rank',
                        default=0, type=int, help='Use distributed training')
    parser.add_argument('-g', '--num_gpus', dest='num_gpus',
                        default=4, type=int, help='The number of accessible gpus')
    parser.set_defaults(debug=False)
    parser.set_defaults(benchmark=True)

    args = parser.parse_args()
    args = vars(args)
    args = {k: v for k, v in args.items() if v is not None}

    if args['distributed']:
        torch.cuda.set_device(args['local_rank'])
        torch.distributed.init_process_group(
            backend='nccl', init_method='env://')

    # conf = Config()
    # experiment_args = conf.compile(conf.load(args['exp']))['Experiment']
    # experiment_args.update(cmd=args)
    # save_json('./experiment_args.json', experiment_args)

    experiment_args = {
        "name": "Experiment",
        "class": "experiment.Experiment",
        "structure": {
            "class": "experiment.Structure",
            "builder": {
                "class": "experiment.Builder",
                "model": "SegDetectorModel",
                "model_args": {
                    "backbone": "deformable_resnet18",
                    "decoder": "SegDetector",
                    "decoder_args": {
                        "adaptive": True,
                        "in_channels": [
                            64,
                            128,
                            256,
                            512
                        ],
                        "k": 50
                    },
                    "loss_class": "L1BalanceCELoss"
                }
            },
            "representer": {
                "class": "experiment.SegDetectorRepresenter",
                "max_candidates": 1000
            },
            "measurer": {
                "class": "experiment.QuadMeasurer"
            },
            "visualizer": {
                "class": "experiment.SegDetectorVisualizer"
            }
        },
        "train": {
            "class": "experiment.TrainSettings",
            "data_loader": {
                "class": "experiment.DataLoader",
                "dataset": {
                    "name": "train_data",
                    "class": "experiment.ImageDataset",
                    "data_dir": [
                        "./datasets/TD_TR/TD500/",
                        "./datasets/TD_TR/TR400/"
                    ],
                    "data_list": [
                        "./datasets/TD_TR/TD500/train_list.txt",
                        "./datasets/TD_TR/TR400/train_list.txt"
                    ],
                    "processes": [
                        {
                            "class": "data.processes.AugmentDetectionData",
                            "augmenter_args": [
                                [
                                    "Fliplr",
                                    0.5
                                ],
                                {
                                    "cls": "Affine",
                                    "rotate": [
                                        -10,
                                        10
                                    ]
                                },
                                [
                                    "Resize",
                                    [
                                        0.5,
                                        3.0
                                    ]
                                ]
                            ],
                            "only_resize": False,
                            "keep_ratio": False
                        },
                        {
                            "class": "data.processes.RandomCropData",
                            "size": [
                                640,
                                640
                            ],
                            "max_tries": 10
                        },
                        {
                            "class": "data.processes.MakeICDARData"
                        },
                        {
                            "class": "data.processes.MakeSegDetectionData"
                        },
                        {
                            "class": "experiment.MakeBorderMap"
                        },
                        {
                            "class": "data.processes.NormalizeImage"
                        },
                        {
                            "class": "data.processes.FilterKeys",
                            "superfluous": [
                                "polygons",
                                "filename",
                                "shape",
                                "ignore_tags",
                                "is_training"
                            ]
                        }
                    ]
                },
                "batch_size": 16,
                "num_workers": 16
            },
            "checkpoint": {
                "class": "experiment.Checkpoint",
                "start_epoch": 0,
                "start_iter": 0,
                "resume": NULL
            },
            "model_saver": {
                "class": "experiment.ModelSaver",
                "dir_path": "model",
                "save_interval": 18000,
                "signal_path": "save"
            },
            "scheduler": {
                "class": "experiment.OptimizerScheduler",
                "optimizer": "SGD",
                "optimizer_args": {
                    "lr": 0.007,
                    "momentum": 0.9,
                    "weight_decay": 0.0001
                },
                "learning_rate": {
                    "class": "training.learning_rate.DecayLearningRate",
                    "epochs": 1200
                }
            },
            "epochs": 1200
        },
        "validation": {
            "class": "experiment.ValidationSettings",
            "data_loaders": {
                "icdar2015": {
                    "class": "experiment.DataLoader",
                    "dataset": {
                        "name": "validate_data",
                        "class": "experiment.ImageDataset",
                        "data_dir": [
                            "./datasets/TD_TR/TD500/"
                        ],
                        "data_list": [
                            "./datasets/TD_TR/TD500/test_list.txt"
                        ],
                        "processes": [
                            {
                                "class": "data.processes.AugmentDetectionData",
                                "augmenter_args": [
                                    [
                                        "Resize",
                                        {
                                            "width": 736,
                                            "height": 736
                                        }
                                    ]
                                ],
                                "only_resize": True,
                                "keep_ratio": True
                            },
                            {
                                "class": "data.processes.MakeICDARData"
                            },
                            {
                                "class": "data.processes.MakeSegDetectionData"
                            },
                            {
                                "class": "data.processes.NormalizeImage"
                            }
                        ]
                    },
                    "batch_size": 1,
                    "num_workers": 16,
                    "collect_fn": {
                        "class": "data.processes.ICDARCollectFN"
                    }
                }
            },
            "visualize": False,
            "interval": 4500,
            "exempt": 1
        },
        "logger": {
            "class": "experiment.Logger",
            "verbose": True,
            "level": "info",
            "log_interval": 450
        },
        "evaluation": {
            "class": "experiment.ValidationSettings",
            "data_loaders": {
                "icdar2015": {
                    "class": "experiment.DataLoader",
                    "dataset": {
                        "name": "validate_data",
                        "class": "experiment.ImageDataset",
                        "data_dir": [
                            "./datasets/TD_TR/TD500/"
                        ],
                        "data_list": [
                            "./datasets/TD_TR/TD500/test_list.txt"
                        ],
                        "processes": [
                            {
                                "class": "data.processes.AugmentDetectionData",
                                "augmenter_args": [
                                    [
                                        "Resize",
                                        {
                                            "width": 736,
                                            "height": 736
                                        }
                                    ]
                                ],
                                "only_resize": True,
                                "keep_ratio": True
                            },
                            {
                                "class": "data.processes.MakeICDARData"
                            },
                            {
                                "class": "data.processes.MakeSegDetectionData"
                            },
                            {
                                "class": "data.processes.NormalizeImage"
                            }
                        ]
                    },
                    "batch_size": 1,
                    "num_workers": 16,
                    "collect_fn": {
                        "class": "data.processes.ICDARCollectFN"
                    }
                }
            },
            "visualize": False,
            "interval": 4500,
            "exempt": 1
        },
        "cmd": {
            "exp": "experiments/seg_detector/td500_resnet18_deform_thre.yaml",
            "verbose": False,
            "visualize": False,
            "force_reload": False,
            "validate": False,
            "print_config_only": False,
            "debug": False,
            "benchmark": True,
            "distributed": False,
            "local_rank": 0,
            "num_gpus": 1
        }
    }

    import importlib
    cls = experiment_args.copy().pop('class')
    package, cls = cls.rsplit('.', 1)
    module = importlib.import_module(package)
    cls = getattr(module, cls)

    experiment = Configurable.construct_class_from_config(experiment_args)

    if not args['print_config_only']:
        torch.backends.cudnn.benchmark = args['benchmark']
        trainer = Trainer(experiment)
        trainer.train()


if __name__ == '__main__':
    main()
```



## cuda 多版本共存

- https://www.nemotos.net/?p=5067

```


https://developer.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.105_418.39_linux.run
	# 下载安装

22.04 安装 cuda 10.1 需要降级 gcc

echo "deb http://archive.ubuntu.com/ubuntu focal main universe" | sudo tee /etc/apt/sources.list.d/focal.list \
  && sudo apt update \
  && sudo apt install gcc-7 g++-7 -y

# 设置默认GCC版本
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 2 \
  && sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 1 \
  && sudo update-alternatives --config gcc
  	# 选择gcc-7

./cuda_10.1.105_418.39_linux.run
	# 安装，不要选驱动	

Please make sure that
 -   PATH includes /usr/local/cuda-10.1/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-10.1/lib64, or, add /usr/local/cuda-10.1/lib64 to /etc/ld.so.conf and run ldconfig as root



update-alternatives --remove cuda /usr/local/cuda-11.8
update-alternatives --install /usr/local/cuda cuda /usr/local/cuda-10.1 101 && 
ln -sfT /usr/local/cuda-10.1 /etc/alternatives/cuda && 
ln -sfT /etc/alternatives/cuda /usr/local/cuda  
	# 切换版本

vi ~/.bashrc 

if [ -z $LD_LIBRARY_PATH ]; then
  LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64
else
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.1/lib64
fi
export LD_LIBRARY_PATH

export PATH=/usr/local/cuda/bin:$PATH


source ~/.bashrc 

nvcc --version




conda install pytorch==1.2.0  -c pytorch
	# 官方文档是这个版本
	# 但是现在下载不了了
	

https://download.pytorch.org/whl/torch_stable.html
	# 这里看有什么可以装
	
pip install https://download.pytorch.org/whl/cu101/torch-1.4.0-cp38-cp38-linux_x86_64.whl
	# 这样装 1.4.0+cu101
	# 实测可以成功训练
	# 但是，为什么会自动下载 Downloading: "https://download.pytorch.org/models/resnet18-5c106cde.pth" to /root/.cache/torch/checkpoints/resnet18-5c106cde.pth
	





	
sudo apt install linux-headers-$(uname -r) -y
reboot

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin



```





## DB

原版代码，成功训练aliocr 结果，只用一张图 格式 TD500，图片500 张，都是同一张图复制500 次

```
7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on DBNet_aliocr_GD500.zip ./DB
```

```

# 修改配置 
sed -i 's/batch_size\:\ 16/batch_size\:\ 10/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/num_workers\:\ 16/num_workers\:\ 10/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/save_interval\:\ 18000/save_interval\:\ 450/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/epochs\:\ 1200/epochs\:\ 30/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml

# 训练
CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1

# 测试
CUDA_VISIBLE_DEVICES=0 python demo.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --image_path datasets/GD500/test_images/IMG_0000.JPG --resume /root/final --polygon --box_thresh 0.7 --visualize 


# vscode 中运行这样改

# /root/DB/train.py

def main():

    import sys
    sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )
    torch.backends.cudnn.enabled = False
    
```



### 训练 icdar2015_dbnet

```

see python summary.md -> OpenCV -> ppcor_aliocr_convert.py


apt-get update \
  && apt-get install build-essential python3-dev libevent-dev
	# 重要：先安装编译环境

wget --no-check-certificate  https://sourceforge.net/projects/p7zip/files/p7zip/16.02/p7zip_16.02_src_all.tar.bz2 && \
tar -jxvf p7zip_16.02_src_all.tar.bz2 && \
cd p7zip_16.02 && \
make && \
make install

7za x DBNet_aliocr_GD500.zip && \  # 500 张是成功了的（一张图复制成500张）
mv DB /root

# 数据生成代码在这里
# doc\lang\programming\pytorch\文本检测\DBNET\dbnet_aliocr\dbnet_aliocr_convert.py

	# 2000 张阿里云的识别结果，导出成 icdar2015 格式
unzip icdar2015_dbnet.zip && \
mv icdar2015_dbnet icdar2015 && \
ln -s /root/autodl-tmp/icdar2015 /root/DB/datasets/icdar2015

	
	
	# 修改数据加载
	/root/DB/data/image_dataset.py
		第41 行，改成下面这样。icdar2015 原版gt 标注就是这样的，不懂DB 为什么改成那样
                gt_path=[self.data_dir[i]+'/train_gts/'+'gt_'+timg.strip().split('.')[0]+'.txt' for timg in image_list]


export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
cd ~/DB/assets/ops/dcn/ && \
python setup.py build_ext --inplace
	# python3.8 要装 pip install more-itertools

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0


tmux
	source activate DB
	
	/root/DB/train.py 加入：
	import sys
    #sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( 'experiments/seg_detector/ic15_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )
    torch.backends.cudnn.enabled = False
    
    python train.py
    
	
tmux attach -t 0
	Contol + b  后按 d 可以离开环境并不影响当前程序的执行（离开后可以断开 ssh 连接）
	ctrl + D # 退出当前 session，中断程序执行
tmux kill-session -t 0 # 在没有进入 session 的情况下 kill 它


conda update --all

conda config --add channels conda-forge && \
conda config --set channel_priority flexible


conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n DB python=3.8 --yes && \
source activate DB && \
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch --yes -c conda-forge
	# 可以训练，但是中途会断，先试和官方一模一样的环境

	
	# pytorch 1.4成功编译 ?

https://download.pytorch.org/whl/torch_stable.html
	# 这里看有什么可以装
	
pip install https://download.pytorch.org/whl/cu101/torch-1.4.0-cp38-cp38-linux_x86_64.whl
	# 这样装 1.4.0+cu101



cd /root/DB && \
source activate DB && \
pip install -r requirement.txt
	# pip install --no-cache-dir --force-reinstall -r requirement.txt
		# 强制重装

pip uninstall opencv-python && \
pip install opencv-python==4.6.0.66



CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/ic15_resnet18_deform_thre.yaml --num_gpus 1

// 验证    
CUDA_VISIBLE_DEVICES=0 python demo.py experiments/seg_detector/ic15_resnet18_deform_thre.yaml --image_path datasets/icdar2015/test_images/img_97.jpg --resume /root/final --polygon --box_thresh 0.7 --visualize 


```



#### 优化

https://zhuanlan.zhihu.com/p/579956622 DBNet GT 构造过程的问题和对应解决方法

```
https://zhuanlan.zhihu.com/p/579956622

```





## mmocr

```
C:\Users\Administrator\.ssh\config
Host region-11.autodl.com
  HostName region-11.autodl.com
  Port 16116
  User root

# 3090 + Python3.8 + torch 1.10.1 + Cuda 11.3 # 这环境 1080ti ~ 3090 都适用

- https://developer.nvidia.com/zh-cn/blog/updating-the-cuda-linux-gpg-repository-key/
    >更新 CUDA Linux GPG 存储库密钥

cat /etc/os-release    
cat /proc/version

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb

dpkg -i cuda-keyring_1.0-1_all.deb

apt-get update
apt-get -y install cuda-11-3




wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
bash Miniforge3-Linux-x86_64.sh -b


~/miniforge3/bin/conda init && \
ln -s ~/miniforge3/bin/conda /usr/local/bin && \
ln -s ~/miniforge3/bin/activate /usr/local/bin && \
ln -s ~/miniforge3/bin/deactivate /usr/local/bin && \
source ~/miniforge3/etc/profile.d/conda.sh


conda deactivate && \
conda env remove -n DB

tmux 

conda create -n MM python=3.8 pytorch=1.10 cudatoolkit=11.3 torchvision -c pytorch -y && \
source activate MM && \
pip3 install openmim && \
mim install mmcv-full && \
mim install mmdet && \
git clone https://github.com/open-mmlab/mmocr.git && \
cd mmocr && \
pip3 install -e .


python mmocr/utils/ocr.py demo/demo_text_ocr.jpg --print-result --imshow

python mmocr/utils/ocr.py demo/demo_text_ocr.jpg --output out.jpg

# 中文识别
wget "https://download.openmmlab.com/mmocr/textrecog/sar/dict_printed_chinese_english_digits.txt"

put it to folder data/chineseocr/labels/

python mmocr/utils/ocr.py t.jpg --det None --recog SAR_CN --output out.jpg
	# 单行中文，不需要检测，否则它会调用英文的文本检测
	# https://github.com/open-mmlab/mmocr/issues/865 中文训练
	# https://github.com/open-mmlab/mmocr/issues/723 中文训练
	# https://github.com/open-mmlab/mmocr/issues/1291 细节满满

python mmocr/utils/ocr.py t2.jpg --det DB_r50 --recog SAR_CN --output out2.jpg
	# 多行中文，检测看看结果怎么样
		# 运行OK，但是只检测到几个字符，漏掉了大部分

python mmocr/utils/ocr.py t3.jpg --det DB_r18 --recog SAR --output out3.jpg --device cuda
	# mmocr 训练、测试、推断 都可以用 cpu

Yes, since your input is a cropped image, it is unnecessary to use a detection model; if the det model is not specified to None here, it will use PANet_IC15 as the detector by default.
MMOCR currently does not provide a Chinese-specific pre-trained model for the detector, however, you may try the model pre-trained on ICDAR2017 (such as MaskRCNN_IC17), since this is a multilingual dataset containing Chinese training samples.


```



### aliocr 训练

用阿里的识别结果训练 dbnet 和 SAR

```
# 图片生成 (把图书图片和识别结果转换成icdar2015 数据集 一模一样的格式)
	# doc\lang\programming\pytorch\文本检测\DBNET\dbnet_aliocr

# 数据转换 
	- https://mmocr.readthedocs.io/en/latest/datasets/det.html#icdar-2015
	
unzip ~/autodl-nas/GD500.zip -d data
cp -r configs/ configs_ali  # 复制原配置
	# 然后修改相应配置

cd data/GD500 && \
mkdir imgs && mkdir annotations && \
mv train_images imgs/training && \
mv test_images imgs/test && \
mv train_gts annotations/training && \
mv test_gts annotations/test

python tools/data/textdet/icdar_converter.py data/GD500 -o data/GD500 -d data/GD500 --split-list training test



# 训练
python tools/train.py configs_ali/textdet/dbnet/dbnet_r18_fpnc_1200e_icdar2015.py --work-dir dbnet_ali


# 检测
python tools/test.py configs/textdet/dbnet/dbnet_r18_fpnc_1200e_icdar2015.py final_60_epoch.pth --eval hmean-iou --show-dir dbnet_result



```







### 完整识别代码

- https://blog.csdn.net/jizhidexiaoming/article/details/124273621

```python

# https://blog.csdn.net/jizhidexiaoming/article/details/124273621

import os.path
 
import cv2
import torch
 
from mmocr.apis.inference import model_inference
from mmocr.apis import init_detector
from mmocr.utils import revert_sync_batchnorm
from mmocr.datasets.pipelines.crop import crop_img
from mmocr.core.visualize import det_recog_show_result
 
textdet_models = {
            'DB_r18': {
                'config':
                'dbnet/dbnet_r18_fpnc_1200e_icdar2015.py',
                'ckpt':
                'dbnet/'
                'dbnet_r18_fpnc_sbn_1200e_icdar2015_20210329-ba3ab597.pth'
            },
            'DB_r50': {
                'config':
                'dbnet/dbnet_r50dcnv2_fpnc_1200e_icdar2015.py',
                'ckpt':
                'dbnet/'
                'dbnet_r50dcnv2_fpnc_sbn_1200e_icdar2015_20211025-9fe3b590.pth'
            },
            'DRRG': {
                'config':
                'drrg/drrg_r50_fpn_unet_1200e_ctw1500.py',
                'ckpt':
                'drrg/drrg_r50_fpn_unet_1200e_ctw1500_20211022-fb30b001.pth'
            },
            'FCE_IC15': {
                'config':
                'fcenet/fcenet_r50_fpn_1500e_icdar2015.py',
                'ckpt':
                'fcenet/fcenet_r50_fpn_1500e_icdar2015_20211022-daefb6ed.pth'
            },
            'FCE_CTW_DCNv2': {
                'config':
                'fcenet/fcenet_r50dcnv2_fpn_1500e_ctw1500.py',
                'ckpt':
                'fcenet/' +
                'fcenet_r50dcnv2_fpn_1500e_ctw1500_20211022-e326d7ec.pth'
            },
            'MaskRCNN_CTW': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_ctw1500.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_ctw1500_20210219-96497a76.pth'
            },
            'MaskRCNN_IC15': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_icdar2015.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_icdar2015_20210219-8eb340a3.pth'
            },
            'MaskRCNN_IC17': {
                'config':
                'maskrcnn/mask_rcnn_r50_fpn_160e_icdar2017.py',
                'ckpt':
                'maskrcnn/'
                'mask_rcnn_r50_fpn_160e_icdar2017_20210218-c6ec3ebb.pth'
            },
            'PANet_CTW': {
                'config':
                'panet/panet_r18_fpem_ffm_600e_ctw1500.py',
                'ckpt':
                'panet/'
                'panet_r18_fpem_ffm_sbn_600e_ctw1500_20210219-3b3a9aa3.pth'
            },
            'PANet_IC15': {
                'config':
                'panet/panet_r18_fpem_ffm_600e_icdar2015.py',
                'ckpt':
                'panet/'
                'panet_r18_fpem_ffm_sbn_600e_icdar2015_20210219-42dbe46a.pth'
            },
            'PS_CTW': {
                'config': 'psenet/psenet_r50_fpnf_600e_ctw1500.py',
                'ckpt':
                'psenet/psenet_r50_fpnf_600e_ctw1500_20210401-216fed50.pth'
            },
            'PS_IC15': {
                'config':
                'psenet/psenet_r50_fpnf_600e_icdar2015.py',
                'ckpt':
                'psenet/psenet_r50_fpnf_600e_icdar2015_pretrain-eefd8fe6.pth'
            },
            'TextSnake': {
                'config':
                'textsnake/textsnake_r50_fpn_unet_1200e_ctw1500.py',
                'ckpt':
                'textsnake/textsnake_r50_fpn_unet_1200e_ctw1500-27f65b64.pth'
            },
            'Tesseract': {}
        }
 
textrecog_models = {
            'CRNN': {
                'config': 'crnn/crnn_academic_dataset.py',
                'ckpt': 'crnn/crnn_academic-a723a1c5.pth'
            },
            'SAR': {
                'config': 'sar/sar_r31_parallel_decoder_academic.py',
                'ckpt': 'sar/sar_r31_parallel_decoder_academic-dba3a4a3.pth'
            },
            'SAR_CN': {
                'config':
                'sar/sar_r31_parallel_decoder_chinese.py',
                'ckpt':
                'sar/sar_r31_parallel_decoder_chineseocr_20210507-b4be8214.pth'
            },
            'NRTR_1/16-1/8': {
                'config': 'nrtr/nrtr_r31_1by16_1by8_academic.py',
                'ckpt':
                'nrtr/nrtr_r31_1by16_1by8_academic_20211124-f60cebf4.pth'
            },
            'NRTR_1/8-1/4': {
                'config': 'nrtr/nrtr_r31_1by8_1by4_academic.py',
                'ckpt':
                'nrtr/nrtr_r31_1by8_1by4_academic_20211123-e1fdb322.pth'
            },
            'RobustScanner': {
                'config': 'robust_scanner/robustscanner_r31_academic.py',
                'ckpt': 'robustscanner/robustscanner_r31_academic-5f05874f.pth'
            },
            'SATRN': {
                'config': 'satrn/satrn_academic.py',
                'ckpt': 'satrn/satrn_academic_20211009-cb8b1580.pth'
            },
            'SATRN_sm': {
                'config': 'satrn/satrn_small.py',
                'ckpt': 'satrn/satrn_small_20211009-2cf13355.pth'
            },
            'ABINet': {
                'config': 'abinet/abinet_academic.py',
                'ckpt': 'abinet/abinet_academic-f718abf6.pth'
            },
            'SEG': {
                'config': 'seg/seg_r31_1by16_fpnocr_academic.py',
                'ckpt': 'seg/seg_r31_1by16_fpnocr_academic-72235b11.pth'
            },
            'CRNN_TPS': {
                'config': 'tps/crnn_tps_academic_dataset.py',
                'ckpt': 'tps/crnn_tps_academic_dataset_20210510-d221a905.pth'
            },
            'Tesseract': {}
        }
 
 
def single_inference(model, arrays, batch_mode, batch_size=0):
    def inference(m, a, **kwargs):
        return model_inference(m, a, **kwargs)
 
    result = []
    if batch_mode:
        if batch_size == 0:
            result = inference(model, arrays, batch_mode=True)
        else:
            n = batch_size
            arr_chunks = [
                arrays[i:i + n] for i in range(0, len(arrays), n)
            ]
            for chunk in arr_chunks:
                result.extend(inference(model, chunk, batch_mode=True))
    else:
        for arr in arrays:
            result.append(inference(model, arr, batch_mode=False))
    return result
 
 
def det_recog_kie_inference(det_model, recog_model, kie_model=None, imgs=None, batch_mode=False, recog_batch_size=0):
    end2end_res = []  # 所有图片的重要结果备份
 
    # 1， 定位（1orbatch）
    det_result = single_inference(det_model, imgs, batch_mode=batch_mode, batch_size=0)
    bboxes_list = [res['boundary_result'] for res in det_result]
 
    # 2, 识别（1orbatch）
    for img, bboxes in zip(imgs, bboxes_list):
        img_e2e_res = {}
        img_e2e_res['result'] = []  # 一张图片中检测到的所有文本位置，和内容
 
        box_imgs = []
        for bbox in bboxes:
            box_res = {}
            box_res['box'] = [round(x) for x in bbox[:-1]]  # 前8个是位置
            box_res['box_score'] = float(bbox[-1])  # 最后一个是概率
            box = bbox[:8]
            if len(bbox) > 9:  # 多边形bbox不止8个位置，返回的是轮廓点集合（xy,xy,...）
                min_x = min(bbox[0:-1:2])  # 从第一个开始到最后一个，间隔为2，找最小的x
                min_y = min(bbox[1:-1:2])  # 从第二个开始到最后一个，间隔为2，找最小的y
                max_x = max(bbox[0:-1:2])
                max_y = max(bbox[1:-1:2])
                box = [   # 最小外接矩形。
                    min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y
                ]
            # 2，裁剪
            box_img = crop_img(img, box)
            if batch_mode:
                box_imgs.append(box_img)  # 先打包成batch
            else:
                # 3，识别
                recog_result = model_inference(recog_model, box_img)
                text = recog_result['text']  # 文本内容
                text_score = recog_result['score']  # 概率
                if isinstance(text_score, list):
                    text_score = sum(text_score) / max(1, len(text))
                box_res['text'] = text
                box_res['text_score'] = text_score
            img_e2e_res['result'].append(box_res)
 
        if batch_mode:
            recog_results = single_inference(recog_model, box_imgs, True, recog_batch_size)
            for i, recog_result in enumerate(recog_results):
                text = recog_result['text']
                text_score = recog_result['score']
                if isinstance(text_score, (list, tuple)):
                    text_score = sum(text_score) / max(1, len(text))
                img_e2e_res['result'][i]['text'] = text
                img_e2e_res['result'][i]['text_score'] = text_score
        end2end_res.append(img_e2e_res)
    return end2end_res
 
 
# Post processing function for end2end ocr
def det_recog_pp(arrays, result, outputs=[None], imshow=True):
    final_results = []
    for arr, output, det_recog_result in zip(arrays, outputs, result):
        if output or imshow:
            res_img = det_recog_show_result(arr, det_recog_result, out_file=output)
            if imshow:
                cv2.namedWindow("inference results", cv2.WINDOW_NORMAL), cv2.imshow("inference results", res_img)
                cv2.waitKey()
                # mmcv.imshow(res_img, 'inference results')
 
 
if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
 
    img_dir = r"./demo"
    img_name_list = os.listdir(img_dir)
    img_name_list = [ 'demo_text_ocr.jpg' ]
    for img_name in img_name_list:
        # img
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (640, 640))
        # detection
        config_dir = r'./configs'
        td = "DB_r50"
        #det_ckpt = r"D:\code\python\mmocr\tools\work_dirs\dbnet_r50_0415\epoch_80.pth"
        det_config = os.path.join(config_dir, "textdet/", textdet_models[td]['config'])
        if True or (not det_ckpt):
            det_ckpt = 'https://download.openmmlab.com/mmocr/textdet/' + textdet_models[td]['ckpt']
        detect_model = init_detector(det_config, det_ckpt, device=device)
        detect_model = revert_sync_batchnorm(detect_model)
 
        # recognition
        tr = "SEG"
        recog_ckpt = None
        recog_config = os.path.join(config_dir, "textrecog/", textrecog_models[tr]['config'])
        if True or (not recog_ckpt):
            recog_ckpt = 'https://download.openmmlab.com/mmocr/' + 'textrecog/' + textrecog_models[tr]['ckpt']
        recog_model = init_detector(recog_config, recog_ckpt, device=device)
        recog_model = revert_sync_batchnorm(recog_model)
 
        # Attribute check
        for model in list(filter(None, [recog_model, detect_model])):
            if hasattr(model, 'module'):
                model = model.module
 
        det_recog_result = det_recog_kie_inference(
            detect_model, recog_model, kie_model=None, imgs=[img], batch_mode=False)
        det_recog_pp([img], det_recog_result, outputs=['./result.jpg'], imshow=False)
 
```



### 训练ICDAR 2015

- https://mmocr.readthedocs.io/en/latest/datasets/det.html

  > 数据转换
  >
  > ```
  > cd ~ && \
  > cp autodl-nas/icdar2015_aliocr.zip . && \
  > unzip icdar2015_aliocr.zip -d mmocr/data
  > 
  > cd ~/mmocr && \
  > source activate DB && \
  > mv data/icdar2015_aliocr data/icdar2015 && \
  > python tools/data/textdet/icdar_converter.py data/icdar2015 -o data/icdar2015 -d icdar2015 --split-list training test
  > ```
  >
  > 
  >
  > python tools/data/textdet/icdar_converter.py data/icdar2015 -o data/icdar2015 -d icdar2015 --split-list training test
  >
  > 开始训练
  >
  > ```
  > tmux && \
  > source activate DB && \
  > python tools/train.py configs/textdet/dbnet/dbnet_r18_fpnc_1200e_icdar2015.py --work-dir dbnet
  > 
  > tmux attach
  > ```
  >
  > 检测
  >
  > ```
  > python tools/test.py configs/textdet/dbnet/dbnet_r18_fpnc_1200e_icdar2015.py dbnet_r18_fpnc_sbn_1200e_icdar2015_20210329-ba3ab597.pth --eval hmean-iou --show-dir dbnet_result
  > 
  > 
  > python tools/test.py configs/textdet/dbnet/dbnet_r18_fpnc_1200e_icdar2015.py /root/mmocr/dbnet/epoch_150.pth --eval hmean-iou --show-dir dbnet_result
  > 
  > ```
  >

 

#### 多卡训练

- https://mmsegmentation.readthedocs.io/zh_CN/latest/train.html



### mmocr训练集可视化

- https://blog.csdn.net/jizhidexiaoming/article/details/124297467

```
# 以dbnet网络训练，icdar2015数据集为例

from mmcv import Config, imdenormalize
from mmocr.datasets import build_dataset
 
if __name__ == '__main__':
    import cv2
    import numpy as np
    import torch
 
    # config = r'D:\code\python\mmocr\configs\textdet\dbnet\dbnet_r50dcnv2_fpnc_1200e_icdar2015.py'
    config = r'D:\code\python\mmocr\configs\textdet\dbnet\dbnet_r50_dcnv2.py'
    cfg = Config.fromfile(config)
    datalayer = build_dataset(cfg.data.train)
    print(len(datalayer))
    for i, data_batch in enumerate(datalayer):
 
        img_info = data_batch['img_metas']
        img = data_batch["img"]
        gt_shrink = data_batch["gt_shrink"]
        gt_shrink_mask = data_batch["gt_shrink_mask"]
        gt_thr = data_batch["gt_thr"]
        gt_thr_mask = data_batch["gt_thr_mask"]
 
        img_norm_cfg = img_info.data["img_norm_cfg"]
        img_numpy = img.data.permute(1, 2, 0).detach().cpu().numpy()
        orig_img = imdenormalize(img_numpy, mean=img_norm_cfg["mean"], std=img_norm_cfg["std"], to_bgr=img_norm_cfg["to_rgb"])
 
        # (h, w ,1)
        gt_shrink = gt_shrink.data.masks.transpose(1, 2, 0)  # 图片上有值的地方是文本索引值，从1开始，像分割mask
        gt_shrink_mask = gt_shrink_mask.data.masks.transpose(1, 2, 0)  # mask. 通过polygons_ignore将不需要地方填0，其他地方都是1. 用于屏蔽不清晰文本
        gt_thr = gt_thr.data.masks.transpose(1, 2, 0)
        gt_thr_mask = gt_thr_mask.data.masks.transpose(1, 2, 0)
 
        print("img shape: ", img_numpy.shape)
        print("gt_shrink shape: ", gt_shrink.shape)
        print("gt_shrink_mask shape: ", gt_shrink_mask.shape)
        print("gt_thr shape: ", gt_thr.shape)
        print("gt_thr_mask shape: ", gt_thr_mask.shape)
 
        cv2.namedWindow("orig_img", cv2.WINDOW_NORMAL), cv2.imshow("orig_img", np.uint8(orig_img))
        cv2.namedWindow("gt_shrink", cv2.WINDOW_NORMAL), cv2.imshow("gt_shrink", np.uint8(gt_shrink*255))
        cv2.namedWindow("gt_shrink_mask", cv2.WINDOW_NORMAL), cv2.imshow("gt_shrink_mask", gt_shrink_mask*255)
        cv2.namedWindow("gt_thr", cv2.WINDOW_NORMAL), cv2.imshow("gt_thr", np.uint8(gt_thr*255))
        cv2.namedWindow("gt_thr_mask", cv2.WINDOW_NORMAL), cv2.imshow("gt_thr_mask", gt_thr_mask*255), cv2.waitKey()
```



### mmocr DBLoss

- https://blog.csdn.net/jizhidexiaoming/article/details/124342274

  > 详细网络结构，有大图

![](深入理解神经网络：从逻辑回归到CNN.assets/dbnet网络结构.jpg)

DBLoss由三种loss组成。

#### 1. balance bce loss

```python
balance_bce_loss(pred=pred_prob, gt=gt_shrink, mask=gt_shrink_mask)
```

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20220907083339531.png" alt="image-20220907083339531" style="zoom:80%;" />

```
def balance_bce_loss(self, pred, gt, mask):
    """
    pred: (b, w,h) 预测分数image, (0, 1)之间；
    gt: (b, w,h) label image, 值0或者1；
    mask：(b, w,h) 屏蔽背景位置，其中屏蔽位置为0，保留位置为1
    """
    positive = (gt * mask)  # positive前景位置，前景位置值为1，其他位置为0（利用mask屏蔽不需要训练的位置，比如字符检测时，模糊不清的字符）
    negative = ((1 - gt) * mask)  # negative背景位置，（1-gt是背景位置，再利用mask屏蔽不训练的背景位置。）
    positive_count = int(positive.float().sum())  # 前景面积
    negative_count = min(
        int(negative.float().sum()),
        int(positive_count * self.negative_ratio))  # 背景面积。（利用negative_ratio，背景区域不能大于前景的3倍）
 
    assert gt.max() <= 1 and gt.min() >= 0
    assert pred.max() <= 1 and pred.min() >= 0
    loss = F.binary_cross_entropy(pred, gt, reduction='none')  # 所有位置的loss: (b, w, h)
    positive_loss = loss * positive.float()  # 前景位置的loss
    negative_loss = loss * negative.float()  # 背景位置的loss
 
    negative_loss, _ = torch.topk(negative_loss.view(-1), negative_count)  # 只取前negative_count个背景位置的loss
 
    balance_loss = (positive_loss.sum() + negative_loss.sum()) / (
        positive_count + negative_count + self.eps)  # 最后把所有位置的loss相加，求平均。
 
    return balance_loss
```



#### 2. dice loss 

和前面bce loss输入的label是一样的。 前面的**bce loss同时关注前后景**，**dice_loss只关注前景**。

```python
dice_loss(pred=pred_db, gt=gt_shrink, mask=gt_shrink_mask)
```

```
def forward(self, pred, target, mask=None):
    """
            pred: (b, w,h) 预测分数image, (0, 1)之间；
            target: (b, w,h) label image, 值0或者1；
            mask：(b, w,h) 屏蔽背景位置，其中屏蔽位置为0，保留位置为1
    """
    pred = pred.contiguous().view(pred.size()[0], -1)  # (b, w*h)
    target = target.contiguous().view(target.size()[0], -1)  # (b, w*h)
 
    if mask is not None:
        mask = mask.contiguous().view(mask.size()[0], -1)  # (b, w*h)
        pred = pred * mask  # 利用mask，将不需要参与训练的预测值置零
        target = target * mask  # 利用mask，将不需要参与训练的label值置零
 
    a = torch.sum(pred * target)  # 这里往后就是dice loss公式了： 1 - 2|A*B| / ( |A| + |B|)
    b = torch.sum(pred)
    c = torch.sum(target)
    d = (2 * a) / (b + c + self.eps)
 
    return 1 - d
```



#### 3. l1 loss

求绝对值距离。 

```python
l1_th_loss(pred=pred_thr, gt=gt_thr, mask=gt_thr_mask)
```

```
def l1_thr_loss(self, pred, gt, mask):
    """
    l1: pred与gt差值绝对值的平均值。
    Args:
        pred: torch.Size([8, 640, 640]).
        gt: torch.Size([8, 640, 640]).
        mask: torch.Size([8, 640, 640]). 只计算mask位置的loss：mask位置的预测值与真实值之间差值绝对值的平均值。
    Returns:
    """
    thr_loss = torch.abs((pred - gt) * mask).sum() / (
        mask.sum() + self.eps)
    return thr_loss
```





### tensorboard可视化训练

```
if self.every_n_inner_iters(runner, self._print_interval_iter):
# loss
loss = runner.batch_iter_output['batch_loss']
prob_dice_loss = runner.batch_iter_output['prob_dice_loss']
thres_dice_loss = runner.batch_iter_output['thres_dice_loss']
thres_l1_loss = runner.batch_iter_output['thres_l1_loss']
 
summary_fun.add_scalar('batch_loss', loss, iters)
summary_fun.add_scalar('prob_dice_loss', prob_dice_loss, iters)
summary_fun.add_scalar('thres_dice_loss', thres_dice_loss, iters)
summary_fun.add_scalar('thres_l1_loss', thres_l1_loss, iters)
 
# orig image and label
target = runner.data_batch[1]  # list
input_tensor = runner.data_batch[0]  # torch.Size([8, 3, 512, 512])
 
input_tensor = input_tensor.detach().cpu().permute(0, 2, 3, 1).numpy() * 255
gt_shrink = target[0].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
gt_shrink_mask = target[1].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
gt_thr = target[2].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
gt_thr_mask = target[3].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
 
# loss and predict
output = runner.batch_iter_output['prediction']
pred_prob = output[0].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
pred_db = output[1].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
pred_thr = output[2].detach().cpu().permute(0, 2, 3, 1).numpy() * 255
 
 
all_img = []
for i in range(input_tensor.shape[0]):
    one_img = input_tensor[i, :, :, :]
    one_gt_shrink = cv2.cvtColor(gt_shrink[i, :, :, :], cv2.COLOR_GRAY2BGR)
    one_gt_shrink_mask = cv2.cvtColor(gt_shrink_mask[i, :, :, :], cv2.COLOR_GRAY2BGR)
    one_gt_thr = cv2.cvtColor(gt_thr[i, :, :, :], cv2.COLOR_GRAY2BGR)
    one_gt_thr_mask = cv2.cvtColor(gt_thr_mask[i, :, :, :], cv2.COLOR_GRAY2BGR)
 
    one_pred_prob = cv2.cvtColor(pred_prob[i, :, :, :], cv2.COLOR_GRAY2BGR)
    one_pred_db = cv2.cvtColor(pred_db[i, :, :, :], cv2.COLOR_GRAY2BGR)
    one_pred_thr = cv2.cvtColor(pred_thr[i, :, :, :], cv2.COLOR_GRAY2BGR)
 
    one_row_img = np.hstack((one_img, one_pred_prob, one_pred_db, one_gt_shrink, one_gt_shrink_mask, one_pred_thr, one_gt_thr, one_gt_thr_mask))
    # cv2.namedWindow("img", cv2.WINDOW_NORMAL), cv2.imshow("img", np.uint8(one_row_img)), cv2.waitKey()
    all_img.append(one_row_img)
 
all_img_numpy = np.vstack(all_img)
all_input_tensor = torch.from_numpy(all_img_numpy / 255.).unsqueeze(0).permute(0, 3, 1, 2)
# train_image = vutils.make_grid(all_input_tensor, normalize=True, scale_each=False)
# summary_fun.add_image('{}_image'.format(mode), train_image, iters)
train_predict = vutils.make_grid(all_input_tensor, normalize=True, scale_each=False, padding=0)
summary_fun.add_image('{}_predict_{}'.format(mode, self._print_interval_iter), train_predict, iters)
```



## 单机多卡负载均衡

[pytorch 单机多卡负载均衡](https://blog.csdn.net/weixin_43922901/article/details/106117774)



### 数据分片

**模型并行（Model Parallel）**在**分布式训练技术**中被广泛使用。先前的文章已经解释了如何使用 [DataParallel](https://zhuanlan.zhihu.com/p/87652320) 在多个GPU上训练神经网络。其中，DataParallel的优缺点如下：

**优点：将相同的模型复制到所有GPU，其中每个GPU消耗输入数据的不同分区，可以极大地加快训练过程。**

**缺点：不适用于某些模型太大而无法容纳单个GPU的用例**。 



### 模型分片

该模型**将单个模型拆分到不同的GPU上，而不是在每个GPU上复制整个模型**（具体来说，模型 `m`包含10层：使用时 `DataParallel`，则每个GPU都具有这10层中每个层的副本，而在两个GPU上使用模型并行时，每个GPU可以托管5层）。

模型并行的高级思想是**将模型的不同子网放置到不同的设备上，并相应地实现该 `forward`方法以在设备之间移动中间输出。由于模型的一部分只能在任何单个设备上运行，因此一组设备可以共同为更大的模型服务**。在本文中，我们不会尝试构建庞大的模型并将其压缩到有限数量的GPU中。取而代之的是，本文着重展示模型并行的思想。读者可以将这些想法应用到实际应用中。



## halcon

https://blog.csdn.net/songhuangong123/article/details/129146123  【halcon】模板匹配和仿射变换总结

```
HALCON是德国MVtec公司开发的一套完善的标准的机器视觉算法包
```





## PaddleOCR

##### manga-ocr

- https://github.com/kha-white/manga-ocr

  - https://github.com/kha-white/mokuro

    - https://github.com/dmMaze/comic-text-detector

      - https://github.com/juvian/Manga-Text-Segmentation

      - https://t.me/SugarPic

- https://github.com/dmMaze/BallonsTranslator  漫画自动翻译

- https://github.com/PaddlePaddle/PaddleOCR/issues/10815  返回单个字坐标

- https://github.com/kha-white/manga-ocr  see nodejs summary -> C++ monads -> Implay -> Memento

- https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/recognition.md

  - https://github.com/PaddlePaddle/PaddleOCR/blob/static/doc/doc_ch/FAQ.md

  > 训练文档

- https://juejin.cn/post/6956430529952481310  PaddleOCR二次全流程——5.FAQ记录

- https://blog.csdn.net/wss794/article/details/122451815  

  > paddleocr：使用自己的数据集微调文字识别模型

- https://www.jianshu.com/p/07623c6bc899  Python PaddleOCR 识别图片中的中文

- https://blog.csdn.net/YY007H/article/details/124973777 单行文本识别

- https://zhuanlan.zhihu.com/p/523972865 PPv3-OCR自定义数据从训练到部署

- https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_ch/knowledge_distillation.md

  > 中文识别推荐用的是知识蒸馏 

- https://github.com/PaddlePaddle/PaddleOCR/issues/7482、

  > SynthText/MJsynth/Synthetic-Chinese-String-Dataset   中文数据集

- https://github.com/PaddlePaddle/PaddleOCR/issues/5921 超大分辨率

  > ```
  > 关于RecAug，源代码实现在ppocr/data/imaug/rec_img_aug.py文件中，参数主要包含不同方法的概率，默认参数是我们调整后比较好的参数了，可以在这里debug看下
  > 关于RecConAug，源代码也在ppocr/data/imaug/rec_img_aug.py文件中，参数主要包含概率，图像shape，ext_data_num参数，这个ext_data_num指的是最多concat的图像数量，默认1的话效果已经很好了，训练数据都是短文本的话，可以设置为2试下。
  > ```

  > ```
  > 1.如你所说，最长边小于该参数时，不做resize操作。
  > 2.有的网络是固定尺寸输入的，所以需要你把图片resize成相同大小，这一情况取决于网络的设定，通常来说分类和目标检测网络使用这一设置。当前paddleocr主推的dbnet文本检测，使用基于语义分割的文本检测，并不需要固定尺寸。裁剪为边长=del_limit_side_len（默认值为960）
  > ```

- https://github.com/PaddlePaddle/PaddleOCR/issues/5021  图片尺寸不规则导致无法识别

  > PaddleOCR(use_angle_cls=True, lang="ch", det_limit_type='min', det_limit_side_len=64)
  > 设定短边的最小分辨率，用你的image图片，det_limit_side_len=64，文字全能检测出来。
  >
  > 默认参数是det_limit_type='max', det_limit_side_len=960，也就是长边最大960.
  >
  > 改为det_limit_type='min', det_limit_side_len=64，也就是短边最小64.

- https://blog.csdn.net/m0_63642362/article/details/122755254  PPOCR文本检测+识别：电表读数和编号识别

- https://aistudio.baidu.com/aistudio/projectdetail/4330587  **实战  讲解详细**

use_shared_memory: False

character_type: CN



#### 最新版

```

see huggingface/PPOCRLabel
	# 图片标注这个是正常的, 原来那个框选就报错了

ubuntu20.04 + Python3.8 + Cuda11.2 + 3090(24GB) + 内存160GB
	# 成功训练的配置

conda install paddlepaddle-gpu==2.3.2 cudatoolkit=11.6 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge
	# 4090 用这个, 4090 可以用 11.3 及以上，官方说最低 11.8 ，实际上大可不必。
	# paddlepaddle-gpu==2.3.2 不可以用 11.3 , 也不可以 11.7 ，所以只能是 11.6 了


# autodl
~/miniconda3/bin/conda init && \
ln -s ~/miniconda3/bin/conda /usr/local/bin && \
ln -s ~/miniconda3/bin/activate /usr/local/bin && \
ln -s ~/miniconda3/bin/deactivate /usr/local/bin && \
source ~/miniconda3/etc/profile.d/conda.sh

conda create -n PP python==3.8 pip && 
conda activate PP && 
pip install paddlepaddle-gpu==2.6.1
	# 实测 4090 2.6.1 正常 (ubuntu20.04 + Python3.8 + Cuda11.6 + paddlepaddle-gpu==2.6.1)
	# https://pypi.org/project/paddlepaddle-gpu/2.6.1/
		# Ubuntu 16.04/18.04/20.04/22.04 (GPUVersion Supports CUDA 10.2/11.2/11.6/11.7)
		# Python Version: 3.8/3.9/3.10/3.11/3.12 (64 bit)
			# 这些都是支持的

vi requirements.txt
paddlepaddle-gpu==2.6.1
pyyaml==6.0.2
numpy==1.23.5
shapely==2.0.6
scikit-image==0.21.0
imgaug==0.4.0
pyclipper==1.3.0.post6
lmdb==1.5.1
tqdm==4.66.6
visualdl==2.5.3
rapidfuzz==3.9.7
opencv-contrib-python==4.10.0.84
Cython==3.0.11
lxml==5.3.0
premailer==3.10.0
openpyxl==3.1.5
attrdict==2.0.1

huggingface/project/ppcor_aliocr_convert.py
	# aliocr 图片识别结果自动生成框选

huggingface\PPOCRLabel\PPOCRLabel.py
	# 查看 aliocr 图片生成的框选

PaddleOCR/PPOCRLabel/gen_ocr_train_val_test.py
	# PaddleOCR/train_data 生成的图片放这里
	# 生成训练集和测试集

python tools/train.py -c configs/det/det_res18_db_v2.0.yml
	# 开始检测训练

vi /root/PaddleOCR/configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml
    decay_epochs : [700, 800]
    values : [0.001, 0.0005, 0.0001]
    	# 改成这样

python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml
	# 开始识别训练



# 检测模型推断
python tools/infer_det.py -c configs/det/det_res18_db_v2.0.yml  -o Global.checkpoints="output/ch_db_res18/best_accuracy" image_dir="train_data/det/test/12.jpg"

	PaddleOCR/configs/det/det_res18_db_v2.0.yml
		Global:
  			use_gpu: false
  				# 如果没有 gpu 把这里设成 false


# 检测模型导出后推断
python tools/export_model.py -c configs/det/det_res18_db_v2.0.yml -o Global.checkpoints=output/ch_db_res18/best_accuracy Global.save_inference_dir=output/det_model

python tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="output/det_model" --image_dir="train_data/det/test/12.jpg" --use_gpu=True --det_limit_side_len=960 --det_db_unclip_ratio=3.5


nvidia-smi
	# 查看显存占用， ps -al 然后 kill -9
	
systemctl restart nvidia-persistenced
	# 重启 cuda 服务


https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_en/inference_ppocr_en.md

You can use the parameters limit_type and det_limit_side_len to limit the size of the input image, The optional parameters of limit_type are [max, min], and det_limit_size_len is a positive integer, generally set to a multiple of 32, such as 960.

The default setting of the parameters is limit_type='max', det_limit_side_len=960. Indicates that the longest side of the network input image cannot exceed 960, If this value is exceeded, the image will be resized with the same width ratio to ensure that the longest side is det_limit_side_len. Set as limit_type='min', det_limit_side_len=960, it means that the shortest side of the image is limited to 960.

If the resolution of the input picture is relatively large and you want to use a larger resolution prediction, you can set det_limit_side_len to the desired value, such as 1216:

python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./ch_PP-OCRv3_det_infer/" --det_limit_type=max --det_limit_side_len=1216
If you want to use the CPU for prediction, execute the command as follows

python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./ch_PP-OCRv3_det_infer/"  --use_gpu=False




mega-cmd
login 1234xxxxx@qq.com  xxxxCNxxxx
put /root/miniforge3_PP_cuda117.tar
	# .77 先装好环境

mkdir -p /root/autodl-tmp/PaddleOCR
ln -s /root/PaddleOCR/train_data/ /root/autodl-tmp/PaddleOCR

python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml
	# 4090 正常训练
	# Python3.8 + ubuntu20.04 + Cuda11.6 + RTX 4090(24GB) 
	

>>> import blinker
>>> blinker.__file__
'/usr/lib/python3/dist-packages/blinker/__init__.py'

rm -rf /usr/lib/python3/dist-packages/blinker*


git clone https://github.com/PaddlePaddle/PaddleOCR 
	# 2024.5.30 PaddleOCRv2.7.5
	# 2024.5.30	PaddlePaddle 2.6.1
	
python3.10 -m pip install paddlepaddle==2.6.1 -i https://mirror.baidu.com/pypi/simple

pip install paddlepaddle-gpu==2.6.1
	# gpu 可能不会出错


Illegal instruction

	lscpu|grep -i flags

Thank you for reporting this issue. It can be fixed by PR(https://github.com/PaddlePaddle/Paddle/pull/64132) , We skip SelfAttentionFusePass on non-avx512 platform

	# gpu 可能就没错


nvidia-smi
nvcc -V
ldconfig -p | grep cuda
ldconfig -p | grep cudnn
conda list | grep cudatoolkit
	# 康达安装的
	# autodl 默认镜像都内置了原生的CUDA和cuDNN，如果您自己安装了cudatoolkits等，那么一般会默认优先使用conda中安装的cudatoolkits



vi ~/.condarc
proxy_servers:
  http: http://172.16.6.253:8118
  https: http://172.16.6.253:8118
ssl_verify: false
	# 康达设置代理

conda clean -a
	# 代理是OK 的，出错执行这个就可以了
	

export PATH=/usr/local/cuda-11.8/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:$LD_LIBRARY_PATH


curl --socks5 192.168.1.3:57882 google.com

unset http_proxy && unset https_proxy


ln -s /root/PaddleOCR/train_data/  /root/autodl-tmp/PaddleOCR
	# 现在要反向 ln 了, train_data 直接在目录下，不知道配置哪里指定了 autodl-tmp
	

# 空间不够用软链接
ln -s /root/autodl-tmp/train_data /root/PaddleOCR/train_data

cd PPOCRLabel && \
python gen_ocr_train_val_test.py

# 训练
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml

# 继续上一次训练(epoch 接着上一次的断点开始)
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.checkpoints=output/rec_ppocr_v3_distillation/best_accuracy

# 微调 (epoch 从一开始)
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.pretrained_model=output/rec_ppocr_v3_distillation/best_accuracy

# 导出模型
python tools/export_model.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.checkpoints=output/rec_ppocr_v3_distillation/best_accuracy Global.save_inference_dir=output/model

# 推断
python tools/infer/predict_rec.py --image_dir=train_data/rec/test/1_crop_0.jpg --rec_model_dir=output/model/Student --rec_char_dict_path=train_data/keys.txt
	# train_data/keys.txt 是自已生成的自定义词典，训练的时侯也要指定这个词典
​```


miniconda pkgs
不论base环境还是虚拟环境都是放在pkgs文件夹下。如果虚拟环境需要安装的包与pkgs中已有的包版本完全一样，则不会再下载，而是通过硬盘链接直接找到该包，反之当一个包被多个环境使用时，从某一个环境卸载该包也不会将其从pkgs文件夹删除

```



#### ppcor_aliocr_convert.py

```
see python summary.md -> OpenCV -> ppcor_aliocr_convert.py
```



```

see huggingface/project/ppcor_aliocr_convert.py

"""
# pip install numpy==1.23.5 opencv-python==4.10.0.84 -i https://mirrors.aliyun.com/pypi/simple/

PPOCRLabel --lang ch  # 启动标注工具

cp autodl-tmp/train_data.zip . && \
unzip train_data.zip -d PaddleOCR

# https://github.com/PaddlePaddle/PaddleOCR/blob/static/doc/doc_ch/FAQ.md

# 7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on data.7z data/

新建文件夹 train_data, 要标注的图片全部放在里面

新建 train_data/Label.txt 内容如下
行中用 \t 分隔 , points 的标记顺序是 左上 右上  右下 左下
train_data/0093.bmp	[{"transcription":"参考答案及解析","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]
train_data/0094.bmp	[{"transcription":"其他内容","points":[[525,179],[1295,167],[1295,268],[521,292]],"difficult":false}]


给 PaddleOCR 用，前面是坐标和图片都变换；这里图像不变，坐标不变


将阿里OCR 的识别结果（图片和标注）转换成 icdar2015 格式 (注意：它的文本是含 utf8 bom 的)

给 mmocr 训练用。格式是 icdar2015 的格式，文件夹的组织方式是按照 mmocr 的要求创建的

"""


"""

! unzip ./GD500.zip -d DB/datasets

icdar2015 文本检测数据集
标注格式: x1,y1,x2,y2,x3,y3,x4,y4,text

其中, x1,y1为左上角坐标,x2,y2为右上角坐标,x3,y3为右下角坐标,x4,y4为左下角坐标。

# 表示text难以辨认。
"""

import random
from pathlib import Path
import os
import shutil
import glob
import base64
from importlib.resources import path
import math
import numpy as np
import cv2
import json
import decimal
import datetime
from pickletools import uint8
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)


def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()


def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

# convert string to json


def parse(s):
    return json.loads(s, strict=False)

# convert dict to string


def string(d):
    return json.dumps(d, cls=DecimalEncoder, ensure_ascii=False)


def transform(points, M):
    # points 算出四个点变换后移动到哪里了
    # points = np.array([[word_x,  word_y],              # 左上
    #                    [word_x + word_width, word_y],                 # 右上
    #                    [word_x + word_width, word_y + word_height],  # 右下
    #                    [word_x, word_y + word_height],  # 左下
    #                    ])
    # add ones
    ones = np.ones(shape=(len(points), 1))

    points_ones = np.hstack([points, ones])

    # transform points
    transformed_points = M.dot(points_ones.T).T

    transformed_points_int = np.round(
        transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

    return transformed_points_int


def cutPoly(img, pts):
    # img = cv2.imdecode(np.fromfile('./t.png', dtype=np.uint8), -1)
    # pts = np.array([[10,150],[150,100],[300,150],[350,100],[310,20],[35,10]])

    # (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y+h, x:x+w].copy()

    # (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    # (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    # (4) add the white background
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst

    # cv2.imwrite("croped.png", croped)
    # cv2.imwrite("mask.png", mask)
    # cv2.imwrite("dst.png", dst)
    # cv2.imwrite("dst2.png", dst2)

    return dst2


def md5(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_all_md5():
    m5s = []
    import glob
    jpgs = glob.glob('./bookimage/**/*.jpg', recursive=True)
    for jpg in jpgs:
       m5 = md5(jpg)
       m5s.append( m5 )
    return m5s

def get_json_paths():
    json_paths = []
    m5s = get_all_md5()
    for m5 in m5s:
        j_pth = f"project/ocr_server_test/data/json/{m5.lower()}.json"
        if os.path.exists(j_pth):
            json_paths.append(j_pth)
    return json_paths

if __name__ == "__main__":

    # 24HLZYZG64/0001.jpg c04d111ef69b9892d39f9430b6906047 md5是这个
        # ls project/ocr_server_test/data/json/0bf0383ece9a533683e615bf57525812.json  aliocr 原始识别结果
        # ls project/ocr_server_test/data/img/0bf0383ece9a533683e615bf57525812.txt    aliocr 原始识别图像（二值化降燥后压缩成2M）



    root = 'train_data'
    tmp = 'tmp'
    label_path = os.path.join(root, 'Label.txt')
    
    key_path = os.path.join(root, 'keys.txt')

    fileState_path = os.path.join(root, 'fileState.txt')

    if os.path.exists(root):
        shutil.rmtree(root)
        # os.rmdir(root)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)

    if not os.path.exists(root):
        os.makedirs(root)

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    label = ''
    keys = ''
    states = ''


    dic_words = {}  # 所有词

    # 开始转换

    # https://help.aliyun.com/document_detail/294540.html 阿里云ocr结果字段定义
    # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换

    dir_json = 'project/ocr_server_test/data/json' # './data/json'  
    dir_img = 'project/ocr_server_test/data/img'        # './data/img'  

    g_count = 1
    g_count2 = 1


    # json_paths = glob.glob('{}/*.json'.format(dir_json), recursive=False)


    json_paths = get_json_paths()

    for json_path in json_paths:

        arr = []

        base = Path(json_path).stem

        # if base == '0bf0383ece9a533683e615bf57525812':
        #     continue

        img_path = os.path.join(dir_img, '{}.txt'.format(base))

        if not os.path.exists(img_path):  # 没有相应的图片，可能被删除了
            print(f'Warnnig: no image {img_path}')
            continue

        jsn = load_json(json_path)

        if not ('prism_wordsInfo' in jsn):
            print(f'Warning: no charater in {img_path}')
            continue

        with open(img_path, "r", encoding="utf-8") as fp:
            imgdata = fp.read()
            imgdata = base64.b64decode(imgdata)
            imgdata = np.frombuffer(imgdata, np.uint8)
            img = cv2.imdecode(imgdata, cv2.IMREAD_UNCHANGED)

            # cv2.imshow('img', img)
            # cv2.waitKey(0)

        if len(img.shape) != 3:  # 转彩图
            img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # DBNet 原版只能处理彩图，这里转一下

        else:
            img_color = img.copy()

        img_color_origin = img_color.copy()
        img_color_origin2 = img_color.copy()

        name = f'{g_count}.jpg'
        dst_img_path = f'{root}/{name}'
        states += f'G:\\train_data\\{name}\t1\n'
        g_count += 1

        cv2.imwrite(dst_img_path, img)

        wordsInfo = jsn['prism_wordsInfo']
        for j in range(len(wordsInfo)):
            jo = wordsInfo[j]
            word = jo["word"]

            for w in list(word):
                if not (w in dic_words):
                    dic_words[w] = True

            # prism-wordsInfo 里的 angle 文字块的角度，这个角度只影响width和height，当角度为-90、90、-270、270，width和height的值需要自行互换
            angle = jo['angle']

            img_color = img_color_origin.copy()

            word_x = jo['x']
            word_y = jo['y']
            word_width = jo['width']
            word_height = jo['height']

            if abs(angle) == 90 or abs(angle) == 270:
                word_width = jo['height']
                word_height = jo['width']
            elif angle != 0:

                # 变换前画出绿框，方便追踪点的前后变化
                # img_color = cv2.rectangle(img_color, (word_x, word_y), (
                #     word_x + word_width, word_y + word_height), (0, 255, 0), 2)  # 矩形的左上角, 矩形的右下角

                # cv2.imshow("green", img_color)
                # cv2.waitKey(0)

                # 变换前的多边形蓝框
                points = np.array([
                    [word_x,  word_y],                             # 左上
                    [word_x + word_width, word_y],                 # 右上
                    [word_x + word_width, word_y + word_height],  # 右下
                    [word_x, word_y + word_height],                # 左下
                ])

                # # cv2.fillPoly(img_color, pts=[points], color=(255, 0, 0)) # 填充
                # cv2.polylines(img_color, [points], isClosed=True, color=(
                #     255, 0, 0), thickness=1)  # 只画线，不填充

                # cv2.imshow("polys", img_color)
                # cv2.waitKey(0)

                # 获取图像的维度，并计算中心
                (h, w) = img_color.shape[:2]
                (cX, cY) = (w // 2, h // 2)

                # - (cX,cY): 旋转的中心点坐标
                # - 180: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
                # - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
                # 1° = π/180弧度   1 弧度 =  180 / 3.1415926   // 0.0190033 是Mathematica 算出来的弧度，先转换成角度  // -0.0190033 * (180 / 3.1415926)
                M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
                img_color = cv2.warpAffine(img_color, M, (w, h))
                img_color_transform = img_color.copy()

                # cv2.imshow("after trans", img_color)
                # cv2.waitKey(0)

                # https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html  # 原理
                # https://stackoverflow.com/questions/30327659/how-can-i-remap-a-point-after-an-image-rotation # How can I remap a point after an image rotation?
                # 如何得到移动后的坐标点

                # points 算出四个点变换后移动到哪里了
                points = np.array([[word_x,  word_y],              # 左上
                                   # 右上
                                   [word_x + word_width, word_y],
                                   [word_x + word_width, word_y + \
                                       word_height],  # 右下
                                   [word_x, word_y + word_height],  # 左下
                                   ])
                # add ones
                ones = np.ones(shape=(len(points), 1))

                points_ones = np.hstack([points, ones])

                # transform points
                transformed_points = M.dot(points_ones.T).T

                transformed_points_int = np.round(
                    transformed_points, decimals=0).astype(np.int32)  # 批量四舍五入

                # cv2.polylines(img_color, [transformed_points_int], isClosed=True, color=(
                #     0, 0, 255), thickness=2)  # 画转换后的点

                # cv2.polylines(img_color_origin, [points], isClosed=True, color=(
                #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

                # cv2.imshow("orgin", img_color_origin)
                # cv2.waitKey(0)

            # 四个角的位置 # 左上、右上、右下、左下，当NeedRotate为true时，如果最外层的angle不为0，需要按照angle矫正图片后，坐标才准确（错，经验证不需要）
            pos = jo["pos"]
            x = int(pos[0]["x"])  # 左上
            y = int(pos[0]["y"])

            x2 = int(pos[2]["x"])  # 右下
            y2 = int(pos[2]["y"])

            lu = [pos[0]['x'], pos[0]['y']]  # left up  四个角顺时针方向数
            ru = [pos[1]['x'], pos[1]['y']]
            rd = [pos[2]['x'], pos[2]['y']]
            ld = [pos[3]['x'], pos[3]['y']]

            # 生成 icdar2015 格式的人工标记训练数据（用于训练 mmocr）
            # gt_txt_list.append( "{},{},{},{},{},{},{},{},{}".format(lu[0], lu[1], ru[0], ru[1], rd[0], rd[1], ld[0], ld[1], word) )

            # 绘制矩形
            start_point = (x, y)  # 矩形的左上角

            end_point = (x2, y2)  # 矩形的右下角

            color = (0, 0, 255)  # BGR

            thickness = 2

            # 逐行画框
            # img_color_origin2 = cv2.rectangle(img_color_origin2, start_point, end_point, color, thickness)
            # cv2.imshow("box", img_color_origin2)

            # cv2.waitKey(0)

            points = [lu, ru, rd, ld]

            points0 = np.array([[word_x,  word_y],              # 左上
                                  # 右上
                                  [word_x + word_width, word_y],
                                    [word_x + word_width, word_y + \
                                     word_height],  # 右下
                                    [word_x, word_y + word_height],  # 左下
                                  ])
            points1 = np.array([lu, ru, rd, ld])

            if not (abs(angle) == 90 or abs(angle) == 270) and angle != 0:
                points = transform(points, M)
            else:
                points = np.array(points)

            ps3 = np.array(
                [
                    [min(points[0][0], points1[0][0]), min(
                        points[0][1], points1[0][1])],  # 左上(取最两者中最小的)

                    [max(points[1][0], points1[1][0]), min(
                        points[1][1], points1[1][1])],  # 右上

                    [max(points[2][0], points1[2][0]), max(
                        points[2][1], points1[2][1])],  # 右下

                    [min(points[3][0], points1[3][0]), max(
                        points[3][1], points1[3][1])]  # 左下
                ]
            )

            # img_cuted = cutPoly(img, points1)
            # cv2.imwrite(f'./tmp/{g_count2}.jpg', img_cuted)
            # with open(f'./tmp/{g_count2}.txt', 'w', encoding='utf-8') as f:
            #     f.write(word)
            # g_count2 += 1

            # cv2.polylines(img_color_origin, [points], isClosed=True, color=(   # 多边形，框得比较全
            #     100, 0, 255), thickness=2)  # 只画线，不填充

            
            arr.append( {"transcription":f"{word}","points":[lu, ru, rd, ld],"difficult":False} )


            cv2.polylines(img_color_origin, [points1], isClosed=True, color=(
                random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=2)  # 画转换前的点

            # cv2.polylines(img_color_origin, [ps3], isClosed=True, color=(255, 0, 0), thickness=2)

            # cv2.imshow("orgin", img_color_origin)
            # cv2.waitKey(0)

            # break


        arr_str = string(arr)
        line = f'{dst_img_path}\t{arr_str}\n'
        label += line

        print( f'{g_count - 1} / {len(json_paths)} task done.' )

    ks = list( dic_words.keys() )

    keys = '\n'.join(ks)

    with open(label_path, "w", encoding='utf-8') as fp:
        fp.write(label)

    with open(key_path, "w", encoding='utf-8') as fp:
        fp.write(keys)

    with open(fileState_path, "w", encoding='utf-8') as fp:
        fp.write(states)

    print('all task done.')

```





#### PaddleOCR_ali1k_det_rec_300epoch



https://github.com/PaddlePaddle/PaddleOCR/issues/11597

- ```
  
  pip install numpy==1.23.5 opencv-python==4.10.0.84 -i https://mirrors.aliyun.com/pypi/simple/
  
  
  Illegal instruction 错误
  
  It can be fixed by PR , We skip SelfAttentionFusePass on non-avx512 platform
  
  pip uninstall paddlepaddle
  
  python3.8 + cuda11.6
  pip install paddlepaddle==2.4.2
  protobuf==3.20 pip install pyyaml
  
  
  pip install -r requirements.txt
  
  python tools/infer/predict_rec.py --image_dir=train_data/rec/test/1_crop_5.jpg --rec_model_dir=output/rec_model/Student --rec_char_dict_path=train_data/keys.txt
  
  
  huggingface/rwkv5-jp-explain-docker/PaddleOCR_ali1k_det_rec_300epoch/ppocr/postprocess/db_postprocess.py
  	np.int = np.int32
  	np.float = np.float64
  	np.bool = np.bool_
  		# 加入。numpy 版本升级没有 np.int 了
          
   
   font_path = args.vis_font_path
   ./doc/fonts/simfang.ttf
  
  
  # vscode F5 运行
  rwkv5-jp-explain-docker/PaddleOCR_ali1k_det_rec_300epoch/tools/infer/predict_system.py
   if __name__ == "__main__":
      
      """
      python3 tools/infer/predict_system.py \
      --image_dir="train_data/det/test/25.jpg" \
      --det_algorithm="DB" \
      --det_model_dir="output/det_model" \
      --det_limit_side_len=960 \
      --det_db_unclip_ratio=3.5 \
      --rec_model_dir="output/rec_model/Student" \
      --rec_char_dict_path="train_data/keys.txt" \
      --use_gpu False \
      --enable_mkldnn=True
      
      """
      import sys
      sys.argv.append( '--image_dir' )
      # sys.argv.append( 'train_data/det/test/12.jpg' )
      sys.argv.append( 'train_data/det/train/3.jpg' )
      sys.argv.append( '--det_algorithm' )
      sys.argv.append( 'DB' )
      sys.argv.append( '--det_model_dir' )
      sys.argv.append( 'output/det_model' )
      sys.argv.append( '--det_limit_side_len' )
      sys.argv.append( '960' )
      sys.argv.append( '--det_db_unclip_ratio' )
      sys.argv.append( '3.5' )
      sys.argv.append( '--rec_model_dir' )
      sys.argv.append( 'output/rec_model/Student' )
      sys.argv.append( '--rec_char_dict_path' )
      sys.argv.append( 'train_data/keys.txt' )
      sys.argv.append( '--use_gpu' )
      sys.argv.append( 'False' )
      sys.argv.append( '--enable_mkldnn' )
      sys.argv.append( 'True' )
      sys.argv.append( '--vis_font_path' )
      sys.argv.append( 'fonts/simfang.ttf' )
   
  
  PaddleOCR_ali1k_det_rec_300epoch.7z
  
  ```



```
pip3 install   --force-reinstall  paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip3 install PPOCRLabel -i https://mirror.baidu.com/pypi/simple

huggingface\PaddleOCR\PPOCRLabel\PPOCRLabel.py
	# 运行这个

PPOCRLabel
	# 运行

```





```

https://matpool.com/supports/doc-vscode-connect-matpool/
    Remote Development 安装插件
    VS Code 远程连接矩池云机器教程

# vscode 打开远程文件夹 DB, ctrl + x 安装 python 扩展, ctrl+shift+p 输入 Python，选择选conda的python ，vscode 中修改train.py 在main 函数下加入命令行参数：

# 推荐使用CUDA11.2
python -m pip install paddlepaddle-gpu==2.3.2.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html

C:\Users\Administrator\.ssh\config
Host region-11.autodl.com
  HostName region-11.autodl.com
  Port 16116
  User root

# 3090 + Python3.8 + torch 1.10.1 + Cuda 11.1 # 这环境 1080ti ~ 3090 都适用

- https://developer.nvidia.com/zh-cn/blog/updating-the-cuda-linux-gpg-repository-key/
    >更新 CUDA Linux GPG 存储库密钥

cat /etc/os-release    
cat /proc/version

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb



dpkg -i cuda-keyring_1.0-1_all.deb

apt-get update && \
apt-get -y install cuda-11-2

wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
bash Miniforge3-Linux-x86_64.sh -b && \
~/miniforge3/bin/conda init && \
ln -s ~/miniforge3/bin/conda /usr/local/bin && \
ln -s ~/miniforge3/bin/activate /usr/local/bin && \
ln -s ~/miniforge3/bin/deactivate /usr/local/bin && \
source ~/miniforge3/etc/profile.d/conda.sh


conda deactivate && \
conda env remove -n PP

conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n PP python=3.8 --yes && \
source activate PP && \
conda install paddlepaddle-gpu==2.3.2 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge 


cp autodl-tmp/PaddleOCR.zip . && \
unzip PaddleOCR.zip && \
mv PaddleOCR-release-2.6 PaddleOCR && \
cd PaddleOCR && \
pip install -r requirements.txt


```



```python
# pip uninstall opencv-python
# pip install opencv-python==4.6.0.66

# 简单Demo：检测+识别
 
from paddleocr import PaddleOCR, draw_ocr  # 导入第三方库
import numpy as np
 
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`

ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # lang表示语言的选择

img_path = './640.jpg' # 测试图片的路径
result = ocr.ocr(img_path, cls=True) # 结果
 
# 打印结果，为一个list，即包含文本框的坐标，识别的文字及其置信度大小
print('shpae:', np.array(result).shape) # 维度大小
for line in result:
    print(line)
```



#### 英文推断

```
git clone git@github.com:PaddlePaddle/PaddleOCR.git

cd PaddleOCR

mkdir inference && cd inference
# 下载英文端到端模型并解压
wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/pgnet/e2e_server_pgnetA_infer.tar && tar xf e2e_server_pgnetA_infer.tar

inference.pdmodel以及inference.pdiparams，前者储存了整个神经网络模型的结构，而后者储存了各层训练完后的权重参数。如果你想可视化地浏览整个文件，可以使用Netron这个工具打开这两个文件，整个模型的结构就一览无余了。

# 批量识别
python3 tools/infer/predict_e2e.py --e2e_algorithm="PGNet" --image_dir="./doc/imgs_en/" --e2e_model_dir="./inference/e2e_server_pgnetA_infer/" --e2e_pgnet_valid_set="totaltext"

nvidia-smi，就能看到一个python任务正在占用GPU


打开保存结果的目录inference_results就能看到识别的结果了
```



#### 中文推断

```
!python3 tools/infer/predict_system.py \
    --image_dir="../../test" \
    --det_model_dir="./inference/det_db" \
    --rec_model_dir="./inference/rec_rare" \
    --rec_image_shape="3, 32, 320" \
    --rec_char_type="ch" \
    --rec_algorithm="RARE" \
    --use_space_char False \
    --max_text_length 7 \
    --rec_char_dict_path="../word_dict.txt" \
    --use_gpu False 
```



```
PaddleOCR(use_angle_cls=True, lang="ch", det_limit_type='min', det_limit_side_len=64)

设定短边的最小分辨率，用你的image图片，det_limit_side_len=64，文字全能检测出来。

默认参数是det_limit_type='max', det_limit_side_len=960，也就是长边最大960.

改为det_limit_type='min', det_limit_side_len=64，也就是短边最小64.

算法本身挺好用的，注意里面参数设置
```



#### 删除原环境

```

apt-get --purge remove cuda nvidia* libnvidia-* && \
dpkg -l | grep cuda- | awk '{print $2}' | xargs -n1 dpkg --purge && \
apt-get remove cuda-* && \
apt autoremove && \
apt-get update


apt-get --purge -y remove 'cuda*'  && \
apt-get --purge -y remove 'nvidia*' && \
apt autoremove -y && \
apt-get clean && \
apt update -qq;

/usr/local/cuda/bin/nvcc --version

ldconfig -p | grep cuda

```



#### 训练 ali1k

- https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_ch/models_list.md#1.1

  > 预训练模型

##### 显卡性能测试

<img src="深入理解神经网络：从逻辑回归到CNN.assets/BGJYVSDTH7{DOS8T{3BZ878.png" alt="img" style="zoom: 50%;" />

```

conda config --add channels conda-forge && \
conda config --set channel_priority flexible

conda deactivate && \
conda env remove -n PP && \
conda config --add channels conda-forge && \
conda config --set channel_priority flexible && \
conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n PP python=3.8 --yes && \
source activate PP && \
conda install paddlepaddle-gpu==2.3.2 cudatoolkit=11.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge && \
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
pip uninstall opencv-python && \
pip install pyyaml opencv-python==4.6.0.66 -i https://pypi.tuna.tsinghua.edu.cn/simple


pip uninstall numpy && \
pip install numpy==1.23

wget --no-check-certificate  https://sourceforge.net/projects/p7zip/files/p7zip/16.02/p7zip_16.02_src_all.tar.bz2 && \
tar -jxvf p7zip_16.02_src_all.tar.bz2 && \
cd p7zip_16.02 && \
make && \
make install

7za x PaddleOCR_ali300epoch.zip

ln -s /root/autodl-tmp/PaddleOCR /root/PaddleOCR

PPOCRLabel --lang ch

python PPOCRLabel/gen_ocr_train_val_test.py

pip install pyyaml

python tools/train.py -c configs/det/det_res18_db_v2.0.yml

# 检测模型评估
python tools/eval.py -c configs/det/det_res18_db_v2.0.yml -o Global.pretrained_model="output/ch_db_res18/best_accuracy"
[2022/10/13 09:42:16] ppocr INFO: metric eval ***************
[2022/10/13 09:42:16] ppocr INFO: precision:0.5296811494647662
[2022/10/13 09:42:16] ppocr INFO: recall:0.9175922253074177
[2022/10/13 09:42:16] ppocr INFO: hmean:0.6716509998911189
[2022/10/13 09:42:16] ppocr INFO: fps:8.796411382643813

# 检测模型推断
python tools/infer_det.py -c configs/det/det_res18_db_v2.0.yml  -o Global.checkpoints="output/ch_db_res18/best_accuracy" image_dir="train_data/det/test/12.jpg"


# 检测模型导出后推断
python tools/export_model.py -c configs/det/det_res18_db_v2.0.yml -o Global.checkpoints=output/ch_db_res18/best_accuracy Global.save_inference_dir=output/det_model

python tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="output/det_model" --image_dir="train_data/det/test/12.jpg" --use_gpu=True --det_limit_side_len=960 --det_db_unclip_ratio=3.5



# 识别训练
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml

# 识别模型导出后推断
python tools/export_model.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.checkpoints=output/rec_ppocr_v3_distillation/best_accuracy Global.save_inference_dir=output/rec_model

python tools/infer/predict_rec.py --image_dir=train_data/rec/test/1_crop_18.jpg --rec_model_dir=output/rec_model/Student --rec_char_dict_path=train_data/keys.txt
	# train_data/keys.txt 是自已生成的自定义词典，训练的时侯也要指定这个词典


# 检测识别二合一

python3 tools/infer/predict_system.py \
    --image_dir="train_data/det/test/12.jpg" \
    --det_algorithm="DB" \
    --det_model_dir="output/det_model" \
    --det_limit_side_len=960 \
    --det_db_unclip_ratio=3.5 \
    --rec_model_dir="output/rec_model/Student" \
    --rec_char_dict_path="train_data/keys.txt" \
    --use_gpu True


# 压缩打包
7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on PaddleOCR_ali1k_det_rec_300epoch.7z PaddleOCR

# CPU部署

conda deactivate && \
conda env remove -n PP && \
conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n PP python=3.8 --yes && \
source activate PP && \
conda install paddlepaddle==2.3.2 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge && \
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && \
pip uninstall opencv-python && \
pip install pyyaml opencv-python==4.6.0.66 -i https://pypi.tuna.tsinghua.edu.cn/simple



python3 tools/infer/predict_system.py \
    --image_dir="train_data/det/test/25.jpg" \
    --det_algorithm="DB" \
    --det_model_dir="output/det_model" \
    --det_limit_side_len=960 \
    --det_db_unclip_ratio=3.5 \
    --rec_model_dir="output/rec_model/Student" \
    --rec_char_dict_path="train_data/keys.txt" \
    --use_gpu False \
    --enable_mkldnn=True



# vscode 运行

tools/infer/predict_system.py # 修改后 F5
if __name__ == "__main__":

    """

    python3 tools/infer/predict_system.py \
    --image_dir="train_data/det/test/25.jpg" \
    --det_algorithm="DB" \
    --det_model_dir="output/det_model" \
    --det_limit_side_len=960 \
    --det_db_unclip_ratio=3.5 \
    --rec_model_dir="output/rec_model/Student" \
    --rec_char_dict_path="train_data/keys.txt" \
    --use_gpu False \
    --enable_mkldnn=True
    
    """

	# tools/infer/predict_system.py 加入：
    import sys
    sys.argv.append( '--image_dir' )
    # sys.argv.append( 'train_data/det/test/12.jpg' )
    sys.argv.append( 'train_data/det/train/3.jpg' )
    sys.argv.append( '--det_algorithm' )
    sys.argv.append( 'DB' )
    sys.argv.append( '--det_model_dir' )
    sys.argv.append( 'output/det_model' )
    sys.argv.append( '--det_limit_side_len' )
    sys.argv.append( '960' )
    sys.argv.append( '--det_db_unclip_ratio' )
    sys.argv.append( '3.5' )
    sys.argv.append( '--rec_model_dir' )
    sys.argv.append( 'output/rec_model/Student' )
    sys.argv.append( '--rec_char_dict_path' )
    sys.argv.append( 'train_data/keys.txt' )
    sys.argv.append( '--use_gpu' )
    sys.argv.append( 'False' )
    sys.argv.append( '--enable_mkldnn' )
    sys.argv.append( 'True' )
    

针对这种情况，去生成或者标注一批容易错的数据，一般精度可以再提升一波

在CPU上加速，可以开启mkldnn，设置参数 --enable_mkldnn=True，并设置合适的线程数

https://github.com/PaddlePaddle/PaddleOCR/issues/6247
	PP-OCRv3识别推理的时候--rec_algorithm是SVTR_LCNet，注意和原始SVTR的区别哈
https://github.com/PaddlePaddle/PaddleOCR/issues/2554
	单个字符坐标
		https://github.com/clovaai/CRAFT-pytorch/issues/3 
			Gaussian heatmap 的完整实现
		https://aistudio.baidu.com/aistudio/projectdetail/1927739 CRAFT论文复现
		https://www.jianshu.com/p/c3799417796a
			CRAFT-Reimplementation 半监督学习样本GT生成存在的问题
		https://github.com/faustomorales/keras-ocr/issues/40
			CRAFT 完整实现，但是Keras
		https://blog.csdn.net/u013403054/article/details/107346165
		https://zhuanlan.zhihu.com/p/76528329
		
方法一：如果是检测+识别的端到端系统，可以试试基于识别结果倒推一下单字位置（之前有开发者这么搞过，但没分享出来，可以探索下。。）
方法二：整理一批单字符标注的数据重新训练检测模型



Q1.1.1：基于深度学习的文字检测方法有哪几种？各有什么优缺点？
A：常用的基于深度学习的文字检测方法一般可以分为基于回归的、基于分割的两大类，当然还有一些将两者进行结合的方法。
（1）基于回归的方法分为box回归和像素值回归。a. 采用box回归的方法主要有CTPN、Textbox系列和EAST，这类算法对规则形状文本检测效果较好，但无法准确检测不规则形状文本。 b. 像素值回归的方法主要有CRAFT和SA-Text，这类算法能够检测弯曲文本且对小文本效果优秀但是实时性能不够。
（2）基于分割的算法，如PSENet，这类算法不受文本形状的限制，对各种形状的文本都能取得较好的效果，但是往往后处理比较复杂，导致耗时严重。目前也有一些算法专门针对这个问题进行改进，如DB，将二值化进行近似，使其可导，融入训练，从而获取更准确的边界，大大降低了后处理的耗时。



paddle_ch = PaddleOCR(
            show_log=False,
            lang="ch",
            cpu_threads=1,
            det_db_thresh=0.1,
            det_db_box_thresh=0.1,
            use_mp=True,
            enable_mkldnn=True,
            total_process_num=os.cpu_count() * 2 - 1,
            use_angle_cls=True,
            cls_model_dir="whl/cls/ch_ppocr_mobile_v2.0_cls_infer",
            det_model_dir="whl/det/ch/ch_PP-OCRv3_det_infer",
            rec_model_dir="whl/rec/ch/ch_PP-OCRv3_rec_infer"
    )

ocr = PaddleOCR(use_angle_cls=True,
lang="ch",
enable_mkldnn=True,
use_gpu=False)
ocr.ocr("image_path")

测试环境：CPU型号为Intel Gold 6148，CPU预测时开启MKLDNN加速。

python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple


```





#### PPOCRLabel

- https://github.com/PFCCLab/PPOCRLabel  新版

  - ```
    see huggingface\PPOCRLabel
    ```
  
- 音视频图片标注

  - ```
    # see -> python summary -> gradio -> video -> 音视频图片标注
    ```

- https://github.com/PaddlePaddle/PaddleOCR/blob/dygraph/PPOCRLabel/README_ch.md

```

D:\usr\Python38\python.exe -m pip install --upgrade pip


# gpu
python -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

# cpu
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

Windows
pip install PPOCRLabel -i https://mirror.baidu.com/pypi/simple # 安装

# 选择标签模式来启动
PPOCRLabel --lang ch  # 启动【普通模式】，用于打【检测+识别】场景的标签
PPOCRLabel --lang ch --kie True  # 启动 【KIE 模式】，用于打【检测+识别+关键字提取】场景的标签

```



```

python -m pip install paddlepaddle-gpu==2.5.1 -i https://pypi.tuna.tsinghua.edu.cn/simple


```





##### 切分数据



```python
/root/PaddleOCR/PPOCRLabel/gen_ocr_train_val_test.py # 修改，直接F5 运行

# coding:utf8
import os
import shutil
import random
import argparse


# 删除划分的训练集、验证集、测试集文件夹，重新创建一个空的文件夹
def isCreateOrDeleteFolder(path, flag):
    flagPath = os.path.join(path, flag)

    if os.path.exists(flagPath):
        shutil.rmtree(flagPath)

    os.makedirs(flagPath)
    flagAbsPath = os.path.abspath(flagPath)
    return flagAbsPath


def splitTrainVal(root, absTrainRootPath, absValRootPath, absTestRootPath, trainTxt, valTxt, testTxt, flag):
    # 按照指定的比例划分训练集、验证集、测试集
    # dataAbsPath = os.path.abspath(root)
    
    dataAbsPath = os.path.dirname( os.path.dirname(os.path.abspath(__file__)) )
    dataAbsPath = os.path.join(dataAbsPath, 'train_data')

    if flag == "det":
        labelFilePath = os.path.join(dataAbsPath, args.detLabelFileName)
    elif flag == "rec":
        labelFilePath = os.path.join(dataAbsPath, args.recLabelFileName)

    labelFileRead = open(labelFilePath, "r", encoding="UTF-8")
    labelFileContent = labelFileRead.readlines()
    random.shuffle(labelFileContent)
    labelRecordLen = len(labelFileContent)

    for index, labelRecordInfo in enumerate(labelFileContent):
        imageRelativePath = labelRecordInfo.split('\t')[0]
        imageLabel = labelRecordInfo.split('\t')[1]
        imageName = os.path.basename(imageRelativePath)

        if flag == "det":
            imagePath = os.path.join(dataAbsPath, imageName)
        elif flag == "rec":
            imagePath = os.path.join(dataAbsPath, args.recImageDirName, imageName)

        # 按预设的比例划分训练集、验证集、测试集
        trainValTestRatio = args.trainValTestRatio.split(":")
        trainRatio = eval(trainValTestRatio[0]) / 10
        valRatio = trainRatio + eval(trainValTestRatio[1]) / 10
        curRatio = index / labelRecordLen

        if curRatio < trainRatio:
            imageCopyPath = os.path.join(absTrainRootPath, imageName)
            shutil.copy(imagePath, imageCopyPath)
            trainTxt.write("{}\t{}".format(imageCopyPath, imageLabel))
        elif curRatio >= trainRatio and curRatio < valRatio:
            imageCopyPath = os.path.join(absValRootPath, imageName)
            shutil.copy(imagePath, imageCopyPath)
            valTxt.write("{}\t{}".format(imageCopyPath, imageLabel))
        else:
            imageCopyPath = os.path.join(absTestRootPath, imageName)
            shutil.copy(imagePath, imageCopyPath)
            testTxt.write("{}\t{}".format(imageCopyPath, imageLabel))


# 删掉存在的文件
def removeFile(path):
    if os.path.exists(path):
        os.remove(path)


def genDetRecTrainVal(args):
    detAbsTrainRootPath = isCreateOrDeleteFolder(args.detRootPath, "train")
    detAbsValRootPath = isCreateOrDeleteFolder(args.detRootPath, "val")
    detAbsTestRootPath = isCreateOrDeleteFolder(args.detRootPath, "test")
    recAbsTrainRootPath = isCreateOrDeleteFolder(args.recRootPath, "train")
    recAbsValRootPath = isCreateOrDeleteFolder(args.recRootPath, "val")
    recAbsTestRootPath = isCreateOrDeleteFolder(args.recRootPath, "test")

    removeFile(os.path.join(args.detRootPath, "train.txt"))
    removeFile(os.path.join(args.detRootPath, "val.txt"))
    removeFile(os.path.join(args.detRootPath, "test.txt"))
    removeFile(os.path.join(args.recRootPath, "train.txt"))
    removeFile(os.path.join(args.recRootPath, "val.txt"))
    removeFile(os.path.join(args.recRootPath, "test.txt"))

    detTrainTxt = open(os.path.join(args.detRootPath, "train.txt"), "a", encoding="UTF-8")
    detValTxt = open(os.path.join(args.detRootPath, "val.txt"), "a", encoding="UTF-8")
    detTestTxt = open(os.path.join(args.detRootPath, "test.txt"), "a", encoding="UTF-8")
    recTrainTxt = open(os.path.join(args.recRootPath, "train.txt"), "a", encoding="UTF-8")
    recValTxt = open(os.path.join(args.recRootPath, "val.txt"), "a", encoding="UTF-8")
    recTestTxt = open(os.path.join(args.recRootPath, "test.txt"), "a", encoding="UTF-8")

    splitTrainVal(args.datasetRootPath, detAbsTrainRootPath, detAbsValRootPath, detAbsTestRootPath, detTrainTxt, detValTxt,
                  detTestTxt, "det")

    for root, dirs, files in os.walk(args.datasetRootPath):
        for dir in dirs:
            if dir == 'crop_img':
                splitTrainVal(root, recAbsTrainRootPath, recAbsValRootPath, recAbsTestRootPath, recTrainTxt, recValTxt,
                              recTestTxt, "rec")
            else:
                continue
        break



if __name__ == "__main__":


    datasetRootPath = os.path.dirname( os.path.dirname(os.path.abspath(__file__)) )
    datasetRootPath = os.path.join(datasetRootPath, 'train_data')

    # 功能描述：分别划分检测和识别的训练集、验证集、测试集
    # 说明：可以根据自己的路径和需求调整参数，图像数据往往多人合作分批标注，每一批图像数据放在一个文件夹内用PPOCRLabel进行标注，
    # 如此会有多个标注好的图像文件夹汇总并划分训练集、验证集、测试集的需求
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--trainValTestRatio",
        type=str,
        default="6:2:2",
        help="ratio of trainset:valset:testset")
    parser.add_argument(
        "--datasetRootPath",
        type=str,
        default=f"{datasetRootPath}",
        help="path to the dataset marked by ppocrlabel, E.g, dataset folder named 1,2,3..."
    )
    parser.add_argument(
        "--detRootPath",
        type=str,
        default=f"{datasetRootPath}/det",
        help="the path where the divided detection dataset is placed")
    parser.add_argument(
        "--recRootPath",
        type=str,
        default=f"{datasetRootPath}/rec",
        help="the path where the divided recognition dataset is placed"
    )
    parser.add_argument(
        "--detLabelFileName",
        type=str,
        default="Label.txt",
        help="the name of the detection annotation file")
    parser.add_argument(
        "--recLabelFileName",
        type=str,
        default="rec_gt.txt",
        help="the name of the recognition annotation file"
    )
    parser.add_argument(
        "--recImageDirName",
        type=str,
        default="crop_img",
        help="the name of the folder where the cropped recognition dataset is located"
    )
    args = parser.parse_args()
    genDetRecTrainVal(args)
```





##### 训练

最后需要提供一个字典（{word_dict_name}.txt），使模型在训练时，可以将所有出现的字符映射为字典的索引。

因此字典需要包含所有希望被正确识别的字符，{word_dict_name}.txt需要写成如下格式，并以 `utf-8` 编码格式保存：

```
l
d
a
d
r
n
```

word_dict.txt 每行有一个单字，将字符与数字索引映射在一起，“and” 将被映射成 [2 5 1]

- 内置字典

PaddleOCR内置了一部分字典，可以按需使用。

`ppocr/utils/ppocr_keys_v1.txt` 是一个包含6623个字符的中文字典



训练中文数据，推荐使用 configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml，



```
source activate PP && \
pip uninstall opencv-python && \
pip install opencv-python==4.6.0.66 && \
pip install pyyaml

pip install opencv-python==4.6.0.66 -i https://pypi.tuna.tsinghua.edu.cn/simple


cp autodl-tmp/train_data.zip . && \
unzip train_data.zip -d PaddleOCR

# 空间不够用软链接
ln -s /root/autodl-tmp/train_data /root/PaddleOCR/train_data

cd PPOCRLabel && \
python gen_ocr_train_val_test.py

# 训练
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml
	python tools/train.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_cml.yml # 不收敛
	python tools/train.py -c configs/det/det_res18_db_v2.0.yml
	python tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="output/det_model" --image_dir="train_data/det/test/6.jpg" --use_gpu=True --det_limit_side_len=960 --det_db_unclip_ratio=3.5
	# --det_db_unclip_ratio 影响检测框的高度
	# https://blog.csdn.net/hhhhhhhhhhwwwwwwwwww/article/details/124767835
		# 关于Paddle OCR检测器检测框偏小的解决方法

	python tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="output/model_tmp" --image_dir="train_data/det/test/6.jpg" --use_gpu=True --det_limit_side_len=960 --det_db_unclip_ratio=3.5

# 继续上一次训练(epoch 接着上一次的断点开始)
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.checkpoints=output/rec_ppocr_v3_distillation/best_accuracy

# 微调 (epoch 从一开始)
source activate PP && \
python tools/train.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.pretrained_model=output/rec_ppocr_v3_distillation/best_accuracy

# 导出模型
python tools/export_model.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.checkpoints=output/rec_ppocr_v3_distillation/best_accuracy Global.save_inference_dir=output/model

python tools/export_model.py -c configs/det/det_res18_db_v2.0.yml -o Global.checkpoints=output/ch_db_res18/best_accuracy Global.save_inference_dir=output/det_model

python tools/export_model.py -c configs/det/det_res18_db_v2.0.yml -o Global.checkpoints=output/ch_db_res18/latest Global.save_inference_dir=output/model_tmp

# 推断
python tools/infer/predict_rec.py --image_dir=train_data/rec/test/1_crop_0.jpg --rec_model_dir=output/model/Student --rec_char_dict_path=train_data/keys.txt
	# train_data/keys.txt 是自已生成的自定义词典，训练的时侯也要指定这个词典


https://github.com/PaddlePaddle/PaddleOCR/issues/6652
paddleocr 检测的训练模型预测结果很好，但转inference后预测，基本检测不到文本
问题目前解决方法：
执行：python tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="./output/det_db_inference_3/student/" --image_dir="./test_data/" --use_gpu=True --det_limit_side_len=736或960 --det_limit_type=min
检测率终于正常了，736的检测率比960高些，因为默认是--det_limit_side_len=960 --det_limit_type=max，当预测样本宽度为300左右时并没有被扩大到960，但训练时是扩大到960后训练的， 配置文件中有默认设置 - EastRandomCropData: size: [960, 960]，所以，训练和预测的参数必须保持一致，才能检测正常。


# 评估
python3 tools/eval.py -c ./configs/rec/rec_chinese_lite_train_v2.0.yml  -o Global.checkpoints=./output/rec_chinese_lite_v2.0/latest

# 预测
python3 tools/infer_rec.py -c ./configs/rec/rec_chinese_common_train_v2.0.yml  -o Global.checkpoints=./output/rec_chinese_common_v2.0/best_accuracy Global.infer_img=doc/13_crop_4.jpg



# 检测识别二合一

!python3 tools/infer/predict_system.py \
    --image_dir="train_data/det/test/6.jpg" \
    --det_model_dir="output/det_model" \
    --rec_model_dir="./inference/rec_rare" \
    --rec_image_shape="3, 32, 320" \
    --rec_char_type="ch" \
    --rec_algorithm="RARE" \
    --use_space_char False \
    --max_text_length 7 \
    --rec_char_dict_path="../word_dict.txt" \
    --use_gpu False



训练的输入尺寸在：

EastRandomCropData:
size: [640, 640]
测试的时候使用的是[736, 1280]，

DetResizeForTest:
image_shape: [736, 1280]
训练的时候输入尺寸小是为了加快训练速度，并减小显存占用，预测的时候设置大一些是为了提升检测精度

预训练模型不对，CML训练需要加载训练好的教师模型，关于PPOCRv3的训练方法参考这个文档：https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/PPOCRv3_det_train.md


由于数据集大多是长文本，因此需要注释掉下面的数据增广策略，以便训练出更好的模型。
- RecConAug:
    prob: 0.5
    ext_data_num: 2
    image_shape: [48, 320, 3]

```





```
python tools/train.py -c D:\pytorch\PaddleOCR\configs\rec\PP-OCRv3\ch_PP-OCRv3_rec_distillation.yml  

# 微调
python tools/train.py -c configs/det/ch_ppocr_v2.0/ch_det_res18_db_v2.0.yml -o Global.checkpoints=output/ch_db_res18/best_accuracy



```



```
# 配置
/root/PaddleOCR/configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml

Global:
  debug: false
  use_gpu: true
  epoch_num: 1200
  log_smooth_window: 20
  print_batch_step: 10
  save_model_dir: ./output/rec_ppocr_v3_distillation
  save_epoch_step: 400
  eval_batch_step: [0, 2000]
  cal_metric_during_train: true
  pretrained_model:
  checkpoints:
  save_inference_dir:
  use_visualdl: false
  infer_img: doc/imgs_words/ch/word_1.jpg
  character_dict_path: train_data/keys.txt
  max_text_length: &max_text_length 45
  infer_mode: false
  use_space_char: true
  distributed: true
  save_res_path: ./output/rec/predicts_ppocrv3_distillation.txt


Optimizer:
  name: Adam
  beta1: 0.9
  beta2: 0.999
  lr:
    name: Piecewise
    decay_epochs : [700, 800]
    values : [0.0005, 0.00005]
    warmup_epoch: 5
  regularizer:
    name: L2
    factor: 3.0e-05


Architecture:
  model_type: &model_type "rec"
  name: DistillationModel
  algorithm: Distillation
  Models:
    Teacher:
      pretrained:
      freeze_params: false
      return_all_feats: true
      model_type: *model_type
      algorithm: SVTR
      Transform:
      Backbone:
        name: MobileNetV1Enhance
        scale: 0.5
        last_conv_stride: [1, 2]
        last_pool_type: avg
      Head:
        name: MultiHead
        head_list:
          - CTCHead:
              Neck:
                name: svtr
                dims: 64
                depth: 2
                hidden_dims: 120
                use_guide: True
              Head:
                fc_decay: 0.00001
          - SARHead:
              enc_dim: 512
              max_text_length: *max_text_length
    Student:
      pretrained:
      freeze_params: false
      return_all_feats: true
      model_type: *model_type
      algorithm: SVTR
      Transform:
      Backbone:
        name: MobileNetV1Enhance
        scale: 0.5
        last_conv_stride: [1, 2]
        last_pool_type: avg
      Head:
        name: MultiHead
        head_list:
          - CTCHead:
              Neck:
                name: svtr
                dims: 64
                depth: 2
                hidden_dims: 120
                use_guide: True
              Head:
                fc_decay: 0.00001
          - SARHead:
              enc_dim: 512
              max_text_length: *max_text_length
Loss:
  name: CombinedLoss
  loss_config_list:
  - DistillationDMLLoss:
      weight: 1.0
      act: "softmax"
      use_log: true
      model_name_pairs:
      - ["Student", "Teacher"]
      key: head_out
      multi_head: True
      dis_head: ctc
      name: dml_ctc
  - DistillationDMLLoss:
      weight: 0.5
      act: "softmax"
      use_log: true
      model_name_pairs:
      - ["Student", "Teacher"]
      key: head_out
      multi_head: True
      dis_head: sar
      name: dml_sar
  - DistillationDistanceLoss:
      weight: 1.0
      mode: "l2"
      model_name_pairs:
      - ["Student", "Teacher"]
      key: backbone_out
  - DistillationCTCLoss:
      weight: 1.0
      model_name_list: ["Student", "Teacher"]
      key: head_out
      multi_head: True
  - DistillationSARLoss:
      weight: 1.0
      model_name_list: ["Student", "Teacher"]
      key: head_out
      multi_head: True

PostProcess:
  name: DistillationCTCLabelDecode
  model_name: ["Student", "Teacher"]
  key: head_out
  multi_head: True

Metric:
  name: DistillationMetric
  base_metric_name: RecMetric
  main_indicator: acc
  key: "Student"
  ignore_space: False

Train:
  dataset:
    name: SimpleDataSet
    data_dir: ./train_data/
    ext_op_transform_idx: 1
    label_file_list:
    - ./train_data/rec/train.txt
    transforms:
    - DecodeImage:
        img_mode: BGR
        channel_first: false
    - RecConAug:
        prob: 0.5
        ext_data_num: 2
        image_shape: [48, 320, 3]
    - RecAug:
    - MultiLabelEncode:
    - RecResizeImg:
        image_shape: [3, 48, 320]
    - KeepKeys:
        keep_keys:
        - image
        - label_ctc
        - label_sar
        - length
        - valid_ratio
  loader:
    shuffle: true
    batch_size_per_card: 64
    drop_last: true
    num_workers: 4
Eval:
  dataset:
    name: SimpleDataSet
    data_dir: ./train_data
    label_file_list:
    - ./train_data/rec/val.txt
    transforms:
    - DecodeImage:
        img_mode: BGR
        channel_first: false
    - MultiLabelEncode:
    - RecResizeImg:
        image_shape: [3, 48, 320]
    - KeepKeys:
        keep_keys:
        - image
        - label_ctc
        - label_sar
        - length
        - valid_ratio
  loader:
    shuffle: false
    drop_last: false
    batch_size_per_card: 64
    num_workers: 4



```





##### 模型转换

- https://www.jianshu.com/p/3c8a14bf2a91

  > 安卓端部署PPOCR的ncnn模型——模型转换



#### 知识蒸馏

> 思路：采用resnet50(teacher)先训练，在利用训练好的resnet50(teacher)对resnet18(student)小模型进行联合训练，实验证明f1score比单独训练resnet18涨一个点。





## PaddleSpeech

- https://cloud.tencent.com/developer/article/2135237 极好的

  > paddlespeech的开源语音识别模型测试

- https://github.com/PaddlePaddle/PaddleSpeech

- https://github.com/PaddlePaddle/PaddleSpeech/wiki/PaddleSpeech-CLI---Batch-Process

  > 同时识别多个音频

- https://github.com/yeyupiaoling/MASR 同作者的语音识别

```

yum groupinstall "Development Tools" "Development Libraries"
	# rm -f /var/run/yum.pid

python -m pip install paddlepaddle==2.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
	# CPU 用这个

python -m pip install paddlepaddle-gpu==2.4.2.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
	# GPU 用这个

paddlespeech tts --am fastspeech2_male --voc pwgan_male --input "你好，欢迎使用百度飞桨深度学习框架！"
	# 命令行识别

global runtts
exec('from paddlespeech.cli.tts import TTSExecutor')  # 不知道为什么一定要这样导入
TTSExecutor = locals()['TTSExecutor']   # 需要的符号已经在当前局部变量里面了，取出来用
runtts = TTSExecutor()
status = runtts.execute([ '--am', 'fastspeech2_male', '--voc', 'pwgan_male', '--input', '你好，欢迎使用百度飞桨深度学习框架！' ])
	# 成功生成音频文件


if __name__ == '__main__':
    import sys
    sys.argv.append( 'tts' )
    sys.argv.append( '--am' )
    sys.argv.append( 'fastspeech2_male' )
    sys.argv.append( '--voc' )
    sys.argv.append( 'pwgan_male' )
    sys.argv.append( '--input' )
    sys.argv.append( '你好，欢迎使用百度飞桨深度学习框架！' )
    
    exec('from paddlespeech.cli.tts import TTSExecutor')
    lcls = locals()
    _entry = lcls['TTSExecutor']
    status = _entry().execute(sys.argv[2:])
    	# 成功生成音频文件


from paddlespeech.cli.entry import _execute
import sys
if __name__ == '__main__':
    sys.argv.append( 'tts' )
    sys.argv.append( '--am' )
    sys.argv.append( 'fastspeech2_male' )
    sys.argv.append( '--voc' )
    sys.argv.append( 'pwgan_male' )
    sys.argv.append( '--input' )
    sys.argv.append( '你好，欢迎使用百度飞桨深度学习框架！' )
    _execute()
	# 实际是这样运行的



from paddlespeech.cli.tts.infer import TTSExecutor
tts = TTSExecutor()
tts(am="fastspeech2_male", voc="pwgan_male", text="今天天气十分不错。", output="output.wav")
```



```
import re
import sys
from paddlespeech.cli.entry import _execute
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(_execute())
```





```
# 显存占用问题
请问如何检查显存释放呢？ -> 训练结束后 nvidia-smi 查看显存是否还被占用
调小了batch_size还是会显存突然增高 -> 看看是不是个别数据长度明显比其他的长
可以尝试加一些 FLAGS https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/flags/memory_cn.html#flags-allocator-strategy
```



### 训练一个自己的TTS

- https://github.com/PaddlePaddle/PaddleSpeech/discussions/1842



### 流式语音识别

[流式语音识别](https://github.com/PaddlePaddle/PaddleSpeech/blob/develop/demos/streaming_asr_server/README_cn.md)  **支持时间戳功能**

[python音乐播放器](https://github.com/feeluown/FeelUOwn)



## 语音唤醒

https://github.com/Picovoice/porcupine



## whisperX 

- https://github.com/openai/whisper

  [whisperX 字级的时间戳](https://github.com/m-bain/whisperX)

  - https://github.com/ahmetoner/whisper-asr-webservice
  - https://github.com/hackingthemarkets/chatgpt-api-whisper-api-voice-assistant

  - https://huggingface.co/openai/whisper-large

  - https://blog.deepgram.com/exploring-whisper/

  - https://colab.research.google.com/drive/1LjfD-euRBnbXyCcL6eC5Ekfhviba-HAX **直接能用**

  - https://github.com/openai/whisper/discussions/277 中文参数

  - https://github.com/openai/whisper/discussions/759 Fine-tuning

    - https://github.com/openai/whisper/discussions/64#discussioncomment-3765117 **细**

  - https://github.com/openai/whisper/discussions/908 内存音频

  - https://blog.deepgram.com/exploring-whisper/ **必看 很细节**

  - https://github.com/openai/whisper/discussions/63 模型下载

  - https://github.com/openai/whisper/discussions/360 多 GPU 训练

    > Download links are in [**init**.py](https://github.com/openai/whisper/blob/f296bcd3fac41525f1c5ab467062776f8e13e4d0/whisper/__init__.py) @ lines 17-27
    >
    > For windows location to download see the above comment, on WSL/Linux they go in
    > `\\wsl$\Ubuntu\home\[username]\.cache\whisper`
    >
    > Note if you are experimenting with both WSL and Windows Native versions you need to put the models in BOTH locations.
    >
    > As of today those links are:
    >
    > - [tiny.en](https://openaipublic.azureedge.net/main/whisper/models/d3dd57d32accea0b295c96e26691aa14d8822fac7d9d27d5dc00b4ca2826dd03/tiny.en.pt)
    > - [tiny](https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt)
    > - [base.en](https://openaipublic.azureedge.net/main/whisper/models/25a8566e1d0c1e2231d1c762132cd20e0f96a85d16145c3a00adf5d1ac670ead/base.en.pt)
    > - [base](https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt)
    > - [small.en](https://openaipublic.azureedge.net/main/whisper/models/f953ad0fd29cacd07d5a9eda5624af0f6bcf2258be67c92b79389873d91e0872/small.en.pt)
    > - [small](https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt)
    > - [medium.en](https://openaipublic.azureedge.net/main/whisper/models/d7440d1dc186f76616474e0ff0b3b6b879abc9d1a4926b7adfa41db2d497ab4f/medium.en.pt)
    > - [medium](https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt)
    > - [large](https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large.pt)

    ```
    beam_size=5
    best_of=None
    temperature=0.0
    
    decode_options = dict(language="en", best_of=best_of, beam_size=beam_size, temperature=temperature)
    transcribe_options = dict(task="transcribe", **decode_options)
    
    transcription = model.transcribe("kittens_30secs.mp3", **transcribe_options)
    print(transcription["text"])
    ```

    

    ```
    It appears that audio is in int16 dtype, whereas Whisper expects float32 or float16. You may try converting it to a float32 array and dividing it by 32768, similar to what's done in audio.py:
    
    whisper/whisper/audio.py
    
    Line 49 in 5c1a8c1
    
    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0 
    ```

    

- https://zhuanlan.zhihu.com/p/595691785

  ```
  whisper -> chatgpt -> dalle2 一条龙
  ```

  

```
pip install git+https://github.com/openai/whisper.git && \
apt update && sudo apt install ffmpeg && \
pip install setuptools-rust


/root/miniconda3/lib/python3.8/site-packages/whisper/__init__.py
	# 模型的地址在这

whisper 1.wav --language Japanese --model medium
whisper 1.wav --language Japanese --model medium --task translate

cp /root/autodl-tmp/large.pt /root/.cache/whisper/large-v2.
whisper 0a2bfdbf-ef8c-49a7-82a6-dd01891b2478.mp3 --language Japanese --model large

```



Transcription can also be performed within Python:

```
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

Internally, the `transcribe()` method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window.

Below is an example usage of `whisper.detect_language()` and `whisper.decode()` which provide lower-level access to the model.

```
import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
```



```
task
--task 分为 transcribe（语音转录）和 translate。Whisper 默认使用 --task transcribe 模式，将语音转录为对应的语言字幕。--task translate 是所有语言翻译为英文，目前尚未支持翻译为其他语言。

language
--language 是设置语音转录的语种，支持语种范围查看 tokenizer.py，比如指定日语 --language japanese。如果你没指定语种，Whisper 会截取音频的前 30 秒来判断语种。

如果指定语种与文件中的语种并不相同，Whisper 会强制翻译，但 10 分钟以上的音视频会出现大量的重复无意义字幕。2假设你把日语视频的转录语言设为汉语，前 8 分钟 Whisper 会正确转录到中文，但 8 分钟后的转录字幕会一直重复，并与实际片段无关。

model
--model 指 Whisper 的转录模型，转录效果为 tiny < base < small < medium < large，默认使用 small。添加参数 --model medium 或 --model large 可以切换到更大的模型，但转录时间也会变长。如果你是对英文视频进行转录，则在模型参数上添加后缀 .en，能提升转录速度。

幻听参数
非英语视频的转录有时会出现幻听，即静默片段被识别出语音，或是转录结果与该片段无关。这些问题是由语气停顿参数引起的。幻听的解决方案是引入 VAD，但 VAD 对动手能力要求较高。如果你的视频转录出现了严重幻听，建议先尝试调节参数阈值。

--no_speech_threshold 无声识别的阈值，默认为 0.6。当 no_speech_threshold 高于阈值且 logprob_threshold 低于预设时，该片段将被标记为静默。对于非英语长视频来说，建议将其调低，否则经常出现大段的重复识别。
--logprob_threshold 转录频次的阈值，默认为 -1.0。当 logprob_threshold 低于预设时，将不对该片段进行转录。建议修改为 None 或更低的值。
--compression_ratio_threshold 压缩比的阈值，默认为 2.4。当 compression_ratio_threshold 高于预设时，将不对该片段进行转录。
--no_speech_threshold 0.5 --logprob_threshold None --compression_ratio_threshold 2.2 是我常用的参数，你可以按视频情况来调节。

--device cpu 或 --device cuda

prompt='以下是普通话的句子'
result = model.transcribe(audioFile, task='translate',language='zh',verbose=True,initial_prompt=prompt)

```



### 从零训练

- https://github.com/openai/whisper/discussions/64



### spleeter 人声分离

- https://github.com/deezer/spleeter



### uvr5 人声分离

- https://github.com/Anjok07/ultimatevocalremovergui  **这个好像更准些**

### parselmouth 音准分析

- https://github.com/YannickJadoul/Parselmouth





https://github.com/openai/whisper/discussions/397   **whisper webui**

https://github.com/snakers4/silero-vad



VAD静音检测



### autoCut

- https://github.com/mli/autocut  必看



### PVE显卡直通

- https://www.labradors.work/2022/05/07/PVE%E6%98%BE%E5%8D%A1%E7%9B%B4%E9%80%9A/





## godot-whisper 

https://github.com/V-Sekai/godot-whisper  语音识别

see nodejs summary.md -> godot -> 必看教程



## CosyVoice

https://github.com/FunAudioLLM/CosyVoice/issues/37

https://www.cnblogs.com/v3ucn/p/18288786

https://github.com/espnet/espnet  mcu

https://github.com/yeyupiaoling/MASR 同作者的语音识别



# 1660TI

- https://blog.csdn.net/sinat_36721621/article/details/115326307

  > 可以安装 cuda11.1

# 1080TI

- https://www.autodl.com/console/instance/list

- https://www.jianshu.com/p/f3a3d8dc9ba6

```

sed -i 's/batch_size\:\ 16/batch_size\:\ 12/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml && \
sed -i 's/num_workers\:\ 16/num_workers\:\ 12/1' ~/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml


cd ~/DB && \
CUDA_VISIBLE_DEVICES=0 python train.py experiments/seg_detector/td500_resnet18_deform_thre.yaml --num_gpus 1

```





# 2080TI

- https://blog.csdn.net/cskywit/article/details/97239371

  > Ubuntu18.04下深度学习环境搭建及问题解决（双系统+2080Ti显卡）

- https://developer.nvidia.com/cuda-gpus

  > cuda gpu 支持列表

- https://blog.csdn.net/liaoningxinmin/article/details/121501720

  > **2080TI + 3080TI 配置**

```
部件	型号	价格	链接	备注
CPU	英特尔（Intel）酷睿六核i7-6850K 盒装CPU处理器 	4599	http://item.jd.com/11814000696.html	
散热器	美商海盗船 H55 水冷	449	https://item.jd.com/10850633518.html	
主板	华硕（ASUS）华硕 X99-E WS/USB 3.1工作站主板	4759	
内存	美商海盗船(USCORSAIR) 复仇者LPX DDR4 3000 32GB(16Gx4条)  	2799 * 2	https://item.jd.com/1990572.html	
SSD	三星(SAMSUNG) 960 EVO 250G M.2 NVMe 固态硬盘	599	https://item.jd.com/3739097.html		
硬盘	希捷(SEAGATE)酷鱼系列 4TB 5900转 台式机机械硬盘 * 2 	629 * 2	https://item.jd.com/4220257.html	
电源	美商海盗船 AX1500i 全模组电源 80Plus金牌	3699	https://item.jd.com/10783917878.html
机箱	美商海盗船 AIR540 USB3.0 	949	http://item.jd.com/12173900062.html
显卡	技嘉（GIGABYTE） GTX1080Ti 11GB 非公版高端游戏显卡深度学习涡轮 * 4 7400 * 4    https://item.jd.com/10583752777.html


CPU：I9 9820X 4600元
主板：华硕WX X299 SAGE 4200元
内存：金士顿骇客神条16G 3000 X4 2200元
机箱：联立 包豪斯O11 800元
散热：海盗船H150i pro 1300元
显卡：技嘉2080ti 涡轮X4 40000元
配件：不需要NVLINK了
固态：三星 970pro 512G 1200元
机械硬盘：西数紫盘3T 480元
电源：振华leadex 2000W 3300元
机箱风扇：利民TL-C12 X5 400元
总计 58480

# 3090

- https://zhuanlan.zhihu.com/p/279401802



```
不过新的问题又出现了：七彩虹Neptune（水神）需要3×8pin供电，而海盗船VS550仅能提供2个8pin PCIE电源接口。

没办法不得不连电源一起换。最后CPU一直采用原厂小风扇，噪声较大。干脆一不做二不休换了水冷散热器。



https://pytorch.org/get-started/previous-versions/

ldconfig -p | grep cuda

cp autodl-nas/DB.zip autodl-nas/TD_TR.zip . && \
unzip DB.zip && \
unzip TD_TR.zip -d DB/datasets

conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=11.3 -c pytorch -c conda-forge







export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
cd ~/DB/assets/ops/dcn/ && \
python setup.py build_ext --inplace

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0
```






```
conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=11.0 -c pytorch --yes




```



```
apt-get --purge remove cuda nvidia* libnvidia-* && \
dpkg -l | grep cuda- | awk '{print $2}' | xargs -n1 dpkg --purge && \
apt-get remove cuda-* && \
apt autoremove && \
apt-get update



# 3080 TI

- https://willylan.medium.com/how-to-install-cuda-11-1-and-cudnn-v8-05-on-ubuntu-20-1-with-rtx3090-8e0b768faaa2

- https://zhuanlan.zhihu.com/p/291332801

  > 2个3080理论上和4个2080ti性能差不多，现在再加2080ti就非常不理智了。所以拆了2080ti，买了两个技嘉GeForce RTX™ 3080 GAMING OC 10G
  >
  > - 操作系统：Ubuntu18.04
  > - Nvidia Driver：455
  > - Python：3.7
  > - Pytorch：>= 1.7.0
  > - cuda： 11.1.1
  > - cudnn： 8.0.5
  >
  > > 版本号很重要，一定要看清楚，选不对小版本就是在瞎折腾。
  >
  > 找到原因了，是因为cudnn的问题，**训练的时候cudnn设为false**就好了
  >
  > a
  >
  > https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/libcudnn8_8.0.5.39-1+cuda11.1_amd64.deb
  >
  > a

```
肯定是选两张RTX3080TI低预算的情况下深度学习主要的瓶颈还是在于训练速度而不是显存容量，同样的模型训练时batch size增大一倍可能最终性能会有很小的提升，但是训练速度增加一倍意味着同样的时间可以试更多的模型/超参数虽然RTX3080TI的12GB显存可能会出现batch size不够大导致GPU没有被“喂饱”的问题，但是可以通过混合精度训练减少显存的占用，正好Ampere增加了BF16的支持。对于具体的硬件选购时要注意的问题：非服务器/HEDT平台主板（这个预算也不够买）会受制于MSDT平台的PCI-E通道数量只能给每张显卡提供8个通道，要注意买PCI-E拆分成X8 + X8的主板，别买成X16 + X4的了非OTES散热的显卡都很厚而且散热容易互相干涉，建议选择两条可用的插槽间距在4槽及以上的主板电源功率得管够，至少1200W往上走，每张显卡的每个供电接口都要和电源单独连线，不要偷懒用一条线分出多个插口另外还可以考虑下性能差距不大的RTX3080 12GB
```





# 3090

- https://medium.com/analytics-vidhya/install-cuda-11-2-cudnn-8-1-0-and-python-3-9-on-rtx3090-for-deep-learning-fcf96c95f7a1
  
  > 超详细
- https://github.com/google/jax/issues/8506
  
  > **Failed to determine best cudnn convolution algorithm**
  >
  > ```
  > pip install --upgrade pip && \
  > pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
  > pip install flax
  > ```
  >
  > ```
  > echo 'import jax
  > import jax.numpy as jnp
  > import flax.linen as nn
  > 
  > class CNN(nn.Module):
  >     @nn.compact
  >     def __call__(self, x):
  >         x = nn.Conv(features=32, kernel_size=(3, 3))(x)
  >         x = nn.relu(x)
  >         x = nn.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
  >         x = nn.Conv(features=64, kernel_size=(3, 3))(x)
  >         x = nn.relu(x)
  >         x = nn.avg_pool(x, window_shape=(2, 2), strides=(2, 2))
  >         x = x.reshape((x.shape[0], -1))  # flatten
  >         x = nn.Dense(features=256)(x)
  >         x = nn.relu(x)
  >         x = nn.Dense(features=10)(x)
  >         x = nn.log_softmax(x)
  >         return x
  > 
  > model = CNN()
  > batch = jnp.ones((32, 64, 64, 10))  # (N, H, W, C) format
  > variables = model.init(jax.random.PRNGKey(0), batch)
  > # output = model.apply(variables, batch)' > cudnn.py && \
  > pip install --upgrade pip && \
  > pip install "jax[cuda11_cudnn805]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
  > pip install flax && \
  > apt-cache policy libcudnn8 && \
  > export TF_FORCE_GPU_ALLOW_GROWTH=true && \
  > export XLA_PYTHON_CLIENT_MEM_FRACTION=0.87 && \
  > python cudnn.py
  > ```
  >
  > ```
  > %%bash
  > pip install --upgrade pip && \
  > pip install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
  > pip install flax && \
  > apt-cache policy libcudnn8 && \
  > export XLA_PYTHON_CLIENT_MEM_FRACTION=0.87 && \
  > python cudnn.py
  > ```
  >
  > 
- https://willylan.medium.com/how-to-install-cuda-11-1-and-cudnn-v8-05-on-ubuntu-20-1-with-rtx3090-8e0b768faaa2
- https://zhuanlan.zhihu.com/p/339062791

```
RTX 3090 是 30 系列中唯一能够通过 NVLink 桥接器进行扩展的 GPU 型号。当与 NVLink 网桥配对使用时，可以将显存扩充为 48 GB 来训练大型模型。


Platinum 8358P
	FCLGA 4189
	PCI Express 通道数的最大值 64
	内核数 32
	线程数 64
	最大睿频频率 3.40 GHz
	处理器基本频率 2.60 GHz
	
```



```python
# 重装cuda 驱动
apt update && \
apt-get install kmod && \
lsmod | grep -i nvidia && \
rmmod nvidia-uvm && \
modprobe -r nvidia_uvm
```





```
apt-get --purge remove cuda nvidia* libnvidia-* && \
dpkg -l | grep cuda- | awk '{print $2}' | xargs -n1 dpkg --purge && \
apt-get remove cuda-* && \
apt autoremove && \
apt-get update
```



```
apt-get --purge -y remove 'cuda*' && \
apt-get --purge -y remove 'nvidia*' && \
apt autoremove -y && \
apt-get clean && \
apt update -qq;
```



```
rm -f /var/lib/dpkg/lock-frontend && \
rm -f /var/lib/dpkg/lock && \
rm -f /var/cache/apt/archives/lock && \
apt-get --purge remove "*cublas*" "cuda*" "nsight*" -y && \
apt-get --purge remove "*nvidia*"
rm -rf /usr/local/cuda*
```



```
# To uninstall cuda
sudo /usr/local/cuda-11.4/bin/cuda-uninstaller 
# To uninstall nvidia
sudo /usr/bin/nvidia-uninstall
```



# 显卡直通

- https://www.docker.com/blog/wsl-2-gpu-support-for-docker-desktop-on-nvidia-gpus/

- https://blog.csdn.net/weixin_45409343/article/details/122478397



# 可视化

		fuse = torch.cat((p5, p4, p3, p2), 1)
	    # this is the pred module, not binarization module; 
	    # We do not correct the name due to the trained model.
	    binary = self.binarize(fuse)
	
	    # 可视化--------
	    binary_img = binary[0].permute((1, 2, 0)).cpu().data.numpy() * 255
	    thresh_img = self.thresh(fuse)[0].permute((1, 2, 0)).cpu().data.numpy() * 255
	    binary_img = binary_img.astype(np.uint8)
	    thresh_img = thresh_img.astype(np.uint8)
	    cv2.imwrite('bin.bmp', binary_img)
	    binary_color_map = cv2.applyColorMap(binary_img, cv2.COLORMAP_JET)
	    cv2.imwrite('cm.bmp', binary_color_map)
	
	    cv2.imwrite('thresh.bmp',thresh_img)
	    thresh_color_map=cv2.applyColorMap(thresh_img, cv2.COLORMAP_JET)
	    cv2.imwrite('color_thresh.bmp',thresh_color_map)
	    # ------------------
```





# Colab



## run shell

```
%%bash
conda install --channel defaults conda python=3.7 --yes
conda update --channel defaults --all --yes
```



## 环境变量



```
%set_env CUDA_HOME=/usr/local/cuda
%cd /content/DB
!pip install -r requirement.txt
%cd /content/DB/assets/ops/dcn/
!python setup.py build_ext --inplace
```



## vscode 远程调试

​```python
https://github.com/MhLiao/DB 验证可运行的环境：

tesla K80 + Ubuntu18.04 +
	+ Python 3.7 + CUDA 10.0 + cuDNN 7.6.5 + NVCC 10.0 

nvcc --version
	Cuda compilation tools, release 10.0, V10.0.130

ldconfig -p | grep cuda
	libnvrtc.so.10.0 (libc6,x86-64) => /usr/local/cuda-10.0/targets/x86_64-linux/lib/libnvrtc.so.10.0


 
conda update -y conda -n base && \
conda install ipython pip --yes && \
conda create -n DB python=3.7 --yes && \
source activate DB && \
conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch --yes


cp /mnt/DB.zip /mnt/TD_TR.zip . && \
unzip DB.zip && \
unzip TD_TR.zip -d DB/datasets


export CUDA_HOME=/usr/local/cuda && \
echo $CUDA_HOME && \
cd ~/DB/assets/ops/dcn/ && \
python setup.py build_ext --inplace

cd ~/DB && \
pip install -r requirement.txt && \
pip install --upgrade protobuf==3.20.0


https://matpool.com/supports/doc-vscode-connect-matpool/
    VS Code 远程连接矩池云机器教程
# train.py 添加命令行参数，并用vscode 远程调试K80 服务器上的 conda 环境(ctrl+shift+p 选conda的python)，vscode 中修改train.py 在main 函数下加入：

def main():

    import sys
    sys.argv.append( 'experiments/seg_detector/td500_resnet18_deform_thre.yaml' )
    sys.argv.append( '--num_gpus' )
    sys.argv.append( '1' )

修改：/root/DB/experiments/seg_detector/td500_resnet18_deform_thre.yaml    
        train: 
        class: TrainSettings
        data_loader: 
            class: DataLoader
            dataset: ^train_data
            batch_size: 16
            num_workers: 16
           
把batch_size 和 num_workers 调小一点，否则K80 顶不住会出错，这里改成12

 
vscode 中然后F5 调试远行train.py

C:\Users\i\.ssh\config
Host hz-t3.matpool.com
  HostName hz-t3.matpool.com
  Port 26517
  User root

```



## colab 远程调试

- https://medium.com/analytics-vidhya/colab-vs-code-github-jupyter-perfect-for-deep-learning-2b257ae94d01

  > Colab + Vs Code + GitHub + Jupyter (Perfect for Deep Learning)



```
D:\usr\cloudflared-windows-amd64.exe
```



```
Colab 还有很多更有意思的功能。比如说用个魔术符号「%」调用 TensorBoard、黑暗系代码主题、文件浏览和操作系统，以及最近才更新的 Pandas DataFrame 可视化操作。
```



## colab Web Server

- https://stackoverflow.com/questions/59741453/is-there-a-general-way-to-run-web-applications-on-google-colab



## 卸载CUDA

- https://stackoverflow.com/questions/56431461/how-to-remove-cuda-completely-from-ubuntu
- https://zhuanlan.zhihu.com/p/279401802
  - https://mirror.sjtu.edu.cn/pytorch-wheels/cu101/?mirror_intel_list
  - https://github.com/CharlesShang/DCNv2   torch实现卷积
- https://zhuanlan.zhihu.com/p/82521884

```
nvidia-smi 
注意：通过nvidia-smi命令查看到的CUDA版本只是驱动支持的最高cuda版本参数，不代表实例中安装的是该版本CUDA。
```





## CUDA/cuDNN

- https://www.autodl.com/docs/cuda/
- https://zhuanlan.zhihu.com/p/279401802

```
export CUDA_HOME=/usr/local/cuda
source ~/.bashrc

unset TORCH_CUDA_ARCH_LIST
export TORCH_CUDA_ARCH_LIST="8.0"

apt-get update
sudo apt install software-properties-common
```

```
from pathlib import Path

PATH = r'<path to datasets\icdar2015\train_gts>'

p = Path(PATH)

for bom_file in p.glob('*.txt'):
    s = open(bom_file, mode='r', encoding='utf-8-sig').read()
    open(bom_file, mode='w', encoding='utf-8').write(s)
```



### 查询默认CUDA/cuDNN版本

> 注意：通过nvidia-smi命令查看到的CUDA版本只是驱动支持的最高cuda版本参数，不代表实例中安装的是该版本CUDA。

终端中执行查看默认镜像自带的CUDA版本（安装目录为/usr/local/）：

```
查询平台内置镜像中的cuda版本
$ ldconfig -p | grep cuda
        libnvrtc.so.11.0 (libc6,x86-64) => /usr/local/cuda-11.0/targets/x86_64-linux/lib/libnvrtc.so.11.0
        libnvrtc.so (libc6,x86-64) => /usr/local/cuda-11.0/targets/x86_64-linux/lib/libnvrtc.so
        libnvrtc-builtins.so.11.0 (libc6,x86-64) => /usr/local/cuda-11.0/targets/x86_64-linux/lib/libnvrtc-builtins.so.11.0

查询平台内置镜像中的cudnn版本
$ ldconfig -p | grep cudnn
        libcudnn_ops_train.so.8 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8
        libcudnn_ops_train.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so
        libcudnn_ops_infer.so.8 (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8
        libcudnn_ops_infer.so (libc6,x86-64) => /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so
```

上边的输出日志`.so`后的数字即为版本号。如果你通过conda安装了cuda那么可以通过以下命令查看：

```
$ conda list | grep cudatoolkit
cudatoolkit               10.1.243             h6bb024c_0    defaults
$ conda list | grep cudnn
cudnn                     7.6.5                cuda10.1_0    defaults
```

### 安装其他版本的CUDA/cuDNN

#### 方法一：使用conda进行安装

优点：简单

缺点：一般不会带头文件，如果需要做编译，则需要照方法二安装

方法：

```
$ conda install cudatoolkit==xx.xx
$ conda install cudnn==xx.xx
```

如果你不知道版本号是什么那么可以搜索：

```
$ conda search cudatoolkit
Loading channels: done
# Name                       Version           Build  Channel             
cudatoolkit                      9.0      h13b8566_0  anaconda/pkgs/main  
cudatoolkit                      9.2               0  anaconda/pkgs/main  
cudatoolkit                 10.0.130               0  anaconda/pkgs/main  
cudatoolkit                 10.1.168               0  anaconda/pkgs/main  
cudatoolkit                 10.1.243      h6bb024c_0  anaconda/pkgs/main  
cudatoolkit                  10.2.89      hfd86e86_0  anaconda/pkgs/main  
cudatoolkit                  10.2.89      hfd86e86_1  anaconda/pkgs/main  
cudatoolkit                 11.0.221      h6bb024c_0  anaconda/pkgs/main  
cudatoolkit                   11.3.1      h2bc3f7f_2  anaconda/pkgs/main
```

#### 方法二：下载安装包安装

CUDA下载地址：https://developer.nvidia.com/cuda-toolkit-archive

安装方法：

```
下载.run格式的安装包后：
$ chmod +x xxx.run   # 增加执行权限
$ ./xxx.run          # 运行安装包
```

cuDNN下载地址：https://developer.nvidia.com/cudnn

安装方法：

先解压， 后将动态链接库和头文件放入相应目录

```
 $ mv cuda/include/* /usr/local/cuda/include/
 $ chmod +x cuda/lib64/* && mv cuda/lib64/* /usr/local/cuda/lib64/
```

安装完成以后，增加环境变量：

```
$ echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:${LD_LIBRARY_PATH} \n" >> ~/.bashrc
$ source ~/.bashrc && ldconfig
```

提示：

默认镜像都内置了最原生的CUDA和cuDNN，如果您自己安装了cudatoolkits等，那么一般会默认优先使用conda中安装的cudatoolkits，



## install pytorch

```
! python -m pip install torch==1.2.0 -f https://download.pytorch.org/whl/torch_stable.html

# 这是 DBNet 官方实现要求的版本
```



## install conda

**注意：虚拟环境只在单个代码格里有效，跨代码格每次都要重新激活！**

```
# Install conda v2

%%bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b

%%bash
~/miniforge3/bin/conda init

! ln -s ~/miniforge3/bin/conda /usr/local/bin

! ln -s ~/miniforge3/bin/activate /usr/local/bin

! ln -s ~/miniforge3/bin/deactivate /usr/local/bin

%%bash
conda update -y conda -n base

!source ~/miniforge3/etc/profile.d/conda.sh

```





```

# Install coda

- https://towardsdatascience.com/conda-google-colab-75f7c867a522
- https://mmocr.readthedocs.io/zh_CN/latest/install.html


!which python
!python --version
!echo $PYTHONPATH
%env PYTHONPATH=

%%bash
MINICONDA_INSTALLER_SCRIPT=Miniconda3-4.5.4-Linux-x86_64.sh
MINICONDA_PREFIX=/usr/local
wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALLER_SCRIPT
chmod +x $MINICONDA_INSTALLER_SCRIPT
./$MINICONDA_INSTALLER_SCRIPT -b -f -p $MINICONDA_PREFIX

!which conda
!conda --version

%%bash
conda install --channel defaults conda python=3.7 --yes
conda update --channel defaults --all --yes

!conda --version
!python --version
import sys
sys.path
```



```
# Install Pytorch

!nvcc --version # check cuda version
!which nvcc

! pip3 uninstall torch --yes

import torch


! ls /usr/local/cuda

! python -m pip install torch==1.2.0 -f https://download.pytorch.org/whl/torch_stable.html

%%bash
git clone https://github.com/MhLiao/DB.git
# python dependencies
cd DB && pip install -r requirement.txt


```







```
https://towardsdatascience.com/conda-google-colab-75f7c867a522
```



```
!which python
!python --version
!echo $PYTHONPATH
%env PYTHONPATH=   # 安装前让此环境变量失效

%%bash
MINICONDA_INSTALLER_SCRIPT=Miniconda3-4.5.4-Linux-x86_64.sh
MINICONDA_PREFIX=/usr/local
wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALLER_SCRIPT
chmod +x $MINICONDA_INSTALLER_SCRIPT
./$MINICONDA_INSTALLER_SCRIPT -b -f -p $MINICONDA_PREFIX


```



## 中文

```
# https://albertauyeung.github.io/2020/03/15/matplotlib-cjk-fonts.html/

!wget 'https://github.com/googlefonts/noto-cjk/raw/main/Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Regular.otf'
import matplotlib.font_manager as fm
fprop = fm.FontProperties(fname='/content/NotoSerifCJKsc-Regular.otf')

import matplotlib.pyplot as plt
import random

# Prepare some data
x = list(range(20))
xticks = ["类別{:d}".format(i) for i in x]
y = [random.randint(10,99) for i in x]

# Plot the graph
plt.figure(figsize=(8, 2))
plt.bar(x, y)
plt.xticks(x, xticks, fontproperties=fprop, fontsize=12, rotation=45)
plt.title("圖1", fontproperties=fprop, fontsize=18)
plt.show()
```



## 聚类



```python
! pip install bert-serving-client
! pip install -U bert-serving-server[http]
%tensorflow_version 1.x
import tensorflow
print(tensorflow.__version__)
! python --version
! wget https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
! unzip ./chinese_L-12_H-768_A-12.zip 
! nohup bert-serving-start -model_dir=/content/chinese_L-12_H-768_A-12 > out.file 2>&1 &


from bert_serving.client import BertClient
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

! git clone https://github.com/fighting41love/funNLP.git
! wget 'https://github.com/googlefonts/noto-cjk/raw/main/Serif/OTF/SimplifiedChinese/NotoSerifCJKsc-Regular.otf'
import matplotlib.font_manager as fm
fprop = fm.FontProperties(fname='/content/NotoSerifCJKsc-Regular.otf')


from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
corpus = []
bc = BertClient()
km = KMeans(n_clusters=2)
pca = PCA(n_components=2)
gb = open('/content/funNLP/data/动物词库/THUOCL_animal.txt',encoding='utf-8').readlines()
for word in gb[:30]:    #为了方便，每个词库只取了前面30个单词
    word = word.split('\t')
    corpus.append(word[0])

fb = open('/content/funNLP/data/地名词库/THUOCL_diming.txt',encoding='utf-8').readlines()
for word in fb[:30]:
    word = word.split('\t')
    corpus.append(word[0])

vectors = bc.encode(corpus)
vectors_ = pca.fit_transform(vectors)   #降维到二维
y_ = km.fit_predict(vectors_)       #聚类
#plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(vectors_[:,0],vectors_[:, 1],c=y_)   #将点画在图上 # fontproperties
for i in range(len(corpus)):    #给每个点进行标注
    plt.annotate(s=corpus[i], xy=(vectors_[:, 0][i], vectors_[:, 1][i]),
                 xytext=(vectors_[:, 0][i] + 0.1, vectors_[:, 1][i] + 0.1),
                 fontproperties=fprop)
plt.show()
```



## 多分类



```
NLP（三十五）使用keras-bert实现文本多分类任务
https://blog.csdn.net/jclian91/article/details/111742576
```











```
# import pdb; pdb.set_trace()

Google Colab可直接从github打开Jupyter notebooks，

只需将“github.com”替换为“colab.research.google.com/github”，就会直接加载到Colab中 
```





```
# start()开始
# stop()结束

function getElementByXpath(path) {
       return document.evaluate(path, document, null, 
       XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}
 
function reconnect(){
	  console.log('working')
	  getElementByXpath("//div[@id='top-toolbar']/colab-connect-button").click()
}
var a = setInterval(reconnect, 1*60*1000);
function stop(){
	 clearInterval(a)
}
function start(){
	 a = setInterval(reconnect, 1*60*1000);
}
```

```
# autoClick.py

# windows
# pip install pygetwindow==0.0.1
# pip install pyautogui===0.9.0

import pyautogui as pygui
import time

print( pygui.position() )

while True:
    pygui.moveTo(555,555,15)
    # time.sleep(10)
    pygui.moveTo(333,333,15)
    # time.sleep(10)
    pygui.moveTo(666,666,15)
    # time.sleep(10)

    pygui.moveTo(1711,184,15) # win10 colab busy button
    pygui.click(x=1711, y=184, clicks=2, interval=10, button='left') # # win10 colab busy button
```





## stack overflow



```
# https://blog.csdn.net/sdujava2011/article/details/50578314

# https://math.stackexchange.com/

```







# 复分析-可视化方法



<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210507101840384.png" alt="image-20210507101840384" style="zoom:50%;" />

<img src="深入理解神经网络：从逻辑回归到CNN.assets/image-20210507101904256.png" alt="image-20210507101904256" style="zoom:50%;" />



当 theta很小时弧长近似于弦长，L=α× r ，其中r 是半径，α 是圆心角（弧度制），L 是弧长





