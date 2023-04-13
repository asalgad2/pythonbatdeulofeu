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
FPS=20

# Bucle d'execució
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	x_relativa = x % ample_img
	print('X :',x)
	print('Amplada img :', ample_img)
	print('X_relativa :', x_relativa)
	x=x-1
	PANTALLA.blit(fons,(x_relativa,y))
	
	clock.tick(FPS)
	pygame.display.update()