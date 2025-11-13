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

# --- Set up figure ---
fig = plt.figure(figsize=(8, 8), dpi=250)
ax = fig.add_subplot(111, projection='3d')

anchor = 8
ax.plot([-anchor, anchor], [0, 0], [0, 0], color="black", linewidth=0.8)  # X-axis
ax.plot([0, 0], [-anchor, anchor], [0, 0], color="black", linewidth=0.8)  # Y-axis
ax.plot([0, 0], [0, 0], [-anchor, anchor], color="black", linewidth=0.8)  # Z-axis

# --- Define subspace W and its orthogonal complement ---
w = np.array([1, 2, 2])  # Direction vector for W = span{w}
v1 = np.array([-2, 1, 0])  # Basis vector for W⊥
v2 = np.array([-2, 0, 1])  # Another basis vector for W⊥

# --- Create the plane for W⊥ ---
a = np.linspace(-3, 3, 20)
b = np.linspace(-3, 3, 20)
A, B = np.meshgrid(a, b)
X = A * v1[0] + B * v2[0]
Y = A * v1[1] + B * v2[1]
Z = A * v1[2] + B * v2[2]

# --- Plot plane W⊥ ---
ax.plot_surface(X, Y, Z, alpha=0.3, color="skyblue", label=r"$W^{\perp}=\operatorname{span}\{w_1\}$")

# --- Plot the line W ---
t = np.linspace(-3, 3, 20)
ax.plot(t * w[0], t * w[1], t * w[2], color="magenta", linewidth=2, label=r"$W=\operatorname{span}\{v_1, v_2\}$")

# --- Plot vectors for visual clarity ---
ax.quiver(0, 0, 0, *w, color="b", linewidth=2, arrow_length_ratio=0.5, label=r"$w_1 = (1,2,2)$")
ax.quiver(0, 0, 0, *v1, color="red", linewidth=1, arrow_length_ratio=0.1, label=r"$v_1 = (-2,1,0)$")
ax.quiver(0, 0, 0, *v2, color="green", linewidth=1, arrow_length_ratio=0.1, label=r"$v_2 = (-2,0,1)$")

# --- Axes settings ---
ax.set_xlim([-anchor, anchor])
ax.set_ylim([-anchor, anchor])
ax.set_zlim([-anchor, anchor])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

ax.set_box_aspect([1, 1, 1])
ax.grid(False)
ax.set_aspect('equal')
ax.legend()
plt.title("Orthogonal Complement in $\mathbb{R}^3$: $W$ and $W^{\perp}$", fontsize=10)
plt.show()
