import numpy
from sympy import Symbol, Eq,sqrt,solve
x = Symbol('x')
vector=numpy.array([1, 1, 1])
vector=vector*x
for i in range(0,len(vector)):
    vector[i]=vector[i]*vector[i]
value=sqrt(sum(vector))
eqn=Eq(pow(value,2), 1)
sol=solve(eqn)
print(sol)


