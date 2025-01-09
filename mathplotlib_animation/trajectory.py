import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import argparse

# Analyse des arguments de la ligne de commande
parser = argparse.ArgumentParser(description="Générer des graphiques et une animation des trajectoires.")
parser.add_argument('--v0', type=float, required=True, help="Vitesse initiale (5 à 25 m/s).")
parser.add_argument('--theta', type=float, required=True, help="Angle de lancement (10° à 90°).")
args = parser.parse_args()

# Validation des arguments
if not (5 <= args.v0 <= 25):
    raise ValueError("La vitesse initiale (v0) doit être comprise entre 5 et 25 m/s.")
if not (15 <= args.theta <= 80):
    raise ValueError("L'angle (theta) doit être compris entre 15° et 90°.")

# Paramètres de simulation
g = 9.81  # Accélération due à la gravité en m/s²
v0 = args.v0  # Vitesse initiale
theta = args.theta  # Angle de lancement
theta_rad = np.radians(theta)

# Calcul du temps total de vol
t_total = 2 * v0 * np.sin(theta_rad) / g

# Définir les points pour le calcul et l'animation
t_points = np.linspace(0, t_total, num=150)
x = v0 * np.cos(theta_rad) * t_points
y = v0 * np.sin(theta_rad) * t_points - 0.5 * g * t_points**2

# Calcul de la portée et de la hauteur maximales
max_x = max(x)
max_y = max(y)
axis_limit = max(3, max(max_x + (1/15)*max_x, max_y + (1/15)*max_y))  # Assure un minimum de 3m pour la limite des axes, ou légèrement au-dessus

# --- Génération des graphiques ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))  # Graphiques côte à côte

# Graphique 1 : Trajectoires pour différentes vitesses initiales
v0_values = v0 * np.array([1/3, 2/3, 1, 4/3, 5/3])
y_max_graph1 = 0  # Initialisation de la hauteur maximale
x_max_graph1 = 0  # Initialisation de la portée maximale

for v in v0_values:
    t_total_v = 2 * v * np.sin(theta_rad) / g
    t_points_v = np.linspace(0, t_total_v, num=150)
    x_v = v * np.cos(theta_rad) * t_points_v
    y_v = v * np.sin(theta_rad) * t_points_v - 0.5 * g * t_points_v**2
    y_max_graph1 = max(y_max_graph1, max(y_v))  # Mise à jour de la hauteur max
    x_max_graph1 = max(x_max_graph1, max(x_v))  # Mise à jour de la portée max
    ax1.plot(x_v, y_v, label=f'v0 = {round(v, 1)} m/s')

# Ajustement des limites des axes pour le graphique 1
ax1.set_ylim(0, max(0.5, (1/3) * x_max_graph1, y_max_graph1 + (1/15) * y_max_graph1))  # Limite Y minimum à 0.5m, 1/3 de la portée maximale, ou légèrement au-dessus de la hauteur maximale
ax1.set_xlim(0, max(1, x_max_graph1 + (1/15) * x_max_graph1))  # Limite X minimum à 1m, ou légèrement au-dessus de la portée maximale

ax1.set_title("Trajectoires pour différentes vitesses initiales")
ax1.set_xlabel("Distance horizontale (m)")
ax1.set_ylabel("Hauteur (m)")
ax1.legend(loc='upper right')
ax1.set_aspect('equal')

# Graphique 2 : Trajectoires pour différents angles
theta_values = [15, 30, 45, 60, 75]
for angle in theta_values:
    angle_rad = np.radians(angle)
    t_total_theta = 2 * v0 * np.sin(angle_rad) / g
    t_points_theta = np.linspace(0, t_total_theta, num=150)
    x_theta = v0 * np.cos(angle_rad) * t_points_theta
    y_theta = v0 * np.sin(angle_rad) * t_points_theta - 0.5 * g * t_points_theta**2
    ax2.plot(x_theta, y_theta, label=f'θ = {angle}°')

ax2.set_title("Trajectoires pour différents angles")
ax2.set_xlabel("Distance horizontale (m)")
ax2.set_ylabel("Hauteur (m)")
ax2.legend(loc='upper right')
ax2.set_aspect('equal')

# Ajustement et sauvegarde du graphique
plt.tight_layout()
plt.savefig("trajectoires_bille.png")


# --- Création de l'animation ---
fig, ax = plt.subplots()
ax.set_xlim(0, axis_limit)
ax.set_ylim(0, axis_limit)
ax.set_aspect('equal')

# Création de la bille
radius = 0.2  # Rayon de la bille
ball = plt.Circle((0, 0), radius, color='blue', ec="black", label="Bille")  # Ajout d'un label ici
ax.add_patch(ball)

# Ajout des labels
ax.set_title("Trajectoire projectile")
ax.set_xlabel("Distance horizontale (m)")
ax.set_ylabel("Hauteur (m)")

# Ajouter une légende en haut à droite
ax.legend(loc='upper right')

# Fonction de mise à jour pour l'animation
def update(frame):
    ball.set_center((x[frame], y[frame]))
    return [ball]

# Création de l'animation
ani = FuncAnimation(fig, update, frames=len(t_points), interval=20, blit=True)

# Sauvegarde de l'animation
ani.save("trajectoire_bille.mp4", writer='ffmpeg', fps=30)