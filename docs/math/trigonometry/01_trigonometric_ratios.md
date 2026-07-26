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

### Guided Interactive Discovery: Parts of a Right Triangle

Explore the parts of a right triangle step-by-step without relying on vertex names:

<div class="cm-discovery-module" id="discovery-module">
  <!-- Step Tracker Header -->
  <div class="cm-step-tracker">
    <div class="cm-step-badge active" id="step-badge-1">
      <span class="step-num">1</span>
      <span class="step-text">Find 90° & Hypotenuse</span>
    </div>
    <div class="cm-step-divider"></div>
    <div class="cm-step-badge" id="step-badge-2">
      <span class="step-num">2</span>
      <span class="step-text">Pick Reference Angle (θ)</span>
    </div>
    <div class="cm-step-divider"></div>
    <div class="cm-step-badge" id="step-badge-3">
      <span class="step-num">3</span>
      <span class="step-text">Identify Opposite & Adjacent</span>
    </div>
  </div>

  <!-- Instruction Banner -->
  <div class="cm-discovery-prompt" id="discovery-prompt">
    <strong>Step 1:</strong> Click on the <span class="highlight-target">90° corner square</span> or the <span class="highlight-target">slanted side opposite to it</span> to locate the Hypotenuse.
  </div>

  <!-- Interactive SVG Triangle Canvas -->
  <div class="cm-triangle-svg-container">
    <svg class="cm-triangle-svg" viewBox="0 0 440 280" width="440" height="280">
      <!-- Triangle Path fill -->
      <polygon points="60,230 360,230 360,40" fill="rgba(99, 102, 241, 0.05)" stroke="none" />
      
      <!-- Right angle marker at corner (360, 230) -->
      <path id="svg-90-marker" class="cm-svg-clickable" d="M 335,230 L 335,205 L 360,205" fill="rgba(99, 102, 241, 0.1)" stroke="#64748b" stroke-width="2.5" onclick="handleDiscoveryClick('right-angle')" />
      <text id="lbl-90-deg" x="312" y="222" font-size="13" font-weight="700" fill="#64748b">90°</text>

      <!-- Reference Angle Arc (Bottom Left angle: 60, 230) -->
      <path id="svg-ref-arc" class="cm-svg-clickable" d="M 105,230 A 45,45 0 0 0 98,206" fill="none" stroke="#94a3b8" stroke-width="4" onclick="handleDiscoveryClick('ref-angle')" />
      <text id="lbl-ref-theta" x="112" y="218" font-size="16" font-weight="800" fill="#94a3b8" style="display:none;">θ</text>
      
      <!-- Side 1: Bottom Side -->
      <line id="line-bottom" class="cm-svg-line cm-svg-clickable" x1="60" y1="230" x2="360" y2="230" stroke="#94a3b8" stroke-width="5" onclick="handleDiscoveryClick('side-bottom')" />
      
      <!-- Side 2: Vertical Side -->
      <line id="line-vertical" class="cm-svg-line cm-svg-clickable" x1="360" y1="230" x2="360" y2="40" stroke="#94a3b8" stroke-width="5" onclick="handleDiscoveryClick('side-vertical')" />
      
      <!-- Side 3: Slanted Side (Hypotenuse) -->
      <line id="line-hypotenuse" class="cm-svg-line cm-svg-clickable" x1="60" y1="230" x2="360" y2="40" stroke="#94a3b8" stroke-width="5" onclick="handleDiscoveryClick('hypotenuse')" />
      
      <!-- Vertices (Unlabeled) -->
      <circle cx="60" cy="230" r="6" fill="#6366f1" />
      <circle cx="360" cy="230" r="6" fill="#64748b" />
      <circle cx="360" cy="40" r="6" fill="#6366f1" />
      
      <!-- Dynamic SVG Text Labels -->
      <text id="lbl-hypotenuse" x="170" y="120" class="cm-svg-text" font-weight="700" fill="#8b5cf6" transform="rotate(-32.3, 185, 125)" style="opacity: 0.2;">Hypotenuse (Longest Side)</text>
      <text id="lbl-adjacent" x="175" y="255" class="cm-svg-text" font-weight="700" fill="#10b981" style="opacity: 0.2;">Adjacent Side</text>
      <text id="lbl-opposite" x="370" y="140" class="cm-svg-text" font-weight="700" fill="#ef4444" style="opacity: 0.2;">Opposite Side</text>
    </svg>
  </div>

  <!-- Interactive Feedback & Explanation Box -->
  <div class="cm-discovery-feedback" id="discovery-feedback">
    Click on the 90° corner square or the slanted hypotenuse side to begin!
  </div>

  <!-- Control Actions -->
  <div class="cm-discovery-actions">
    <button class="cm-discovery-btn cm-btn-secondary" id="btn-reset-discovery" onclick="resetDiscoveryModule()">Reset Explorer</button>
    <button class="cm-discovery-btn cm-btn-primary" id="btn-next-step" onclick="advanceDiscoveryStep()" disabled>Next Step →</button>
  </div>
