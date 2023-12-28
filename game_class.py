import pygame, random
from arts.colors import Color
from space_sprites import Meteor, Player

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720


class Game(object):
    def __init__(self) -> None:
        self.game_over = False

        self.score = 0

        self.meteor_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            meteor = Meteor()
            meteor.rect.x = random.randrange(700)
            meteor.rect.y = random.randrange(700)
            self.meteor_list.add(meteor)
            self.all_sprites_list.add(meteor)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False

    def run_logic(self):
        if not self.game_over:
            pygame.mouse.set_visible(0)
            self.all_sprites_list.update()

            meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            for meteor in meteor_hit_list:
                self.score += 1
                print(self.score)

            if len(self.meteor_list) == 0:
                pygame.mouse.set_visible(1)
                self.game_over = True

    def display_frame(self, screen):
        screen.fill(Color.WHITE.value)

        if self.game_over:
            font = pygame.font.SysFont("Calibri", 25)
            text = font.render("GAME OVER, Click para Jugar otra vez", True, Color.RED.value)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        else:        
            self.all_sprites_list.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    done = False
    clock = pygame.time.Clock()
    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()