
from manim import *
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


class OrbitePlanetes(Scene):
    def construct(self):
        # Parametres modifiables par l'utilisateur
        demi_grand_axe = 5   # en unites de Manim
        excentricite = 0.9   # entre 0 et 1
        periode_orbitale = 10  # en secondes

        # Calcul des parametres de l'ellipse
        c = demi_grand_axe * excentricite  # distance focale
        a = demi_grand_axe  # semi-grand axe
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
            MoveAlongPath(planete, orbite, rate_func=linear, run_time=periode_orbitale)
        )