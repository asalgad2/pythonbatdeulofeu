from time import time
print('Calcula el temps que trigues a escriure una paraula')
t1=time()
paraula=input('Escriu una paraula i prem intro :')
t2=time()
temps=t2-t1
print('Has trigat ',temps,'segons')
