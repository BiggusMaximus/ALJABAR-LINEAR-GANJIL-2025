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
FONTSIZE = 12
fig = plt.figure(figsize=(8, 8), dpi=250)
ax = fig.add_subplot(111, projection='3d')

anchor = 10
ax.plot([-anchor, anchor], [0, 0], [0, 0], color="black", linewidth=0.8, zorder=10)  # X-axis
ax.plot([0, 0], [-anchor, anchor], [0, 0], color="black", linewidth=0.8, zorder=10)  # Y-axis
ax.plot([0, 0], [0, 0], [-anchor, anchor], color="black", linewidth=0.8, zorder=10)  # Z-axis

# --- Define the plane x+y+z=0 ---
xx = np.linspace(-8, 8, 20)
yy = np.linspace(-8, 8, 20)
XX, YY = np.meshgrid(xx, yy)
ZZ = -(XX + YY)   # from equation x+y+z=0

ax.plot_surface(XX, YY, ZZ, alpha=0.3, color="blue", zorder=1)

# --- Example spanning vectors for W ---
v1 = np.array([1, -1, 0])
v2 = np.array([1, 0, -1])
ax.quiver(0, 0, 0, *v1, color="red", linewidth=1.2, arrow_length_ratio=0.1, label=r'$v_1=(1,-1,0)$')
ax.quiver(0, 0, 0, *v2, color="green", linewidth=1.2, arrow_length_ratio=0.1, label=r'$v_2=(1,0,-1)$')

# --- Formatting ---
ax.set_xlim([-anchor, anchor])
ax.set_ylim([-anchor, anchor])
ax.set_zlim([-anchor, anchor])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

ax.set_aspect('auto')
ax.grid(False)
ax.legend()
plt.title(r"Subspace $W=\{(x,y,z):x+y+z=0\}$")
plt.show()
