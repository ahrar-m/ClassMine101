# UI Elements & Cards Showcase

This page demonstrates the visual aesthetics and usage of standard and advanced UI elements in **Material for MkDocs**, including Admonitions, Grid Cards, Buttons, Content Tabs, Tooltips, and Badges.

---

## 1. Admonition Callout Boxes

Material for MkDocs provides 12 built-in admonition types with custom icons and color schemes.

### Standard Admonitions

!!! note "Note Callout"
    This is a standard **Note** admonition. Use it for general contextual information.

!!! abstract "Abstract / Summary"
    This is an **Abstract** or TL;DR summary callout block.

!!! info "Information Callout"
    This is an **Info** callout highlighting useful information.

!!! tip "Tip & Recommendation"
    This is a **Tip** callout. Use it for best practices and helpful advice.

!!! success "Success & Completion"
    This is a **Success** callout indicating successful validation or task completion.

!!! question "Question & FAQ"
    This is a **Question** callout for FAQs or user inquiries.

!!! warning "Warning Alert"
    This is a **Warning** callout for cautioning users against potential issues.

!!! failure "Failure Alert"
    This is a **Failure** callout for error messages or failing operations.

!!! danger "Danger / High Risk"
    This is a **Danger** callout for high-risk operations or potential data loss.

!!! bug "Bug Report"
    This is a **Bug** callout for highlighting known issues or tracking bugs.

!!! example "Example Demonstration"
    This is an **Example** callout box for sample code or usage demonstrations.

!!! quote "Quote / Citation"
    This is a **Quote** block for quotes, testimonials, or reference citations.

??? note "View Source Markdown for Standard Admonitions"

    ```markdown
    !!! note "Note Callout"
        This is a standard **Note** admonition. Use it for general contextual information.

    !!! abstract "Abstract / Summary"
        This is an **Abstract** or TL;DR summary callout block.

    !!! info "Information Callout"
        This is an **Info** callout highlighting useful information.

    !!! tip "Tip & Recommendation"
        This is a **Tip** callout. Use it for best practices and helpful advice.

    !!! success "Success & Completion"
        This is a **Success** callout indicating successful validation or task completion.

    !!! question "Question & FAQ"
        This is a **Question** callout for FAQs or user inquiries.

    !!! warning "Warning Alert"
        This is a **Warning** callout for cautioning users against potential issues.

    !!! failure "Failure Alert"
        This is a **Failure** callout for error messages or failing operations.

    !!! danger "Danger / High Risk"
        This is a **Danger** callout for high-risk operations or potential data loss.

    !!! bug "Bug Report"
        This is a **Bug** callout for highlighting known issues or tracking bugs.

    !!! example "Example Demonstration"
        This is an **Example** callout box for sample code or usage demonstrations.

    !!! quote "Quote / Citation"
        This is a **Quote** block for quotes, testimonials, or reference citations.
    ```

---

### Collapsible & Default-Open Admonitions

??? note "Collapsible Admonition (Closed by Default — Click to Expand!)"
    This content is hidden inside a collapsible admonition drawer until the user clicks the title bar.

???+ tip "Collapsible Admonition (Open by Default)"
    This admonition can be collapsed by the user, but starts expanded by default using `???+`.

??? note "View Source Markdown for Collapsible Admonitions"

    ```markdown
    ??? note "Collapsible Admonition (Closed by Default — Click to Expand!)"
        This content is hidden inside a collapsible admonition drawer until the user clicks the title bar.

    ???+ tip "Collapsible Admonition (Open by Default)"
        This admonition can be collapsed by the user, but starts expanded by default using `???+`.
    ```

---

## 2. Interactive Grid Cards

Grid cards create responsive, multi-column card grids for features, documentation sections, or landing pages.

<div class="grid cards" markdown>

