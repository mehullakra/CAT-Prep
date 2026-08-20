# Quadrilaterals & Polygons

> CAT quant. Mostly a bookkeeping topic — the formulas are short and the marks are lost to using the wrong one for the wrong shape. The two things worth real attention are the **trapezium** and the **optimisation** family, which are where CAT actually sets hard questions.

Approach discipline for any plane figure lives in `17-Triangles.md` §1.

---

## 1. The quadrilateral family

| Shape | Sides | Angles | Diagonals | Area |
|---|---|---|---|---|
| Parallelogram | opposite equal | opposite equal | bisect each other | base × height = ab·sin θ |
| Rectangle | opposite equal | all 90° | equal, bisect | l × b |
| Rhombus | all equal | opposite equal | **perpendicular**, bisect | ½ d₁d₂ = a²·sin θ |
| Square | all equal | all 90° | equal, perpendicular, bisect | a² = ½ d² |
| Kite | two adjacent pairs equal | one pair equal | **perpendicular**, long one bisects short | ½ d₁d₂ |
| Trapezium | one pair parallel | — | — | ½(a + b)h |
| Cyclic | — | opposite sum 180° | — | Brahmagupta (`18-Circles.md` §4) |

**Any quadrilateral with perpendicular diagonals has area ½ d₁d₂.** That covers rhombus, square and kite in one line — do not memorise three formulas.

**The general quadrilateral:** split it into two triangles along a diagonal. There is no usable single formula unless it is cyclic, so the diagonal split *is* the method.

**Every quadrilateral's midpoint figure is a parallelogram** (Varignon), with **half the area** of the original — a neat fact that occasionally answers a whole question.

---

## 2. Parallelogram, rhombus, rectangle, square

- **Parallelogram law:** d₁² + d₂² = 2(a² + b²) — the sum of the squares of the diagonals equals the sum of the squares of the four sides
- A diagonal splits a parallelogram into **two congruent triangles**; both diagonals split it into **four equal-area** triangles (not congruent in general)
- **Rhombus:** the diagonals bisect the vertex angles, and half-diagonals with a side form a right triangle ⟹ (d₁/2)² + (d₂/2)² = a²
- **Square:** diagonal = a√2, and area = ½d². A square of diagonal 10√2 has area ½(200) = **100**
- **Rectangle:** the diagonals are equal, so the circumcircle exists with R = d/2

**Worked example:** A rhombus has diagonals 24 and 10. Find its area and side.
- Area = ½ × 24 × 10 = **120**
- Side = √(12² + 5²) = **13** (5-12-13)

**A rhombus is not a square.** CAT sets equal-side quadrilaterals that are deliberately not right-angled; nothing about a rhombus forces 90°.

---

## 3. Trapezium

One pair of parallel sides, a and b, with perpendicular height h between them.

- **Area = ½(a + b)h** — the average of the parallel sides times the height
- **Midsegment** (joining the midpoints of the two non-parallel sides) = **(a + b)/2**, and it is parallel to both. So the area is also midsegment × height.
- **Isosceles trapezium:** the non-parallel sides are equal, base angles are equal, diagonals are equal, and it is **cyclic**
- The diagonals cut it into four triangles: the two on the parallel sides have areas in ratio **a² : b²**, and the two side triangles are **equal in area**

**Finding h when only the four sides are given:** drop perpendiculars from both ends of the shorter parallel side. The base splits into (a − b) in the middle plus two right-triangle feet — solve those with Pythagoras.

**Worked example:** Parallel sides 12 and 20, height 9. Find the area.
- ½(12 + 20)(9) = ½ × 32 × 9 = **144**

**The trap:** using a slant side as the height. h is the **perpendicular** distance between the parallel sides, never the length of the leg — unless the trapezium is right-angled and that leg *is* the perpendicular.

---

## 4. Type 1 — Tangential quadrilaterals and the incircle

A quadrilateral has an **incircle** (all four sides tangent to one circle) ⟺ **a + c = b + d** (Pitot: sums of opposite sides are equal).

For any tangential polygon, **Area = r × s** with s the semi-perimeter, so

**r = Area / s**

That one relation answers nearly every "find the inradius" question; the work is computing the area.

**Worked example:** A quadrilateral circumscribes a circle; three consecutive sides are 6, 8 and 9. Find the fourth.
- Pitot: 6 + 9 = 8 + d ⟹ d = **7**

### Kite circumscribing a circle

A kite has sides a, a, b, b, so Pitot holds automatically — **every kite has an incircle**.

- Diagonals are perpendicular; the long one bisects the short one and the two vertex angles it passes through
- Area = ½ d₁d₂, semi-perimeter s = a + b, hence **r = (½d₁d₂)/(a + b)**

**Worked example:** Sides 13, 13, 20, 20, short diagonal 24.
- Half the short diagonal is 12. From the 13-side vertex: √(169 − 144) = 5. From the 20-side vertex: √(400 − 144) = 16.
- Long diagonal = 5 + 16 = 21 ⟹ Area = ½ · 24 · 21 = 252; s = 33 ⟹ r = 252/33 = **84/11 ≈ 7.64**

**Rhombus special case:** all sides a ⟹ s = 2a and r = d₁d₂/(4a).

There is no simpler kite-inradius formula. Get both diagonals by Pythagoras, take ½d₁d₂, divide by s.

---

## 5. Polygons — angles and diagonals

