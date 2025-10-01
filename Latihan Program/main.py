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

P1 = np.array([2, 8, 4])
P2 = np.array([7, 10, -8])

# Define vector from P1 to P2
v = P2 - P1   # (5, 6, -12)

# 3D Plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# --- Draw vector from origin to P1
ax.quiver(0, 0, 0, P1[0], P1[1], P1[2], color="blue", arrow_length_ratio=0.1, linewidth=2)
ax.text(P1[0]+0.3, P1[1], P1[2], r"$\vec{OP}_1$", fontsize=12, color="blue")

# --- Draw vector from origin to P2
ax.quiver(0, 0, 0, P2[0], P2[1], P2[2], color="red", arrow_length_ratio=0.1, linewidth=2)
ax.text(P2[0]+0.3, P2[1], P2[2], r"$\vec{OP}_2$", fontsize=12, color="red")

# --- Draw vector from P1 to P2
ax.quiver(P1[0], P1[1], P1[2], v[0], v[1], v[2], color="green", arrow_length_ratio=0.1, linewidth=2)
ax.text(P1[0]+v[0]/2, P1[1]+v[1]/2, P1[2]+v[2]/2, r"$\vec{v} = \overrightarrow{P_1P_2}$", fontsize=12, color="green")

# Set axes limits
ax.set_xlim([-1, 8])
ax.set_ylim([-2, 8])
ax.set_zlim([-12, 5])

# Axis labels
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_zlabel("Z", fontsize=12)

# Draw Cartesian axes
anchor = 8
ax.plot([-anchor, anchor], [0,0], [0,0], color="black", linewidth=0.8)  # X-axis
ax.plot([0,0], [-anchor, anchor], [0,0], color="black", linewidth=0.8)  # Y-axis
ax.plot([0,0], [0,0], [-anchor, anchor], color="black", linewidth=0.8)  # Z-axis
ax.grid(False)  
ax.set_title(v)
plt.show()
