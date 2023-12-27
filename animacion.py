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

# definir reloj (controlar FPS)
clock = pygame.time.Clock()

'''
OBJETO -> CUADRADO
'''

# definir posicion del cuadrado
coord_x = 400
coord_y = 200
# definir velocidad del cuadrado
speed_x = 3
speed_y = 3

# crear bucle principal
while True:
    
    # registrar eventos en la ventana
    for event in pygame.event.get():
        # cerrar ventana al pulsar CERRAR
        if event.type == pygame.QUIT:
            sys.exit()

    '''
     ZONA DE LOGICA
    '''
    # hacer que el cuadrado rebote en los límites de la ventana
    if (coord_x >= 720 or coord_x <= 0):
        speed_x *= -1
    if (coord_y >= 420 or coord_y <= 0):
        speed_y *= -1

    coord_x += speed_x
    coord_y += speed_y

    '''
     ZONA DE LOGICA
    '''

    # color de fondo
    screen.fill(WHITE)

    """
     ZONA DE DIBUJO
    """

    # dibujar cuadrado
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 80, 80))


    """
     ZONA DE DIBUJO 
    """
    
    # actualizar pantalla
    pygame.display.flip()
    
    # Set 60 FPS
    clock.tick(60)
