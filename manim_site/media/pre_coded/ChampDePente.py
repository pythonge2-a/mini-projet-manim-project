from manim import *
import argparse
import numpy as np

class ChampDePenteSimple(Scene):
    def __init__(self, a_func, b_func, c_func, **kwargs):
        super().__init__(**kwargs)
        self.a_func = a_func
        self.b_func = b_func
        self.c_func = c_func

    def construct(self):
        # Paramètres pour les axes
        taille_x = 10  # Taille de l'axe x
        taille_y = 10  # Taille de l'axe y
        pas_x = 0.5  # Espacement sur l'axe x
        pas_y = 0.5  # Espacement sur l'axe y

        # Fonctions définies par l'utilisateur (évaluées à partir des arguments)
        a = lambda t, y: eval(self.a_func)
        b = lambda t, y: eval(self.b_func)
        c = lambda t, y: eval(self.c_func)

        # Fonction pour calculer la pente : y'(t)
        def pente(x, y):
            denom = a(x, y)
            if abs(denom) < 1e-3:  # Éviter la division par zéro
                return 0
            return (c(x, y) - b(x, y) * y) / denom

        # Fonction pour déterminer la couleur en fonction de la pente
        def couleur_pente(valeur_pente):
            norm_pente = np.clip(valeur_pente / 10, -1, 1)
            return interpolate_color(BLUE, RED, (norm_pente + 1) / 2)

        # Création des axes
        axes = Axes(
            x_range=[-taille_x, taille_x, pas_x],
            y_range=[-taille_y, taille_y, pas_y],
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        )

        # Ajouter les labels aux axes
        axes_labels = axes.get_axis_labels(x_label="t", y_label="y")

        # Génération du champ de pente
        champ = VGroup()
        for x in np.arange(-taille_x, taille_x, pas_x):
            for y in np.arange(-taille_y, taille_y, pas_y):
                pente_value = pente(x, y)
                pente_value = np.clip(float(pente_value), -100, 100)  # Convertir en float et limiter les valeurs extrêmes
                angle = np.arctan(pente_value)
                couleur = couleur_pente(pente_value)
                fleche = Arrow(
                    start=np.array([-0.2, 0, 0]),
                    end=np.array([0.2, 0, 0]),
                    stroke_width=2,
                    color=couleur,
                    buff=0,
                    max_tip_length_to_length_ratio=0.2,
                )
                fleche.rotate(angle)
                fleche.move_to(axes.c2p(x, y))
                champ.add(fleche)

        # Animation : Affichage des axes et du champ de pente
        self.play(Create(axes), Write(axes_labels))
        self.play(FadeIn(champ))
        self.wait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manim script for generating a slope field.")
    parser.add_argument("--a_func", type=str, required=True, help="Function a(t, y)")
    parser.add_argument("--b_func", type=str, required=True, help="Function b(t, y)")
    parser.add_argument("--c_func", type=str, required=True, help="Function c(t, y)")
    parser.add_argument("--output_name", type=str, required=True, help="Output filename")
    args = parser.parse_args()

    config.media_width = "100%"
    config.verbosity = "WARNING"
    config.quality = "high_quality"
    config.frame_rate = 60
    config.background_color = "#1e1e1e"
    config.video_dir = f"media/videos/temp_{args.output_name}/1080p60"
    video_name = "output_" + args.output_name
    config.output_file = video_name

    scene = ChampDePenteSimple(a_func=args.a_func, b_func=args.b_func, c_func=args.c_func)
    scene.render()
