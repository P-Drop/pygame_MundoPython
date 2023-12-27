import pygame, sys
from arts.colors import Color as Color

# inicializar pygame
pygame.init()


# definir tamaño de ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# definir reloj para controlar FPS
clock = pygame.time.Clock()

# definir visibilidad del mouse
pygame.mouse.set_visible(0)

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

    x, y = pygame.mouse.get_pos()

    """
    ---- ZONA DE LOGICA
    """

    # color de fondo
    screen.fill(Color.WHITE.value)

    """
    ---- ZONA DE DIBUJO
    """

    pygame.draw.rect(screen, Color.RED.value, (x, y, 100, 100))

    """
    ---- ZONA DE DIBUJO 
    """
    
    # actualizar pantalla
    pygame.display.flip()

    # set FPS
    clock.tick(60)
