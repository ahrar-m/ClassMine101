# Trigonometric Ratios & Particular Angles

!!! info "Chapter Overview"
    Complete theoretical foundation, geometric definitions, reciprocal & quotient identities, scale-independence proofs, and evaluation of trigonometric ratios for acute angles ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$).

---

## Topics

<div class="grid cards" markdown>

-   :material-check-circle: **[1. Introduction & Right Triangle Geometry](#1-introduction-right-triangle-geometry)**

    ---

    Definition of acute angle $\theta$, Hypotenuse, Perpendicular (Opposite side), and Base (Adjacent side) in a right-angled triangle.

    *:material-check-bold: Completed*

-   :material-function-variant: **[2. The Six Trigonometric Ratios](#2-the-six-trigonometric-ratios)**

    ---

    Definitions of $\sin \theta$, $\cos \theta$, $\tan \theta$, $\csc \theta$, $\sec \theta$, and $\cot \theta$.

    *:material-clock-outline: Content coming soon*

-   :material-swap-horizontal: **[3. Reciprocal & Quotient Relations](#3-reciprocal-quotient-relations)**

    ---

    Fundamental relations: $\csc \theta = \frac{1}{\sin \theta}$, $\sec \theta = \frac{1}{\cos \theta}$, $\cot \theta = \frac{1}{\tan \theta}$, $\tan \theta = \frac{\sin \theta}{\cos \theta}$, $\cot \theta = \frac{\cos \theta}{\sin \theta}$.

    *:material-clock-outline: Content coming soon*

-   :material-ruler-square: **[4. Scale Independence of T-Ratios](#4-scale-independence-of-t-ratios)**

    ---

    Proof using similar triangles showing that T-ratios depend strictly on the angle $\theta$ and not on the size of the triangle.

    *:material-clock-outline: Content coming soon*

-   :material-calculator: **[5. Evaluating T-Ratios using Pythagoras Theorem](#5-evaluating-t-ratios-using-pythagoras-theorem)**

    ---

    Given one trigonometric ratio, determine all remaining five ratios using the right triangle property and constant ratio factor $k$.

    *:material-clock-outline: Content coming soon*

-   :material-angle-acute: **[6. T-Ratios of Specific Angles](#6-t-ratios-of-specific-angles)**

    ---

    Geometric derivations of ratio values for standard angles ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$), ratio tables, and algebraic evaluation.

    *:material-clock-outline: Content coming soon*

-   :material-book-open-outline: **[7. Core Concept Walkthroughs](#7-core-concept-walkthroughs)**

    ---

    Step-by-step solutions and conceptual walkthroughs for standard topic problems.

    *:material-clock-outline: Content coming soon*

-   :material-notebook-edit-outline: **[8. High-Yield Practice Problems](#8-high-yield-practice-problems)**

    ---

    Exhaustive practice set covering foundational and advanced problem types.

    *:material-clock-outline: Content coming soon*

</div>

---

## 1. Introduction & Right Triangle Geometry

### 1.1 What is Trigonometry?

The word **Trigonometry** is derived from three Greek words:
* **Tri** ($\text{tr\bar{\imath}s}$) — meaning *three*
* **Gon** ($\text{g\bar{o}n\acute{\imath}a}$) — meaning *angle* or *corner*
* **Metron** ($\text{metron}$) — meaning *measure*

At its core, **trigonometry is the branch of mathematics concerned with the relationships between the side lengths and interior angles of triangles**. While its origins lie in surveying, navigation, and astronomy, modern trigonometry underpins advanced science, engineering, signal processing, computer graphics, wave theory, and visual physics modeling.

---

### 1.2 Right-Angled Triangle Nomenclature

Every trigonometric ratio is fundamentally established upon a **right-angled triangle** (a triangle in which one interior angle is exactly $90^\circ$).

Consider $\triangle ABC$ right-angled at vertex $C$ ($\angle C = 90^\circ$):

```
                     B
                     |\
                     | \
                     |  \  Hypotenuse (h)
 Perpendicular (p)   |   \  [Opposite to ∠A]
 [Opposite to ∠A]    |    \
                     |     \
                     |______\
                     C       A
                      Base (b)
                  [Adjacent to ∠A]
```

In any right-angled triangle $\triangle ABC$ with $\angle C = 90^\circ$:

1. **Sum of Interior Angles**:
   $$\angle A + \angle B + \angle C = 180^\circ \implies \angle A + \angle B + 90^\circ = 180^\circ \implies \angle A + \angle B = 90^\circ$$
   Since $\angle A + \angle B = 90^\circ$, both acute angles $\angle A$ and $\angle B$ must be strictly strictly between $0^\circ$ and $90^\circ$ ($0^\circ < \angle A, \angle B < 90^\circ$).

2. **The Three Sides Defined Relative to Reference Angle $\theta$**:
   Let $\angle A = \theta$ be our chosen **acute reference angle**:

   * **Hypotenuse ($h$)**: The side opposite to the right angle ($\angle C = 90^\circ$). It is always the longest side of the right triangle ($AB$).
   * **Perpendicular / Opposite Side ($p$)**: The side directly opposite to the reference angle $\theta$ ($BC$).
   * **Base / Adjacent Side ($b$)**: The side adjacent to (touching) the reference angle $\theta$, excluding the hypotenuse ($AC$).

---

### 1.3 Reference Angle Dependency

!!! warning "Crucial Concept: Perpendicular and Base depend on the Reference Angle!"
    Unlike the **Hypotenuse** (which is fixed as the side opposite the $90^\circ$ angle), the terms **Perpendicular (Opposite)** and **Base (Adjacent)** are NOT fixed properties of the physical triangle. They depend entirely on **which acute angle** you choose as your reference.

Let us compare the two acute angles $\angle A$ and $\angle B$ in the same right triangle $\triangle ABC$ ($\angle C = 90^\circ$):

| Element | Reference Angle $\theta = \angle A$ | Reference Angle $\phi = \angle B$ |
| :--- | :--- | :--- |
| **Right Angle** | $\angle C = 90^\circ$ | $\angle C = 90^\circ$ |
| **Hypotenuse ($h$)** | $AB$ (Opposite to $90^\circ$) | $AB$ (Opposite to $90^\circ$) |
| **Perpendicular ($p$)** | $BC$ (Opposite to $\angle A$) | $AC$ (Opposite to $\angle B$) |
| **Base ($b$)** | $AC$ (Adjacent to $\angle A$) | $BC$ (Adjacent to $\angle B$) |

```
    For Reference Angle ∠A (θ):              For Reference Angle ∠B (ϕ):

             B                                        B
             |\                                       |\
             | \                                      | \
   p = BC    |  \  h = AB                   b = BC    |  \  h = AB
 [Opposite]  |   \  [Hypotenuse]          [Adjacent]  |   \  [Hypotenuse]
             |    \                                   |    \
             |_____\θ                                 |_____\
             C  b = AC                                C  p = AC
            [Adjacent]                               [Opposite]
```

!!! tip "Key Takeaway"
    $$\text{Opposite to } \angle A = \text{Adjacent to } \angle B$$
    $$\text{Adjacent to } \angle A = \text{Opposite to } \angle B$$

---

### 1.4 The Pythagorean Theorem

The geometric foundation of all right-triangle calculations is the **Pythagorean Theorem**:

!!! note "Pythagoras Theorem"
    In a right-angled triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.

$$\text{Hypotenuse}^2 = \text{Perpendicular}^2 + \text{Base}^2$$

$$h^2 = p^2 + b^2 \quad \text{or} \quad AB^2 = BC^2 + AC^2$$

#### Expressing Side Lengths algebraically:
* **To find Hypotenuse ($h$)**: $h = \sqrt{p^2 + b^2}$
* **To find Perpendicular ($p$)**: $p = \sqrt{h^2 - b^2}$
* **To find Base ($b$)**: $b = \sqrt{h^2 - p^2}$

#### Fundamental Pythagorean Triples
Sets of positive integers $(a, b, c)$ that satisfy $a^2 + b^2 = c^2$ are called **Pythagorean Triples**. Recognizing them speeds up solving trigonometric problems:

* **$(3, 4, 5)$**: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$
* **$(5, 12, 13)$**: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$
* **$(7, 24, 25)$**: $7^2 + 24^2 = 49 + 576 = 625 = 25^2$
* **$(8, 15, 17)$**: $8^2 + 15^2 = 64 + 225 = 289 = 17^2$
* **$(9, 40, 41)$**: $9^2 + 40^2 = 81 + 1600 = 1681 = 41^2$

!!! info "Scaling Property of Pythagorean Triples"
    If $(a, b, c)$ is a Pythagorean Triple, then for any positive real constant ratio $k > 0$, the scaled triplet $(ka, kb, kc)$ also forms a right-angled triangle. For instance, scaling $(3, 4, 5)$ by $k = 2$ yields $(6, 8, 10)$, which satisfies $6^2 + 8^2 = 36 + 64 = 100 = 10^2$.

---

### 1.5 Solved Examples

#### **Example 1.1: Identifying Sides Relative to Acute Angles**

??? example "Problem Statement & Solution"
    In a right-angled triangle $\triangle PQR$, $\angle Q = 90^\circ$, $PQ = 5\text{ cm}$, and $QR = 12\text{ cm}$.

    1. Calculate the length of hypotenuse $PR$.
    2. Identify the Hypotenuse, Perpendicular, and Base relative to angle $\angle R$.
    3. Identify the Hypotenuse, Perpendicular, and Base relative to angle $\angle P$.

    ---

    **Solution:**

    **Step 1: Calculate hypotenuse $PR$ using Pythagoras Theorem**
    $$\text{In } \triangle PQR \text{ with } \angle Q = 90^\circ:$$
    $$PR^2 = PQ^2 + QR^2$$
    $$PR^2 = 5^2 + 12^2 = 25 + 144 = 169$$
    $$PR = \sqrt{169} = 13\text{ cm}$$

    **Step 2: Relative to acute angle $\angle R$ ($\theta = \angle R$)**
    * **Hypotenuse ($h$)**: $PR = 13\text{ cm}$ (opposite to $90^\circ$ angle $\angle Q$)
    * **Perpendicular ($p$)**: $PQ = 5\text{ cm}$ (side opposite to $\angle R$)
    * **Base ($b$)**: $QR = 12\text{ cm}$ (side adjacent to $\angle R$)

    **Step 3: Relative to acute angle $\angle P$ ($\phi = \angle P$)**
    * **Hypotenuse ($h$)**: $PR = 13\text{ cm}$ (opposite to $90^\circ$ angle $\angle Q$)
    * **Perpendicular ($p$)**: $QR = 12\text{ cm}$ (side opposite to $\angle P$)
    * **Base ($b$)**: $PQ = 5\text{ cm}$ (side adjacent to $\angle P$)

---

#### **Example 1.2: Finding Missing Side Lengths**

??? example "Problem Statement & Solution"
    In $\triangle ABC$ right-angled at $C$, the hypotenuse $AB = 25\text{ cm}$ and base side $AC = 7\text{ cm}$ relative to angle $\angle A$. Find the length of side $BC$ and verify the Pythagorean relation.

    ---

    **Solution:**

    **Step 1: Apply Pythagoras Theorem**
    $$AB^2 = AC^2 + BC^2$$
    $$25^2 = 7^2 + BC^2$$
    $$625 = 49 + BC^2$$
    $$BC^2 = 625 - 49 = 576$$
    $$BC = \sqrt{576} = 24\text{ cm}$$

    **Step 2: Verification**
    $$p^2 + b^2 = 24^2 + 7^2 = 576 + 49 = 625 = 25^2 = h^2$$
    Thus, side $BC = 24\text{ cm}$, forming the Pythagorean triple $(7, 24, 25)$.

---

## 2. The Six Trigonometric Ratios

!!! info "Coming Soon"
    Detailed definitions and geometric setup for $\sin \theta$, $\cos \theta$, $\tan \theta$, $\csc \theta$, $\sec \theta$, and $\cot \theta$.

---

## 3. Reciprocal & Quotient Relations

!!! info "Coming Soon"
    Detailed mathematical proofs and simplifications of reciprocal and quotient identities.

---

## 4. Scale Independence of T-Ratios

!!! info "Coming Soon"
    Geometric proof using similar triangles ($\triangle ABC \sim \triangle ADE$) proving T-ratios are invariant under uniform scaling.

---

## 5. Evaluating T-Ratios using Pythagoras Theorem

!!! info "Coming Soon"
    Step-by-step $k$-method to find all 5 remaining trigonometric ratios given any single ratio.

---

## 6. T-Ratios of Specific Angles

!!! info "Coming Soon"
    Geometric derivations for $0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$ and master reference table.

---

## 7. Core Concept Walkthroughs

!!! info "Coming Soon"
    Interactive problem walkthroughs and step-by-step guidance.

---

## 8. High-Yield Practice Problems

!!! info "Coming Soon"
    Graded practice set with full solutions.
