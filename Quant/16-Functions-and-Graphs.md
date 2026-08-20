# Functions & Graphs

> CAT quant. The topic where **drawing beats solving**. A question that looks like it needs algebra — how many solutions, what is the maximum, for which k does this hold — usually collapses the moment you sketch it. The algebraic machinery for inequalities and maxima lives in `13-Algebra.md`; this file is about the function itself and its picture.

---

## 1. What CAT actually asks

Four shapes of question, and almost nothing else:

1. **Evaluate or invert** — find f(2), find f⁻¹, find f(g(x)). Mechanical.
2. **Domain and range** — where is this defined, what values does it take.
3. **Count the solutions** — how many x satisfy this. Sketch it; do not solve it.
4. **Find the maximum or minimum** — pick the right tool from §11 rather than differentiating.

**The habit that decides the topic:** before manipulating anything, ask *what does this look like*. A rough sketch takes fifteen seconds and answers types 3 and 4 outright.

---

## 2. Domain and range

**Domain** = the x values that are legal. Only four things make an x illegal:

| Structure | Requirement |
|---|---|
| denominator | ≠ 0 |
| **even** root √(…) | the inside must be ≥ 0 |
| log(…) | the inside must be **> 0**, and the base > 0, ≠ 1 |
| f(g(x)) | g(x) must lie in the domain of f |

Odd roots (∛) impose nothing — a very common false restriction.

**Range** = the y values actually reached. Three reliable methods, in order of preference:

1. **Sketch it.** Fastest whenever the shape is standard (§7).
2. **Solve for x in terms of y**, then apply the domain rules *to y*. This is the workhorse for rational functions.
3. **Complete the square** or bound each piece for quadratics and sums of squares.

**Worked example:** Find the range of f(x) = (x + 1)/(x − 2).
- Solve for x: y(x − 2) = x + 1 ⟹ x(y − 1) = 2y + 1 ⟹ x = (2y + 1)/(y − 1)
- x exists for every y except y = 1 ⟹ range = **ℝ \ {1}**
- (Domain, by the same reading, is ℝ \ {2}.)

**Worked example:** Find the range of f(x) = x² − 4x + 7.
- Complete the square: (x − 2)² + 3 ⟹ minimum 3, unbounded above ⟹ **[3, ∞)**

**The reflex worth building:** for a rational function (ax+b)/(cx+d), the domain excludes −d/c and the range excludes a/c. Both are read off the coefficients with no work.

---

## 3. Classifying a function

- **One-one (injective):** different x give different f(x). Graphically, no horizontal line meets the curve twice.
- **Onto (surjective):** the range equals the stated co-domain.
- **Even:** f(−x) = f(x) — symmetric about the **y-axis**. Only even powers.
- **Odd:** f(−x) = −f(x) — symmetric about the **origin**. Only odd powers, and f(0) = 0 if 0 is in the domain.
- **Periodic:** f(x + T) = f(x) for some smallest T > 0. {x} has period 1; trigonometric functions have their own.

**Most functions are neither even nor odd** — x² + x, for instance. "Neither" is a legitimate answer and CAT offers it.

**Useful decomposition:** any f can be written as an even part plus an odd part, [f(x) + f(−x)]/2 + [f(x) − f(−x)]/2. That identity is occasionally the entire question.

---

## 4. Composition and inverse

- **Composite:** work **inside out**. f(g(x)) means apply g first. In general f(g(x)) ≠ g(f(x)) — and a question asking you to verify that is asking you to find one counterexample, not to prove anything.
- **Inverse exists only if f is one-one.** To find it: write y = f(x), swap x and y, solve for y.
- **f and f⁻¹ are reflections of each other in the line y = x.** So their graphs meet *on* y = x — which turns "solve f(x) = f⁻¹(x)" into the far easier "solve f(x) = x".
- Domain of f⁻¹ = range of f, and vice versa.

**Worked example:** f(x) = (3x − 2)/5. Find f⁻¹(x).
- y = (3x − 2)/5 ⟹ swap ⟹ x = (3y − 2)/5 ⟹ 5x + 2 = 3y ⟹ f⁻¹(x) = **(5x + 2)/3**

**Self-inverse functions** — f(f(x)) = x — appear regularly: 1/x, a − x, and (ax + b)/(cx − a) for any a, b, c. Spotting one collapses "find f applied 99 times" to a parity check.

**Iterated functions:** if f is applied n times, compute f(f(x)) and f(f(f(x))) and look for a cycle. Almost every CAT iteration question has a cycle of length 2, 3 or 4.

---

## 5. Type 1 — Functional equations

**The reciprocal / negation trick.** Given one relation in f(x) and f(1/x) (or f(−x)), substitute the *other* value to get a second equation, then solve the pair simultaneously.

