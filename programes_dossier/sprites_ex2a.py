import pygame

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
H_50D2FE = (94,210,254)

class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heretem l' init de la classe Sprite de Pygame
        super().__init__()
        # Rectangle (jugador)
        self.image = pygame.Surface((200, 200))
        self.image.fill(BLAU)
        # Obtenim el rectangle (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectangle en pantalla (sprite)
        self.rect.center = (100, 100)

    def update(self):
        # Actualiza esto cada vuelta de bucle.
        if self.rect.y ==0:
            self.rect.y=0
            self.rect.x += 10
        if self.rect.right == AMPLADA and not self.rect.bottom == ALÇADA:
            self.rect.right=AMPLADA
            self.rect.y +=10
        if self.rect.bottom == ALÇADA and self.rect.right == AMPLADA:
            self.rect.bottom = ALÇADA
            self.rect.x -=10
            
            
            
    
    

# InicialiTzació de Pygame, creació de la finestra, títol i control de rellotge.
pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption("Treballant amb sprites")
rellotge = pygame.time.Clock()

#Grup de sprites, instanciació de l'objecte jugador.
sprites = pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)

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

    # Fons de pantalla, dibuix de sprites i formes geomètriques.
    pantalla.fill(BLANC)
    sprites.draw(pantalla)
    pygame.draw.line(pantalla, H_50D2FE, (400, 0), (400, 800), 1)
    pygame.draw.line(pantalla, BLAU, (0, 300), (800, 300), 1)
    # ActualiTza el contingut de la pantalla.
    pygame.display.flip()

pygame.quit()