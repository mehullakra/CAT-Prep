# Logarithms — Practice Sets

> Companion to `14-Logarithms.md`. Hints point to the section of the notes that contains the intended method — read the hint only after you've been stuck for a minute. Answer key with short solutions is at the bottom.
>
> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.
>
> Suggested timing: 1.5 min/question for Sets A–E, and attempt the Mixed Set in one timed block.
>
> **When stuck, go back to the definition.** log_a b = c means a^c = b, and rewriting in exponential form settles most doubts in one line (§1).
>
> Check the domain before you celebrate a root: the argument of every log must be positive and the base must be positive and ≠ 1. Extraneous roots are the main source of lost marks here.

---

## Set A — Definition and evaluation

**A1.** (TITA) Find the value of log₂ 64.

*Hint: §1 — ask what power of 2 gives 64.*

**A2.** (MCQ) log₃ (1/81) equals

- (a) −4
- (b) −3
- (c) 3
- (d) 4

*Hint: §1 — a reciprocal argument gives a negative log.*

**A3.** (TITA) If log_x 27 = 3, find x.

*Hint: §1 — rewrite as x³ = 27. The unknown is the base here, not the argument.*

**A4.** (MCQ) log₈ 32 equals

- (a) 5/3
- (b) 4/3
- (c) 3/2
- (d) 2

*Hint: §2 — put both numbers on base 2 and take the ratio of the exponents.*

**A5.** (TITA) Find the value of log₅ 125 + log₂ 32.

*Hint: §1 — evaluate each term separately; the bases differ, so no law applies across them.*

**A6.** (MCQ) If log₁₀ 2 = 0.3010, then log₁₀ 5 equals

- (a) 0.6990
- (b) 0.6021
- (c) 0.7000
- (d) 0.5000

*Hint: §3 — 5 = 10/2, so use the quotient law.*

---

## Set B — The laws

**B1.** (TITA) Find the value of log₁₀ 8 + log₁₀ 125.

*Hint: §2 — the product law. 8 × 125 is deliberately a power of 10.*

**B2.** (MCQ) log₁₀ 45 − log₁₀ 9 + log₁₀ 2 equals

- (a) 0
- (b) 1
- (c) 2
- (d) log₁₀ 8

*Hint: §2 — combine into a single log of one fraction before evaluating.*

**B3.** (TITA) If log₂ x = 5, find log₈ x (as a fraction).

*Hint: §2, change of base — log₈ x = log₂x / log₂8.*

**B4.** (MCQ) The value of log₂ 3 × log₃ 4 × log₄ 8 is

- (a) 2
- (b) 3
- (c) 4
- (d) 6

*Hint: §2 — a chain of change-of-base factors telescopes: the intermediate bases cancel.*

**B5.** (TITA) Given log₁₀ 2 = 0.3010 and log₁₀ 3 = 0.4771, find log₁₀ 12 to four decimal places.

*Hint: §2 — factorise 12 as 2² × 3, then use the product and power laws.*

**B6.** (MCQ) If log_a b = 3, then log_b a equals

- (a) 3
- (b) 1/3
- (c) −3
- (d) −1/3

*Hint: §2 — swapping base and argument takes the reciprocal, not the negative.*

---

## Set C — Equations that reduce to quadratics

**C1.** (TITA) Solve (log₂ x)² − 3 log₂ x + 2 = 0 and give the sum of the roots in x.

*Hint: §4 — substitute t = log₂ x, solve for t, then convert back. The question asks for x, not t.*

**C2.** (MCQ) If (log₁₀ x)² − 5 log₁₀ x + 6 = 0, the product of the roots in x is

- (a) 5
- (b) 6
- (c) 10⁵
- (d) 10⁶

*Hint: §4 — the roots in x multiply to 10^(sum of the t values).*

**C3.** (TITA) Solve log₃ x + log_x 3 = 2. Find x.

*Hint: §4 — the second term is the reciprocal of the first, so set t = log₃ x and use t + 1/t.*

**C4.** (MCQ) If log₂ x + log_x 2 = 5/2, the possible values of x are

- (a) 4 and √2
- (b) 4 and 2
- (c) 2 and √2
- (d) 4 and ½

*Hint: §4 — t + 1/t = 5/2 gives two reciprocal values of t, and both are valid here.*

**C5.** (TITA) If (log₅ x)² = log₅ x + 2, find the sum of all values of x.

*Hint: §4 — t² − t − 2 = 0. A negative value of t is perfectly legal; it gives a fractional x.*

---

## Set D — Nested logs, domains and extraneous roots

