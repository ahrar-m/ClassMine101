from manim import *

class DerivativeScene(Scene):
    def construct(self):
        # Title
        title = Text("Derivative of f(x) = x²", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create Axes
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 9, 2],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        # Plot f(x) = x^2
        graph = axes.plot(lambda x: x**2, color=YELLOW, x_range=[0, 3])
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2", x_val=2.5, direction=UR)

        self.play(Create(axes), Create(graph), Write(graph_label))

        # Tangent line at x = 2
        x_val = 2
        point = axes.c2p(x_val, x_val**2)
        dot = Dot(point, color=RED)
        
        # Slope of f(x) = x^2 at x=2 is f'(2) = 4
        tangent = axes.get_secant_line(
            x_val,
            graph,
            dx=0.001,
            length=4,
            line_color=GREEN
        )
        
        tangent_label = MathTex("f'(2) = 4", color=GREEN).next_to(dot, RIGHT)

        self.play(FadeIn(dot), Create(tangent), Write(tangent_label))
        self.wait(2)
