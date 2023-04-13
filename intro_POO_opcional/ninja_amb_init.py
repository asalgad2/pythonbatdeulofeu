class Ninjas:
	def __init__(self, hp, resistencia, xp, vides):
 		self.hp = hp
		self.resistencia = resistencia
		self.xp = xp
		self.vides = vides
	def game_over(self):
		print('Game over')
#Creació dels ninjas
		       #Ninjas(hp,resistencia,xp,vides)
ninja_jugador = Ninjas(100, 50, 1, 3)
ninja_vermell = Ninjas(40,50,1,1)
ninja_groc = Ninjas(50,10,3,1)
ninja_blau = Ninjas (40,10,1,1,)