-   :material-flash:{ .lg .middle } **Lightning Fast**

    ---

    Built on top of modern web standards with instant loading capabilities for immediate responses.

    [Learn More :octicons-arrow-right-24:](#)

-   :material-palette:{ .lg .middle } **Beautiful Themes**

    ---

    Automatic light and dark mode toggling with customizable primary and accent color schemes.

    [Learn More :octicons-arrow-right-24:](#)

-   :material-magnify:{ .lg .middle } **Built-in Search**

    ---

    Client-side fast full-text search with query auto-suggestions and term highlighting.

    [Learn More :octicons-arrow-right-24:](#)

-   :material-responsive:{ .lg .middle } **Responsive Layout**

    ---

    Designed for seamless rendering across desktop monitors, tablets, and mobile devices.

    [Learn More :octicons-arrow-right-24:](#)

</div>

??? note "View Source Markdown for Grid Cards"

    ```markdown
    <div class="grid cards" markdown>

    -   :material-flash:{ .lg .middle } **Lightning Fast**

        ---

        Built on top of modern web standards with instant loading capabilities for immediate responses.

        [Learn More :octicons-arrow-right-24:](#)

    -   :material-palette:{ .lg .middle } **Beautiful Themes**

        ---

        Automatic light and dark mode toggling with customizable primary and accent color schemes.

        [Learn More :octicons-arrow-right-24:](#)

    -   :material-magnify:{ .lg .middle } **Built-in Search**

        ---

        Client-side fast full-text search with query auto-suggestions and term highlighting.

        [Learn More :octicons-arrow-right-24:](#)

    -   :material-responsive:{ .lg .middle } **Responsive Layout**

        ---

        Designed for seamless rendering across desktop monitors, tablets, and mobile devices.

        [Learn More :octicons-arrow-right-24:](#)

    </div>
    ```

---

## 3. Buttons & Action Links

Material for MkDocs provides styled primary and secondary action buttons using Markdown attribute lists.

<a href="#" class="md-button md-button--primary">Primary Action Button :material-rocket-launch:</a>
<a href="#" class="md-button">Secondary Action Button</a>

??? note "View Source Markdown for Buttons"

    ```markdown
    <a href="#" class="md-button md-button--primary">Primary Action Button :material-rocket-launch:</a>
    <a href="#" class="md-button">Secondary Action Button</a>
    ```

---

## 4. Content Tabs

Organize alternate examples, multi-language code snippets, or configuration instructions into clean tab groups.

=== "Python"

    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    ```

=== "JavaScript"

    ```javascript
    function greet(name) {
      return `Hello, ${name}!`;
    }
    ```

=== "Rust"

    ```rust
    fn greet(name: &str) -> String {
        format!("Hello, {}!", name)
    }
    ```

??? note "View Source Markdown for Content Tabs"

    ```markdown
    === "Python"

        ```python
        def greet(name: str) -> str:
            return f"Hello, {name}!"
        ```

    === "JavaScript"

        ```javascript
        function greet(name) {
          return `Hello, ${name}!`;
        }
        ```

    === "Rust"

        ```rust
        fn greet(name: &str) -> String {
            format!("Hello, {}!", name)
        }
        ```
    ```

---

## 5. Tooltips, Abbreviations & Badges

Hover over the dotted terms below to see interactive tooltips powered by `abbr` extension.

The HTML standard defines web elements. CSS styles the layout, and JS provides interactivity.

<span class="badge badge-primary">Version 9.7</span>
<span class="badge badge-accent">Featured</span>
<span class="badge badge-success">Passed</span>
<span class="badge badge-warning">Beta</span>

*[HTML]: HyperText Markup Language
*[CSS]: Cascading Style Sheets
*[JS]: JavaScript

??? note "View Source Markdown for Tooltips & Badges"

    ```markdown
    The HTML standard defines web elements. CSS styles the layout, and JS provides interactivity.

    <span class="badge badge-primary">Version 9.7</span>
    <span class="badge badge-accent">Featured</span>
    <span class="badge badge-success">Passed</span>
    <span class="badge badge-warning">Beta</span>

    *[HTML]: HyperText Markup Language
    *[CSS]: Cascading Style Sheets
    *[JS]: JavaScript
    ```
