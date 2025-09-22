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
x0 = np.array([1, 2, 0])     # point on the plane
v1 = np.array([1, 0, 2])     # direction vector 1
v2 = np.array([0, 2, 1])     # direction vector 2

# ----------------------------
# Create a grid of parameters s, t
# ----------------------------
s_vals = np.linspace(-2, 2, 20)
t_vals = np.linspace(-2, 2, 20)
S, T = np.meshgrid(s_vals, t_vals)

# Parametric equation of the plane: X = x0 + s v1 + t v2
X = x0[0] + S * v1[0] + T * v2[0]
Y = x0[1] + S * v1[1] + T * v2[1]
Z = x0[2] + S * v1[2] + T * v2[2]

# ----------------------------
# Plot
# ----------------------------
fig = plt.figure(figsize=(8,6), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# Plot the plane
ax.plot_surface(X, Y, Z, alpha=0.4, color="lightblue")

# Plot the point x0
ax.scatter(*x0, color="red", s=50, label=r"$\vec{x}_0$")

# Plot the direction vectors from x0
ax.quiver(*x0, *v1, color="blue" , arrow_length_ratio=0.2, label=r"$\vec{v}_1$")
ax.text(
    (v1[0] + x0[0])/2, 
    (v1[1] + x0[1])/2, 
    (v1[2] + x0[2])/2, r"$\vec{v}_1$", fontsize=12, color="blue")

ax.quiver(*x0, *v2, color="green", arrow_length_ratio=0.2, label=r"$\vec{v}_2$")
ax.text(
    (v2[0] + x0[0])/2, 
    (v2[1] + x0[1])/2, 
    (v2[2] + x0[2])/2, r"$\vec{v}_2$", fontsize=12, color="green")

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.grid(False)
ax.legend(fontsize=12)
plt.show()
