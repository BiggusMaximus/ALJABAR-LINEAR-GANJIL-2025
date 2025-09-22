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
# --- Define planes
n1 = np.array([1, 2, -2])   # normal of plane 1
n2 = np.array([2, 4, -4])   # normal of plane 2 (parallel to n1)

# Plane equations:
# Plane 1: x + 2y - 2z = 3  --> n1·X = 3
# Plane 2: 2x + 4y - 4z = 7 --> n2·X = 7

# --- Pick a point P0 on plane 1
# Set y=z=0 → x=3
P0 = np.array([3, 0, 0])

# --- Distance from P0 to plane 2
D = np.abs(np.dot(n2, P0) - 7) / np.linalg.norm(n2)

# --- Foot of perpendicular from P0 onto plane 2
t = (7 - np.dot(n2, P0)) / np.dot(n2, n2)
P = P0 + t*n2   # projection point on plane 2

# --- Meshgrid for visualization
xx, yy = np.meshgrid(np.linspace(-2, 6, 10), np.linspace(-2, 6, 10))

# Plane 1 surface
zz1 = (3 - xx - 2*yy) / (-2)
# Plane 2 surface
zz2 = (7 - 2*xx - 4*yy) / (-4)

# --- 3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

# --- Plot planes
ax.plot_surface(xx, yy, zz1, alpha=0.3, color="green", label="Plane 1")
ax.plot_surface(xx, yy, zz2, alpha=0.3, color="orange", label="Plane 2")

# --- Plot P0
ax.scatter(*P0, color="red", s=50)
ax.text(P0[0]+0.2, P0[1], P0[2], r"$P_0(3,0,0)$", fontsize=12, color="red")

# --- Plot projection P
ax.scatter(*P, color="purple", s=50)
ax.text(P[0]+0.2, P[1]+0.2, P[2], r"$P$", fontsize=12, color="purple")

# --- Draw perpendicular line from P0 to P
ax.plot([P0[0], P[0]], [P0[1], P[1]], [P0[2], P[2]],
        color="black", linewidth=2, linestyle="--")

# --- Annotate distance
ax.text((P0[0]+P[0])/2, (P0[1]+P[1])/2, (P0[2]+P[2])/2 + 0.4,
        rf"$D = \frac{{|2(3)+4(0)-4(0)-7|}}{{\sqrt{{2^2+4^2+(-4)^2}}}} = {D:.3f}$",
        fontsize=11, color="black")

# --- Axes setup
ax.set_xlim([-2, 6])
ax.set_ylim([-2, 6])
ax.set_zlim([-4, 4])
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.set_zlabel("Z", fontsize=12)

# --- Draw Cartesian axes
anchor = 7
ax.plot([-anchor, anchor], [0,0], [0,0], color="black", linewidth=0.8)
ax.plot([0,0], [-anchor, anchor], [0,0], color="black", linewidth=0.8)
ax.plot([0,0], [0,0], [-anchor, anchor], color="black", linewidth=0.8)
ax.grid(False)

plt.show()
