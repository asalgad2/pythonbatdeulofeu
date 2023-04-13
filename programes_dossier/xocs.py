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
# InicialiTzació de Pygame, creació de la finestra, títol i control de rellotge.
pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Treballant amb sprites")
rellotge = pygame.time.Clock()

#Grup de sprites, instanciació de l'objecte jugador i enemics
sprites = pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)

dolents = pygame.sprite.Group()
nau_enemiga = Enemics()
dolents.add(nau_enemiga)

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
    dolents.update()

    # Fons de pantalla, dibuix de sprites i formes geomètriques.
    pantalla.fill(NEGRE)
    sprites.draw(pantalla)
    pygame.draw.line(pantalla, H_50D2FE, (400, 0), (400, 800), 1)
    pygame.draw.line(pantalla, BLAU, (0, 300), (800, 300), 1)
    # ActualiTza el contingut de la pantalla.
    pygame.display.flip()

pygame.quit()
