# Number System

> CAT quant. The largest and most unpredictable topic. Almost everything reduces to one of three tools: **prime factorisation**, **remainder cycles**, or **the mod-9 digit sum**. Learn which tool a question wants and it stops being scary.

---

## 1. The three tools

| Tool | Use it when the question is about… |
|---|---|
| **Prime factorisation** | factors, HCF/LCM, perfect squares/cubes, trailing zeros |
| **Remainders / cyclicity** | last digit, last two digits, "remainder when divided by", powers |
| **Digit sum (mod 9)** | digit-sum functions, divisibility by 3 and 9, checking answers |

If you can classify the question in ten seconds, you've done the hard part.

---

## 2. Divisibility rules

| Divisor | Test |
|---|---|
| 2, 4, 8 | last 1, 2, 3 digits |
| 3, 9 | **digit sum** divisible by 3, 9 |
| 5, 25 | last 1, 2 digits |
| 6 | divisible by 2 **and** 3 |
| 7 | drop last digit, subtract twice it, repeat |
| 11 | alternating sum of digits divisible by 11 |
| 13 | drop last digit, add 4× it, repeat |
| 8 | last 3 digits divisible by 8 |

**Composite divisors:** test the coprime factors separately. Divisible by 12 ⟺ divisible by 3 and 4. Note 12 = 2 × 6 is *not* a valid split — the factors must be coprime.

---

## 2a. Terminating and recurring decimals

**Core idea.** Write the fraction **in lowest terms** first — everything below is false otherwise. Then the denominator alone decides the decimal's shape.

| Denominator q (lowest terms) | Decimal |
|---|---|
| q = 2ᵃ5ᵇ only | **terminates**, after max(a, b) places |
| q coprime to 10 | **purely recurring** |
| q = 2ᵃ5ᵇ × k, with k coprime to 10 | **mixed** — max(a,b) non-repeating digits, then recurs |

**Length of the recurring block** = the smallest d with 10ᵈ ≡ 1 (mod k). That d always **divides φ(k)**, which is usually enough to pin it down by testing the divisors.

**Worked examples:**
- 7/40: 40 = 2³·5 ⟹ terminates after max(3,1) = **3 places** (0.175)
- 1/7: 7 is coprime to 10, φ(7) = 6, and no smaller divisor works ⟹ period **6** (0.142857…)
- 1/6: 6 = 2 × 3 ⟹ mixed, 1 non-repeating digit then period 1 (0.1666…)
- 1/13: φ(13) = 12; 10⁶ ≡ 1 (mod 13) ⟹ period **6** (0.076923…)

The 1/7 and 1/13 digit families are worth recognising on sight — see `Reference/Calculation-Toolkit.md` §10.

**Traps:** not reducing first (6/8 looks like it has denominator 8 but is 3/4); assuming every non-terminating decimal is purely recurring; assuming the period equals φ(k) rather than a divisor of it.

---

## 2b. Parity — the even/odd test

Cheap, and it settles "prove no solution exists" questions in one line.

- even ± even = even; odd ± odd = **even**; even ± odd = odd
- even × anything = even; odd × odd = odd
- **a + b and a − b always have the same parity**
- the sum of n odd numbers is odd **iff n is odd**
- the product of k consecutive integers is divisible by **k!** — so any two consecutive give an even, any three give a multiple of 6

**Squares mod 4 and mod 8 are the sharpest form of this** (§10): a square is ≡ 0 or 1 (mod 4), so a sum of two squares is ≡ 0, 1 or 2 (mod 4) and **never 3**.

**Worked example:** Can x² + y² = 2023 have integer solutions?
- 2023 = 4(505) + 3 ⟹ 2023 ≡ 3 (mod 4), which no sum of two squares can be ⟹ **no**

**Worked example:** Can the sum of five odd numbers be 100?
- Five odds sum to odd; 100 is even ⟹ **no**. No algebra required.

---

## 3. Prime factorisation — everything it gives you

If N = p^a · q^b · r^c …

