
# import sympy


from sympy import  integrate ,cos,sin
from sympy.abc import  a,x,y

print( integrate(sin(x)/x,(x,-float("inf"),float("inf"))) )

print( integrate(1+15*x+2*x**2+12*x**3,(x,float(-1),float(1))) )


print("hi,,,")
