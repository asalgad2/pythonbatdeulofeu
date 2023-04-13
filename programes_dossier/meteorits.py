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
       
class Enemics(pygame.sprite.Sprite):
# Sprite del enemigo
    def __init__(self):
    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("enemiga.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(AMPLADA - self.rect.width)
        self.rect.y = random.randrange(ALÇADA - self.rect.height)
        self.velocitat_x = random.randrange(1,10)
        self.velocitat_y = random.randrange(1,10)
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
grupenemics = pygame.sprite.Group()
bales = pygame.sprite.Group()
meteorits = pygame.sprite.Group()
#instanciació jugador
jugador = Jugador()
sprites.add(jugador)
#instanciació enemics
nau_enemiga = Enemics()
grupenemics.add(nau_enemiga)
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
    grupenemics.update()
    bales.update()
    meteorits.update()
    
    #Programem les colisions
        #Bales amb enemics
    colisio_bales = pygame.sprite.groupcollide(grupenemics, bales, False, True)
        #Jugador amb meteorits
    colision_nave = pygame.sprite.spritecollide(jugador, meteorits, False, pygame.sprite.collide_circle)
        #Meteorits amb bales
    colision_disparos = pygame.sprite.groupcollide(meteorits, bales, False, False, pygame.sprite.collide_circle)

    if colision_nave:
        print("Colisión de la nau...")
    if colision_disparos:
        print("Impacte d'un tret...")
    
    if colisio_bales:
        nau_enemiga.image = pygame.image.load("explosio.png")
        nau_enemiga.velocitat_y += 10
    elif nau_enemiga.rect.top > ALÇADA:
        nau_enemiga.kill()

    # Fons de pantalla, dibuix de sprites i formes geomètriques.
    pantalla.fill(NEGRE)
    sprites.draw(pantalla)
    grupenemics.draw(pantalla)
    bales.draw(pantalla)
    meteorits.draw(pantalla)
    # ActualiTza el contingut de la pantalla.
    pygame.display.flip()

pygame.quit()