

[Pytorch autograd,backward详解](https://zhuanlan.zhihu.com/p/83172023)

[pytorch-tutorial-for-deep-learning-lovers](https://www.kaggle.com/kanncaa1/pytorch-tutorial-for-deep-learning-lovers)



[Yann LeCun 深度学习（Pytorch）2020 春季课程【官方字幕】](https://www.bilibili.com/video/av796677275/)

> [讲义](https://atcold.github.io/pytorch-Deep-Learning/)

[全-中英字幕-吴恩达 深度学习_Deep Learning_Pytorch特别制作版](https://www.bilibili.com/video/BV1BZ4y1M7hF/)

> [代码](https://gitee.com/inkCode/pytorch_tutorial)



## 张量

> x = torch.full((2,3), 4, requires_grad=True)  # (2*3) 初值4



## 导数



计算某个Tensor的导数，需要设置其`.requires_grad`属性为`True`

> 不需要算导数的就不设了吧？



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



### 自动求导

> [Pytorch中的vector-Jacobian product](https://juejin.im/post/6844904009841524750)
>
> [PyTorch for Deep Learning - Full Course / Tutorial](https://www.youtube.com/watch?v=GIsg-ZUy0MY&ab_channel=freeCodeCamp.org)
>
> [PyTorch 101, Part 1: Understanding Graphs, Automatic Differentiation and Autograd](https://blog.paperspace.com/pytorch-101-understanding-graphs-and-automatic-differentiation/)
>
> [pytorch自动求导Autograd系列教程](https://blog.csdn.net/qq_27825451/article/details/89393332)



####  grad_tensor 梯度张量

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









