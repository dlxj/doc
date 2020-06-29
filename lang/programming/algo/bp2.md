


$$
X = 
\begin{bmatrix}
x^{1}_{1} & x^{1}_{2} & \cdots & x^{1}_{n}  \\
x^{2}_{1} & x^{2}_{2} & \cdots & x^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
x^{m}_{1} & x^{m}_{2} & \cdots & x^{m}_{n} \\
\end{bmatrix}
$$

$$
W = 
\begin{bmatrix}
w^{1}_{1} & w^{1}_{2} & \cdots & w^{1}_{n}  \\
w^{2}_{1} & w^{2}_{2} & \cdots & w^{2}_{n} \\
\vdots & \vdots & \ddots & \vdots & \\
w^{n}_{1} & w^{n}_{2} & \cdots & w^{n}_{n} \\
\end{bmatrix}
$$

$$
V = 
\begin{bmatrix}
v^{1} \\
v^{2} \\
\vdots    \\
v^{n} \\
\end{bmatrix}
$$

$$
X \cdot W = 
\begin{bmatrix}
x^{(1)} \cdot w_{(1)} & x^{(1)} \cdot w_{(2)} & \cdots & x^{(1)} \cdot w_{(n)}  \\
x^{(2)} \cdot w_{(1)} & x^{(2)} \cdot w_{(2)} & \cdots & x^{(2)} \cdot w_{(n)}  \\
\vdots & \vdots & \ddots & \vdots & \\
x^{(m)} \cdot w_{(1)} & x^{(m)} \cdot w_{(2)} & \cdots & x^{(m)} \cdot w_{(n)}  \\
\end{bmatrix}
$$




$$
(X \cdot W) \cdot V =
\begin{bmatrix}
x^{(1)} \cdot w_{(1)} & x^{(1)} \cdot w_{(2)} & \cdots & x^{(1)} \cdot w_{(n)}  \\
x^{(2)} \cdot w_{(1)} & x^{(2)} \cdot w_{(2)} & \cdots & x^{(2)} \cdot w_{(n)}  \\
\vdots & \vdots & \ddots & \vdots & \\
x^{(m)} \cdot w_{(1)} & x^{(m)} \cdot w_{(2)} & \cdots & x^{(m)} \cdot w_{(n)}  \\
\end{bmatrix}
\cdot
\begin{bmatrix}
v^{1} \\
v^{2} \\
\vdots    \\
v^{n} \\
\end{bmatrix}
\\
= 
\begin{bmatrix}
v^{1} x^{(1)} \cdot w_{(1)} & v^{2} x^{(1)} \cdot w_{(2)} & \cdots & v^{n} x^{(1)} \cdot w_{(n)}  \\
v^{1} x^{(2)} \cdot w_{(1)} & v^{2} x^{(2)} \cdot w_{(2)} & \cdots & v^{n} x^{(2)} \cdot w_{(n)}  \\
\vdots & \vdots & \ddots & \vdots & \\
v^{1} x^{(m)} \cdot w_{(1)} & v^{2} x^{(m)} \cdot w_{(2)} & \cdots & v^{n} x^{(m)} \cdot w_{(n)}  \\
\end{bmatrix}
$$









$$
u(W) = X \cdot W  \\

z(V) = u(W) \cdot V \\
$$

$$
E(W,V,Y) = z(V) - Y
$$



  































