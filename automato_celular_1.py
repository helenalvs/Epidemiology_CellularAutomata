import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


grid_size = 50  
p_infection = 0.3  
t_recovery = 2  
steps = 100  


np.random.seed(42)
grid = np.zeros((grid_size, grid_size), dtype=int)


num_initial_infected = 5
infected_positions = np.random.choice(grid_size**2, num_initial_infected, replace=False)
for pos in infected_positions:
    x, y = divmod(pos, grid_size)
    grid[x, y] = 1 


time_infected = np.zeros_like(grid)

def update(frame):
    global grid, time_infected
    new_grid = grid.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:  
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < grid_size and 0 <= nj < grid_size and grid[ni, nj] == 1:
                        if np.random.rand() < p_infection:
                            new_grid[i, j] = 1 
                            break
            elif grid[i, j] == 1: 
                time_infected[i, j] += 1
                if time_infected[i, j] >= t_recovery:
                    new_grid[i, j] = 2 
    
    grid = new_grid.copy()
    im.set_array(grid)
    return [im]

fig, ax = plt.subplots()
im = ax.imshow(grid, cmap="viridis", vmin=0, vmax=2)
ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, repeat=False)
plt.show()
