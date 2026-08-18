# Coordinate Geometry

> CAT quant. The topic you switch *into* when a synthetic argument stalls. Anything involving midpoints, parallels, perpendiculars or a fixed axis is usually faster on axes than in a hand-drawn figure — and the answer comes out exact instead of eyeballed. Formulas here are deliberately few; the skill is choosing the origin well.

---

## 1. When to reach for coordinates

Put the figure on axes when the question gives you any of:

- **Actual coordinates** — then there is no choice, and no synthetic detour is worth trying.
- **Midpoints, medians, or ratios along a segment** — the section formula handles them in one line.
- **Perpendiculars, or a rectangle/square** — align the sides with the axes and everything becomes arithmetic.
- **A reflection or a fold** — see `Triangles.md` §11; a fold is a reflection, and reflections are trivial on axes.

**Choose the origin to kill the most zeros.** Put it at a right-angle vertex, at the centre of a circle, or at the midpoint of a symmetric figure. Half the algebra in a coordinate question is decided before you write a single equation.

---

## 2. Points — distance, section, midpoint

For A(x₁, y₁) and B(x₂, y₂):

- **Distance** AB = √((x₂ − x₁)² + (y₂ − y₁)²)
- **Midpoint** = ((x₁ + x₂)/2, (y₁ + y₂)/2)
- **Section formula**, point dividing AB internally in m : n (measured **from A**):

  **P = ((mx₂ + nx₁)/(m + n), (my₂ + ny₁)/(m + n))**

