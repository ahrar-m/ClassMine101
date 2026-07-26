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

<div class="cm-discovery-module" id="discovery-module">

  <!-- Interactive SVG Triangle Canvas -->
  <div class="cm-triangle-svg-container">
    <svg class="cm-triangle-svg" viewBox="0 0 440 260" width="440" height="260">
      <!-- Triangle Fill -->
      <polygon points="60,210 360,210 360,40" fill="rgba(99, 102, 241, 0.04)" stroke="none" />
      
      <!-- 90 Deg Marker -->
      <path id="svg-90-marker" d="M 335,210 L 335,185 L 360,185" fill="none" stroke="#94a3b8" stroke-width="2.5" />
      <text id="lbl-90-deg" x="312" y="202" class="cm-svg-label" font-size="13" font-weight="700" fill="#94a3b8" style="opacity: 0; display: none;">90°</text>

      <!-- Bottom-Left Angle Arc (Theta) -->
      <path id="svg-arc-theta" d="M 95,210 A 35,35 0 0 0 88,190" fill="none" stroke="#94a3b8" stroke-width="3" />
      <text id="lbl-theta" x="100" y="200" class="cm-svg-label" font-size="15" font-weight="800" fill="#6366f1" style="opacity: 0; display: none;">θ</text>
      
      <!-- Top-Right Angle Arc (Phi) -->
      <path id="svg-arc-phi" d="M 360,75 A 35,35 0 0 1 342,62" fill="none" stroke="#94a3b8" stroke-width="3" />
      <text id="lbl-phi" x="340" y="85" class="cm-svg-label" font-size="15" font-weight="800" fill="#06b6d4" style="opacity: 0; display: none;">φ</text>

      <!-- Triangle Side Visible Lines -->
      <line id="line-bottom" class="cm-svg-line" x1="60" y1="210" x2="360" y2="210" stroke="#94a3b8" stroke-width="4.5" />
      <line id="line-vertical" class="cm-svg-line" x1="360" y1="210" x2="360" y2="40" stroke="#94a3b8" stroke-width="4.5" />
      <line id="line-hypotenuse" class="cm-svg-line" x1="60" y1="210" x2="360" y2="40" stroke="#94a3b8" stroke-width="4.5" />
      
      <!-- Vertex Points -->
      <circle cx="60" cy="210" r="5" fill="#64748b" />
      <circle cx="360" cy="210" r="5" fill="#64748b" />
      <circle cx="360" cy="40" r="5" fill="#64748b" />

      <!-- Thick Invisible Hitboxes for Easy Mouse/Touch Interaction -->
      <line class="cm-hitbox" x1="60" y1="210" x2="360" y2="40" stroke="transparent" stroke-width="28" onclick="handleTriangleClick('hypotenuse')" onmouseenter="highlightHover('hypotenuse', true)" onmouseleave="highlightHover('hypotenuse', false)" />
      <line class="cm-hitbox" x1="360" y1="210" x2="360" y2="40" stroke="transparent" stroke-width="28" onclick="handleTriangleClick('vertical')" onmouseenter="highlightHover('vertical', true)" onmouseleave="highlightHover('vertical', false)" />
      <line class="cm-hitbox" x1="60" y1="210" x2="360" y2="210" stroke="transparent" stroke-width="28" onclick="handleTriangleClick('bottom')" onmouseenter="highlightHover('bottom', true)" onmouseleave="highlightHover('bottom', false)" />
      
      <circle class="cm-hitbox" cx="360" cy="210" r="32" fill="transparent" onclick="handleTriangleClick('right-angle')" />
      <circle class="cm-hitbox" cx="60" cy="210" r="32" fill="transparent" onclick="handleTriangleClick('angle-theta')" />
      <circle class="cm-hitbox" cx="360" cy="40" r="32" fill="transparent" onclick="handleTriangleClick('angle-phi')" />

      <!-- Dynamic SVG Labels (Invisible until discovered) -->
      <text id="lbl-hypotenuse-text" x="160" y="110" class="cm-svg-label" font-weight="700" font-size="14" fill="#8b5cf6" transform="rotate(-29.5, 175, 115)" style="opacity: 0; display: none;">Hypotenuse (Longest Side)</text>
      <text id="lbl-bottom-text" x="175" y="235" class="cm-svg-label" font-weight="700" font-size="14" fill="#64748b" style="opacity: 0; display: none;">Base Side</text>
      <text id="lbl-vertical-text" x="372" y="130" class="cm-svg-label" font-weight="700" font-size="14" fill="#64748b" style="opacity: 0; display: none;">Vertical Side</text>
    </svg>
  </div>

  <!-- Prompt Banner -->
  <div class="cm-prompt-box" id="discovery-prompt">
    <strong>Step 1:</strong> Click on the <span class="highlight-target">90° right angle corner</span> or the <span class="highlight-target">slanted side</span> to locate the Hypotenuse.
  </div>

  <!-- Feedback & Instructions Box -->
  <div class="cm-discovery-feedback" id="discovery-feedback">
    Click on the 90° corner square symbol or the slanted side on the triangle to begin!
  </div>

  <!-- Step 2: Parallel Two-Column Reference Angle Choice (Hidden until Step 1 complete) -->
  <div class="cm-angle-columns" id="angle-columns" style="display: none;">
    <div class="cm-angle-column" id="col-theta">
      <h4>Reference Angle: Bottom-Left (θ)</h4>
      <p class="cm-col-desc">Select this angle to see side roles relative to Angle θ:</p>
      <button class="cm-discovery-btn cm-btn-column" id="btn-select-theta" onclick="selectReferenceAngle('theta')">Select Angle θ</button>
      <div class="cm-col-results" id="res-theta" style="display: none;">
        <p class="cm-step-action">Next, click the side directly across from Angle θ to mark <strong>Opposite</strong>.</p>
        <button class="cm-discovery-btn cm-btn-sub" id="btn-opp-theta" onclick="confirmOpposite('theta')">Mark Opposite Side →</button>
        <ul class="cm-role-list" id="list-theta" style="display: none;">
          <li><strong style="color:#ef4444;">Opposite:</strong> Vertical Side</li>
          <li><strong style="color:#10b981;">Adjacent:</strong> Bottom Side</li>
        </ul>
      </div>
    </div>

    <div class="cm-angle-column" id="col-phi">
      <h4>Reference Angle: Top-Right (φ)</h4>
      <p class="cm-col-desc">Select this angle to see side roles relative to Angle φ:</p>
      <button class="cm-discovery-btn cm-btn-column" id="btn-select-phi" onclick="selectReferenceAngle('phi')">Select Angle φ</button>
      <div class="cm-col-results" id="res-phi" style="display: none;">
        <p class="cm-step-action">Next, click the side directly across from Angle φ to mark <strong>Opposite</strong>.</p>
        <button class="cm-discovery-btn cm-btn-sub" id="btn-opp-phi" onclick="confirmOpposite('phi')">Mark Opposite Side →</button>
        <ul class="cm-role-list" id="list-phi" style="display: none;">
          <li><strong style="color:#ef4444;">Opposite:</strong> Bottom Side</li>
          <li><strong style="color:#10b981;">Adjacent:</strong> Vertical Side</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Controls -->
  <div class="cm-discovery-actions">
    <button class="cm-discovery-btn cm-btn-secondary" onclick="resetExplorer()">Reset Explorer</button>
  </div>