**D1.** (TITA) Solve log₂(log₃(log₄ x)) = 0. Find x.

*Hint: §5 — peel one layer at a time from the outside in. Remember log_a 1 = 0.*

**D2.** (MCQ) If log₃(log₂ x) = 1, then x is

- (a) 6
- (b) 8
- (c) 9
- (d) 27

*Hint: §5 — two layers only.*

**D3.** (TITA) Solve log₂(x² − 3x + 4) = 1 and give the sum of the roots.

*Hint: §5 — convert to exponential form, then check that both roots keep the argument positive.*

**D4.** (MCQ) The number of real solutions of log₁₀(x − 1) + log₁₀(x + 1) = log₁₀ 8 is

- (a) 0
- (b) 1
- (c) 2
- (d) infinitely many

*Hint: §6 — combine, solve, then apply the domain condition x > 1. One algebraic root does not survive.*

**D5.** (TITA) Solve log₄(x + 3) − log₄(x − 1) = 1. Find x (as a fraction).

*Hint: §5 — the quotient law, then convert. Check x > 1 at the end.*

---

## Set E — Inequalities and digit counting

**E1.** (MCQ) The solution set of log₂ x > 3 is

- (a) x > 8
- (b) 0 < x < 8
- (c) x > 6
- (d) x < 8

*Hint: §7 — a base greater than 1 preserves the direction of the inequality.*

**E2.** (TITA) How many digits does 2¹⁰⁰ have? (Take log₁₀ 2 = 0.3010.)

*Hint: §3 — the number of digits is ⌊n log₁₀ 2⌋ + 1.*

**E3.** (MCQ) The solution set of log_(1/2) x > 2 is

- (a) 0 < x < 1/4
- (b) x > 1/4
- (c) x > 4
- (d) 0 < x < 4

*Hint: §7 — a base between 0 and 1 flips the inequality. Don't forget x > 0.*

**E4.** (TITA) Find the number of digits in 3⁵⁰. (Take log₁₀ 3 = 0.4771.)

*Hint: §3 — same rule as E2.*

**E5.** (MCQ) The characteristic of log₁₀ 0.00456 is

- (a) −4
- (b) −3
- (c) 3
- (d) 4

*Hint: §3 — write the number in scientific notation; the power of 10 is the characteristic.*

---

## Mixed Set — exam feel (15 minutes)

**M1.** (TITA) Find log₉ 27.

**M2.** (MCQ) If log₁₀ x = 2.5, then x equals

- (a) 25
- (b) 250
- (c) 316.23
- (d) 500

**M3.** (TITA) Simplify log₂ 8 + log₃ 9 − log₅ 25.

**M4.** (MCQ) The value of log₂ 5 × log₅ 8 is

- (a) 2
- (b) 3
- (c) 5
- (d) 8

**M5.** (TITA) Solve log₃(x − 2) = 2. Find x.

**M6.** (MCQ) Given log₁₀ 2 = 0.3010, the number of digits in 2⁶⁴ is

- (a) 19
- (b) 20
- (c) 21
- (d) 64

**M7.** (TITA) If (log₂ x)² − 4 log₂ x + 3 = 0, find the product of the roots in x.

**M8.** (MCQ) The value of 1/log₂ 30 + 1/log₃ 30 + 1/log₅ 30 is

- (a) 0
- (b) 1
- (c) 2
- (d) 30

**M9.** (TITA) Solve log₅(x + 1) + log₅(x − 3) = 1. Find x.

**M10.** (MCQ) If a, b, c are in GP, then log a, log b, log c are in

- (a) AP
- (b) GP
- (c) HP
- (d) no particular progression

---

# Answer key

## Set A

**A1 — 6.** 2⁶ = 64 ⟹ **6**.

**A2 — (a) −4.** 1/81 = 3⁻⁴ ⟹ **−4**.

**A3 — 3.** x³ = 27 ⟹ x = **3**.

**A4 — (a) 5/3.** log₈ 32 = log₂32/log₂8 = 5/3 ⟹ **5/3**.

**A5 — 8.** 3 + 5 = **8**.

**A6 — (a) 0.6990.** log 5 = log 10 − log 2 = 1 − 0.3010 = **0.6990**.

## Set B

**B1 — 3.** log(8 × 125) = log 1000 = **3**.

**B2 — (b) 1.** log(45 × 2/9) = log 10 = **1**.

**B3 — 5/3.** log₈ x = 5/3 ⟹ **5/3** (x = 32 = 8^(5/3) ✓).

