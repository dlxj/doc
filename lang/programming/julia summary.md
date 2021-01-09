 

清晰、全 [u](https://juliadocs.github.io/Julia-Cheat-Sheet/zh-cn/)

wikibook [u](https://zh.m.wikibooks.org/zh-hans/Introducing_Julia/Arrays_and_tuples)

 [u](https://julialang.org/blog/2017/01/moredots/)

[u](https://julialang.org/blog/2017/01/moredots/) dot "**.**" 运算符和**向量化**有关 vectorized

[u](https://docs.julialang.org/en/v1/base/math/#Base.:\-Tuple{Any,Any}) 所有算符文档



**高斯求积简介** [u](https://discourse.juliacn.com/t/topic/1024) [u2](GitHub\doc\lang\programming\高斯求积简介.pdf)





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





Julia中，定义 A × B = C 则 A \ C = B （ \ 为**矩阵左除**运算符，A \ B = inv(A) * B）

Julia还有一个矩阵的右除运算符（/，就是标准的除法，A / B = A * inv(B) )

共轭转置, M' 或 adjoint(M)

- 先对矩阵的每一个元素取复共轭。 复共轭是虚部取负数

- 再转置



```julia
区间是可以迭代的，直接用就好

julia> map(x->2x,1:3)
3-element Array{Int64,1}:
 2
 4
 6

julia> collect(range(1;stop=2,length=10))
10-element Array{Float64,1}:
 1.0               
 1.1111111111111112
 1.2222222222222223
 1.3333333333333333
 1.4444444444444444
 1.5555555555555556
 1.6666666666666667
 1.7777777777777777
 1.8888888888888888
 2.0
```



```julia
julia> V(x) = [x[j]^(i-1) for i in eachindex(x), j in eachindex(x)]
V (generic function with 1 method)

julia> x = range(-1, stop=1, length=4)
-1.0:0.6666666666666666:1.0

julia> w = V(x)\[2, 0, 2/3, 0]
4-element Array{Float64,1}:
 0.24999999999999978
 0.7500000000000002
 0.7500000000000002
 0.24999999999999983

julia> f(x) = 1+15x+2x^2+12x^3
f (generic function with 1 method)

julia> w'f.(x)
3.333333333333334
```







数组的索引从1 开始

collect(**eachindex**(x))

