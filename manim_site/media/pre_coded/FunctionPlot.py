from manim import *
import argparse
import numpy as np

class FunctionPlot(Scene):
    def __init__(self, equation, graph_color, x_range, y_range, **kwargs):
        super().__init__(**kwargs)
        self.equation = equation
        self.graph_color = graph_color
        self.x_range = [float(v) for v in x_range.split(',')]
        self.y_range = [float(v) for v in y_range.split(',')]

    def construct(self):
        # Configuration des axes
        axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            axis_config={"include_tip": True},
            x_axis_config={"numbers_to_include": range(int(self.x_range[0]), int(self.x_range[1]) + 1, int(self.x_range[2]))},
            y_axis_config={"numbers_to_include": range(int(self.y_range[0]), int(self.y_range[1]) + 1, int(self.y_range[2]))},
        )

        # Ajouter les labels des axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Dessiner la fonction
        graph = axes.plot(
            lambda x: eval(self.equation),  # Evaluer l'equation entree
            color=self.graph_color,
        )

        # Animation et rendu
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph))
        self.wait(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manim script for plotting a function.")
    parser.add_argument("--equation", type=str, required=True, help="Mathematical equation to plot")
    parser.add_argument("--graph_color", type=str, required=True, help="Color of the graph (e.g., RED, BLUE, GREEN)")
    parser.add_argument("--x_range", type=str, required=True, help="Range for x-axis in format 'min,max,step'")
    parser.add_argument("--y_range", type=str, required=True, help="Range for y-axis in format 'min,max,step'")
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

    scene = FunctionPlot(equation=args.equation, graph_color=args.graph_color, x_range=args.x_range, y_range=args.y_range)
    scene.render()
