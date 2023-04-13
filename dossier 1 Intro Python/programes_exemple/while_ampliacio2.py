password = 'deulofeu'
contrassenya = ''
comptador=0
while contrassenya != password and comptador<3:
    contrassenya = input('Entra la contrassenya : ')
    comptador=comptador+1
    if password==contrassenya:
        print('Correcte!')
    else:
        print('Incorrecte')
    if comptador==3:
        print("T'has quedat sense intents!")
