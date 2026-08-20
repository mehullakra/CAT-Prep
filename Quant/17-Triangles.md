# Triangles

> CAT quant. The centre of gravity of the whole geometry section — circles, quadrilaterals and solids all reduce to triangles once you draw the right line. Formula recall matters less than **drawing the figure and marking what's equal**.

---

## 1. How to approach a plane-geometry question

This applies to `18-Circles.md` and `19-Quadrilaterals-and-Polygons.md` too; it is stated once, here.

1. **Draw it, roughly to scale.** A badly drawn figure invents relationships that aren't there; a roughly accurate one lets you eliminate options by eye.
2. **Mark every equal length and equal angle** the question implies — tangents from a point, radii, folded segments, isosceles triangles.
3. **Name the unknown you actually want**, then look for a triangle containing it.
4. **Pythagoras, similarity, or an area equation** closes almost every problem. Try them in that order.
5. If a figure is given, **do not trust it**. CAT figures are schematic; a right angle or an equal length must be stated, not eyeballed.

When perpendiculars, midpoints and a fixed axis all appear at once, stop and consider `21-Coordinate-Geometry.md` §1 — computing beats hunting for a synthetic argument more often than people expect.

---

## 2. Lines and angles

- Angles on a straight line sum to 180°; angles round a point sum to 360°
- **Vertically opposite angles are equal**
- A transversal across parallel lines: **corresponding** and **alternate** angles equal, **co-interior** (allied) angles supplementary
- The converse holds — equal alternate angles *prove* the lines parallel, which is how many CAT figures are unlocked

**The construction that solves most angle-chase questions:** if a figure has two parallel lines and a bent path between them, **draw a line through the bend parallel to both**. The bend angle splits into two alternate angles and the question collapses.

---

## 3. Triangles — the essential set

- **Angle sum** 180°; **exterior angle** = sum of the two remote interior angles
- **Triangle inequality:** |b − c| < a < b + c
- **Area:** ½·base·height = ½ab·sin C = √(s(s−a)(s−b)(s−c)) (Heron) = abc/4R = r·s
- **Pythagorean triples to recognise instantly:** 3-4-5, 5-12-13, 8-15-17, 7-24-25, 9-40-41, 20-21-29, and all multiples
- **13-14-15** has area 84 — not a triple, but CAT's favourite Heron triangle. Memorise it.
- **Special right triangles:** 45-45-90 is 1 : 1 : √2; 30-60-90 is 1 : √3 : 2
- **Equilateral of side a:** area (√3/4)a², height (√3/2)a, r = a/(2√3), R = a/√3

**Classifying by the largest side c:** c² < a² + b² acute, = right, > obtuse. One line, and it settles every "is this triangle obtuse" sub-question.

---

## 4. Similarity, congruence and area ratios

**Congruence:** SSS, SAS, ASA, AAS, RHS. **Similarity: AA is enough** — never look for more.

- Sides in ratio k ⟹ **perimeters in ratio k, areas in ratio k²**
- Read backwards: areas in ratio 9 : 16 ⟹ sides and perimeters in ratio **3 : 4**

**Basic proportionality (Thales/BPT):** a line parallel to one side cuts the other two **proportionally**. In △ABC with DE ∥ BC, AD/DB = AE/EC, and △ADE ~ △ABC.

**Worked example:** DE ∥ BC with AD : DB = 2 : 3. Find area(ADE) : area(ABCDE region) and : area(ABC).
- AD : AB = 2 : 5, so the similarity ratio is 2/5 and **area(ADE) : area(ABC) = 4 : 25**
- The trapezium DBCE therefore takes the remaining **21**, so ADE : DBCE = 4 : 21

**The same-height rule — the workhorse of this whole topic:**

**Two triangles with the same height have areas in the ratio of their bases.**

So a median splits a triangle into two equal areas; a point dividing BC in 2 : 1 splits the area in 2 : 1; and any cevian's area split is read straight off the base split, with no heights ever computed. Nearly every "find the area of this shaded sub-triangle" question is this sentence applied twice.

**The companion rule:** two triangles sharing the *same base* have areas in the ratio of their heights — so all triangles on one base with their apex on a line parallel to it are **equal in area**.

---

## 5. The four centres

