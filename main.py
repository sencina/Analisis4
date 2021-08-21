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

def newtonRaphson(f,a,b,cota):
    return 1


f = lambda x: math.pow(x, 3) - 3

cotaInf = 1
cotaSup = 2

print(biseccion(f, cotaInf, cotaSup, pow(10, -15)))

print(f(cotaInf))
print(f(cotaSup))
