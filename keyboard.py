import pygame, sys
from arts.colors import Color as Color

# inicializar pygame
pygame.init()


# definir tamaño de ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# definir reloj para controlar FPS
clock = pygame.time.Clock()

# coordenadas iniciales del cuadrado (centrado)
coord_x = 350
coord_y = 200
# velocidad
x_speed = 0
y_speed = 0

# crear bucle principal
while True:
    
    # registrar eventos en la ventana
    for event in pygame.event.get():
        # cerrar ventana al pulsar CERRAR
        if event.type == pygame.QUIT:
            sys.exit()
        
        # identificar eventos del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP:
            pass


    """
    ---- ZONA DE LOGICA
    """
    coord_x += x_speed
    coord_y += y_speed

    """
    ---- ZONA DE LOGICA
    """

    # color de fondo
    screen.fill(Color.WHITE.value)

    """
    ---- ZONA DE DIBUJO
    """

    pygame.draw.rect(screen, Color.RED.value, (coord_x, coord_y, 100, 100))

    """
    ---- ZONA DE DIBUJO 
    """
    
    # actualizar pantalla
    pygame.display.flip()

    # set FPS
    clock.tick(60)
