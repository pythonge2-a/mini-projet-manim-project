import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import argparse
import sys

# Parser pour les arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Simulation d'une collision élastique entre deux billes.")
parser.add_argument("--m1", type=float, required=True, help="Masse de la bille 1 (kg, 0.1 < m1 <= 15)")
parser.add_argument("--m2", type=float, required=True, help="Masse de la bille 2 (kg, 0.1 < m2 <= 15)")
parser.add_argument("--v1", type=float, required=True, help="Vitesse initiale de la bille 1 (m/s, 0.1 < v1 <= 15)")
parser.add_argument("--v2", type=float, required=True, help="Vitesse initiale de la bille 2 (m/s, -15 < v2 < v1 <= 15)")
args = parser.parse_args()

# Vérification des limites des paramètres
if args.m1 <= 0.1 or args.m1 > 15:
    sys.exit("Erreur : La masse m1 doit être comprise entre 0.1 kg et 15 kg.")
if args.m2 <= 0.1 or args.m2 > 15:
    sys.exit("Erreur : La masse m2 doit être comprise entre 0.1 kg et 15 kg.")
if args.v1 <= 0.1 or args.v1 > 15:
    sys.exit("Erreur : La vitesse v1 doit être comprise entre 0.1 m/s et 15 m/s.")
if not (-15 < args.v2 < args.v1 <= 15):
    sys.exit("Erreur : La vitesse v2 doit être comprise entre -15 m/s et v1, et v1 ne doit pas dépasser 15 m/s.")

# Paramètres des masses et vitesses
m1 = args.m1
m2 = args.m2
v1 = args.v1
v2 = args.v2


# Calcul des vitesses après la collision
def calculate_velocities(m1, m2, v1, v2):
    v1_prime = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_prime = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_prime, v2_prime

v1_prime, v2_prime = calculate_velocities(m1, m2, v1, v2)

# Création de la figure et de l'axe
fig, ax = plt.subplots(figsize=(10, 3.5))  # Ajustement de la taille de l'image, largeur=10, hauteur=3.5
ax.set_xlim(-5, 25)
ax.set_ylim(-5, 5)  # Les limites des axes restent inchangées
ax.set_aspect('equal')  # Maintien du rapport d'aspect égal pour les objets

# Création des billes
radius = 0.5
ball1 = plt.Circle((0, 0), radius, color='blue', label=f'Bille 1: m1={m1}kg, v1={v1}m/s, v1\'={v1_prime:.2f}m/s', ec="black")
ball2 = plt.Circle((8, 0), radius, color='red', label=f'Bille 2: m2={m2}kg, v2={v2}m/s, v2\'={v2_prime:.2f}m/s', ec="black")
ax.add_patch(ball1)
ax.add_patch(ball2)

# Variables pour les positions et vitesses
x1, x2 = 0, 8
y1, y2 = 0, 0
dx1, dx2 = v1, v2
collision_time = 0

# Fonction de mise à jour de l'animation
def update(frame):
    global x1, x2, dx1, dx2, collision_time

    x1 += dx1 * 0.05
    x2 += dx2 * 0.05

    if abs(x1 - x2) <= 2 * radius and collision_time == 0:
        dx1, dx2 = calculate_velocities(m1, m2, dx1, dx2)
        collision_time = frame

    ball1.set_center((x1, y1))
    ball2.set_center((x2, y2))

    return [ball1, ball2]

ax.legend()
ax.set_title("Collision élastique entre Deux Billes")
ax.set_xlabel("Position x (m)")
ax.set_ylabel("Position y (m)")

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)
ani.save('collision_élastique_billes.mp4', writer='ffmpeg', fps=30)
