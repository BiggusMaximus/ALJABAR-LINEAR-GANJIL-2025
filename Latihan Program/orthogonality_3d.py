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
# Define point and normal
P0 = np.array([3, 0, 7])
n = np.array([4, 2, -5])   # normal vector

# --- Define the plane ax+by+cz = d
d = np.dot(n, P0)  # plane constant

xx, yy = np.meshgrid(np.linspace(-2, 6, 10), np.linspace(-2, 6, 10))
zz = (d - n[0]*xx - n[1]*yy) / n[2]

# 3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')
# --- Draw the plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color="green")

# --- Draw the normal vector from P0
ax.quiver(P0[0], P0[1], P0[2], n[0], n[1], n[2],
          color="blue", arrow_length_ratio=0.1, linewidth=2)
ax.text(P0[0]+n[0]/2, P0[1]+n[1]/2, P0[2]+n[2]/2,
        rf"$\vec{{n}} = \begin{{bmatrix}}{n[0]} \\ {n[1]} \\ {n[2]}\end{{bmatrix}}$",
        fontsize=12, color="blue")

# --- Mark point P0
ax.scatter(*P0, color="red", s=50)
ax.text(P0[0]+0.2, P0[1]-0.3, P0[2], r"$P_0(2,-1,4)$", fontsize=12, color="red")

# --- Add annotation for orthogonality
ax.text(0, -2, 6, r"$\vec{n} \cdot \overrightarrow{P_0P} = 0$", fontsize=12, color="k")

# Set axes limits
ax.set_xlim([-2, 6])
ax.set_ylim([-2, 6])
ax.set_zlim([-2, 8])

# Axis labels
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_zlabel("Z", fontsize=12)

# Draw Cartesian axes
anchor = 7
ax.plot([-anchor, anchor], [0,0], [0,0], color="black", linewidth=0.8)  # X-axis
ax.plot([0,0], [-anchor, anchor], [0,0], color="black", linewidth=0.8)  # Y-axis
ax.plot([0,0], [0,0], [-anchor, anchor], color="black", linewidth=0.8)  # Z-axis
ax.grid(False)

plt.show()
