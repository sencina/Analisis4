import math


def trapecios(f, a, b, n):

    h = (b - a) / (n)
    suma=0
    i=1
    while i<n:
        suma+=f(a+i*h)
        i+=1

    return h/2*(f(a)+f(b)+2*suma)

def nCalculator(h,a,b):
    return (b-a)/h

#%%
f = lambda x: math.sqrt(1+math.cos(x))-1+math.pow(math.sin(x),2)

h = math.pi/8
a = 0
b = math.pi/2

print(trapecios(f,a,b,nCalculator(h,a,b)))