import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Paramètres du projectile
v0 = 10  # Vitesse initiale en m/s (module de la vitesse)
theta = 45  # Angle de lancement en degrés par rapport à l'axe des X
g = 9.81  # Accélération due à la gravité en m/s²

# Conversion de l'angle en radians
theta_rad = np.radians(theta)

# Calcul du temps total de vol (lorsque la bille atteint le sol)
t_total = 2 * v0 * np.sin(theta_rad) / g

# Définir le nombre de points pour l'animation
t_points = np.linspace(0, t_total, num=500)

# Calcul des positions x et y à chaque instant t
x = v0 * np.cos(theta_rad) * t_points
y = v0 * np.sin(theta_rad) * t_points - 0.5 * g * t_points**2

# Calcul de la portée maximale
max_x = max(x)
max_y = max(y)

# Rayon de la bille (constant de 0,2 mètre)
radius = 0.2  # Le rayon est maintenant fixé à 0,2 mètre

# Calcul du facteur de mise à l'échelle pour garantir que les axes ont la même échelle
factor = max(max_x, max_y)

# Création de la figure et de l'axe
fig, ax = plt.subplots()
ax.set_xlim(0, factor)
ax.set_ylim(0, factor)

# Assurer que les axes sont à la même échelle
ax.set_aspect('equal')

# Création de la bille (sphère représentée par un cercle)
ball = plt.Circle((0, 0), radius, color='blue', ec="black")
ax.add_patch(ball)

# Variables pour les positions
x_pos, y_pos = 0, 0  # Position initiale du projectile

# Fonction de mise à jour de l'animation
def update(frame):
    global x_pos, y_pos
    
    # Mise à jour de la position de la bille
    x_pos = x[frame]
    y_pos = y[frame]
    
    # Mettre à jour la position de la bille
    ball.set_center((x_pos, y_pos))
    
    return [ball]

# Ajout du titre et des labels des axes
ax.set_title("Trajectoire d'une Sphère Lancée")
ax.set_xlabel("Distance horizontale (m)")
ax.set_ylabel("Hauteur (m)")

# Création de l'animation
ani = FuncAnimation(fig, update, frames=len(t_points), interval=20, blit=True)

# Sauvegarder l'animation dans un fichier MP4
ani.save(f'trajectoire_bille.mp4', writer='ffmpeg', fps=30)

