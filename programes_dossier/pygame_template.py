# importación de paquetes
import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Creación de la pantalla
PANTALLA = pygame.display.set_mode((500, 300))

# Especificación de título
pygame.display.set_caption('El meu primer joc')

# Bucle de ejecución
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	pygame.display.update()