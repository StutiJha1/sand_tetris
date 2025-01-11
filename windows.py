import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_WIDTH = int(SCREEN_WIDTH * 0.8)
GRID_HEIGHT = int(SCREEN_HEIGHT * 0.8)
CELL_SIZE = 40

# Colors
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
SAND_COLOR = (255, 255, 0)
BLOCK_COLOR = (0, 0, 255)

# Grid properties
COLUMNS = GRID_WIDTH // CELL_SIZE
ROWS = GRID_HEIGHT // CELL_SIZE
OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sand Tetris")
clock = pygame.time.Clock() #initialize the clock

#adding score
#score = 0
#font = pygame.display.font.FONT(None, 36)

# Initialize grid
grid = []
for _ in range(ROWS):
    row = []
    for _ in range(COLUMNS):
        row.append(0)  # Add 0 for each column
    grid.append(row)  # Add the row to the grid


# Tetromino shapes
SHAPES = [
    [[1, 1, 1], [0, 1, 0]],  # T-shape
    [[1, 1, 1, 1]],          # I-shape
    [[1, 1], [1, 1]],        # O-shape
    [[0, 1, 1], [1, 1, 0]],  # S-shape
    [[1, 1, 0], [0, 1, 1]]   # Z-shape
]


class Tetromino:
    def __init__(self, shape): 
        self.shape = random.choice(SHAPES)
        self.row = 0
        #self.col = COLUMNS // 2 - len(shape[0]) // 2
        self.col = random.randint(0, COLUMNS - len(self.shape[0])) #random fall 

    def draw(self):
        for r, row in enumerate(self.shape): #r = index, row = content
            for c, cell in enumerate(row): 
                if cell: 
                    rect = pygame.Rect( #(h,v,width,height)
                        OFFSET_X + (self.col + c) * CELL_SIZE, 
                        OFFSET_Y + (self.row + r) * CELL_SIZE, 
                        CELL_SIZE,
                        CELL_SIZE,
                    )
                    pygame.draw.rect(screen, BLOCK_COLOR, rect) #filling the block
                    pygame.draw.rect(screen, GRAY, rect, 1) #lines 

    def move_down(self): 
        self.row += 1

    def can_move(self, grid, dr, dc):
        """Check if the tetromino can move by (dr, dc)."""
        for r, row in enumerate(self.shape): #iterate through rows
            for c, cell in enumerate(row): #iterate through cells of each row
                if cell:
                    nr, nc = self.row + r + dr, self.col + c + dc 
                    if nr >= ROWS or nc < 0 or nc >= COLUMNS or grid[nr][nc]: #already occupied:
                        return False
        return True

    def place_on_grid(self, grid):
        """Turn the tetromino into sand particles on the grid."""
        for r, row in enumerate(self.shape):
            for c, cell in enumerate(row):
                if cell:
                    nr, nc = self.row + r, self.col + c 
                    grid[nr][nc] = 1
                    if nr == 0:
                        return True
        return False


def draw_grid():
    """Draw the grid and its contents."""
    for row in range(ROWS):
        for col in range(COLUMNS):
            rect = pygame.Rect( #(x ,y, width, height)
                OFFSET_X + col * CELL_SIZE,
                OFFSET_Y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            # Draw sand particles
            if grid[row][col] == 1:
                pygame.draw.rect(screen, SAND_COLOR, rect)
            # Draw grid lines
            pygame.draw.rect(screen, GRAY, rect, 1)


'''def update_sand():
    """Update the falling sand particles."""
    for row in range(ROWS - 2, -1, -1):  # Start from bottom-1 and go upward
        for col in range(COLUMNS):
            if grid[row][col] == 1:  # Sand particle
                if grid[row + 1][col] == 0:  # Move down
                    grid[row + 1][col] = 1
                    grid[row][col] = 0'''
def update_sand():
    """Update the falling sand particles to the lowest possible position in one go."""
    # Go through each column
    for col in range(COLUMNS):
        # Initialize a variable to keep track of the lowest empty row
        lowest_empty_row = ROWS - 1  # Start at the bottom of the grid

        # Loop through the column from bottom to top (check if there's a sand particle)
        for row in range(ROWS - 1, -1, -1):
            if grid[row][col] == 1:  # If there's a sand particle in this cell
                if row != lowest_empty_row:
                    grid[lowest_empty_row][col] = 1  # Move the sand particle to the lowest empty space
                    grid[row][col] = 0  # Clear the original position of the sand particle
                lowest_empty_row -= 1  # Move the lowest empty row up by one




# Initialize font for Game Over text
font = pygame.font.Font(None, 48)  # Default font, size 48

# Game loop
running = True
current_tetromino = Tetromino(random.choice(SHAPES))
spawn_timer = 0
fall_speed = 1000  # Milliseconds per step

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and current_tetromino.can_move(grid, 0, -1):
                current_tetromino.col -= 1
            elif event.key == pygame.K_RIGHT and current_tetromino.can_move(grid, 0, 1):
                current_tetromino.col += 1
            elif event.key == pygame.K_DOWN and current_tetromino.can_move(grid, 1, 0):
                current_tetromino.move_down()

    # Tetromino falling
    spawn_timer += clock.get_time()
    if spawn_timer >= fall_speed:
        if current_tetromino.can_move(grid, 1, 0):
            current_tetromino.move_down()
        else:
            if current_tetromino.place_on_grid(grid):  # If Tetromino touches row 0
                text = font.render("Game Over!", True, (255, 0, 0))
                screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.wait(3000)  # Wait 3 seconds
                running = False
            else:
                update_sand()
                current_tetromino = Tetromino(random.choice(SHAPES))
        spawn_timer = 0

    # Draw everything
    screen.fill(BLACK)
    draw_grid()
    current_tetromino.draw()
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
