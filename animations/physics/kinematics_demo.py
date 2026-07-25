from manim import *

class ProjectileMotionScene(Scene):
    def construct(self):
        title = Text("Projectile Motion: Parabolic Trajectory", font_size=36, color=CYAN)
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 6, 1],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        # Trajectory equation: y = -0.2*(x-5)^2 + 5
        trajectory = axes.plot(lambda x: -0.2 * ((x - 5) ** 2) + 5, x_range=[0, 10], color=YELLOW)
        trajectory_label = axes.get_graph_label(trajectory, label="y(x)", x_val=9, direction=UR)

        # Peak Point
        peak_point = axes.c2p(5, 5)
        peak_dot = Dot(peak_point, color=RED)
        peak_label = MathTex("h_{max} = 5\\text{ m}", color=RED).next_to(peak_dot, UP)

        self.play(Create(axes))
        self.play(Create(trajectory), run_time=2.5)
        self.play(FadeIn(peak_dot), Write(peak_label))
        self.wait(2)
