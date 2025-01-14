import matplotlib.pyplot as plt
import numpy as np
import random

# Defining grid size
ROWS = 10
COLUMNS = 5

# Creating subplots and adjusting space between them
fig, axes = plt.subplots(ROWS, COLUMNS, figsize=(COLUMNS, ROWS))
fig.subplots_adjust(hspace=0, wspace=0)

for ax in axes.flat:  # Iterates through each subplot
    ax.set_xticks([])  # Remove x-axis tick marks
    ax.set_yticks([])  # Remove y-axis tick marks
    ax.set_xlabel('')  # Remove x-axis label
    ax.set_ylabel('')  # Remove y-axis label

# Initializing the subplots of the grid with zeros
grid = np.zeros((ROWS, COLUMNS), dtype=int)

# List of colors
tetromino_colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'yellow']

# Function to update color based on cell's value
def update_colour(grid, current_tetromino, tetromino_position, color):
    temp_grid = grid.copy()
    r, c = current_tetromino.shape
    row_pos, col_pos = tetromino_position

    for i in range(r):
        for j in range(c):
            if current_tetromino[i][j] == 1:
                temp_grid[row_pos + i][col_pos + j] = 1

    for row in range(ROWS):
        for col in range(COLUMNS):
            cell_value = temp_grid[row][col]
            if cell_value == 1:
                axes[row, col].set_facecolor(color)  # Set color for filled cells
            else:
                axes[row, col].set_facecolor('white')  # Set empty cells to white

# Defining tetrominoes
tetrominoes = [
    np.array([[1, 1, 1, 1]]),  # I-shape
    np.array([[1, 0],          # L-shape
              [1, 0],
              [1, 1]]),
    np.array([[1, 1],          # O-shape
              [1, 1]])
]

# Choosing random tetromino and assigning a random color
current_tetromino = random.choice(tetrominoes)
current_color = random.choice(tetromino_colors)

# Defining tetromino's position
tetromino_position = (0, random.randint(0, COLUMNS - current_tetromino.shape[1]))

# Checking if the tetromino can fall down
def can_fall(grid, current_tetromino, tetromino_position):
    r, c = current_tetromino.shape
    row_pos, col_pos = tetromino_position

    for i in range(r):
        for j in range(c):
            if current_tetromino[i][j] == 1:
                if row_pos + i + 1 >= ROWS or grid[row_pos + i + 1][col_pos + j] == 1:
                    return False
    return True

# Moving tetromino down by one step
def move_tetromino_down(grid, current_tetromino, tetromino_position):
    row_pos, col_pos = tetromino_position
    if can_fall(grid, current_tetromino, tetromino_position):
        row_pos += 1
        tetromino_position = (row_pos, col_pos)
    return tetromino_position

# Sand-like effect after collision
def sand_settle(grid, current_tetromino, tetromino_position):
    r, c = current_tetromino.shape
    row_pos, col_pos = tetromino_position

    # Initially placing the tetromino in the grid
    for i in range(r):
        for j in range(c):
            if current_tetromino[i][j] == 1:
                grid[row_pos + i][col_pos + j] = 1

    # Settling the tetromino into the grid
    for i in range(ROWS-2, -1, -1):
        for j in range(COLUMNS):
            if grid[i][j] == 1:  
                k = i
                while k + 1 < ROWS and grid[k + 1][j] == 0:
                    grid[k + 1][j] = 1
                    grid[k][j] = 0
                    k += 1

                if k + 1 < ROWS:
                    if j > 0 and grid[k + 1][j - 1] == 0 and grid[k][j - 1] == 0:
                        grid[k + 1][j - 1] = 1
                        grid[k][j] = 0
                    elif j + 1 < COLUMNS and grid[k + 1][j + 1] == 0 and grid[k][j + 1] == 0:
                        grid[k + 1][j + 1] = 1
                        grid[k][j] = 0

    # Checking if the grid is full at the top (game over condition)
    if any(grid[0] == 1):
        plt.text(0.5, 0.5, "Game Over!", color='red', fontsize=15, ha='center', va='center', transform=fig.transFigure)
        plt.draw()
        plt.pause(2)  # Pause to display "Game Over!" before the program exits
        return False  # Game over
    return True

# Game loop with sand-like behavior
def game_loop():
    global current_tetromino, tetromino_position, current_color
    while True:
        # Moving the tetromino down one step (gravity)
        if can_fall(grid, current_tetromino, tetromino_position):
            tetromino_position = move_tetromino_down(grid, current_tetromino, tetromino_position)
        else:
            # Settling the tetromino (like sand effect)
            if not sand_settle(grid, current_tetromino, tetromino_position):
                break  # End the game if it's over

            # Generating a new tetromino and color only after settling
            current_tetromino = random.choice(tetrominoes)
            current_color = random.choice(tetromino_colors)
            tetromino_position = (0, random.randint(0, COLUMNS - current_tetromino.shape[1]))

        # Updating the grid and plot
        update_colour(grid, current_tetromino, tetromino_position, current_color)
        plt.draw()
        plt.pause(0.5)  # Gravity speed: how fast the tetromino falls

# Starting the game loop
current_tetromino = random.choice(tetrominoes)
current_color = random.choice(tetromino_colors)
tetromino_position = (0, random.randint(0, COLUMNS - current_tetromino.shape[1]))
game_loop()

plt.show()