- **Number of factors** = (a+1)(b+1)(c+1)…
- **Sum of factors** = [(p^(a+1) −1)/(p−1)] × [(q^(b+1) −1)/(q−1)] × …
- **Product of factors** = N^(number of factors / 2)
- **Number of ways to write N as a product of two factors** = (number of factors)/2, rounded up if N is a perfect square
- **Odd factors:** drop the powers of 2 entirely, then count
- **Number of factors that are perfect squares:** count only even exponents — ⌊a/2⌋+1 times ⌊b/2⌋+1 …

**Worked example:** N = 720 = 2⁴ · 3² · 5.
- Factors = 5 × 3 × 2 = **30**
- Odd factors = 3 × 2 = **6**
- Perfect-square factors = 3 × 2 × 1 = **6** (1, 4, 9, 16, 36, 144)

**Trailing zeros in n!** = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + …
(100! has 20 + 4 = 24 trailing zeros.)

---

## 4. HCF and LCM

- **HCF × LCM = product of the two numbers** (only for two numbers)
- HCF = product of common primes to the **lowest** power
- LCM = all primes to the **highest** power
- HCF of fractions = HCF(numerators)/LCM(denominators); LCM of fractions = LCM(num)/HCF(den)

**Remainder-based HCF questions:** "the largest number that divides 43, 91, 183 leaving the same remainder" ⟹ take HCF of the *differences*: HCF(91−43, 183−91) = HCF(48, 92) = 4.

---

## 4a. HCF and LCM word problems

§4 gives the machinery. These are the five shapes it gets used in, and recognising which one you are looking at *is* the question.

| Phrasing | Take |
|---|---|
| largest tile / longest tape / greatest measure that fits exactly | **HCF** |
| bells toll together, lights blink together, buses depart together | **LCM** |
| least number leaving remainder r with each of a, b, c | **LCM(a,b,c)·k + r** |
| least number leaving remainders r₁, r₂, r₃ where each divisor − remainder is the same d | **LCM − d** |
| largest number dividing a, b, c leaving remainders r₁, r₂, r₃ | **HCF(a−r₁, b−r₂, c−r₃)** |

"Same remainder, remainder unknown" is the §4 case: HCF of the **differences**.

**Worked example (LCM, and the +1):** Bells toll at intervals of 2, 4, 6, 8, 10 and 12 seconds, starting together. How many times do they toll together in 30 minutes?
- LCM(2,4,6,8,10,12) = **120 s**
- 1800/120 = 15 further coincidences, **plus the one at the start = 16**
- Whether the initial toll counts is the entire difficulty; read the wording.

**Worked example (constant deficit):** The least number which, divided by 5, 6 and 7, leaves remainders 3, 4 and 5.
- Each remainder is **2 less** than its divisor ⟹ the number is 2 less than a common multiple
- LCM(5,6,7) = 210 ⟹ answer **208**

**Worked example (plain remainder):** Least number leaving remainder 3 when divided by 6, 7 and 8.
- LCM = 168 ⟹ **171**

**Worked example (ratio):** Two numbers are in the ratio 3 : 4 and their HCF is 4. Find their LCM.
- The numbers are 3k and 4k with k = HCF = 4 ⟹ 12 and 16 ⟹ LCM = **48**
- General: numbers a·h and b·h with a, b coprime have LCM = **abh**, and product = HCF × LCM ✓

**Traps:** forgetting the initial simultaneous event; using HCF where "together again" wants LCM; applying HCF × LCM = product to three numbers (§4 — two only).

---

## 5. Unit digit and cyclicity

Unit digits repeat with period ≤ 4.

| Last digit of base | Cycle |
|---|---|
| 0, 1, 5, 6 | always itself |
| 4, 9 | period 2 |
| 2, 3, 7, 8 | period 4 |

**Method:** take the exponent mod 4. If the remainder is 0, use the 4th term of the cycle.

**Worked example:** Unit digit of 7^105.
- 7 has cycle 7, 9, 3, 1. 105 mod 4 = 1 ⟹ **7**

---

## 5a. Last two digits

§5 gives the last digit. The last **two** needs a different tool for each ending, and these four cases cover everything CAT sets.

**1. Base ends in 1.** The answer ends in 1, and the tens digit is

**(tens digit of the base × exponent) mod 10**

