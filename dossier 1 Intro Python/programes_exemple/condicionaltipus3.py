print('Aquest programa dirà si és divisible per 2')
print('Sinò mirarà si ho és per 3')
print('I sinò comprovarà si ho és per 5')
nombre=input('Escriu un nombre :')
nombre=eval(nombre)
if nombre%2==0:
        div2=nombre/2
        print('El nombre',nombre,'és divisible per 2.')
        print('El resultat és',div2)
elif nombre%3==0:
        div3=nombre/3
        print('El nombre',nombre,'és divisible per 3.')
        print('El resultat és',div3)
elif nombre%5==0:
        div5=nombre/5
        print('El nombre',nombre,'és divisible per 5.')
        print('El resultat és',div5)
else:
        print('El nombre no és múltiple de 2,3 i 5')