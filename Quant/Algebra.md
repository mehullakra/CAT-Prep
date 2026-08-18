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

## 3a. Finite differences — P(x + 1) − P(x)

**Core idea.** If P has degree n with leading coefficient a, then

**Q(x) = P(x + 1) − P(x) has degree n − 1 and leading coefficient n·a.**

Only the top term survives: (x + 1)ⁿ − xⁿ = n·xⁿ⁻¹ + (lower). Differencing is the discrete twin of differentiating and behaves the same way on degrees.

The second half of the idea is that differences **telescope**:

**P(b) − P(a) = Q(a) + Q(a+1) + … + Q(b−1)**

So a question that hands you Q and asks for a difference of P values never requires P's coefficients at all. (Telescoping sums in general: `Progressions-AP-GP.md` §7.)

**Method:**
1. Read off deg Q = deg P − 1 and its leading coefficient n·a.
2. Combine that with the given roots to pin Q down completely.
3. Telescope: sum Q(k) over k = a to b − 1.

**Worked example:** P(x) = x⁴ + bx³ + cx² + dx + e, and P(x + 1) − P(x) has roots 1, 2 and 3. Find P(7) − P(1).

- P is degree 4, leading coefficient 1 ⟹ Q is degree **3** with leading coefficient 4 × 1 = **4**.
- A cubic with roots 1, 2, 3 and leading coefficient 4 is fully determined: Q(x) = 4(x − 1)(x − 2)(x − 3).
- Telescope: P(7) − P(1) = Q(1) + Q(2) + … + Q(6).
- Q(1) = Q(2) = Q(3) = 0; Q(4) = 4·3·2·1 = 24; Q(5) = 4·4·3·2 = 96; Q(6) = 4·5·4·3 = 240.
- Sum = 24 + 96 + 240 = **360**

b, c, d and e were never needed — and could not have been found, since Q determines P only up to the constant e.

**Traps:**
- Taking Q's leading coefficient as 1 because P is monic. It is n·a = 4; dropping it divides every answer by 4.
- Summing k = 1 to 7. P(b) − P(a) has **b − a** terms, k = a … b − 1 — here 6 terms, not 7.
- Trying to solve for b, c, d, e first. Three conditions cannot fix four unknowns, and the question doesn't need them.

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

## 6a. AM–GM with split terms — maximising xᵃyᵇzᶜ under a linear constraint

**The shape:** "Given px + qy + rz = S with x, y, z > 0, maximise xᵃ y^b z^c."

Plain AM–GM on the three terms fails, because its equality condition px = qy = rz is the optimum only when a = b = c = 1.

**Core idea — split each term into as many equal pieces as its exponent.**

Write px as a copies of (px/a), qy as b copies of (qy/b), rz as c copies of (rz/c), then apply AM–GM to all **n = a + b + c** pieces. Their product contains xᵃyᵇzᶜ exactly, and equality becomes

**px/a = qy/b = rz/c = S/n**

In words: **the constraint is divided in proportion to the exponents.**

**Method:**
1. n = sum of the exponents. Each piece equals S/n at the optimum.
2. Read x, y, z straight off px/a = S/n, and so on.
3. Substitute to get the maximum. You almost never need to write the inequality chain — only its equality condition.

**Worked example:** If 4x + 9y + 2z = 72 with x, y, z positive reals, find the maximum value of x²y³z.

- Exponents 2, 3, 1 ⟹ n = 6 pieces, each equal to 72/6 = **12**
- 4x splits into 2 pieces of 2x ⟹ 2x = 12 ⟹ **x = 6**
- 9y splits into 3 pieces of 3y ⟹ 3y = 12 ⟹ **y = 4**
- 2z is a single piece ⟹ 2z = 12 ⟹ **z = 6**
- Constraint check: 24 + 36 + 12 = 72 ✓
- Maximum = 6² · 4³ · 6 = 36 × 64 × 6 = **13,824**

(In full: 12 = (2x + 2x + 3y + 3y + 3y + 2z)/6 ≥ ((2x)²(3y)³(2z))^(1/6), so 216·x²y³z ≤ 12⁶ = 2,985,984 ⟹ x²y³z ≤ 13,824.)

**The mirror version** — minimise a linear expression given a fixed product — is the same split read backwards.

