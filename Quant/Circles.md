# Circles

> CAT quant. A small, closed set of theorems that get combined rather than extended. The skill is spotting **which** of six or seven facts a figure is pointing at — and the tangent–chord angle is the one students forget and CAT loves.

Approach discipline for any plane figure lives in `Triangles.md` §1.

---

## 1. The essential set

- **Circumference** 2πr, **Area** πr²
- **Arc length** = (θ/360)·2πr
- **Sector area** = (θ/360)·πr² = ½ · (arc length) · r
- **Segment area = sector − triangle** = (θ/360)·πr² − ½r²·sin θ

That last line is the one most often missing from a formula sheet and most often needed. A **minor segment** is the region between a chord and the arc it cuts off; you get it by removing the triangle formed by the chord and the two radii.

**For the standard angles:**

| θ | Sector | Triangle to subtract | Segment |
|---|---|---|---|
| 60° | πr²/6 | (√3/4)r² | r²(π/6 − √3/4) |
| 90° | πr²/4 | r²/2 | r²(π/4 − ½) |
| 120° | πr²/3 | (√3/4)r² | r²(π/3 − √3/4) |

(At 60° and 120° the triangle is the same — an isosceles triangle with apex θ has area ½r²sin θ, and sin 60° = sin 120°.)

**Useful numbers:** π ≈ 22/7 when the radius is a multiple of 7 (CAT signals this), otherwise 3.14. A circle of radius 7 has circumference 44 and area 154.

---

## 2. Chords and angles

- **Angle at the centre = 2 × angle at the circumference** on the same arc
- **Angle in a semicircle = 90°** — the single most used circle fact in CAT, because it converts a diameter into a right triangle (`Triangles.md` §7)
- **Angles in the same segment are equal**
- **The perpendicular from the centre bisects the chord** — and conversely
- **Equal chords are equidistant from the centre**, and the longer chord is nearer the centre

**Chord length from the distance to the centre:** half-chord, distance d and radius r form a right triangle, so

**chord = 2√(r² − d²)**

**Worked example:** A chord of length 16 lies 6 cm from the centre. Find r.
- Half-chord 8, distance 6 ⟹ r = √(64 + 36) = **10** (an 6-8-10 triple)

---

## 3. Tangents

- A tangent is **perpendicular to the radius** at the point of contact
- **Two tangents from an external point are equal**, and the line to the centre bisects the angle between them
- **Tangent length** from a point at distance d from the centre = **√(d² − r²)**
- **Power of a point — tangent–secant:** PT² = PA · PB
- **Two chords intersecting inside:** PA · PB = PC · PD
- **Tangent–chord (alternate segment) theorem:** the angle between a tangent and a chord equals the inscribed angle in the alternate segment

Whenever a figure shows a tangent touching a circle with a chord drawn from the point of contact, **mark the equal angle immediately** — it usually unlocks the whole diagram.

**Worked example:** From a point 13 cm from the centre of a circle of radius 5, find the tangent length.
- √(169 − 25) = √144 = **12** (5-12-13)

**Note the unification:** the tangent case, the two-secant case and the two-chord case are one statement — the *power of the point*, equal to |d² − r²|. Positive outside, negative inside. Recognising them as one fact halves what you have to remember.

---

## 4. Cyclic quadrilaterals

A quadrilateral is **cyclic** ⟺ **opposite angles sum to 180°**. Also: the exterior angle equals the interior opposite angle.

- **Area (Brahmagupta):** √((s−a)(s−b)(s−c)(s−d)), s = (a+b+c+d)/2
- **Ptolemy:** d₁·d₂ = ac + bd — the product of the diagonals equals the sum of the products of opposite sides

Brahmagupta reduces to Heron when one side is 0, which is a good memory hook. It also gives the **maximum** possible area for any quadrilateral with those four sides — itself a commonly asked fact.

**Worked example:** A cyclic quadrilateral has sides 3, 4, 5, 6. Find its area.
- s = 9 ⟹ √(6·5·4·3) = √360 = **6√10 ≈ 18.97**

**Which quadrilaterals are always cyclic?** Rectangles and squares (opposite angles are 90° each). An isosceles trapezium is cyclic; a general parallelogram is **not**, unless it is a rectangle.

---

## 5. Type 1 — Segments, shaded regions and overlaps

**The method is always subtraction, and the whole difficulty is choosing what to subtract from what.**

1. Name the outer region (square, sector, triangle).
2. Name the pieces removed.
3. Watch for pieces removed **twice** — that's where the marks are lost.

**Worked example (classic):** A circle is inscribed in a square of side 14. Find the area between them.
- Square 196; circle radius 7 ⟹ area 154 ⟹ difference = **42**

