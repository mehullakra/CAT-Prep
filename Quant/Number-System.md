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

## 12. Base systems and factorials (brief)

- Number in base b: digits are the remainders of repeated division by b.
- Highest power of prime p in n!: ⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + …
- n! is never a perfect square for n > 1.

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

---

## Practical exam habits

- Prime factorise before doing anything else. Nine times in ten, the factorisation *is* the solution.
- For any "remainder when divided by p" question, first check whether the base is ≡ ±1 mod p. If it is, you're done in one line.
- Use the digital root as a free error check on any large multiplication or addition.
- For counting questions with digit constraints, translate to an equation and use stars-and-bars rather than listing.
- If a question mentions "least" or "smallest", you're almost certainly in prime-exponent-parity or Diophantine territory.

**Where this feeds forward:** `PnC-Probability.md` (stars-and-bars counting), `Algebra.md` (surd manipulation, symmetric identities), `Progressions-AP-GP.md` (counting terms in a range).