</div>

<script>
let currentStep = 1;
let stepCompleted = [false, false, false];

function handleDiscoveryClick(target) {
  const feedback = document.getElementById('discovery-feedback');
  const nextBtn = document.getElementById('btn-next-step');

  if (currentStep === 1) {
    if (target === 'right-angle' || target === 'hypotenuse') {
      document.getElementById('line-hypotenuse').setAttribute('stroke', '#8b5cf6');
      document.getElementById('line-hypotenuse').setAttribute('stroke-width', '7');
      document.getElementById('svg-90-marker').setAttribute('stroke', '#8b5cf6');
      document.getElementById('svg-90-marker').setAttribute('fill', 'rgba(139, 92, 246, 0.15)');
      document.getElementById('lbl-90-deg').setAttribute('fill', '#8b5cf6');
      document.getElementById('lbl-hypotenuse').style.opacity = '1';

      feedback.className = 'cm-discovery-feedback success-box';
      feedback.innerHTML = '<strong>Spot on!</strong> The side directly opposite the 90° right angle is always the <strong>Hypotenuse</strong>. It is the longest side of a right triangle.';
      
      stepCompleted[0] = true;
      nextBtn.disabled = false;
      document.getElementById('step-badge-1').classList.add('completed');
    } else {
      feedback.className = 'cm-discovery-feedback info-box';
      feedback.innerHTML = '<em>Hint:</em> Look for the side directly across from the 90° corner square symbol.';
    }
  } else if (currentStep === 2) {
    if (target === 'ref-angle' || target === 'side-bottom') {
      document.getElementById('svg-ref-arc').setAttribute('stroke', '#6366f1');
      document.getElementById('svg-ref-arc').setAttribute('stroke-width', '5');
      document.getElementById('lbl-ref-theta').style.display = 'block';
      document.getElementById('lbl-ref-theta').setAttribute('fill', '#6366f1');

      feedback.className = 'cm-discovery-feedback success-box';
      feedback.innerHTML = '<strong>Reference Angle (θ) Selected!</strong> Choosing an acute reference angle allows us to determine which of the remaining two sides is <strong>Opposite</strong> and which is <strong>Adjacent</strong>.';
      
      stepCompleted[1] = true;
      nextBtn.disabled = false;
      document.getElementById('step-badge-2').classList.add('completed');
    } else {
      feedback.className = 'cm-discovery-feedback info-box';
      feedback.innerHTML = '<em>Hint:</em> Click on the angle arc at the bottom-left vertex to choose it as your Reference Angle (θ).';
    }
  } else if (currentStep === 3) {
    if (target === 'side-vertical') {
      feedback.className = 'cm-discovery-feedback success-box';
      feedback.innerHTML = '<strong>Opposite Side:</strong> This side is directly across from Reference Angle θ (it does not touch angle θ).';
    } else if (target === 'side-bottom') {
      feedback.className = 'cm-discovery-feedback success-box';
      feedback.innerHTML = '<strong>Adjacent Side:</strong> This side lies next to Reference Angle θ (it forms angle θ along with the Hypotenuse).';
    } else if (target === 'hypotenuse') {
      feedback.className = 'cm-discovery-feedback info-box';
      feedback.innerHTML = '<strong>Hypotenuse:</strong> The longest side opposite the 90° right angle.';
    }
  }
}

function advanceDiscoveryStep() {
  if (currentStep === 1 && stepCompleted[0]) {
    currentStep = 2;
    updateDiscoveryUI();
  } else if (currentStep === 2 && stepCompleted[1]) {
    currentStep = 3;
    stepCompleted[2] = true;
    updateDiscoveryUI();
  }
}

