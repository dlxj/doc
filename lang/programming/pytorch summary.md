

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
> W = torch.tensor(
>
>   np.random.uniform(size=(3, 1))
>
> ) # 3*1 权重
>
> A = torch.matmul( X, W )









