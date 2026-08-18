# Triangles — Practice Sets

> Companion to `Triangles.md`. Hints point to the section of the notes that contains the intended method — read the hint only after you've been stuck for a minute. Answer key with short solutions is at the bottom.
>
> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.
>
> Suggested timing: 2.0 min/question for Sets A–A, and attempt the Mixed Set in one timed block.
>
> **Draw it, then label every known length and angle on the figure.** Most geometry errors are bookkeeping errors, not reasoning errors (§1).
>
> Learn the Pythagorean triples cold — 3-4-5, 5-12-13, 7-24-25, 8-15-17, 9-40-41 — and that 13-14-15 has area 84. CAT picks its numbers from that list (§3).

---

## Set A — Triangles

**A1.** (TITA) The sides of a triangle are 13, 14 and 15. Find its area.

*Hint: §3 — Heron's formula with s = 21. This particular triangle appears constantly in CAT; memorise that its area is 84.*

**A2.** (MCQ) In a right triangle the legs are 9 and 12. The altitude to the hypotenuse is

- (a) 6
- (b) 7.2
- (c) 7.5
- (d) 8

*Hint: §7 — the area computed two ways: ½(9)(12) = ½(hypotenuse)(altitude).*

**A3.** (TITA) An equilateral triangle has area 36√3. Find its side.

*Hint: §3 — area = (√3/4)a². The √3 cancels, which is why the numbers look ugly but aren't.*

**A4.** (MCQ) In triangle ABC, D is the midpoint of BC and the area of ABC is 48. The area of ABD is

- (a) 12
- (b) 16
- (c) 24
- (d) 32

*Hint: §4 — a median splits a triangle into two of equal area, regardless of shape.*

**A5.** (TITA) Two similar triangles have areas in the ratio 9 : 16. If the smaller has perimeter 45, find the perimeter of the larger.

*Hint: §4 — areas scale as the square of the linear ratio, so take square roots before scaling a length.*

**A6.** (MCQ) The sides of a triangle are 7, 24 and 25. Its inradius is

- (a) 2
- (b) 3
- (c) 3.5
- (d) 4

*Hint: §5 — this is a right triangle, and for a right triangle r = (a + b − c)/2.*

---

## Mixed Set — exam feel (5 minutes)

**M1.** (TITA) Find the area of a triangle with sides 9, 12 and 15.

**M2.** (TITA) In a right triangle, the hypotenuse is 26 and one leg is 10. Find the area.

**M3.** (MCQ) In triangle ABC, DE is parallel to BC with AD : DB = 2 : 3. The ratio of the area of ADE to that of ABC is

- (a) 2 : 5
- (b) 4 : 25
- (c) 4 : 9
- (d) 2 : 3

---

# Answer key

## Set A

**A1 — 84.** s = 21 ⟹ √(21 × 8 × 7 × 6) = √7056 = **84**.

**A2 — (b) 7.2.** Hypotenuse = 15 (a 3-4-5 triple scaled by 3) ⟹ altitude = 9 × 12/15 = **7.2**.

**A3 — 12.** (√3/4)a² = 36√3 ⟹ a² = 144 ⟹ a = **12**.

**A4 — (c) 24.** A median bisects the area ⟹ **24**.

**A5 — 60.** Linear ratio = 3 : 4 ⟹ perimeter = 45 × 4/3 = **60**. (Scaling by 16/9 gives 80 — the planted error.)

**A6 — (b) 3.** 7² + 24² = 25² ⟹ right angled ⟹ r = (7 + 24 − 25)/2 = **3**. (Check with r = Area/s = 84/18 … careful: s = 28, Area = 84 ⟹ r = 3 ✓)

## Mixed Set

**M1 — 54.** 9-12-15 is 3-4-5 tripled ⟹ right angled ⟹ ½(9)(12) = **54**.

**M2 — 120.** The other leg is 24 ⟹ area = ½(10)(24) = **120**.

**M3 — (b) 4 : 25.** AD : AB = 2 : 5 ⟹ area ratio = **4 : 25**. (4 : 9 uses AD : DB — the planted error.)

---

**Common error audit** — if you got a question wrong, find it here before moving on:

| Question | The error it is designed to catch |
|---|---|
| A2, A6, M1, M2 | grinding through Heron or algebra where a Pythagorean triple was staring at you (§3) |
| A5, M3 | scaling a length by the area ratio instead of by its square root — areas go as k², so take the root first (§4) |
| A4 | computing heights instead of using the same-height rule: a median always halves the area (§4) |
