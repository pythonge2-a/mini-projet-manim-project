from manim import *

class LowPassFilter(Scene):
    def construct(self):
        # 1. Titre
        title = Text("Filtre du premier Ordre", font_size=48).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)

        self.play(FadeOut(title))
        self.wait(1)

        # 2. Text explicatif et formule
        txt = Text("La fonction de transfert d'un filtre").shift(UP*2)
        txt2 = Text(" est donnée par :").next_to(txt, DOWN, buff=0.5)
        transfer_function = MathTex(r"H(f) = \frac{Uout}{Uin} =\frac{Z2}{Z1 + Z2}").next_to(txt2, DOWN, buff=0.5)

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(transfer_function))
        self.wait(1)

        self.play(FadeOut(txt, txt2, transfer_function))
        self.wait(1)

        # 4. Insertion de l'image
        txt = Text("Prenons un cas simple :").shift(UP*2)
        image = ImageMobject("media/images/LowPassFilter.PNG").next_to(txt, DOWN, buff=1.5)
        image.scale(2)

        self.play(Write(txt))
        self.play(FadeIn(image))

        self.wait(1)
        self.play(FadeOut(txt, image))

        # 5. Résultat
        txt = Text("Nous avons donc pour la H(f):", font_size=30).move_to(ORIGIN + UP*2)
        transfer_function = MathTex(r"H(f) = \frac{ZC}{ZC + R}", font_size=30).next_to(txt, DOWN, buff=0.5)
        txt2 = Text("Sachant que:", font_size=30)
        txt3 = MathTex(r"ZC = \frac{1}{j\omega C}", font_size=30)

        txt2.align_to(txt, LEFT)  
        txt3.next_to(txt2, RIGHT, buff=1)     

        txt4 = Text("Nous obtenons:", font_size=30)
        result = MathTex(r"H(f) = \frac{1}{1 + j\omega RC}")

        txt4.align_to(txt2, LEFT)  
        txt4.next_to(txt2, DOWN, buff=1)
        result.next_to(txt4, RIGHT)  

        # Animation des objets
        self.play(Write(txt))
        self.play(Write(transfer_function))
        self.play(Write(txt2), Write(txt3))  
        self.play(Write(txt4), Write(result))
        
        self.wait(1)

        self.play(FadeOut(txt, transfer_function, txt2, txt3, txt4, result))

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