function updateDiscoveryUI() {
  const prompt = document.getElementById('discovery-prompt');
  const feedback = document.getElementById('discovery-feedback');
  const nextBtn = document.getElementById('btn-next-step');

  document.getElementById('step-badge-1').classList.remove('active');
  document.getElementById('step-badge-2').classList.remove('active');
  document.getElementById('step-badge-3').classList.remove('active');
  document.getElementById(`step-badge-${currentStep}`).classList.add('active');

  if (currentStep === 2) {
    prompt.innerHTML = '<strong>Step 2:</strong> Click on the <span class="highlight-target">bottom-left angle arc</span> to mark your Reference Angle (θ).';
    feedback.className = 'cm-discovery-feedback';
    feedback.innerHTML = 'Select the reference angle arc (θ) on the triangle!';
    nextBtn.disabled = !stepCompleted[1];
  } else if (currentStep === 3) {
    prompt.innerHTML = '<strong>Step 3:</strong> Discover how the remaining sides are classified as <strong>Opposite</strong> and <strong>Adjacent</strong> relative to θ!';
    feedback.className = 'cm-discovery-feedback success-box';
    feedback.innerHTML = '<strong>Complete Triangle Anatomy Discovered!</strong><br/>' +
      '<span style="color:#8b5cf6;">• Hypotenuse:</span> Longest side, opposite 90°.<br/>' +
      '<span style="color:#ef4444;">• Opposite Side:</span> Directly across from Reference Angle θ.<br/>' +
      '<span style="color:#10b981;">• Adjacent Side:</span> Next to Reference Angle θ.<br/>' +
      '<em>Click on any side of the triangle above to inspect its definition.</em>';

    // Highlight all sides in their respective colors
    document.getElementById('line-vertical').setAttribute('stroke', '#ef4444');
    document.getElementById('line-vertical').setAttribute('stroke-width', '6');
    document.getElementById('lbl-opposite').style.opacity = '1';

    document.getElementById('line-bottom').setAttribute('stroke', '#10b981');
    document.getElementById('line-bottom').setAttribute('stroke-width', '6');
    document.getElementById('lbl-adjacent').style.opacity = '1';

    nextBtn.innerText = 'Completed ✓';
    nextBtn.disabled = true;
    document.getElementById('step-badge-3').classList.add('completed');
  }
}

function resetDiscoveryModule() {
  currentStep = 1;
  stepCompleted = [false, false, false];

  document.getElementById('step-badge-1').className = 'cm-step-badge active';
  document.getElementById('step-badge-2').className = 'cm-step-badge';
  document.getElementById('step-badge-3').className = 'cm-step-badge';

  document.getElementById('line-hypotenuse').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-hypotenuse').setAttribute('stroke-width', '5');
  document.getElementById('line-vertical').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-vertical').setAttribute('stroke-width', '5');
  document.getElementById('line-bottom').setAttribute('stroke', '#94a3b8');
  document.getElementById('line-bottom').setAttribute('stroke-width', '5');

  document.getElementById('svg-90-marker').setAttribute('stroke', '#64748b');
  document.getElementById('svg-90-marker').setAttribute('fill', 'rgba(99, 102, 241, 0.1)');
  document.getElementById('lbl-90-deg').setAttribute('fill', '#64748b');

  document.getElementById('svg-ref-arc').setAttribute('stroke', '#94a3b8');
  document.getElementById('svg-ref-arc').setAttribute('stroke-width', '4');
  document.getElementById('lbl-ref-theta').style.display = 'none';

  document.getElementById('lbl-hypotenuse').style.opacity = '0.2';
  document.getElementById('lbl-opposite').style.opacity = '0.2';
  document.getElementById('lbl-adjacent').style.opacity = '0.2';

  document.getElementById('discovery-prompt').innerHTML = '<strong>Step 1:</strong> Click on the <span class="highlight-target">90° corner square</span> or the <span class="highlight-target">slanted side opposite to it</span> to locate the Hypotenuse.';
  
  const feedback = document.getElementById('discovery-feedback');
  feedback.className = 'cm-discovery-feedback';
  feedback.innerHTML = 'Click on the 90° corner square or the slanted hypotenuse side to begin!';

  const nextBtn = document.getElementById('btn-next-step');
  nextBtn.innerText = 'Next Step →';
  nextBtn.disabled = true;
}
</script>

