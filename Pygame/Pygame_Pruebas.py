import pygame
from pygame.locals import *

pygame.init()

#	Creamos la ventana del juego
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")

# Creamos una variable "Color"
Color = pygame.Color(70,80,150)

#	Metodo para crar un circulo
pygame.draw.circle(ventana,Color,(80,90),20)

#	Metodo para crear un rectangulo
pygame.draw.rect(ventana,(130,70,70),(0,0,100,50))
#	Metodo para crear un pentagono
pygame.draw.polygon(ventana,(90,180,70),((140,0),(291,106),(237,277),(56,277),(0,106)))

while True:
	
	for evento in pygame.event.get():
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
