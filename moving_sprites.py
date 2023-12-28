import pygame, random
from arts.colors import Color

class Moneda(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/elementos/coin.png').convert()
        self.image.set_colorkey(Color.WHITE.value)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > screen_size[1]:
            self.rect.y =- 10
            self.rect.x = random.randrange(screen_size[0])

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/elementos/balon.png').convert()
        self.image.set_colorkey(Color.WHITE.value)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x, self.rect.y = pygame.mouse.get_pos()

pygame.init()

screen_size = (720, 720)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

score = 0

done = False

background = pygame.image.load('arts/bg/bg_azul.png').convert()


monedas_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    moneda = Moneda()
    moneda.rect.x = random.randrange(720)
    moneda.rect.y = random.randrange(720)
    monedas_list.add(moneda)
    all_sprite_list.add(moneda)

player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    player.update()

    moneda_hit_list = pygame.sprite.spritecollide(player, monedas_list, True)

    for moneda in moneda_hit_list:
        score += 1
        print(score)

    screen.blit(background, [0,0])

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()