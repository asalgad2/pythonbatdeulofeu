ant=0
seguir=True
while seguir==True:
    num=eval(input('Entra un nombre :'))
    
    if ant<num:
        print('Correcte')
        ant=num
        seguir=True
    else:
        seguir=False
    
print("T'has equivocat")