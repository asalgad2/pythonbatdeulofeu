print('Aquest programa lletreja una paraula')
print('escriu els seus caràcters i el valor unicode')
paraula=input('Escriu una paraula :')
for c in paraula:
    print(c,'valor unicode',ord(c),'\n')