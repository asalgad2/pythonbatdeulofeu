print('Escriu nombres parells')
print('Si escrius un nombre imparell el programa acabarà')
seguir=True
while seguir:
    nombre=input('Escriu un nombre:')
    nombre=eval(nombre)
    if nombre%2==1:
        print('Nombre imparell!!')
        seguir=False