**Traps:**
- Setting 4x = 9y = 2z. That is the all-exponents-1 condition; it gives 8,192, well short of 13,824.
- Splitting by the coefficients instead of the exponents. The coefficients 4, 9, 2 stay attached to their variables; only 2, 3, 1 decide the number of pieces.
- Applying AM–GM without the positivity condition (§6). It is a positives-only tool.

---

## 6b. Inequalities with a sum of moduli

**Core idea.** f(x) = |x − p₁| + |x − p₂| + … is **piecewise linear and convex** — a chain of straight segments whose slope only increases as x increases. Two consequences do all the work:

- The solution set of **f(x) ≤ k is a single interval** (possibly empty). It never breaks into two pieces.
- So only the **two outermost pieces** matter. Take x far right (every bracket opens positive) and x far left (every bracket opens negative); those two linear inequalities give the endpoints. Every critical point in between can be ignored.

That turns a four-case slog into two lines.

**Method:**
1. Far right: drop all the modulus signs as-is, solve for the upper endpoint.
2. Far left: negate every bracket, solve for the lower endpoint.
3. Confirm the set is non-empty by evaluating f at any interior critical point and checking it is ≤ k.
4. Count integers in the closed interval: **⌊right⌋ − ⌈left⌉ + 1**.

**Worked example:** For how many integer values of x is |x − 2| + |x + 1| + |2x − 5| ≤ 10?

- Critical points are x = 2, −1, 2.5 — noted, then ignored.
- **Far right** (x ≥ 2.5): (x − 2) + (x + 1) + (2x − 5) = 4x − 6 ≤ 10 ⟹ x ≤ **4**
- **Far left** (x ≤ −1): (2 − x) + (−x − 1) + (5 − 2x) = 6 − 4x ≤ 10 ⟹ x ≥ **−1**
- Non-empty check at x = 2: 0 + 3 + 1 = 4 ≤ 10 ✓
- Solution set = [−1, 4]; integers −1, 0, 1, 2, 3, 4 ⟹ **6**

**Where the minimum sits** (asked directly nearly as often): for |x − p₁| + … + |x − pₙ| the minimum is at the **median** of the pᵢ, or anywhere between the two middle ones when n is even. A coefficient counts as multiplicity — |2x − 5| = 2|x − 2.5| is *two* copies of the point 2.5. Here the points are −1, 2, 2.5, 2.5, so f is flat and minimal at 4 across [2, 2.5].

**Traps:**
- Case-splitting all four regions. Correct but slow, and every case is a chance to flip a sign.
- Counting integers as right − left. A closed interval holds right − left + 1 of them: 4 − (−1) + 1 = **6**, not 5.
- Assuming a modulus inequality always splits into two disjoint rays. True for |x| ≥ k; false for a *sum* of moduli bounded above, which is always one interval.
- Ignoring the coefficient inside a modulus when locating the minimum. |2x − 5| carries weight 2.

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

## 8a. Symmetric linear systems with a parameter

**The shape:** ax + by = k and bx + ay = k — the same two coefficients, swapped, with the same right-hand side. CAT dresses it up by asking for how many integer values of a parameter the solution meets some sign or size condition.

**Core idea — use the symmetry, not Cramer's rule.**

- **Subtract:** (a − b)x + (b − a)y = 0 ⟹ (a − b)(x − y) = 0. So **either a = b, or x = y.**
- **Add:** (a + b)(x + y) = 2k.

If a ≠ b then x = y, and one substitution collapses the system to a single fraction: **x = y = k/(a + b)**.

**Uniqueness** is the §8 condition a₁/a₂ ≠ b₁/b₂, which here reads a² ≠ b², i.e. **a ≠ ±b**.

**Method:**
1. Discard the parameter values that break uniqueness (a = ±b).
2. Use the symmetry to get x = y = k/(a + b).
3. Impose the stated condition on that one expression and count the parameter values.

**Worked example:** For how many negative integers m does mx + 3y = 11, 3x + my = 11 have a unique solution with x and y both strictly positive?

- Unique ⟺ m² ≠ 9 ⟹ m ≠ −3 (m is negative, so m = 3 is already out).
- m ≠ 3, so subtracting gives x = y. Substituting: mx + 3x = 11 ⟹ x = y = 11/(m + 3).
- x > 0 ⟹ m + 3 > 0 ⟹ m > −3. Negative integers greater than −3: **m = −1, −2**.
- Check: m = −1 ⟹ x = y = 11/2 ✓; m = −2 ⟹ x = y = 11 ✓; m = −4 ⟹ x = y = −11 ✗.
- Answer: **2**

