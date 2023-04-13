import sys
import pygame

#inicia la llíbreria
pygame.init()

#Creació de la pantalla
PANTALLA = pygame.display.set_mode ((300,600))

#Títol
pygame.display.set_caption('Hello World')

#Creem la paleta de colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (16, 229, 213)
HC74225 = (199, 66, 37)
H61CD45 = (97, 205, 53)
TARONJA = (248, 190, 11)
RA = (234, 118, 3)
#Pintem la pantalla amb el color triat
PANTALLA.fill(RA)
#separació x   
pygame.draw.rect(PANTALLA, BLAU, (0,0,350,350))

pygame.draw.line(PANTALLA, VERMELL,[20,320],[200,320],59)
pygame.draw.line(PANTALLA, VERD,[250,100],[250,200],80)


pygame.draw.rect(PANTALLA, TARONJA, (300,300,100,100))
pygame.draw.line(PANTALLA, RA,[0,0],[0,600],50)
pygame.draw.line(PANTALLA, RA,[300,-600],[300,600],59)
pygame.draw.line(PANTALLA, RA,[0,0],[300,0],50)
pygame.draw.line(PANTALLA, NEGRE,[85,440],[215,440],30)
pygame.draw.line(PANTALLA, NEGRE,[150,385],[150,500],35)

#Inici
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit ()
                        pygame.sys.exit()
        pygame.display.update()