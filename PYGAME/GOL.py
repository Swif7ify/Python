import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set the screen size and grid parameters
WIDTH, HEIGHT = 1000, 800
GRID_SIZE = 100
CELL_SIZE = WIDTH // GRID_SIZE

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Create the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)


def update_grid(grid):
    # Count neighbors
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1)
                    for i in (-1, 0, 1)
                    for j in (-1, 0, 1)
                    if (i != 0 or j != 0))

    # Apply the rules of the Game of Life
    new_grid = (neighbors == 3) | (grid & (neighbors == 2))
    return new_grid.astype(int)


def draw_grid(screen, grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = WHITE if grid[x, y] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def generate_random_pattern(grid, fill_probability=0.2):
    """Generates a random pattern on the grid."""
    grid[:] = np.random.choice([0, 1], GRID_SIZE * GRID_SIZE, p=[1 - fill_probability, fill_probability]).reshape(
        GRID_SIZE, GRID_SIZE)


def main():
    running = True
    paused = True
    tck = 15
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_l:  # Press 'L' to generate a random pattern
                    generate_random_pattern(grid)
                elif event.key == pygame.K_e:
                    tck += 10
                elif event.key == pygame.K_q:
                    tck -= 10
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    grid[x, y] = 1

        if not paused:
            grid[:] = update_grid(grid)

        screen.fill(BLACK)
        draw_grid(screen, grid)
        pygame.display.flip()

        if tck <= 5:
            tck = 5
        if tck >= 100:
            tck = 100

        clock.tick(tck)  # Control the speed of the simulation
    pygame.quit()


if __name__ == "__main__":
    main()