</div>

<script>
let isHypotenuseDiscovered = false;
let selectedAngle = null; // 'theta' or 'phi'

function highlightHover(side, isHover) {
  if (!isHover) {
    if (!isHypotenuseDiscovered && side === 'hypotenuse') {
      document.getElementById('line-hypotenuse').setAttribute('stroke', '#94a3b8');
      document.getElementById('line-hypotenuse').setAttribute('stroke-width', '4.5');
    }
    return;
  }
  const el = document.getElementById(side === 'hypotenuse' ? 'line-hypotenuse' : (side === 'vertical' ? 'line-vertical' : 'line-bottom'));
  if (el) {
    el.setAttribute('stroke-width', '6.5');
  }
}

function handleTriangleClick(target) {
  if (!isHypotenuseDiscovered) {
    if (target === 'right-angle' || target === 'hypotenuse') {
      isHypotenuseDiscovered = true;
      
      // Highlight Hypotenuse
      const lineHyp = document.getElementById('line-hypotenuse');
      lineHyp.setAttribute('stroke', '#8b5cf6');
      lineHyp.setAttribute('stroke-width', '6.5');
      
      document.getElementById('svg-90-marker').setAttribute('stroke', '#8b5cf6');
      const lbl90 = document.getElementById('lbl-90-deg');
      lbl90.style.display = 'block';
      lbl90.style.opacity = '1';
      lbl90.setAttribute('fill', '#8b5cf6');

      const lblHyp = document.getElementById('lbl-hypotenuse-text');
      lblHyp.style.display = 'block';
      lblHyp.style.opacity = '1';

      const prompt = document.getElementById('discovery-prompt');
      prompt.innerHTML = '<strong>Step 2:</strong> Hypotenuse identified! Now select a <strong>Reference Angle</strong> below to discover Opposite & Adjacent sides.';

      const feedback = document.getElementById('discovery-feedback');
      feedback.className = 'cm-discovery-feedback success-box';
      feedback.innerHTML = '<strong>Hypotenuse Discovered!</strong> The side opposite the 90° right angle is the <strong>Hypotenuse</strong> (the longest side). Now pick an acute reference angle below to compare side roles!';

      document.getElementById('angle-columns').style.display = 'flex';
    } else {
      const feedback = document.getElementById('discovery-feedback');
      feedback.className = 'cm-discovery-feedback info-box';
      feedback.innerHTML = '<em>Hint:</em> Click on the 90° corner square or the slanted side directly opposite to it.';
    }
  } else {
    // If user clicks sides in Step 2
    if (selectedAngle === 'theta') {
      if (target === 'vertical') {
        confirmOpposite('theta');
      } else if (target === 'bottom') {
        const feedback = document.getElementById('discovery-feedback');
        feedback.className = 'cm-discovery-feedback info-box';
        feedback.innerHTML = '<em>Hint:</em> For Angle θ (bottom-left), the <strong>Opposite</strong> side is directly across from it (the Vertical side).';
      }
    } else if (selectedAngle === 'phi') {
      if (target === 'bottom') {
        confirmOpposite('phi');
      } else if (target === 'vertical') {
        const feedback = document.getElementById('discovery-feedback');
        feedback.className = 'cm-discovery-feedback info-box';
        feedback.innerHTML = '<em>Hint:</em> For Angle φ (top-right), the <strong>Opposite</strong> side is directly across from it (the Bottom side).';
      }
    }
  }
}

