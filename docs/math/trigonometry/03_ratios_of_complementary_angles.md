# Trigonometric Ratios of Complementary Angles

Welcome to the **Trigonometric Ratios of Complementary Angles** chapter. In geometry, two acute angles are complementary if their sum equals \(90^\circ\). This chapter explores how trigonometric functions convert into their co-functions when operating on complementary angle complements.

---

## Topics

<div class="grid cards" markdown>

-   :material-angle-acute: **Concept of Complementary Angles**

    ---

    Understand the geometric definition of complementary angle pairs in right-angled triangles.

    [:octicons-arrow-right-24: Read Guide](#concept-of-complementary-angles)

-   :material-sigma-lower: **Geometric Derivation of Identities**

    ---

    Prove step-by-step why \(\sin(90^\circ - \theta) = \cos \theta\), \(\tan(90^\circ - \theta) = \cot \theta\), and \(\sec(90^\circ - \theta) = \csc \theta\).

    [:octicons-arrow-right-24: Read Guide](#geometric-derivation-of-identities)

-   :material-format-list-checks: **Summary of Complementary Identities**

    ---

    Quick reference list for all six complementary angle transformations.

    [:octicons-arrow-right-24: Read Guide](#summary-of-complementary-identities)

-   :material-book-open-variant: **Solved Examples**

    ---

    Step-by-step solutions showing how to simplify trigonometric ratios without requiring trigonometric lookup tables.

    [:octicons-arrow-right-24: View Examples](#solved-examples)

-   :material-pencil-box-multiple: **Practice Questions**

    ---

    Comprehensive exercise problems for self-assessment.

    [:octicons-arrow-right-24: View Questions](#practice-questions)

</div>

---

## Concept of Complementary Angles

Two angles are said to be **complementary** if their sum is \(90^\circ\).

In a right-angled triangle \(\Delta ABC\), right-angled at \(B\):

$$
\angle A + \angle B + \angle C = 180^\circ
$$

$$
\angle A + 90^\circ + \angle C = 180^\circ \implies \angle A + \angle C = 90^\circ
$$

If we denote acute angle \(\angle A = \theta\), then acute angle \(\angle C = 90^\circ - \theta\). Therefore, angles \(\angle A\) and \(\angle C\) form a pair of complementary angles.

---

## Geometric Derivation of Identities

Consider right-angled triangle \(\Delta ABC\), right-angled at \(B\). Let \(\angle A = \theta\), so \(\angle C = 90^\circ - \theta\).

```
        C (90° - θ)
        | \
        |   \
   P    |     \   H
(Perp)  |       \ (Hypotenuse)
        |         \
        |__ _ _ _ _ \
        B    (Base)   A (θ)
```

### Ratios for Reference Angle θ
*   \(\sin \theta = \frac{BC}{AC}\)
*   \(\cos \theta = \frac{AB}{AC}\)
*   \(\tan \theta = \frac{BC}{AB}\)
*   \(\csc \theta = \frac{AC}{BC}\)
*   \(\sec \theta = \frac{AC}{AB}\)
*   \(\cot \theta = \frac{AB}{BC}\)

### Ratios for Complementary Angle (90° - θ)
For angle \(C\), the Perpendicular is \(AB\), the Base is \(BC\), and the Hypotenuse is \(AC\):
*   \(\sin (90^\circ - \theta) = \frac{AB}{AC}\)
*   \(\cos (90^\circ - \theta) = \frac{BC}{AC}\)
*   \(\tan (90^\circ - \theta) = \frac{AB}{BC}\)
*   \(\csc (90^\circ - \theta) = \frac{AC}{AB}\)
*   \(\sec (90^\circ - \theta) = \frac{AC}{BC}\)
*   \(\cot (90^\circ - \theta) = \frac{BC}{AB}\)

Comparing the two sets of equations:

$$
\sin (90^\circ - \theta) = \cos \theta
$$

$$
\cos (90^\circ - \theta) = \sin \theta
$$

$$
\tan (90^\circ - \theta) = \cot \theta
$$

---

## Summary of Complementary Identities

For any acute angle \(\theta\) (\(0^\circ \le \theta \le 90^\circ\)):

1.  \(\sin (90^\circ - \theta) = \cos \theta\)
2.  \(\cos (90^\circ - \theta) = \sin \theta\)
3.  \(\tan (90^\circ - \theta) = \cot \theta\)
4.  \(\cot (90^\circ - \theta) = \tan \theta\)
5.  \(\sec (90^\circ - \theta) = \csc \theta\)
6.  \(\csc (90^\circ - \theta) = \sec \theta\)

---

## Solved Examples

### Example 1
Evaluate: \(\frac{\sin 18^\circ}{\cos 72^\circ}\).

**Solution:**

Notice that \(18^\circ + 72^\circ = 90^\circ\), so \(18^\circ\) and \(72^\circ\) are complementary angles.

We can express \(\sin 18^\circ\) as:

$$
\sin 18^\circ = \sin (90^\circ - 72^\circ) = \cos 72^\circ
$$

Substituting into the given fraction:

$$
\frac{\sin 18^\circ}{\cos 72^\circ} = \frac{\cos 72^\circ}{\cos 72^\circ} = 1
$$

---

### Example 2
Show that: \(\tan 48^\circ \tan 23^\circ \tan 42^\circ \tan 67^\circ = 1\).

**Solution:**

Group complementary angle pairs together:
*   \(48^\circ + 42^\circ = 90^\circ \implies \tan 42^\circ = \tan (90^\circ - 48^\circ) = \cot 48^\circ\)
*   \(23^\circ + 67^\circ = 90^\circ \implies \tan 67^\circ = \tan (90^\circ - 23^\circ) = \cot 23^\circ\)

Now rewrite LHS:

$$
\text{LHS} = \tan 48^\circ \cdot \tan 23^\circ \cdot \tan 42^\circ \cdot \tan 67^\circ
$$

$$
= \tan 48^\circ \cdot \tan 23^\circ \cdot \cot 48^\circ \cdot \cot 23^\circ
$$

$$
= (\tan 48^\circ \cot 48^\circ) \cdot (\tan 23^\circ \cot 23^\circ)
$$

Using the reciprocal relation \(\tan \theta \cot \theta = 1\):

$$
\text{LHS} = (1) \cdot (1) = 1 = \text{RHS}
$$

---

### Example 3
If \(\sin 3A = \cos(A - 26^\circ)\), where \(3A\) is an acute angle, find the value of \(A\).

**Solution:**

Using complementary identity \(\sin \theta = \cos (90^\circ - \theta)\):

$$
\sin 3A = \cos (90^\circ - 3A)
$$

Equating this to the given RHS:

$$
\cos (90^\circ - 3A) = \cos (A - 26^\circ)
$$

Since both angles are acute, their measures must be equal:

$$
90^\circ - 3A = A - 26^\circ
$$

$$
90^\circ + 26^\circ = A + 3A
$$

$$
116^\circ = 4A \implies A = \frac{116^\circ}{4} = 29^\circ
$$

**Answer:** \(A = 29^\circ\).

---

### Example 4
Express \(\cot 85^\circ + \cos 75^\circ\) in terms of trigonometric ratios of angles between \(0^\circ\) and \(45^\circ\).

**Solution:**

Apply complementary transformations to both terms:

$$
\cot 85^\circ = \cot (90^\circ - 5^\circ) = \tan 5^\circ
$$

$$
\cos 75^\circ = \cos (90^\circ - 15^\circ) = \sin 15^\circ
$$

Therefore:

$$
\cot 85^\circ + \cos 75^\circ = \tan 5^\circ + \sin 15^\circ
$$

Since \(5^\circ\) and \(15^\circ\) lie between \(0^\circ\) and \(45^\circ\), the expression is in the required form.

---

## Practice Questions

1. Evaluate:
    * (i) \(\frac{\tan 65^\circ}{\cot 25^\circ}\)
    * (ii) \(\cos 48^\circ - \sin 42^\circ\)
    * (iii) \(\csc 31^\circ - \sec 59^\circ\)
2. Show that:
    * (i) \(\tan 48^\circ \tan 23^\circ \tan 42^\circ \tan 67^\circ = 1\)
    * (ii) \(\cos 38^\circ \cos 52^\circ - \sin 38^\circ \sin 52^\circ = 0\)
3. If \(\tan 2A = \cot (A - 18^\circ)\), where \(2A\) is an acute angle, find the value of \(A\).
4. If \(\sec 4A = \csc (A - 20^\circ)\), where \(4A\) is an acute angle, find the value of \(A\).
5. If \(A, B\), and \(C\) are interior angles of a triangle \(\Delta ABC\), show that \(\sin\left(\frac{B + C}{2}\right) = \cos\left(\frac{A}{2}\right)\).
