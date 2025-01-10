from manim import *
import argparse
from manim import tempconfig
import numpy as np
import math

class OrbitePlanetes(Scene):
    def __init__(self, demi_grand_axe=0, excentricite=0, periode_orbitale = 0, **kwargs):
        super().__init__(**kwargs)
        self.demi_grand_axe = demi_grand_axe
        self.excentricite = excentricite
        self.periode_orbitale = periode_orbitale

    def construct(self):
        # Calcul des parametres de l'ellipse
        c = self.demi_grand_axe * self.excentricite  # distance focale
        a = self.demi_grand_axe  # semi-grand axe
        b = np.sqrt(a**2 - c**2)  # semi-petit axe

        # Creation de l'orbite elliptique
        orbite = Ellipse(width=2*a, height=2*b)
        orbite.set_color(WHITE)

        # Creation du Soleil
        soleil = Dot(ORIGIN, color=YELLOW)

        # Creation de la planète
        planete = Dot(orbite.point_at_angle(0), color=BLUE)

        # Ajout des objets à la scene
        self.add(orbite, soleil, planete)


        self.play(
            MoveAlongPath(planete, orbite, rate_func=linear, run_time=self.periode_orbitale)
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manim script to visualize ellipse trajectory of a planet")
    args = parser.parse_args()
    config.media_width = "100%"
    config.verbosity = "WARNING"
    config.quality = "high_quality"
    config.frame_rate = 60
    config.background_color = "#1e1e1e"
    config.video_dir = f"media/videos/temp_{args.output_name}/1080p60"
    video_name = "output_" + args.output_name
    config.output_file = video_name