import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import argparse
import sys

# Parser pour les arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Simulation d'une collision inélastique entre deux billes.")
parser.add_argument("--m1", type=float, required=True, help="Masse de la bille 1 (kg, > 0.1)")
parser.add_argument("--m2", type=float, required=True, help="Masse de la bille 2 (kg, > 0.1)")
parser.add_argument("--v1", type=float, required=True, help="Vitesse initiale de la bille 1 (m/s, > 0.1)")
parser.add_argument("--v2", type=float, required=True, help="Vitesse initiale de la bille 2 (m/s, -5 < v2 < v1)")
args = parser.parse_args()

# Vérification des limites des paramètres
if args.m1 <= 0.1:
    sys.exit("Erreur : La masse m1 doit être supérieure à 0.1 kg.")
if args.m2 <= 0.1:
    sys.exit("Erreur : La masse m2 doit être supérieure à 0.1 kg.")
if args.v1 <= 0.1:
    sys.exit("Erreur : La vitesse v1 doit être supérieure à 0.1 m/s.")
if not (-5 < args.v2 < args.v1):
    sys.exit("Erreur : La vitesse v2 doit être inférieure à v1 et supérieure à -5 m/s.")

# Paramètres des masses et vitesses
m1 = args.m1
m2 = args.m2
v1 = args.v1
v2 = args.v2

# Calcul de la vitesse après la collision inélastique
def calculate_velocity_inelastic(m1, m2, v1, v2):
    # Vitesse commune après la collision inélastique
    v_common = (m1 * v1 + m2 * v2) / (m1 + m2)
    return v_common

v_common = calculate_velocity_inelastic(m1, m2, v1, v2)

# Création de la figure et de l'axe
fig, ax = plt.subplots()
ax.set_xlim(-5, 25)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Création des billes
radius = 0.5
ball1 = plt.Circle((0, 0), radius, color='blue', label=f'Bille 1: m1={m1}kg, v1={v1}m/s, v\'={v_common:.2f}m/s', ec="black")
ball2 = plt.Circle((8, 0), radius, color='red', label=f'Bille 2: m2={m2}kg, v2={v2}m/s, v\'={v_common:.2f}m/s', ec="black")
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

    # Déplacement des billes en fonction du temps
    x1 += dx1 * 0.05
    x2 += dx2 * 0.05

    # Collision entre les billes (si elles se chevauchent)
    if abs(x1 - x2) <= 2 * radius and collision_time == 0:
        dx1 = dx2 = v_common  # Après la collision, les deux billes partagent la même vitesse
        collision_time = frame

    # Mettre à jour la position des billes
    ball1.set_center((x1, y1))
    ball2.set_center((x2, y2))

    return [ball1, ball2]

# Ajout des légendes
ax.legend()

# Ajout du titre et des labels des axes
ax.set_title("Collision inélastique entre Deux Billes")
ax.set_xlabel("Position x (m)")
ax.set_ylabel("Position y (m)")

# Création de l'animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# Sauvegarder l'animation dans un fichier MP4
ani.save('collision_inélastique_billes.mp4', writer='ffmpeg', fps=30)
