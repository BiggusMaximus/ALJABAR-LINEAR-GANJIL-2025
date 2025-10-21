import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


plt.rcParams.update({
    'font.size': 8,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}\usepackage{amsmath}',
    "font.family": "Times New Roman"
})
# Create 3D plot

fig = plt.figure(figsize=(10, 8), dpi=250)
ax = fig.add_subplot(111, projection='3d')

anchor = 10
# Axes
ax.plot([-anchor, anchor], [0, 0], [0, 0], color="black", linewidth=0.8, zorder=10)
ax.plot([0, 0], [-anchor, anchor], [0, 0], color="black", linewidth=0.8, zorder=10)
ax.plot([0, 0], [0, 0], [-anchor, anchor], color="black", linewidth=0.8, zorder=10)

# Grid for plane x + y + z = 0
s = np.linspace(-3, 3, 20)
t = np.linspace(-3, 3, 20)
S, T = np.meshgrid(s, t)
X = 3 - 2*S - 3*T
Y = S
Z = T


# Plot plane
ax.plot_surface(X, Y, Z, alpha=0.5, color='cyan', rstride=1, cstride=1, edgecolor='none', label=r"$\textbf{Solution Space: } (3-2s-3t, s, t)$")

# Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_aspect('equal')
ax.legend()
ax.grid(False)

plt.show()
