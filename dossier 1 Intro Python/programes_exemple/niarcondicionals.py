print('Aquest programa comptarà els caràcters del teu nom ')
nom=input('Siusplau, escriu el teu nom : ')
longitud=len(nom)
print('Hola',nom,'encantat de saludar-te')

if longitud<=7:
    print('El teu nom té',longitud,'caràcters')
else:
    print('Tens un nom llarg')
    if ' ' in nom:
        print('A més, tens un nom compost')
    else:
        print('A més, no és un nom compost')