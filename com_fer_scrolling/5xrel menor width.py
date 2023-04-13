# importació de llibreries
import pygame
import sys

# Iniciem pygame
pygame.init()

# Creació de la pantalla
AMPLADA=1000
ALÇADA=600
PANTALLA = pygame.display.set_mode((AMPLADA, ALÇADA))

# Títol de la pantalla
pygame.display.set_caption('Exterminator')

#Fons de la pantalla i icona
fons = pygame.image.load("city.png").convert()
ample_img=fons.get_rect().width
print(ample_img)
x=0
y=0

icona = pygame.image.load("exterminator.png")
pygame.display.set_icon(icona)
clock=pygame.time.Clock()
FPS=120

# Bucle d'execució
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    x_relativa = x % ample_img
    
    x=x-1
    PANTALLA.blit(fons,(x_relativa-ample_img,y))
    if (x_relativa<AMPLADA):
        PANTALLA.blit(fons,(x_relativa,y))
    
    pygame.draw.line(PANTALLA,(0,255,255),(x_relativa,0),(x_relativa,ALÇADA),(3))
    clock.tick(FPS)
    pygame.display.update()