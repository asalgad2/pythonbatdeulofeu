# Es crea la classe.
class NinjaPrincipal:
	HP = 100
	resistencia = 50
	XP = 1

	def game_over(self):
		print('Game over')

# Es crea l'objecte ninja a partir de la classe.
ninja = NinjaPrincipal()

# Es crea l'objecte ninja_enemic a partir de la classe NinjaPrincipal.
ninja_enemic = NinjaPrincipal()

# Se li assigna un valor diferent del valor por defecte a l'atribut HP.
ninja_enemic.HP = 25
ninja_enemic.resistencia = 10
ninja_enemic.XP = 1
print(ninja_enemic.HP, ninja_enemic.resistencia, ninja_enemic.XP)