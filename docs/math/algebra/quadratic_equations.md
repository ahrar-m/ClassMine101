# Quadratic Equations

Welcome to the comprehensive guide on **Quadratic Equations**, based on the complete topic lecture breakdown. This guide covers fundamental definitions, checking methods, factorization algorithms (from basic integers to radicals and algebraic terms), Sridharacharya's Quadratic Formula, Discriminant analysis with parameter edge cases, and real-world word problems.

---

## 1. Overview & Standard Form

### Definition
A **Quadratic Equation** in a single variable $x$ is a polynomial equation of degree **2**. It can be written in the **Standard Form**:

$$ax^2 + bx + c = 0$$

where:
- $a, b, c$ are real numbers ($\mathbb{R}$).
- $a \neq 0$ (**Crucial Condition**: If $a = 0$, the equation reduces to $bx + c = 0$, which is linear, not quadratic).
- $x$ is the unknown variable.

---

### Identifying Quadratic Equations

To check whether a given equation is quadratic:
1. **Simplify completely**: Expand brackets, clear fractions (multiply by LCM of denominators), and move all terms to the left-hand side (LHS) so the right-hand side (RHS) is $0$.
2. **Examine the highest power of $x$**:
   - Degree must be **exactly 2**.
   - The coefficient of $x^2$ must **not be zero**.
   - Variable exponents must be non-negative integers (no fractional or negative powers such as $\sqrt{x}$ or $x^{-1}$ in polynomial form).

!!! example "Standard vs. Non-Quadratic Examples"
    - $(x + 1)^2 = 2(x - 3) \implies x^2 + 2x + 1 = 2x - 6 \implies x^2 + 7 = 0$ : **Quadratic** ($a=1, b=0, c=7$).
    - $(x - 2)(x + 1) = (x - 1)(x + 3) \implies x^2 - x - 2 = x^2 + 2x - 3 \implies 3x - 1 = 0$ : **NOT Quadratic** ($x^2$ cancels out).
    - $x + \frac{1}{x} = 2 \implies x^2 + 1 = 2x \implies x^2 - 2x + 1 = 0$ : **Quadratic** (after multiplying by $x, x \neq 0$).
    - $(x + 2)^3 = 2x(x^2 - 1) \implies x^3 + 6x^2 + 12x + 8 = 2x^3 - 2x \implies x^3 - 6x^2 - 14x - 8 = 0$ : **NOT Quadratic** (Degree is 3).

---

## 2. Solving by Factorization (Splitting the Middle Term)

### Core Principle
If a quadratic equation $ax^2 + bx + c = 0$ can be factored into a product of two linear factors:

$$(px + q)(rx + s) = 0$$

By the **Zero Product Property**, either $(px + q) = 0$ or $(rx + s) = 0$, yielding the roots:

$$x = -\frac{q}{p} \quad \text{or} \quad x = -\frac{s}{r}$$

---

### The Splitting Middle Term Algorithm
To split the middle term $b$:
1. Calculate the product $P = a \times c$.
2. Find two numbers $m$ and $n$ such that:
   - $m + n = b$
   - $m \times n = a \times c$
3. Rewrite $bx$ as $mx + nx$.
4. Group terms in pairs and factor out common expressions.

---

### Level 1: Standard Integer Coefficients

!!! tip "Example 1: Basic Trinomial"
    Solve: $x^2 - 7x + 12 = 0$

    - $a = 1, b = -7, c = 12 \implies a \times c = 12$.
    - Find two numbers that multiply to $12$ and add up to $-7$: $-3$ and $-4$.
    - Split middle term:
      $$x^2 - 3x - 4x + 12 = 0$$
      $$x(x - 3) - 4(x - 3) = 0$$
      $$(x - 3)(x - 4) = 0$$
    - **Roots**: $x = 3, 4$.

---

### Level 2: Radical / Square Root Coefficients

When coefficients involve square roots ($\sqrt{k}$), factor the radical into the product $a \times c$.

!!! example "Example 2: Radical Middle Term & Coefficients"
    Solve: $\sqrt{3}x^2 + 10x + 7\sqrt{3} = 0$

    - $a = \sqrt{3}, b = 10, c = 7\sqrt{3}$.
    - Product $a \cdot c = \sqrt{3} \cdot 7\sqrt{3} = 21$.
    - Sum $b = 10$. Two numbers multiplying to $21$ and adding to $10$: $7$ and $3$.
    - Rewrite $3x$ as $\sqrt{3} \cdot \sqrt{3}x$:
      $$\sqrt{3}x^2 + 3x + 7x + 7\sqrt{3} = 0$$
      $$\sqrt{3}x(x + \sqrt{3}) + 7(x + \sqrt{3}) = 0$$
      $$(x + \sqrt{3})(\sqrt{3}x + 7) = 0$$
    - **Roots**: $x = -\sqrt{3}, \quad x = -\frac{7}{\sqrt{3}} = -\frac{7\sqrt{3}}{3}$.

