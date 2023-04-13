from random import randint
from time import sleep

print('Programa que genera 10 nombres aleatoris')
for n in range(10):
    nombre=randint(1,100)
    print(n+1, 'Nombre generat:',nombre)
    sleep(1)