function selectReferenceAngle(angle) {
  if (!isHypotenuseDiscovered) return;

  selectedAngle = angle;
  const colTheta = document.getElementById('col-theta');
  const colPhi = document.getElementById('col-phi');

  const arcTheta = document.getElementById('svg-arc-theta');
  const arcPhi = document.getElementById('svg-arc-phi');
  const lblTheta = document.getElementById('lbl-theta');
  const lblPhi = document.getElementById('lbl-phi');

  const resTheta = document.getElementById('res-theta');
  const resPhi = document.getElementById('res-phi');

  if (angle === 'theta') {
    colTheta.classList.add('active');
    colPhi.classList.remove('active');

    arcTheta.setAttribute('stroke', '#6366f1');
    arcTheta.setAttribute('stroke-width', '4.5');
    lblTheta.style.display = 'block';
    lblTheta.style.opacity = '1';

    arcPhi.setAttribute('stroke', '#94a3b8');
    arcPhi.setAttribute('stroke-width', '3');

    resTheta.style.display = 'block';
    resPhi.style.display = 'none';

    // Clear previous side highlights except hypotenuse
    document.getElementById('line-vertical').setAttribute('stroke', '#94a3b8');
    document.getElementById('line-bottom').setAttribute('stroke', '#94a3b8');

    const feedback = document.getElementById('discovery-feedback');
    feedback.className = 'cm-discovery-feedback info-box';
    feedback.innerHTML = 'Reference Angle <strong>θ (Bottom-Left)</strong> chosen. Click on the side directly across from Angle θ (or click the button) to mark the <strong>Opposite Side</strong>.';
  } else {
    colPhi.classList.add('active');
    colTheta.classList.remove('active');

    arcPhi.setAttribute('stroke', '#06b6d4');
    arcPhi.setAttribute('stroke-width', '4.5');
    lblPhi.style.display = 'block';
    lblPhi.style.opacity = '1';

    arcTheta.setAttribute('stroke', '#94a3b8');
    arcTheta.setAttribute('stroke-width', '3');

    resPhi.style.display = 'block';
    resTheta.style.display = 'none';

    // Clear previous side highlights except hypotenuse
    document.getElementById('line-vertical').setAttribute('stroke', '#94a3b8');
    document.getElementById('line-bottom').setAttribute('stroke', '#94a3b8');

    const feedback = document.getElementById('discovery-feedback');
    feedback.className = 'cm-discovery-feedback info-box';
    feedback.innerHTML = 'Reference Angle <strong>φ (Top-Right)</strong> chosen. Click on the side directly across from Angle φ (or click the button) to mark the <strong>Opposite Side</strong>.';
  }
}