**Worked example (leaf/petal):** Two quarter-circles of radius a are drawn inside a square of side a, centred at opposite corners. Find the area common to both.
- Each quarter-circle has area πa²/4; together they cover πa²/2, but the square is only a², so the double-counted overlap is πa²/2 − a² = **a²(π/2 − 1)**
- This "sum of the parts minus the container" move is inclusion–exclusion (`Set-Theory-Venn.md` §2) applied to areas, and it is far faster than integrating or splitting into segments.

**Worked example (segment):** A chord subtends 90° at the centre of a circle of radius 10. Find the minor segment's area.
- Sector = ¼ · 100π = 25π; triangle = ½ · 10 · 10 = 50
- Segment = **25π − 50 ≈ 28.5**

---

## 6. Type 2 — Two circles

For circles of radii r₁, r₂ with centre distance d:

| Configuration | Condition |
|---|---|
| One inside the other, no touching | d < \|r₁ − r₂\| |
| Touching **internally** | d = \|r₁ − r₂\| |
| Intersecting at two points | \|r₁ − r₂\| < d < r₁ + r₂ |
| Touching **externally** | **d = r₁ + r₂** |
| Separate | d > r₁ + r₂ |

- **Direct (external) common tangent length** = √(d² − (r₁ − r₂)²) — there are 2 of these when the circles don't contain one another
- **Transverse (internal) common tangent length** = √(d² − (r₁ + r₂)²) — 2 of these, and only when the circles are separate
- **Number of common tangents:** 4 if separate, 3 if touching externally, 2 if intersecting, 1 if touching internally, 0 if one is inside the other

**Common chord of two intersecting circles:** the line of centres is the **perpendicular bisector** of the common chord. Drop that perpendicular and you get two right triangles sharing the half-chord — solve for it from r₁² − x² = r₂² − (d − x)².

**Worked example:** Two circles of radii 5 and 3 touch externally. Find the centre distance.
- Externally ⟹ d = 5 + 3 = **8** (the decoy is 5 − 3 = 2, which is the *internal* case)

---

## 7. Type 3 — Circles inscribed in and circumscribing figures

| Figure | Inradius | Circumradius |
|---|---|---|
| Square of side a | a/2 | a/√2 |
| Equilateral triangle, side a | a/(2√3) | a/√3 |
| Regular hexagon, side a | a√3/2 | a |
| Any triangle | Area/s | abc/(4·Area) |
| Right triangle, legs a,b, hyp c | (a + b − c)/2 | c/2 |

For a general regular n-gon the formulas live in `Quadrilaterals-and-Polygons.md` §6.

**Circles packed in a square:** n² equal circles in an n × n grid inside a square of side a each have radius a/(2n), and the total circle area is πa²/4 **regardless of n** — a favourite CAT observation, since the packing fraction never changes.

**Three mutually touching circles** of radii r₁, r₂, r₃ have centres forming a triangle with sides r₁+r₂, r₂+r₃, r₃+r₁. Almost every "three touching circles" question is that one sentence plus Heron.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Segment area | sector area | sector **minus** the triangle |
| Externally touching circles | d = r₁ − r₂ | d = r₁ + r₂ |
| Common tangent length | one formula for both | direct uses (r₁ − r₂), transverse uses (r₁ + r₂) |
| Tangent–chord angle | ignored | equals the alternate segment angle |
| Cyclic quadrilateral area | Heron with three sides | Brahmagupta with all four |
| Parallelogram assumed cyclic | yes | only if it's a rectangle |
| Overlapping shaded regions | subtract each piece once | a doubly-covered piece must be added back |
| Chord and radius | chord = √(r² − d²) | chord = **2**√(r² − d²) |
| π = 22/7 | used always | only when the radius is a multiple of 7 |
| Angle at centre | equals the inscribed angle | it is **twice** it |

---

## Practical exam habits

- The instant you see a **diameter**, look for the right angle it creates. That single reflex solves a large share of circle questions.
- The instant you see a **tangent with a chord**, mark the alternate segment angle before reading further.
- Join the centre to everything — radii are free equal lengths, and most figures open up once three or four are drawn.
- For shaded regions, write the subtraction as an explicit expression before computing any number. Most errors here are bookkeeping, not arithmetic.
- If the radius is a multiple of 7, the setter intends π = 22/7 and the answer will be clean. If it isn't, expect the answer to stay in terms of π.

**Where this feeds forward:** `Triangles.md` §7 (angle in a semicircle → altitude on the hypotenuse), `Quadrilaterals-and-Polygons.md` §4 (tangential quadrilaterals, Pitot), `Coordinate-Geometry.md` §7 (circle equations and tangency by distance), `Mensuration.md` (every cross-section of a sphere, cone or cylinder is a circle).
