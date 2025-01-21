from manim import *
import numpy as np


class SineProductPlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        plane = Surface(
            lambda u, v: np.array([u, v, np.sin(u * v)]),  # z = sin(xy)
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.5,
            color=RED
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes)
        self.play(Create(plane))
        self.wait(3)

