import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 10,
    'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}\usepackage{amsmath}',
    "font.family": "Times New Roman"
})


# --- Original vectors ---
u1 = np.array([1, 1, 1])
u2 = np.array([0, 1, 1])
u3 = np.array([0, 0, 1])

# --- Gram-Schmidt process ---
v1 = u1
v2 = u2 - np.dot(u2, v1)/np.dot(v1, v1) * v1
v3 = u3 - np.dot(u3, v1)/np.dot(v1, v1) * v1 - np.dot(u3, v2)/np.dot(v2, v2) * v2

q1 = v1 / np.linalg.norm(v1)
q2 = v2 / np.linalg.norm(v2)
q3 = v3 / np.linalg.norm(v3)

vectors = [
    (u1, [v1, v2, v3]   , None      , [u1, u2, u3]  , [q1, q2, q3], "Original Basis Vector"),
    (u1, [v1]           , None      , [u1]          , [], "Step 1: $v_1 = u_1$"),
    (u2, [v1, v2]       , [v1]      , [u1, u2]      , [], "Step 2: $v_2 = u_2 - \operatorname{proj}_{W_1} u_2$"),
    (u3, [v1, v2, v3]   , [v1, v2]  , [u1, u2, u3]  , [], "Step 3: $v_3 = u_3 - \operatorname{proj}_{W_2} u_3$")
]

anchor = 1.5

# --- Create 3 subplots side by side ---
fig = plt.figure(figsize=(24, 6), dpi=120)

for i, (u, orig_vecs, subspace, basis, orthonormal, title) in enumerate(vectors, 1):
    ax = fig.add_subplot(1, 4, i, projection='3d')

    # Axes
    ax.plot([-anchor, anchor], [0, 0], [0, 0], 'k', linewidth=0.8)
    ax.plot([0, 0], [-anchor, anchor], [0, 0], 'k', linewidth=0.8)
    ax.plot([0, 0], [0, 0], [-anchor, anchor], 'k', linewidth=0.8)

    if i == 1:
        for idx, u in enumerate(basis):
            ax.quiver(0, 0, 0, *u, color='g', linewidth=1.5, arrow_length_ratio=0.1, label=f'$u_{idx+1} = ({u[0]}, {u[1]}, {u[2]})$')
            ax.text(u[0], u[1], u[2], f'$u_{idx+1}$', color='g')

        for idx, v in enumerate(orthonormal):
            ax.quiver(0, 0, 0, *v, color='r', linewidth=1, arrow_length_ratio=0.1, label=f'$v_{idx+1} = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})$')
            ax.text(v[0] * 1.25, v[1], v[2], f'$q_{idx+1}$', color='r')
        
        ax.set_xlim([-anchor, anchor])
        ax.set_ylim([-anchor, anchor])
        ax.set_zlim([-anchor, anchor])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_box_aspect([1,1,1])
        ax.grid(False)
        ax.set_aspect('equal')
        ax.set_title(title)
        ax.legend(loc='lower left')
        continue
    print(f"Basis plotted i:{i}")

    # Plot all original vectors (gray)
    for idx, v in enumerate(orig_vecs):
        ax.quiver(0, 0, 0, *v, color='r', linewidth=1, arrow_length_ratio=0.1, label=f'$v_{idx+1} = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})$')
        ax.text(v[0] * 1.25, v[1], v[2], f'$v_{idx+1}$', color='r')
    

    # Plot current orthogonal vector (red)
    ax.quiver(0, 0, 0, *u, color='g', linewidth=2, arrow_length_ratio=0.1, label=f'$u_{i-1} = ({u[0]}, {u[1]}, {u[2]})$')
    ax.text(u[0], u[1], u[2], f'$u_{i-1}$', color='g')

    # Plot subspace if exists
    if subspace is not None:
        if len(subspace) == 1:
            # Line for W1
            w1 = subspace[0]
            t = np.linspace(-1.5, 1.5, 20)
            ax.plot(t*w1[0], t*w1[1], t*w1[2], color='magenta', linewidth=2, alpha=0.3, label=r'$W_1 = \text{span}\{v_1\}$')
        elif len(subspace) == 2:
            # Plane for W2
            a = np.linspace(-1, 1, 20)
            b = np.linspace(-1, 1, 20)
            A, B = np.meshgrid(a, b)
            X = A*subspace[0][0] + B*subspace[1][0]
            Y = A*subspace[0][1] + B*subspace[1][1]
            Z = A*subspace[0][2] + B*subspace[1][2]
            ax.plot_surface(X, Y, Z, color='cyan', alpha=0.3, label=r'$W_2 = \text{span}\{v_1,v_2\}$')

    # Settings
    ax.set_xlim([-anchor, anchor])
    ax.set_ylim([-anchor, anchor])
    ax.set_zlim([-anchor, anchor])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1,1,1])
    ax.grid(False)
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.legend(loc='lower left')

plt.tight_layout()
plt.show()