import sympy as sym
help(sym.sin)
sym.sin? # in Ipython

############################################################
sym.init_printing() #pretty printing, use best available

#also latex , how check later?
str(sym1)
#####
sym.pretty(sym1,use_unicode=False) # return pretty string # True for a better by using Unicode
sym.pprint(sym1,use_unicode=False) # print pretty string # print(sym.pretty())
sym.latex(sym1) # return string form in latex
############################################################
# 0.1. algebraic arithmatics
a=sym.Symbol('a',positive=True) #negative=True 
a,b,c = sym.symbols('a b c')
eta , xi , sigma
sym.sympify('x**2-3*x+cos(x)') # returns the sym1
from sympy import oo , pi ,E as e, I # don't change their values later or redefine the symbols
#from sympy.abc import x,y,z
+ - * / **
g = x**3 - 2*x**2 + 3*x + 4

#####
# 0.2. algebraic arithmatic special functions
sqrt , root(sym1,n)
exp , log(x,n=e) , LambertW, pow , expj
sin , cos , tan
sinh , cosh , tanh
asin, acos , atan

factorial
binomial(n,k)
gamma
f = sym.cos(x)**2 + sym.sin(x) + x**3 - 2*y*x
#####
# 0.3. general functions
#https://docs.sympy.org/latest/modules/functions/index.html
sym.Piecewise( (expr,cond) , (expr,cond) , ..) #the first place it's true, nan if all false
sym.Piecewise( (0 , x<-1) , (f,x<=1) , (g,True) )

sym.Min
sym.Max
sym.Abs
re
im
sign
arge
conjugate

Heaviside
DiracDelta

x = Symbol('x')
sym.Function('f')(x)

#####
EmptySet
#S.Reals #S.Naturals #Naturals0 , Integers
Interval(a,b,True,False)
##### to numeric
subs/evalf 	50us 	Simple 	None
lambdify 	1us 	Scalar functions 	math
lambdify-numpy 	10ns 	Vector functions 	numpy
ufuncify 	10ns 	Complex vector expressions 	f2py, Cython
Theano 	10ns 	Many outputs, CSE, GPUs 	Theano
###
sym1.subs(x,x*y)
sym1.subs(x,2)
sym1.subs( [(x,2) , (y,3) ] )

sym1.evalf(N) make a numeric approximation with .fN precision
sym1.evalf(N,subs={x:2.4})

f= sym.lambdify(x,sym1,'numpy')
a=np.arange(1,10,0.01)
f(a) # return the np.ndarray # it's fast
Eq(f,2) or f-2

from  sympy.utilities.autowrap import ufuncify
g = ufuncify([x],f)


ufuncify is better than lambdify for larger than 1 s; do to its compile overhead
############################################################
# 1.1
sym1.simplify()
sym1.expand()
sym1.factor()
sym.factor_list(expr)
sym1.collect(x)
sym1.coeff(x,2)
sym1.cancel()
sym1.apart() # tajziye kasr ha
# 1.2
sym1.trigsimp()
sym1.rewrite(sin) # tan(x).rewrite(sin) , foctorial(x).rewrite(gamma)
######
# 2.1
sym1.series(x,x0,n)
sym1.removeO()
###########################################################
# 3.1 # 3.2
sym.solveset(f,x,domain=sym.S.Complexes) 
sym.solveset(f<0,domain=sym.S.Reals)
sym.roots(f,x) # multiple roots not only once {0:1 , 3:2} 0 order 1 and 3 order 2
sym.solve(f)

sym.nsolve(f,x0)
#####
# 4.1
#use limit instead of subs when necessary
sym.limit(f,x,x0)
sym.limit(f,x,x0,'+') # or '-'
sym.Limit(f,x,x0)
#####
sym.singularities(f,x)
#####
is_monotonic
is_increasing
is_decreasing
is_strictly_increasing
is_strictly_decreasing

#####
# 4.2 #4.3
sym1.diff(x,y,z,z)
sym.diff(f,x,y,z,z)
sym1.diff( (x,n) ) # unspecified n is sym or int. float?
sym.Derivative(f,x,y,z) # unevaluated , later can be by:
sym1.doit()
sym.hessian(f,(x,y))
#####
sym.integrate(f,x) # indefinite
sym.integrate(f , (x,0,oo))
sym.integrate(f , (x,-oo,oo) , (y,0,5)) # dx dy # first x then y
sym.Integral(f,x)
#if unable to solve, returns an Integral obj to sym1.doit() later

####
numerical integral??

#####
f , g = symbols('f g',cls=sym.Function) # unevaluated function variable
f(x)
f(x).diff(x)

diffeq = Eq( f(x).diff(x,x) -2*f(x).diff(x) + f(x) , sin(x) )

sym.dsolve(diffeq, f(x) )


#####
# linalg
Matrix( t of l)
eye
zeros

v1.dot(v2)
v1.cross(v2)

f = lambda x: 2*x
eye(3).applyfunc(f)


M.det()
M.inv()
M.norm()
M.T
M.conjugate()
M.eigenvals()
M.eigenvects

###############
sym.plot(f,x)
sym.plot(f , (x,a,b) ) 
