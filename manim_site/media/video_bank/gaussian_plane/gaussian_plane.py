from manim import *
import numpy as np


class GaussianPlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        plane = Surface(
            lambda u, v: np.array([u, v, np.exp(-u**2 - v**2)]),  # z = e^(-x^2 - y^2)
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.5,
            color=GREEN
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes)
        self.play(Create(plane))
        self.wait(3)

