print('Programa per comprovar si un nombre és divisible per 2,3,5,7 i 11')
nombre=eval(input('Escriu un nombre :'))

if nombre%2 ==0 :
    print('El nombre',nombre,'sí és divisible per 2')
else:
    print('El nombre',nombre,'no és divisible per 2')

if nombre%3 ==0 :
    print('El nombre',nombre,'sí és divisible per 3')
else:
    print('El nombre',nombre,'no és divisible per 3')

if nombre%5 ==0 :
    print('El nombre',nombre,'sí és divisible per 5')
else:
    print('El nombre',nombre,'no és divisible per 5')
    
if nombre%7 ==0 :
    print('El nombre',nombre,'sí és divisible per 7')
else:
    print('El nombre',nombre,'no és divisible per 7')
    
if nombre%11 ==0 :
    print('El nombre',nombre,'sí és divisible per 11')
else:
    print('El nombre',nombre,'no és divisible per 11')