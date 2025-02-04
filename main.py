import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Number of dots
num_dots = 1000

# Create a sphere
phi = np.random.uniform(0, np.pi, num_dots)  # Polar angle
theta = np.random.uniform(0, 2 * np.pi, num_dots)  # Azimuthal angle

# Convert spherical coordinates to Cartesian coordinates
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the dots
scatter = ax.scatter(x, y, z, c='b', s=1)

# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Remove axis labels and grid for a cleaner look
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)

# Function to update the sphere's rotation
def update(frame):
    # Rotate the sphere by updating the azimuthal angle
    angle = frame * 0.05  # Rotation speed
    x_rot = x * np.cos(angle) - y * np.sin(angle)
    y_rot = x * np.sin(angle) + y * np.cos(angle)
    z_rot = z

    # Update the scatter plot data
    scatter._offsets3d = (x_rot, y_rot, z_rot)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()