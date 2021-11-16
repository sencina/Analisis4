import math


def taylor(x0,y0,b,n):

    h = (b-x0)/n
    x = x0
    y = y0
    k = 0

    while k<=n:

        print(k, x, y)
        yp = math.cos(x) - math.sin(y)+x**2
        ys = -math.sin(x) - math.cos(y) * yp + 2*x
        yt = -math.cos(x) - ys*math.cos(y) + (yp**2)*math.sin(y) + 2
        yc = math.sin(x) + (yp**3-yt)*math.cos(y)+3*yp*ys*math.sin(y)

        y = y + h*(yp+(h/2)*(ys+(h/3)*(yt+(h/4)*yc)))
        x = x + h
        k =k+1

def euler(f,x0,y0,b,n):

    h = (b-x0)/n
    for i in range(n):
        y1 = y0 + h*f(x0,y0)
        x0 = x0 + h
        y0 = y1

    return [x0,y0]

def eulerModificado(f,x0,y0,b,n):
    h = (b-x0)/n
    for i in range(n):
        F1 = h*f(x0,y0)
        F2 = h*f(x0+1/2*h,y0+1/2*F1)
        y1 = y0+F2
        x0 = x0+h
        y0 = y1
    return [x0,y0]

def eulerMejorado(f,x0,y0,b,n):
    h = (b - x0) / n
    for i in range(n):
        F1 = h*f(x0,y0)
        F2 = h*f(x0+h,y0+F1)
        y1 = y0+1/2*(F1+F2)
        x0=x0+h
        y0=y1
    return [x0,y0]

def rungeKutta(f,x0,y0,b,n):
    h = (b - x0) / n
    for i in range(n):
        F1 = h*f(x0,y0)
        F2 = h*f(x0+1/2*h,y0+1/2*F1)
        F3 = h*f(x0+1/2*h,y0+1/2*F2)
        F4 = h*f(x0+h,y0+F3)

        y1 = y0+1/6*(F1 + 2*F2+2*F3+F4)
        y0 = y1
        x0 = x0 + h
    return [x0,y0]

def eulerModificado2(f, g, x0, y0, z0, b, n): #sistemas
    h = (b - x0) / n
    for i in range(n):
        F1 = h*f(x0,y0,z0)
        G1 = h*g(x0,y0,z0)
        F2 = h*f(x0+1/2*h,y0+1/2*F1,z0+1/2*G1)
        G2 = h*g(x0+1/2*h,y0+1/2*F1,z0+1/2*G1)
        y1 = y0+F2
        z1 = z0 + G2
        x0 = x0 + h
        y0 = y1
        z0 = z1
    return [x0,y0,z0]

def eulerMejorado2(f, g, x0, y0, z0, b, n): #sistemas
    h = (b - x0) / n
    for i in range(n):
        F1 = h*f(x0,y0,z0)
        G1 = h*g(x0,y0,z0)
        F2 = h*f(x0+h,y0+F1,z0+G1)
        G2 = h*g(x0+h,y0+F1,z0+G1)
        y1 = y0+(1/2)*(F1+F2)
        z1 = z0 + (G1+G2)/2
        x0 = x0 + h
        y0 = y1
        z0 = z1
    return [x0,y0,z0]

def f(x,y,z):
    return z
def g(x,y,z):
    return x+2*y+z

x0 = 0
y0 = 2
z0 = 1
b = 1
n = 2

print(eulerMejorado2(f,g,x0,y0,z0,b,n))