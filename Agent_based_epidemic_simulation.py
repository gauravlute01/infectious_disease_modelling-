# Agent Based Epidemic Simulation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Model parameters
R_circle = 2       # Circle radius for city boundary
r_infection = 0.1  # Infection radius
sigma = 0.03       # Random walk parameter (std deviation)
alpha = 0.5        # Probability of infection on contact
beta = 0.007       # Probability of recovery
gamma = 0.0        # Probability of losing immunity
N = 200            # Total number of agents
T = 2000           # Total time steps
S0, I0, R0 = 198, 2, 0  # Initial counts

# Initialize agents' states
states = np.array(['S'] * S0 + ['I'] * I0 + ['R'] * R0)

# Generate initial positions within the circle
positions = []
while len(positions) < N:
    pos = np.random.uniform(-R_circle, R_circle, (N, 2))
    pos = pos[np.linalg.norm(pos, axis=1) <= R_circle]  # Keep within circle
    positions.extend(pos)
positions = np.array(positions[:N])  # Trim to exact N agents if more were generated

# Function for random walk within boundary
def random_walk(positions):
    displacements = np.random.normal(0, sigma, positions.shape)
    positions += displacements
    distances_from_center = np.linalg.norm(positions, axis=1)
    outside = distances_from_center > R_circle
    positions[outside] = np.random.uniform(-R_circle, R_circle, positions[outside].shape)
    return positions

# Setting up the plot
fig, ax = plt.subplots()
ax.set_xlim(-R_circle, R_circle)
ax.set_ylim(-R_circle, R_circle)
circle = plt.Circle((0, 0), R_circle, color='black', fill=False)
ax.add_artist(circle)

# Initialize scatter plot for agents
scat = ax.scatter(positions[:, 0], positions[:, 1], c='blue')

# Function to update states and positions
def update(frame):
    global positions, states
    positions = random_walk(positions)

    # Update infection dynamics
    for i in range(N):
        if states[i] == 'I':
            distances = np.linalg.norm(positions - positions[i], axis=1)
            susceptible_neighbors = (states == 'S') & (distances < r_infection)
            states[susceptible_neighbors] = np.where(np.random.rand(np.sum(susceptible_neighbors)) < alpha, 'I', 'S')
    
    # Recovery process
    infected_agents = (states == 'I')
    states[infected_agents] = np.where(np.random.rand(np.sum(infected_agents)) < beta, 'R', 'I')

    # Loss of immunity process
    recovered_agents = (states == 'R')
    states[recovered_agents] = np.where(np.random.rand(np.sum(recovered_agents)) < gamma, 'S', 'R')
    
    # Update scatter plot colors based on states
    colors = np.array(['blue' if state == 'S' else 'red' if state == 'I' else 'green' for state in states])
    scat.set_offsets(positions)
    scat.set_color(colors)
    return scat,

# Run the animation
ani = FuncAnimation(fig, update, frames=T, interval=30, blit=True)
plt.title("Agent-Based Epidemic Simulation")
plt.savefig('Agent-Based Epidemic Simulation')
plt.show()
