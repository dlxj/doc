$$
\begin{align}
f(x) &= cx^{n} \\
f(x)'&= cn \ast x^{n -1}
\end{align}
$$

$$
(f \circ g)'(x) = f'\big( g(x) \big ) g'(x)
$$





$$
\mathcal{L} = \frac{1}{2} (y - t) ^ 2
$$

令：$z = y - t$,  则  $\mathcal{L} = \frac{1}{2} z ^ 2 \\$,  根据链式法则有：

 $\frac{\partial \mathcal{L}}{\partial z} = \frac{1}{2} * 2 * z = z$ ,  $\frac{\partial \mathcal{z}}{\partial y} = 1$

$\frac{\partial \mathcal{L}}{\partial y} = \frac{\partial \mathcal{L}}{\partial z} \frac{\partial \mathcal{z}}{\partial y} = z * 1 = z = y - t$   



根据复合函数求导法则： $(f \circ g)'(x) = f'\big( g(x) \big ) g'(x)$ 有，



$$
(\mathcal{L} \circ z)'(y) = \mathcal{L}' ( z(y) ) z'(y) \\
= z(z(y)) \\
= z(y-t) \\
= (y-t) -t \\
= y - 2t
$$











<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220816091436676.png" alt="image-20220816091436676" style="zoom: 80%;" />

注：符号 $\overline{z}$  表示 $\frac{\partial \mathcal{L}}{\partial z}$ 
$$
\mathcal{L} = \frac{1}{2} (y - t) ^ 2 \\
y = \sigma(z)
$$

$$
\frac{\partial \mathcal{L}}{\partial y} = y - t = \overline{y} \\

\frac{\partial \mathcal{y}}{\partial z} = \frac{\partial \mathcal{\sigma}}{\partial z} = \mathcal{\sigma}'(z) \\

\frac{\partial \mathcal{z}}{\partial w} = x
$$


所以有：
$$
\overline{z} = \frac{\partial \mathcal{L}}{\partial y} \frac{\partial \mathcal{y}}{\partial z} = \overline{y} \ \mathcal{\sigma}'(z)
$$

$$
\overline{w} = \frac{\partial \mathcal{L}}{\partial y} \frac{\partial \mathcal{y}}{\partial z} \ \frac{\partial \mathcal{z}}{\partial w} \\
= \overline{z} x
$$


- 克罗内克积

  - https://baike.baidu.com/item/%E5%85%8B%E7%BD%97%E5%86%85%E5%85%8B%E7%A7%AF/6282573

    > vec(X)表示矩阵X的向量化，它是把X的所有列堆起来所形成的列向量。



- **矩阵求导术(下)**



![image-20220816162311376](CSC321 Lecture 10：Automatic Differentiation.assets/image-20220816162311376.png)

![image-20220816162431342](CSC321 Lecture 10：Automatic Differentiation.assets/image-20220816162431342.png)



```
jax.numpy.kron(a, b)
```







- https://www.zhihu.com/question/58312854

