Because (1 + 10a)ⁿ ≡ 1 + 10an (mod 100) — every later binomial term carries 100.

- 31⁴⁵: tens = (3 × 45) mod 10 = 135 mod 10 = 5 ⟹ **51**

**2. Base ends in 3, 7 or 9 — convert to case 1.** 3⁴ = 81, 7⁴ = 2401, 9² = 81. Raise to that power first, then apply case 1.

- 7¹⁰⁰ = (7⁴)²⁵ ≡ 01²⁵ ⟹ **01**
- 3¹⁰⁰ = (3⁴)²⁵ ≡ 81²⁵; tens = (8 × 25) mod 10 = 0 ⟹ **01**

**3. Even bases — use 2¹⁰ ≡ 24 and the 76 fixed point.** Any number ending in **76 stays ending in 76** under any power, which collapses most of these.

- 2¹⁰⁰ = (2¹⁰)¹⁰ ≡ 24¹⁰; 24² = 576 ≡ 76 ⟹ 24¹⁰ = (24²)⁵ ≡ 76⁵ ≡ **76**

**4. The general fallback — split mod 4 and mod 25**, then recombine. Slower, but never fails.

- 2¹⁰⁰: ≡ 0 (mod 4). φ(25) = 20 ⟹ 2¹⁰⁰ = (2²⁰)⁵ ≡ 1 (mod 25). The number ≡ 0 mod 4 and ≡ 1 mod 25 is **76** ✓

**Worth memorising:** …76 raised to any power ends in 76. …25 ends in 25. …01 ends in 01. Spotting one of these ends the question immediately.

**Traps:** applying the case-1 rule to a base not ending in 1; using the *unit* digit of the base where the rule wants the *tens* digit; forgetting to reduce the exponent mod 10 in case 1.

---

## 6. Remainder theorems worth knowing

- **Fermat:** if p is prime and gcd(a,p) = 1, then a^(p−1) ≡ 1 (mod p)
- **Euler:** a^φ(n) ≡ 1 (mod n) when gcd(a,n) = 1, where φ(n) = n·Π(1 − 1/p)
- **Wilson:** (p−1)! ≡ −1 (mod p) for prime p
- **Negative-remainder trick:** replace a base by base − modulus. Remainder of 6^100 by 7: 6 ≡ −1, so (−1)^100 = **1**.

The negative-remainder trick is worth more exam marks than Fermat and Euler combined. Look for a base that's one more or one less than the divisor.

---

## 7. Digit-sum functions on powers — F(N) = digit sum of Nᵏ

This is a recurring CAT-style question: "Let F(N) be the sum of the digits of N. Find F(F(F(2^2020)))."

**The key fact: repeatedly taking the digit sum until one digit remains gives the *digital root*, and**

**digital root of N = N mod 9** (with the convention that a result of 0 means 9, for N ≠ 0).

Why: 10 ≡ 1 (mod 9), so every digit's place value is ≡ 1, and the number is congruent to its digit sum.

**Method:**
1. Compute N mod 9 using cyclicity.
2. That is the value after enough digit sums to reach one digit.
3. Check the question isn't asking for a *single* digit sum of a specific number — that's different and needs actual digits.

**Worked example:** Find the repeated digit sum of 2^100.
- Powers of 2 mod 9 cycle with period 6: 2, 4, 8, 7, 5, 1
- 100 mod 6 = 4 ⟹ the 4th term = **7**

**Worked example:** F(N) = digit sum. Find F(F(F(4^444))).
- 4 mod 9 cycles 4, 7, 1 (period 3). 444 mod 3 = 0 ⟹ the 3rd term = **1**
- Sanity: 4^444 has about 268 digits, so F ≤ 2412, F(F) ≤ 28, F(F(F)) is a single digit. Three applications are enough to reach the digital root, so the answer is **1**.

**Always do that sanity check.** The examiner chooses the number of F-applications so that you *just* reach one digit. If the count is too small, you cannot use the digital root and must bound the value instead.

**Bounding rule:** a number with d digits has digit sum ≤ 9d. Use it to show the chain has collapsed to one digit.

---

## 8. Divisibility + digit-sum constraint counting

