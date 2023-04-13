# importació de llibreries
import pygame
import sys

# Iniciem pygame
pygame.init()

# Creació de la pantalla
PANTALLA = pygame.display.set_mode((1000, 600))

# Títol de la pantalla
pygame.display.set_caption('Exterminator')

# Bucle d'execució
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()