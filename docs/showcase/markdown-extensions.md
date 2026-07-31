# Markdown Extensions Showcase

This page demonstrates **PyMdown Extensions** and core Markdown features including Keyboard Keys, Tasklists, Definition Lists, Footnotes, Special Text Formatting, and Data Tables.

---

## 1. Keyboard Key Combinations

Display keyboard shortcuts using formatted key caps with `pymdownx.keys`.

Press ++ctrl+alt+del++ to access system options.

To open the Command Palette in VS Code, press ++cmd+shift+p++ (macOS) or ++ctrl+shift+p++ (Windows/Linux).

Press ++ctrl+c++ to copy selection, and ++ctrl+v++ to paste.

??? note "View Source Markdown for Keyboard Keys"

    ```markdown
    Press ++ctrl+alt+del++ to access system options.

    To open the Command Palette in VS Code, press ++cmd+shift+p++ (macOS) or ++ctrl+shift+p++ (Windows/Linux).

    Press ++ctrl+c++ to copy selection, and ++ctrl+v++ to paste.
    ```

---

## 2. Interactive Tasklists

Create structured checklists with interactive checkboxes.

- [x] Configure `mkdocs.yml` dependencies and plugins
- [x] Implement Light/Dark theme color palettes
- [x] Set up Mermaid diagram rendering
- [ ] Add custom domain SSL certificate
- [ ] Deploy to production hosting server

??? note "View Source Markdown for Tasklists"

    ```markdown
    - [x] Configure `mkdocs.yml` dependencies and plugins
    - [x] Implement Light/Dark theme color palettes
    - [x] Set up Mermaid diagram rendering
    - [ ] Add custom domain SSL certificate
    - [ ] Deploy to production hosting server
    ```

---

## 3. Definition Lists

Present clear terms, glossary items, and API definitions.

MkDocs
: A fast, simple, and customizable static site generator geared towards building project documentation.

PyMdown Extensions
: A collection of extensions for Python-Markdown that add enhanced syntax features, code blocks, tabbed content, and math support.

Mermaid.js
: A JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions and rendering.

??? note "View Source Markdown for Definition Lists"

    ```markdown
    MkDocs
    : A fast, simple, and customizable static site generator geared towards building project documentation.

    PyMdown Extensions
    : A collection of extensions for Python-Markdown that add enhanced syntax features, code blocks, tabbed content, and math support.

    Mermaid.js
    : A JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions and rendering.
    ```

---

## 4. Footnotes

Add inline citations and references to footnotes[^1] that link automatically to notes at the page bottom[^2].

[^1]: Material for MkDocs provides over 50 configuration options for customization.
[^2]: Footnotes are automatically numbered and include back-to-content navigation links.

??? note "View Source Markdown for Footnotes"

    ```markdown
    Add inline citations and references to footnotes[^1] that link automatically to notes at the page bottom[^2].

    [^1]: Material for MkDocs provides over 50 configuration options for customization.
    [^2]: Footnotes are automatically numbered and include back-to-content navigation links.
    ```

---

## 5. Text Formatting & Highlighting

Enhance plain text with highlighting, subscript, superscript, and strikethrough syntax.

- **Highlighted Text**: Use ==marked text== to draw attention.
- **Subscript**: Chemical formula for water is H~2~O, and carbon dioxide is CO~2~.
- **Superscript**: Einstein's equation $E = mc^2$ or polynomial expression $x^3^ + y^2^$.
- **Strikethrough**: Deprecated feature syntax ~~`old_function()`~~ replaced by `new_function()`.

??? note "View Source Markdown for Text Formatting"

    ```markdown
    - **Highlighted Text**: Use ==marked text== to draw attention.
    - **Subscript**: Chemical formula for water is H~2~O, and carbon dioxide is CO~2~.
    - **Superscript**: Einstein's equation $E = mc^2$ or polynomial expression $x^3^ + y^2^$.
    - **Strikethrough**: Deprecated feature syntax ~~`old_function()`~~ replaced by `new_function()`.
    ```

---

## 6. Advanced Data Tables

Data tables support alignment options (Left, Center, Right), inline formatting, icons, and status badges.

| Extension Name | Category | Status | Supported Features | Performance Rating |
| :--- | :---: | :---: | :--- | ---: |
| `pymdownx.superfences` | Diagrams | <span class="badge badge-success">Active</span> | Mermaid.js, Custom Fences, Nesting | 99.8% |
| `pymdownx.highlight` | Code | <span class="badge badge-success">Active</span> | Line numbers, Pygments, Annotations | 99.9% |
| `pymdownx.tabbed` | UI Layout | <span class="badge badge-success">Active</span> | Alternate tabs, Linked groups | 100.0% |
| `pymdownx.arithmatex` | Math | <span class="badge badge-info">Optional</span> | MathJax 3, KaTeX, Inline/Block | 98.5% |
| `pymdownx.keys` | Text | <span class="badge badge-success">Active</span> | Key caps, Combo shortcuts | 100.0% |

??? note "View Source Markdown for Data Tables"

    ```markdown
    | Extension Name | Category | Status | Supported Features | Performance Rating |
    | :--- | :---: | :---: | :--- | ---: |
    | `pymdownx.superfences` | Diagrams | <span class="badge badge-success">Active</span> | Mermaid.js, Custom Fences, Nesting | 99.8% |
    | `pymdownx.highlight` | Code | <span class="badge badge-success">Active</span> | Line numbers, Pygments, Annotations | 99.9% |
    | `pymdownx.tabbed` | UI Layout | <span class="badge badge-success">Active</span> | Alternate tabs, Linked groups | 100.0% |
    | `pymdownx.arithmatex` | Math | <span class="badge badge-info">Optional</span> | MathJax 3, KaTeX, Inline/Block | 98.5% |
    | `pymdownx.keys` | Text | <span class="badge badge-success">Active</span> | Key caps, Combo shortcuts | 100.0% |
    ```
