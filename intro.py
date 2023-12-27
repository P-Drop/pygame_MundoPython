import pygame, sys

# inicializar pygame
pygame.init()

# definir colores
BLACK   =   (   0,   0,   0)
WHITE   =   ( 255, 255, 255)
GREEN   =   (   0, 255,   0)
RED     =   ( 255,   0,   0)
BLUE    =   (   0,   0, 255)



# definir tamaño de ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# crear bucle principal
while True:
    
    # registrar eventos en la ventana
    for event in pygame.event.get():
        # cerrar ventana al pulsar CERRAR
        if event.type == pygame.QUIT:
            sys.exit()

    # color de fondo
    screen.fill(WHITE)

    """
    ---- ZONA DE DIBUJO
    """
    # linea horizontal
    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 5)
    
    # rectangulo
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))

    # circulo
    pygame.draw.circle(screen, RED, [300, 300], 30)

    """
    ---- ZONA DE DIBUJO 
    """
    
    # actualizar pantalla
    pygame.display.flip()

