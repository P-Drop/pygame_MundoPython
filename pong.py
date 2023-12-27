import pygame, random
from arts.colors import Color

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

# Player variables
player_width = 15
player_heigh = 90
backspace = 50

# Jugador 1
player1_x = backspace
player1_y = (screen_size[1] - player_heigh) / 2
player1_speed = 0

# Jugador 2
player2_x = screen_size[0] - backspace - player_width
player2_y = (screen_size[1] - player_heigh) / 2
player2_speed = 0

# Ball
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                if player1_y <= 0:
                    pygame.event.clear()
                else:
                    player1_speed = -3
            if event.key == pygame.K_s:
                if player1_y >= (screen_size[1]- player_heigh):
                    pygame.event.clear()
                else:
                    player1_speed = 3
            
            # Jugador 2
            if event.key == pygame.K_UP:
                if player2_y <= 0:
                    pygame.event.clear()
                else:
                    player2_speed = -3
            if event.key == pygame.K_DOWN:
                if player2_y >= (screen_size[1] - player_heigh):
                    pygame.event.clear()
                else:
                    player2_speed = 3

            # Mas velocidad de bola
            if event.key == pygame.K_SPACE:
                ball_speed_x *= 1.2
                ball_speed_y *= 1.2

                
        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_speed = 0
            if event.key == pygame.K_s:
                player1_speed = 0

            # Jugador 2
            if event.key == pygame.K_UP:
                player2_speed = 0
            if event.key == pygame.K_DOWN:
                player2_speed = 0

            # Mas velocidad de bola
            if event.key == pygame.K_SPACE:
                ball_speed_x *= 1
                ball_speed_y *= 1

    # Movimiento jugadores

    player1_y += player1_speed
    player2_y += player2_speed

    # Limite superior / inferior
    if ball_y >= 590 or ball_y <= 10:
        ball_speed_y *= -1

    # Limite izquierdo / derecho
    if ball_x >= 800 or ball_x <= 0:
        counter = 0
        ball_x = 400
        ball_y = random.randint(100, 500)
        ball_speed_x *= -1/1.2
        ball_speed_y *= 1/1.2

    # Movimiento pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    
    screen.fill(Color.BLACK.value)
    #Zona de dibujo
    jugador1 = pygame.draw.rect(screen, Color.WHITE.value, (player1_x, player1_y, player_width, player_heigh))
    jugador2 = pygame.draw.rect(screen, Color.WHITE.value, (player2_x, player2_y, player_width, player_heigh))
    ball = pygame.draw.circle(screen, Color.WHITE.value, (ball_x, ball_y), 10)

    # Colisiones
    if ball.colliderect(jugador1) or ball.colliderect(jugador2):
        ball_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