function confirmOpposite(angle) {
  const lineVert = document.getElementById('line-vertical');
  const lineBot = document.getElementById('line-bottom');
  const lblVert = document.getElementById('lbl-vertical-text');
  const lblBot = document.getElementById('lbl-bottom-text');

  lblVert.style.display = 'block';
  lblVert.style.opacity = '1';
  lblBot.style.display = 'block';
  lblBot.style.opacity = '1';

  if (angle === 'theta') {
    lineVert.setAttribute('stroke', '#ef4444');
    lineVert.setAttribute('stroke-width', '6');
    lblVert.innerText = 'Opposite (to θ)';
    lblVert.setAttribute('fill', '#ef4444');

    lineBot.setAttribute('stroke', '#10b981');
    lineBot.setAttribute('stroke-width', '6');
    lblBot.innerText = 'Adjacent (to θ)';
    lblBot.setAttribute('fill', '#10b981');

    document.getElementById('list-theta').style.display = 'block';
    document.getElementById('btn-opp-theta').style.display = 'none';

    const feedback = document.getElementById('discovery-feedback');
    feedback.className = 'cm-discovery-feedback success-box';
    feedback.innerHTML = '<strong>Side Classification Complete for Angle θ!</strong><br/>' +
      '• <span style="color:#ef4444; font-weight:700;">Opposite Side:</span> Vertical side (directly across from θ).<br/>' +
      '• <span style="color:#10b981; font-weight:700;">Adjacent Side:</span> Bottom side (next to θ).<br/>' +
      '<em>Try selecting Angle φ in the right column to compare how Opposite and Adjacent swap roles!</em>';
  } else {
    lineBot.setAttribute('stroke', '#ef4444');
    lineBot.setAttribute('stroke-width', '6');
    lblBot.innerText = 'Opposite (to φ)';
    lblBot.setAttribute('fill', '#ef4444');

    lineVert.setAttribute('stroke', '#10b981');
    lineVert.setAttribute('stroke-width', '6');
    lblVert.innerText = 'Adjacent (to φ)';
    lblVert.setAttribute('fill', '#10b981');

    document.getElementById('list-phi').style.display = 'block';
    document.getElementById('btn-opp-phi').style.display = 'none';

    const feedback = document.getElementById('discovery-feedback');
    feedback.className = 'cm-discovery-feedback success-box';
    feedback.innerHTML = '<strong>Side Classification Complete for Angle φ!</strong><br/>' +
      '• <span style="color:#ef4444; font-weight:700;">Opposite Side:</span> Bottom side (directly across from φ).<br/>' +
      '• <span style="color:#10b981; font-weight:700;">Adjacent Side:</span> Vertical side (next to φ).<br/>' +
      '<em>Try selecting Angle θ in the left column to compare how Opposite and Adjacent swap roles!</em>';
  }
}

function resetExplorer() {
  isHypotenuseDiscovered = false;
  selectedAngle = null;

  document.getElementById('line-hypotenuse').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-hypotenuse').setAttribute('stroke-width', '4.5');
  document.getElementById('line-vertical').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-vertical').setAttribute('stroke-width', '4.5');
  document.getElementById('line-bottom').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-bottom').setAttribute('stroke-width', '4.5');

  document.getElementById('svg-90-marker').setAttribute('stroke', '#94a3b8');
  document.getElementById('svg-arc-theta').setAttribute('stroke', '#94a3b8');
  document.getElementById('svg-arc-phi').setAttribute('stroke', '#94a3b8');

  ['lbl-90-deg', 'lbl-theta', 'lbl-phi', 'lbl-hypotenuse-text', 'lbl-bottom-text', 'lbl-vertical-text'].forEach(id => {
    const el = document.getElementById(id);
    el.style.opacity = '0';
    el.style.display = 'none';
  });

  document.getElementById('angle-columns').style.display = 'none';
  document.getElementById('col-theta').classList.remove('active');
  document.getElementById('col-phi').classList.remove('active');
  document.getElementById('res-theta').style.display = 'none';
  document.getElementById('res-phi').style.display = 'none';
  document.getElementById('list-theta').style.display = 'none';
  document.getElementById('list-phi').style.display = 'none';
  document.getElementById('btn-opp-theta').style.display = 'inline-block';
  document.getElementById('btn-opp-phi').style.display = 'inline-block';

  document.getElementById('discovery-prompt').innerHTML = '<strong>Step 1:</strong> Click on the <span class="highlight-target">90° right angle corner</span> or the <span class="highlight-target">slanted side</span> to locate the Hypotenuse.';
  const feedback = document.getElementById('discovery-feedback');
  feedback.className = 'cm-discovery-feedback';
  feedback.innerHTML = 'Click on the 90° corner square symbol or the slanted side on the triangle to begin!';
}
</script>


