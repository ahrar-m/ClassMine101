# Trigonometric Ratios

Welcome to the **Trigonometric Ratios** chapter. Here we explore the fundamental relationships between the acute angles and side lengths of right-angled triangles.

---

## Topics

<div class="grid cards" markdown>

-   :material-triangle-outline: **Introduction & Right Triangle Geometry**

    ---

    Understand what trigonometry is, its etymological roots, and how to identify the Hypotenuse, Opposite, and Adjacent sides of a right triangle.

    [:octicons-arrow-right-24: Read Guide](#introduction-right-triangle-geometry)

</div>

---

## Introduction & Right Triangle Geometry

### What is Trigonometry?

The word **Trigonometry** is derived from three Greek root words:

* **Trigonon** ($\tau\rho\acute{\iota}\gamma\omega\nu o\nu$) – meaning **"Triangle"**
* **Metron** ($\mu\acute{\epsilon}\tau\rho o\nu$) – meaning **"Measure"**

Together, **Trigonometry** literally translates to **"the measurement of triangles"**. 

In modern mathematics, trigonometry is the branch that investigates the precise quantitative relationships between the **side lengths** and **angles** of triangles. While it originated in astronomy and navigation to calculate distances to stars and across oceans, today it forms the foundation of physics, engineering, computer graphics, architecture, and signal processing.

---

### The Anatomy of a Right-Angled Triangle

Trigonometric ratios are initially defined using a **right-angled triangle**—a triangle in which one interior angle measures exactly $90^\circ$.

Consider a right-angled triangle $\triangle ABC$, where the right angle is located at vertex $B$ ($\angle B = 90^\circ$).

```
       C
       |\
       | \
       |  \  Hypotenuse
Opposite |   \  (c)
  (a)  |    \
       |_____\
       B  (b)  A
       [90°]  (θ = Reference Angle)
     Adjacent
```

In any right-angled triangle, we classify the three sides into three distinct roles based on a chosen acute angle called the **Reference Angle** ($\theta$):

#### 1. Hypotenuse
* **Definition**: The side lying directly opposite to the $90^\circ$ right angle.
* **Key Property**: It is always the **longest side** of the right triangle.
* **Fixed Nature**: The hypotenuse never changes regardless of which acute angle you select as your reference angle.

#### 2. Opposite Side (Perpendicular)
* **Definition**: The side situated directly across from the chosen reference angle $\theta$.
* **Key Property**: It does not touch the vertex of reference angle $\theta$.

#### 3. Adjacent Side (Base)
* **Definition**: The side located next to the reference angle $\theta$.
* **Key Property**: Together with the hypotenuse, it forms the reference angle $\theta$.

---

### Critical Concept: The Choice of Reference Angle Matters!

A common mistake is assuming that the vertical side is always "opposite" and the horizontal side is always "adjacent". **Opposite and Adjacent sides depend entirely on which angle you choose as your reference.**

Let's observe how side designations change in $\triangle ABC$ (right-angled at $B$):

| Reference Angle | Hypotenuse | Opposite Side | Adjacent Side |
| :--- | :--- | :--- | :--- |
| **Angle $A$ ($\theta = \angle A$)** | Side $AC$ | Side $BC$ | Side $AB$ |
| **Angle $C$ ($\phi = \angle C$)** | Side $AC$ | Side $AB$ | Side $BC$ |

!!! tip "Key Takeaway"
    - The **Hypotenuse** is always fixed (opposite the $90^\circ$ angle).
    - Swapping the reference angle from $\angle A$ to $\angle C$ **swaps the Opposite and Adjacent sides**!

---

### Interactive Concept Quiz: Test Your Understanding

Use the visual triangle below to test your understanding of hypotenuse, opposite, and adjacent sides!

<div class="cm-quiz-container">
  <div class="cm-quiz-header">
    <h3><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 22g-2 0-3.5-1.5T2 17V7g0-2 1.5-1.5T7 2h10g2 0 3.5 1.5T24 7v10g0 2-1.5 1.5T20 22H9zm3-4h2v-2h-2v2zm1-4q.825 0 1.413-.587Q15 12.825 15 12t-.587-1.413Q13.825 10 13 10t-1.413.587Q11 11.175 11 12t.587 1.413Q12.175 14 13 14z"/></svg></span> Quick Self-Assessment Quiz</h3>
    <p>Target Triangle: $\triangle PQR$ with right angle at $Q$ ($\angle Q = 90^\circ$).</p>
  </div>

  <div class="cm-quiz-card">
    <div class="cm-quiz-question">
      <strong>Question 1:</strong> In right-angled triangle $\triangle PQR$ ($\angle Q = 90^\circ$), which side is the <strong>Hypotenuse</strong>?
    </div>
    <div class="cm-quiz-options" id="q1-options">
      <button class="cm-quiz-opt" onclick="checkAnswer(1, 'PQ', false)">Side PQ</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(1, 'PR', true)">Side PR</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(1, 'QR', false)">Side QR</button>
    </div>
    <div class="cm-quiz-feedback" id="q1-feedback"></div>
  </div>

  <div class="cm-quiz-card">
    <div class="cm-quiz-question">
      <strong>Question 2:</strong> If we choose <strong>$\angle P$</strong> as our reference angle, which side is the <strong>Opposite Side</strong>?
    </div>
    <div class="cm-quiz-options" id="q2-options">
      <button class="cm-quiz-opt" onclick="checkAnswer(2, 'PQ', false)">Side PQ</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(2, 'PR', false)">Side PR</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(2, 'QR', true)">Side QR</button>
    </div>
    <div class="cm-quiz-feedback" id="q2-feedback"></div>
  </div>

  <div class="cm-quiz-card">
    <div class="cm-quiz-question">
      <strong>Question 3:</strong> If we choose <strong>$\angle R$</strong> as our reference angle, which side is the <strong>Adjacent Side</strong>?
    </div>
    <div class="cm-quiz-options" id="q3-options">
      <button class="cm-quiz-opt" onclick="checkAnswer(3, 'PQ', false)">Side PQ</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(3, 'PR', false)">Side PR</button>
      <button class="cm-quiz-opt" onclick="checkAnswer(3, 'QR', true)">Side QR</button>
    </div>
    <div class="cm-quiz-feedback" id="q3-feedback"></div>
  </div>
</div>

<script>
function checkAnswer(questionNum, selectedOpt, isCorrect) {
  const feedbackEl = document.getElementById(`q${questionNum}-feedback`);
  const optionsEl = document.getElementById(`q${questionNum}-options`);
  const buttons = optionsEl.querySelectorAll('button');
  
  buttons.forEach(btn => {
    btn.disabled = true;
    if (btn.innerText.includes(selectedOpt)) {
      if (isCorrect) {
        btn.classList.add('correct');
      } else {
        btn.classList.add('incorrect');
      }
    }
  });

  if (isCorrect) {
    feedbackEl.className = 'cm-quiz-feedback show correct-box';
    if (questionNum === 1) {
      feedbackEl.innerHTML = '<strong>Correct!</strong> Side <em>PR</em> lies directly opposite to the $90^\\circ$ angle at $Q$, making it the hypotenuse.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = '<strong>Correct!</strong> For reference angle $\\angle P$, side <em>QR</em> is directly opposite across the triangle.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = '<strong>Correct!</strong> For reference angle $\\angle R$, side <em>QR</em> is adjacent to angle $R$ (forming angle $R$ alongside hypotenuse $PR$).';
    }
  } else {
    feedbackEl.className = 'cm-quiz-feedback show incorrect-box';
    if (questionNum === 1) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> Remember: The Hypotenuse is always the side opposite the $90^\\circ$ right angle ($\angle Q$). That side is <em>PR</em>.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> The Opposite side is the side directly across from reference angle $\\angle P$, which is side <em>QR</em>.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> For angle $\\angle R$, side <em>PQ</em> is opposite, <em>PR</em> is hypotenuse, and <em>QR</em> is the adjacent side.';
    }
  }
  
  if (window.MathJax) {
    window.MathJax.typesetPromise([feedbackEl]);
  }
}
</script>
