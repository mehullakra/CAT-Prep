# Progressions — AP, GP, HP

> CAT quant. An AP is a straight line through integer inputs; a GP is a constant multiplier. Once you write down a and d (or a and r), everything else is substitution.

---

## 1. Arithmetic Progression — the core

- **nth term:** aₙ = a + (n − 1)d
- **Sum of n terms:** Sₙ = (n/2)[2a + (n−1)d] = **(n/2)(first + last)**

The second form of Sₙ is the one to use. Sum = (number of terms) × (average term), and the average of an AP is just (first + last)/2.

- **Number of terms** from first term f to last term l with common difference d: **n = (l − f)/d + 1**

That "+1" is the single most common slip in the topic. Count 10, 20, 30: (30−10)/10 + 1 = 3. ✓

- aₙ = Sₙ − Sₙ₋₁ — use this whenever a question defines Sₙ by a formula
- If Sₙ is a quadratic in n with no constant term, the sequence is an AP

---

## 2. Type 1 — Sum of a term range

To sum from the mᵗʰ term to the nᵗʰ term: **S(m to n) = Sₙ − Sₘ₋₁**.

The subscript is m − 1, not m. Getting this wrong drops one whole term.

**Worked example:** In the AP 5, 9, 13, …, find the sum of the 10th to the 20th terms.
- a = 5, d = 4
- a₁₀ = 5 + 9(4) = 41; a₂₀ = 5 + 19(4) = 81
- Number of terms from the 10th to the 20th inclusive = 20 − 10 + 1 = **11**
- Sum = (11/2)(41 + 81) = (11/2)(122) = **671**

Working directly with first-and-last is faster and safer than computing S₂₀ − S₉. Use it whenever you can identify both endpoints.

**Cross-check:** S₂₀ = (20/2)(5 + 81) = 860; S₉ = (9/2)(5 + 37) = 189; 860 − 189 = 671 ✓

---

## 3. Type 2 — Counting and locating integer terms in a subsequence

A frequent CAT setup: "How many terms common to two APs lie below 1000?" or "How many terms of this AP are also perfect squares / multiples of 7?"

**The governing fact: the terms common to two APs themselves form an AP, whose common difference is the LCM of the two common differences.**

**Method:**
1. Find the **first** common term (by inspection, or by solving a congruence).
2. New common difference = LCM(d₁, d₂).
3. Count terms up to the limit with n = (last − first)/d + 1.

**Worked example:** How many terms are common to the APs 2, 5, 8, … , 299 and 3, 7, 11, … , 399?
- First AP: ≡ 2 (mod 3). Second: ≡ 3 (mod 4).
- First common term: 11 (11 = 2+9 ✓, 11 = 3+8 ✓)
- New d = LCM(3, 4) = 12
- Upper bound = min(299, 399) = 299 ⟹ largest common term ≤ 299 of the form 11 + 12k: 11 + 12(24) = 299 ✓
- Count = (299 − 11)/12 + 1 = 24 + 1 = **25**

**Worked example (locating, not just counting):** In the AP 7, 11, 15, …, which term is 407?
- 407 = 7 + (n−1)4 ⟹ 400 = 4(n−1) ⟹ n = **101**

If n comes out non-integer, the value simply isn't a term — that's often the intended answer.

**Multiples within a range:** the count of multiples of k in [1, N] is ⌊N/k⌋. In [A, B] it is ⌊B/k⌋ − ⌊(A−1)/k⌋. Use this rather than building an AP when the question is purely about multiples.

---

## 4. Useful AP facts

- Sum of the first n naturals = n(n+1)/2
- Sum of the first n odd numbers = **n²**
- Sum of the first n even numbers = n(n+1)
- Sum of squares = n(n+1)(2n+1)/6
- Sum of cubes = [n(n+1)/2]² — the square of the sum
- If a, b, c are in AP then **2b = a + c** (b is the arithmetic mean)
- **Symmetric selection:** for 3 terms in AP take a−d, a, a+d; for 4 take a−3d, a−d, a+d, a+3d (common difference 2d). This makes the sum condition trivial and is the standard trick for "three numbers in AP sum to S" questions.
- The average of an AP equals its middle term (odd count) or the average of the two middle terms (even count)

