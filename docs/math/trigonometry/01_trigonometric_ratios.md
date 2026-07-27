# Trigonometric Ratios

Welcome to the **Trigonometric Ratios** chapter. Trigonometry is that branch of mathematics which deals with the measurement of angles and the problems allied with angles. In this chapter, we explore the fundamental ratios of side lengths in right-angled triangles and their foundational algebraic properties.

---

## Topics

<div class="grid cards" markdown>

-   :material-triangle-outline: **Right Triangle Geometry & Terms**

    ---

    Learn how to classify sides of a right triangle into Perpendicular, Base, and Hypotenuse relative to a reference acute angle.

    [:octicons-arrow-right-24: Read Guide](#right-triangle-geometry-terms)

-   :material-function-variant: **Definitions of the Six Trigonometric Ratios**

    ---

    Understand the formal mathematical definitions of \(\sin \theta\), \(\cos \theta\), \(\tan \theta\), \(\csc \theta\), \(\sec \theta\), and \(\cot \theta\).

    [:octicons-arrow-right-24: Read Guide](#definitions-of-the-six-trigonometric-ratios)

-   :material-swap-vertical: **Reciprocal & Quotient Relations**

    ---

    Discover the fundamental algebraic dependencies connecting sine, cosine, tangent, secant, cosecant, and cotangent.

    [:octicons-arrow-right-24: Read Guide](#reciprocal-quotient-relations)

-   :material-vector-arrange-below: **Independence of Triangle Size**

    ---

    Study the geometric proof showing that trigonometric ratios depend strictly on the angle measure, regardless of triangle dimensions.

    [:octicons-arrow-right-24: Read Guide](#independence-of-triangle-size)

-   :material-book-open-variant: **Solved Examples**

    ---

    Step-by-step solutions to textbook problems determining trigonometric ratios, side lengths, and algebraic expressions.

    [:octicons-arrow-right-24: View Examples](#solved-examples)

-   :material-pencil-box-multiple: **Practice Questions**

    ---

    Test your understanding with conceptual and numerical exercise problems.

    [:octicons-arrow-right-24: View Questions](#practice-questions)

</div>

---

## Right Triangle Geometry & Terms

Consider a right-angled triangle \(\Delta ABC\), right-angled at \(B\). Let \(\angle BAC = \theta\) be an acute angle (\(0^\circ < \theta < 90^\circ\)).

```
        C
        | \
        |   \
   P    |     \   H
(Perp)  |       \ (Hypotenuse)
        |         \
        |__ _ _ _ _ \
        B    (Base)   A  (θ)
```

In relation to angle \(\theta\):

*   **Hypotenuse (\(H\))**: The side opposite to the right angle (\(90^\circ\)). It is the longest side of the right triangle (\(AC\)).
*   **Perpendicular / Opposite (\(P\))**: The side opposite to the chosen reference acute angle \(\theta\) (\(BC\)).
*   **Base / Adjacent (\(B\))**: The side adjacent to the chosen reference acute angle \(\theta\) (\(AB\)).

!!! note "Important Observation"
    The positions of the **Perpendicular** and **Base** depend on which acute angle is chosen as the reference:
    
    * For acute angle \(\angle A\): Perpendicular = \(BC\), Base = \(AB\), Hypotenuse = \(AC\).
    * For acute angle \(\angle C\): Perpendicular = \(AB\), Base = \(BC\), Hypotenuse = \(AC\).

---

## Definitions of the Six Trigonometric Ratios

For an acute angle \(\theta\) in a right-angled triangle \(\Delta ABC\) right-angled at \(B\), the six trigonometric ratios (T-ratios) are defined as follows:

$$
\sin \theta = \frac{\text{Perpendicular}}{\text{Hypotenuse}} = \frac{P}{H} = \frac{BC}{AC}
$$

$$
\cos \theta = \frac{\text{Base}}{\text{Hypotenuse}} = \frac{B}{H} = \frac{AB}{AC}
$$

$$
\tan \theta = \frac{\text{Perpendicular}}{\text{Base}} = \frac{P}{B} = \frac{BC}{AB}
$$

$$
\csc \theta = \frac{\text{Hypotenuse}}{\text{Perpendicular}} = \frac{H}{P} = \frac{AC}{BC}
$$

$$
\sec \theta = \frac{\text{Hypotenuse}}{\text{Base}} = \frac{H}{B} = \frac{AC}{AB}
$$

$$
\cot \theta = \frac{\text{Base}}{\text{Perpendicular}} = \frac{B}{P} = \frac{AB}{BC}
$$

---

## Reciprocal & Quotient Relations

### Reciprocal Relations

From the definitions above, the following reciprocal identities hold for any acute angle \(\theta\):

1.  \(\csc \theta = \frac{1}{\sin \theta} \iff \sin \theta \cdot \csc \theta = 1\)
2.  \(\sec \theta = \frac{1}{\cos \theta} \iff \cos \theta \cdot \sec \theta = 1\)
3.  \(\cot \theta = \frac{1}{\tan \theta} \iff \tan \theta \cdot \cot \theta = 1\)

### Quotient Relations

The tangent and cotangent ratios can be expressed as quotients of sine and cosine:

$$
\tan \theta = \frac{\frac{P}{H}}{\frac{B}{H}} = \frac{\sin \theta}{\cos \theta}
$$

$$
\cot \theta = \frac{\frac{B}{H}}{\frac{P}{H}} = \frac{\cos \theta}{\sin \theta}
$$

---

## Independence of Triangle Size

!!! tip "Theorem"
    The value of each trigonometric ratio of an acute angle depends only on the magnitude of the angle \(\theta\) and is independent of the size of the right triangle.

### Proof
Let \(\angle XAY = \theta\) be an acute angle. Take any point \(P\) on \(AY\) and draw \(PM \perp AX\). Take another point \(P'\) on \(AY\) and draw \(P'M' \perp AX\).

In \(\Delta AMP\) and \(\Delta AM'P'\):

*   \(\angle AMP = \angle AM'P' = 90^\circ\)
*   \(\angle PAM = \angle P'AM' = \theta\) (Common angle)

By AA Similarity Criterion, \(\Delta AMP \sim \Delta AM'P'\).

Therefore, the corresponding sides are proportional:

$$
\frac{PM}{P'M'} = \frac{AP}{AP'} = \frac{AM}{AM'} \implies \frac{PM}{AP} = \frac{P'M'}{AP'}
$$

This shows that \(\sin \theta = \frac{\text{Perpendicular}}{\text{Hypotenuse}}\) remains identical regardless of whether it is calculated using \(\Delta AMP\) or \(\Delta AM'P'\). Similar equal ratios hold for all six trigonometric functions.

---

## Solved Examples

### Example 1
Given \(\tan A = \frac{4}{3}\), find the remaining trigonometric ratios of angle \(A\).

**Solution:**

Let \(\Delta ABC\) be a right triangle, right-angled at \(B\), with reference angle \(A\).

We are given:

$$
\tan A = \frac{\text{Perpendicular}}{\text{Base}} = \frac{BC}{AB} = \frac{4}{3}
$$

Let \(BC = 4k\) and \(AB = 3k\), where \(k > 0\) is a constant multiplier.

By Pythagoras Theorem in right \(\Delta ABC\):

$$
AC^2 = AB^2 + BC^2 = (3k)^2 + (4k)^2 = 9k^2 + 16k^2 = 25k^2
$$

$$
AC = \sqrt{25k^2} = 5k
$$

Now, substituting values for Perpendicular (\(P = 4k\)), Base (\(B = 3k\)), and Hypotenuse (\(H = 5k\)):

*   \(\sin A = \frac{BC}{AC} = \frac{4k}{5k} = \frac{4}{5}\)
*   \(\cos A = \frac{AB}{AC} = \frac{3k}{5k} = \frac{3}{5}\)
*   \(\csc A = \frac{1}{\sin A} = \frac{5}{4}\)
*   \(\sec A = \frac{1}{\cos A} = \frac{5}{3}\)
*   \(\cot A = \frac{1}{\tan A} = \frac{3}{4}\)

---

### Example 2
In \(\Delta PQR\), right-angled at \(Q\), \(PR + QR = 25\text{ cm}\) and \(PQ = 5\text{ cm}\). Determine the values of \(\sin P\), \(\cos P\), and \(\tan P\).

**Solution:**

Let \(QR = x\text{ cm}\). Then \(PR = (25 - x)\text{ cm}\).

Applying Pythagoras Theorem to right-angled \(\Delta PQR\):

$$
PR^2 = PQ^2 + QR^2
$$

$$
(25 - x)^2 = 5^2 + x^2
$$

$$
625 - 50x + x^2 = 25 + x^2
$$

$$
625 - 25 = 50x \implies 50x = 600 \implies x = 12
$$

Thus:
*   \(QR = 12\text{ cm}\) (Perpendicular relative to \(\angle P\))
*   \(PR = 25 - 12 = 13\text{ cm}\) (Hypotenuse)
*   \(PQ = 5\text{ cm}\) (Base relative to \(\angle P\))

Calculating the required ratios:

$$
\sin P = \frac{QR}{PR} = \frac{12}{13}
$$

$$
\cos P = \frac{PQ}{PR} = \frac{5}{13}
$$

$$
\tan P = \frac{QR}{PQ} = \frac{12}{5}
$$

---

### Example 3
If \(3 \cot A = 4\), check whether \(\frac{1 - \tan^2 A}{1 + \tan^2 A} = \cos^2 A - \sin^2 A\) holds true.

**Solution:**

We have \(3 \cot A = 4 \implies \cot A = \frac{4}{3}\).

Therefore, \(\tan A = \frac{1}{\cot A} = \frac{3}{4}\).

In a right triangle with Base = \(4k\) and Perpendicular = \(3k\):

$$
\text{Hypotenuse} = \sqrt{(4k)^2 + (3k)^2} = \sqrt{16k^2 + 9k^2} = 5k
$$

Hence:

$$
\cos A = \frac{4}{5}, \quad \sin A = \frac{3}{5}
$$

Now evaluate Left-Hand Side (LHS):

$$
\text{LHS} = \frac{1 - \left(\frac{3}{4}\right)^2}{1 + \left(\frac{3}{4}\right)^2} = \frac{1 - \frac{9}{16}}{1 + \frac{9}{16}} = \frac{\frac{7}{16}}{\frac{25}{16}} = \frac{7}{25}
$$

Now evaluate Right-Hand Side (RHS):

$$
\text{RHS} = \cos^2 A - \sin^2 A = \left(\frac{4}{5}\right)^2 - \left(\frac{3}{5}\right)^2 = \frac{16}{25} - \frac{9}{25} = \frac{7}{25}
$$

Since \(\text{LHS} = \text{RHS} = \frac{7}{25}\), the equality holds true.

---

## Practice Questions

1. In \(\Delta ABC\), right-angled at \(B\), \(AB = 24\text{ cm}\) and \(BC = 7\text{ cm}\). Determine:
    * (i) \(\sin A, \cos A\)
    * (ii) \(\sin C, \cos C\)
2. If \(\sin A = \frac{3}{4}\), calculate \(\cos A\) and \(\tan A\).
3. Given \(15 \cot A = 8\), find \(\sin A\) and \(\sec A\).
4. If \(\sec \theta = \frac{13}{12}\), calculate all other trigonometric ratios.
5. In \(\Delta OPQ\), right-angled at \(P\), \(OP = 7\text{ cm}\) and \(OQ - PQ = 1\text{ cm}\). Prove that \(\sin Q = \frac{7}{25}\) and \(\cos Q = \frac{24}{25}\).
