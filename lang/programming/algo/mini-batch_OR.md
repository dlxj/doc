

```
用随机选择的小批量数据（mini-batch）作为全体训练数据的近似值，损失函数要计算这一批数据的总体损失

OR 问题的每一个输入维度是 (2,) , batch 大小设为3，既每次训练三组输入数据，作为全体训练数据的近似


使用单隐层网络结构，矩阵的维度变化：
	(3,2).(2,2) = (3,2)
	
```



$m=3, n=2, c=2, nclass=2$


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
a^{1}_{1,1} = x^0_{1,*} \cdot w^1_{*,1} \\
= x^0_{1,1} w^1_{1,1} + x^0_{1,2} w^1_{2,1} + \cdots + x^0_{1,n} w^1_{n,1}
$$

$$
a^{1}_{1,c} = x^0_{1,*} \cdot w^1_{*,c} \\
= x^0_{1,1} w^1_{1,c} + x^0_{1,2} w^1_{2,c} + \cdots + x^0_{1,n} w^1_{n,c}
$$

$$
a^{1}_{m,c} = x^0_{m,*} \cdot w^1_{*,c} + b^1_{m,c} \\
= x^0_{m,1} w^1_{1,c} + x^0_{m,2} w^1_{2,c} + \cdots + x^0_{m,n} w^1_{n,c}
$$


$$
\frac{ \partial }{ \partial w^1_{s,r} } a^1_{i,j} = 0, if \ r  \neq j
$$

$$
\frac{ \partial }{ \partial w^1_{s,r} } a^1_{i,j} = x^0_{i,s} \ , if \ r  = j
$$


$$
\frac{ \partial }{ \partial b^1_{s,r} } a^1_{i,j} = 0, if \ r  \neq j \ OR  \ s  \neq i
$$

$$
\frac{ \partial }{ \partial b^1_{s,r} } a^1_{i,j} = 1, if \ r  = j \ AND  \ s  = i
$$