| Centre | Defined by | Key fact |
|---|---|---|
| **Centroid** | medians | divides each median **2 : 1** from the vertex |
| **Incentre** | angle bisectors | **r = Area/s**; always inside |
| **Circumcentre** | perpendicular bisectors | **R = abc/(4·Area)** |
| **Orthocentre** | altitudes | in a right triangle it *is* the right-angle vertex |

**For a right triangle** (c the hypotenuse): **r = (a + b − c)/2** and **R = c/2** — the circumcentre is the midpoint of the hypotenuse. Both turn several CAT questions into one line.

**Where the centre sits** depends on the triangle, and CAT tests this directly:

| | Acute | Right | Obtuse |
|---|---|---|---|
| Incentre, centroid | inside | inside | inside |
| Circumcentre | inside | midpoint of hypotenuse | **outside** |
| Orthocentre | inside | at the right angle | **outside** |

The centroid divides the triangle into **three** equal areas (joining it to the vertices) and, with all three medians drawn, into **six** equal areas.

---

## 6. Medians, bisectors and the midpoint theorem

- **Angle bisector theorem:** the bisector from A meets BC at D with **BD/DC = AB/AC**
- **Midpoint theorem:** the segment joining midpoints of two sides is parallel to the third and **half its length**
- **Median length (Apollonius):** for the median m_a to side a,

  **m_a² = (2b² + 2c² − a²)/4**

  Equivalently b² + c² = 2m_a² + a²/2. Asked directly, and also the fastest route to "the sum of the squares of the medians", which is **¾(a² + b² + c²)**.

### The medial triangle

Joining the three midpoints gives the **medial triangle**, similar with ratio ½:

- **Perimeter = ½** the original perimeter
- **Area = ¼** the original area
- It cuts the original into 4 congruent triangles

The perimeter fact is the shortcut — you never need the medial triangle's individual sides.

---

## 7. Type 1 — Altitudes: outside the base, and on the hypotenuse

### The altitude of an obtuse triangle falls outside

In an obtuse triangle the foot of the altitude from a vertex lands on the **extension** of the opposite side. The question signals it with a collinearity order like "LX is an altitude with **X–M–N**": X is the foot, sitting *beyond* M, outside segment MN.

- **Area = ½ × MN × LX still holds.** The base is the actual side MN; the height is the full perpendicular LX. Do **not** use XN as the base.
- Both right triangles LXM and LXN are valid: LM² = LX² + XM², LN² = LX² + XN².
- The letter order fixes the sign. **X–M–N ⟹ XN = XM + MN**; with M–X–N you subtract instead.

**Worked example:** ∠M is obtuse, LX is an altitude of length 16 with X–M–N, LN = 20, area = 48. Find the perimeter of the medial triangle of △LMN.
- 48 = ½ × MN × 16 ⟹ **MN = 6**
- XN = √(400 − 256) = **12**; X–M–N ⟹ XM = 12 − 6 = **6**
- LM = √(256 + 36) = √292 = **2√73**
- Perimeter of LMN = 26 + 2√73 ⟹ medial perimeter = **13 + √73**
- Obtuse check: 292 + 36 = 328 < 400 ✓

### The altitude on the hypotenuse — three geometric means

Right angle at C, altitude CD onto hypotenuse AB. Equivalently, and this is CAT's usual disguise: **AB is a diameter, C is on the circle** (`18-Circles.md` §2) **and CD ⊥ AB**.

Triangles ACD, CBD and ABC are **all similar**, giving:

- **CD² = AD · DB** — the altitude is the geometric mean of the two segments
- **AC² = AD · AB** and **BC² = DB · AB** — each leg is the geometric mean of its adjacent segment and the whole hypotenuse

**Worked example:** AB is a diameter, C on the circle, CD ⊥ AB, AD = 8, DB = 12. Find area(ABC).
- ∠ACB = 90°, so CD² = 8 × 12 = 96 ⟹ CD = **4√6**; AB = **20**
- Area = ½ × 20 × 4√6 = **40√6**
- (Legs check: AC = √160 = 4√10, BC = √240 = 4√15, ½·4√10·4√15 = 40√6 ✓)

The altitude on the hypotenuse also gives **1/h² = 1/a² + 1/b²**, occasionally the quickest form.

---

## 8. Type 2 — Splitting area with cevians