!!! example "Example 3: Middle Term containing Radical"
    Solve: $x^2 - 3\sqrt{5}x + 10 = 0$

    - Product $a \cdot c = 10$. Sum $b = -3\sqrt{5}$.
    - Express $10$ as $2 \cdot 5 = 2 \sqrt{5} \cdot \sqrt{5}$.
    - Two terms: $-2\sqrt{5}$ and $-\sqrt{5}$.
    - Split middle term:
      $$x^2 - 2\sqrt{5}x - \sqrt{5}x + 10 = 0$$
      $$x(x - 2\sqrt{5}) - \sqrt{5}(x - 2\sqrt{5}) = 0$$
      $$(x - 2\sqrt{5})(x - \sqrt{5}) = 0$$
    - **Roots**: $x = 2\sqrt{5}, \sqrt{5}$.

---

### Level 3: Algebraic Coefficients ($a, b, c$ Expressions)

!!! example "Example 4: Algebraic Terms in Coefficients"
    Solve for $x$: $4x^2 - 4ax + (a^2 - b^2) = 0$

    - Product $P = 4(a^2 - b^2) = 4(a - b)(a + b) = 2(a - b) \cdot 2(a + b)$.
    - Sum $S = -4a = -[2(a + b) + 2(a - b)]$.
    - Split middle term $-4ax$:
      $$4x^2 - 2(a + b)x - 2(a - b)x + (a - b)(a + b) = 0$$
      $$2x[2x - (a + b)] - (a - b)[2x - (a + b)] = 0$$
      $$[2x - (a + b)][2x - (a - b)] = 0$$
    - **Roots**: $x = \frac{a + b}{2}, \quad x = \frac{a - b}{2}$.

---

### Level 4: Algebraic Fractions

!!! warning "Crucial Algebraic Problem"
    Solve for $x$: 
    $$\frac{1}{a + b + x} = \frac{1}{a} + \frac{1}{b} + \frac{1}{x} \quad (a, b, x \neq 0, a+b+x \neq 0)$$

    **Step-by-step Solution**:
    1. Collect variables on LHS and constants on RHS:
       $$\frac{1}{a + b + x} - \frac{1}{x} = \frac{1}{a} + \frac{1}{b}$$

    2. Take LCM on both sides:
       $$\frac{x - (a + b + x)}{x(a + b + x)} = \frac{b + a}{ab}$$
       $$\frac{-(a + b)}{x^2 + (a + b)x} = \frac{a + b}{ab}$$

    3. Divide both sides by $(a + b)$ (since $a + b \neq 0$):
       $$\frac{-1}{x^2 + (a + b)x} = \frac{1}{ab}$$

    4. Cross-multiply:
       $$-ab = x^2 + (a + b)x \implies x^2 + (a + b)x + ab = 0$$

    5. Factorize by grouping:
       $$x(x + a) + b(x + a) = 0 \implies (x + a)(x + b) = 0$$

    - **Roots**: $x = -a, \quad x = -b$.

---

## 3. Quadratic Formula & Nature of Roots

### Derivation of Sridharacharya's Formula
Starting with $ax^2 + bx + c = 0$ ($a \neq 0$):

1. Divide by $a$: $x^2 + \frac{b}{a}x + \frac{c}{a} = 0$.
2. Move constant term to RHS: $x^2 + \frac{b}{a}x = -\frac{c}{a}$.
3. Complete the square by adding $\left(\frac{b}{2a}\right)^2$ to both sides:
   $$\left(x + \frac{b}{2a}\right)^2 = \left(\frac{b}{2a}\right)^2 - \frac{c}{a} = \frac{b^2 - 4ac}{4a^2}$$
4. Taking square root:
   $$x + \frac{b}{2a} = \frac{\pm \sqrt{b^2 - 4ac}}{2a} \implies x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

---

### The Discriminant ($D$)
The quantity under the square root $b^2 - 4ac$ is called the **Discriminant**, denoted by $D$:

$$D = b^2 - 4ac$$

---

### Nature of Roots Summary Table

| Discriminant Value | Nature of Roots | Roots Formula |
| :--- | :--- | :--- |
| **$D > 0$** | Two **Real and Distinct** (unequal) roots | $x = \frac{-b + \sqrt{D}}{2a}, \quad x = \frac{-b - \sqrt{D}}{2a}$ |
| **$D = 0$** | Two **Real and Equal** (coincident) roots | $x = -\frac{b}{2a}, \quad x = -\frac{b}{2a}$ |
| **$D < 0$** | **No Real Roots** (Imaginary / Complex conjugate roots) | No real solutions |

