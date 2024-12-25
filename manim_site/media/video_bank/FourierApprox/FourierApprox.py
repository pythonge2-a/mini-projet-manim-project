# manim -pqh .\FourierApprox.py

from manim import *
import numpy as np

class output(Scene):
    def construct(self):
        # Create axes with specified x and y ranges
        a = Axes(x_range=[0, 20], y_range=[-2, 2])

        # Number of harmonics to use in the Fourier approximation
        n_harmonics = 10

        # Function to generate the sum of sinusoids for a square wave signal
        def generate_square_wave(n_harmonics):
            return lambda x: sum((4/np.pi) * (1/n) * np.sin(n * x) for n in np.arange(1, n_harmonics * 2, 2))

        # Create the signals for each number of harmonics (from 1 to n_harmonics)
        signals = [
            a.plot(generate_square_wave(i), color=WHITE)
            for i in range(1, n_harmonics + 1)
        ]

        # Display the axes
        self.play(GrowFromCenter(a))

        # Animate the transformation of signals
        for i, signal in enumerate(signals):
            if i == 0:
                # Display the initial text for the first Fourier approximation
                signal_number = Text(f"Fourier Approximation of Order {i}", font_size=24).to_edge(UP)
                self.play(Create(signal), 
                          Write(signal_number), 
                          run_time=1, rate_func=linear)
            else:
                # Transform the signal and update the text for subsequent approximations
                self.play(Transform(signals[0], signal),
                          Transform(signal_number, Text(f"Fourier Approximation of Order {i}", font_size=24).to_edge(UP)),
                          run_time=0.5, rate_func=linear)
            self.wait(1)

        # Remove all objects from the scene
        self.play(FadeOut(signals[0]), FadeOut(a), run_time=0.5)
