import pygame


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


GRID_WIDTH = int(SCREEN_WIDTH * 0.8)
GRID_HEIGHT = int(SCREEN_HEIGHT * 0.8)


CELL_SIZE = 30  # Size of each cell in the grid

# Number of rows and columns for the grid
COLUMNS = GRID_WIDTH // CELL_SIZE
ROWS = GRID_HEIGHT // CELL_SIZE

# Offsets to center the grid
OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

def draw_grid(surface):
    """Draw a grid on the surface."""
    for row in range(ROWS):
        for col in range(COLUMNS):
            # Draw the cell (empty, black for now)
            pygame.draw.rect(surface, (255, 255, 255), 
                             (OFFSET_X + col * CELL_SIZE, OFFSET_Y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Set up the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sand Tetris")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

   
    draw_grid(screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
