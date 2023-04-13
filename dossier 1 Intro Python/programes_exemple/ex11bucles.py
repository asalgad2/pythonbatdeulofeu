nombre=input('Escriu un nombre :')
comptador=0
suma=0
mitjana=0
while nombre!='':
    numero=eval(nombre)
    comptador=comptador+1
    suma=suma+numero
    nombre=input('Escriu un nombre :')
    
mitjana=suma/comptador
print('nombres entrats :', comptador)
print('mitjana :', mitjana)
print('suma :', suma)
    