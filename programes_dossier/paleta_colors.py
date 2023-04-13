# importación de paquetes
import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((500, 400))

# Especificación de título
pygame.display.set_caption('El meu primer joc')

# Creem la paleta de colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

PANTALLA.fill(VERMELL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.sys.exit()
    pygame.display.update()





