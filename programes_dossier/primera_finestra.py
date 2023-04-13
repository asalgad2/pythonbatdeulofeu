import sys
import pygame

pygame.init()  #Inicia la llibreria

#Creació de la pantalla
pantalla = pygame.display.set_mode((500,400))
#Títol de la pantalla
pygame.display.set_caption('Primer joc')
#Cal posar el programa principal en un bucle per tal que es mantingui activa

# Creem la paleta de colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)
HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

pantalla.fill(VERMELL)

#Aquest codi l'haureu d'utilitzar sempre!!
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()