Typical: "How many 3-digit numbers are divisible by 9 and have all distinct digits?" or "How many 4-digit numbers have digit sum 9?"

**Method:**
1. Convert the divisibility into a digit-sum condition (works for 3 and 9 only).
2. Count the digit combinations satisfying that sum.
3. Arrange, subtracting cases with a leading zero.

**Worked example:** How many 3-digit numbers have digit sum equal to 6?
- Solve a + b + c = 6 with 1 ≤ a ≤ 9, 0 ≤ b, c ≤ 9.
- Substitute a′ = a − 1 ≥ 0: a′ + b + c = 5.
- Non-negative solutions = C(5+2, 2) = C(7,2) = **21**
- (No upper-bound violations since 5 < 10.)

Each of those 21 is divisible by 3 but not 9 — a follow-up question about divisibility by 9 would instead set the sum to 9 or 18.

**Worked example:** How many 3-digit numbers are divisible by 9? Digit sum ∈ {9, 18, 27}. Easier route: count multiples of 9 from 108 to 999 ⟹ (999 − 108)/9 + 1 = **100**.

**Rule of thumb:** if the question is *pure* divisibility, count multiples directly with an AP. Use digit-sum counting only when a digit condition is also imposed.

The counting engine here is stars-and-bars: non-negative solutions of x₁+…+x_r = n is C(n + r − 1, r − 1). See `PnC-Probability.md` §9.

---

## 9. Surd and exponent ratio simplification

**The pattern:** expressions like (aⁿ − bⁿ)/(aⁿ⁻¹ + bⁿ⁻¹) look intimidating but almost always collapse by **factoring out the smallest power**.

**Worked example:** Simplify (3^11 − 3^10)/(3^10 + 3^9).
- Numerator = 3^10(3 − 1) = 2·3^10
- Denominator = 3^9(3 + 1) = 4·3^9
- Ratio = (2·3^10)/(4·3^9) = 3/2 = **1.5**

**Worked example:** Simplify (2^12 − 2^10)/(2^11 + 2^9).
- = 2^10(4 − 1) / 2^9(4 + 1) = 2 × 3/5 = **6/5**

**The one identity that actually simplifies the stated form:** for n = 2,

(a² − b²)/(a + b) = **a − b**

So whenever the exponents in numerator and denominator differ by exactly one and the numerator is a difference of squares, the answer is just a − b. Test for that shape first.

**General factorisations to recognise:**
- a^n − b^n = (a − b)(a^(n−1) + a^(n−2)b + … + b^(n−1)) — always divisible by (a − b)
- a^n − b^n is divisible by (a + b) when **n is even**
- a^n + b^n is divisible by (a + b) when **n is odd**

**Surd version — use conjugates.** If a = √3 + √2 and b = √3 − √2, then:
- a + b = 2√3, a − b = 2√2, **ab = 3 − 2 = 1**

That last fact (ab = 1, so b = 1/a) is what makes these questions tractable. Rationalise by multiplying by the conjugate: 1/(√3 + √2) = √3 − √2.

More in `Algebra.md` §4.

---

## 9a. Equations in exponents — match prime by prime

**Core idea.** Unique prime factorisation means an equation between two products of prime powers is really **one equation per prime**. Rewrite every base in primes, collect exponents, and equate each prime's exponent separately. One intimidating equation becomes a small linear system.

**Method:**
1. Rewrite every base in primes: 4 = 2², 8 = 2³, 16 = 2⁴, 20 = 2²·5, 6 = 2·3, 12 = 2²·3.
2. Add exponents across a product; multiply exponents through a power — (2ᵃ)ᵇ = 2^(ab).
3. Write one linear equation per prime.
4. Solve, then apply the natural-number and ordering constraints. With fewer equations than unknowns, **the inequality is what pins the answer down** — it is data, not decoration.

**Worked example:** If 16^(6x) × 4^(24x+12) × 5^(2y) = 8^(4z) × 20^(12x), where x, y, z are natural numbers with x < y ≤ z, find x + y + z.

