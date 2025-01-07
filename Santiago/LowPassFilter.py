from manim import *

class LowPassFilter(Scene):
    def construct(self):
        # 1. Titre
        title = Text("Filtre passe-bas").to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # 2. Supprimer le titre avant de créer les axes
        self.play(FadeOut(title))

        # 3. Text explicatif et formule
        txt = Text("La fonction de transfert d'un filtre").shift(UP*2)
        txt2 = Text(" passe-bas est donnée par :").next_to(txt, DOWN, buff=0.5)
        transfer_function_formula = MathTex(r"H(f) = \frac{Uout}{Uin} =\frac{K}{1 + j\frac{\omega}{\omega c}}").next_to(txt2, DOWN, buff=0.5)

        # Affichage du texte explicatif et de la formule
        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(transfer_function_formula))
        self.wait(2)

        self.play(FadeOut(txt), FadeOut(transfer_function_formula), FadeOut(txt2))

        # 4. Système d'axes
        axes = Axes(
            x_range=[0, 5, 1],  # Fréquence (kHz)
            y_range=[0, 1.2, 0.2],  # Amplitude de H(f)
            axis_config={"color": WHITE},  # Retire les labels ici
            x_axis_config={"include_tip": True},  # Pas de label ici non plus
            y_axis_config={"include_tip": True}
        ).add_coordinates()

        axes_labels = axes.get_axis_labels(x_label="f (kHz)", y_label="|H(f)|")  # Ajouter les labels manuellement
        self.play(Create(axes), Write(axes_labels))

        # 5. Fonction de transfert H(f) = 1 / sqrt(1 + (f/fc)^2)
        fc = 2  # Fréquence de coupure en kHz
        transfer_function = axes.plot(
            lambda f: 1 / (1 + (f / fc) ** 2) ** 0.5,
            color=BLUE,
        )
        self.play(Create(transfer_function), run_time=2)
        self.wait(1)

        # 6. Annotation de fc
        critical_freq = Dot(axes.coords_to_point(fc, 0.707), color=RED)
        self.play(FadeIn(critical_freq))
        self.play(Indicate(critical_freq))
        annotation = MathTex("f_c").next_to(critical_freq, DOWN)
        self.play(Write(annotation))
        self.wait(2)

        # 7. Fin
        # On supprime définitivement tous les objets avant la fin
        self.play(FadeOut(transfer_function, critical_freq, annotation, axes, axes_labels))