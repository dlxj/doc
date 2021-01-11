
using SymPy
x = symbols("x")
println( integrate(sin(x)/x, (x, -oo, oo)) )
println( integrate(1+15*x+2*x^2+12*x^3, (x, -1.0, 1.0)) )

x = range(-1, stop=1, length=4) # 均匀取值
#=
julia> x = range(-1, stop=1, length=4)
-1.0:0.6666666666666666:1.0

julia> collect(x)
4-element Array{Float64,1}:
 -1.0
 -0.3333333333333333
  0.3333333333333333
  1.0
=#

#=
julia> b = [ [i,j] for i in eachindex(a), j in eachindex(a) ]
3×3 Array{Array{Int64,1},2}:
 [1, 1]  [1, 2]  [1, 3]
 [2, 1]  [2, 2]  [2, 3]
 [3, 1]  [3, 2]  [3, 3]
=#

V(x) = [x[j]^(i-1) for i in eachindex(x), j in eachindex(x)] # julia 的下标从1 开始
#=
x1^0, x1^1, x1^2, x1^3
x2^0, x2^1, x2^2, x2^3
x3^0, x3^1, x3^2, x3^3
x4^0, x4^1, x4^2, x4^3
=#

w = V(x)\[2, 0, 2/3, 0]
f(x) = 1+15x+2x^2+12x^3
println( w'f.(x) ) # 根据积分的近似公式算的， W  点乘 f(X) ，既权重与函数采样值的线性组合
#=
Julia中，定义 A × B = C 则 A \ C = B （ \ 为矩阵左除运算符，A \ B = inv(A) * B）
Julia还有一个矩阵的右除运算符（/，就是标准的除法，A / B = A * inv(B) )

四个方程，四个未知数(W)
(4*4) x (4,) -> (4,)
A x W = [2, 0, 2/3, 0]
    所以 W = A \ [2, 0, 2/3, 0]
=#

#=
共轭转置, M' 或 adjoint(M)
    - 先对矩阵的每一个元素取复共轭。 复共轭是虚部取负数
    - 再转置
W'：(4,) -> (1,4)
X:  (4,)
f.(X)：(4,)  # f. 是向量化的意思，因为参数X 不是标量
W'f.(X)：(1,4) x (4,) -> (1,)
=#

println("hi,,,")
