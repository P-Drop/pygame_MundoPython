import pygame
from arts.colors import Color

pygame.init()

screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

done = False

pygame.mouse.set_visible(0)

background = pygame.image.load('arts/bg/bg_azul.png').convert()
player = pygame.image.load('arts/elementos/balon.png').convert()
player.set_colorkey(Color.WHITE.value)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x, y = pygame.mouse.get_pos()

    screen.blit(background, [0,0])

    screen.blit(player, [x- 50, y + 50])

    pygame.display.flip()
    clock.tick(60)


pygame.quit()