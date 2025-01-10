from manim import *
import argparse
from manim import tempconfig
import numpy as np
from scipy.integrate import quad
import math

class FunctionPlot(Scene):

    def construct(self):
        # Definition des paramètres
        equation = "10*np.exp(-10*x**2) + np.sin(x**4)"     # Equation a tracer
        graph_color = RED                     # Couleur du graphe (ex: BLUE, RED, GREEN)
        x_range = [-20, 20, 5]                # Plage pour l'axe X : [min, max, graduation]
        y_range = [-10, 10, 5]                # Plage pour l'axe Y : [min, max, graduation]

        # Configuration des axes
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            axis_config={"include_tip": True},
            x_axis_config={"numbers_to_include": range(int(x_range[0]), int(x_range[1]) + 1, x_range[2])},
            y_axis_config={"numbers_to_include": range(int(y_range[0]), int(y_range[1]) + 1, y_range[2])},
        )

        # Ajouter les labels des axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Dessiner la fonction
        graph = axes.plot(
            lambda x: eval(equation),  # Evaluer l'equation entree
            color=graph_color,
        )

        # Animation et rendu
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.wait(2)