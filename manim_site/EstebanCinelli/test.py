
from manim import *
import numpy as np
from scipy.integrate import quad
import math

class ChampDePenteSimple(Scene):
    def construct(self):
        # Paramètres pour les axes
        taille_x = 10  # Taille de l'axe x
        taille_y = 10  # Taille de l'axe y
        pas_x = 0.5  # Espacement sur l'axe x
        pas_y = 0.5  # Espacement sur l'axe y

        # Fonctions définies par l'utilisateur
        a = lambda t, y: 5  # Fonction a(t, y)
        b = lambda t, y: 3  # Fonction b(t, y)
        c = lambda t, y: np.tan(t)  # Fonction c(t, y)

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


class FirstHarmonicAnimation(Scene):
    def construct(self):
        # Paramètres utilisateur
        amplitude = 24          # Amplitude A
        pulsation = 6     # Pulsation omega
        dephasage = PI     # Déphasage phi
        num_periods = 2        # Nombre de périodes à afficher

        # Calcul des bornes des axes
        period = 2 * PI / pulsation  # Période fondamentale
        x_min = -num_periods * period
        x_max = num_periods * period
        x_step = period / 2          # Espacement des ticks sur x
        y_min = -amplitude
        y_max = amplitude
        y_step = amplitude / 2       # Espacement des ticks sur y

        # Création des axes adaptés aux paramètres
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

        # Fonction trigonométrique : y = A * cos(omega * t + phi)
        trig_func = axes.plot(
            lambda x: amplitude * np.cos(pulsation * x + dephasage),
            color=BLUE
        )

        # Affichage de l'équation
        equation = MathTex("y = A \\cos(\\omega t + \\phi)")
        equation.to_corner(UP)

        # Animation du tracé de la fonction
        self.play(Create(axes))
        self.play(Create(trig_func))
        self.play(Write(equation))
        self.wait(2)


class FunctionPlot(Scene):

    def construct(self):
        # Définition des paramètres
        equation = "np.exp(-x)*np.cos(x)"     # Fonction (en notation Python, ex: "x**2", "sin(x)")
        graph_color = RED          # Couleur du graphe (ex: BLUE, RED, GREEN)
        x_range = [-20, 20, 5]      # Plage pour l'axe X : [min, max, graduation]
        y_range = [-10, 10, 5]      # Plage pour l'axe Y : [min, max, graduation]

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
            lambda x: eval(equation),  # Évaluer l'équation entrée
            color=graph_color,
        )

        # Animation et rendu
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.wait(2)


class GeometricTransform(Scene):
    def construct(self):
        # Définition des paramètres
        shape_type = "triangle"  # "circle", "square", "triangle"
        transformation = "scaling"  # "rotation", "translation", "scaling"
        param = 0.1  # Angle pour rotation, facteur pour scaling, vecteur pour translation

        # Création de la figure
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
        # Variable pour sélectionner la fonction (square, triangle, toothsaw) et le nombre de termes dans l'approximation
        function_type = "square"  
        number_of_terms = 10

        # Ajuster les axes
        axes = Axes(
            x_range=[0, 6 * PI, PI / 4],  
            y_range=[-1.5, 1.5, 0.5],
            tips=False
        )

        # Définir les séries de Fourier pour chaque fonction
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
        # Matrice et opération définies par l'utilisateur
        matrix = [[2, 1, 8, 20], [1, 3, 7, 5], [1, 2, 4, 3], [1, 4, 6, 12]]  # Matrice carrée
        operation = "inverse"  # "inverse", "transpose", "determinant"

        # Formattage de la matrice initiale
        formatted_matrix = self.format_matrix(matrix)
        matrix_manim = Matrix(formatted_matrix).scale(0.8).set_color(BLUE)
        matrix_label = Text("Matrice initiale").next_to(matrix_manim, UP)
        self.play(Write(matrix_label), Write(matrix_manim))

        # Appliquer l'opération
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
            determinant_text = Text(f"Déterminant = {determinant_value:.3f}").scale(0.8)
            determinant_text.next_to(matrix_manim, DOWN)
            self.play(Write(determinant_text))
            self.wait()
            return
        else:
            error_text = Text("Opération inconnue").set_color(RED)
            error_text.next_to(matrix_manim, DOWN)
            self.play(Write(error_text))
            self.wait()
            return

        # Animation de la transformation
        result_manim = Matrix(formatted_result).scale(0.8).set_color(GREEN)
        result_label = Text("Résultat").next_to(result_manim, UP)

        self.play(Transform(matrix_manim, result_manim), Transform(matrix_label, result_label))
        self.wait()

    def inverse(self, matrix):
        """Calcul l'inverse d'une matrice carrée."""
        import numpy as np
        np_matrix = np.array(matrix)
        if np.linalg.det(np_matrix) == 0:
            raise ValueError("La matrice est singulière et n'a pas d'inverse.")
        return np.linalg.inv(np_matrix).tolist()

    def transpose(self, matrix):
        """Retourne la transposée d'une matrice."""
        return list(map(list, zip(*matrix)))

    def determinant(self, matrix):
        """Retourne le déterminant d'une matrice carrée."""
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


