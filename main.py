import math


def biseccion(f, a, b, cota):
    error = cota + 1
    p_ant = a

    while error > cota:
        p = (a + b) / 2.0
        error = abs(p - p_ant)
        p_ant = p

        if f(a) * f(p) > 0:
            a = p
        elif f(b) * f(p) > 0:
            b = p
        else:
            return p
    return p

def newtonRaphson(f,fprima,a,cota):
    error = cota +1
    xk = a
    while error > cota:
        xk2 = xk-f(xk)/fprima(xk)
        error = abs(xk2-xk)
        xk = xk2
    return xk



f = lambda x: x-1-0.5*math.sin(x)
fprima = lambda x: 1-0.5*math.cos(x)


print("newtonRaphson = "+ str(newtonRaphson(f, fprima,2, pow(10, -4))))