**B4 — (b) 3.** The chain collapses to log₂ 8 = **3**.

**B5 — 1.0791.** 2(0.3010) + 0.4771 = **1.0791**.

**B6 — (b) 1/3.** log_b a = 1/log_a b = **1/3**.

## Set C

**C1 — 6.** t² − 3t + 2 = 0 ⟹ t = 1 or 2 ⟹ x = 2 or 4 ⟹ sum = **6**. (Answering 3 gives the sum of the t values.)

**C2 — (c) 10⁵.** t = 2 or 3 ⟹ x = 100 or 1000 ⟹ product = **10⁵**.

**C3 — 3.** t + 1/t = 2 ⟹ t = 1 ⟹ x = **3**.

**C4 — (a) 4 and √2.** t = 2 or ½ ⟹ x = 2² or 2^½ ⟹ **4 and √2**.

**C5 — 25.2.** t = 2 or −1 ⟹ x = 25 or 1/5 ⟹ sum = **25.2**.

## Set D

**D1 — 64.** log₃(log₄ x) = 1 ⟹ log₄ x = 3 ⟹ x = 4³ = **64**.

**D2 — (b) 8.** log₂ x = 3 ⟹ x = **8**.

**D3 — 3.** x² − 3x + 4 = 2 ⟹ x² − 3x + 2 = 0 ⟹ x = 1 or 2 ⟹ sum = **3**. Both are valid (the argument equals 2 in each case).

**D4 — (b) 1.** x² − 1 = 8 ⟹ x = ±3, but x = −3 makes log(x − 1) undefined ⟹ **1 solution** (x = 3).

**D5 — 7/3.** (x + 3)/(x − 1) = 4 ⟹ 3x = 7 ⟹ x = **7/3**, which satisfies x > 1 ✓

## Set E

**E1 — (a) x > 8.** x > 2³ ⟹ **x > 8**.

**E2 — 31.** 100 × 0.3010 = 30.10 ⟹ ⌊30.10⌋ + 1 = **31 digits**.

**E3 — (a) 0 < x < 1/4.** x < (½)² = ¼ together with x > 0 ⟹ **0 < x < 1/4**.

**E4 — 24.** 50 × 0.4771 = 23.855 ⟹ ⌊23.855⌋ + 1 = **24 digits**.

**E5 — (b) −3.** 0.00456 = 4.56 × 10⁻³ ⟹ characteristic = **−3**.

## Mixed Set

**M1 — 3/2.** log₉ 27 = 3/2 = **1.5**.

**M2 — (c) 316.23.** 100 × 3.1623 = **316.23**.

**M3 — 3.** 3 + 2 − 2 = **3**.

**M4 — (b) 3.** log₂ 8 = **3**.

**M5 — 11.** x − 2 = 9 ⟹ x = **11**.

**M6 — (b) 20.** 64 × 0.3010 = 19.264 ⟹ **20 digits**.

**M7 — 16.** t = 1 or 3 ⟹ x = 2 or 8 ⟹ product = **16** (= 2^(1+3) ✓).

**M8 — (b) 1.** log₃₀2 + log₃₀3 + log₃₀5 = log₃₀ 30 = **1**.

**M9 — 4.** (x + 1)(x − 3) = 5 ⟹ x² − 2x − 8 = 0 ⟹ x = 4 or −2; only **x = 4** satisfies x > 3.

**M10 — (a) AP.** b² = ac ⟹ 2 log b = log a + log c ⟹ the logs are in **AP**.

---

**Common error audit** — if you got a question wrong, find it here before moving on:

| Question | The error it is designed to catch |
|---|---|
| A2, A3 | solving for the argument when the base is the unknown, or missing the sign on a reciprocal argument (§1) |
| A4, B3, B4, M4 | not converting to a common base before combining (§2) |
| A6, B1, B2, B5 | applying a law across logs with different bases, which is not permitted |
| B6 | negating instead of reciprocating when base and argument swap |
| C1, C2, C5, M7 | reporting the answer in t when the question asks for x (§4) |
| C3, C4 | missing the second reciprocal root of t + 1/t = k |
| D1, D2 | peeling the nested logs from the inside out instead of the outside in (§5) |
| D4, M9 | keeping an algebraic root that violates the domain (§6) |
| E1, E3 | not flipping the inequality when the base lies between 0 and 1 (§7) |
| E2, E4, M6 | forgetting the +1 in the digit-count rule (§3) |
| E5 | reading the characteristic of a number below 1 as one unit too negative |
| M10 | not recognising that logs convert a GP into an AP (§8) |