- LHS: 16^(6x) = 2^(24x), and 4^(24x+12) = 2^(48x+24). So LHS = 2^(72x+24) · 5^(2y).
- RHS: 8^(4z) = 2^(12z), and 20^(12x) = (2²·5)^(12x) = 2^(24x) · 5^(12x). So RHS = 2^(12z+24x) · 5^(12x).
- **Prime 5:** 2y = 12x ⟹ y = 6x
- **Prime 2:** 72x + 24 = 12z + 24x ⟹ 48x + 24 = 12z ⟹ z = 4x + 2
- Constraints: x < y reads x < 6x — true for every natural x, so it gives nothing. y ≤ z reads 6x ≤ 4x + 2 ⟹ 2x ≤ 2 ⟹ **x = 1**.
- x = 1, y = 6, z = 6 ⟹ **x + y + z = 13**

**Traps:**
- Forgetting that a composite base carries two primes. 20^(12x) feeds *both* the 2-equation and the 5-equation; treating it as a pure power of either one breaks the system.
- Stopping once the equations are solved. Two equations in three unknowns leave a whole family — the ordering condition selects the member.
- Assuming every given inequality bites. Here x < y is automatic; only y ≤ z does work. Check which one is live before spending time on it.
- Multiplying exponents when bases are multiplied. 2ᵃ · 2ᵇ = 2^(a+b); only (2ᵃ)ᵇ multiplies.

**Related:** reading structure back *out of* exponents is §10 and §10a.

---

## 10. Perfect squares, cubes, and "least n"

**A number is a perfect square ⟺ every prime exponent is even.** Perfect cube ⟺ every exponent is a multiple of 3.

**Method for "find the least n such that Nn is a perfect square":**
1. Prime factorise N.
2. Identify the primes with **odd** exponents.
3. n = product of exactly those primes.

**Worked example:** Least n such that 1008n is a perfect square.
- 1008 = 2⁴ · 3² · 7
- Odd exponent: 7 only ⟹ n = **7** (1008 × 7 = 7056 = 84²)

**With an added divisibility condition:** "Find the least n such that 1008n is a perfect square **and** n is divisible by 6."
- Bare requirement: n must contain 7 to an odd power.
- Must also contain 2 and 3, and adding them must keep all exponents even ⟹ add 2 and 3 to odd powers too, i.e. n must supply 2¹·3¹ making 1008n have 2⁵·3³ — odd, so bump each to 2²·3² in n: n = 2²·3²·7? Check 1008·(4·9·7) = 2⁴⁺²·3²⁺²·7² = 2⁶3⁴7² ✓ and n = 252 is divisible by 6.
- Answer: **252**

**The general principle:** write down the exponent parity you need, then take the smallest n satisfying *all* constraints simultaneously. Handle each prime independently — the primes never interact.

**Perfect-square facts worth memorising:**
- Squares end only in 0, 1, 4, 5, 6, 9 — never 2, 3, 7, 8
- A perfect square has an **odd** number of factors; every other number has an even number
- Squares are ≡ 0 or 1 (mod 4), and ≡ 0, 1, 4, 7 (mod 9)

That last line kills many questions instantly: if a candidate is ≡ 2 (mod 4), it cannot be a square.

---

## 10a. Reading N's structure back from its factor count

§10 runs forwards: given N, decide whether it is a perfect power. This is the **reverse** question, and CAT asks it more often — *given only the number of factors, could N be a perfect square / cube / sixth power?*

**Core idea.** N is a perfect k-th power ⟺ every prime exponent aᵢ is a multiple of k ⟺ every (aᵢ + 1) ≡ **1 (mod k)**.

The factor count F = ∏(aᵢ + 1) (§3) is therefore a product of numbers all ≡ 1 (mod k), so **F itself must be ≡ 1 (mod k)**.

| N is a… | every (aᵢ + 1) is | so F must be |
|---|---|---|
| perfect square | odd | odd |
| perfect cube | ≡ 1 (mod 3) | ≡ 1 (mod 3) |
| square **and** cube | ≡ 1 (mod 6) | ≡ 1 (mod 6) |

"Both a perfect square and a perfect cube" always means **perfect sixth power** — exponents divisible by lcm(2,3) = 6.

