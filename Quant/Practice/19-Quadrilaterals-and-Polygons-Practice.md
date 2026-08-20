# Quadrilaterals & Polygons — Practice Sets

> Companion to `19-Quadrilaterals-and-Polygons.md`. Hints point to the section of the notes that contains the intended method — read the hint only after you've been stuck for a minute. Answer key with short solutions is at the bottom.
>
> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.
>
> Suggested timing: 2.0 min/question for Sets A–C, and attempt the Mixed Set in one timed block.
>
> **Classify the shape before writing a formula.** Most errors here are applying a rhombus fact to a parallelogram, or a cyclic fact to a general quadrilateral (§1).
>
> For anything asking for the number of sides, start from the exterior angle 360/n — it is several times faster than the interior-angle formula (§5).

---

## Set A — Quadrilaterals

**A1.** (TITA) A quadrilateral circumscribes a circle. Three consecutive sides measure 6, 8 and 9. Find the fourth side.

*Hint: §4 — in a tangential quadrilateral, the two pairs of opposite sides have equal sums.*

**A2.** (MCQ) The area of a rhombus with diagonals 24 and 10 is

- (a) 100
- (b) 120
- (c) 240
- (d) 260

*Hint: §2 — half the product of the diagonals. Forgetting the half is the planted error.*

**A3.** (TITA) A trapezium has parallel sides 12 and 20 and height 9. Find its area.

*Hint: §3 — ½ (sum of the parallel sides) × height.*

---

## Set B — Polygons

**B1.** (TITA) Find the number of diagonals of a decagon.

*Hint: §5 — n(n − 3)/2.*

**B2.** (MCQ) The interior angle of a regular polygon is 156°. The number of sides is

- (a) 12
- (b) 15
- (c) 18
- (d) 20

*Hint: §5 — go via the exterior angle, which is always 360/n. Much faster than the interior-angle formula.*

**B3.** (TITA) The sum of the interior angles of a polygon is 1440°. Find the number of sides.

*Hint: §5 — (n − 2) × 180.*

**B4.** (MCQ) A regular hexagon of side 6 has area

- (a) 54√3
- (b) 36√3
- (c) 72√3
- (d) 108√3

*Hint: §6 — six equilateral triangles of side 6, or (3√3/2)a².*

**B5.** (TITA) A polygon has 54 diagonals. Find the number of sides.

*Hint: §5 — solve n(n − 3)/2 = 54, or just test the options mentally.*

---

## Set C — Areas and optimisation

**C1.** (TITA) A rectangle has perimeter 40. Find its maximum possible area.

*Hint: §7 — for a fixed perimeter, the square maximises the area.*

**C2.** (MCQ) A rectangular field of area 400 m² is to be fenced. The least length of fence needed is

- (a) 70 m
- (b) 80 m
- (c) 90 m
- (d) 100 m

*Hint: §7 — the dual statement: for a fixed area, the square minimises the perimeter.*

**C3.** (TITA) A rectangular plot is fenced on three sides only (a wall forms the fourth) using 60 m of fencing. Find the maximum area (in m²).

*Hint: §7, the wall variant — the square is no longer optimal. Write A = x(60 − 2x) and use the vertex.*

---

## Mixed Set — exam feel (4 minutes)

**M1.** (TITA) The diagonal of a square is 10√2. Find its area.

**M2.** (MCQ) The number of sides of a regular polygon whose exterior angle is 20° is

- (a) 15
- (b) 16
- (c) 18
- (d) 20

---

# Answer key

## Set A

**A1 — 7.** a + c = b + d ⟹ 6 + 9 = 8 + d ⟹ d = **7**.

**A2 — (b) 120.** ½ × 24 × 10 = **120**.

**A3 — 144.** ½ × 32 × 9 = **144**.

## Set B

**B1 — 35.** 10 × 7/2 = **35**.

**B2 — (b) 15.** Exterior = 180 − 156 = 24° ⟹ n = 360/24 = **15**.

**B3 — 10.** (n − 2)180 = 1440 ⟹ n = **10**.

**B4 — (a) 54√3.** 6 × (√3/4)(36) = **54√3** ≈ 93.5.

**B5 — 12.** n² − 3n − 108 = 0 ⟹ n = **12**.

## Set C

**C1 — 100.** A 10 × 10 square gives **100**.

**C2 — (b) 80 m.** A 20 × 20 square ⟹ perimeter = **80 m**.

**C3 — 450.** 2x + y = 60 ⟹ A = x(60 − 2x), maximal at x = 15 ⟹ y = 30 ⟹ A = **450 m²**. (The square 15 × 15 would give only 225.)

## Mixed Set

**M1 — 100.** a = 10 ⟹ area = **100**.

**M2 — (c) 18.** 360/20 = **18**.

---

**Common error audit** — if you got a question wrong, find it here before moving on:

| Question | The error it is designed to catch |
|---|---|
| A1 | forgetting the equal-sums property of a tangential quadrilateral, a + c = b + d (§4) |
| A2, A3 | dropping the ½ in the rhombus or trapezium area formula (§2, §3) |
| C1, C2, C3 | assuming the square is optimal even when one side is free — the wall variant has a 2 : 1 shape (§7) |
| B2, B3, M2 | using the interior-angle formula where the exterior angle 360/n is far quicker (§5) |
| B1, B5 | misremembering the diagonal count as n(n − 1)/2, which counts all the sides too (§5) |
| B4 | recalling the hexagon area formula instead of splitting it into six equilateral triangles (§6) |
| M1 | confusing a square's side with its diagonal — area is ½d² (§2) |
