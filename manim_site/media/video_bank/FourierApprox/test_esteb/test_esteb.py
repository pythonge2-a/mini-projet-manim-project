from manim import *
import numpy as np

from manim import *

class SineCosinePlane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        plane = Surface(
            lambda u, v: np.array([u, v, np.sin(u) * np.cos(v)]),  # z = sin(x) * cos(y)
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.5,
            color=BLUE
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes, plane)

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
        self.add(axes, plane)

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
        self.add(axes, plane)
