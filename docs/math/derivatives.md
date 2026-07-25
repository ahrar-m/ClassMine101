# Derivatives & Tangent Lines 📐

The **derivative** measures how a function changes as its input changes. Geometrically, the derivative at a point is the slope of the tangent line to the graph of the function at that point.

---

## 💡 Mathematical Definition

The derivative of a function \( f(x) \) with respect to \( x \) is defined using limits:

\[
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
\]

### Example: Derivative of \( f(x) = x^2 \)

Applying the limit definition:

\[
f'(x) = \lim_{\Delta x \to 0} \frac{(x + \Delta x)^2 - x^2}{\Delta x}
\]

Expanding the numerator:

\[
f'(x) = \lim_{\Delta x \to 0} \frac{x^2 + 2x\Delta x + (\Delta x)^2 - x^2}{\Delta x} = \lim_{\Delta x \to 0} (2x + \Delta x) = 2x
\]

!!! formula "Power Rule Formula"
    For any real constant \( n \):
    \[
    \frac{d}{dx}[x^n] = n x^{n-1}
    \]

---

## 🎥 Visual Manim Animation

Below is the Python script used to generate the visual scene illustrating the tangent line slope \( f'(2) = 4 \):

```python
from manim import *

class DerivativeScene(Scene):
    def construct(self):
        title = Text("Derivative of f(x) = x²", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 9, 2],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True},
        ).shift(DOWN * 0.5)

        graph = axes.plot(lambda x: x**2, color=YELLOW, x_range=[0, 3])
        self.play(Create(axes), Create(graph))
```

---

## 📺 YouTube Walkthrough

Watch the full explanation and animated video step-by-step on our official YouTube channel:
[Watch Derivative Animation on YouTube :fontawesome-brands-youtube:](https://youtube.com){ .md-button .md-button--primary }
