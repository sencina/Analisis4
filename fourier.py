import math

listaY = [1.0004, -0.119, 1.5987, 0.2115, -0.6567, -0.3514, -1.6824]
listaX = [0,0.897597901,1.795195802,2.692793703,3.590391604,4.487989505,5.385587406]

def a0(listaY):
      length = len(listaY)
      suma = 0

      for i in range(length):
            suma = suma + listaY[i]

      return suma*(1/length)

def ak(listaX,listaY,k):
      length = len(listaY)
      suma = 0

      for i in range(length):
            suma = suma +listaY[i]*math.cos(k*listaX[i])

      suma = (2/length) * suma

      return suma


def bk(listaX,listaY, k):
      length = len(listaY)
      suma = 0

      for i in range(length):
            suma = suma + listaY[i] * math.sin(k*listaX[i])

      suma = (2 / length) * suma

      return suma


print(a0(listaY))
print(ak(listaX,listaY,1))
print(bk(listaX,listaY,1))