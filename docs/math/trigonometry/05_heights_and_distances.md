# Heights and Distances

Welcome to the **Heights and Distances** chapter. This section applies trigonometric principles to solve practical real-world measuring problems, such as determining the heights of tall towers, mountains, and trees, or finding distances between moving objects without direct measurement.

---

## Topics

<div class="grid cards" markdown>

-   :material-eye-outline: **Line of Sight & Basic Terms**

    ---

    Understand the definitions of line of sight, observer eye level, and horizontal reference lines.

    [:octicons-arrow-right-24: Read Guide](#line-of-sight-basic-terms)

-   :material-angle-acute: **Angle of Elevation**

    ---

    Learn how the angle formed when looking upward at an elevated target is defined and measured.

    [:octicons-arrow-right-24: Read Guide](#angle-of-elevation)

-   :material-angle-obtuse: **Angle of Depression**

    ---

    Understand downward observation angles and their equivalence to upward angles of elevation.

    [:octicons-arrow-right-24: Read Guide](#angle-of-depression)

-   :material-sitemap: **Systematic Problem-Solving Workflow**

    ---

    Follow a step-by-step strategy to convert word problems into geometric diagrams and right triangle equations.

    [:octicons-arrow-right-24: Read Guide](#systematic-problem-solving-workflow)

-   :material-book-open-variant: **Solved Examples**

    ---

    Step-by-step solutions to classic single-triangle and multi-triangle application problems.

    [:octicons-arrow-right-24: View Examples](#solved-examples)

-   :material-pencil-box-multiple: **Practice Questions**

    ---

    Comprehensive word problems for assessment.

    [:octicons-arrow-right-24: View Questions](#practice-questions)

</div>

---

## Line of Sight & Basic Terms

When an observer looks at an object, the line connecting the observer's eye to the target object is called the **Line of Sight**.

```
             Object P (Top of Tower)
            /|
           / |
Line of   /  | Height
Sight    /   |
        / θ  |
Eye O  /_____| Horizontal Line OX
      Observer Foot
```

*   **Observer Point (\(O\))**: The point where the observer's eye is located.
*   **Target Point (\(P\))**: The point being observed.
*   **Line of Sight (\(OP\))**: The straight ray pointing from eye \(O\) to object \(P\).
*   **Horizontal Line (\(OX\))**: The level line drawn parallel to flat ground through eye point \(O\).

---

## Angle of Elevation

If the target object \(P\) is **above** the horizontal level of the observer's eye, the angle between the horizontal line \(OX\) and the line of sight \(OP\) is called the **Angle of Elevation**.

\[
\angle XOP = \theta \quad (\text{Angle of Elevation})
\]

!!! note "Key Observation"
    To measure an angle of elevation, the observer must raise their eyes upward from the horizontal level line.

---

## Angle of Depression

If the target object \(P\) is **below** the horizontal level of the observer's eye, the angle between the horizontal line \(OX\) and the line of sight \(OP\) is called the **Angle of Depression**.

```
Eye O ____________ Horizontal Line OX
      \ θ |
       \  |
Line of \ | Depth
Sight    \|
          P (Object on Ground/Sea)
```

\[
\angle XOP = \theta \quad (\text{Angle of Depression})
\]

!!! tip "Equivalence Theorem"
    Since the horizontal line drawn at eye level is parallel to the ground surface:
    
    \[
    \text{Angle of Depression of } P \text{ from } O = \text{Angle of Elevation of } O \text{ from } P
    \]
    *(By alternate interior angles formed by parallel horizontal lines).*

---

## Systematic Problem-Solving Workflow

To solve heights and distances word problems reliably:

1.  **Draw a Diagram**: Construct a neat geometric diagram translating every sentence of the word problem into points, vertical lines, horizontal ground lines, and right triangles.
2.  **Label Knowns and Unknowns**: Assign variables (e.g., \(h\) for height, \(x\) for distance) and note all given angles and segment lengths.
3.  **Identify Right-Angled Triangles**: Locate the right-angled triangles containing the target variables.
4.  **Apply Trigonometric Functions**:
    * Use \(\tan \theta = \frac{\text{Perpendicular}}{\text{Base}}\) when relating heights and ground distances.
    * Use \(\sin \theta = \frac{\text{Perpendicular}}{\text{Hypotenuse}}\) when ladders, ropes, or slanted distances are involved.
5.  **Solve System of Equations**: Solve algebraically for the unknown variables.

---

## Solved Examples

### Example 1
A tower stands vertically on the ground. From a point on the ground which is \(15\text{ m}\) away from the foot of the tower, the angle of elevation of the top of the tower is found to be \(60^\circ\). Find the height of the tower.

**Solution:**

Let \(AB\) represent the height of the tower (\(h\text{ meters}\)), and let \(C\) be the point on the ground such that ground distance \(BC = 15\text{ m}\).

Given: \(\angle ACB = 60^\circ\).

In right \(\Delta ABC\):
\[
\tan 60^\circ = \frac{\text{Perpendicular}}{\text{Base}} = \frac{AB}{BC}
\]
\[
\sqrt{3} = \frac{h}{15} \implies h = 15\sqrt{3}\text{ m}
\]

Taking \(\sqrt{3} \approx 1.732\):
\[
h = 15 \times 1.732 = 25.98\text{ m}
\]

**Answer:** Height of the tower is \(15\sqrt{3}\text{ m}\) (or \(25.98\text{ m}\)).

---

### Example 2
A tree breaks due to a storm and the broken part bends so that the top of the tree touches the ground making an angle of \(30^\circ\) with it. The distance between the foot of the tree to the point where the top touches the ground is \(8\text{ m}\). Find the total height of the tree.

**Solution:**

Let the original unbroken vertical tree be \(AB\). Suppose it breaks at point \(C\). The top part \(AC\) bends over such that point \(A\) touches the ground at point \(D\).

Therefore:
*   Unbroken lower trunk = \(BC\)
*   Broken upper stem = \(CD = AC\)
*   Total height of tree = \(BC + CD\)
*   Distance \(BD = 8\text{ m}\), \(\angle CDB = 30^\circ\).

In right \(\Delta CBD\):

1.  **To find \(BC\)**:
    \[
    \tan 30^\circ = \frac{BC}{BD} \implies \frac{1}{\sqrt{3}} = \frac{BC}{8} \implies BC = \frac{8}{\sqrt{3}}\text{ m}
    \]

2.  **To find \(CD\)**:
    \[
    \cos 30^\circ = \frac{BD}{CD} \implies \frac{\sqrt{3}}{2} = \frac{8}{CD} \implies CD = \frac{16}{\sqrt{3}}\text{ m}
    \]

3.  **Total height of the tree**:
    \[
    \text{Height} = BC + CD = \frac{8}{\sqrt{3}} + \frac{16}{\sqrt{3}} = \frac{24}{\sqrt{3}} = \frac{24\sqrt{3}}{3} = 8\sqrt{3}\text{ m}
    \]

**Answer:** Total height of the tree is \(8\sqrt{3}\text{ m}\).

---

### Example 3
As observed from the top of a \(75\text{ m}\) high lighthouse from the sea-level, the angles of depression of two ships are \(30^\circ\) and \(45^\circ\). If one ship is exactly behind the other on the same side of the lighthouse, find the distance between the two ships.

**Solution:**

Let \(AB = 75\text{ m}\) be the lighthouse. Let \(C\) and \(D\) be the positions of the two ships on the same line through foot \(B\).

Angles of depression:
*   For closer ship \(C\): \(\angle ACB = 45^\circ\)
*   For farther ship \(D\): \(\angle ADB = 30^\circ\)

Let \(BC = x\text{ m}\) and distance between ships \(CD = y\text{ m}\), so \(BD = x + y\text{ m}\).

1.  In right \(\Delta ABC\):
    \[
    \tan 45^\circ = \frac{AB}{BC} \implies 1 = \frac{75}{x} \implies x = 75\text{ m}
    \]

2.  In right \(\Delta ABD\):
    \[
    \tan 30^\circ = \frac{AB}{BD} \implies \frac{1}{\sqrt{3}} = \frac{75}{x + y}
    \]
    \[
    x + y = 75\sqrt{3}
    \]

3.  Substitute \(x = 75\):
    \[
    75 + y = 75\sqrt{3} \implies y = 75\sqrt{3} - 75 = 75(\sqrt{3} - 1)\text{ m}
    \]

Taking \(\sqrt{3} \approx 1.732\):
\[
y = 75(1.732 - 1) = 75 \times 0.732 = 54.9\text{ m}
\]

**Answer:** The distance between the two ships is \(75(\sqrt{3} - 1)\text{ m}\) (or \(54.9\text{ m}\)).

---

## Practice Questions

1. A 1.5 m tall boy is standing at some distance from a 30 m tall building. The angle of elevation from his eyes to the top of the building increases from \(30^\circ\) to \(60^\circ\) as he walks towards the building. Find the distance he walked towards the building.
2. From a point on a bridge across a river, the angles of depression of the banks on opposite sides of the river are \(30^\circ\) and \(45^\circ\), respectively. If the bridge is at a height of \(3\text{ m}\) from the banks, find the width of the river.
3. A 1.2 m tall girl spots a balloon moving with the wind in a horizontal line at a height of 88.2 m from the ground. The angle of elevation of the balloon from the eyes of the girl at any instant is \(60^\circ\). After some time, the angle of elevation reduces to \(30^\circ\). Find the distance travelled by the balloon during the interval.
4. A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of \(30^\circ\), which is approaching the foot of the tower with a uniform speed. Six seconds later, the angle of depression of the car is found to be \(60^\circ\). Find the time taken by the car to reach the foot of the tower from this point.
