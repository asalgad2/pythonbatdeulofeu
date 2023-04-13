lletra=input('Entra una lletra: ')
frase=input('Entra una frase: ')
comptador=0
for n in range(0,len(frase)):
    if frase[n]==lletra:
        comptador=comptador+1
print(lletra,'apareix',comptador,' vegades')