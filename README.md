# ClassMine 101 🎓✨

> High School Mathematics interactive learning hub, step-by-step problem walkthroughs, visual diagrams, and concept check quizzes.

---

## 🌟 Project Overview

**ClassMine 101** is an open-source educational platform created to provide intuitive, visual, and interactive learning for high-school level Mathematics concepts (with Physics modules planned for future release).

Key features include:
- **Visual Problem Solving**: Step-by-step diagrams illustrating math principles and geometric intuition.
- **Dedicated Web Portal**: Hosted via **MkDocs (Material Theme)**, featuring crisp LaTeX math formatting.
- **Interactive Quizzes & Walkthroughs**: Instant self-assessment quizzes after every concept to reinforce understanding.

---

## 🎯 Target Audience & Curriculum

ClassMine 101 targets high school students, educators, and self-learners covering topics in:

- 📐 **Mathematics**: *(Topics will be added as content is developed)*
- ⚡ **Physics**: *(Planned for future expansion)*

---

## 📁 Repository Structure

The repository follows a clean, modular structure designed for documentation rendering, diagrams, and quiz management:

```text
ClassMine-101/
├── docs/                # MkDocs website content (Markdown files)
│   ├── math/            # Web pages for math problems & explanations
│   ├── physics/         # Web pages for physics problems & explanations
│   ├── index.md         # Website homepage
│   └── stylesheets/     # Custom CSS for MkDocs Material theme
├── mkdocs.yml           # MkDocs site configuration file
├── requirements.txt     # Python dependencies (MkDocs, Material theme)
└── README.md            # Project documentation
```

---

## 🛠️ Quick Start & Setup Guide

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

```bash
# Clone the repository
git clone https://github.com/ahrar-m/ClassMine101.git
cd ClassMine101

# Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

Install MkDocs and Material theme:

```bash
pip install -r requirements.txt
```

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

---

## 🤝 Contributing

Contributions from students, teachers, and developers are welcome!
- **Request a Topic/Problem**: Open an issue detailing a high school math or physics problem.
- **Improve Documentation**: Enhance LaTeX explanations, add diagrams, or contribute quiz questions in `docs/`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).