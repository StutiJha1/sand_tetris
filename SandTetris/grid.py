import pygame

# Grid Constants
ROWS = 20
COLUMNS = 10
CELL_SIZE = 30

def create_grid():
    return [[(0, 0, 0) for _ in range(COLUMNS)] for _ in range(ROWS)]

def draw_grid(surface, grid):
    for i in range(ROWS):
        for j in range(COLUMNS):
            pygame.draw.rect(surface, grid[i][j], (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, (128, 128, 128), (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


