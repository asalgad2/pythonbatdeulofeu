'''Calcula la quant hem de pagar per un regal comú!'''
'''Posant try simplement ens informa dun error,però no atura l'execució'''
try:
    preu=int(input('Quant val el regal?'))
except ValueError:
    print('No és un nombre')

assistents=int(input('Quants assistents a la festa?'))

a_pagar=preu/assistents

print('Us toca pagar ', a_pagar, 'euros')