**The method, in full:** apply the same-height rule (§4) repeatedly, working from the whole triangle inwards. Never compute an actual area until the last step.

**Worked example:** In △ABC, D on BC with BD : DC = 1 : 2, and E on AD with AE : ED = 3 : 1. If area(ABC) = 60, find area(BEC).
- △ABD : △ADC = 1 : 2 (same height from A) ⟹ areas 20 and 40
- Split the target: △BEC = △BED + △DEC, and both have their base on segment ED
- △BED : △BAD = ED : AD = 1 : 4 ⟹ △BED = 20/4 = 5; likewise △DEC = 40/4 = 10
- area(BEC) = **15**

**The general shape:** a ratio on a side transfers to the areas directly; a ratio on a cevian transfers to the areas of the two sub-triangles hanging off it. Chain the two and you never need a height.

**Worth knowing:** the three medians divide the triangle into 6 equal parts (§5); a cevian through the centroid does **not** in general.

---

## 9. Sine rule and cosine rule

**Sine rule:** a/sin A = b/sin B = c/sin C = **2R**

That "= 2R" tail is the part people forget and CAT uses — it converts an angle-and-side into the circumradius in one step.

**Cosine rule:** **c² = a² + b² − 2ab·cos C**, rearranged as cos C = (a² + b² − c²)/(2ab)

Pythagoras is the C = 90° case. The rearranged form is how you decide whether an angle is obtuse without knowing it: the numerator's sign *is* the answer (§3).

**Values worth having cold:** sin/cos of 30°, 45°, 60° as ½, 1/√2, √3/2 (and the reverse for cos); tan 30° = 1/√3, tan 45° = 1, tan 60° = √3.

**Worked example:** Two sides are 5 and 8 with the included angle 60°. Find the third side.
- c² = 25 + 64 − 2(5)(8)(½) = 89 − 40 = 49 ⟹ c = **7**

---

## 9a. Trigonometric identities, and maxima of a·sin x + b·cos x

§9 solves triangles. This is the small amount of pure trigonometry CAT asks outside a triangle.

**The three Pythagorean identities:**

- sin²θ + cos²θ = 1
- 1 + tan²θ = sec²θ
- 1 + cot²θ = cosec²θ

**Compound and double angles** (the ones that actually appear):

- sin(A ± B) = sin A cos B ± cos A sin B
- cos(A ± B) = cos A cos B ∓ sin A sin B
- **sin 2A = 2 sin A cos A**; cos 2A = 1 − 2sin²A = 2cos²A − 1
- tan(A + B) = (tan A + tan B)/(1 − tan A tan B)

**Signs by quadrant — "ASTC":** **A**ll positive in the first, **S**ine in the second, **T**angent in the third, **C**osine in the fourth.

### The maximum and minimum of a·sin x + b·cos x

**Range = [−√(a² + b²), +√(a² + b²)]**

Why: write a sin x + b cos x = √(a²+b²) · sin(x + φ), where φ has tan φ = b/a. The bracket is a single sine, so it swings between −1 and 1.

**Worked example:** Find the maximum of 3 sin x + 4 cos x.
- √(9 + 16) = **5**, minimum −5. The 3-4-5 triple is not a coincidence — setters choose a and b so the root is clean.

**The related maxima worth knowing:**

| Expression | Maximum | Minimum |
|---|---|---|
| sin x · cos x = ½ sin 2x | **½** | −½ |
| sin⁴x + cos⁴x = 1 − ½sin²2x | 1 | **½** |
| sin²x + cosec²x (and the cos/sec pair) | unbounded | **2** (AM–GM, `13-Algebra.md` §6) |
| a sin x + b cos x | √(a²+b²) | −√(a²+b²) |

**Traps:**
- Taking the maximum of a sin x + b cos x as a + b. That would need both to peak at the same x, which they never do.
- Reading sin⁴ + cos⁴ as 1. Only sin² + cos² is 1; the fourth powers range over [½, 1].
- Assuming sin²x + cosec²x can be small. Its minimum is 2, not 0 — reciprocals under AM–GM.

---

## 10. Type 3 — Heights and distances

Angle of **elevation** is measured up from the horizontal; angle of **depression** is measured down from the horizontal at the observer — and it equals the elevation from the other end (alternate angles, §2). Confusing which is which is the entire difficulty of most of these.