**Method:**
1. Reduce F mod k. If F ≢ 1 (mod k), it is impossible — stop there.
2. If F ≡ 1 (mod k), it is achievable: take the single-prime shape N = p^(F−1), whose exponent F − 1 is divisible by k by construction. So for a *possibility* question, step 1 is the whole answer.

**Worked example:** The factor counts of P, Q, R, S are 25, 36, 49, 64. How many of these can be both a perfect square and a perfect cube?

- Need F ≡ 1 (mod 6).
- 25 ≡ 1 ✓ — take a + 1 = 25, so N = p²⁴, and 24 is a multiple of 6 ✓
- 36 ≡ 0 ✗ — the only divisor of 36 that is ≡ 1 (mod 6) is 1, and 1's cannot multiply to 36
- 49 ≡ 1 ✓ — N = p⁴⁸, and 48 is a multiple of 6 ✓
- 64 ≡ 4 ✗ — same reason as 36
- Answer: **2**

**Companion facts this generalises:**
- Odd factor count ⟺ perfect square — the §10 fact, now just the k = 2 case
- F prime ⟹ N = p^(F−1); only one shape of N is possible
- F = 2 ⟹ N is prime

**Traps:**
- Testing 36 and 64 as "even, so N could be a square". Even F rules out a *square*; the sixth-power test is mod 6, not parity.
- Splitting F into any factorisation. 25 = 5 × 5 is useless here — 5 ≢ 1 (mod 6). Every factor must pass, not just the product.
- Treating "square and cube" as exponents divisible by 2 or by 3. It is 6.

---

## 11. Diophantine equations — integer solutions

**ax + by = c has integer solutions ⟺ gcd(a, b) divides c.**

**Method:**
1. Divide through by gcd(a,b) if possible.
2. Find one solution by inspection (try small values, or use mod arithmetic).
3. **General solution:** x = x₀ + (b/g)t, y = y₀ − (a/g)t for integer t.
4. Apply the constraints (positive, non-negative, bounded) to restrict t.

**Worked example:** Find all positive integer solutions of 5x + 7y = 100.
- One solution by inspection: y = 5 ⟹ 5x = 65 ⟹ x = 13. So (13, 5).
- General: x = 13 + 7t, y = 5 − 5t.
- Positive requires 13 + 7t > 0 and 5 − 5t > 0 ⟹ t < 1 and t > −13/7 ⟹ t ∈ {−1, 0}
- Solutions: **(6, 10) and (13, 5)** — two of them.

**Faster route for counting only:** solve mod the smaller coefficient. 5x + 7y = 100 ⟹ 7y ≡ 100 ≡ 0 (mod 5) ⟹ 2y ≡ 0 (mod 5) ⟹ y ≡ 0 (mod 5) ⟹ y ∈ {5, 10} for positivity. Two solutions. This is usually the fastest method in the exam.

**Counting shortcut:** for ax + by = c with a, b coprime and positive solutions required, the number of solutions is either ⌊c/(ab)⌋ or ⌊c/(ab)⌋ + 1. Here ⌊100/35⌋ = 2. ✓

### Optimising x − y (or any linear expression) under the constraint

Since the solutions lie on a line, **any linear expression in x and y is monotonic in t** — so the optimum is always at an **endpoint** of the allowed t-range. Never test the middle.

**Worked example:** For 5x + 7y = 100 with x, y positive integers, maximise x − y.
- Solutions: (6, 10) and (13, 5) ⟹ x − y = −4 and **8**
- Maximum = **8**, at the extreme t.

**Worked example (larger range):** 3x + 5y = 200, x, y ≥ 0 integers. Maximise x − y.
- x − y is largest when x is largest and y smallest ⟹ y = 1 (need 200 − 5y divisible by 3; y = 1 gives 195/3 = 65 ✓)
- x = 65, y = 1 ⟹ x − y = **64**
- Check y = 0: 200/3 not an integer, so y = 1 is the true minimum.

**Method summary:** to maximise x − y, push x to its largest feasible value; to minimise, push y up. Then step through t (or y) by the smallest legal increment until the divisibility condition is met. Usually one or two steps.

---

## 12. Factorials — highest powers and trailing zeros

**Legendre's formula.** The highest power of a **prime** p dividing n! is

**⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + …**

