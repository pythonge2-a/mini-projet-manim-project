from manim import *
import argparse
from manim import tempconfig

class output(Scene):
    def __init__(self, dest_x=0, dest_y=0, **kwargs):
        super().__init__(**kwargs)
        self.dest_x = dest_x
        self.dest_y = dest_y

    def construct(self):
        dot = Dot(radius=0.1, color=WHITE, point=ORIGIN)
        self.add(dot)

        # AShow the destination coordinates
        text = Text(f"({self.dest_x}, {self.dest_y})", color=WHITE).next_to(dot, UP)
        self.add(text)

        # Move the dot to the destination coordinates
        self.play(dot.animate.move_to([self.dest_x, self.dest_y, 0]), run_time=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manim script with destination coordinates.")
    parser.add_argument("--x_coord", type=float, default=0, help="Destination x-coordinate")
    parser.add_argument("--y_coord", type=float, default=0, help="Destination y-coordinate")
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
    
    scene = output(dest_x=args.x_coord, dest_y=args.y_coord)
    scene.render()