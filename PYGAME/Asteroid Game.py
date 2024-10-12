import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Dodger")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Spaceship settings
spaceship = pygame.Rect(375, 500, 50, 50)
spaceship_speed = 5

# Asteroid settings
asteroid_speed = 5
asteroid_spawn_time = 500  # milliseconds
last_asteroid_spawn = pygame.time.get_ticks()
asteroids = []

# Score settings
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.left > 0:
        spaceship.move_ip(-spaceship_speed, 0)
    if keys[pygame.K_RIGHT] and spaceship.right < SCREEN_WIDTH:
        spaceship.move_ip(spaceship_speed, 0)

    # Spawn asteroids
    if pygame.time.get_ticks() - last_asteroid_spawn > asteroid_spawn_time:
        asteroid = pygame.Rect(random.randint(0, SCREEN_WIDTH - 50), 0, 50, 50)
        asteroids.append(asteroid)
        last_asteroid_spawn = pygame.time.get_ticks()

    # Move asteroids
    for asteroid in asteroids[:]:
        asteroid.move_ip(0, asteroid_speed)
        if asteroid.top > SCREEN_HEIGHT:
            asteroids.remove(asteroid)
            score += 1

    # Check for collisions
    if any(spaceship.colliderect(asteroid) for asteroid in asteroids):
        running = False  # Game over

    # Draw spaceship and asteroids
    pygame.draw.rect(screen, WHITE, spaceship)
    for asteroid in asteroids:
        pygame.draw.rect(screen, RED, asteroid)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(200)

# Game over screen
screen.fill(BLACK)
game_over_text = font.render("Game Over!", True, WHITE)
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 30))
screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))
pygame.display.flip()
pygame.time.wait(2000)

# Clean up
pygame.quit()
sys.exit()
