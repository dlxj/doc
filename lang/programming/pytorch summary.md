

**Udacity — deep-learning**-v2-pytorch [u](https://github.com/udacity/deep-learning-v2-pytorch)

**OpenAI — Spinning Up** [u](https://spinningup.readthedocs.io/zh_CN/latest/user/introduction.html)

DearPyGui 基础 [u](https://blog.csdn.net/hekaiyou/article/details/109386393)

DearPyGui 实现队列模型仿真[u](https://www.zhihu.com/zvideo/1307375212308856832)



**How Pytorch Backward() function works** [u](https://medium.com/@mustafaghali11/how-pytorch-backward-function-works-55669b3b7c62)

CSC321 Lecture 10: Automatic Differentiation [u](https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/slides/lec10.pdf)

官方电子书

> [Deep Learning With Pytorch by Eli Stevens, Luca Antiga, Thomas Viehmann (z-lib.org)]()

MatrixSlow 手写框架

> https://gitee.com/zackchen/MatrixSlow
>
> ```
> pip install protobuf
> pip install grpcio
> ```



[动手学深度学习Pytorch版](https://github.com/ShusenTang/Dive-into-DL-PyTorch)

[PyTorch for Deep Learning - Full Course / Tutorial](https://www.youtube.com/watch?v=GIsg-ZUy0MY&ab_channel=freeCodeCamp.org)

> [Linear Regression with PyTorch](https://jovian.ai/aakashns/02-linear-regression)

> conda list



李宏毅2020机器学习深度学习(完整版)国语

> [课程主页](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html)
>
> > [第一课作业](https://mrsuncodes.github.io/2020/03/15/%E6%9D%8E%E5%AE%8F%E6%AF%85%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0-%E7%AC%AC%E4%B8%80%E8%AF%BE%E4%BD%9C%E4%B8%9A/#more)
>
> [B站视频](https://www.bilibili.com/video/av94519857/)
>
> [PyTorch_Introduction.slides](http://speech.ee.ntu.edu.tw/~tlkagk/courses/ML2020/PyTorch_Introduction.slides.html#/)



[Pytorch autograd,backward详解](https://zhuanlan.zhihu.com/p/83172023)

[pytorch-tutorial-for-deep-learning-lovers](https://www.kaggle.com/kanncaa1/pytorch-tutorial-for-deep-learning-lovers)



[Yann LeCun 深度学习（Pytorch）2020 春季课程【官方字幕】](https://www.bilibili.com/video/av796677275/)

> [讲义](https://atcold.github.io/pytorch-Deep-Learning/)

[全-中英字幕-吴恩达 深度学习_Deep Learning_Pytorch特别制作版](https://www.bilibili.com/video/BV1BZ4y1M7hF/)

> [代码](https://gitee.com/inkCode/pytorch_tutorial)



## Kaggle 练习



> 1. Titanic（泰坦尼克之灾）
> 中文教程： 逻辑回归应用之Kaggle泰坦尼克之灾
> 英文教程：An Interactive Data Science Tutorial
>
> 2. House Prices: Advanced Regression Techniques（房价预测）
> 中文教程：Kaggle竞赛 — 2017年房价预测
> 英文教程：How to get to TOP 25% with Simple Model using sklearn
>
> 3. Digital Recognition（数字识别）
> 中文教程：大数据竞赛平台—Kaggle 入门
> 英文教程：Interactive Intro to Dimensionality Reduction





## 线性回归 [u](https://jovian.ai/aakashns/02-linear-regression)

### 要点：更新仅重时不要跟踪梯度

> ```python
> with torch.no_grad():
> ```

### 要点：梯度用完后置0再重新算

> ```python
> .grad.zero_()
> ```



> \# 前向传播, @ 是矩阵乘
>
> def model(x):
>
>   return x @ w.t() + b
>
> \# 均方误差损失函数 MSE loss 
>
> def mse(t1, t2):
>
>   diff = t1 - t2
>
>   return torch.sum(diff * diff) / diff.numel()
>
> \# Train for 100 epochs
>
> for i in range(10000):
>
>   preds = model(inputs)
>
>   print(preds)
>
>   print(targets)
>
>   loss = mse(preds, targets)
>
>   loss.backward()
>
>   **with torch.no_grad()**:
>
> ​    w -= w.grad * 1e-5
>
> ​    b -= b.grad * 1e-5
>
> ​    **w.grad.zero_()**
>
> ​    **b.grad.zero_()**



## 提前退出

```python
with torch.no_grad():
	errs = torch.sum( torch.abs(E) )

if errs < 0.05:
	print(f'stop at {k}')
    print("Weight: ")
    print(W)
    break
```



## 线性模型
> **自动生成并初始化权重和偏置**
>
> ```python
> """
> 定义线性模型，自动生成并初始化所需权重和偏置
> y = x A^T + b --> x @ A.t() + b
> nn.Linear
>    第一参：一条输入样本的维数(行向量)
>    第二参：一条输出样本的维数(行向量)
> """
> model = nn.Linear(3, 2)  # 输入3 维(行向量)，输出2 维(行向量)
> print(model.weight)
> print(model.bias)
> list(model.parameters()) # 返回模型中的所有权重和偏置
> ```

```python
    seq_model = nn.Sequential( # 双隐层模型
        nn.Linear(2, 2),       # 一输入，一隐层
        nn.Sigmoid(),
        nn.Linear(2, 1),       # 一隐层，一输出
    )
	
    # seq_model = nn.Sequential(OrderedDict([
    #     ('hidden_linear', nn.Linear(1, 8)),
    #     ('hidden_activation', nn.Tanh()),
    #     ('output_linear', nn.Linear(8, 1))
    # ]))
```







计算构建了计算图，输出结果带有grad_fn，否则没有

t1.sum().detach() # 和原来的计算图分离

loss_fn = F.cross_entropy



## 张量

```python
torch.rand()
torch.randn()
torch.normal()
torch.linespace()
```

```python
x = torch.full((2,3), 4, requires_grad=True)  # (2*3) 初值4
inputs = torch.from_numpy(inputs)
```

```python
X = np.array([
	[0,0],
	[0,1],
	[1,0],
	[1,1]
], dtype=float)

Y = np.array([
	[0],
	[1],
	[1],
	[0]
], dtype=float)
X = torch.from_numpy(X)
Y = torch.from_numpy(Y)
```



### 矩阵乘@和转置t

> ```python
> def model(x):
>     return x @ w.t() + b
> ```
>
> `@` represents matrix multiplication in PyTorch, and the `.t` method returns the transpose of a tensor.



### torch.stack()

> 低维张量堆叠起来（维度增加），生成高维空间中的高维张量
>
> > 就像把桌面上的书堆起来一样



## 损失函数

> ```
> # MSE loss
> def mse(t1, t2):
>     diff = t1 - t2
>     return torch.sum(diff * diff) / diff.numel()
> ```
>
> `torch.sum` returns the sum of all the elements in a tensor, and the `.numel` method returns the number of elements in a tensor. Let's compute the mean squared error for the current predictions of our model.



## 导数



### 计算雅可比 [u](https://pytorch.org/docs/stable/autograd.html)

```python
x = torch.ones(3, requires_grad=True)
def calc(x):
	return torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))
jacobian = torch.autograd.functional.jacobian(calc, x)
```

```python
def calc(w, x):
	return w @ x
j = torch.autograd.functional.jacobian( lambda w: calc(w, X), W ) 
# 现在X是常量了，只算W的雅可比
```







计算某个Tensor的导数，需要设置其`.requires_grad`属性为`True`

> 不需要算导数的就不设了吧？



### **vector-Jacobian product** 

- $J \cdot v$ 中的v 是人为的给各**微量变化比加权重**，调大调小变化影响力

  > $J^T \cdot v$ 是列向量 [CSC321 Lecture 10：Automatic Differentiation]()
  >
  > $v^T \cdot J$ 是行向量

 [u](https://stackoverflow.com/questions/64260561/pytorch-compute-vector-jacobian-product-for-vector-function)

> ```python
> def j3():
>     x = torch.ones(3, requires_grad=True)
> 
>     y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))
> 
>     v = torch.tensor([3, 5, 7])
> 
>     y.backward(v)
>     print(x.grad)
>     """
>     The Jacobian seems correct and if it multiplies on vector (3, 5, 7) I would expect result to be (11, 17, 14).
>     Got it! We should transpose Jacobian before multiplication. Then everything matches.
>     """
> 
>     print( torch.matmul(  torch.tensor([ [2, 0, 0], [1, 2 , 0], [0, 1, 2] ]),  torch.tensor([ [3], [5], [7] ]) ) )       # J.t() @ v  结果是列向量
>     print( torch.matmul(  torch.tensor([ [3], [5], [7] ]).t(), torch.tensor([ [2, 1, 0], [0, 2 , 1], [0, 0, 2] ])  ) )   # v.t() @ J  结果是行向量
> ```



### Generalized Jacobian

- 广义雅可比

> There are two ways to compute the Generalized Jacobian that I'm aware of in PyTorch.
>
> ## Option 1
>
> Repeated application of back-propagation on each element of Y.
>
> ```python
> import torch
> 
> def construct_jacobian(y, x, retain_graph=False):
>     x_grads = []
>     for idx, y_element in enumerate(y.flatten()):
>         if x.grad is not None:
>             x.grad.zero_()
>         # if specified set retain_graph=False on last iteration to clean up
>         y_element.backward(retain_graph=retain_graph or idx < y.numel() - 1)
>         x_grads.append(x.grad.clone())
>     return torch.stack(x_grads).reshape(*y.shape, *x.shape)
> ```
>
> then the Jacobian for your test case may be computed using
>
> ```python
> a = torch.tensor([1., 2., 3.])
> b = torch.tensor([4., 5., 6.], requires_grad=True)
> c = a * b
> 
> jacobian = construct_jacobian(c, b)
> 
> print(jacobian)
> ```
>
> which results in
>
> ```py
> tensor([[1., 0., 0.],
>         [0., 2., 0.],
>         [0., 0., 3.]])
> ```
>
> ## Option 2
>
> In PyTorch 1.5.1 a new autograd.functional API was introduced, including the new function [`torch.autograd.functional.jacobian`](https://pytorch.org/docs/stable/autograd.html#torch.autograd.functional.jacobian). This produces the same results as the previous example but takes a function as an argument. Not demonstrated here, but you can provide the `jacobian` function a list of inputs if your function takes multiple independent tensors as input. In that case the `jacobian` would return a tuple containing the Generalized Jacobian for each of the input arguments.
>
> ```python
> import torch
> 
> a = torch.tensor([1., 2., 3.])
> 
> def my_fun(b):
>     return a * b
> 
> b = torch.tensor([4., 5., 6.], requires_grad=True)
> 
> jacobian = torch.autograd.functional.jacobian(my_fun, b)
> 
> print(jacobian)
> ```
>
> which also produces
>
> ```py
> tensor([[1., 0., 0.],
>         [0., 2., 0.],
>         [0., 0., 3.]])
> ```
>
> ------
>
> As an aside, in some literature the term "gradient" is used to refer to the transpose of the Jacobian matrix. If that's what you're after then, assuming Y and X are vectors, you can simply use the code above and take the transpose of the resulting Jacobian matrix. If Y or X are higher order tensors (matrices or n-dimensional tensors) then I'm not aware of any literature that distinguishes between gradient and Generalized Jacobian. A natural way to represent such a "transpose" of the Generalized Jacobian would be to use `Tensor.permute` to turn it into a tensor of shape (n1, n2, ..., nD, m1, m2, ..., mE).
>
> ------
>
> As another aside, the concept of the Generalized Jacobian is rarely used in literature ([example usage](http://cs231n.stanford.edu/handouts/derivatives.pdf)) but is actually relatively useful in practice. This is because it basically works as a bookkeeping technique to keep track of the original dimensionality of Y and X. By this I mean you could just as easily take Y and X and flatten them into vectors, regardless of their original shape. Then the derivative would be a standard Jacobian matrix. Consequently this Jacobian matrix would be equivalent to a reshaped version of the Generalized Jacobian.



**pytorch: compute vector-Jacobian product for vector function** [u](https://stackoverflow.com/questions/64260561/pytorch-compute-vector-jacobian-product-for-vector-function)

You should not define tensor y by `torch.tensor()`, `torch.tensor()` is a tensor constructor, not an operator, so it is not trackable in the operation graph. You should use `torch.stack()` instead.

Just change that line to:

```py
y = torch.stack((x[0]**2+x[1], x[1]**2+x[2], x[2]**2))
```

the result of `x.grad` should be `tensor([ 6., 13., 19.])`

> Thank you very much! Could you please elaborate on why the result is (6, 13, 19)? The Jacobian seems correct and if it multiplies on vector (3, 5, 7) I would expect result to be (11, 17, 14)... Probably I misunderstand how backward + grad are executed. 
>
> Got it! We should transpose Jacobian before multiplication. Then everything matches. 



**CSC321 Lecture 10：Automatic Differentiation** [u]()

<img src="pytorch summary.assets/image-20201106170230230.png" alt="image-20201106170230230" style="zoom:67%;" />



**Pytorch most efficient Jacobian calculation** [u](https://stackoverflow.com/questions/56480578/pytorch-most-efficient-jacobian-hessian-calculation)



Choose a Jacobian Method for an Implicit Solver [u](https://www.mathworks.com/help/simulink/ug/choose-a-jacobian-method-for-an-implicit-solver.html)

> 稀疏方程组的“稀疏” 雅可比

![image-20201106150018039](pytorch summary.assets/image-20201106150018039.png)

<img src="pytorch summary.assets/image-20201106150102142.png" alt="image-20201106150102142" style="zoom: 67%;" />



### 清空梯度

- 梯度计算时会一直自动累加所以需要清掉

> 清空张量的梯度
> ```python
> if W.grad is not None:
> 	W.grad.data.zero_()
> ```
>
> 清空优化器的梯度
>
> ```python
> opt.zero_grad()
> ```



### leaf nodes (叶子节点)

> **自定义产生**的tensor 是叶子节点
>
> grad_fn 通常为None
>
> grad: 该Tensor的梯度值，每次在计算backward时都需要将前一时刻的梯度归零，否则梯度值会一直累加



**结果节点**

> **计算产生**的tensor 是结果节点
>
> **grad_fn** 指出梯度函数是哪种类型 PowBackward，AddBackward 等



**计算叶子节点的梯度值**

> 结果节点是标量，直接调用.backward()
>
> 非结果节点需要定义`grad_tensor`来计算矩阵的梯度
>
> > 



### 自动求导 [u](https://www.jianshu.com/p/aa7e9f65fa3e)

> [Pytorch中的vector-Jacobian product](https://juejin.im/post/6844904009841524750)
>
> [PyTorch for Deep Learning - Full Course / Tutorial](https://www.youtube.com/watch?v=GIsg-ZUy0MY&ab_channel=freeCodeCamp.org)
>
> [PyTorch 101, Part 1: Understanding Graphs, Automatic Differentiation and Autograd](https://blog.paperspace.com/pytorch-101-understanding-graphs-and-automatic-differentiation/)
>
> [pytorch自动求导Autograd系列教程](https://blog.csdn.net/qq_27825451/article/details/89393332)



> `torch.autograd.backward(tensors, grad_tensors=None, retain_graph=None, create_graph=False, grad_variables=None)`参数介绍如下：
>
> - **tensors**(tensor序列) — 需要被求导的张量
> - **grad_tensors**(tensor序列或None) — Jacobian矢量积中的矢量，也可理解为链式法则的中间变量的梯度
> - **create_graph**(bool) — 默认为false，否则会对反向传播过程再次构建计算图，可通过backward of backward实现求高阶函数
>    `backward()`函数中的grad_tesnors参数size需要与根节点的size相同。当根节点为标量时，则无需说明该参数，例如对`out`进行反向求导



####  grad_tensor 梯度张量

> ```python
> A.backward( torch.ones_like(A) )
> ```
>
> 作为参数传递给`backward()` 函数
>
> Y计算标量损失l。假设向量v恰好是标量损失l关于向量Y的梯度
>
> PyTorch从不显式地构造整个雅可比矩阵。直接计算JVP (Jacobian vector product)通常更简单、更有效



> ```php
> # 假如针对一个模型有两个Loss，先执行第一个的backward，再执行第二个backward
> loss1.backward(retain_graph=True)
> loss2.backward()  # 执行完这个后，所有中间变量都会被释放，以便下一次的循环
> optimizer.step()  # 更新参数
> ```
> ```objectivec
> self.target = target.detach() * weight # 这里只是单纯地将其当作常量来对待，因此使用了detach，则在backward中计算梯度时不对target之前所在的计算图存在任何影响
> ```




Torch张量和numpy数组将共享潜在的内存，改变其中一个也将改变另一个

> a = torch.ones(5)
>
> b = a.**numpy()**
>
> a.add_(1)
>
> --> tensor([2., 2., 2., 2., 2.]) 
>
> [ 2.  2.  2.  2.  2.]

> a = np.ones(5)
>
> b = **torch.from_numpy**(a)
>
> np.add(a, 1, out=a)



更改Tensor的**requires_grad 自动求导标志**

>  **requires_grad  默认是False, 它有传递性**
>
> a.requires_grad_(True)
>
> print(a.requires_grad)



使用**torch.no_grad()包装代码块**

> ```python
> with torch.no_grad():
> 	errs = torch.sum( torch.abs(E) )
> ```
>
> 显示的指明不需要梯度，既使变量拥有requires_grad = True 属性



矩阵乘

> import torch
>
> import numpy as np
>
> X = torch.tensor(
>
>   np.array([
>
> ​        [1, 0, 0],
>
> ​        [1, 0, 1],
>
> ​        [1, 1, 0],
>
> ​        [1, 1, 1]
>
> ​       ], np.float)
>
> )
>
> X.requires_grad = True # **requires_grad  默认是False, 它有传递性**
>
> 
>
> W = torch.tensor(
>
>   np.random.uniform(size=(3, 1))
>
> ) # 3*1 权重
>
> A = torch.matmul( X, W )



## Data load

> 比如你有1000组数据（假设每组数据为三通道256px×256px的图像），batchsize为4，那么每次训练则提取(4,3,256,256)维度的张量来训练，刚好250个epoch解决(250×4=1000)。但是如果你有999组数据，你继续使用batchsize为4的话，这样999和4并不能整除，你在训练前249组时的张量维度都为(4,3,256,256)但是最后一个批次的维度为(3,3,256,256)，Pytorch检查到(4,3,256,256) != (3,3,256,256)，维度不匹配，自然就会报错了，这可以称为一个小bug


## Coursera.org

## IBM 

[Deep Neural Networks with PyTorch](https://www.coursera.org/learn/deep-neural-networks-with-pytorch/home/welcome)

[第 2 周](https://www.coursera.org/learn/deep-neural-networks-with-pytorch/home/week/2)

<img src="pytorch summary.assets/image-20201104174215977.png" alt="image-20201104174215977" style="zoom:50%;" />



<img src="pytorch summary.assets/image-20201104174752047.png" alt="image-20201104174752047" style="zoom:50%;" />



<img src="pytorch summary.assets/image-20201104175236699.png" alt="image-20201104175236699" style="zoom:50%;" />

```python

# https://jovian.ai/aakashns/02-linear-regression

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

class hardway():
    # 前向传播, @ 是矩阵乘
    def model(self, x, w, b):
        return x @ w.t() + b

    # 均方误差损失函数 MSE loss 
    def mse(self, t1, t2):
        diff = t1 - t2
        return torch.sum(diff * diff) / diff.numel()

    def dosomething(self):
        
        model = self.model
        mse = self.mse

        # Input (temp, rainfall, humidity)
        inputs = np.array([
                   [73, 67, 43], 
                   [91, 88, 64], 
                   [87, 134, 58], 
                   [102, 43, 37], 
                   [69, 96, 70]], dtype='float32')
        #(5 * 3)

        # Targets (apples, oranges)
        targets = np.array([[56, 70], 
                    [81, 101], 
                    [119, 133], 
                    [22, 37], 
                    [103, 119]], dtype='float32')
        #(5 * 2)

        # Convert inputs and targets to tensors
        inputs = torch.from_numpy(inputs)
        targets = torch.from_numpy(targets)

        # Weights and biases
        w = torch.randn(2, 3, requires_grad=True)
        b = torch.randn(2, requires_grad=True)
        print(w)
        print(b)

        # Train for 100 epochs
        for i in range(10000):
            preds = model(inputs, w, b)
            print(preds)
            print(targets)
            loss = mse(preds, targets)
            loss.backward()
            with torch.no_grad():
                w -= w.grad * 1e-5
                b -= b.grad * 1e-5
                w.grad.zero_()
                b.grad.zero_()

class easyway():
    def dosomething(self):

        # Define loss function
        loss_fn = F.mse_loss

        # Input (temp, rainfall, humidity)
        inputs = np.array([[73, 67, 43], [91, 88, 64], [87, 134, 58], 
                   [102, 43, 37], [69, 96, 70], [73, 67, 43], 
                   [91, 88, 64], [87, 134, 58], [102, 43, 37], 
                   [69, 96, 70], [73, 67, 43], [91, 88, 64], 
                   [87, 134, 58], [102, 43, 37], [69, 96, 70]], 
                  dtype='float32')

        # Targets (apples, oranges)
        targets = np.array([[56, 70], [81, 101], [119, 133], 
                    [22, 37], [103, 119], [56, 70], 
                    [81, 101], [119, 133], [22, 37], 
                    [103, 119], [56, 70], [81, 101], 
                    [119, 133], [22, 37], [103, 119]], 
                   dtype='float32')

        inputs = torch.from_numpy(inputs)
        targets = torch.from_numpy(targets)

        # Define dataset
        train_ds = TensorDataset(inputs, targets)  # 生成训练样本  (  tensor(输入), tensor(输出)  )
        print( train_ds[0:3] )  # 查看前三条样本

        # Define data loader
        batch_size = 5
        train_dl = DataLoader(train_ds, batch_size, shuffle=True)  # 样本分组(batches)，5 条样本一组 # shuffle 重新洗牌，既乱序

        for xb, yb in train_dl:
            print(xb)
            print(yb)
            break
        
        # Define model
        """
        y = x A^T + b
        nn.Linear
            第一参：x 一条样本的维数(行向量)
            第二参：y 一条样本的维数(行向量)  
        """
        model = nn.Linear(3, 2)  # 自动生成并初始化权重和偏置  # 输入3 维(行向量)，输出2 维(行向量)
        print(model.weight)
        print(model.bias)

        # Parameters
        list(model.parameters())  # 返回模型中的所有权重和偏置

        opt = torch.optim.SGD(model.parameters(), lr=1e-5)

        num_epochs = 5000

        # Repeat for given number of epochs
        for epoch in range(num_epochs):
        
            # Train with batches of data
            for xb,yb in train_dl:
            
                # 1. Generate predictions
                pred = model(xb)
            
                # 2. Calculate loss
                loss = loss_fn(pred, yb)
            
                # 3. Compute gradients
                loss.backward()
            
                # 4. Update parameters using gradients
                opt.step()
            
                # 5. Reset the gradients to zero
                opt.zero_grad()
        
            # Print the progress
            if (epoch+1) % 10 == 0:
                print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))


if __name__ == "__main__":

    hard = hardway()
    #hard.dosomething()

    easy = easyway()
    easy.dosomething()

    print('hi,,,')
```



```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

def OR():
    X = torch.tensor([
            [0,0],
            [0,1],
            [1,0],
            [1,1]
        ], dtype=torch.float32)

    Y = torch.tensor([
            [0],
            [1],
            [1],
            [1]
        ], dtype=torch.float32)

    """
    定义线性模型，自动生成并初始化所需权重和偏置
    y = x w^T + b --> x @ w.t() + b
    nn.Linear
        第一参：一条输入样本的维数(行向量)
        第二参：一条输出样本的维数(行向量)
    """
    model = nn.Linear(2, 1)  # X 第一行维度是2， Y 第一行的维度是1
    print(model.weight)
    print(model.bias)
    list(model.parameters()) # 返回模型中的所有权重和偏置

    # Define dataset
    train_ds = TensorDataset(X, Y)  # 生成训练样本  (  tensor(输入), tensor(输出)  )
    print( train_ds[0:2] )          # 查看前两条样本

    # Define data loader
    batch_size = 2
    train_dl = DataLoader(train_ds, batch_size, shuffle=True)  # 样本分组(batches)，2 条样本一组 # shuffle 重新洗牌，既乱序

    opt = torch.optim.SGD(model.parameters(), lr=1e-5)  # 定义优化方法：随机梯度下降

    # Define loss function
    loss_fn = F.mse_loss  # 定义损失函数：均方误差损失函数

    num_epochs = 10000

    # Repeat for given number of epochs
    for epoch in range(num_epochs):
        
        # Train with batches of data
        for xb,yb in train_dl:
            
            # 1. Generate predictions
            pred = model(xb)
            
            # 2. Calculate loss
            loss = loss_fn(pred, yb)
            
            # 3. Compute gradients
            loss.backward()
            
            # 4. Update parameters using gradients
            opt.step()
            
            # 5. Reset the gradients to zero
            opt.zero_grad()
        
        # Print the progress
        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

if __name__ == "__main__":
    OR()
```



## 用pytorch实现吴恩达老师深度学习课程课后编程作业 [u](https://blog.csdn.net/weixin_44581161/article/details/106697267)

```python
import torch.nn as nn
import torch
import numpy as np
#我们随机创建一组训练数据，100个具有500维特征的数据
M=100
features=500
train_x = torch.randn(M, features)
train_y = torch.randint(0, 2, [M,1]).float()         #数据集统一是float类型

#建立网络
in_put=features
Hidden1=10
Hidden2=5
out_put=1         #这里是一个输入层，两个隐藏层和一个输出层。

model = torch.nn.Sequential(
     torch.nn.Linear(in_put, Hidden1, bias=True),
     torch.nn.Sigmoid(),
     torch.nn.Linear(Hidden1, Hidden2, bias=True),
     torch.nn.ReLU(),
     torch.nn.Linear(Hidden2, out_put, bias=True),
     torch.nn.Sigmoid(),
)


#模型建好以后要定义损失函数和模型优化方法，torch包含多种方法，可自行百度
iter_n=1000       #迭代次数
learn_rate=1e-2
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)

#开始优化
for i in range(iter_n):
    y_pred=model(train_x)            #一次训练后得到的结果
    loss=loss_fn(y_pred,train_y)
    print(i,loss.item())
    optimizer.zero_grad()            #下面这三行可理解为固定搭配，就是更新w，b的值的
    loss.backward()
    optimizer.step()
```

```python
参数初始化
#model[0].weight是第0层的w参数，其他层可同样的方法初始化参数，初始化在建好model后使用，怎样建model参考上一篇。
# 0-1之间均匀分布
torch.nn.init.uniform_(model[0].weight, a=0, b=1)
# 初始化为常数0.5
torch.nn.init.constant_(model[0].weight, 0.5)
# 正态分布
torch.nn.init.normal_(model[0].weight)


正则化
正则化是用来减小过拟合的方法，这里给出L2正则化方法和dropout方法
L2正则化

optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate,weight_decay=0.01)
#这里的weight_decay=0.01相当于λ参数。
1
2
dropout方法

model=torch.nn.Sequential(
    torch.nn.Linear(in_put,Hidden1,bias=True),
    torch.nn.ReLU(),
    torch.nn.Dropout(0.2),
    torch.nn.Linear(Hidden1,Hidden2,bias=True),
    torch.nn.ReLU(),
    torch.nn.Dropout(0.2),
    torch.nn.Linear(Hidden2,out_put,bias=True),
    torch.nn.Sigmoid(),
)
#在每层后边加上torch.nn.Dropout(0.2)，0.2是随机架空该层20%神经元。
```



