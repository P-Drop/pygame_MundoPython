import pygame, sys, random
from arts.colors import Color

pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coor_list = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    coor_list.append([x,y])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(Color.WHITE.value)

    for punto in coor_list:
        punto[1] += 5
        if punto[1] >= 500:
            punto[1] = 0 
        pygame.draw.circle(screen, Color.RED.value, (punto[0], punto[1]), 2)

    pygame.display.flip()
    clock.tick(30)
