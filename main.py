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


f= lambda x: pow(x,4)-2*pow(x,3)-4*pow(x,2)+4*x+4

cotaInf = -2
cotaSup = 0

print(biseccion(f,cotaInf,cotaSup,pow(10,-10)))

print(f(cotaInf))
print(f(cotaSup))

