import matplotlib.pyplot as plt
import numpy as np

#defining grid size
ROWS = 20
COLUMNS = 10

#creating subplots and adjusting space between them
fig, axes = plt.subplots(ROWS, COLUMNS, figsize=(COLUMNS, ROWS)) 
fig.subplots_adjust(hspace= 0, wspace= 0) 

for ax in axes.flat: #iterates through each subplot
    ax.set_xticks([])  # Remove x-axis tick marks
    ax.set_yticks([])  # Remove y-axis tick marks
    ax.set_xlabel('')  # Remove x-axis label
    ax.set_ylabel('')  # Remove y-axis label

#initialising the subplots of grid with zeros
grid = np.zeros((ROWS,COLUMNS), dtype = int)

#setting colour based on cell's value
def update_colour(grid):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if grid[row][col] == 1:
                color = 'black'
            else:
                color = 'white'
            axes[row, col].set_facecolor(color)

#defining tetrominoes
tetrominoes = [
    np.array([[1,1], # O-shape
              [1,1]]),

    np.array([[1,1,1,1]]) # I-shape

    np.array([[0,1,0], # T-shape
              [1,1,1]]),

    np.array([[1,0], # L-shape
              [1,0],
              [1,1]])
]

#choosing random tetromino
current_tetromino = random.choice(tetrominoes)

#defining tetromino's position
tetromino_position = (0, random.radint(0, COLUMNS- current_tetromino.shape[1]))

#checking if the tetromino can fall down
def can_fall(grid, current_tetromino, tetromino_position):
    r , c = current_tetromino.shape
    row_pos, col_pos = tetromino_position

    for i in range(r):
        for j in range(c):
            if current_tetromino[i][j] == 1:
                if row_pos+ i + 1 >= ROWS or grid[row_pos+i+1][col_pos+j] == 1:
                    return False
    return True

#moving the tetromino down
def move_tetromino(grid, current_tetromino, tetromino_position):
    row_pos, col_pos = tetromino_position
    if can_fall(grid, current_tetromino, tetromino_position):
        row_pos += 1
        tetromino_position = (row_pos, col_pos)
    return tetromino_position

#detecting collision
