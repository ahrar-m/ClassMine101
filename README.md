# ClassMine 101 🎓✨

> Bringing High School Mathematics & Physics to life with visual [Manim](https://www.manim.community/) animations, interactive documentation, and YouTube video walkthroughs.

---

## 🌟 Project Overview

**ClassMine 101** is an open-source educational platform created to bridge the gap in intuitive, visual learning for high-school level Mathematics and Physics concepts using the Manim animation library.

Key features include:
- **Visual Problem Solving**: Step-by-step Manim animations illustrating physical phenomena and math principles.
- **Dedicated Web Portal**: Hosted via **MkDocs (Material Theme)**, featuring crisp LaTeX math formatting and embedded video explanations.
- **YouTube Channel Integration**: Video playlists linked directly to each problem statement for flexible learning.

---

## 🎯 Target Audience & Curriculum

ClassMine 101 targets high school students, educators, and self-learners covering topics in:

- 📐 **Mathematics**: *(Topics will be added as content is developed)*
- ⚡ **Physics**: *(Topics will be added as content is developed)*

---

## 📁 Repository Structure

The repository follows a clean, modular, AI-friendly structure designed for automated scene generation, documentation rendering, and media management:

```text
ClassMine-101/
├── animations/           # Manim Python scripts
│   ├── math/            # Math scene scripts (e.g., calculus, geometry)
│   └── physics/         # Physics scene scripts (e.g., kinematics, optics)
├── docs/                # MkDocs website content (Markdown files)
│   ├── math/            # Web pages for math problems & explanations
│   ├── physics/         # Web pages for physics problems & explanations
│   ├── index.md         # Website homepage
│   └── stylesheets/     # Custom CSS for MkDocs Material theme
├── media/               # Manim rendered videos, GIFs, and image outputs
├── mkdocs.yml           # MkDocs site configuration file
├── requirements.txt     # Python dependencies (Manim, MkDocs, Material theme)
└── README.md            # Project documentation
```

---

## 🛠️ Quick Start & Setup Guide

### 1. Prerequisites
Ensure you have Python 3.8+ and standard build tools installed on your system.

```bash
# Clone the repository
git clone https://github.com/your-username/ClassMine-101.git
cd ClassMine-101

# Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

Install Manim and MkDocs Material theme:

```bash
pip install -r requirements.txt
```

*(Note: Manim requires `ffmpeg` and LaTeX (such as TeX Live or MikTeX) for text and equation rendering. Refer to the [Manim Installation Guide](https://docs.manim.community/en/stable/installation.html) for system-level dependencies).*

---

## 🎥 Running Manim Animations

To render a scene from the `animations/` folder:

```bash
# Render a math scene in medium quality (480p) for quick preview
manim -pql animations/math/derivatives_intro.py DerivativeIntro

# Render in high quality (1080p, 60fps) for YouTube / Web export
manim -pqh animations/math/derivatives_intro.py DerivativeIntro
```

Rendered videos will automatically save into the `media/` directory.

---

## 🌐 Local Website Development & Preview

ClassMine 101 uses **MkDocs** with the **Material** theme for fast, responsive web rendering with LaTeX support.

To preview the website locally:

```bash
mkdocs serve
```

Open your browser at `http://127.0.0.1:8000` to view the live website.

---

## 🚀 Deployment to GitHub Pages

Publish the website to GitHub Pages with a single command:

```bash
mkdocs gh-deploy
```

Alternatively, automated deployment can be configured via GitHub Actions.

---

## 📺 YouTube Channel Integration Workflow

Each concept or problem in ClassMine 101 follows a 3-step release pipeline:
1. **Scene Scripting**: Write clean, reproducible Manim Python scenes under `animations/`.
2. **Video Production**: Render high-definition videos, add voiceovers/soundtrack if needed, and publish to the **ClassMine 101 YouTube Channel**.
3. **Web Publishing**: Create a corresponding Markdown entry in `docs/` featuring:
   - Full LaTeX problem statement and step-by-step explanation.
   - Embedded YouTube video player.
   - Direct link badge to "Watch on YouTube".

---

## 🤝 Contributing

Contributions from students, teachers, and developers are welcome!
- **Request a Topic/Problem**: Open an issue detailing a high school math or physics problem you'd like visualized.
- **Submit a Scene**: Create a Pull Request with a new Manim script in `animations/`.
- **Improve Documentation**: Enhance LaTeX explanations or MkDocs pages in `docs/`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).