$$
Softmax \bigg (

\begin{bmatrix}
a^{1}_{1,1} & a^{1}_{1,2} & \cdots & a^{1}_{1,c}  \\
a^{1}_{2,1} & a^{1}_{2,2} & \cdots & a^{1}_{2,c} \\
\vdots & \vdots & \ddots & \vdots & \\
a^{1}_{m,1} & a^{1}_{m,2} & \cdots & a^{1}_{m,c} \\
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


$$ { }
\frac{\partial}{\partial a^1_{s,r}} p_{i,j} = 0, if \ s  \neq i
$$

$$
\frac{\partial}{\partial a^1_{s,r}} p_{i,j} = p_{i,j} (1 - p_{i,j}), \ if \ s  = i \ AND \ r = j
$$

$$
\frac{\partial}{\partial a^1_{s,r}} p_{i,j} = -p_{i,j} \ p_{i,r}, \ if \ s  = i \ AND \ r \neq j
$$


$$
\frac{\partial}{\partial w^1_{s,r}} log(p_{i,j}) = log'(p_{i,j}(w^1_{s,r})) p_{i,j}'(w^1_{s,r})
$$


$$
p_{i,j} = \frac{e^{a^1_{i,j}}}{\sum^{nclass}_{k=1} e^{a^1_{i,k}}}, \ i \in 1 \cdots m; \ j \in 1 \cdots nclass \\
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


$$
y_i 是真实概率 \\
ce_{i,1} = - \sum^{nclass}_{j=1} y_{i,j}  log \ p_{i,j}
$$

$$
\ if \ s = i \  AND \ \ r = j \\
\frac{\partial}{\partial a^1_{s,r}} ce_{i,1} = - y_{i,r}  (1 - p_{i,r}) \\
$$

$$
\ if \ s = i \  AND \ \ r \neq j \\
\frac{\partial}{\partial a^1_{s,r}} ce_{i,1} = - \sum^{nclass}_{j=1} y_{i,j} \frac{1}{p_{i,j}} \frac{\partial}{\partial a^1_{s,r}} p_{i,j}  \\

= - \sum^{nclass}_{j=1} y_{i,j} \frac{1}{p_{i,j}} \frac{\partial}{\partial a^1_{s,r}} p_{i,j} \\

= - \sum^{nclass}_{j \neq r} y_{i,j} \frac{1}{p_{i,j}} (-p_{i,j} \ p_{i,r}) \\

=  \sum^{nclass}_{j \neq r} y_{i,j} p_{i,r}
$$

$$
\ if \ s = i \ \\
\frac{\partial}{\partial a^1_{s,r}} ce_{i,1} = - y_{i,r}  (1 - p_{i,r}) +  

\sum^{nclass}_{j \neq r} y_{i,j} p_{i,r}

\\
$$



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


$$
\ if \ s = i \  \\ 
\frac{\partial}{\partial a^1_{s,r}} L = \frac{1}{m} \frac{\partial}{\partial a^1_{s,r}} ce_{s,1} \\

= \frac{1}{m} \bigg ( - y_{i,r}  (1 - p_{i,r}) +  

\sum^{nclass}_{j \neq r} y_{i,j} p_{i,r} \bigg )
$$



$$
L(w^1_{1,1}, w^1_{1,2}, \cdots, w^1_{n,c}) = \frac{1}{m} \sum^{m}_{i=1} ce_{i,1} \\

= - \frac{1}{m} \sum^{m}_{i=1} \sum^{nclass}_{j=1} y_{i,j}  log \ p_{i,j} \\
$$



$$
\frac{\partial}{\partial w^1_{s,r}} L = - \frac{1}{m} \sum^{m}_{i=1} \sum^{nclass}_{j=1} y_{i,j}  \frac{\partial}{\partial w^1_{s,r}} log \ p_{i,j} \\



$$


$$
\frac{\partial}{\partial w^1_{s,r}} log ( \ p_{i,j} ) = \frac{1}{p_{i,j}}  \frac{\partial}{\partial w^1_{s,r}} p_{i,j} \\
$$




$$
\frac{\partial}{\partial w^1_{s,r}} p_{i,j}  = \frac{\partial}{\partial w^1_{s,r}} \frac{e^{a^1_{i,j}}}{\sum^{nclass}_{k=1} e^{a^1_{i,k}}}, \ i \in 1 \cdots m; \ j \in 1 \cdots nclass \\
$$




```
# https://zhuanlan.zhihu.com/p/86184547
# https://stats.stackexchange.com/questions/235528/backpropagation-with-softmax-cross-entropy
```




$$
\text{p 是真实分类概率，one-hot encoding}  \\

\begin{bmatrix}
p_{1,1} & p_{1,2} \\
p_{2,1} & p_{2,2} \\
p_{3,1} & p_{3,2} \\
\end{bmatrix}
$$

$$
\begin{bmatrix}
x_{1,1} & x_{1,2} \\
x_{2,1} & x_{2,2} \\
x_{3,1} & x_{3,2}  \\
\end{bmatrix}

\cdot

\begin{bmatrix}
w_{1,1} & w_{1,2} \\
w_{2,1} & w_{2,2} \\
\end{bmatrix}

+ 

\begin{bmatrix}
b_{1,1} & b_{1,2} \\
b_{2,1} & b_{2,2} \\
b_{3,1} & b_{3,2} \\
\end{bmatrix}

\\

= 

\begin{bmatrix}
a_{1,1} & a_{1,2} \\
a_{2,1} & a_{2,2} \\
a_{3,1} & a_{3,2} \\
\end{bmatrix}
$$

$$
a_{1,1} = x_{1,1} w_{1,1} + x_{1,2} w_{2,1} + b_{1,1} \\

a_{1,2} = x_{1,1} w_{1,2} + x_{1,2} w_{2,2} + b_{1,2}
$$

$$
a_{2,1} = x_{2,1} w_{1,1} + x_{2,2} w_{2,1} + b_{2,1} \\

a_{2,2} = x_{2,1} w_{1,2} + x_{2,2} w_{2,2} + b_{2,2}
$$




$$
\text{q 是预测出的近似概率} \\ 

Softmax \bigg (

\begin{bmatrix}
a_{1,1} & a_{1,2} \\
a_{2,1} & a_{2,2} \\
a_{3,1} & a_{3,2} \\
\end{bmatrix}

\bigg ) 


= 

\begin{bmatrix}
q_{1,1} & q_{1,2} \\
q_{2,1} & q_{2,2} \\
q_{3,1} & q_{3,2} \\
\end{bmatrix}
$$

$$
q_{1,1} = \frac{e^{a_{1,1}}}{e^{a_{1,1}} + e^{a_{1,2}} } \\

q_{1,2} = \frac{e^{a_{1,2}}}{e^{a_{1,1}} + e^{a_{1,2}} }
$$

$$
q_{2,1} = \frac{e^{a_{2,1}}}{e^{a_{2,1}} + e^{a_{2,2}} } \\

q_{2,2} = \frac{e^{a_{2,2}}}{e^{a_{2,1}} + e^{a_{2,2}} }
$$




$$
\text{交叉熵} \\

Cross \bigg (

\begin{bmatrix}
q_{1,1} & q_{1,2} \\
q_{2,1} & q_{2,2} \\
q_{3,1} & q_{3,2} \\
\end{bmatrix}

\bigg ) 


= 

\begin{bmatrix}
c_{1} \\
c_{2} \\
c_{3} \\
\end{bmatrix}
$$

$$
c_1 = -p_{1,1} log(q_{1,1}) - p_{1,2} log(q_{1,2}) 
$$

$$
c_2 = -p_{2,1} log(q_{2,1}) - p_{2,2} log(q_{2,2})
$$


$$
\text{ mini-batch 的总损失 } \\
L = \frac{1}{2} (c_1 + c_2)
$$

$$
\frac{ \partial }{ \partial w_{1,1} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{1,1} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{1,1} } \\


+ \frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial w_{1,1} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial w_{1,1} }
$$



