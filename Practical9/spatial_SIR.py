import numpy as np
import matplotlib.pyplot as plt

# Grid size
size = 100
population = np.zeros((size, size))   # 0 = susceptible

# Randomly select one infected individual
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1   # 1 = infected

# Parameters
beta = 0.3
gamma = 0.05
time_steps = 100

# Plot initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Time 0')
plt.savefig('spatial_0.png')
plt.show()

# Neighbour offsets (8 directions)
neighbour_offsets = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),           (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]

# Simulation loop
for t in range(1, time_steps + 1):
    # Find all infected cells
    infected_indices = np.where(population == 1)
    infected_list = list(zip(infected_indices[0], infected_indices[1]))

    new_population = population.copy()

    for x, y in infected_list:
        # Recovery
        if np.random.random() < gamma:
            new_population[x, y] = 2   # 2 = recovered

        # Infect neighbours
        for dx, dy in neighbour_offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if population[nx, ny] == 0:   # susceptible
                    if np.random.random() < beta:
                        new_population[nx, ny] = 1   # becomes infected

    population = new_population

    # Plot every 10 time steps
    if t % 10 == 0 or t == time_steps:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {t}')
        plt.savefig(f'spatial_{t}.png')
        plt.show()