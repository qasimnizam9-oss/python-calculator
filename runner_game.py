import pygame
import sys

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Boy (player)
player_x = 50
player_y = 300
player_width = 40
player_height = 60
player_speed = 5

# Game state
is_fallen = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move right
    if keys[pygame.K_RIGHT] and not is_fallen:
        player_x += player_speed

    # Fall (simulate obstacle)
    if keys[pygame.K_f]:
        is_fallen = True

    # Stand up
    if keys[pygame.K_s]:
        is_fallen = False

    # Drawing
    screen.fill(WHITE)

    if is_fallen:
        # fallen boy
        pygame.draw.rect(screen, RED, (player_x, player_y + 30, 60, 30))
    else:
        # standing boy
        pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.update()
    clock.tick(60)