Keep going until the term is 0. Each term counts the multiples of that power of p, so the multiples of p² get counted twice, which is exactly right.

**Worked example:** The highest power of 3 in 100!
- ⌊100/3⌋ + ⌊100/9⌋ + ⌊100/27⌋ + ⌊100/81⌋ = 33 + 11 + 3 + 1 = **48**

### The highest power of a *composite*

Factor the composite, apply Legendre to each prime, then **divide each exponent by the power it is needed in and take the minimum**. The scarcest prime is the binding constraint.

**Worked example:** The highest power of 12 dividing 50!
- 12 = 2²·3, so 12ᵏ needs 2^(2k) and 3^k.
- Power of 2 in 50! = 25 + 12 + 6 + 3 + 1 = 47 ⟹ 2k ≤ 47 ⟹ k ≤ 23
- Power of 3 in 50! = 16 + 5 + 1 = 22 ⟹ k ≤ 22
- **k = 22** — 3 is the binding prime, not the more numerous 2.

Applying Legendre to 12 directly, as if it were prime, is the standard wrong answer.

### Trailing zeros, in any base

Base-10 trailing zeros are the power of **5** (see §3) — 2s are always in surplus. In a general base b, factor b and use the same minimum rule.

**Worked example:** How many trailing zeros does 100! have in base 6?
- 6 = 2 × 3. Power of 2 in 100! = 50+25+12+6+3+1 = 97; power of 3 = 48.
- min(97, 48) = **48 zeros**

**Worked example:** Trailing zeros of 100! in base 12 (= 2²·3): min(⌊97/2⌋, 48) = min(48, 48) = **48**.

**Two facts CAT builds questions on:**
- The trailing-zero count **skips values**. No factorial ends in exactly 5 zeros — 24! has 4 and 25! jumps to 6, because 25 contributes two 5s. "For how many n does n! end in exactly k zeros" is answered by that jump structure: the answer is 5 or 0.
- **n! is never a perfect square for n > 1** (Bertrand: there is always a prime between n/2 and n, appearing to the first power).

---

## 13. Base systems

A number written in base b uses digits **0 to b − 1** only. So a numeral containing a 7 must be in base 8 or higher — a one-line elimination that answers several questions outright.

**Value:** (dₖ…d₁d₀)_b = dₖbᵏ + … + d₁b + d₀

**Decimal → base b:** divide repeatedly by b and read the remainders **bottom to top**.

**Worked example:** Write 156 in base 7.
- 156 ÷ 7 = 22 r **2**; 22 ÷ 7 = 3 r **1**; 3 ÷ 7 = 0 r **3**
- Reading upwards: **(312)₇**. Check: 3(49) + 1(7) + 2 = 147 + 7 + 2 = 156 ✓

**Base b → decimal:** expand positionally. (245)₇ = 2(49) + 4(7) + 5 = **131**.

**Between two non-decimal bases:** go through decimal unless one base is a power of the other. Base 2 → base 8 groups the binary digits in **threes**, base 2 → base 16 in **fours**, from the right — no arithmetic needed.

### Arithmetic inside a base

Add and multiply exactly as in decimal, but **carry at b instead of 10**.

**Worked example:** (34)₅ + (23)₅
- Units: 4 + 3 = 7 = 5 + 2 ⟹ write **2**, carry 1
- Next: 3 + 2 + 1 = 6 = 5 + 1 ⟹ write **1**, carry 1 ⟹ leading **1**
- Result **(112)₅**. Check: 19 + 13 = 32, and 1(25) + 1(5) + 2 = 32 ✓

### Divisibility and digit sums in base b

In base b, **(b − 1) plays the role that 9 plays in base 10** — because b ≡ 1 (mod b−1), a number is congruent to its digit sum mod (b − 1). So in base 8 the digit sum tests divisibility by 7; in base 16, by 15. Likewise b + 1 plays the role of 11, via the alternating digit sum. This is §2 and §7 generalised.

**Number of digits** of N in base b = ⌊log_b N⌋ + 1 (`Logarithms.md` §3).

