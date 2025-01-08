#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

m=10
n=5

# Create the figure and subplots
fig, axes = plt.subplots(m, n,figsize=(n,m))
fig.subplots_adjust(hspace=0, wspace=0)

# Remove all axes labels
for ax in axes.flat:
    ax.set_xticks([])  # Remove x-axis tick marks
    ax.set_yticks([])  # Remove y-axis tick marks
    ax.set_xlabel('')  # Remove x-axis label
    ax.set_ylabel('')  # Remove y-axis label

# board = np.zeros((m, n), dtype=int)
board = np.random.randint(2, size=(m, n)) 

# Function to update the figure based on the board
def update_fig(board):
    for i in range(m):
        for j in range(n):
            color = 'black' if board[i, j] == 1 else 'white'
            axes[i, j].set_facecolor(color)


# Initial display
update_fig(board)

plt.show()