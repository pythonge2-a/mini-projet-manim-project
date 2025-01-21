from manim import *
import argparse
import numpy as np

class FourierSeries(Scene):
    def __init__(self, function_type, number_of_terms, **kwargs):
        super().__init__(**kwargs)
        self.function_type = function_type
        self.number_of_terms = number_of_terms

    def construct(self):
        # Ajuster les axes
        axes = Axes(
            x_range=[0, 6 * PI, PI / 4],  
            y_range=[-1.5, 1.5, 0.5],
            tips=False
        )

        # Définir les séries de Fourier pour chaque fonction
        def fourier_series(x, n_terms=10):
            result = 0
            if self.function_type == "square":
                for n in range(1, n_terms + 1):
                    if n % 2 != 0:
                        result += (4 / (PI * n)) * np.sin(n * x)
            elif self.function_type == "triangle":
                for n in range(1, n_terms + 1):
                    result += (8 / (PI**2 * n**2)) * (-1)**((n-1)//2) * np.sin(n * x)
            elif self.function_type == "toothsaw":
                for n in range(1, n_terms + 1):
                    result += (2 / (PI * n)) * (-1)**(n+1) * np.sin(n * x)
            return result

        # Placer le texte en haut au centre
        wave_label = Text(f"{self.function_type.capitalize()} Wave, n = {self.number_of_terms}").to_edge(UP)

        self.play(Create(axes), Write(wave_label))

        series_graph = always_redraw(lambda: axes.plot(lambda x: fourier_series(x, n_terms=self.number_of_terms), color=RED))

        self.add(series_graph)
        self.wait(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manim script for plotting Fourier series.")
    parser.add_argument("--function_type", type=str, required=True, choices=["square", "triangle", "toothsaw"], help="Type of the function (square, triangle, toothsaw)")
    parser.add_argument("--number_of_terms", type=int, required=True, help="Number of terms in the Fourier series")
    parser.add_argument("--output_name", type=str, required=True, help="Output filename")
    args = parser.parse_args()

    config.media_width = "100%"
    config.verbosity = "WARNING"
    config.quality = "high_quality"
    config.frame_rate = 60
    config.background_color = "#1e1e1e"
    config.video_dir = f"media/videos/temp_{args.output_name}/1080p60"
    video_name = "output_" + args.output_name
    config.output_file = video_name

    scene = FourierSeries(function_type=args.function_type, number_of_terms=args.number_of_terms)
    scene.render()