class IntegralCalculator(Scene):
    def construct(self):
        # Fonction à intégrer : ln(x)
        func = lambda x: (x-1)  # Vous pouvez modifier cette fonction

        # Intervalle [a, b] pour l'intégrale
        a, b = 2, 10  # Exemple d'un intervalle invalide pour ln(x)
        
        # Vérification de la validité de la fonction sur l'intervalle
        if not self.is_valid_function(func, a, b):
            self.handle_invalid_function()
            return  # Quitter si la fonction est invalide

        # Ajuster l'intervalle des axes en fonction de la fonction et des limites
        x_min = a
        x_max = b
        try:
            y_min = func(x_min)
            y_max = func(x_max)
        except Exception as e:
            self.handle_invalid_function()
            return

        axes = Axes(
            x_range=[x_min, x_max, (x_max - x_min) / 5],  # ajuster l'échelle de x
            y_range=[y_min, y_max, (y_max - y_min) / 5],  # ajuster l'échelle de y
            axis_config={"color": BLUE}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))

        # Tracer la courbe
        curve = axes.plot(func, color=YELLOW)
        self.play(Create(curve))

        # Affichage de l'aire sous la courbe
        area = axes.get_area(curve, x_range=[a, b], color=GREEN, opacity=0.5)
        self.play(FadeIn(area))

        # Affichage des labels a et b
        a_label = MathTex("a").next_to(axes.c2p(a, 0), DOWN)
        b_label = MathTex("b").next_to(axes.c2p(b, 0), DOWN)
        self.play(Write(a_label), Write(b_label))

        self.wait(1)

        # Calcul de l'intégrale
        integral_result = self.calculate_integral(func, a, b)
        if integral_result is None:
            self.handle_invalid_integral()
            return

        result_text = MathTex(f"{integral_result:.2f}").scale(1.5).to_edge(UP)
        self.play(Write(result_text))
        self.wait(2)

        # Nettoyage
        self.play(FadeOut(result_text), FadeOut(area), FadeOut(curve), FadeOut(a_label), FadeOut(b_label))
        self.wait(1)

    def calculate_integral(self, func, a, b):
        try:
            result, _ = quad(func, a, b)
            if np.isinf(result) or np.isnan(result):
                return None  # Si l'intégrale est infinie ou indéfinie
            return result
        except Exception as e:
            return None  # En cas d'erreur dans le calcul de l'intégrale

    def is_valid_function(self, func, a, b):
        # Vérification si la fonction est définie et valable sur l'intervalle
        try:
            # Tester si la fonction est définie à un ou plusieurs points de l'intervalle
            for x in np.linspace(a, b, 100):
                func(x)  # Vérifie si la fonction renvoie une valeur valide
            return True
        except Exception:
            return False  # Si une exception est levée, la fonction est invalide

    def handle_invalid_function(self):
        error_message = MathTex("La fonction n'est pas définie sur l'intervalle").scale(1.5).to_edge(UP)
        self.play(Write(error_message))
        self.wait(2)
        self.play(FadeOut(error_message))

    def handle_invalid_integral(self):
        error_message = MathTex("L'intégrale est divergente ou indéfinie").scale(1.5).to_edge(UP)
        self.play(Write(error_message))
        self.wait(2)
        self.play(FadeOut(error_message))


class Integral(Scene):
    def construct(self):
        # Title
        title = Text("Integral")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Explanation 1
        explanation1 = Text("An integral is a fundamental concept in calculus.").scale(0.8).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(1)
        self.play(FadeOut(explanation1))
        
        # Explanation 2
        explanation3 = Text("The integral of a function f(x) from a to b is written as:").scale(0.5).to_edge(UP)
        self.play(Write(explanation3))
        
        # Equation
        equation = MathTex(r"\int_a^b f(x) \, dx").scale(2)
        self.play(Write(equation))
        self.wait(2)
        self.play(FadeOut(explanation3))
        self.play(FadeOut(equation))
        
        # Explanation 4
        explanation4 = Text("It is used to find the area under the curve of f(x) between a and b.").scale(0.5).to_edge(UP)
        self.play(Write(explanation4))
        self.play(FadeOut(explanation4))
        
        self.wait(1)

        title = MathTex(r"S =\int_a^b f(x) \, dx").to_edge(UP)
        self.play(Write(title))
        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels))
        
        curve = axes.plot(lambda x: 0.1 * x**2, color=YELLOW)
        self.play(Create(curve))
        
        area = axes.get_area(curve, x_range=[2, 8], color=[GREEN, BLUE])
        self.play(FadeIn(area))
        
        a_label = MathTex("a").next_to(axes.c2p(2, 0), DOWN)
        b_label = MathTex("b").next_to(axes.c2p(8, 0), DOWN)
        self.play(Write(a_label), Write(b_label))
        
        self.wait(1)