---

### Equal Roots Parameter Determination ($D = 0$) & Edge Case Traps

!!! caution "Coefficient Trap in Equal Roots Problems"
    Find the values of $m$ for which the equation has equal roots:
    $$(m - 1)x^2 + 2(m - 1)x + 1 = 0$$

    **Solution**:
    Here, $a = m - 1$, $b = 2(m - 1)$, $c = 1$.
    For equal roots, Discriminant $D = 0$:
    $$D = b^2 - 4ac = [2(m - 1)]^2 - 4(m - 1)(1) = 0$$
    $$4(m - 1)^2 - 4(m - 1) = 0$$
    $$4(m - 1)[(m - 1) - 1] = 0 \implies 4(m - 1)(m - 2) = 0$$

    This gives $m = 1$ or $m = 2$.

    **CRITICAL CHECK FOR $a \neq 0$**:
    - If $m = 1$, then $a = m - 1 = 0$. Substituting $m = 1$ into the original equation yields:
      $$0 \cdot x^2 + 0 \cdot x + 1 = 0 \implies 1 = 0 \quad \text{(Contradiction!)}$$
      Thus, $m = 1$ collapses the quadratic equation into an invalid statement and **MUST BE REJECTED**.
    - **Final Answer**: $m = 2$ only.

---

### Proof-Based Discriminant Problems

!!! tip "Proof: Equal Roots Ratio Condition"
    If the equation $(a^2 + b^2)x^2 - 2(ac + bd)x + (c^2 + d^2) = 0$ has equal roots, prove that $\frac{a}{b} = \frac{c}{d}$.

    **Proof**:
    For equal roots, $D = 0 \implies B^2 - 4AC = 0$:
    $$[-2(ac + bd)]^2 - 4(a^2 + b^2)(c^2 + d^2) = 0$$
    $$4(ac + bd)^2 - 4(a^2 + b^2)(c^2 + d^2) = 0$$

    Divide by $4$:
    $$(a^2c^2 + 2abcd + b^2d^2) - (a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2) = 0$$
    $$2abcd - a^2d^2 - b^2c^2 = 0$$

    Multiply by $-1$:
    $$a^2d^2 - 2abcd + b^2c^2 = 0$$
    $$(ad - bc)^2 = 0 \implies ad - bc = 0 \implies ad = bc$$
    $$\frac{a}{b} = \frac{c}{d} \quad \blacksquare$$

---

## 4. Word Problems & Applications

### Category 1: Speed, Distance & Time

#### Uniform Speed vs. Speed Increase/Decrease
- Relationship: $\text{Time} = \frac{\text{Distance}}{\text{Speed}}$.
- If speed increases by $\Delta v$, time taken decreases: $t_{\text{slow}} - t_{\text{fast}} = \Delta t$.

!!! example "Problem 1: Train Speed"
    A train travels $360\text{ km}$ at a uniform speed. If the speed had been $5\text{ km/h}$ more, it would have taken $1\text{ hour}$ less for the same journey. Find the speed of the train.

    **Setup**:
    Let uniform speed of train = $x\text{ km/h}$.
    Time taken at original speed = $\frac{360}{x}\text{ hours}$.
    Time taken at increased speed $(x+5)\text{ km/h} = \frac{360}{x+5}\text{ hours}$.

    **Equation**:
    $$\frac{360}{x} - \frac{360}{x + 5} = 1$$
    $$360 \left( \frac{x + 5 - x}{x(x + 5)} \right) = 1 \implies \frac{360(5)}{x^2 + 5x} = 1$$
    $$1800 = x^2 + 5x \implies x^2 + 5x - 1800 = 0$$
    
    Factorizing ($45 \times 40 = 1800$):
    $$(x + 45)(x - 40) = 0 \implies x = 40 \quad (\text{since speed } x > 0)$$
    **Answer**: Speed of train = $40\text{ km/h}$.

---

#### Upstream and Downstream Boat Problems
Let:
- Speed of boat in still water = $v\text{ km/h}$
- Speed of stream / current = $y\text{ km/h}$

Then:
- **Upstream Speed** (against current): $v_{\text{up}} = v - y$
- **Downstream Speed** (with current): $v_{\text{down}} = v + y$

