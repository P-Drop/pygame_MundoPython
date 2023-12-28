import pygame, random
from arts.colors import Color
from space_sprites import Meteor, Player, Laser

pygame.init()

screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('arts/mundo_python/background.png').convert()
clock = pygame.time.Clock()
done = False
score = 0

all_sprite_list = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()
laser_list  = pygame.sprite.Group()

for i in range(50):
    meteor = Meteor()
    meteor.rect.x = random.randrange(45, 650)
    meteor.rect.y = random.randrange(500)
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

player = Player()

sound = pygame.mixer.Sound('arts/mundo_python/laser5.ogg')

all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3)
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20
                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3)
            if event.key == pygame.K_SPACE:
                pass
            

    all_sprite_list.update()

    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
        if laser.rect.y <= -10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    screen.blit(background, (0,0))

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()