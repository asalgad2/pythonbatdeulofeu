paraula=input('Escriu una paraula, que safegirà a una llista :')
llista=[]
seguir=True
while seguir:
    paraula=input('Escriu una paraula, que safegirà a una llista :')
    llista.append(paraula)
    if paraula =='':
        print(llista)
        seguir=False
