from manim import *

class ProjectileMotionDemo(Scene):
    def construct(self):
        title = Text("Projectile Motion Visualizer", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 5, 1],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        # Parabolic trajectory y = -0.2 * (x - 5)^2 + 5
        trajectory = axes.plot(lambda x: -0.2 * ((x - 5) ** 2) + 5, x_range=[0, 10], color=YELLOW)

        self.play(Create(axes))
        self.play(Create(trajectory), run_time=3)
        self.wait(1)
