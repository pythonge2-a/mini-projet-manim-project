import matplotlib.pyplot as plt
import numpy as np

# Paramètres de la simulation
g = 9.81  # Accélération due à la gravité en m/s²

# Valeur de v0 choisie par l'utilisateur
v0 = 10  # v0 référence en m/s

# Calcul des vitesses initiales autour de v0
v0_values = v0 * np.array([1/3, 2/3, 1, 4/3, 5/3])  # Vitesses initiales (en m/s)
theta = 60  # Angle de lancement en degrés
theta_rad = np.radians(theta)

# Création de la figure avec une hauteur réduite
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3.5))  # 1 ligne, 2 colonnes

# Tracé des trajectoires pour les vitesses initiales
for v in v0_values:
    t_total = 2 * v * np.sin(theta_rad) / g
    t_points = np.linspace(0, t_total, num=500)
    x = v * np.cos(theta_rad) * t_points
    y = v * np.sin(theta_rad) * t_points - 0.5 * g * t_points**2
    ax1.plot(x, y, label=f'v0 = {round(v, 1)} m/s')

# Détails du graphique 1
ax1.set_title("Trajectoires pour différentes vitesses initiales")
ax1.set_xlabel("Distance horizontale (m)")
ax1.set_ylabel("Hauteur (m)")
ax1.legend()
ax1.set_aspect('equal')

# Deuxième graphique : Angles variables
theta_values = [15, 30, 45, 60, 75]  # Angles de lancement
theta_rad_values = np.radians(theta_values)

for theta_rad in theta_rad_values:
    t_total = 2 * v0 * np.sin(theta_rad) / g
    t_points = np.linspace(0, t_total, num=500)
    x = v0 * np.cos(theta_rad) * t_points
    y = v0 * np.sin(theta_rad) * t_points - 0.5 * g * t_points**2
    ax2.plot(x, y, label=f'θ = {round(np.degrees(theta_rad))}°')

# Détails du graphique 2
ax2.set_title("Trajectoires pour différents angles de lancement")
ax2.set_xlabel("Distance horizontale (m)")
ax2.set_ylabel("Hauteur (m)")
ax2.legend()
ax2.set_aspect('equal')

# Sauvegarder l'image
plt.tight_layout()
plt.savefig('trajectoires.png')
