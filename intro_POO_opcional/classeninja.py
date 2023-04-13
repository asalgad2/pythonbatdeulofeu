class NinjaPrincipal:
    hp = 100
    resistencia = 50
    xp = 1

    def game_over(self):
        print('Game over')


ninja = NinjaPrincipal()

print(ninja.hp)

ninja.hp = 0

if ninja.hp == 0:
    ninja.game_over()