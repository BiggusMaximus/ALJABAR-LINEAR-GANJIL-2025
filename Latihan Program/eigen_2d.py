import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plt.rcParams.update({
    'font.size': 8,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}\usepackage{amsmath}',
    "font.family": "Times New Roman"
})
# Fixed eigenvectors
v1 = np.array([1, 2])
v2 = np.array([2, -1])
P = np.column_stack((v1, v2))  # eigenvector matrix

# Initial eigenvalues
lambda1_init = 3
lambda2_init = -1

# Function to create matrix A from eigenvalues and fixed eigenvectors
def create_matrix(l1, l2):
    D = np.diag([l1, l2])
    return P @ D @ np.linalg.inv(P)

# Set up figure
fig, ax = plt.subplots(figsize=(7,7))
plt.subplots_adjust(bottom=0.25)

origin = np.array([[0,0],[0,0]])

# Initial matrix
A = create_matrix(lambda1_init, lambda2_init)
Av1 = A @ v1
Av2 = A @ v2

# Plot original vectors
q1 = ax.quiver(*origin[:,0], v1[0], v1[1], color='blue', scale=1, scale_units='xy', angles='xy')
q2 = ax.quiver(*origin[:,0], v2[0], v2[1], color='green', scale=1, scale_units='xy', angles='xy')

# Plot transformed vectors
q1t = ax.quiver(*origin[:,0], Av1[0], Av1[1], color='red', scale=1, scale_units='xy', angles='xy')
q2t = ax.quiver(*origin[:,0], Av2[0], Av2[1], color='orange', scale=1, scale_units='xy', angles='xy')

# Axes settings
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Matrix A and its effect on eigenvectors')

# Initial legend
legend = ax.legend([
        fr'$v_1 = \begin{{bmatrix}} {v1[0]} \\ {v1[1]} \end{{bmatrix}}$',
        fr'$v_2 = \begin{{bmatrix}} {v2[0]} \\ {v2[1]} \end{{bmatrix}}$',
        fr'$A = \begin{{bmatrix}} {A[0,0]:.2f} & {A[0,1]:.2f} \\ {A[1,0]:.2f} & {A[1,1]:.2f} \end{{bmatrix}}$',
        fr'$Av_1 = \lambda v_1$',
        fr'$Av_2 = \lambda v_2$',
    ], loc='upper left', fontsize=12)

# Slider axes
ax_lambda1 = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_lambda2 = plt.axes([0.25, 0.1, 0.65, 0.03])

slider_lambda1 = Slider(ax_lambda1, 'Lambda 1', -5.0, 5.0, valinit=lambda1_init)
slider_lambda2 = Slider(ax_lambda2, 'Lambda 2', -5.0, 5.0, valinit=lambda2_init)

def update(val):
    l1 = slider_lambda1.val
    l2 = slider_lambda2.val
    A = create_matrix(l1, l2)
    Av1 = A @ v1
    Av2 = A @ v2

    # Update quivers
    q1t.set_UVC(Av1[0], Av1[1])
    q2t.set_UVC(Av2[0], Av2[1])

    # Remove old legend
    global legend
    legend.remove()

    # Add new legend with updated values
    legend = ax.legend([
        fr'$v_1 = \begin{{bmatrix}} {v1[0]} \\ {v1[1]} \end{{bmatrix}}$',
        fr'$v_2 = \begin{{bmatrix}} {v2[0]} \\ {v2[1]} \end{{bmatrix}}$',
        fr'$A = \begin{{bmatrix}} {A[0,0]:.2f} & {A[0,1]:.2f} \\ {A[1,0]:.2f} & {A[1,1]:.2f} \end{{bmatrix}}$',
        fr'$Av_1 = {l1:.2f}v_1$',
        fr'$Av_2 = {l2:.2f}v_2$',
    ], loc='upper left', fontsize=12)
    
    fig.canvas.draw_idle()

slider_lambda1.on_changed(update)
slider_lambda2.on_changed(update)

plt.show()
