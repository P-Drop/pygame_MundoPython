import pygame
from arts.colors import Color

class Meteor(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/meteor.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()

    def update(self):
        if self.rect.y >= 720:
            self.rect.y = -10
        self.rect.y += 3

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/player.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.y = 600
        self.rect.x = 400
        self.speed_x = 0
        self.speed_y = 0

    def changespeed(self, x):
        self.speed_x += x
    
    def update(self):
        """
        self.rect.x += self.speed_x
        """
        pos_x, pos_y = pygame.mouse.get_pos()
        if pos_x <= 680:
            self.rect.x = pos_x
        if pos_y <= 680:
            self.rect.y = pos_y

class Laser(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('arts/mundo_python/laser.png').convert()
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5