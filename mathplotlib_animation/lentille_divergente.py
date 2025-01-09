import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Paramètres de la lentille
focal_length = 5  # Distance focale (positive pour lentille divergente)
lens_x = 0  # Position en x de la lentille
lens_width = 1.5  # Largeur horizontale totale de la lentille
lens_height = 6  # Hauteur maximale de la lentille

# Positions initiales des rayons lumineux (différents y)
y_starts = np.linspace(-2, 2, 5)  # 5 rayons espacés verticalement

# Fonction pour calculer la déviation d'un rayon
def refract_ray(x, y, focal_length):
    # Point focal (avant la lentille pour une lentille divergente)
    focal_point = (lens_x - focal_length, 0)
    # Calcul de la pente après la lentille
    slope_out = (y - focal_point[1]) / (x - focal_point[0])
    return slope_out

# Initialisation des données pour l'animation
num_frames = 100
x_ray_in = np.linspace(-5, lens_x, num_frames // 2)  # Rayon avant la lentille
x_ray_out = np.linspace(lens_x, 10, num_frames // 2)  # Rayon après la lentille

# Initialisation du graphique
fig, ax = plt.subplots()
ax.set_xlim(-6, 10)
ax.set_ylim(-3.5, 3.5)

# Tracé de la lentille divergente (en forme de sablier)
theta = np.linspace(0, np.pi, 100)  # Demi-cercle pour le haut
x_top = lens_x + (lens_width / 2) * np.cos(theta)  # x pour l'arc supérieur
y_top = -(lens_height / 2) * np.sin(theta)  # y inversé pour l'arc supérieur
x_bottom = lens_x + (lens_width / 2) * np.cos(theta)  # x pour l'arc inférieur
y_bottom = (lens_height / 2) * np.sin(theta)  # y pour l'arc inférieur

# Ajouter la forme complète de la lentille
x_lens = np.concatenate([x_top, x_bottom[::-1]])
y_lens = np.concatenate([y_top, y_bottom[::-1]])
ax.fill(x_lens, y_lens, color="skyblue", alpha=0.5, edgecolor="black", label="Lentille divergente")

# Position de la focale
focal_point = (lens_x - focal_length, 0)
ax.scatter(*focal_point, color="green", label="Focale", zorder=5)

# Tracés initiaux des rayons lumineux
ray_lines = [
    ax.plot([], [], color='red', lw=2, label="Rayon lumineux" if i == 0 else None)[0]
    for i in range(len(y_starts))
]

# Fonction d'initialisation
def init():
    for ray in ray_lines:
        ray.set_data([], [])
    return ray_lines

# Fonction d'animation
def update(frame):
    for i, y_start in enumerate(y_starts):
        if frame < num_frames // 2:
            # Avant la lentille
            y_ray_in = np.full_like(x_ray_in[:frame], y_start)  # Horizontal (y constant)
            ray_lines[i].set_data(x_ray_in[:frame], y_ray_in)
        else:
            # Après la lentille
            slope_out = refract_ray(lens_x, y_start, focal_length)
            y_ray_out = y_start + slope_out * (x_ray_out[:frame - num_frames // 2] - lens_x)
            ray_lines[i].set_data(
                np.concatenate([x_ray_in, x_ray_out[:frame - num_frames // 2]]),
                np.concatenate([np.full_like(x_ray_in, y_start), y_ray_out])
            )
    return ray_lines

# Création de l'animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

# Configuration des labels, titre et légende
plt.xlabel("Position x")
plt.ylabel("Position y")
plt.title("Déviation de rayons lumineux à travers une lentille divergente")
plt.grid()
plt.legend(loc="upper right")

# Sauvegarde de l'animation en vidéo MP4
ani.save('lens_divergente.mp4', writer='ffmpeg', fps=30)
