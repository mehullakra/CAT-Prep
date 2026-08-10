# Algebra

> CAT quant. Almost never asks you to *solve* messy equations — it asks you to **recognise a form**. Identities, symmetry, and substitution do the work; brute-force algebra is the trap.

---

## 1. The identities that actually appear

| Identity | Note |
|---|---|
| (a ± b)² = a² ± 2ab + b² | |
| a² − b² = (a − b)(a + b) | the single most used line in CAT algebra |
| (a + b)³ = a³ + b³ + 3ab(a + b) | rearranged form is more useful than the expanded one |
| a³ ± b³ = (a ± b)(a² ∓ ab + b²) | |
| (a + b + c)² = a² + b² + c² + 2(ab + bc + ca) | converts between the two symmetric sums |
| **a³ + b³ + c³ − 3abc = (a+b+c)(a² + b² + c² − ab − bc − ca)** | the workhorse — see §5 |
| a² + b² = (a+b)² − 2ab | |
| a⁴ + a²b² + b⁴ = (a² + ab + b²)(a² − ab + b²) | occasional |

**The x + 1/x family** — worth memorising as a chain, because CAT asks for the next link:

- x² + 1/x² = (x + 1/x)² − 2
- x³ + 1/x³ = (x + 1/x)³ − 3(x + 1/x)
- x⁴ + 1/x⁴ = (x² + 1/x²)² − 2
- x − 1/x: (x − 1/x)² = (x + 1/x)² − 4

**Worked example:** If x + 1/x = 3, find x³ + 1/x³.
- 3³ − 3(3) = 27 − 9 = **18**

---

## 2. Quadratics

For ax² + bx + c = 0 with roots α, β:

- **α + β = −b/a**, **αβ = c/a**
- Discriminant D = b² − 4ac: D > 0 two real roots, D = 0 equal, D < 0 complex
- α² + β² = (α+β)² − 2αβ
- 1/α + 1/β = (α+β)/αβ
- To build the equation from roots: x² − (sum)x + (product) = 0

**Vertex:** ax² + bx + c has its extremum at x = −b/2a, value (4ac − b²)/4a. Minimum if a > 0, maximum if a < 0. Use this for any "maximum value of a quadratic expression" question — never differentiate.

**Sign of a quadratic:** for a > 0, the expression is negative strictly between the roots and positive outside. Sketching the parabola settles every inequality question in two seconds.

**Common roots:** two quadratics share both roots ⟺ a₁/a₂ = b₁/b₂ = c₁/c₂.

---

## 3. Higher-degree and symmetric systems

For a cubic ax³ + bx² + cx + d with roots p, q, r:
- p + q + r = −b/a
- pq + qr + rp = c/a
- pqr = −d/a

**Recognise symmetry.** If an expression is unchanged when you swap any two variables, express it in the elementary symmetric sums (Σa, Σab, abc) and use the coefficient relations. Never solve for the individual roots.

**Worked example:** If a + b + c = 6 and ab + bc + ca = 11, find a² + b² + c².
- (a+b+c)² = Σa² + 2Σab ⟹ 36 = Σa² + 22 ⟹ **14**

---

## 4. Surds — rationalisation and equations

**Conjugate rule:** multiply by the conjugate to clear a surd from a denominator.

- 1/(√a + √b) = (√a − √b)/(a − b)
- (√a + √b)(√a − √b) = a − b

**Key structural facts:**
- √3 + √2 and √3 − √2 multiply to **1** — so each is the reciprocal of the other. Whenever a question pairs two surds whose product is 1, set t = one of them and the other is 1/t; the x + 1/x machinery of §1 then applies directly.
- If p + q√n = r + s√n with p, q, r, s rational and √n irrational, then **p = r and q = s**. Rational and irrational parts must match separately. This "compare parts" step ends many questions.

### Solving for x + y given √x ± √y forms

**Method:** square, isolate the remaining surd, square again. Track the extraneous roots.

**Worked example:** If √x + √y = 7 and √x − √y = 3, find x + y and xy.
- Add: 2√x = 10 ⟹ √x = 5 ⟹ x = 25
- Subtract: 2√y = 4 ⟹ √y = 2 ⟹ y = 4
- x + y = **29**, xy = **100**

**Worked example (single equation):** If √(x + 7) + √(x − 2) = 9, find x.
- Isolate: √(x + 7) = 9 − √(x − 2)
- Square: x + 7 = 81 − 18√(x − 2) + x − 2 ⟹ 18√(x − 2) = 72 ⟹ √(x − 2) = 4 ⟹ x = **18**
- Check: √25 + √16 = 5 + 4 = 9 ✓

**Always substitute back.** Squaring introduces roots that don't satisfy the original equation; CAT includes them among the options.

**The sum-and-difference shortcut:** if √x + √y = p and √x − √y = q, then immediately

**x + y = (p² + q²)/2** and **xy = ((p² − q²)/4)²**

Check with p = 7, q = 3: (49 + 9)/2 = 29 ✓, ((49 − 9)/4)² = 10² = 100 ✓.

**Nested surds:** √(a ± 2√b) = √m ± √n where m + n = a and mn = b. So √(7 + 2√12)? m + n = 7, mn = 12 ⟹ m, n = 4, 3 ⟹ **2 + √3**.

---

## 5. The a + b + c = 0 identity (high frequency)

