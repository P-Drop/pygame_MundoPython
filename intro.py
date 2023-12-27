import pygame, sys

# inicializar pygame
pygame.init()

# definir tamaño de ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# crear bucle principal
while True:
    # registrar eventos en la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