**Traps:**
- Counting m = −3. It gives −3x + 3y = 11 and 3x − 3y = 11 — parallel and contradictory, so *no* solution, not a unique one.
- Reading "strictly positive" as "positive integer". x = 11/2 is a perfectly valid solution; nothing required integrality.
- Answering "infinitely many" because every m < −3 gives a unique solution. It does — but with x and y both negative, which the question forbids.
- Grinding the determinant when x = y drops out of a single subtraction.

---

## 8b. The shortfall trick — one variable instead of four

**The shape:** someone buys several things, has money left over, and the question states how much *more* they would need for one unit of each item. It looks like four unknowns; it is one.

**Core idea.** Let **r = the money left over**. "She needs ₹7 more to buy an apple" says the apple costs r + 7. Every price is now r + (its stated shortfall), so the purchase equation has a single unknown.

The same move covers any "falls short by", "is short of", "needs x more" phrasing — including the classic "if each child gets 5 sweets, 8 are left; if each gets 6, we are 4 short."

**Method:**
1. Name the leftover (or the shortfall) — not the prices.
2. Write each price as leftover + its own shortfall.
3. Substitute into the total-spent equation and solve the single linear equation.
4. Sanity-check that the leftover really is smaller than every price, since the question said she could not buy any item.

**Worked example:** Sushila buys 11 pomegranates, 7 apples and a dozen kiwis for ₹1090, and is left with too little to buy even one more of any of them. She would need ₹7 more for an apple, ₹9 more for a pomegranate and ₹16 more for a kiwi. Find the total price of one apple, one pomegranate and one kiwi.

- Let the leftover be r. Then apple = r + 7, pomegranate = r + 9, kiwi = r + 16.
- 11(r + 9) + 7(r + 7) + 12(r + 16) = 1090
- 11r + 99 + 7r + 49 + 12r + 192 = 1090 ⟹ **30r + 340 = 1090** ⟹ 30r = 750 ⟹ **r = 25**
- Prices: apple 32, pomegranate 34, kiwi 41. Sum = **107**
- Checks: 11(34) + 7(32) + 12(41) = 374 + 224 + 492 = 1090 ✓, and 25 < 32, so indeed she cannot buy any ✓

**Traps:**
- Treating the three shortfalls as the prices, or as differences *between* prices. ₹7 and ₹9 are each measured from the same leftover, so pomegranate − apple = 2 — that is all the direct comparison you get.
- Naming three price variables. One equation and three unknowns looks unsolvable and sends people hunting for information that is not there; the leftover is the hidden fourth quantity that makes it determinate.
- Missing "a dozen" = 12.
- Forgetting the feasibility check. If r came out larger than the cheapest item, the reading of the question would be wrong.

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
| Maximising xᵃyᵇzᶜ | set the linear terms equal | split each in proportion to its exponent |
| Sum of moduli ≤ k | split every case | convex ⟹ one interval; only the two outer pieces matter |
| "Needs ₹7 more for an apple" | ₹7 is the price, or a price gap | name the leftover r; price = r + 7 |
| Comparing surd expressions | equate whole sides | equate rational and irrational parts separately |
| Solving for x and y | always find both | often x+y or xy is obtainable directly |
| Symmetric system with a parameter | apply Cramer's rule | subtract ⟹ x = y, then one fraction |

---

## Practical exam habits

- Before solving, scan for a recognisable form: difference of squares, x + 1/x, symmetric sum, (a−b)³ + (b−c)³ + (c−a)³. Recognition beats computation almost every time.
- If an expression is symmetric in its variables, don't solve for the variables — express the target in Σa, Σab, abc.
- With surds, ask "is the product of these two conjugates 1?" If so, you're in reciprocal territory and §1's chain applies.
- Substitute back into the original equation for anything involving squaring, moduli, or logs. It costs ten seconds and catches extraneous roots.
- If the algebra is getting long, you've missed the intended identity. Stop and re-read the expression's shape.

**Where this feeds forward:** `Number-System.md` §9 and §11 (surd/exponent forms, integer solutions), `Logarithms.md` (log equations use the same substitute-and-check discipline), `Means-and-Weighted-Averages.md` §8 (AM–GM), `Progressions-AP-GP.md` (symmetric term selection), `Quadrilaterals-and-Polygons.md` §7 (AM–GM as geometric optimisation).
