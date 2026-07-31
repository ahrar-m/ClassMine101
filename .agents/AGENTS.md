# Workspace Guidelines & Anti-Patterns — Material for MkDocs

This document records key lessons, configuration rules, rendering pitfalls, and tool usage guidelines discovered during the setup of the Material for MkDocs showcase in this repository. Future AI agents and developers working in this workspace **MUST** follow these rules to avoid repeating past mistakes.

---

## 1. Material for MkDocs Rendering & Extension Rules

### ❌ Issue 1: Standard Admonitions (`!!! note`) Rendering as Plain Text Paragraphs
- **Symptom**: Callouts defined with `!!! note`, `!!! tip`, `!!! danger`, etc. rendered as plain text or standard blockquotes rather than styled callout containers.
- **Root Cause**: `pymdownx.details` was enabled in `mkdocs.yml`, but core `admonition` extension was missing. `pymdownx.details` strictly handles collapsible callouts (`???`), while standard callouts (`!!!`) require Python-Markdown's `admonition` extension.
- **Rule**: ALWAYS include both `admonition` and `pymdownx.details` under `markdown_extensions:` in `mkdocs.yml`:
  ```yaml
  markdown_extensions:
    - admonition
    - pymdownx.details
  ```

---

### ❌ Issue 2: LaTeX MathJax Formulas ($E=mc^2$) Not Typesetting on Page Load
- **Symptom**: LaTeX math formulas written with `$` or `$$` remained as raw text strings in the browser.
- **Root Cause**: `pymdownx.arithmatex` with `generic: true` wraps math in HTML elements with the `.arithmatex` class, but MathJax 3 requires a client-side initialization script (`window.MathJax = { tex: { ... }, options: { processHtmlClass: "arithmatex" } }`) executed **before** loading the MathJax script library.
- **Rule**: ALWAYS create `docs/javascripts/mathjax.js` with `window.MathJax` configuration and include it in `extra_javascript` before the MathJax CDN script:
  ```yaml
  extra_javascript:
    - javascripts/mathjax.js
    - https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js
  ```

---

### ❌ Issue 3: Markdown Attribute Lists for Buttons (`[Button]{ .md-button }`) Displaying Literal Text
- **Symptom**: `[Primary Action Button :material-rocket-launch:]{ .md-button .md-button--primary }` displayed as unparsed literal syntax on the page.
- **Root Cause**: Python-Markdown `attr_list` requires a leading colon `{: .md-button}` directly appended to elements without spaces, and mixing complex inline icon shortcodes inside brackets can fail attribute parsing.
- **Rule**: When creating styled Material buttons with embedded icons, use explicit HTML links (`<a href="#" class="md-button md-button--primary">...</a>`) with `md_in_html` enabled for 100% reliable rendering across all browsers.

---

### ❌ Issue 4: Invalid/Non-existent Material Icon Slugs Rendering as Text
- **Symptom**: `:material-markdown-space:` appeared as a plain text string instead of a rendered SVG icon.
- **Root Cause**: The icon slug did not exist in the official Material Design Icons index.
- **Rule**: Always verify Material, FontAwesome, and Octicons shortcode names against valid indexes (e.g. `:material-language-markdown:`, `:material-code-json:`, `:material-palette:`).

---

## 2. Tool Usage Rules for AI Assistants

### ❌ Issue 5: Tool API Argument Error when modifying Workspace Project Files
- **Symptom**: `write_to_file` call failed when attempting to write `mkdocs.yml`.
- **Root Cause**: `ArtifactMetadata` was passed in the tool arguments for a file outside the agent brain directory. `ArtifactMetadata` is strictly reserved for artifact `.md` files located within `<appDataDir>\brain\<conversation-id>`.
- **Rule**: DO NOT include `ArtifactMetadata` when creating or modifying standard project files (like `mkdocs.yml`, `docs/*.md`, `extra.css`) in the workspace repository.

---

## Summary Checklist for New Pages in this Repository

- [ ] Ensure `mkdocs.yml` has `- admonition` and `- pymdownx.details` enabled.
- [ ] For math formulas, verify `docs/javascripts/mathjax.js` is loaded in `extra_javascript`.
- [ ] For collapsible code blocks, wrap source snippets in `??? note "View Source Markdown"`.
- [ ] Test local builds with `python -m mkdocs build --strict` before submitting changes.
