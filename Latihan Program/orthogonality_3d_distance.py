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
P0 = np.array([1, -4, -3])       # given point
n = np.array([2, -3, 6])         # normal vector
d = -1                           # plane constant (from 2x - 3y + 6z = -1)

# Rewrite plane as ax+by+cz+d=0
# Here: 2x - 3y + 6z + 1 = 0
plane_d = 1

# --- Create meshgrid for the plane
xx, yy = np.meshgrid(np.linspace(-6, 6, 10), np.linspace(-6, 6, 10))
zz = (-plane_d - n[0]*xx - n[1]*yy) / n[2]

# --- Foot of perpendicular (projection of P0 onto plane)
t = -(np.dot(n, P0) + plane_d) / np.dot(n, n)
P = P0 + t*n   # projected point on plane

# --- Distance formula
D = np.abs(np.dot(n, P0) + plane_d) / np.linalg.norm(n)

# --- 3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect('equal')

# --- Draw the plane
ax.plot_surface(xx, yy, zz, alpha=0.3, color="green")

# --- Draw normal vector at P0
ax.quiver(P0[0], P0[1], P0[2], n[0], n[1], n[2],
          color="blue", arrow_length_ratio=0.1, linewidth=2)
ax.text(P0[0]+n[0]/2, P0[1]+n[1]/2, P0[2]+n[2]/2,
        rf"$\vec{{n}} = \begin{{bmatrix}}{n[0]} \\ {n[1]} \\ {n[2]}\end{{bmatrix}}$",
        fontsize=12, color="blue")

# --- Mark point P0
ax.scatter(*P0, color="red", s=50)
ax.text(P0[0]+0.2, P0[1]-0.3, P0[2], r"$P_0(1,-4,-3)$", fontsize=12, color="red")

# --- Mark projection point P
ax.scatter(*P, color="purple", s=50)
ax.text(P[0]+0.2, P[1]+0.2, P[2], r"$P$", fontsize=12, color="purple")

# --- Draw perpendicular line from P0 to plane
ax.plot([P0[0], P[0]], [P0[1], P[1]], [P0[2], P[2]], 
        color="black", linewidth=2, linestyle="--")

# --- Annotate distance
ax.text((P0[0]+P[0])/2, (P0[1]+P[1])/2, (P0[2]+P[2])/2 + 0.4,
        rf"$D = \frac{{|2(1) - 3(-4) + 6(-3) + 1|}}{{\sqrt{{2^2 + (-3)^2 + 6^2}}}} = \frac{{3}}{{7}}$",
        fontsize=11, color="black")

# Axes setup
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([-6, 6])
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