**Worked example:** If f(x) + 2f(1/x) = 3x, find f(2).
- x = 2: f(2) + 2f(1/2) = 6
- x = 1/2: f(1/2) + 2f(2) = 3/2
- Double the second and subtract the first: 3f(2) = 3 − 6 ⟹ f(2) = **−1**

**The standard families, worth recognising on sight:**

| Given | Conclusion |
|---|---|
| f(x + y) = f(x) + f(y) | f(x) = cx — set y = x to get f(2x) = 2f(x), then build up |
| f(xy) = f(x) + f(y) | f is a **logarithm** |
| f(x + y) = f(x)·f(y) | f is an **exponential**, f(x) = aˣ |
| f(x)·f(1/x) = f(x) + f(1/x) | f(x) = 1 ± xⁿ |

**Method for any unfamiliar one:** substitute the special values x = 0, x = 1, y = x, y = 1/x, y = −x in that order. One of them almost always cracks it.

---

## 6. Greatest integer [x] and fractional part {x}

- **[x]** = the greatest integer ≤ x. So [2.7] = 2 but **[−2.7] = −3**, not −2. This sign behaviour is the single most tested point.
- **{x}** = x − [x], always in **[0, 1)**. {−2.7} = 0.3.
- **x = [x] + {x}** always. Splitting an equation into its integer and fractional parts is the standard method — the integer parts must match and the fractional parts must match, exactly as with rational and irrational parts (`13-Algebra.md` §4).
- [x + n] = [x] + n for **integer** n only.
- [x] + [−x] = 0 if x is an integer, **−1** otherwise.

**Worked example:** Solve [x] = 2{x} + 1 for real x.
- {x} ∈ [0,1) ⟹ 2{x} + 1 ∈ [1, 3) ⟹ [x] ∈ {1, 2}
- [x] = 1 ⟹ {x} = 0 ⟹ x = 1
- [x] = 2 ⟹ {x} = ½ ⟹ x = 2.5
- **x = 1 or 2.5**

**Graph shapes:** y = [x] is a staircase, flat on [n, n+1) with a jump of 1 at each integer. y = {x} is a sawtooth, period 1, rising from 0 to 1.

---

## 7. The standard graphs — know these by shape

| Function | Shape | Note |
|---|---|---|
| y = mx + c | line | slope m, intercept c |
| y = x² | parabola, opening up | vertex at the origin |
| y = x³ | rising S through the origin | odd |
| y = 1/x | rectangular hyperbola | asymptotes at both axes; odd |
| y = 1/x² | two branches, both above the axis | even |
| y = \|x\| | V | vertex at the origin |
| y = √x | half-parabola, x ≥ 0 only | |
| y = aˣ (a > 1) | rising, always positive | passes (0, 1) |
| y = log x | rising, slow | passes (1, 0); undefined for x ≤ 0 |
| y = [x] | staircase | jumps at integers |
| y = {x} | sawtooth | period 1 |

**The three you must be able to draw without thinking** are the parabola, y = 1/x and y = |x|. Between them they underlie most CAT graph questions.

---

## 8. Transformations — how to get any graph from a standard one

Starting from y = f(x):

| New function | Effect |
|---|---|
| f(x) + a | shifts **up** by a |
| f(x + a) | shifts **left** by a (not right — this is the classic slip) |
| a·f(x), a > 1 | stretches vertically |
| f(ax), a > 1 | **compresses** horizontally by a |
| −f(x) | reflects in the **x-axis** |
| f(−x) | reflects in the **y-axis** |

Apply them in the order the expression is built from the inside out. y = 2(x − 3)² + 1 is: parabola → right 3 → stretch ×2 → up 1.

**The two modulus transformations are different from each other and both are tested:**

- **y = \|f(x)\|** — take everything below the x-axis and **flip it up**. The graph never goes negative.
- **y = f(\|x\|)** — **delete** the left half and replace it with a mirror image of the right half. The result is always even.

**Worked example:** How do y = |x² − 4| and y = |x|² − 4 differ?
- The first flips the dip between x = −2 and 2 upward, giving a W-like shape with minimum 0.
- The second is just x² − 4, since |x|² = x². Unchanged parabola, minimum −4.

---

## 9. Type 2 — Counting solutions graphically

**The method, and it is the whole section:** put the equation in the form **f(x) = g(x)**, sketch both, and count intersections. Never solve.

Choose the split so that both sides are standard shapes. For x² = 2ˣ, sketch a parabola and an exponential rather than attacking x² − 2ˣ = 0.

**Worked example:** How many real solutions does |x − 1| + |x − 3| = 4 have?
- The left side is a piecewise-linear valley: it equals 2 on the whole interval [1, 3], and rises with slope 2 outside.
- y = 4 is a horizontal line, above the flat floor of 2 ⟹ it cuts each rising arm once ⟹ **2 solutions** (x = 0 and x = 4).
- Had the right side been 2, the line would lie **along** the floor ⟹ infinitely many. Had it been 1, none.