**Traps:**
- A digit ≥ the base. (49)₇ is not a valid numeral.
- Reading the remainders top-down. They come out least-significant first.
- Applying Legendre's formula to a composite directly.
- Assuming trailing zeros in base b equal those in base 10.
- Forgetting that b = 1 and negative digits do not exist; the smallest usable base is 2.

---

## 13a. Repunits and digit-pattern numbers

**Core idea.** A **repunit** Rₓ is the number made of x ones — 1, 11, 111, …. Every digit-pattern number is a geometric series in disguise, and one identity converts it:

**Rₓ = 111…1 (x ones) = (10ˣ − 1)/9**

The same move covers the family: 222…2 = 2·Rₓ, and 999…9 = 10ˣ − 1.

**Method:** replace the pattern by its closed form *before* doing anything else. A sum over x then becomes an ordinary GP (`Progressions-AP-GP.md` §5).

**Worked example:** f(x) = 10ˣ − Rₓ, where Rₓ is the x-digit repunit. Find Σ(x = 1 to 10) f(x).

- f(x) = 10ˣ − (10ˣ − 1)/9 = (9·10ˣ − 10ˣ + 1)/9 = **(8·10ˣ + 1)/9**
- Σ 10ˣ for x = 1…10 is a GP with first term 10: 10(10¹⁰ − 1)/9 = 11,111,111,110
- Σ f(x) = [8 × 11,111,111,110 + 10] / 9 = 88,888,888,890 / 9 = **9,876,543,210**

The answer coming out as the digits 9 down to 0 in order is a strong signal nothing slipped.

**Facts worth carrying:**
- R_d divides Rₓ whenever d divides x (so R₆ is divisible by R₂ = 11 and R₃ = 111)
- **Rₓ can be prime only if x is prime** — the converse fails: R₅ = 11111 = 41 × 271
- The digit sum of Rₓ is x, so 3 | Rₓ ⟺ 3 | x and 9 | Rₓ ⟺ 9 | x (§2)
- 10ˣ − 1 is a string of x nines: always divisible by 9, and by 11 when x is even

**Traps:**
- Writing Rₓ as (10ˣ − 1)/10 or 10ˣ/9. Test against R₂ = 11 = (100 − 1)/9 every single time.
- Expanding the sum term by term. Ten terms is short enough to tempt you and long enough to guarantee a slip.
- Off-by-one in the GP. Σ(x = 1 to n) 10ˣ starts at 10, so it is 10(10ⁿ − 1)/9 = 11…10 with n ones, not (10ⁿ − 1)/9.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Divisibility by 12 | check 2 and 6 | check 3 and 4 (coprime factors) |
| Digital root of 0 remainder | 0 | 9 |
| Digit sum vs repeated digit sum | treated as the same | only the repeated one equals N mod 9 |
| "Least n for perfect square" | multiply by N | multiply by the odd-exponent primes only |
| HCF × LCM = product | applied to three numbers | valid for two numbers only |
| Unit digit, exponent ≡ 0 mod 4 | use the 1st term | use the 4th term of the cycle |
| Diophantine optimisation | test all solutions | linear ⟹ optimum at an endpoint |
| Counting 3-digit numbers | allow leading zero | exclude a = 0 |
| Number of factors of a square | even | **odd** — this is the defining property |
| Factor count and perfect powers | check parity of F | perfect k-th power needs F ≡ 1 (mod k) |
| Equation in exponents | one equation for the whole thing | one equation per prime |
| Repunit Rₓ | (10ˣ − 1)/10 | (10ˣ − 1)/9 — check against R₂ = 11 |

---

## Practical exam habits

- Prime factorise before doing anything else. Nine times in ten, the factorisation *is* the solution.
- For any "remainder when divided by p" question, first check whether the base is ≡ ±1 mod p. If it is, you're done in one line.
- Use the digital root as a free error check on any large multiplication or addition.
- For counting questions with digit constraints, translate to an equation and use stars-and-bars rather than listing.
- If a question mentions "least" or "smallest", you're almost certainly in prime-exponent-parity or Diophantine territory.

**Where this feeds forward:** `PnC-Probability.md` (stars-and-bars counting), `Algebra.md` (surd manipulation, symmetric identities), `Progressions-AP-GP.md` (counting terms in a range).
