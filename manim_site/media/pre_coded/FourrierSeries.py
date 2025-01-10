from manim import *
import argparse
from manim import tempconfig
import numpy as np
from scipy.integrate import quad
import math

class FourierSeries(Scene):
    def construct(self):
        # Variable pour selectionner la fonction (square, triangle, toothsaw) et le nombre de termes dans l'approximation
        function_type = "square"  
        number_of_terms = 10

        # Ajuster les axes
        axes = Axes(
            x_range=[0, 6 * PI, PI / 4],  
            y_range=[-1.5, 1.5, 0.5],
            tips=False
        )

        # Definir les séries de Fourier pour chaque fonction
        def fourier_series(x, n_terms=10):
            result = 0
            if function_type == "square":
                for n in range(1, n_terms + 1):
                    if n % 2 != 0:
                        result += (4 / (PI * n)) * np.sin(n * x)
            elif function_type == "triangle":
                for n in range(1, n_terms + 1):
                    result += (8 / (PI**2 * n**2)) * (-1)**((n-1)//2) * np.sin(n * x)
            elif function_type == "toothsaw":
                for n in range(1, n_terms + 1):
                    result += (2 / (PI * n)) * (-1)**(n+1) * np.sin(n * x)
            return result

        # Placer le texte en haut au centre
        wave_label = Text(f"{function_type.capitalize()} Wave, n = {number_of_terms}").to_edge(UP)

        self.play(Create(axes), Write(wave_label))

        # Initialiser l'attribut self.current_term
        self.current_term = number_of_terms

        series_graph = always_redraw(lambda: axes.plot(lambda x: fourier_series(x, n_terms=self.current_term), color=RED))

        self.add(series_graph)

        for n in range(1, 11):
            self.current_term = n
            self.wait(0.5)

        self.wait()