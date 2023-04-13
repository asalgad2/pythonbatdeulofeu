import os
print(os.getcwd())

'''Llegir un arxiu de text'''

arxiu = open('helloworld.txt','rt')
salutacio=arxiu.read()
print(salutacio)
arxiu.close()