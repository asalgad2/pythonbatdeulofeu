import random
print('Programa per generar nombres aleatoris')
v1=random.random()
print('Valor aleatori entre 0 i 1: ',v1)
v2=random.randint(1,100)
print('Valor enter entre 1 i 100',v2)
v3=random.uniform(10,20)
print('Valor decimal entre 10 i 20',v3)
noms=['Joan','Pere','Enric','Aniol','David','Maria','Helga']
nom=random.choice(noms)
print('El nom escollit és',nom)