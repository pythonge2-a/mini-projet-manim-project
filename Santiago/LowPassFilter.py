from manim import *
import math

class LowPassFilter(Scene):
    def construct(self):
        # Constantes globales
        f_start, f_end = 10, 1e6  # Fréquences de départ et de fin pour l'axe (valeur limite ajustée)
        PI = math.pi

        # Utilitaires pour générer les textes
        def create_text(content, position=ORIGIN, font_size=40):
            return Text(content, font_size=font_size).move_to(position)

        def create_latex(content, position=ORIGIN, font_size=40):
            return MathTex(content, font_size=font_size).move_to(position)

        # 1. Titre
        title = create_text("Filtre du premier Ordre", font_size=60)
        self.play(Write(title))
        self.wait(2)

        self.play(FadeOut(title))
        
        # 2. Texte explicatif et formule
        txt = create_text("La fonction de transfert d'un filtre", position=UP * 2)
        txt2 = create_text("est donnée par :", position=UP * 1)
        transfer_function = create_latex(r"H(f) = \frac{U_{out}}{U_{in}} =\frac{Z_2}{Z_1 + Z_2}", position=DOWN * 0.5) 

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(transfer_function))
        self.wait(1)

        self.play(FadeOut(txt, txt2, transfer_function))

        # 3. Insertion de l'image
        txt = create_text("Prenons un cas simple :", position=UP * 2)
        image = ImageMobject("media/images/LowPassFilter.PNG").scale(2).shift(DOWN * 0.5)

        self.play(Write(txt))
        self.play(FadeIn(image))
        self.wait(1)
        self.play(FadeOut(txt, image))

        # 4. Résultat de la fonction de transfert
        txt = create_text("Nous avons donc pour H(f):", position=UP * 2)
        transfer_function = create_latex(r"H(f) = \frac{Z_C}{Z_C + R}", position=UP * 1)
        txt2 = create_text("Sachant que:", font_size=30).align_to(txt, LEFT).next_to(transfer_function, DOWN, buff=1)
        txt3 = create_latex(r"Z_C = \frac{1}{j\omega C}", font_size=30).next_to(txt2, RIGHT, buff=1)
        txt4 = create_text("Nous obtenons:", font_size=30).align_to(txt2, LEFT).next_to(txt2, DOWN, buff=1)
        result = create_latex(r"H(f) = \frac{1}{1 + j\omega RC}", font_size=30).next_to(txt4)

        self.play(Write(txt), Write(transfer_function))
        self.wait(1)
        self.play(Write(txt2), Write(txt3))
        self.wait(1)
        self.play(Write(txt4), Write(result))
        self.wait(2)
        self.play(FadeOut(txt, transfer_function, txt2, txt3, txt4, result))

        # 5. Trouver la pulsation
        txt = create_text("Trouvons la pulsation de coupure", font_size=30, position=UP * 2)
        txt2 = create_text("en annulant la partie imaginaire Im(H(f)) = 0 :", font_size=30, position=UP * 1.5)
        txt3 = create_text("On trouve :", font_size=30, position=UP * 0.5)
        pulsation = create_latex(r"\omega_c = \frac{1}{RC}", position=DOWN * 0.5)

        self.play(Write(txt), Write(txt2))
        self.play(Write(txt3))
        self.play(Write(pulsation))
        self.wait(2)
        self.play(FadeOut(txt, txt2, txt3, pulsation))

        # 6. Calcul de la fréquence de coupure
        R = 159
        C = 1e-6
        wc = 1 / (R * C)
        fc = wc / (2 * PI)

        txt = create_text("Calculons la fréquence de coupure pour R = 159 Ohm et C = 1 \u00b5F",font_size=30, position=UP * 2)
        txt2 = create_text("On trouve :",font_size=30, position=UP * 1)
        freq = create_latex(fr"f_c = \frac{{\omega_c}}{{2\pi}} = \frac{{1}}{{2\pi RC}} = {fc:.2f} Hz", position=ORIGIN)

        self.play(Write(txt))
        self.play(Write(txt2))
        self.play(Write(freq))
        self.wait(2)
        self.play(FadeOut(txt, txt2, freq))

        # 7. Système d'axes et tracé de la magnitude
        magnitude_axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-40, 5, 5],
            axis_config={"color": WHITE},
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True}
        ).add_coordinates()

        magnitude_labels = magnitude_axes.get_axis_labels(x_label="f (kHz)", y_label="dB")
        self.play(Create(magnitude_axes), Write(magnitude_labels))

        # Tracé
        magnitude_plot = magnitude_axes.plot(
            lambda f: -20 * math.log10(math.sqrt(1 + (f / 1)**2)),
            color=BLUE,
            x_range=[0.1, 5]
        )
        self.play(Create(magnitude_plot), run_time=2)

        # Indication de la fréquence de coupure
        critical_freq_magnitude = Dot(magnitude_axes.coords_to_point(1, -3), color=RED)
        annotation_magnitude = create_latex("f_c").next_to(critical_freq_magnitude, DOWN)
        self.play(FadeIn(critical_freq_magnitude), Write(annotation_magnitude))
        self.wait(2)
        
        # Conclusion
        self.play(FadeOut(magnitude_axes, magnitude_labels, magnitude_plot, critical_freq_magnitude, annotation_magnitude))
