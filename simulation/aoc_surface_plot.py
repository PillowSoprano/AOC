import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fixed Parameters
I2 = 20  # Fixed Heterogeneity
AUC_values = np.linspace(0.6, 0.95, 50)
Corr_values = np.linspace(0.2, 0.9, 50)

# Generate Grid
AUC_grid, Corr_grid = np.meshgrid(AUC_values, Corr_values)

# AOC Formula
AOC_grid = (AUC_grid * Corr_grid) / (1 + I2 / 100)

# Rendering 3D Surfaces
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(AUC_grid, Corr_grid, AOC_grid, cmap='plasma', alpha=0.9)
ax.set_xlabel('AUC', labelpad=10)
ax.set_ylabel('Corr', labelpad=10)
ax.set_zlabel('AOC', labelpad=10)
ax.set_title('AOC surface vs. AUC & Corr (I² = 20%)')

fig.colorbar(surf, shrink=0.5, aspect=10, label='AOC value')

plt.tight_layout()
plt.savefig("AOC_surface_plot.png", dpi=300)
plt.show()
