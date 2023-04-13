print('Aquest programa demana nombres fins que contestis en blanc')
print('Compta quants nombres shan introduït')
print('i la seva suma')
n=0
suma=0
seguir=True
while seguir:
    nombre=input('Escriu un nombre: ')
    if nombre=='':
        seguir=False
    else:
        nombre=eval(nombre)
        n=n+1
        suma=suma+nombre

print('Shan introduït',n,'nombres')
print('Els nombres sumen',suma)