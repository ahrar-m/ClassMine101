# Agent Instructions & Project Rules

## Local Build & Preview
- After every single execution/prompt, compile the website locally (`mkdocs build`).
- Prepare a localhost preview link (e.g. `http://127.0.0.1:8000` or `http://localhost:8000`) and present it directly so the user can click and open it to analyze locally.

## Version Control Guidelines
- **DO NOT** push to GitHub directly without explicit user approval. Only push when explicitly specified by the user.
- At the end of every prompt execution, stage all changes and commit locally with a detailed commit message so that the commit history is rich and informative.

## Curriculum & Organization Rules
- **Pure Topic-Based Structure**: Organize the website purely by core mathematical topics and categories directly under `math/`.
- **Textbook Sequence & Ordering**: Order chapters within each category following the logical textbook sequence (Class 9 topics first, followed by Class 10 topics). Files in `docs/math/` may use numerical prefixes (`01_`, `02_`, etc.) for filesystem ordering.
- **No Class/Grade/Unit/Chapter Prefixes in UI**: Do NOT display numerical prefixes or labels like "Class 9", "Class 10", "Unit 1", "Chapter 1", or "Ch 1" in page titles, menu navigation, or headings. Keep all displayed titles clean and topic-focused.
- **Terminology & Page Structure**:
  - **Category Overview Pages**: Use heading `## Chapters` and display interactive visual cards (`<div class="grid cards" markdown>`) instead of plain bullet points.
  - **Chapter Pages**: Use heading `## Topics` listing the topics/lessons (or placeholders for upcoming Manim animations).
- **Placeholder Content**: For pages or sections that are not yet populated with Manim animations or full guides, explicitly mention that content is coming soon.
