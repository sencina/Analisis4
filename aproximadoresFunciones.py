def S(c, k):
    s = 0
    for i in range(k):
        p = 1
        for j in range(i):
            p *= x[k] - x[j]
        s += c[i] * p
    return s


def Q(k):
    p = 1
    for j in range(k):
        p *= x[k] - x[j]
    return p


def newton_interpol(x, y):
    coefs = [y[0]]
    n = len(x)
    for k in range(1, n):
        ck = (y[k] - S(coefs, k)) / Q(k)
        coefs.append(ck)

    pol_str = ""
    for i in range(n):
        pol_str += str(coefs[i])
        for j in range(i):
            pol_str += "*(x - %s)" % x[j]
        if i != n - 1:
            pol_str += "+"
    print(pol_str)

    pol = lambda x: eval(pol_str, {'x': x})
    return pol

def lagrange_interpol(x,y,z):
    n = len(x)
    p=0
    l=0
    for i in range(n):
        l=1
        for j in range(n):
            if (j != i):
                l = l*(z-x[j])/(x[i]-x[j])
        p=p+l*y[i]
    return p;


x=[1,2,3,4]
y=[2.1,2.5,3,2.8]

pol = newton_interpol(x, y)

print(pol(5))
