import math
print('Aquest programa calcula mcd i mcm de dos nombres')
n1=eval(input('Escriu el nombre 1:'))
n2=eval(input('Escriu el nombre 2:'))
mcd=math.gcd(n1,n2)
mcm=(n1*n2)/mcd
print('El màxim comú divisor és :',mcd)
print('El mínim comú múltiple és :',mcm)