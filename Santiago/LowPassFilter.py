from manim import *
import math

class LowPassFilter(Scene):
    def construct(self):
        # Constantes globales
        f_start, f_end = 10, 1e6  # Fréquences de départ et de fin pour l'axe (valeur limite ajustée)
        PI = math.pi

        # 1. Titre
        title = Text("Filtre du premier Ordre", font_size=48).move_to(ORIGIN)
        self.play(Write(title))
        self.wait(2)

        self.play(FadeOut(title))
        self.wait(1)

        # 2. Text explicatif et formule
        txt = Text("La fonction de transfert d'un filtre").shift(UP*2)
        txt2 = Text(" est donnée par :").next_to(txt, DOWN, buff=0.5)
        transfer_function = MathTex(r"H(f) = \frac{U_{out}}{U_{in}} =\frac{Z_2}{Z_1 + Z_2}").next_to(txt2, DOWN, buff=0.5)

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

        # 5. Résultat de la fonction de transfert
        txt = Text("Nous avons donc pour H(f):", font_size=30).move_to(ORIGIN + UP*2)
        transfer_function = MathTex(r"H(f) = \frac{Z_C}{Z_C + R}", font_size=30).next_to(txt, DOWN, buff=0.5)
        txt2 = Text("Sachant que:", font_size=30)
        txt3 = MathTex(r"Z_C = \frac{1}{j\omega C}", font_size=30)

        txt2.align_to(txt, LEFT)  
        txt3.next_to(txt2, RIGHT, buff=1)     

        txt4 = Text("Nous obtenons:", font_size=30)
        result = MathTex(r"H(f) = \frac{1}{1 + j\omega RC}", font_size=30)

        txt4.align_to(txt2, LEFT)  
        txt4.next_to(txt2, DOWN, buff=1)
        result.next_to(txt4, RIGHT)  

        self.play(Write(txt))
        self.play(Write(transfer_function))
        self.play(Write(txt2), Write(txt3))  
        self.play(Write(txt4), Write(result))
        
        self.wait(2)

        self.play(FadeOut(txt, transfer_function, txt2, txt3, txt4, result))

        # 6. Trouver la pulsation

        txt = Text("Trouvons la pulsation de coupure", font_size=30).move_to(ORIGIN + UP*2)
        txt2 = Text("en annulant la partie imaginaire Im(H(f)) = 0 :", font_size=30).next_to(txt, DOWN, buff=0.5)
        txt3 = Text("On trouve :", font_size=30).next_to(txt2, DOWN, buff=0.5)
        pulsation = MathTex(r"\omega_c = \frac{1}{RC}", font_size=35).next_to(txt3)

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(txt3))
        self.play(Write(pulsation))

        self.wait(2)

        self.play(FadeOut(txt, txt2, txt3, pulsation))

        # 7. Calcul de la fréquence de coupure pour 1 kHz
        R = 159
        C = 0.000001
        wc = 1 / (R * C)
        fc = wc / (2 * PI)

        txt = Text("Calculons la fréquence de coupure pour R = 159 Ohm et C = 1 \u00b5F", font_size=30).move_to(ORIGIN + UP*2)
        txt2 = Text("On trouve :", font_size=30).next_to(txt, DOWN, buff=2)

        self.wait(1)

        freq = MathTex(fr"f_c = \frac{{\omega_c}}{{2 * pi}} = \frac{{1}}{{2 * pi * RC}} = {fc:.2f} Hz", font_size=35).next_to(txt2)

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(freq))

        self.wait(2)

        self.play(FadeOut(txt, txt2, freq))

        # 6. Système d'axes : Magnitude
        magnitude_axes = Axes(
            x_range=[0, 5, 1],  # Fréquence (kHz)
            y_range=[-40, 5, 5],  # Amplitude de H(f) en dB
            axis_config={"color": WHITE},
            x_axis_config={"include_tip": True, "label_direction": DOWN},
            y_axis_config={"include_tip": True, "label_direction": LEFT}
        ).add_coordinates()

        magnitude_labels = magnitude_axes.get_axis_labels(
            x_label="f (kHz)",
            y_label="dBgit "
        )
        self.play(Create(magnitude_axes), Write(magnitude_labels))

        # 7. Tracé de la magnitude
        fc = 1  # Fréquence de coupure en kHz
        magnitude_plot = magnitude_axes.plot(
            lambda f: -20 * math.log10(math.sqrt(1 + (f / fc)**2)),  # Formule correcte pour la magnitude en dB
            color=BLUE,
            x_range=[0.1, 5]
        )
        self.play(Create(magnitude_plot), run_time=2)

        # 8. Indication de la fréquence de coupure
        critical_freq_magnitude = Dot(
            magnitude_axes.coords_to_point(fc, -3), color=RED
        )  # À -3 dB pour f_c
        self.play(FadeIn(critical_freq_magnitude))
        self.play(Indicate(critical_freq_magnitude))
        annotation_magnitude = MathTex("f_c", font_size=30).next_to(
            critical_freq_magnitude, DOWN
        )
        self.play(Write(annotation_magnitude))
        self.wait(2)

        # Fin de l'animation
        self.play(FadeOut(magnitude_axes, magnitude_labels, magnitude_plot, critical_freq_magnitude, annotation_magnitude))
        