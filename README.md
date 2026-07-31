# ClassMine 101 🎓✨

> High School Mathematics interactive learning hub featuring conceptual walkthroughs, visual diagrams, TeX math rendering, and self-assessment topic guides.

---

## 🌟 Project Overview

**ClassMine 101** is an open-source educational documentation platform created to provide intuitive, visual, and conceptual learning for high-school level Mathematics (with Physics modules planned for future release). 

Built using **MkDocs** and **Material for MkDocs**, the hub focuses on pure topic-driven learning without textbook clutter.

### Key Features
- **Conceptual Topic Hierarchy**: Pure, topic-based learning organized logically without grade or textbook publisher labels in UI.
- **TeX Math Rendering**: Powered natively by MathJax 3 with support for inline `\(...\)` and dedicated block `$$` expressions.
- **Trigonometry Module**: Detailed concept guides covering ratios, specific angles, complementary angles, Pythagorean identities, and real-world heights and distances.
- **Native Material UI**: Dynamic dark/light mode toggle, sticky tab navigation, search suggestions, code copy, and responsive grid layouts.

---

## 🎯 Curriculum & Topics Covered

### 📐 Mathematics
- 🟢 **Trigonometry** *(Active)*
  - Trigonometric Ratios
  - Ratios of Specific Angles ($0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ$)
  - Ratios of Complementary Angles
  - Trigonometric Identities
  - Heights and Distances (Applications of Trigonometry)
- ⏳ **Upcoming Core Categories**:
  - Number Systems
  - Algebra
  - Coordinate Geometry
  - Geometry
  - Mensuration
  - Statistics & Probability

### ⚡ Physics *(Planned Expansion)*
- Mechanics, Thermodynamics, Waves, Optics, and Electromagnetism.

---

## 📁 Repository Structure

```text
ClassMine101/
├── .github/             # CI/CD workflows and repository metadata
├── animations/          # Visual animations and media assets
│   ├── math/
│   └── physics/
├── docs/                # MkDocs markdown documentation source pages
│   ├── index.md         # ClassMine 101 homepage
│   ├── javascripts/     # JavaScript configurations
│   │   └── mathjax.js   # MathJax 3 LaTeX rendering configuration
│   ├── math/            # Mathematics hub & category modules
│   │   ├── index.md     # Mathematics category overview hub
│   │   └── trigonometry/# Trigonometry module chapters
│   │       ├── index.md
│   │       ├── 01_trigonometric_ratios.md
│   │       ├── 02_ratios_of_specific_angles.md
│   │       ├── 03_ratios_of_complementary_angles.md
│   │       ├── 04_trigonometric_identities.md
│   │       └── 05_heights_and_distances.md
│   └── stylesheets/     # Custom stylesheet overrides
│       └── extra.css
├── textbooks/           # Curriculum reference materials & resources
├── AGENTS.md            # Agent instructions & development guidelines
├── mkdocs.yml           # Master MkDocs site metadata & navigation config
├── requirements.txt     # Python dependencies (mkdocs, mkdocs-material)
└── README.md            # Project documentation overview
```

---

## 🛠️ Quick Start & Setup Guide

### 1. Prerequisites
Ensure Python 3.8 or higher is installed on your system.

```bash
# Clone the repository
git clone https://github.com/ahrar-m/ClassMine101.git
cd ClassMine101

# Create and activate a virtual environment
python -m venv venv

# On Windows (PowerShell / Command Prompt):
venv\Scripts\activate

# On Linux / macOS:
source venv/bin/activate
```

### 2. Install Dependencies

Install the required Python packages (`mkdocs`, `mkdocs-material`):

```bash
pip install -r requirements.txt
```

---

## 🌐 Local Website Development & Preview

### Live Development Server
Start the local MkDocs preview server with live reloading:

```bash
mkdocs serve
```

Open your web browser and navigate to:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

### Build Static Site
To test local compilation and generate static HTML inside the `site/` folder:

```bash
mkdocs build
```

---

## 🚀 Deployment to GitHub Pages

Deploy the compiled site directly to GitHub Pages:

```bash
mkdocs gh-deploy
```

---

## 🤝 Contributing & Development Rules

Contributions from students, educators, and open-source developers are welcome!

- **Branch Workflow**: All active development takes place on the `dev` branch.
- **Topic-Based Focus**: Content must remain strictly concept and topic-based without textbook brand names or grade tags in page UI.
- **LaTeX Math Rules**: Always use `\(...\)` for inline math, separated multi-line `$$` blocks for display math, and plain text for Markdown headings.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).