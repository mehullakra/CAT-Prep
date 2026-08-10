# Geometry & Mensuration

> CAT quant. Formula recall matters less than **drawing the figure and marking what's equal**. Most hard questions are easy once the right pair of equal lengths or equal angles is marked.

---

## 1. How to approach any geometry question

1. **Draw it, roughly to scale.** A badly drawn figure invents relationships that aren't there; a roughly accurate one lets you eliminate options by eye.
2. **Mark every equal length and equal angle** the question implies — tangents from a point, radii, folded segments, isosceles triangles.
3. **Name the unknown you actually want**, then look for a triangle containing it.
4. **Pythagoras, similarity, or an area equation** closes almost every problem. Try them in that order.

---

## 2. Triangles — the essential set

- **Angle sum** 180°; exterior angle = sum of the two remote interior angles
- **Triangle inequality:** |b − c| < a < b + c
- **Area:** ½·base·height = ½ab·sinC = √(s(s−a)(s−b)(s−c)) (Heron) = abc/4R = r·s
- **Pythagorean triples to recognise instantly:** 3-4-5, 5-12-13, 8-15-17, 7-24-25, 9-40-41, 20-21-29 (and all multiples)
- **Similarity:** AA is enough. Sides in ratio k ⟹ areas in ratio k².
- **Median** divides a triangle into two equal areas. The three medians meet at the centroid, which divides each in **2 : 1** from the vertex.
- **Angle bisector theorem:** the bisector from A meets BC at D with BD/DC = AB/AC.
- **Midpoint theorem:** the segment joining midpoints of two sides is parallel to the third and half its length.

**Special right triangles:** 45-45-90 has sides 1 : 1 : √2. 30-60-90 has 1 : √3 : 2.

**Centres:**

| Centre | Definition | Key fact |
|---|---|---|
| Centroid | medians | divides median 2:1 |
| Incentre | angle bisectors | r = Area/s |
| Circumcentre | perpendicular bisectors | R = abc/(4·Area) |
| Orthocentre | altitudes | in a right triangle, it's the right-angle vertex |

For a right triangle: **r = (a + b − c)/2** where c is the hypotenuse, and **R = c/2** (the circumcentre is the midpoint of the hypotenuse). Both are worth memorising — they turn several CAT questions into one line.

---

## 3. Type 1 — Folding and crease problems

A fold is a **reflection**. That single sentence solves the whole family.

**What a fold guarantees:**
- The crease is the **perpendicular bisector** of the segment joining a point to its image.
- **Lengths are preserved:** if vertex A folds onto point A′, then for any point P on the crease, PA = PA′.
- The folded-over region is congruent to its original.

**Method:**
1. Mark the image point and the crease.
2. Write the "preserved length" equation: the part of the side that moves keeps its length.
3. That gives one equation in one unknown — usually solved by Pythagoras.

**Worked example:** A rectangle 8 × 6 (AB = 8, BC = 6) is folded so that vertex B lands on D. Find the length of the crease.

- Fold takes B → D, so the crease is the perpendicular bisector of BD.
- BD = diagonal = √(64 + 36) = 10, so the crease passes through the centre of the rectangle, perpendicular to BD.
- The crease is a segment of the perpendicular bisector cut off by the rectangle's sides; by similar triangles its length = BD × (shorter side / longer side) reasoning gives crease = **7.5**.
  - Concretely: place B(8,0), D(0,6). Midpoint (4,3). BD slope = −3/4 ⟹ crease slope = 4/3, line y − 3 = (4/3)(x − 4). It meets AB (y = 0) at x = 4 − 9/4 = 7/4 and CD (y = 6) at x = 4 + 9/4 = 25/4. Length = √((25/4 − 7/4)² + 36) = √(20.25 + 36) = √56.25 = **7.5**

**Worked example (perimeter after fold):** An equilateral triangle of side 12 is folded so that one vertex lands on the midpoint of the opposite side. Find the perimeter of the resulting figure.

- Let the triangle be ABC, A folded onto M, the midpoint of BC (BM = MC = 6).
- The crease meets AB at P and AC at Q, with PA = PM and QA = QM (reflection preserves distance).
- On side AB: let BP = x, so PA = PM = 12 − x. In triangle PBM, angle B = 60°, PB = x, BM = 6:
  PM² = x² + 36 − 2·x·6·cos60° = x² + 36 − 6x
  (12 − x)² = x² + 36 − 6x ⟹ 144 − 24x = 36 − 6x ⟹ 18x = 108 ⟹ x = 6
