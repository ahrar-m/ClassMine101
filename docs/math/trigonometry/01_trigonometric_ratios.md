# Trigonometric Ratios

Welcome to the Trigonometric Ratios chapter. Here we explore the fundamental relationships between the angles and side lengths of right-angled triangles.

---

## Topics

<div class="grid cards" markdown>

-   :material-triangle-outline: **Introduction & Right Triangle Geometry**

    ---

    Learn what trigonometry means and how to identify the Hypotenuse, Opposite, and Adjacent sides of a right triangle.

    [:octicons-arrow-right-24: Read Guide](#introduction-right-triangle-geometry)

</div>

---

## Introduction & Right Triangle Geometry

### Origin of the Name

The word Trigonometry comes from three simple Greek words:

* tri — meaning three
* gon — meaning sides
* metron — meaning measure

Together, trigonometry means measuring the three sides and angles of a triangle.

---

### Parts of a Right-Angled Triangle

In a right-angled triangle, one angle measures exactly $90^\circ$. We classify the three sides based on a chosen reference angle:

* **Hypotenuse**: The longest side of the triangle, located directly opposite the $90^\circ$ right angle. It stays in the same position regardless of which acute angle you pick.
* **Opposite Side**: The side directly across from your chosen reference angle.
* **Adjacent Side**: The side next to your chosen reference angle (the side that forms the angle along with the hypotenuse).

---

### Reference Angle Side Switcher

The position of the Opposite and Adjacent sides depends on which angle you pick as your reference angle. Try selecting Angle A or Angle C below to see how the side roles change on the triangle:

<div class="cm-angle-switcher">
  <div class="cm-switcher-buttons">
    <button id="btn-angle-A" class="cm-switch-btn active" onclick="switchAngle('A')">Reference Angle: Angle A</button>
    <button id="btn-angle-C" class="cm-switch-btn" onclick="switchAngle('C')">Reference Angle: Angle C</button>
  </div>

  <div class="cm-triangle-svg-container">
    <svg class="cm-triangle-svg" viewBox="0 0 420 280" width="420" height="280">
      <!-- Triangle Path fill -->
      <polygon points="50,220 330,220 330,40" fill="rgba(99, 102, 241, 0.04)" stroke="none" />
      
      <!-- Right angle marker at B (330, 220) -->
      <path d="M 305,220 L 305,195 L 330,195" fill="none" stroke="#64748b" stroke-width="2" />
      
      <!-- Angle A Arc (at 50, 220) -->
      <path id="svg-arc-A" d="M 90,220 A 40,40 0 0 0 83,198" fill="none" stroke="#6366f1" stroke-width="3" />
      
      <!-- Angle C Arc (at 330, 40) -->
      <path id="svg-arc-C" d="M 330,80 A 40,40 0 0 1 310,65" fill="none" stroke="#6366f1" stroke-width="3" style="display:none;" />
      
      <!-- Triangle Side Lines -->
      <!-- Side AB (Base): (50,220) to (330,220) -->
      <line id="line-AB" class="cm-svg-line" x1="50" y1="220" x2="330" y2="220" stroke="#10b981" stroke-width="5" />
      
      <!-- Side BC (Height): (330,220) to (330,40) -->
      <line id="line-BC" class="cm-svg-line" x1="330" y1="220" x2="330" y2="40" stroke="#ef4444" stroke-width="5" />
      
      <!-- Side AC (Hypotenuse): (50,220) to (330,40) -->
      <line id="line-AC" class="cm-svg-line" x1="50" y1="220" x2="330" y2="40" stroke="#8b5cf6" stroke-width="5" />
      
      <!-- Vertex Points -->
      <circle cx="50" cy="220" r="5" fill="#6366f1" />
      <circle cx="330" cy="220" r="5" fill="#64748b" />
      <circle cx="330" cy="40" r="5" fill="#6366f1" />
      
      <!-- Vertex Labels -->
      <text x="25" y="235" font-weight="700" font-size="18" fill="#1e293b">A</text>
      <text x="345" y="235" font-weight="700" font-size="18" fill="#1e293b">B (90°)</text>
      <text x="345" y="40" font-weight="700" font-size="18" fill="#1e293b">C</text>
      
      <!-- Side Function Labels -->
      <!-- Hypotenuse label -->
      <text x="160" y="115" class="cm-svg-text" font-weight="700" fill="#8b5cf6" transform="rotate(-32.6, 175, 120)">Hypotenuse (AC)</text>
      
      <!-- Dynamic Side Labels -->
      <text id="lbl-side-ab" x="160" y="248" class="cm-svg-text" font-weight="700" fill="#10b981">Adjacent (AB)</text>
      <text id="lbl-side-bc" x="342" y="135" class="cm-svg-text" font-weight="700" fill="#ef4444">Opposite (BC)</text>
    </svg>
  </div>

  <div class="cm-angle-card" id="angle-card-info">
    <h4 id="card-title">Reference Angle: Angle A</h4>
    <ul class="cm-side-list">
      <li><strong class="tag-hyp">Hypotenuse:</strong> Side AC (opposite the 90° right angle at B)</li>
      <li><strong class="tag-opp" id="desc-opp">Opposite Side:</strong> Side BC (directly across from Angle A)</li>
      <li><strong class="tag-adj" id="desc-adj">Adjacent Side:</strong> Side AB (next to Angle A)</li>
    </ul>
  </div>
</div>

---

### Self-Assessment

Refer to triangle $\triangle PQR$ below (with right angle at vertex $Q$) to answer the questions:

<div class="cm-triangle-svg-container">
  <svg class="cm-triangle-svg" viewBox="0 0 400 240" width="400" height="240">
    <polygon points="50,190 320,190 320,40" fill="rgba(6, 182, 212, 0.04)" stroke="none" />
    <path d="M 298,190 L 298,168 L 320,168" fill="none" stroke="#64748b" stroke-width="2" />
    
    <!-- Lines -->
    <line x1="50" y1="190" x2="320" y2="190" stroke="#06b6d4" stroke-width="4" />
    <line x1="320" y1="190" x2="320" y2="40" stroke="#06b6d4" stroke-width="4" />
    <line x1="50" y1="190" x2="320" y2="40" stroke="#8b5cf6" stroke-width="4" />
    
    <!-- Vertices -->
    <circle cx="50" cy="190" r="5" fill="#06b6d4" />
    <circle cx="320" cy="190" r="5" fill="#64748b" />
    <circle cx="320" cy="40" r="5" fill="#06b6d4" />
    
    <!-- Labels -->
    <text x="25" y="205" font-weight="700" font-size="16" fill="#1e293b">P</text>
    <text x="332" y="205" font-weight="700" font-size="16" fill="#1e293b">Q (90°)</text>
    <text x="332" y="40" font-weight="700" font-size="16" fill="#1e293b">R</text>
    
    <!-- Side Names -->
    <text x="160" y="105" font-size="13" font-weight="600" fill="#8b5cf6" transform="rotate(-29, 170, 110)">Side PR</text>
    <text x="165" y="212" font-size="13" font-weight="600" fill="#06b6d4">Side PQ</text>
    <text x="330" y="120" font-size="13" font-weight="600" fill="#06b6d4">Side QR</text>
  </svg>
</div>

<div class="cm-quiz-container">
  <div class="cm-quiz-card">
    <div class="cm-quiz-question">
      Question 1: Which side is the Hypotenuse in $\triangle PQR$?
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
      Question 2: If your reference angle is Angle P, which side is the Opposite Side?
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
      Question 3: If you switch your reference angle to Angle R, which side is the Adjacent Side?
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
  const cardTitle = document.getElementById('card-title');
  const descOpp = document.getElementById('desc-opp');
  const descAdj = document.getElementById('desc-adj');
  
  const arcA = document.getElementById('svg-arc-A');
  const arcC = document.getElementById('svg-arc-C');
  const lineAB = document.getElementById('line-AB');
  const lineBC = document.getElementById('line-BC');
  const lblAB = document.getElementById('lbl-side-ab');
  const lblBC = document.getElementById('lbl-side-bc');

  if (angle === 'A') {
    btnA.classList.add('active');
    btnC.classList.remove('active');
    cardTitle.innerText = 'Reference Angle: Angle A';
    
    descOpp.innerHTML = 'Opposite Side: Side BC (directly across from Angle A)';
    descAdj.innerHTML = 'Adjacent Side: Side AB (next to Angle A)';
    
    arcA.style.display = 'block';
    arcC.style.display = 'none';
    
    lineAB.setAttribute('stroke', '#10b981');
    lineBC.setAttribute('stroke', '#ef4444');
    
    lblAB.innerText = 'Adjacent (AB)';
    lblAB.setAttribute('fill', '#10b981');
    
    lblBC.innerText = 'Opposite (BC)';
    lblBC.setAttribute('fill', '#ef4444');
  } else {
    btnC.classList.add('active');
    btnA.classList.remove('active');
    cardTitle.innerText = 'Reference Angle: Angle C';
    
    descOpp.innerHTML = 'Opposite Side: Side AB (directly across from Angle C)';
    descAdj.innerHTML = 'Adjacent Side: Side BC (next to Angle C)';
    
    arcA.style.display = 'none';
    arcC.style.display = 'block';
    
    lineAB.setAttribute('stroke', '#ef4444');
    lineBC.setAttribute('stroke', '#10b981');
    
    lblAB.innerText = 'Opposite (AB)';
    lblAB.setAttribute('fill', '#ef4444');
    
    lblBC.innerText = 'Adjacent (BC)';
    lblBC.setAttribute('fill', '#10b981');
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
      feedbackEl.innerHTML = 'Correct! Side PR is opposite the 90° right angle at Q, so it is the hypotenuse.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = 'Correct! Side QR is directly across from Angle P, making it the opposite side.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = 'Correct! For Angle R, side QR touches Angle R alongside hypotenuse PR, so it is the adjacent side.';
    }
  } else {
    feedbackEl.className = 'cm-quiz-feedback show incorrect-box';
    if (questionNum === 1) {
      feedbackEl.innerHTML = 'Incorrect. The Hypotenuse is always the side opposite the 90° right angle (Angle Q). That side is PR.';
    } else if (questionNum === 2) {
      feedbackEl.innerHTML = 'Incorrect. The Opposite side is directly across from reference Angle P, which is side QR.';
    } else if (questionNum === 3) {
      feedbackEl.innerHTML = 'Incorrect. For Angle R, side PQ is opposite and QR is the adjacent side.';
    }
  }
}
</script>
