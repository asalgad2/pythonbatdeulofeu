gots=eval(input('Quants gots té la comanda : '))
coberts=eval(input('Quants coberts té la comanda : '))
pes_total=gots*30+coberts*5
preu_a_pagar=int((pes_total)/100)*0.025
print('La comanda té un pes de ',pes_total,'grams i un import de ',preu_a_pagar,'euros')