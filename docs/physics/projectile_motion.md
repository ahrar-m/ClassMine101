# Projectile Motion & Kinematics ⚡

**Projectile motion** is a form of motion experienced by an object launched into the air, subject to only the acceleration of gravity (\(g \approx 9.81 \text{ m/s}^2\)).

---

## 📐 Governing Kinematic Equations

Assuming no air resistance, projectile motion decomposes into independent horizontal and vertical motions:

### 1. Horizontal Motion (\(x\)-axis)
No horizontal forces act on the projectile (\(a_x = 0\)):

\[
v_x = v_0 \cos(\theta) \quad \text{and} \quad x(t) = (v_0 \cos\theta) t
\]

### 2. Vertical Motion (\(y\)-axis)
Subject to constant gravitational acceleration downward (\(a_y = -g\)):

\[
v_y(t) = v_0 \sin(\theta) - gt \quad \text{and} \quad y(t) = (v_0 \sin\theta) t - \frac{1}{2}g t^2
\]

!!! formula "Maximum Height & Range"
    - **Maximum Height (\(h_{max}\))**:
      \[
      h_{max} = \frac{v_0^2 \sin^2\theta}{2g}
      \]
    - **Total Horizontal Range (\(R\))**:
      \[
      R = \frac{v_0^2 \sin(2\theta)}{g}
      \]

---

## 🎥 Manim Trajectory Script

The trajectory is animated using Manim by plotting the parametric function:

```python
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

        trajectory = axes.plot(lambda x: -0.2 * ((x - 5) ** 2) + 5, x_range=[0, 10], color=YELLOW)
        self.play(Create(axes), Create(trajectory))
```

---

## 📺 YouTube Walkthrough

Watch the full explanation and video demonstration:
[Watch Projectile Motion on YouTube :fontawesome-brands-youtube:](https://youtube.com){ .md-button .md-button--primary }
