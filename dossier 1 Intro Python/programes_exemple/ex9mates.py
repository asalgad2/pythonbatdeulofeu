import random
for n in range(1,16):
    possible_resultat=['1','X','2']
    resultat=random.choice(possible_resultat)
    print('Partit',n,' : ' ,resultat)