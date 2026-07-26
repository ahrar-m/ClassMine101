# Trigonometric Ratios

Welcome to the **Trigonometric Ratios** chapter. Here we explore the basic relationships between the angles and side lengths of a right-angled triangle.

---

## Topics

<div class="grid cards" markdown>

-   :material-triangle-outline: **Introduction & Right Triangle Geometry**

    ---

    Discover real-life examples, what the word trigonometry means, and how to identify the Hypotenuse, Opposite, and Adjacent sides of a right triangle.

    [:octicons-arrow-right-24: Read Guide](#introduction-right-triangle-geometry)

</div>

---

## Introduction & Right Triangle Geometry

### Real-Life Examples: Why Do We Need Trigonometry?

Imagine these real-world situations:

1. **Standing near a tall tower (like Qutub Minar)**: Imagine you are standing on the ground looking up at the top of the Qutub Minar. A right-angled triangle is formed between your feet, the base of the tower, and the top of the tower. Can you find the height of the tower without actually climbing up to measure it?
2. **Looking across a river**: Imagine a girl sitting on the balcony of a house on a riverbank, looking down at a flower pot on the opposite bank. If you know the height of the balcony, can you find the width of the river?

In both situations, we can easily find the missing heights or distances without measuring them physically! The branch of mathematics that makes this possible is called **Trigonometry**.

---

### Where Does the Word Come From?

The word **Trigonometry** comes from three simple Greek words:

* **tri** — meaning **"three"**
* **gon** — meaning **"sides"**
* **metron** — meaning **"measure"**

Putting them together, **trigonometry simply means "measuring the sides and angles of a triangle"**.

---

### Parts of a Right-Angled Triangle

Trigonometry begins with a **right-angled triangle** (a triangle where one angle is $90^\circ$). 

Consider a right-angled triangle $\triangle ABC$, where the right angle is at vertex $B$ ($\angle B = 90^\circ$). We name the three sides based on a chosen acute angle called the **Reference Angle**:

```
       C
       |\
       | \
       |  \  Hypotenuse
Opposite |   \  (AC)
 (BC)  |    \
       |_____\
       B (AB)  A
      [90°]  (Reference Angle)
     Adjacent
```

1. **Hypotenuse**: The longest side of the triangle, located directly opposite the $90^\circ$ right angle. It **never changes** regardless of which acute angle you pick.
2. **Opposite Side**: The side directly across from your chosen reference angle.
3. **Adjacent Side**: The side next to your chosen reference angle (the side that forms the angle along with the hypotenuse).

---

### Interactive Visual Tool: Switch the Reference Angle

**Crucial Rule**: Swapping your reference angle swaps which side is **Opposite** and which side is **Adjacent**! 

Try clicking the buttons below to see how the side roles change in $\triangle ABC$ (right angle at $B$):

<div class="cm-angle-switcher">
  <div class="cm-switcher-buttons">
    <button id="btn-angle-A" class="cm-switch-btn active" onclick="switchAngle('A')">Reference Angle: Angle A (θ)</button>
    <button id="btn-angle-C" class="cm-switch-btn" onclick="switchAngle('C')">Reference Angle: Angle C (ϕ)</button>
  </div>

  <div class="cm-switcher-display" id="angle-display-box">
    <div class="cm-angle-card">
      <h4 id="display-title">Active Reference Angle: Angle A</h4>
      <ul class="cm-side-list">
        <li><strong class="tag-hyp">Hypotenuse:</strong> Side <span id="side-hyp">AC</span> (opposite the 90° right angle at B)</li>
        <li><strong class="tag-opp">Opposite Side:</strong> Side <span id="side-opp">BC</span> (directly across from Angle A)</li>
        <li><strong class="tag-adj">Adjacent Side:</strong> Side <span id="side-adj">AB</span> (next to Angle A)</li>
      </ul>
      <p class="cm-switcher-tip" id="switcher-tip">
        Notice that side <strong>BC</strong> is across from Angle A, so it is the Opposite side!
      </p>
    </div>
  </div>
</div>

---

### Self-Assessment Quiz: Test Your Understanding

Test what you have learned about triangle sides using right triangle $\triangle PQR$ (where $\angle Q = 90^\circ$):

<div class="cm-quiz-container">
  <div class="cm-quiz-header">
    <h3><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 22g-2 0-3.5-1.5T2 17V7g0-2 1.5-1.5T7 2h10g2 0 3.5 1.5T24 7v10g0 2-1.5 1.5T20 22H9zm3-4h2v-2h-2v2zm1-4q.825 0 1.413-.587Q15 12.825 15 12t-.587-1.413Q13.825 10 13 10t-1.413.587Q11 11.175 11 12t.587 1.413Q12.175 14 13 14z"/></svg></span> Quick Concept Check</h3>
    <p>Triangle setup: Right-angled triangle $\triangle PQR$ with right angle at vertex $Q$ ($\angle Q = 90^\circ$).</p>
  </div>

  <div class="cm-quiz-card">
    <div class="cm-quiz-question">
      <strong>Question 1:</strong> Which side is the <strong>Hypotenuse</strong> in $\triangle PQR$?
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
      <strong>Question 2:</strong> If your reference angle is <strong>Angle P</strong>, which side is the <strong>Opposite Side</strong>?
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
      <strong>Question 3:</strong> If you switch your reference angle to <strong>Angle R</strong>, which side is now the <strong>Adjacent Side</strong>?
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
function switchAngle(angle) {
  const btnA = document.getElementById('btn-angle-A');
  const btnC = document.getElementById('btn-angle-C');
  const title = document.getElementById('display-title');
  const hyp = document.getElementById('side-hyp');
  const opp = document.getElementById('side-opp');
  const adj = document.getElementById('side-adj');
  const tip = document.getElementById('switcher-tip');

  if (angle === 'A') {
    btnA.classList.add('active');
    btnC.classList.remove('active');
    title.innerText = 'Active Reference Angle: Angle A';
    hyp.innerText = 'AC';
    opp.innerText = 'BC';
    adj.innerText = 'AB';
    tip.innerHTML = 'For Angle A: Side <strong>BC</strong> is across (Opposite) and side <strong>AB</strong> is next to it (Adjacent).';
  } else {
    btnC.classList.add('active');
    btnA.classList.remove('active');
    title.innerText = 'Active Reference Angle: Angle C';
    hyp.innerText = 'AC';
    opp.innerText = 'AB';
    adj.innerText = 'BC';
    tip.innerHTML = 'For Angle C: Side <strong>AB</strong> is across (Opposite) and side <strong>BC</strong> is next to it (Adjacent). Notice how Opposite and Adjacent swapped!';
  }
}

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
      feedbackEl.innerHTML = '<strong>Correct!</strong> Side <em>PR</em> is opposite the 90° right angle at Q, so it is the hypotenuse.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = '<strong>Correct!</strong> Side <em>QR</em> is directly across from Angle P, making it the opposite side.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = '<strong>Correct!</strong> For Angle R, side <em>QR</em> touches Angle R (along with hypotenuse PR), so it is the adjacent side.';
    }
  } else {
    feedbackEl.className = 'cm-quiz-feedback show incorrect-box';
    if (questionNum === 1) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> The Hypotenuse is always the side opposite the 90° right angle (Angle Q). That side is <em>PR</em>.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> The Opposite side is directly across from reference Angle P, which is side <em>QR</em>.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = '<strong>Incorrect.</strong> For Angle R, side <em>PQ</em> is opposite and <em>QR</em> is the adjacent side.';
    }
  }
}
</script>
