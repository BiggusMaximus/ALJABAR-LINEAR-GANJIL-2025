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
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Unit Vector
anchor = 10
ax.plot([-anchor, anchor], [0, 0], [0, 0]  , color="black", linestyle="solid", linewidth=0.1, zorder=10)  # X-axis
ax.plot([0, 0], [-anchor, anchor], [0, 0]  , color="black", linestyle="solid", linewidth=0.1, zorder=10)  # Y-axis
ax.plot([0, 0], [0, 0], [-anchor, anchor]          , color="black", linestyle="solid", linewidth=0.1, zorder=10)       # Z-axis

i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])
ax.quiver(0, 0, 0, *i, color="r", arrow_length_ratio=0.1, linewidth=0.5, label=rf'$i=\begin{{bmatrix}} {i[0]} & {i[1]} & {i[2]} \end{{bmatrix}}$')
ax.quiver(0, 0, 0, *j, color="g", arrow_length_ratio=0.1, linewidth=0.5, label=rf'$j=\begin{{bmatrix}} {j[0]} & {j[1]} & {j[2]} \end{{bmatrix}}$')
ax.quiver(0, 0, 0, *k, color="b", arrow_length_ratio=0.1, linewidth=0.5, label=rf'$k=\begin{{bmatrix}} {k[0]} & {k[1]} & {k[2]} \end{{bmatrix}}$')

# New Basis 
v1 = np.array([1, 1, 0])
v2 = np.array([0, 1, 1])
v3 = np.array([1, 0, 1])
anchor = 10
ax.plot(
    [-anchor * v1[0], anchor*v1[0]], 
    [-anchor * v1[1], anchor*v1[1]],
    [-anchor * v1[2], anchor*v1[2]], 
    color="black", linestyle="solid", linewidth=0.8, zorder=10)  
ax.plot(
    [-anchor * v2[0], anchor*v2[0]], 
    [-anchor * v2[1], anchor*v2[1]],
    [-anchor * v2[2], anchor*v2[2]], 
    color="black", linestyle="solid", linewidth=0.8, zorder=10)  
ax.plot(
    [-anchor * v3[0], anchor*v3[0]], 
    [-anchor * v3[1], anchor*v3[1]],
    [-anchor * v3[2], anchor*v3[2]], 
    color="black", linestyle="solid", linewidth=0.8, zorder=10)  

ax.quiver(0, 0, 0, *v1, color="lime", arrow_length_ratio=0.1, linewidth=2, label=rf'$v_1=\begin{{bmatrix}} {i[0]} & {i[1]} & {i[2]} \end{{bmatrix}}$')
ax.quiver(0, 0, 0, *v2, color="royalblue", arrow_length_ratio=0.1, linewidth=2, label=rf'$v_2=\begin{{bmatrix}} {j[0]} & {j[1]} & {j[2]} \end{{bmatrix}}$')
ax.quiver(0, 0, 0, *v3, color="yellow", arrow_length_ratio=0.1, linewidth=2, label=rf'$v_3=\begin{{bmatrix}} {k[0]} & {k[1]} & {k[2]} \end{{bmatrix}}$')

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_aspect('equal')
ax.grid(False)
ax.legend()

plt.show()