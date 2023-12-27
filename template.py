import pygame, sys
from arts.colors import Color as Color

# inicializar pygame
pygame.init()


# definir tamaño de ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# definir reloj para controlar FPS
clock = pygame.time.Clock()

# crear bucle principal
while True:
    
    # registrar eventos en la ventana
    for event in pygame.event.get():
        # cerrar ventana al pulsar CERRAR
        if event.type == pygame.QUIT:
            sys.exit()


    """
    ---- ZONA DE LOGICA
    """


    """
    ---- ZONA DE LOGICA
    """

    # color de fondo
    screen.fill(Color.WHITE.value)

    """
    ---- ZONA DE DIBUJO
    """


    """
    ---- ZONA DE DIBUJO 
    """
    
    # actualizar pantalla
    pygame.display.flip()

    # set FPS
    clock.tick(60)
