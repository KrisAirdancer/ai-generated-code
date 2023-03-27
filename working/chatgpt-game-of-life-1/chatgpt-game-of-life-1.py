import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the grid and the number of frames to run the simulation
N = 50
frames = 100

# Initialize the grid with random values
grid = np.random.randint(2, size=(N, N))

# Define a function to update the grid for each frame of the animation
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count the number of live neighbors
            neighbors = (grid[(i-1)%N][(j-1)%N] + grid[(i-1)%N][j] + grid[(i-1)%N][(j+1)%N] +
                         grid[i][(j-1)%N] + grid[i][(j+1)%N] +
                         grid[(i+1)%N][(j-1)%N] + grid[(i+1)%N][j] + grid[(i+1)%N][(j+1)%N])
            # Apply the rules of the Game of Life
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                newGrid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                newGrid[i][j] = 1
    # Update the grid for the next frame
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# Set up the plot and animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, frames=frames, fargs=(img, grid, N), interval=50, blit=True)

# Show the plot and start the animation
plt.show()
