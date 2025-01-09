
from manim import *
import numpy as np
from scipy.integrate import quad
import math

class FirstHarmonicAnimation(Scene):
    def construct(self):
        # Paramètres utilisateur
        amplitude = 24          # Amplitude A
        pulsation = 6     # Pulsation omega
        dephasage = PI     # Dephasage phi
        num_periods = 2        # Nombre de periodes a afficher

        # Calcul des bornes des axes
        period = 2 * PI / pulsation  # Periode fondamentale
        x_min = -num_periods * period
        x_max = num_periods * period
        x_step = period / 2          # Espacement des ticks sur x
        y_min = -amplitude
        y_max = amplitude
        y_step = amplitude / 2       # Espacement des ticks sur y

        # Creation des axes adaptes aux parametres
        axes = Axes(
            x_range=[x_min, x_max, x_step],
            y_range=[y_min, y_max, y_step],
            tips=True,
            axis_config={"font_size": 24},
        )

        # Ajout des labels en LaTeX pour l'axe des x
        x_ticks = {
            -num_periods * period: MathTex(f"-{num_periods}T"),
            0: MathTex("0"),
            num_periods * period: MathTex(f"{num_periods}T")
        }
        axes.x_axis.add_labels(x_ticks)

        # Fonction trigonometrique : y = A * cos(omega * t + phi)
        trig_func = axes.plot(
            lambda x: amplitude * np.cos(pulsation * x + dephasage),
            color=BLUE
        )

        # Affichage de l'equation
        equation = MathTex("y = A \\cos(\\omega t + \\phi)")
        equation.to_corner(UP)

        # Animation du trace de la fonction
        self.play(Create(axes))
        self.play(Create(trig_func))
        self.play(Write(equation))
        self.wait(2)


class GeometricTransform(Scene):
    def construct(self):
        # Definition des parametres
        shape_type = "triangle"  # "circle", "square", "triangle"
        transformation = "scaling"  # "rotation", "translation", "scaling"
        param = 0.1  # Angle pour rotation, facteur pour scaling, vecteur pour translation

        # Creation de la figure
        if shape_type == "circle":
            shape = Circle()
        elif shape_type == "square":
            shape = Square()
        elif shape_type == "triangle":
            shape = Triangle()

        shape.set_color(BLUE)
        self.play(Create(shape))

        # Application de la transformation
        if transformation == "rotation":
            self.play(Rotate(shape, angle=param * DEGREES))
        elif transformation == "translation":
            self.play(shape.animate.shift(RIGHT * param))
        elif transformation == "scaling":
            self.play(shape.animate.scale(param))

        self.wait()


## Code test 


class MatrixTransformation(Scene):
    def construct(self):
        # Matrice et operation definies par l'utilisateur
        matrix = [[2, 1, 8, 20], [1, 3, 7, 5], [1, 2, 4, 3], [1, 4, 6, 12]]  # Matrice carree
        operation = "inverse"  # "inverse", "transpose", "determinant"

        # Formattage de la matrice initiale
        formatted_matrix = self.format_matrix(matrix)
        matrix_manim = Matrix(formatted_matrix).scale(0.8).set_color(BLUE)
        matrix_label = Text("Matrice initiale").next_to(matrix_manim, UP)
        self.play(Write(matrix_label), Write(matrix_manim))

        # Appliquer l'operation
        if operation == "inverse":
            try:
                result_matrix = self.inverse(matrix)
                formatted_result = self.format_matrix(result_matrix)
            except ValueError as e:
                error_text = Text(str(e)).set_color(RED)
                error_text.next_to(matrix_manim, DOWN)
                self.play(Write(error_text))
                self.wait()
                return
        elif operation == "transpose":
            result_matrix = self.transpose(matrix)
            formatted_result = self.format_matrix(result_matrix)
        elif operation == "determinant":
            determinant_value = self.determinant(matrix)
            determinant_text = Text(f"Determinant = {determinant_value:.3f}").scale(0.8)
            determinant_text.next_to(matrix_manim, DOWN)
            self.play(Write(determinant_text))
            self.wait()
            return
        else:
            error_text = Text("Operation inconnue").set_color(RED)
            error_text.next_to(matrix_manim, DOWN)
            self.play(Write(error_text))
            self.wait()
            return

        # Animation de la transformation
        result_manim = Matrix(formatted_result).scale(0.8).set_color(GREEN)
        result_label = Text("Resultat").next_to(result_manim, UP)

        self.play(Transform(matrix_manim, result_manim), Transform(matrix_label, result_label))
        self.wait()

    def inverse(self, matrix):
        """Calcul l'inverse d'une matrice carree."""
        import numpy as np
        np_matrix = np.array(matrix)
        if np.linalg.det(np_matrix) == 0:
            raise ValueError("La matrice est singuliere et n'a pas d'inverse.")
        return np.linalg.inv(np_matrix).tolist()

    def transpose(self, matrix):
        """Retourne la transposee d'une matrice."""
        return list(map(list, zip(*matrix)))

    def determinant(self, matrix):
        """Retourne le determinant d'une matrice carrée."""
        import numpy as np
        np_matrix = np.array(matrix)
        return np.linalg.det(np_matrix)

    def format_matrix(self, matrix):
        """
        Formatte une matrice pour limiter les nombres à 3 chiffres significatifs.
        :param matrix: Liste de listes représentant la matrice.
        :return: Matrice formatée avec des chaînes de caractères.
        """
        formatted = []
        for row in matrix:
            formatted_row = [f"{value:.3g}" for value in row]
            formatted.append(formatted_row)
        return formatted
