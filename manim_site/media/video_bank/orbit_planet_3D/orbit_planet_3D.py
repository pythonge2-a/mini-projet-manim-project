from manim import *

class OrbitingPlanet(ThreeDScene):
    def construct(self):
        # Create axes
        axes = ThreeDAxes()

        # Create the central planet (larger)
        central_planet = Sphere(radius=0.8).move_to(ORIGIN)

        # Create the orbiting planet (smaller)
        orbiting_planet = Sphere(radius=0.25).move_to([5, 0, 0])

        # Add both planets to the scene
        self.add(axes, central_planet, orbiting_planet)

        # Define the orbit path for the smaller planet
        orbit_path = Circle(radius=5).rotate_about_origin(PI/2)

        # Animate the orbiting planet along the path
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(MoveAlongPath(orbiting_planet, orbit_path, run_time=8, rate_func=linear))
        self.wait()
