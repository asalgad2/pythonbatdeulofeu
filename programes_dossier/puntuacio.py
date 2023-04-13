import pygame
import random

#Mida de pantalla
AMPLADA = 800
ALÇADA = 600

#FPS
FPS = 30

# Paleta de colorss
NEGRE = (0,0,0)
BLANC = (255,255,255)
VERMELL = (255,0,0)
H_FA2F2F = (250,47,47)
VERD= (0,255,0)
BLAU = (0,0,255)
BLAU2 = (64,64,255)
H_50D2FE = (94,210,254)

puntuacio=0

#definició de fonts
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

def mostra_text(pantalla,font,text,color, dimensions, x, y):
	tipus_lletra = pygame.font.Font(font,dimensions)
	superficie = tipus_lletra.render(text,True, color)
	rectangle = superficie.get_rect()
	rectangle.center = (x, y)
	pantalla.blit(superficie,rectangle)

class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heretem l' init de la classe Sprite de Pygame
        super().__init__()
        # Imatge del sprite(nau)
        self.image = pygame.image.load("nau.png").convert()
        # Obtenim el rectangle (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectangle en pantalla (sprite)
        self.rect.center = (AMPLADA // 2, ALÇADA // 2)
        #Velocitats del personatge inicialment
        self.velocitat_x = 0
        self.velocitat_y = 0
    def disparem(self):
        bala = Projectils(self.rect.centerx, self.rect.top)
        bales.add(bala)

    def update(self):
        # Actualitza això a cada volta del bucle.
        #Velocitats a cada iteració del bucle
        self.velocitat_x = 0
        self.velocitat_y = 0
        #Quina tecla es prem?
        tecla = pygame.key.get_pressed()
        
        # Mou a esquerra
        if tecla[pygame.K_a]:
            self.velocitat_x = -10
        # Mou a dreta
        if tecla[pygame.K_d]:
            self.velocitat_x = 10
        # Mou a dalt
        if tecla[pygame.K_w]:
            self.velocitat_y = -10
        # Mou a dreta
        if tecla[pygame.K_s]:
            self.velocitat_y = 10
        if tecla[pygame.K_SPACE]:
            self.disparem()
        #Actualitza la velocitat x i y del personatge
        self.rect.x += self.velocitat_x
        self.rect.y += self.velocitat_y
        #Limita els marges
            # Marge inferior
        if self.rect.bottom > ALÇADA:
            self.rect.bottom = ALÇADA
            # Marge superior
        if self.rect.top < 0:
            self.rect.top = 0
            # Marge dret
        if self.rect.right > AMPLADA:
            self.rect.right = AMPLADA
            # Marge esquerre
        if self.rect.left < 0:
            self.rect.left = 0
       
class EnemicsGrocs(pygame.sprite.Sprite):
# Sprite del enemigo
    def __init__(self):
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("enemigo1.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius=48
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.rect.y = random.randrange(ALÇADA - self.rect.height)
        self.velocitat_x = random.randrange(1,3)
        self.velocitat_y = random.randrange(1,3)
    def update(self):
        self.rect.x += self.velocitat_x
        self.rect.y += self.velocitat_y
        # Limita el margen derecho
        if self.rect.right > AMPLADA:
            self.velocitat_x -=1

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocitat_x +=1

        # Limita el margen inferior
        if self.rect.bottom > ALÇADA:
            self.velocitat_y -=1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocitat_y +=1
class EnemicsVerds(pygame.sprite.Sprite):
# Sprite del enemigo
    def __init__(self):
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("enemigo2.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius=48
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.rect.y = random.randrange(ALÇADA - self.rect.height)
        self.velocitat_x = random.randrange(3,5)
        self.velocitat_y = random.randrange(3,5)
    def update(self):
        self.rect.x += self.velocitat_x
        self.rect.y += self.velocitat_y
        # Limita el margen derecho
        if self.rect.right > AMPLADA:
            self.velocitat_x -=1

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocitat_x +=1

        # Limita el margen inferior
        if self.rect.bottom > ALÇADA:
            self.velocitat_y -=1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocitat_y +=1

class EnemicsBlaus(pygame.sprite.Sprite):
# Sprite del enemigo
    def __init__(self):
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("enemigo3.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius=48
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.rect.y = random.randrange(ALÇADA - self.rect.height)
        self.velocitat_x = random.randrange(5,10)
        self.velocitat_y = random.randrange(5,10)
    def update(self):
        self.rect.x += self.velocitat_x
        self.rect.y += self.velocitat_y
        # Limita el margen derecho
        if self.rect.right > AMPLADA:
            self.velocitat_x -=1

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocitat_x +=1

        # Limita el margen inferior
        if self.rect.bottom > ALÇADA:
            self.velocitat_y -=1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocitat_y +=1
class EnemicsVermells(pygame.sprite.Sprite):
# Sprite del enemigo
    def __init__(self):
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("enemigo4.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.radius=48
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.rect.y = random.randrange(ALÇADA - self.rect.height)
        self.velocitat_x = random.randrange(10,15)
        self.velocitat_y = random.randrange(10,15)
    def update(self):
        self.rect.x += self.velocitat_x
        self.rect.y += self.velocitat_y
        # Limita el margen derecho
        if self.rect.right > AMPLADA:
            self.velocitat_x -=1

        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocitat_x +=1

        # Limita el margen inferior
        if self.rect.bottom > ALÇADA:
            self.velocitat_y -=1

        # Limita el margen superior
        if self.rect.top < 0:
            self.velocitat_y +=1

class Projectils(pygame.sprite.Sprite):
    def __init__(self, x, y): #x i y dinàmics
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("tret.png").convert(),(10,20))
        self.image.set_colorkey(NEGRE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
    def update(self):
        self.rect.y -= 25
        if self.rect.bottom < 0:
            self.kill()
class Meteorits(pygame.sprite.Sprite):
    def __init__(self):
        # Heretem  init de la classe Sprite de Pygame
        super().__init__()
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria == 0:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert(),(100,100))
            self.radius = 50
        if self.img_aleatoria == 1:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert(),(50,50))
            self.radius = 25
        if self.img_aleatoria == 2:
            self.image = pygame.transform.scale(pygame.image.load("meteorito.png").convert(),(25,25))
            self.radius = 12
        #Generació del rectangle i posició i velocitats inicial
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.width
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.velocitat = random.randrange(1, 15)
    def update(self):
        self.rect.y += self.velocitat
        if self.rect.top > ALÇADA: #Quan arriba al final
            self.rect.x = random.randrange(AMPLADA - self.rect.width)
            self.rect.y = -self.rect.width
            self.velocitat = random.randrange(1, 15)


# InicialiTzació de Pygame, creació de la finestra, títol i control de rellotge.
pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Treballant amb sprites")
rellotge = pygame.time.Clock()

#Grup de sprites, instanciació de l'objecte jugador i enemics
sprites = pygame.sprite.Group()
enemics_grocs = pygame.sprite.Group()
enemics_verds = pygame.sprite.Group()
enemics_blaus = pygame.sprite.Group()
enemics_vermells = pygame.sprite.Group()
bales = pygame.sprite.Group()
meteorits = pygame.sprite.Group()
#instanciació jugador
jugador = Jugador()
sprites.add(jugador)
#instanciació enemics
enemic1 = EnemicsGrocs()
enemics_grocs.add(enemic1)

enemic2 = EnemicsVerds()
enemics_verds.add(enemic2)

enemic3 = EnemicsBlaus()
enemics_blaus.add(enemic3)

enemic4 = EnemicsVermells()
enemics_vermells.add(enemic4)
#Instanciació meteorits
for x in range(10):
    meteorit = Meteorits()
    meteorits.add(meteorit)

# Bucle principal del joc
Seguir = True
while Seguir:
    # Velocitat del bucle
    rellotge.tick(FPS)
    # Events
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualització de sprites
    sprites.update()
    enemics_grocs.update()
    enemics_verds.update()
    enemics_blaus.update()
    enemics_vermells.update()
    bales.update()
    meteorits.update()
    
    #Programem les colisions
        #Bales amb enemics
    colisio_bales_grocs = pygame.sprite.groupcollide(enemics_grocs, bales, False, True)
    colisio_bales_verds = pygame.sprite.groupcollide(enemics_verds, bales, False, True)
    colisio_bales_blaus = pygame.sprite.groupcollide(enemics_blaus, bales, False, True)
    colisio_bales_vermells = pygame.sprite.groupcollide(enemics_vermells, bales, False, True)
    
        #Jugador amb meteorits
    colision_nave = pygame.sprite.spritecollide(jugador, meteorits, False, pygame.sprite.collide_circle)
        #Meteorits amb bales
    colision_disparos = pygame.sprite.groupcollide(meteorits, bales, False, False, pygame.sprite.collide_circle)

    if colisio_bales_grocs :
        puntuacio+=10
    if colisio_bales_verds :
        puntuacio+=20
    if colisio_bales_blaus :
        puntuacio+=40
    if colisio_bales_vermells :
        puntuacio+=50
    if colision_nave:
        print("Colisión de la nau...")
    if colision_disparos:
        print("Impacte d'un tret...")
    
    #if colisio_bales:
    #    nau_enemiga.image = pygame.image.load("explosio.png")
    #    nau_enemiga.velocitat_y += 10
    #elif nau_enemiga.rect.top > ALÇADA:
    #    nau_enemiga.kill()
        

    # Fons de pantalla, dibuix de sprites i formes geomètriques.
    pantalla.fill(NEGRE)
    sprites.draw(pantalla)
    enemics_blaus.draw(pantalla)
    enemics_vermells.draw(pantalla)
    enemics_grocs.draw(pantalla)
    enemics_verds.draw(pantalla)
    bales.draw(pantalla)
    meteorits.draw(pantalla)
    mostra_text(pantalla,consolas,str(puntuacio).zfill(7), VERMELL, 40, 700, 50)
    # ActualiTza el contingut de la pantalla.
    pygame.display.flip()

pygame.quit()
