import pygame
from arts.colors import Color

class Meteor(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/meteor.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/player.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.y = 600
        self.rect.x = 400
    
    def update(self):
        pos_x = pygame.mouse.get_pos()[0]
        if pos_x <= 620:
            self.rect.x = pos_x

class Laser(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/laser.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5