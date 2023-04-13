print('Programa que analitza una paraula')
paraula=input('Escriu una paraula :')
longitud = len(paraula)

if longitud<=5:
    print('La paraula',paraula,'té',longitud,'lletres')
    primera=paraula[0]
    ultima=paraula[longitud-1]
    print('La primera lletra és',primera)
    print('La última lletra és',ultima)
    
if longitud>5:
    print('La paraula',paraula,'té',longitud,'lletres')
    qprimeres=paraula[0:4]
    qultimes=paraula[longitud-4:longitud]
    print('Les quatre primeres són',qprimeres)
    print('La quatre últimes són',qultimes)
    