- By symmetry BP = CQ = 6, PM = QM = 6.
- The resulting figure (quadrilateral BPQC with the flap folded down onto it) has boundary BP + PQ + QC + CB. With x = 6, P and Q are the midpoints of AB and AC, so PQ = 6.
- Perimeter = 6 + 6 + 6 + 12 = **30**

**The habit:** always write PA = PM (or the equivalent). Every folding question hinges on that equality, not on any special formula.

---

## 4. Circles — the essential set

- **Circumference** 2πr, **Area** πr²
- **Arc length** = (θ/360)·2πr; **Sector area** = (θ/360)·πr²
- **Angle at centre = 2 × angle at circumference** on the same arc
- **Angle in a semicircle = 90°**
- **Angles in the same segment are equal**
- **Perpendicular from the centre bisects the chord**
- **Equal chords are equidistant from the centre**

### Tangents

- A tangent is **perpendicular to the radius** at the point of contact.
- **Two tangents from an external point are equal**, and the line to the centre bisects the angle between them.
- **Tangent–secant (power of a point):** PT² = PA · PB
- **Two chords intersecting inside:** PA · PB = PC · PD
- **Tangent–chord angle (alternate segment theorem):** the angle between a tangent and a chord equals the inscribed angle in the alternate segment.

The alternate segment theorem is the one students forget and CAT loves. Whenever a figure shows a tangent touching a circle with a chord drawn from the point of contact, mark that equal angle immediately — it usually unlocks the whole diagram.

**Worked example:** TA is a tangent at A, and AB is a chord. If ∠TAB = 50°, find the inscribed angle ∠ACB in the alternate segment.
- By the alternate segment theorem, ∠ACB = **50°**.

**Direct and transverse common tangents** between circles of radii r₁, r₂ with centre distance d:
- Direct (external) tangent length = √(d² − (r₁ − r₂)²)
- Transverse (internal) tangent length = √(d² − (r₁ + r₂)²)

### Cyclic quadrilaterals

A quadrilateral is **cyclic** (all four vertices on one circle) ⟺ opposite angles sum to **180°**.

- **Area (Brahmagupta):** √((s−a)(s−b)(s−c)(s−d)) where s = (a+b+c+d)/2
- **Ptolemy:** for a cyclic quadrilateral, d₁·d₂ = ac + bd (product of diagonals = sum of products of opposite sides)
- Exterior angle = interior opposite angle

**Worked example:** A cyclic quadrilateral has sides 3, 4, 5, 6. Find its area.
- s = 18/2 = 9
- Area = √((9−3)(9−4)(9−5)(9−6)) = √(6·5·4·3) = √360 = **6√10 ≈ 18.97**

Brahmagupta reduces to Heron when one side is 0 — a good memory hook. It gives the **maximum** possible area for a quadrilateral with those four sides, which is itself a commonly asked fact.

---

## 5. Type 2 — Tangential (circumscribing) quadrilaterals, incircle radius

A quadrilateral has an **incircle** (all four sides tangent to one circle) ⟺ **a + c = b + d** (Pitot theorem — sums of opposite sides are equal).

For any such tangential polygon: **Area = r × s**, where s is the semi-perimeter. So

**r = Area / s**

That one relation answers nearly every "find the inradius" question — the work is in computing the area.

### Kite circumscribing a circle

A kite has two pairs of adjacent equal sides: a, a, b, b. Pitot gives a + b = a + b, automatically true, so **every kite has an incircle**.

- Diagonals of a kite are **perpendicular**; the long diagonal bisects the short one and both vertex angles it passes through.
- **Area = ½ · d₁ · d₂**
- Semi-perimeter s = a + b
- Therefore **r = (½·d₁·d₂)/(a + b)**

**Worked example:** Sides 13, 13, 20, 20, with the short diagonal 24.
- Half the short diagonal = 12. For the side-13 pair: the distance from that vertex to the intersection = √(169 − 144) = 5. For the side-20 pair: √(400 − 144) = 16.
- Long diagonal = 5 + 16 = 21
- Area = ½ · 24 · 21 = 252; s = (13+13+20+20)/2 = 33
- r = 252/33 = **84/11 ≈ 7.64**

**The method to carry away:** get both diagonals (Pythagoras on the half-diagonal), area = ½d₁d₂, then r = Area/s. Never look for a special kite-inradius formula — there isn't a simpler one.

**Rhombus special case:** all sides a, so s = 2a and r = (½d₁d₂)/(2a) = d₁d₂/(4a).

---

## 6. Type 3 — Optimisation: fixed area, minimum perimeter

**The two governing principles:**

