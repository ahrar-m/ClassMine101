# Trigonometric Identities

Welcome to the **Trigonometric Identities** chapter. A trigonometric identity is an equality between expressions involving trigonometric ratios that holds true for every valid angle value. Master these fundamental identities and systematic proof techniques to simplify complex mathematical expressions.

---

## Topics

<div class="grid cards" markdown>

-   :material-book-information-variant: **Definition & Meaning**

    ---

    Understand what distinguishes a trigonometric identity from a standard conditional equation.

    [:octicons-arrow-right-24: Read Guide](#definition-meaning)

-   :material-math-integral: **Proof of Fundamental Pythagorean Identities**

    ---

    Derive the three fundamental identities directly from Pythagoras' Theorem in a right triangle.

    [:octicons-arrow-right-24: Read Guide](#proof-of-fundamental-pythagorean-identities)

-   :material-format-list-numbered: **Derived Algebraic Forms**

    ---

    Explore equivalent algebraic rearrangements used in proof transformations.

    [:octicons-arrow-right-24: Read Guide](#derived-algebraic-forms)

-   :material-lightbulb-on-outline: **Proof Strategies & Techniques**

    ---

    Learn practical algebraic techniques for transforming Left-Hand Side (LHS) into Right-Hand Side (RHS).

    [:octicons-arrow-right-24: Read Guide](#proof-strategies-techniques)

-   :material-book-open-variant: **Solved Examples**

    ---

    Step-by-step rigorous proofs of classic board exam and textbook identity problems.

    [:octicons-arrow-right-24: View Examples](#solved-examples)

-   :material-pencil-box-multiple: **Practice Questions**

    ---

    A rich list of identity verification questions for mastery.

    [:octicons-arrow-right-24: View Questions](#practice-questions)

</div>

---

## Definition & Meaning

An equation involving trigonometric ratios of an angle \(\theta\) is called a **Trigonometric Identity** if it is satisfied by all permissible values of \(\theta\) for which the trigonometric functions are defined.

!!! example "Contrast: Identity vs. Conditional Equation"
    *   **Identity**: \(\sin^2 \theta + \cos^2 \theta = 1\) is true for every angle \(\theta \in [0^\circ, 30^\circ, 45^\circ, 90^\circ, \dots]\).
    *   **Conditional Equation**: \(\sin \theta = \frac{1}{2}\) is true only for specific angles (e.g., \(\theta = 30^\circ\)), not for all angles.

---

## Proof of Fundamental Pythagorean Identities

Consider right-angled triangle \(\Delta ABC\), right-angled at \(B\), with reference acute angle \(\angle BAC = \theta\).

```
        C
        | \
        |   \
   P    |     \   H
(Perp)  |       \ (Hypotenuse)
        |         \
        |__ _ _ _ _ \
        B    (Base)   A (θ)
```

By Pythagoras Theorem:

$$
AB^2 + BC^2 = AC^2 \quad \text{--- (Equation 1)}
$$

---

### Identity 1: Sine and Cosine Pythagorean Identity

Divide each term in Equation (1) by \(AC^2\):

$$
\frac{AB^2}{AC^2} + \frac{BC^2}{AC^2} = \frac{AC^2}{AC^2}
$$

$$
\left(\frac{AB}{AC}\right)^2 + \left(\frac{BC}{AC}\right)^2 = 1
$$

Since \(\frac{AB}{AC} = \cos \theta\) and \(\frac{BC}{AC} = \sin \theta\):

$$
\cos^2 \theta + \sin^2 \theta = 1 \iff \sin^2 \theta + \cos^2 \theta = 1
$$

*(Valid for all \(0^\circ \le \theta \le 90^\circ\)).*

---

### Identity 2: Secant and Tangent Pythagorean Identity

Divide each term in Equation (1) by \(AB^2\):

$$
\frac{AB^2}{AB^2} + \frac{BC^2}{AB^2} = \frac{AC^2}{AB^2}
$$

$$
1 + \left(\frac{BC}{AB}\right)^2 = \left(\frac{AC}{AB}\right)^2
$$

Since \(\frac{BC}{AB} = \tan \theta\) and \(\frac{AC}{AB} = \sec \theta\):

$$
1 + \tan^2 \theta = \sec^2 \theta
$$

*(Valid for all \(0^\circ \le \theta < 90^\circ\)).*

---

### Identity 3: Cosecant and Cotangent Pythagorean Identity

Divide each term in Equation (1) by \(BC^2\):

$$
\frac{AB^2}{BC^2} + \frac{BC^2}{BC^2} = \frac{AC^2}{BC^2}
$$

$$
\left(\frac{AB}{BC}\right)^2 + 1 = \left(\frac{AC}{BC}\right)^2
$$

Since \(\frac{AB}{BC} = \cot \theta\) and \(\frac{AC}{BC} = \csc \theta\):

$$
1 + \cot^2 \theta = \csc^2 \theta
$$

*(Valid for all \(0^\circ < \theta \le 90^\circ\)).*

---

## Derived Algebraic Forms

In mathematical proofs, we frequently rewrite the three fundamental identities into these useful variations:

### From Sine-Cosine Identity
*   \(\sin^2 \theta = 1 - \cos^2 \theta \iff \sin \theta = \sqrt{1 - \cos^2 \theta}\)
*   \(\cos^2 \theta = 1 - \sin^2 \theta \iff \cos \theta = \sqrt{1 - \sin^2 \theta}\)

### From Tangent-Secant Identity
*   \(\sec^2 \theta - \tan^2 \theta = 1\)
*   \(\tan^2 \theta = \sec^2 \theta - 1 \iff \tan \theta = \sqrt{\sec^2 \theta - 1}\)

### From Cotangent-Cosecant Identity
*   \(\csc^2 \theta - \cot^2 \theta = 1\)
*   \(\cot^2 \theta = \csc^2 \theta - 1 \iff \cot \theta = \sqrt{\csc^2 \theta - 1}\)

---

## Proof Strategies & Techniques

When asked to prove that \(\text{LHS} = \text{RHS}\):

1.  **Express in terms of Sine and Cosine**: Convert \(\tan \theta, \cot \theta, \sec \theta\), and \(\csc \theta\) into \(\sin \theta\) and \(\cos \theta\).
2.  **Combine Fractions**: Take common denominators when adding or subtracting fractional terms.
3.  **Apply Algebraic Identities**:
    *   \(a^2 - b^2 = (a - b)(a + b)\)
    *   \((a + b)^2 = a^2 + 2ab + b^2\)
    *   \(a^3 + b^3 = (a + b)(a^2 - ab + b^2)\)
    *   \(a^3 - b^3 = (a - b)(a^2 + ab + b^2)\)
4.  **Rationalization**: Multiply both numerator and denominator by conjugate factors (e.g., multiply by \(1 + \cos \theta\) when seeing \(1 - \cos \theta\)).

---

## Solved Examples

### Example 1
Express \(\cos A, \tan A\), and \(\sec A\) in terms of \(\sin A\).

**Solution:**

1.  **For \(\cos A\)**:
    Using \(\sin^2 A + \cos^2 A = 1 \implies \cos^2 A = 1 - \sin^2 A\):

$$
    \cos A = \sqrt{1 - \sin^2 A}
$$

2.  **For \(\tan A\)**:
    Using quotient relation \(\tan A = \frac{\sin A}{\cos A}\):

$$
    \tan A = \frac{\sin A}{\sqrt{1 - \sin^2 A}}
$$

3.  **For \(\sec A\)**:
    Using reciprocal relation \(\sec A = \frac{1}{\cos A}\):

$$
    \sec A = \frac{1}{\sqrt{1 - \sin^2 A}}
$$

---

### Example 2
Prove that: \(\frac{\sin \theta - 2\sin^3 \theta}{2\cos^3 \theta - \cos \theta} = \tan \theta\).

**Solution:**

Start from Left-Hand Side (LHS):

$$
\text{LHS} = \frac{\sin \theta (1 - 2\sin^2 \theta)}{\cos \theta (2\cos^2 \theta - 1)}
$$

Using identity \(\sin^2 \theta = 1 - \cos^2 \theta\) in the numerator:

$$
1 - 2\sin^2 \theta = 1 - 2(1 - \cos^2 \theta) = 1 - 2 + 2\cos^2 \theta = 2\cos^2 \theta - 1
$$

Substitute back into LHS:

$$
\text{LHS} = \frac{\sin \theta (2\cos^2 \theta - 1)}{\cos \theta (2\cos^2 \theta - 1)}
$$

Cancel out the common factor \((2\cos^2 \theta - 1)\):

$$
\text{LHS} = \frac{\sin \theta}{\cos \theta} = \tan \theta = \text{RHS}
$$

Hence proved.

---

### Example 3
Prove that: \(\sqrt{\frac{1 + \sin A}{1 - \sin A}} = \sec A + \tan A\).

**Solution:**

Start from Left-Hand Side (LHS):

$$
\text{LHS} = \sqrt{\frac{1 + \sin A}{1 - \sin A}}
$$

Multiply numerator and denominator inside the square root by \((1 + \sin A)\):

$$
\text{LHS} = \sqrt{\frac{(1 + \sin A)(1 + \sin A)}{(1 - \sin A)(1 + \sin A)}} = \sqrt{\frac{(1 + \sin A)^2}{1 - \sin^2 A}}
$$

Since \(1 - \sin^2 A = \cos^2 A\):

$$
\text{LHS} = \sqrt{\frac{(1 + \sin A)^2}{\cos^2 A}} = \frac{1 + \sin A}{\cos A}
$$

Split the fraction:

$$
\text{LHS} = \frac{1}{\cos A} + \frac{\sin A}{\cos A} = \sec A + \tan A = \text{RHS}
$$

Hence proved.

---

### Example 4
Prove that: \((\sin A + \csc A)^2 + (\cos A + \sec A)^2 = 7 + \tan^2 A + \cot^2 A\).

**Solution:**

Expand LHS using \((a + b)^2 = a^2 + 2ab + b^2\):

$$
\text{LHS} = (\sin^2 A + 2\sin A \csc A + \csc^2 A) + (\cos^2 A + 2\cos A \sec A + \sec^2 A)
$$

Use reciprocal relations \(\sin A \csc A = 1\) and \(\cos A \sec A = 1\):

$$
\text{LHS} = \sin^2 A + 2(1) + \csc^2 A + \cos^2 A + 2(1) + \sec^2 A
$$

$$
= (\sin^2 A + \cos^2 A) + 4 + \csc^2 A + \sec^2 A
$$

Substitute \(\sin^2 A + \cos^2 A = 1\):

$$
\text{LHS} = 1 + 4 + \csc^2 A + \sec^2 A = 5 + \csc^2 A + \sec^2 A
$$

Now convert \(\csc^2 A\) and \(\sec^2 A\) using fundamental identities:
*   \(\csc^2 A = 1 + \cot^2 A\)
*   \(\sec^2 A = 1 + \tan^2 A\)

$$
\text{LHS} = 5 + (1 + \cot^2 A) + (1 + \tan^2 A) = 7 + \tan^2 A + \cot^2 A = \text{RHS}
$$

Hence proved.

---

## Practice Questions

1. Prove the following identities:
    * (i) \(\frac{\csc \theta - \cot \theta}{1} = \frac{1 - \cos \theta}{\sin \theta}\)
    * (ii) \(\frac{\cos A}{1 + \sin A} + \frac{1 + \sin A}{\cos A} = 2 \sec A\)
    * (iii) \(\frac{\tan \theta}{1 - \cot \theta} + \frac{\cot \theta}{1 - \tan \theta} = 1 + \sec \theta \csc \theta\)
    * (iv) \(\frac{1 + \sec A}{\sec A} = \frac{\sin^2 A}{1 - \cos A}\)
    * (v) \(\frac{\sin \theta - \cos \theta + 1}{\sin \theta + \cos \theta - 1} = \frac{1}{\sec \theta - \tan \theta}\)
2. Prove that \((1 + \cot A - \csc A)(1 + \tan A + \sec A) = 2\).
3. If \(\tan \theta + \sin \theta = m\) and \(\tan \theta - \sin \theta = n\), prove that \(m^2 - n^2 = 4\sqrt{mn}\).
