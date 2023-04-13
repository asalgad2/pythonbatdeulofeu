numero=eval(input('Escriu un nombre :'))
compt=0
for n in range (1,numero):
    if numero%n==0:
        compt=compt+1
        print('comptador :',compt)
        print('divisor :',n)