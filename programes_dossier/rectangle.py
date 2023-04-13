# importació de llibreries
import pygame
import sys

# Inicialització de pygame
pygame.init()

# Creació de la pantalla
PANTALLA = pygame.display.set_mode((500, 400))

# Títol
pygame.display.set_caption('El meu primer joc')

# Creem la paleta de colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

#Pintem la pantalla amb el color triat
PANTALLA.fill(HC74225)
#Dibuixa un rectangle
pygame.draw.rect(PANTALLA, BLANC, (100,50,100,50))
#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.sys.exit()
    pygame.display.update() #Actualitza la pantalla