!!! example "Problem 2: Motorboat Stream Problem"
    A motorboat whose speed is $18\text{ km/h}$ in still water takes $1\text{ hour}$ more to go $24\text{ km}$ upstream than to return downstream to the same spot. Find the speed of the stream.

    **Setup**:
    Let speed of stream = $y\text{ km/h}$.
    Upstream speed = $18 - y$, Downstream speed = $18 + y$.
    
    $$\text{Time upstream} - \text{Time downstream} = 1\text{ hour}$$
    $$\frac{24}{18 - y} - \frac{24}{18 + y} = 1$$
    $$24 \left( \frac{(18 + y) - (18 - y)}{(18 - y)(18 + y)} \right) = 1$$
    $$\frac{24(2y)}{324 - y^2} = 1 \implies 48y = 324 - y^2$$
    $$y^2 + 48y - 324 = 0$$

    Factorizing ($54 \times 6 = 324$):
    $$(y + 54)(y - 6) = 0 \implies y = 6 \quad (\text{rejecting } y = -54)$$
    **Answer**: Speed of stream = $6\text{ km/h}$.

---

### Category 2: Work & Time (Taps & Pipes)

- If a pipe fills a tank in $x$ hours, part filled in 1 hour = $\frac{1}{x}$.

!!! example "Problem 3: Simultaneous Taps"
    Two water taps together can fill a tank in $9\frac{3}{8} = \frac{75}{8}\text{ hours}$. The tap of larger diameter takes $10\text{ hours}$ less than the smaller one to fill the tank separately. Find the time in which each tap can separately fill the tank.

    **Setup**:
    Let time taken by smaller tap = $x\text{ hours}$.
    Time taken by larger tap = $(x - 10)\text{ hours}$.
    Combined 1-hour work:
    $$\frac{1}{x} + \frac{1}{x - 10} = \frac{8}{75}$$
    $$\frac{x - 10 + x}{x(x - 10)} = \frac{8}{75} \implies \frac{2x - 10}{x^2 - 10x} = \frac{8}{75}$$
    $$75(2x - 10) = 8(x^2 - 10x)$$
    $$150x - 750 = 8x^2 - 80x \implies 8x^2 - 230x + 750 = 0$$
    Divide by 2:
    $$4x^2 - 115x + 375 = 0$$

    Factorizing ($4 \times 375 = 1500 = 100 \times 15$):
    $$4x^2 - 100x - 15x + 375 = 0$$
    $$4x(x - 25) - 15(x - 25) = 0 \implies (4x - 15)(x - 25) = 0$$
    - If $x = \frac{15}{4} = 3.75$, then larger tap time $x - 10 = 3.75 - 10 = -6.25$ (impossible).
    - Therefore $x = 25$.
    
    **Answer**: Smaller tap = $25\text{ hours}$, Larger tap = $15\text{ hours}$.

---

### Category 3: Geometry & Right-Angled Triangles

- By Pythagoras Theorem: $\text{Base}^2 + \text{Altitude}^2 = \text{Hypotenuse}^2$.

!!! example "Problem 4: Inscribed Triangle in Circle"
    $AB$ is the diameter of a circle of length $65\text{ cm}$. A point $C$ on the circle forms a right-angled triangle $ABC$ with angle $C = 90^\circ$ (angle in a semicircle). If $AC$ exceeds $BC$ by $7\text{ cm}$, find the lengths of $AC$ and $BC$.

    **Setup**:
    Hypotenuse $AB = 65\text{ cm}$.
    Let $BC = x\text{ cm} \implies AC = (x + 7)\text{ cm}$.

    By Pythagoras Theorem:
    $$BC^2 + AC^2 = AB^2$$
    $$x^2 + (x + 7)^2 = 65^2$$
    $$x^2 + x^2 + 14x + 49 = 4225$$
    Using the Quadratic Formula for $x^2 + 7x - 2088 = 0$:
    $$x = \frac{-7 \pm \sqrt{7^2 - 4(1)(-2088)}}{2(1)} = \frac{-7 \pm \sqrt{49 + 8352}}{2} = \frac{-7 \pm \sqrt{8401}}{2}$$
    
    Since length $x > 0$:
    $$x = \frac{-7 + \sqrt{8401}}{2} \approx 42.33\text{ cm}$$

    **Answer**: $BC \approx 42.33\text{ cm}$, $AC = x + 7 \approx 49.33\text{ cm}$.

---

## Quick Formula Reference Cheat Sheet

1. **Standard Form**: $ax^2 + bx + c = 0 \quad (a \neq 0)$
2. **Discriminant**: $D = b^2 - 4ac$
3. **Roots Formula**: $x = \frac{-b \pm \sqrt{D}}{2a}$
4. **Nature of Roots**:
   - $D > 0 \implies$ Two Real & Distinct Roots
   - $D = 0 \implies$ Two Real & Equal Roots ($x = -\frac{b}{2a}$)
   - $D < 0 \implies$ No Real Roots
5. **Upstream/Downstream Speeds**:
   - $v_{\text{up}} = v_{\text{boat}} - v_{\text{stream}}$
   - $v_{\text{down}} = v_{\text{boat}} + v_{\text{stream}}$