**a³ + b³ + c³ − 3abc = (a + b + c)(a² + b² + c² − ab − bc − ca)**

So: **if a + b + c = 0, then a³ + b³ + c³ = 3abc.**

This is the single most tested algebraic identity in CAT, usually disguised with cube roots.

**Worked example (cube-root form):** If ∛x + ∛y + ∛z = 0, find (x + y + z)³ in terms of xyz.
- Let a = ∛x, b = ∛y, c = ∛z. Then a + b + c = 0 ⟹ a³ + b³ + c³ = 3abc
- x + y + z = 3∛(xyz) ⟹ **(x + y + z)³ = 27xyz**

**Worked example (numeric):** Find the value of (7 − 4)³ + (4 − 9)³ + (9 − 7)³.
- The three brackets are 3, −5, 2, which sum to **0**
- So the expression = 3 · 3 · (−5) · 2 = **−90**

**The recognition cue:** any expression of the form (a−b)³ + (b−c)³ + (c−a)³ — the three terms always sum to zero inside, so the value is **3(a−b)(b−c)(c−a)**, no expansion needed. Spot this shape and you're done in five seconds.

**The converse matters too:** if a³ + b³ + c³ = 3abc, then either a + b + c = 0 **or** a = b = c. Questions that give you the cubic condition and ask "which of the following must be true" are testing exactly this both-cases point.

---

## 6. Inequalities and maxima–minima

- **AM ≥ GM:** for positive numbers, (a+b)/2 ≥ √(ab). Equality iff a = b.
- Fixed **sum** ⟹ product is maximum when terms are equal.
- Fixed **product** ⟹ sum is minimum when terms are equal.
- x + 1/x ≥ 2 for x > 0; ≤ −2 for x < 0.
- **Modulus:** |x| < a ⟺ −a < x < a. |x| > a ⟺ x < −a or x > a.
- **Triangle inequality:** |a + b| ≤ |a| + |b|.

**Worked example:** Minimum value of 4x + 9/x for x > 0.
- AM ≥ GM: (4x + 9/x)/2 ≥ √36 = 6 ⟹ minimum = **12**, at 4x = 9/x ⟹ x = 3/2.

**Modulus equations — always case-split** at the points where each expression inside changes sign, then solve each case and check the solution lies in that case's range. Solutions outside their own range are discarded.

---

## 7. Functions (brief but tested)

- **f(x) + f(1/x)** and **f(x) + f(−x)** type identities: substitute the second value into the given relation to get a second equation, then solve the pair.
- **Even:** f(−x) = f(x). **Odd:** f(−x) = −f(x).
- **Composite:** work from the inside out; f(g(x)) ≠ g(f(x)) in general.
- **Inverse:** swap x and y, solve for y.

**Worked example:** If f(x) + 2f(1/x) = 3x, find f(2).
- Put x = 2: f(2) + 2f(1/2) = 6
- Put x = 1/2: f(1/2) + 2f(2) = 3/2
- Multiply the second by 2 and subtract: 4f(2) − f(2) = 3 − 6 ⟹ 3f(2) = −3 ⟹ f(2) = **−1**

That substitute-the-reciprocal move is the standard trick for the whole family.

---

## 8. Linear equations in word problems

- **Number of equations must match the number of unknowns** — unless the question exploits integer constraints (then see `Number-System.md` §11).
- For two equations a₁x + b₁y = c₁ and a₂x + b₂y = c₂:
  - Unique solution if a₁/a₂ ≠ b₁/b₂
  - Infinitely many if all three ratios are equal
  - No solution if the a and b ratios are equal but the c ratio differs

**The habit that saves time:** name the *quantity the question asks about* as your variable, not some intermediate. Many CAT questions ask for x + y or x/y directly, which can often be obtained by adding or dividing the equations without ever finding x and y.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Squaring a surd equation | accept all roots | substitute back; discard extraneous |
| a³+b³+c³ = 3abc | conclude a+b+c = 0 | also possible: a = b = c |
| (a+b)³ | a³ + b³ | plus 3ab(a+b) |
| Max of a quadratic | differentiate | use x = −b/2a |
| Modulus equation | solve one case | case-split at every sign change |
| AM ≥ GM | applied to negatives | positives only |
| Comparing surd expressions | equate whole sides | equate rational and irrational parts separately |
| Solving for x and y | always find both | often x+y or xy is obtainable directly |

---

## Practical exam habits

- Before solving, scan for a recognisable form: difference of squares, x + 1/x, symmetric sum, (a−b)³ + (b−c)³ + (c−a)³. Recognition beats computation almost every time.
- If an expression is symmetric in its variables, don't solve for the variables — express the target in Σa, Σab, abc.
- With surds, ask "is the product of these two conjugates 1?" If so, you're in reciprocal territory and §1's chain applies.
- Substitute back into the original equation for anything involving squaring, moduli, or logs. It costs ten seconds and catches extraneous roots.
- If the algebra is getting long, you've missed the intended identity. Stop and re-read the expression's shape.

**Where this feeds forward:** `Number-System.md` §9 and §11 (surd/exponent forms, integer solutions), `Logarithms.md` (log equations use the same substitute-and-check discipline), `Means-and-Weighted-Averages.md` §8 (AM–GM), `Progressions-AP-GP.md` (symmetric term selection), `Geometry-Mensuration.md` §6 (AM–GM as geometric optimisation).
