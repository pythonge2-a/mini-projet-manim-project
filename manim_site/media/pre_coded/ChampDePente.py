from manim import *
import argparse
from manim import tempconfig
import numpy as np
from scipy.integrate import quad
import math

class ChampDePenteSimple(Scene):
    def construct(self):
        # Parametres pour les axes
        taille_x = 10  # Taille de l'axe x
        taille_y = 10  # Taille de l'axe y
        pas_x = 0.5  # Espacement sur l'axe x
        pas_y = 0.5  # Espacement sur l'axe y

        # Fonctions definies par l'utilisateur
        a = lambda t, y: 5  # Fonction a(t, y)
        b = lambda t, y: 3  # Fonction b(t, y)
        c = lambda t, y: np.tan(t)  # Fonction c(t, y)

        # Fonction pour calculer la pente : y'(t)
        def pente(x, y):
            denom = a(x, y)
            if abs(denom) < 1e-3:  # Eviter la division par zéro
                return 0
            return (c(x, y) - b(x, y) * y) / denom

        # Fonction pour determiner la couleur en fonction de la pente
        def couleur_pente(valeur_pente):
            norm_pente = np.clip(valeur_pente / 10, -1, 1)
            return interpolate_color(BLUE, RED, (norm_pente + 1) / 2)

        # Creation des axes
        axes = Axes(
            x_range=[-taille_x, taille_x, pas_x],
            y_range=[-taille_y, taille_y, pas_y],
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        )

        # Ajouter les labels aux axes
        axes_labels = axes.get_axis_labels(x_label="t", y_label="y")

        # Generation du champ de pente
        champ = VGroup()
        for x in np.arange(-taille_x, taille_x, pas_x):
            for y in np.arange(-taille_y, taille_y, pas_y):
                pente_value = pente(x, y)
                pente_value = np.clip(float(pente_value), -100, 100)  # Convertir en float et limiter les valeurs extremes
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