**Worked example:** Three numbers in AP sum to 24 and their product is 440. Find them.
- Take a−d, a, a+d ⟹ 3a = 24 ⟹ a = 8
- (8−d)(8)(8+d) = 440 ⟹ 64 − d² = 55 ⟹ d² = 9 ⟹ d = 3
- Numbers: **5, 8, 11**

---

## 5. Geometric Progression

- **nth term:** aₙ = ar^(n−1)
- **Sum of n terms:** Sₙ = a(rⁿ − 1)/(r − 1) for r ≠ 1
- **Infinite sum:** S∞ = **a/(1 − r)**, valid only when |r| < 1
- If a, b, c are in GP then **b² = ac** (b is the geometric mean)
- Symmetric selection: for 3 terms take a/r, a, ar — the product is then a³, which handles "product = P" conditions instantly

**Worked example:** Three numbers in GP have product 216 and sum 26. Find them.
- a/r · a · ar = a³ = 216 ⟹ a = 6
- 6/r + 6 + 6r = 26 ⟹ 6/r + 6r = 20 ⟹ 3r² − 10r + 3 = 0 ⟹ r = 3 or 1/3
- Numbers: **2, 6, 18**

**Infinite GP — the two standard uses:**
- Repeating decimals: 0.333… = 0.3/(1 − 0.1) = 1/3
- Bouncing ball / repeated-halving distance problems: total distance = h + 2h·r/(1 − r) for a ball dropped from h rebounding to fraction r.

**Worked example:** A ball dropped from 10 m rebounds to 3/5 of its height each time. Total distance until rest?
- 10 + 2(10)(3/5)/(1 − 3/5) = 10 + 12/0.4 = 10 + 30 = **40 m**

---

## 6. Harmonic Progression

a, b, c are in HP ⟺ their reciprocals are in AP.

- **Always convert to reciprocals and treat it as an AP.** There is no useful HP sum formula.
- Harmonic mean of a and b = 2ab/(a+b)
- If a, b, c are in HP then b = 2ac/(a+c)

**AM ≥ GM ≥ HM** for positive numbers, with equality only when all terms are equal. See `Means-and-Weighted-Averages.md` §8.

---

## 7. Type 3 — AGP and telescoping (occasional but decisive)

**Arithmetico-geometric:** terms like n·rⁿ. Method: write S, write rS, subtract. The middle collapses into a GP.

**Worked example:** S = 1 + 2x + 3x² + 4x³ + … (|x| < 1)
- S − xS = 1 + x + x² + … = 1/(1 − x) ⟹ S = **1/(1 − x)²**

**Telescoping:** if a term can be written as f(n) − f(n+1), the sum collapses to f(1) − f(last+1).

**Worked example:** Sum of 1/(1·2) + 1/(2·3) + … + 1/(99·100).
- 1/(n(n+1)) = 1/n − 1/(n+1)
- Sum = 1 − 1/100 = **99/100**

The recognition cue for telescoping is a **product of consecutive terms in the denominator**. Split by partial fractions and almost everything cancels.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Counting terms from f to l | (l − f)/d | (l − f)/d + 1 |
| Sum of mᵗʰ to nᵗʰ terms | Sₙ − Sₘ | Sₙ − Sₘ₋₁ |
| Infinite GP sum | always a/(1−r) | only when \|r\| < 1 |
| Common terms of two APs | new d = d₁ × d₂ | new d = LCM(d₁, d₂) |
| Sum of cubes | n(n+1)(2n+1)/6 | [n(n+1)/2]² |
| Three terms in AP | a, a+d, a+2d | use a−d, a, a+d — sum becomes 3a |
| HP handled directly | HP formulas | invert to an AP |
| Bouncing ball | h·2r/(1−r) only | add the initial drop h |

---

## Practical exam habits

- Write a and d (or a and r) on the page before reading the rest of the question.
- For any sum, prefer (n/2)(first + last). It needs no memory and no sign errors.
- Use symmetric selection whenever the question gives a sum or product of 3 or 4 terms — it removes one unknown for free.
- When two progressions are involved, think LCM and congruences, not listing.
- Sanity-check n: it must be a positive integer. A fractional n means the value isn't in the sequence, which is frequently the answer itself.

**Where this feeds forward:** `Number-System.md` §8 and §11 (counting multiples, congruences), `Means-and-Weighted-Averages.md` §8 and §10 (means, sequence averages), `Algebra.md` (symmetric selection is the same idea as symmetric sums), `Logarithms.md` (logs of a GP form an AP).
