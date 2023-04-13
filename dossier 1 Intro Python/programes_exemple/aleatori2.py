from random import randint
print('Programa que generarà nombres aleatoris')
print('entre 0 i 10 fins que surti el 10')
n=0
while n!=10:
    n=randint(1,10)
    print('Ha sortit el ',n)