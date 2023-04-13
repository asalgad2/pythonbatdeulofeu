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
alt_img=fons.get_rect().height
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
    
    clock.tick(FPS)
    y_relativa = y % alt_img
    
    y=y+1
    PANTALLA.blit(fons,(x,y_relativa-alt_img))
    if (y_relativa<ALÇADA):
        PANTALLA.blit(fons,(x,y_relativa))
    
    
    
    pygame.display.update()