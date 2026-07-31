# Theme & Plugins Showcase

This page highlights the core theme settings, color palettes, built-in search engine, and navigation capabilities configured in **Material for MkDocs**.

---

## 1. Light & Dark Color Palettes

Material for MkDocs includes standard light mode (default) and slate dark mode color schemes with automatic OS preference detection and header toggle switches.

=== "Light Mode Palette"

    - **Scheme**: `default`
    - **Primary Color**: `indigo` (`#3f51b5`)
    - **Accent Color**: `indigo`
    - **Toggle Icon**: `:material-brightness-7:` (Sun)

=== "Dark Mode Palette"

    - **Scheme**: `slate` (`#1e2129`)
    - **Primary Color**: `indigo`
    - **Accent Color**: `lime` (`#c0ca33`)
    - **Toggle Icon**: `:material-brightness-4:` (Moon)

??? note "View Source Markdown for Theme Palettes"

    ```markdown
    === "Light Mode Palette"

        - **Scheme**: `default`
        - **Primary Color**: `indigo` (`#3f51b5`)
        - **Accent Color**: `indigo`
        - **Toggle Icon**: `:material-brightness-7:` (Sun)

    === "Dark Mode Palette"

        - **Scheme**: `slate` (`#1e2129`)
        - **Primary Color**: `indigo`
        - **Accent Color**: `lime` (`#c0ca33`)
        - **Toggle Icon**: `:material-brightness-4:` (Moon)
    ```

---

## 2. Built-in Search Engine Features

The search engine operates client-side using a client web-worker index built at compile time.

| Search Feature | Config Flag | Description |
| :--- | :--- | :--- |
| **Auto Suggestions** | `search.suggest` | Displays live autocomplete predictions while typing into the search box. |
| **Term Highlighting** | `search.highlight` | Highlights matched search terms directly on target pages when navigated. |
| **Search Deep Sharing** | `search.share` | Generates a shareable URL containing search query parameters. |

??? note "View Source Markdown for Search Engine Configuration"

    ```markdown
    | Search Feature | Config Flag | Description |
    | :--- | :--- | :--- |
    | **Auto Suggestions** | `search.suggest` | Displays live autocomplete predictions while typing into the search box. |
    | **Term Highlighting** | `search.highlight` | Highlights matched search terms directly on target pages when navigated. |
    | **Search Deep Sharing** | `search.share` | Generates a shareable URL containing search query parameters. |
    ```

---

## 3. Advanced Navigation Features

Material for MkDocs provides rich navigation capabilities for large documentation suites:

- **Instant Loading (`navigation.instant`)**: Transforms site pages into a Single Page Application (SPA), preventing page reloads when clicking internal links.
- **Sticky Tabs (`navigation.tabs.sticky`)**: Keeps navigation category tabs pinned to the top of the screen when scrolling down.
- **Back-to-Top Button (`navigation.top`)**: Appears at the bottom right corner when scrolling down long pages for quick return to header.
- **Navigation Path / Breadcrumbs (`navigation.path`)**: Displays breadcrumb navigation trails at the top of pages.
- **Section Indexes (`navigation.indexes`)**: Allows section folders to have dedicated landing index pages (e.g. `showcase/index.md`).

??? note "View Source Markdown for Navigation Features"

    ```markdown
    - **Instant Loading (`navigation.instant`)**: Transforms site pages into a Single Page Application (SPA), preventing page reloads when clicking internal links.
    - **Sticky Tabs (`navigation.tabs.sticky`)**: Keeps navigation category tabs pinned to the top of the screen when scrolling down.
    - **Back-to-Top Button (`navigation.top`)**: Appears at the bottom right corner when scrolling down long pages for quick return to header.
    - **Navigation Path / Breadcrumbs (`navigation.path`)**: Displays breadcrumb navigation trails at the top of pages.
    - **Section Indexes (`navigation.indexes`)**: Allows section folders to have dedicated landing index pages (e.g. `showcase/index.md`).
    ```

---

## 4. Code Block Utilities

Every code block rendered on this site includes built-in interactive features:

1. **One-Click Copy Button**: Allows readers to copy raw code content to clipboard instantly.
2. **Code Line Annotation Tooltips**: Enables interactive click/hover annotations on marked lines.
3. **Select Code Action**: Selects code content for rapid copying or inspection.

??? note "View Source Markdown for Code Block Utilities"

    ```markdown
    1. **One-Click Copy Button**: Allows readers to copy raw code content to clipboard instantly.
    2. **Code Line Annotation Tooltips**: Enables interactive click/hover annotations on marked lines.
    3. **Select Code Action**: Selects code content for rapid copying or inspection.
    ```
