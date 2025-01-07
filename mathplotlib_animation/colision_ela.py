import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Paramètres des masses et vitesses
m1 = 10  # Masse du premier corps (kg)
m2 = 1   # Masse du second corps (kg)
v1 = 2   # Vitesse initiale du premier corps (m/s)
v2 = 0   # Vitesse initiale du second corps (m/s)

# Calcul des vitesses après la collision
def calculate_velocities(m1, m2, v1, v2):
    v1_prime = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_prime = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_prime, v2_prime

# Calcul des vitesses après la collision
v1_prime, v2_prime = calculate_velocities(m1, m2, v1, v2)

# Création de la figure et de l'axe
fig, ax = plt.subplots()
ax.set_xlim(-5, 25)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Création des billes (cercles pour les visualiser)
radius = 0.5  # Rayon des billes
ball1 = plt.Circle((0, 0), radius, color='blue', label=f'Bille 1: m1={m1}kg, v1={v1}m/s, v1\'={v1_prime:.2f}m/s', ec="black")
ball2 = plt.Circle((8, 0), radius, color='red', label=f'Bille 2: m2={m2}kg, v2={v2}m/s, v2\'={v2_prime:.2f}m/s', ec="black")
ax.add_patch(ball1)
ax.add_patch(ball2)

# Variables pour les positions et vitesses
x1, x2 = 0, 8  # Position initiale des billes
y1, y2 = 0, 0  # Position initiale des billes
dx1, dx2 = v1, v2  # Vitesses initiales des billes
collision_time = 0  # Temps d'impact

# Fonction de mise à jour de l'animation
def update(frame):
    global x1, x2, dx1, dx2, collision_time

    # Déplacement des billes en fonction du temps
    x1 += dx1 * 0.05  # Temps de pas (réduit pour plus de fluidité)
    x2 += dx2 * 0.05  # Temps de pas (réduit pour plus de fluidité)

    # Collision entre les billes (si elles se chevauchent)
    if abs(x1 - x2) <= 2 * radius and collision_time == 0:
        # Calcul des vitesses après la collision
        dx1, dx2 = calculate_velocities(m1, m2, v1, v2)
        collision_time = frame  # Marquer le temps de la collision

    # Mettre à jour la position des billes
    ball1.set_center((x1, y1))
    ball2.set_center((x2, y2))

    return [ball1, ball2]

# Ajout de la légende
ax.legend()

# Ajout du titre et des labels des axes
ax.set_title("Collision élastique entre Deux Billes")
ax.set_xlabel("Position x (m)")
ax.set_ylabel("Position y (m)")

# Création de l'animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# Sauvegarder l'animation dans un fichier MP4
ani.save('collision_élastique_billes.mp4', writer='ffmpeg', fps=30)

# Afficher l'animation (si nécessaire)
# plt.show()
