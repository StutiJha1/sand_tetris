import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
GRID_WIDTH = int(SCREEN_WIDTH * 0.8)
GRID_HEIGHT = int(SCREEN_HEIGHT * 0.8)
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
SAND_COLOR = (194, 178, 128)

# Grid properties
COLUMNS = GRID_WIDTH // CELL_SIZE
ROWS = GRID_HEIGHT // CELL_SIZE
OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sand Tetris")
clock = pygame.time.Clock()

# Initialize grid
grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]


def draw_grid(surface):
    """Draw the grid and its contents."""
    for row in range(ROWS):
        for col in range(COLUMNS):
            rect = pygame.Rect(
                OFFSET_X + col * CELL_SIZE,
                OFFSET_Y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            # Draw sand particles
            if grid[row][col] == 1:
                pygame.draw.rect(surface, SAND_COLOR, rect)
            # Draw grid lines
            pygame.draw.rect(surface, GRAY, rect, 1)


def update_sand():
    """Update the falling sand particles."""
    for row in range(ROWS - 2, -1, -1):  # Start from bottom-1 and go upward
        for col in range(COLUMNS):
            if grid[row][col] == 1:  # Sand particle
                if grid[row + 1][col] == 0:  # Move down
                    grid[row + 1][col] = 1
                    grid[row][col] = 0
                elif col > 0 and grid[row + 1][col - 1] == 0:  # Move diagonally left
                    grid[row + 1][col - 1] = 1
                    grid[row][col] = 0
                elif col < COLUMNS - 1 and grid[row + 1][col + 1] == 0:  # Move diagonally right
                    grid[row + 1][col + 1] = 1
                    grid[row][col] = 0


def spawn_sand():
    """Spawn a sand particle at a random column."""
    col = random.randint(0, COLUMNS - 1)
    if grid[0][col] == 0:  # Only spawn if the top row is empty
        grid[0][col] = 1


def check_game_over():
    """Check if the top row is filled."""
    for col in range(COLUMNS):
        if grid[0][col] == 1:
            return True
    return False


# Game loop
running = True
spawn_timer = 0
spawn_interval = 500  # Spawn sand every 500ms

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn sand particles at intervals
    spawn_timer += clock.get_time()
    if spawn_timer >= spawn_interval:
        spawn_sand()
        spawn_timer = 0

    # Update game logic
    update_sand()
    if check_game_over():
        print("Game Over!")
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_grid(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()

