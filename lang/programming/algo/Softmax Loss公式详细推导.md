



# 激活函数(Activation Function)









# 前向传播(Forward propagation)



上标是行，下标是列。**上标带括号的是行向量**，否则是标量


$$
X = 
\begin{bmatrix}
x^{1}_{0} & x^{1}_{1} & \cdots & x^{1}_{n}  \\
x^{2}_{0} & x^{2}_{1} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{0} & x^{m}_{1} & \cdots & x^{m}_{n} \\
\end{bmatrix}
$$

$$
Y =
\begin{bmatrix}
y^{1}  \\
y^{2}  \\
...  \\
y^{m}  \\
\end{bmatrix}
$$



> 手写数字识别图片大小是 28*28 = 784 像素，mini-batch 大小是64，既每次随机地取64 张图片来训练。
>
> 用随机选择的小批量数据（mini-batch）作为全体训练数据的近似值，损失函数要计算这一批数据的总体损失
>
> 所以 $X$ 的维度是：(64*784)，既 m = 64, n = 784
>
> 