- For a **fixed perimeter**, the area is maximised by the most symmetric shape (square among rectangles, circle among all shapes).
- For a **fixed area**, the perimeter is minimised by the same symmetric shape.

These are just AM–GM (`Means-and-Weighted-Averages.md` §8) in geometric clothing.

**Plain case:** rectangle of area A. Perimeter = 2(x + A/x), minimised when x = A/x ⟹ x = √A ⟹ **a square**, perimeter 4√A.

### The wall variant (one side free)

This is the version CAT actually asks, and the answer is **not** a square.

**Setup:** a rectangular plot against a straight wall; fencing is needed on three sides only. Let the side parallel to the wall be y and the two perpendicular sides be x each. Area A = xy is fixed. Fence F = 2x + y.

- F = 2x + A/x. By AM–GM, 2x + A/x ≥ 2√(2A), with equality when 2x = A/x ⟹ x = √(A/2), y = 2x.
- **Result: the side parallel to the wall is twice each perpendicular side.** Minimum fencing = 2√(2A).

**Worked example:** Minimum fencing to enclose 1,800 m² against a wall on one side.
- x = √(1800/2) = 30, y = 60
- Fence = 2(30) + 60 = **120 m** (check: 2√(2·1800) = 2√3600 = 120 ✓)

**The mirror case (fixed fence, maximum area):** with F metres of fence against a wall, area is maximised when y = F/2 and x = F/4, giving A = F²/8. Same condition, read the other way.

**General rule to remember:** at the optimum, **the total length spent on each direction is equal**. Two sides of x and one of y ⟹ 2x = y. Three parallel dividers plus two ends ⟹ same balancing logic. This generalises to plots subdivided by internal fences, which is the harder CAT variant.

---

## 7. Mensuration — solids

| Solid | Volume | Surface area |
|---|---|---|
| Cube (a) | a³ | 6a² |
| Cuboid | lbh | 2(lb + bh + hl) |
| Cylinder | πr²h | 2πr(r + h); curved 2πrh |
| Cone | ⅓πr²h | πr(r + l); curved πrl, l = √(r²+h²) |
| Sphere | (4/3)πr³ | 4πr² |
| Hemisphere | (2/3)πr³ | 3πr² (total) |
| Prism | base area × h | perimeter × h + 2×base |
| Pyramid | ⅓ × base area × h | — |

**Scaling rule:** scale all linear dimensions by k ⟹ areas scale by k², volumes by k³. Half the CAT mensuration questions are only this.

**Cone frustum:** V = (πh/3)(R² + Rr + r²). A cone cut by a plane parallel to the base at height ratio k from the apex gives a small cone of volume k³ times the original.

**Diagonal of a cuboid** = √(l² + b² + h²); of a cube = a√3.

---

## 8. Polygons

- Sum of interior angles = (n − 2)·180°
- Each interior angle of a **regular** n-gon = (n−2)·180/n; each exterior angle = 360/n
- Number of diagonals = n(n−3)/2
- Regular hexagon of side a = 6 equilateral triangles ⟹ area = (3√3/2)a²
- Equilateral triangle of side a: area = (√3/4)a², height = (√3/2)a, r = a/(2√3), R = a/√3

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Folding | treat as a new arbitrary figure | it's a reflection — lengths are preserved |
| Similar triangles | areas scale like sides | areas scale like sides **squared** |
| Cyclic quadrilateral area | Heron with three sides | Brahmagupta with all four |
| Incircle of a quadrilateral | assume every quadrilateral has one | needs a + c = b + d |
| Fixed area, wall on one side | square is optimal | y = 2x is optimal |
| Tangent–chord angle | ignored | equals the alternate segment angle |
| Right-triangle circumradius | computed via abc/4Δ | it's just c/2 |
| Volume scaling | ×k | ×k³ |
| Triangle from three lengths | always exists | check the triangle inequality |

---

## Practical exam habits

- Draw large. A 2 cm sketch hides the relationship you need.
- Coordinate geometry is a legitimate escape hatch. If a figure has perpendiculars and midpoints (folds, rectangles, kites), placing it on axes and computing is often faster and safer than hunting for a synthetic argument — the folding example in §3 is exactly this.
- Check answers against the figure's rough scale. If your computed side is longer than the visibly longest one, something's wrong.
- Memorise the triples. Recognising 5-12-13 saves a square root every time.
- When a question says "minimum" or "maximum" with a fixed area or perimeter, go straight to AM–GM; don't differentiate.

**Where this feeds forward:** `Means-and-Weighted-Averages.md` §8 (AM–GM for the optimisation cases), `Algebra.md` (surds from Pythagoras), `Number-System.md` (Pythagorean triples as integer solutions).
