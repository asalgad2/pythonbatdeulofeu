print('Programa per saber si un nombre és múltiple de 3')
nombre=input('Escriu un nombre :')
nombre=eval(nombre)
if nombre%3==0 :
        print('És múltiple de 3!')
        div = nombre/3
        print('El resultat de',nombre,'dividit entre 3 és',div)
else :
        print('El nombre no és múltiple de 3!')