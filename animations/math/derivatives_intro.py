from manim import *

class DerivativeIntro(Scene):
    def construct(self):
        # Title
        title = Text("Derivative as Slope of Tangent Line", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes and curve f(x) = x^2 / 4
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        curve = axes.plot(lambda x: (x ** 2) / 4, color=BLUE)
        curve_label = axes.get_graph_label(curve, label="f(x) = \\frac{x^2}{4}", x_val=4, direction=UR)

        self.play(Create(axes), Create(curve), Write(curve_label))
        self.wait(1)
