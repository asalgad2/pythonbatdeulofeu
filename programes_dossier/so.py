import pygame

# Iniciació de Pygame
pygame.init()

# Pantalla - finestra
AMPLADA, ALÇADA = 1000, 600
PANTALLA = pygame.display.set_mode((AMPLADA, ALÇADA))
pygame.display.set_caption('Exterminator')
icona=pygame.image.load('exterminator.png')
pygame.display.set_icon(icona)

# Fons del joc
fons = pygame.image.load('city.png')

# Música de fondo
pygame.mixer.music.load('gunner/so/intergalacticodyssey.ogg')
pygame.mixer.music.play(-1)

#Definició del personatge

quiet = pygame.image.load('gunner/idle.png')

caminaDreta = [pygame.image.load('gunner/run1.png'),
				 pygame.image.load('gunner/run2.png'),
				 pygame.image.load('gunner/run3.png'),
				 pygame.image.load('gunner/run4.png'),
				 pygame.image.load('gunner/run5.png'),
				 pygame.image.load('gunner/run6.png')]

caminaEsquerra = [pygame.image.load('gunner/run1-esq.png'),
				 pygame.image.load('gunner/run2-esq.png'),
				 pygame.image.load('gunner/run3-esq.png'),
				 pygame.image.load('gunner/run4-esq.png'),
				 pygame.image.load('gunner/run5-esq.png'),
				 pygame.image.load('gunner/run6-esq.png')]

salta = [pygame.image.load('gunner/jump1.png'),
		 pygame.image.load('gunner/jump2.png')]

# So. Imatges per quan premem la tecla corresponent
pujar_so = pygame.image.load('gunner/volumeup.png')
baixar_so = pygame.image.load('gunner/volumedown.png')
so_mute = pygame.image.load('gunner/volumemute.png')
so_max = pygame.image.load('gunner/volumemax.png')

x = 0
px = 50
py = 400
ample = 40
velocitat = 10 #És la velocitat del personatge (en px)

# Control de FPS
RELOJ = pygame.time.Clock()

# Variables salt
salt = False
# Comptador de salt
comptaSalt = 10

# Variables direcció
esquerra = False
dreta = False

# Passes
comptaPasses = 0

# Moviment
def actualitza_pantalla():
	# Variables globals
	global comptaPasses
	global x

	# Fons en moviment
	x_relativa = x % fons.get_rect().width
	PANTALLA.blit(fons, (x_relativa - fons.get_rect().width, 0))
	if x_relativa < AMPLADA:
		PANTALLA.blit(fons, (x_relativa, 0))
	x -= 5
	# Comptador de passes. Serveix per saber quina imatge caldrà obrir en cada animació i quantes passes
	# ha fet el nostre personatge
	if comptaPasses + 1 >= 6:
		comptaPasses = 0
	# Moviment a l'esquerra
	if esquerra:
		PANTALLA.blit(caminaEsquerra[comptaPasses // 1], (int(px), int(py)))
		comptaPasses += 1

	# Moviment a la dreta
	elif dreta:
		PANTALLA.blit(caminaDreta[comptaPasses // 1], (int(px), int(py)))
		comptaPasses += 1

	elif salt + 1 >= 2:
		PANTALLA.blit(salta[comptaPasses // 1], (int(px), int(py)))
		comptaPasses += 1

	else:
		PANTALLA.blit(quiet,(int(px), int(py)))

Seguir = True

# Bucle d'accions i controls
while Seguir:
	# FPS
	RELOJ.tick(18)

	# Bucle del joc
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Seguir = False

	# Quina tecla han premut?
	tecla = pygame.key.get_pressed()

	# Tecla A - Moviment a l'esquerra
	if tecla[pygame.K_a] and px > velocitat:
		px -= velocitat
		esquerra = True
		dreta = False

	# Tecla D - Moviment a la dreta
	elif tecla[pygame.K_d] and px < 900 - velocitat - ample:
		px += velocitat
		esquerra = False
		dreta = True

	# Personatge quiet
	else:
		esquerra = False
		dreta = False
		comptaPasses = 0

	# Tecla W - Moviment cap a dalt
	if tecla[pygame.K_w] and py > 200:
		py -= velocitat

	# Tecla S - Moviment cap a baix
	if tecla[pygame.K_s] and py < 500:
		py += velocitat
	# Tecla SPACE - Salt
	if not salt:
		if tecla[pygame.K_SPACE]:
			salt = True
			izquierda = False
			derecha = False
			cuentaPasos = 0
	else:
		if comptaSalt >= -10:
			py -= (comptaSalt * abs(comptaSalt)) * 0.5
			comptaSalt -= 1
		else:
			comptaSalt = 10
			salt = False
    # Control del volum
	# Baixa el volum
	if tecla[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
		PANTALLA.blit(baixar_so, (850, 25))
	elif tecla[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
		PANTALLA.blit(so_mute, (850, 25))

	# Sube volumen
	if tecla[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
		pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
		PANTALLA.blit(pujar_so, (850, 25))
	elif tecla [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
			PANTALLA.blit(so_max, (850, 25))

	# Desactivar sonido
	elif tecla[pygame.K_m]:
		pygame.mixer.music.set_volume(0.0)
		PANTALLA.blit(so_mute, (850, 25))

	# Reactivar sonido
	elif tecla[pygame.K_COMMA]:
		pygame.mixer.music.set_volume(1.0)
		PANTALLA.blit(so_max, (850, 25))

	# Actualización de la ventana
	pygame.display.update()
	#Llamada a la función de actualización de la ventana
	actualitza_pantalla()

# Salida del juego
pygame.quit()