import math

def print_row(lst):
    print(' '.join('%11.8f' % x for x in lst))

def romberg(f, a, b, r):
    R = [[0.5 * (b - a) * (f(a) + f(b))]]
    print_row(R[0])
    n = 1
    i = 0
    while True:
        i += 1
        h = float(b-a)/2**n
        R.append((n+1)*[None])
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1))
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print_row(R[n])
        if i>=r:
            return R[n][n]
        n += 1


#%%

f = f = lambda x: math.sqrt(1+math.cos(x))-1+math.pow(math.sin(x),2)
a = 0
b = math.pi/2
print(romberg(f, a, b, 2))