**Method:** draw the vertical, mark the horizontal, and write **tan θ = opposite/adjacent** for each position. Two positions give two equations in the height and one horizontal distance.

**Worked example:** The angle of elevation of a tower's top is 30° from a point, and 60° from a point 40 m nearer. Find the height.
- h/x = tan 60° = √3 and h/(x + 40) = tan 30° = 1/√3
- From the first, x = h/√3. Substituting: h√3 = x + 40 = h/√3 + 40 ⟹ h(√3 − 1/√3) = 40 ⟹ h(2/√3) = 40
- **h = 20√3 ≈ 34.6 m**

**The two shortcuts worth memorising:** if the elevation goes from 30° to 60°, the observer has covered **two-thirds** of the total horizontal distance; if from 45° to 60°, the height is always d·(√3 + 3)/2 for a walk of d. Deriving them takes longer than remembering the first one.

---

## 11. Type 4 — Folding and creases

A fold is a **reflection**. That single sentence solves the whole family.

- The crease is the **perpendicular bisector** of the segment joining a point to its image.
- **Lengths are preserved:** if A folds onto A′, then PA = PA′ for every P on the crease.
- The folded region is congruent to its original.

**Method:** mark the image point and the crease, write the preserved-length equation (the part of the side that moves keeps its length), and close with Pythagoras or the cosine rule.

**Worked example:** An equilateral triangle of side 12 is folded so one vertex lands on the midpoint of the opposite side. Find the perimeter of the resulting figure.
- A folds onto M, the midpoint of BC (BM = MC = 6). The crease meets AB at P and AC at Q, with PA = PM and QA = QM.
- Let BP = x, so PA = PM = 12 − x. In △PBM, ∠B = 60°: PM² = x² + 36 − 6x
- (12 − x)² = x² + 36 − 6x ⟹ 144 − 24x = 36 − 6x ⟹ x = 6
- So P and Q are the midpoints, PQ = 6, and the perimeter = 6 + 6 + 6 + 12 = **30**

**For a rectangle fold, coordinates are usually faster** than a synthetic argument — see `21-Coordinate-Geometry.md` §8, which owns the reflection formulas.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Reading the given figure | trust the drawing | only stated equalities count; CAT figures aren't to scale |
| Similar triangles | areas scale like sides | areas scale like sides **squared** |
| Areas 9 : 16 → perimeters | 9 : 16 | 3 : 4 — take the square root |
| Altitude in an obtuse triangle | foot lies on the side | it falls outside; the base is still the side |
| Altitude on the hypotenuse | AD, DB are the legs | they are hypotenuse pieces; CD² = AD·DB |
| Circumcentre location | always inside | outside for obtuse; hypotenuse midpoint for right |
| Medial triangle | perimeter ¼, area ½ | perimeter ½, area ¼ |
| Right-triangle circumradius | computed via abc/4Δ | it's just c/2 |
| Cevian area split | compute both heights | same height ⟹ area ratio = base ratio |
| Sine rule | a/sin A = b/sin B only | it also equals **2R** |
| Angle of depression | measured from the vertical | from the **horizontal** at the observer |
| Folding | a new arbitrary figure | it's a reflection — lengths are preserved |
| Triangle from three lengths | always exists | check the triangle inequality |

---

## Practical exam habits

- Draw large. A 2 cm sketch hides the relationship you need.
- Memorise the triples and 13-14-15. Recognition saves a square root every time.
- Before reaching for Heron, check whether the triangle is right — half of CAT's "three sides given" questions are triples in disguise.
- For any area-splitting question, say "same height" out loud before writing anything. It is the intended method roughly always.
- Coordinate geometry is a legitimate escape hatch for folds, midpoints and perpendiculars.
- Check your answer against the figure's rough scale. A side longer than the visibly longest one means something is wrong.

**Where this feeds forward:** `18-Circles.md` (inscribed triangles, the angle in a semicircle), `19-Quadrilaterals-and-Polygons.md` (every polygon is triangles), `20-Mensuration.md` (cross-sections of cones and pyramids), `21-Coordinate-Geometry.md` §6 (shoelace area), `13-Algebra.md` §6 (AM–GM behind the optimisation cases).
