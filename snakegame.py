import time
import random
import sys
import pygame


# Game Variables
snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

food_pos = [random.randrange(1, (window_x//10)) *
            10, random.randrange(1, (window_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# Pygame Init
pygame.init()

# Pygame Display
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Direction Validation
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Food Spawn
    if not food_spawn:
        food_pos = [random.randrange(
            1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    # GFX
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
        pygame.quit()
        sys.exit()

    # Self hit
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    fps.tick(snake_speed)
