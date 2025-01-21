from manim import *


class output(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(RED, opacity=0.8)  # set the color and transparency
        circle.set_stroke(RED, width=10)
        self.play(Create(circle))  # show the circle on screen