- Sum of **interior** angles = **(n − 2)·180°**
- Sum of **exterior** angles = **360°**, always, for any convex polygon
- Regular n-gon: each interior angle = (n−2)·180/n, each exterior angle = **360/n**
- **Number of diagonals = n(n − 3)/2**
- Number of triangles formed by joining vertices (no three collinear) = C(n, 3) — see `23-PnC-Probability.md` §11

**Always work from the exterior angle.** It is 360/n, so "interior angle 156°" means exterior 24°, so n = 360/24 = **15**. Going via the interior formula takes three times as long and invites arithmetic slips.

**Worked example:** A polygon has 54 diagonals. Find n.
- n(n−3)/2 = 54 ⟹ n² − 3n − 108 = 0 ⟹ (n − 12)(n + 9) = 0 ⟹ **n = 12**

**Worked example:** The interior angles sum to 1440°. Find n.
- (n − 2)180 = 1440 ⟹ n − 2 = 8 ⟹ **n = 10**

---

## 6. Regular polygons — the metric formulas

For a regular n-gon of side a, with R the circumradius and r the inradius (apothem):

- **R = a / (2 sin(180°/n))**
- **r = a / (2 tan(180°/n))**
- **Area = ½ · perimeter · r = ½ n a r**, equivalently **(n a²)/(4 tan(180°/n))**

You will rarely need the general form in the exam; the three cases below cover almost everything.

| Regular figure | R | r | Area |
|---|---|---|---|
| Equilateral triangle | a/√3 | a/(2√3) | (√3/4)a² |
| Square | a/√2 | a/2 | a² |
| Hexagon | a | a√3/2 | **(3√3/2)a²** |

**The hexagon is six equilateral triangles** of side a, which is why R = a. Deriving the area that way is faster and safer than recalling 3√3/2.

**Worked example:** A regular hexagon of side 6 has area (3√3/2)(36) = **54√3**.

---

## 7. Type 2 — Optimisation: fixed area or fixed perimeter

**The two governing principles:**

- For a **fixed perimeter**, area is maximised by the most symmetric shape — square among rectangles, circle among all shapes
- For a **fixed area**, perimeter is minimised by that same shape

These are AM–GM in geometric clothing (`13-Algebra.md` §6).

**Plain case:** rectangle of perimeter P ⟹ maximum area P²/16, at the square. Rectangle of area A ⟹ minimum perimeter 4√A, again at the square.

**Worked example:** Perimeter 40 ⟹ max area = 40²/16 = **100** (a 10 × 10 square).

### The wall variant (one side free) — the version CAT actually asks

A rectangular plot against a straight wall, fenced on three sides. Let y be the side parallel to the wall and x each perpendicular side. Fence F = 2x + y, area A = xy.

- F = 2x + A/x ≥ 2√(2A), equality when 2x = A/x ⟹ **y = 2x**
- **The side parallel to the wall is twice each perpendicular side.** Minimum fencing = 2√(2A).
- Read the other way: with F metres of fence, area is maximised at y = F/2, x = F/4, giving **A = F²/8**

**Worked example:** 60 m of fence against a wall. Maximum area?
- y = 30, x = 15 ⟹ A = **450 m²** (check: F²/8 = 3600/8 = 450 ✓)

**The general rule:** at the optimum, **the total length spent in each direction is equal**. Two sides of x and one of y ⟹ 2x = y. That same balancing extends to plots with internal dividing fences, which is the harder CAT variant — three parallel dividers plus two ends means 3x = y.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Trapezium height | use the slant side | h is the perpendicular distance |
| Rhombus / kite area | base × height guessed | ½ d₁d₂ — any perpendicular-diagonal quadrilateral |
| Rhombus assumed square | 90° angles | equal sides only; no right angle is implied |
| Parallelogram assumed cyclic | yes | only if it's a rectangle |
| Incircle of a quadrilateral | every quadrilateral has one | needs a + c = b + d |
| Polygon side count | via the interior-angle formula | exterior angle = 360/n is far faster |
| Exterior angle sum | (n−2)·180 | always 360° |
| Diagonals of an n-gon | C(n,2) | C(n,2) − n = n(n−3)/2 |
| Fixed area, wall on one side | square is optimal | y = 2x is optimal |
| Regular hexagon area | (√3/4)a² | six of those: (3√3/2)a² |
| General quadrilateral area | Brahmagupta | only if cyclic; otherwise split along a diagonal |

---

## Practical exam habits

- Classify the shape before writing a formula. Half the errors here are applying a rhombus fact to a parallelogram or a cyclic fact to a general quadrilateral.
- For any polygon question about n, start from the exterior angle.
- For a hexagon, redraw it as six equilateral triangles rather than recalling its area formula.
- For a trapezium with all four sides given, drop the two perpendiculars immediately — the base splits into (a − b) plus two feet, and the rest is Pythagoras.
- When a question says "maximum" or "minimum" with a fixed area or perimeter, go straight to the symmetry principle. Don't differentiate, and check whether a side is free before assuming a square.

**Where this feeds forward:** `17-Triangles.md` (every quadrilateral is two triangles), `18-Circles.md` §4 and §7 (cyclic quadrilaterals, inscribed and circumscribed circles), `20-Mensuration.md` (cross-sections and faces of prisms), `21-Coordinate-Geometry.md` §5 (identifying these shapes from vertices), `13-Algebra.md` §6 (AM–GM behind §7).
