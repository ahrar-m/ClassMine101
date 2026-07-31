# Code & Math Showcase

This page demonstrates **Material for MkDocs** code syntax capabilities, line annotations, inline code highlighting, and LaTeX math equation rendering via MathJax and `pymdownx.arithmatex`.

---

## 1. Syntax Highlighting & Titles

Code blocks support language auto-detection, Pygments syntax highlighting, copy buttons, and title headers.

```python title="data_processor.py"
import asyncio
from typing import List, Dict

class DataPipeline:
    def __init__(self, name: str):
        self.name = name
        self.queue: asyncio.Queue = asyncio.Queue()

    async def process_item(self, item: Dict[str, str]) -> bool:
        """Process a single record asynchronously."""
        await asyncio.sleep(0.1)
        print(f"[{self.name}] Processed: {item.get('id')}")
        return True
```

??? note "View Source Markdown for Code Block with Title"

    ````markdown
    ```python title="data_processor.py"
    import asyncio
    from typing import List, Dict

    class DataPipeline:
        def __init__(self, name: str):
            self.name = name
            self.queue: asyncio.Queue = asyncio.Queue()

        async def process_item(self, item: Dict[str, str]) -> bool:
            """Process a single record asynchronously."""
            await asyncio.sleep(0.1)
            print(f"[{self.name}] Processed: {item.get('id')}")
            return True
    ```
    ````

---

## 2. Line Highlighting & Line Numbers

Highlight specific lines of interest within a code block to guide the reader's focus.

```python linenums="1" hl_lines="4 7-9"
def calculate_metrics(values: list[float]) -> dict[str, float]:
    if not values:
        return {"mean": 0.0, "total": 0.0}
    
    total_sum = sum(values) # (1) Highlighted line
    mean_val = total_sum / len(values)
    
    # Highlighted calculation block
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    
    return {"mean": mean_val, "total": total_sum, "std_dev": std_dev}
```

??? note "View Source Markdown for Line Highlighting"

    ````markdown
    ```python linenums="1" hl_lines="4 7-9"
    def calculate_metrics(values: list[float]) -> dict[str, float]:
        if not values:
            return {"mean": 0.0, "total": 0.0}
        
        total_sum = sum(values)
        mean_val = total_sum / len(values)
        
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        std_dev = variance ** 0.5
        
        return {"mean": mean_val, "total": total_sum, "std_dev": std_dev}
    ```
    ````

---

## 3. Interactive Code Annotations

Attach interactive markers directly inside code blocks. Click or hover on numbers `(1)` and `(2)` below!

```python title="app.py"
from fastapi import FastAPI, HTTPException # (1)

app = FastAPI(title="Showcase API")

@app.get("/items/{item_id}")
async def read_item(item_id: int): # (2)
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Invalid item ID")
    return {"item_id": item_id, "status": "active"}
```

1.  **FastAPI Import**: Loads the core application framework and exception handler.
2.  **Path Parameter**: Automatically validates that `item_id` is parsed as an integer.

??? note "View Source Markdown for Code Annotations"

    ````markdown
    ```python title="app.py"
    from fastapi import FastAPI, HTTPException # (1)

    app = FastAPI(title="Showcase API")

    @app.get("/items/{item_id}")
    async def read_item(item_id: int): # (2)
        if item_id < 0:
            raise HTTPException(status_code=400, detail="Invalid item ID")
        return {"item_id": item_id, "status": "active"}
    ```

    1.  **FastAPI Import**: Loads the core application framework and exception handler.
    2.  **Path Parameter**: Automatically validates that `item_id` is parsed as an integer.
    ````

---

## 4. Inline Code Highlighting

You can highlight code inline using syntax specs, like `#!python import sys` or `#!sql SELECT * FROM users WHERE active = 1`.

??? note "View Source Markdown for Inline Code Highlighting"

    ```markdown
    You can highlight code inline using syntax specs, like `#!python import sys` or `#!sql SELECT * FROM users WHERE active = 1`.
    ```

---

## 5. Mathematical Formula Rendering (LaTeX / MathJax)

Render LaTeX mathematical equations seamlessly, both inline and as standalone display blocks.

### Inline Math

Einstein's famous mass-energy equivalence equation is $E = mc^2$.

The normal distribution density function uses $\mu$ for mean and $\sigma$ for standard deviation.

### Block Math Equations

#### Gaussian Integral

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

#### The Quadratic Formula

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### Matrix Algebra & Linear Systems

$$\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}$$

#### Maxwell's Equations

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$

$$\nabla \times \mathbf{B} - \frac{1}{c^2}\frac{\partial \mathbf{E}}{\partial t} = \mu_0 \mathbf{J}$$

??? note "View Source Markdown for Math Equations"

    ```markdown
    ### Inline Math
    Einstein's famous mass-energy equivalence equation is $E = mc^2$.

    ### Block Math Equations

    #### Gaussian Integral
    $$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

    #### The Quadratic Formula
    $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

    #### Matrix Algebra & Linear Systems
    $$\begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}
    \begin{pmatrix}
    x \\
    y
    \end{pmatrix}
    =
    \begin{pmatrix}
    ax + by \\
    cx + dy
    \end{pmatrix}$$

    #### Maxwell's Equations
    $$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$

    $$\nabla \times \mathbf{B} - \frac{1}{c^2}\frac{\partial \mathbf{E}}{\partial t} = \mu_0 \mathbf{J}$$
    ```