- **External division** in m : n — same formula with n replaced by −n
- **Centroid** of a triangle = ((x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3)

The section formula is a **weighted average** (`Means-and-Weighted-Averages.md` §3): the far endpoint gets the near weight. If you remember it as "cross the weights", you will never write it upside down.

---

## 3. Straight lines

**Slope** m = (y₂ − y₁)/(x₂ − x₁). Vertical lines have no slope; horizontal lines have slope 0.

| Form | Equation | Use when |
|---|---|---|
| Slope–point | y − y₁ = m(x − x₁) | you have one point and the slope — **the default** |
| Two-point | (y − y₁)/(x − x₁) = (y₂ − y₁)/(x₂ − x₁) | two points given |
| Slope–intercept | y = mx + c | c is the y-intercept, read off directly |
| Intercept | x/a + y/b = 1 | the question mentions axis intercepts |
| General | ax + by + c = 0 | slope = −a/b |

**Axis intercepts, the one-second version:** in any equation, set **x = 0 for the y-intercept** and **y = 0 for the x-intercept**. Most "where does the line meet the axis" questions are exactly this and nothing more.

---

## 4. Parallel, perpendicular, angle, distance

- **Parallel** ⟺ m₁ = m₂
- **Perpendicular** ⟺ **m₁·m₂ = −1** (a vertical and a horizontal line are the exception — the product is undefined)
- **Angle between two lines:** tan θ = |(m₁ − m₂)/(1 + m₁m₂)|
- **Distance from (x₀, y₀) to ax + by + c = 0:** |ax₀ + by₀ + c| / √(a² + b²)
- **Distance between parallels** ax + by + c₁ = 0 and ax + by + c₂ = 0: |c₁ − c₂| / √(a² + b²) — the a and b must match first

---

## 5. Type 1 — Quadrilaterals from their vertices

**The one fact that answers most of them: the diagonals of a parallelogram bisect each other.** So for parallelogram ABCD (vertices named *in order* round the shape),

**midpoint of AC = midpoint of BD**, and therefore **D = A + C − B**

Add coordinatewise. The same relation rearranged finds any missing vertex.

**Recognising the other shapes from coordinates:**

| Shape | Test |
|---|---|
| Parallelogram | diagonals share a midpoint (or one pair of opposite sides equal and parallel) |
| Rhombus | parallelogram **and** all four sides equal |
| Rectangle | parallelogram **and** equal diagonals |
| Square | both of the above |
| Any quadrilateral, is it cyclic? | opposite angles sum to 180° — usually easier via `Circles.md` §4 |

**Worked example:** Three consecutive vertices of parallelogram ABCD are A(−4, −2), B(2, 3) and C(7, 1). The diagonal BD meets the y-axis at P. Find the y-coordinate of P.

- **Find D.** D = A + C − B = (−4 + 7 − 2, −2 + 1 − 3) = **(1, −4)**
  - (Check: midpoint of AC = (1.5, −0.5); midpoint of BD = (1.5, −0.5) ✓)
- **Slope of BD** = (−4 − 3)/(1 − 2) = (−7)/(−1) = **7**
- **Line BD** through B(2, 3): y − 3 = 7(x − 2)
- **y-axis** means x = 0: y = 3 + 7(0 − 2) = 3 − 14 = **−11**

**Traps:**
- Using D = B + C − A or any other permutation. Only the *diagonals* bisect, so the missing vertex is (sum of the two ends of the known diagonal) − (the known vertex on the other diagonal). With A, B, C consecutive, AC and BD are the diagonals, so D = A + C − B.
- Being thrown that P lies **outside** segment BD (B has x = 2, D has x = 1, the y-axis is at x = 0). "The diagonal meets the y-axis" means the *line* through B and D; extending is expected.
- Sign slips in the slope. Both differences must be taken in the same order, B → D or D → B.
- Assuming ABCD is a rectangle. Nothing here says the sides are perpendicular — check before using any right-angle fact.

---

## 6. Area from coordinates, and collinearity

**Triangle area (shoelace):**

**Area = ½ |x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|**

- **Collinear ⟺ this area is 0.** That is the fastest collinearity test there is — faster than comparing two slopes, and it never divides by zero.
- For a polygon, walk the vertices in order and sum x_i·y_{i+1} − x_{i+1}·y_i, then halve the absolute value. Going round in the wrong order gives nonsense, so keep the cycle consistent.
- **Quadrilateral shortcut:** if the diagonals are known and perpendicular, Area = ½ d₁d₂ (`Quadrilaterals-and-Polygons.md` §1).

**Worked example:** Are (1, 2), (3, 6) and (5, 10) collinear?
- ½ |1(6 − 10) + 3(10 − 2) + 5(2 − 6)| = ½ |−4 + 24 − 20| = **0** ⟹ yes.

---

## 7. Circles in coordinates

- **Centre (h, k), radius r:** (x − h)² + (y − k)² = r²
- **General form:** x² + y² + 2gx + 2fy + c = 0 ⟹ centre **(−g, −f)**, radius **√(g² + f² − c)**
- A point is inside / on / outside according as x² + y² + 2gx + 2fy + c is < / = / > 0
- **Tangency of a line to a circle** ⟺ distance from the centre to the line = r. Use §4's distance formula; do not substitute and take a discriminant unless you must.

The synthetic circle facts — chords, tangents, alternate segment, power of a point — live in `Circles.md` §2–§4 and are not repeated here.

---

## 8. Type 2 — Reflections and shortest paths

- **Reflection in the x-axis:** (a, b) → (a, −b). **In the y-axis:** (a, b) → (−a, b). **In the origin:** (a, b) → (−a, −b). **In y = x:** (a, b) → (b, a).
- **Reflection in a general line:** the line is the perpendicular bisector of the segment joining a point to its image — the same statement that governs folding in `Triangles.md` §11.

**Shortest path touching a line:** to minimise PA + AB where A must lie on a given line, reflect one endpoint across the line and join it straight to the other. The straight distance between P′ and B *is* the minimum, and it crosses the line at the optimal A.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Missing vertex of a parallelogram | any of A+B−C, B+C−A | the diagonals bisect: D = A + C − B for ABCD in order |
| Section formula | m with the near point | cross the weights — m goes with the far endpoint |
| "Diagonal meets the axis" | must lie between the vertices | the *line* is meant; extend it |
| Perpendicular slopes | m₁ = −m₂ | m₁·m₂ = −1 |
| Collinearity | compare slopes and divide by zero | set the shoelace area to 0 |
| Shoelace on a polygon | vertices in any order | walk the boundary in a consistent cycle |
| General circle radius | √(g² + f²) | √(g² + f² − c) |
| Distance between parallels | subtract the constants directly | normalise so a and b match, then |c₁ − c₂|/√(a²+b²) |
| Choosing the origin | wherever the figure sits | at a right angle, centre, or symmetry point |

---

## Practical exam habits

- **Place the origin before you write anything.** A well-chosen origin turns half the coordinates into zeros and is worth more than any formula on this page.
- If the question hands you numeric coordinates, do not look for a synthetic shortcut. Compute.
- Sketch the points roughly to scale. It catches sign errors instantly, and it tells you whether an intersection falls inside or outside a segment.
- Prefer the distance-from-a-point formula over substituting and solving a quadratic. It is one line and cannot produce extraneous roots.
- When a figure has a right angle, a midpoint and a reflection all at once, coordinates will beat synthetic geometry nearly every time.

**Where this feeds forward:** `Triangles.md`, `Circles.md` and `Quadrilaterals-and-Polygons.md` (the synthetic versions of everything here, plus Triangles §11 folding as reflection), `Algebra.md` §2 (line–curve intersections are quadratics), `Means-and-Weighted-Averages.md` §3 (the section formula is a weighted average).
