seguir=True
minim=eval(input('Digues el mínim : '))
maxim=eval(input('Digues el màxim : '))
while seguir==True:
    
    num=eval(input('Digues el nombre : '))
    if minim<=num and maxim>=num:
        seguir=True
        print('Correcte')
    else:
        seguir=False
        print('Incorrecte')