$$
\frac{ \partial }{ \partial w_{2,1} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{2,1} }

+

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{2,1} } \\



+ \frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial w_{2,1} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial w_{2,1} }
$$

$$
\frac{ \partial }{ \partial w_{1,2} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial w_{1,2} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial w_{1,2} } \\


+ \frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial w_{1,2} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial w_{1,2} }
$$

$$
\frac{ \partial }{ \partial w_{2,2} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial w_{2,2} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial w_{2,2} } \\


+ \frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial w_{2,2} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial w_{2,2} }
$$



$$
\frac{ \partial }{ \partial b_{1,1} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial b_{1,1} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial b_{1,1} } \\
$$

$$
\frac{ \partial }{ \partial b_{1,2} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial b_{1,2} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,2} }

\frac{ \partial a_{1,2}}{ \partial b_{1,2} } \\
$$

$$
\frac{ \partial }{ \partial b_{2,1} } L = 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial b_{2,1} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,1} }

\frac{ \partial a_{2,1}}{ \partial b_{2,1} } \\
$$

$$
\frac{ \partial }{ \partial b_{2,2} } L = 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial b_{2,2} }

+ 

\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,2} }

\frac{ \partial a_{2,2}}{ \partial b_{2,2} } \\
$$




$$
\frac{ \partial }{ \partial w_{1,1} } L = - \frac{1}{2} p_{1,1}(1 - q_{1,1}) x_{1,1} + \frac{1}{2} p_{1,2} q_{1,1} x_{1,1} \\ 

- \frac{1}{2} p_{2,1} (1 - q_{2,1}) x_{2,1} + \frac{1}{2} p_{2,2} q_{2,1} x_{2,1}
$$



$$
\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,1} } = \frac{1}{2} (-p_{1,1} \frac{1}{q_{1,1}} ) q_{1,1} (1 - q_{1,1}) \\ 

= - \frac{1}{2} p_{1,1}(1 - q_{1,1})
$$

$$
\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,1} } = \frac{1}{2} (- p_{1,2} \frac{1}{q_{1,2}}) (-q_{1,1} q_{1,2}) \\

= \frac{1}{2} p_{1,2} q_{1,1}
$$

$$
\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,1} }

\frac{ \partial q_{2,1}}{ \partial a_{2,1} }
 = 
 
 \frac{1}{2} (-p_{2,1} \frac{1}{q_{2,1}}) q_{2,1} (1 - q_{2,1}) \\
 = - \frac{1}{2} p_{2,1} (1 - q_{2,1})
$$

$$
\frac{ \partial L}{ \partial c_2 }

\frac{ \partial c_2}{ \partial q_{2,2} }

\frac{ \partial q_{2,2}}{ \partial a_{2,1} } =  \frac{1}{2} (- p_{2,2} \frac{1}{q_{2,2}}) (- q_{2,2} q_{2,1}) \\

= \frac{1}{2} p_{2,2} q_{2,1}
$$
















```
# https://zhuanlan.zhihu.com/p/352215536
	绝对不会出 bug 的矩阵求导——定义，推导，动机；非交换链式法则
```


$$
a_{1,1} = x_{1,1} w_{1,1} + x_{1,2} w_{2,1} + b_{1,1} \\

a_{1,2} = x_{1,1} w_{1,2} + x_{1,2} w_{2,2} + b_{1,2}
$$

$$
a_{2,1} = x_{2,1} w_{1,1} + x_{2,2} w_{2,1} + b_{2,1} \\

a_{2,2} = x_{2,1} w_{1,2} + x_{2,2} w_{2,2} + b_{2,2}
$$

$$
q_{1,1} = \frac{e^{a_{1,1}}}{e^{a_{1,1}} + e^{a_{1,2}} } \\

q_{1,2} = \frac{e^{a_{1,2}}}{e^{a_{1,1}} + e^{a_{1,2}} }
$$

$$
q_{2,1} = \frac{e^{a_{2,1}}}{e^{a_{2,1}} + e^{a_{2,2}} } \\

q_{2,2} = \frac{e^{a_{2,2}}}{e^{a_{2,1}} + e^{a_{2,2}} }
$$

$$
c_1 = -p_{1,1} log(q_{1,1}) - p_{1,2} log(q_{1,2})
$$

$$
c_2 = -p_{2,1} log(q_{2,1}) - p_{2,2} log(q_{2,2})
$$

$$
\text{ mini-batch 的总损失 } \\
L = \frac{1}{2} (c_1 + c_2)
$$

$$
\frac{ \partial }{ \partial w_{1,1} } L = 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,1} }

\frac{ \partial q_{1,1}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{1,1} }

+ 

\frac{ \partial L}{ \partial c_1 }

\frac{ \partial c_1}{ \partial q_{1,2} }

\frac{ \partial q_{1,2}}{ \partial a_{1,1} }

\frac{ \partial a_{1,1}}{ \partial w_{1,1} }
$$