That parameter sweep — no solutions / infinitely many / exactly two — is exactly what CAT asks, and the sketch answers all three at once. The algebraic treatment of these sums is `13-Algebra.md` §6b.

**Worked example:** For how many integers k does x² − 6x + k = 0 have two distinct real roots with both roots positive?
- Two distinct real: discriminant 36 − 4k > 0 ⟹ k < 9
- Both roots positive: sum = 6 > 0 ✓ and product = k > 0
- ⟹ 0 < k < 9 ⟹ **k = 1 … 8, eight values**

---

## 10. Type 3 — Regions of a two-variable inequality

**y > f(x)** is the region **above** the curve; y < f(x) is below. For a straight line, test the origin — if it satisfies the inequality, shade the side containing it, otherwise the other side. A strict inequality means a dashed boundary that is not included.

Several inequalities together give a **feasible region**; its corners are the intersections of the boundary lines, and any linear expression is maximised or minimised **at a corner** (the same endpoint logic as `01-Number-System.md` §11).

**|x| + |y| ≤ a** is the square with vertices (±a, 0) and (0, ±a) — a diamond, area 2a². **max(|x|, |y|) ≤ a** is the ordinary axis-aligned square of side 2a. Both appear as "find the area of the region" questions and both are answered by drawing four lines.

---

## 11. Maxima and minima — pick the tool, don't differentiate

| Shape of the expression | Tool |
|---|---|
| quadratic | vertex at x = −b/2a — `13-Algebra.md` §2 |
| product with a fixed sum, or sum with a fixed product | AM ≥ GM — `13-Algebra.md` §6 |
| xᵃyᵇzᶜ under a linear constraint | AM–GM with split terms — `13-Algebra.md` §6a |
| sum of moduli | convex; minimum at the median — `13-Algebra.md` §6b |
| sum of squares | each square ≥ 0; minimum when each is 0 |
| a rational function | solve for x in terms of y and force the discriminant ≥ 0 |
| anything with a sketchable shape | read it off the graph |

**The discriminant method, worth one worked example** because it is the one people never think of:

**Worked example:** Find the range of y = (x² + 2x + 1)/(x² + 2x + 7) for real x.
- Cross-multiply: y(x² + 2x + 7) = x² + 2x + 1 ⟹ (y − 1)x² + 2(y − 1)x + (7y − 1) = 0
- For real x the discriminant must be ≥ 0: 4(y−1)² − 4(y−1)(7y−1) ≥ 0 ⟹ 4(y−1)[(y−1) − (7y−1)] ≥ 0 ⟹ 4(y−1)(−6y) ≥ 0
- ⟹ y(y − 1) ≤ 0 ⟹ **0 ≤ y < 1** (y = 1 is excluded, since it kills the x² term and forces 6 = 0)
- Sanity check: the numerator is (x+1)², never negative, and always smaller than the denominator ⟹ 0 ≤ y < 1 ✓

**Never differentiate in this exam.** Every maximum CAT sets is reachable by one of the rows above, and calculus is slower and more error-prone under time pressure.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| f(x + a) | shifts right by a | shifts **left** by a |
| \|f(x)\| vs f(\|x\|) | treated as the same | flip up the negatives vs mirror the right half |
| [−2.7] | −2 | **−3** — [x] rounds *down*, always |
| {x} of a negative number | negative | always in [0, 1): {−2.7} = 0.3 |
| Domain of ∛(…) | inside ≥ 0 | odd roots accept everything |
| Domain of log | inside ≥ 0 | strictly **> 0** |
| f(g(x)) | equals g(f(x)) | not in general |
| Inverse of a many-one function | computed anyway | it does not exist |
| Solving f(x) = f⁻¹(x) | expand both | they meet on y = x, so solve f(x) = x |
| Even/odd | every function is one or the other | most are neither |
| Counting solutions | solve the equation | sketch both sides and count crossings |
| Maxima | differentiate | vertex, AM–GM, or discriminant |
| Range of a rational function | same as the domain | solve for x in terms of y |

---

## Practical exam habits

- Sketch first. Fifteen seconds of drawing routinely replaces two minutes of algebra, and it is the only reliable way to count solutions.
- For any "how many solutions" question, split into f(x) = g(x) so that **both sides are shapes you already know**.
- Read every square root and log for its domain restriction before doing anything else — a large share of these questions are decided by the domain alone.
- With [x] or {x}, immediately write x = [x] + {x} and split the equation into integer and fractional parts.
- If a maximum or minimum question is taking more than a minute, you have picked the wrong tool from §11, not made an arithmetic error.

**Where this feeds forward:** `13-Algebra.md` §2 (quadratics), §6–§6b (AM–GM, moduli, the inequality machinery this file draws on), `21-Coordinate-Geometry.md` §3 (lines as graphs), `14-Logarithms.md` (the log and exponential shapes), `01-Number-System.md` §11 (optimisation at an endpoint).
