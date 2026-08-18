# Number System — Practice Sets

> Companion to `Number-System.md`. Hints point to the section of the notes that contains the intended method — read the hint only after you've been stuck for a minute. Answer key with short solutions is at the bottom.
>
> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.
>
> Suggested timing: 1.5 min/question for Sets A–F, and attempt the Mixed Set in one timed block.
>
> **Prime-factorise first, ask the question second.** Factor counts, HCF, LCM, perfect-power conditions and trailing zeroes all fall straight out of the factorisation (§3).
>
> For remainders, look for the small power that is ≡ 1 or ≡ −1. That collapses the exponent immediately (§6).

---

## Set A — Divisibility, factors and factorials

**A1.** (TITA) Find the number of factors of 720.

*Hint: §3 — factorise, then multiply (exponent + 1) across the primes.*

**A2.** (MCQ) The number of even factors of 360 is

- (a) 12
- (b) 16
- (c) 18
- (d) 24

*Hint: §3 — an even factor must take at least one 2, so the exponent of 2 has 3 choices, not 4.*

**A3.** (TITA) Find the sum of all factors of 200.

*Hint: §3 — the sum of factors is the product of the geometric sums over each prime.*

**A4.** (MCQ) The largest 3-digit number divisible by both 8 and 12 is

- (a) 960
- (b) 972
- (c) 984
- (d) 996

*Hint: §4 — divisible by both means divisible by their LCM, which is 24, not 96.*

**A5.** (TITA) How many trailing zeroes does 100! have?

*Hint: §12 — count the 5s, not the 2s, and don't forget that 25, 50, 75 and 100 each contribute an extra one.*

**A6.** (MCQ) The number of factors of 1800 that are perfect squares is

- (a) 4
- (b) 6
- (c) 8
- (d) 12

*Hint: §10 — a perfect-square factor needs every exponent even, so count the even choices for each prime.*

---

## Set B — HCF and LCM

**B1.** (TITA) Find the HCF of 108 and 144.

*Hint: §4 — take the lowest power of each shared prime.*

**B2.** (MCQ) The LCM of two numbers is 495 and their HCF is 5. If their sum is 100, the numbers are

- (a) 45 and 55
- (b) 40 and 60
- (c) 35 and 65
- (d) 25 and 75

*Hint: §4 — the product of the numbers is HCF × LCM. With the sum known, they are the roots of a quadratic.*

**B3.** (TITA) Find the greatest number that divides 43, 91 and 183 leaving the same remainder in each case.

*Hint: §4 — if the remainder is equal but unknown, it cancels in the differences. Take the HCF of the differences.*

**B4.** (MCQ) The least number which, when divided by 5, 6, 7 and 8, leaves remainder 3 in each case is

- (a) 803
- (b) 843
- (c) 863
- (d) 1683

*Hint: §4 — a common remainder means LCM + remainder.*

**B5.** (TITA) Three bells toll at intervals of 9, 12 and 15 minutes. If they toll together at 9:00 a.m., after how many minutes do they next toll together?

*Hint: §4 — simultaneous events recur at the LCM of the intervals.*

**B6.** (MCQ) The HCF of two numbers is 12 and their LCM is 336. If one number is 84, the other is

- (a) 24
- (b) 48
- (c) 56
- (d) 72

*Hint: §4 — HCF × LCM = product of the two numbers.*

---

## Set C — Unit digit and cyclicity

**C1.** (TITA) Find the unit digit of 7¹⁰⁵.

*Hint: §5 — 7 has a cycle of 4: 7, 9, 3, 1. Reduce the exponent modulo 4.*

**C2.** (MCQ) The unit digit of 2⁶⁴ is

- (a) 2
- (b) 4
- (c) 6
- (d) 8

*Hint: §5 — cycle 2, 4, 8, 6. A remainder of 0 means the last entry, not the first.*

**C3.** (TITA) Find the unit digit of 13⁴⁷ × 17²³.

*Hint: §5 — only the unit digits 3 and 7 matter; handle each cycle separately, then multiply.*

**C4.** (MCQ) The unit digit of 1! + 2! + 3! + … + 100! is

- (a) 1
- (b) 3
- (c) 5
- (d) 7

*Hint: §12 — every factorial from 5! onward ends in 0, so only four terms matter.*

**C5.** (TITA) Find the unit digit of 4³⁷³.

*Hint: §5 — 4 has a cycle of length 2: odd powers end in 4, even powers in 6.*

---

## Set D — Remainders

**D1.** (TITA) Find the remainder when 2⁵¹ is divided by 7.

*Hint: §6 — hunt for the small power ≡ 1. Here 2³ = 8 ≡ 1 (mod 7).*

**D2.** (MCQ) The remainder when 15²³ is divided by 16 is

- (a) 1
- (b) 7
- (c) 14
- (d) 15

*Hint: §6 — write 15 as −1 modulo 16. An odd power keeps the sign.*

**D3.** (TITA) Find the remainder when 7¹⁰⁰ is divided by 100.

*Hint: §6 — 7⁴ = 2401 ends in 01.*

**D4.** (MCQ) The remainder when 16! is divided by 17 is

- (a) 0
- (b) 1
- (c) 16
- (d) 17

*Hint: §6 — Wilson's theorem: (p − 1)! ≡ −1 (mod p) for a prime p.*

**D5.** (TITA) A number divided by 296 leaves remainder 75. What remainder does it leave when divided by 37?

*Hint: §6 — 296 is a multiple of 37, so that part vanishes and only the remainder needs reducing.*

**D6.** (MCQ) The remainder when 3⁵⁷ is divided by 8 is

- (a) 1
- (b) 3
- (c) 5
- (d) 7

*Hint: §6 — 3² = 9 ≡ 1 (mod 8), so only the parity of the exponent matters.*

---

## Set E — Perfect squares, cubes and least multipliers

**E1.** (TITA) Find the least positive integer n such that 1176n is a perfect square.

*Hint: §10 — factorise, then supply exactly what is missing to make every exponent even.*

**E2.** (MCQ) The least number by which 8232 must be divided to give a perfect cube is

- (a) 3
- (b) 6
- (c) 7
- (d) 21

*Hint: §10 — for a cube, every exponent must be a multiple of 3. Here you remove rather than add.*

**E3.** (TITA) How many perfect squares lie strictly between 100 and 1000?

*Hint: §10 — find the first and last integer whose square lies in range, then count inclusively.*

**E4.** (MCQ) The smallest number that must be added to 1780 to make it a perfect square is

- (a) 21
- (b) 49
- (c) 69
- (d) 89

*Hint: §10 — locate the nearest squares on either side: 42² and 43².*

**E5.** (TITA) Find the smallest positive integer by which 2925 must be multiplied to become a perfect square.

*Hint: §10 — factorise and look for the lone prime.*

---

## Set F — Integer solutions

**F1.** (TITA) How many solutions in positive integers does 3x + 5y = 100 have?

*Hint: §11 — reduce modulo the smaller coefficient to pin down y, then step by 3.*

**F2.** (MCQ) The number of non-negative integer solutions of 2x + 3y = 30 is

- (a) 5
- (b) 6
- (c) 7
- (d) 11

*Hint: §11 — 3y must be even, so y must be even. Note that here 0 is allowed.*

**F3.** (TITA) If x and y are positive integers satisfying 7x + 11y = 100, find x + y.

*Hint: §11 — reduce modulo 7 to fix y, then check that only one value stays in range.*

**F4.** (MCQ) The number of solutions of x + y + z = 10 in positive integers is

- (a) 28
- (b) 36
- (c) 45
- (d) 66

*Hint: §11 — stars and bars: C(n − 1, r − 1) for positive solutions.*

**F5.** (TITA) Pens cost ₹7 each and notebooks ₹9 each. A man spends exactly ₹62 and buys at least one of each. Find the number of notebooks.

*Hint: §11 — reduce modulo 7 to fix the number of notebooks; the range does the rest.*

---

## Mixed Set — exam feel (15 minutes)

**M1.** (TITA) Find the number of factors of 2520.

**M2.** (MCQ) The unit digit of 3²⁰²⁰ is

- (a) 1
- (b) 3
- (c) 7
- (d) 9

**M3.** (TITA) Find the remainder when 5⁹⁹ is divided by 13.

**M4.** (MCQ) The HCF of 391, 425 and 527 is

- (a) 13
- (b) 17
- (c) 19
- (d) 23

**M5.** (TITA) How many zeroes are at the end of 50!?

**M6.** (MCQ) The least number which when divided by 12, 15 and 20 leaves remainders 5, 8 and 13 respectively is

- (a) 53
- (b) 55
- (c) 60
- (d) 67

**M7.** (TITA) Find the smallest positive integer n such that 720n is a perfect cube.

**M8.** (MCQ) The number of even factors of 2⁴ × 3³ × 5² is

- (a) 36
- (b) 45
- (c) 48
- (d) 60

**M9.** (TITA) The sum of two numbers is 528 and their HCF is 33. How many such pairs of numbers exist?

**M10.** (MCQ) The remainder when 32^(32^32) is divided by 7 is

- (a) 1
- (b) 2
- (c) 4
- (d) 6

---

# Answer key

## Set A

**A1 — 30.** 720 = 2⁴ × 3² × 5 ⟹ (4+1)(2+1)(1+1) = **30 factors**.

**A2 — (c) 18.** 360 = 2³ × 3² × 5 ⟹ even factors = 3 × 3 × 2 = **18**. (Total 24, odd 6, and 24 − 6 = 18 ✓)

**A3 — 465.** 200 = 2³ × 5² ⟹ (1+2+4+8)(1+5+25) = 15 × 31 = **465**.

**A4 — (c) 984.** LCM(8, 12) = 24 ⟹ 999 ÷ 24 = 41 remainder 15 ⟹ 41 × 24 = **984**.

**A5 — 24.** ⌊100/5⌋ + ⌊100/25⌋ = 20 + 4 = **24**.

**A6 — (c) 8.** 1800 = 2³ × 3² × 5². Even exponents: 2 has {0,2}, 3 has {0,2}, 5 has {0,2} ⟹ 2 × 2 × 2 = **8**.

## Set B

**B1 — 36.** 108 = 2²·3³ and 144 = 2⁴·3² ⟹ HCF = 2²·3² = **36**.

**B2 — (a) 45 and 55.** Product = 5 × 495 = 2475 with sum 100 ⟹ x² − 100x + 2475 = 0 ⟹ x = **45 and 55**. (Check: HCF 5, LCM 495 ✓ — the other options fail the HCF test.)

**B3 — 4.** Differences 48, 92 and 140 ⟹ HCF = **4**. (Each of 43, 91, 183 leaves remainder 3 on division by 4 ✓)

**B4 — (b) 843.** LCM(5, 6, 7, 8) = 840 ⟹ answer = 840 + 3 = **843**.

**B5 — 180.** LCM(9, 12, 15) = **180 minutes** (at noon).

**B6 — (b) 48.** 12 × 336 / 84 = **48**. (Check: HCF(84, 48) = 12 ✓)

## Set C

**C1 — 7.** 105 mod 4 = 1 ⟹ the first entry of the cycle ⟹ unit digit **7**.

**C2 — (c) 6.** 64 mod 4 = 0 ⟹ the fourth entry ⟹ unit digit **6**.

**C3 — 1.** 3⁴⁷: 47 mod 4 = 3 ⟹ 7. 7²³: 23 mod 4 = 3 ⟹ 3. Then 7 × 3 = 21 ⟹ unit digit **1**.

**C4 — (b) 3.** 1 + 2 + 6 + 24 = 33 ⟹ unit digit **3**.

**C5 — 4.** 373 is odd ⟹ unit digit **4**.

## Set D

**D1 — 1.** 2³ ≡ 1 (mod 7) and 51 = 3 × 17 ⟹ 2⁵¹ ≡ 1³⁷ ≡ **1**.

**D2 — (d) 15.** 15 ≡ −1 ⟹ (−1)²³ = −1 ≡ **15** (mod 16).

**D3 — 1.** 7⁴ ≡ 1 (mod 100) ⟹ 7¹⁰⁰ = (7⁴)²⁵ ≡ **1**.

**D4 — (c) 16.** 17 is prime ⟹ 16! ≡ −1 ≡ **16** (mod 17). (A remainder can never equal the divisor, which rules out option (d) instantly.)

**D5 — 1.** 296 = 8 × 37 ⟹ N = 296k + 75 ≡ 75 (mod 37), and 75 = 2(37) + 1 ⟹ remainder **1**.

**D6 — (b) 3.** 3⁵⁷ = (3²)²⁸ × 3 ≡ 1 × 3 = **3**.

## Set E

**E1 — 6.** 1176 = 2³ × 3 × 7². The 2 and the 3 have odd exponents ⟹ n = 2 × 3 = **6**. (1176 × 6 = 7056 = 84² ✓)

**E2 — (a) 3.** 8232 = 2³ × 3 × 7³ ⟹ divide by **3** to leave 2744 = 14³.

**E3 — 21.** 11² = 121 through 31² = 961 ⟹ 31 − 11 + 1 = **21**. (100 = 10² and 1024 = 32² are both outside.)

**E4 — (c) 69.** 42² = 1764 and 43² = 1849 ⟹ 1849 − 1780 = **69**.

**E5 — 13.** 2925 = 3² × 5² × 13 ⟹ multiply by **13** (giving 195²).

## Set F

**F1 — 6.** 5y ≡ 100 (mod 3) ⟹ 2y ≡ 1 ⟹ y ≡ 2 (mod 3) ⟹ y = 2, 5, 8, 11, 14, 17 ⟹ **6 solutions**. (y = 20 gives x = 0, which is not positive.)

**F2 — (b) 6.** y ∈ {0, 2, 4, 6, 8, 10} ⟹ **6 solutions**.

**F3 — 12.** 4y ≡ 2 (mod 7) ⟹ y ≡ 4 (mod 7). Only y = 4 keeps 11y below 100 ⟹ x = 8 ⟹ x + y = **12**.

**F4 — (b) 36.** C(9, 2) = **36**. (66 = C(12, 2) is the non-negative count — the planted decoy.)

**F5 — 3.** 2y ≡ 6 (mod 7) ⟹ y ≡ 3 (mod 7). y = 10 already exceeds ₹62 ⟹ y = **3 notebooks** (and 5 pens: 35 + 27 = 62 ✓).

## Mixed Set

**M1 — 48.** 2520 = 2³ × 3² × 5 × 7 ⟹ 4 × 3 × 2 × 2 = **48**.

**M2 — (a) 1.** 2020 mod 4 = 0 ⟹ the fourth entry of 3, 9, 7, 1 ⟹ **1**.

**M3 — 8.** 5⁴ = 625 = 48(13) + 1 ⟹ period 4. 99 mod 4 = 3 ⟹ 5³ = 125 ≡ **8** (mod 13).

**M4 — (b) 17.** 391 = 17 × 23, 425 = 17 × 25, 527 = 17 × 31 ⟹ HCF = **17**.

**M5 — 12.** ⌊50/5⌋ + ⌊50/25⌋ = 10 + 2 = **12**.

**M6 — (a) 53.** 12 − 5 = 15 − 8 = 20 − 13 = 7 ⟹ answer = LCM(12, 15, 20) − 7 = 60 − 7 = **53**.

**M7 — 300.** 720 = 2⁴ × 3² × 5 ⟹ needs 2² × 3 × 5² = **300**. (720 × 300 = 216000 = 60³ ✓)

**M8 — (c) 48.** 4 × 4 × 3 = **48**. (Total 60 minus the 12 odd factors ✓)

**M9 — 4.** a + b = 16 with gcd(a, b) = 1 ⟹ (1,15), (3,13), (5,11), (7,9) ⟹ **4 pairs**.

**M10 — (c) 4.** 32 ≡ 4 (mod 7), and 4 has cycle 4, 2, 1 of length 3. 32³² ≡ 2³² ≡ (−1)³² ≡ 1 (mod 3) ⟹ 4¹ = **4**.

---

**Common error audit** — if you got a question wrong, find it here before moving on:

| Question | The error it is designed to catch |
|---|---|
| A1, A2, A6, M1, M8 | counting factors without first prime-factorising, or forgetting the constraint that makes a factor even or square (§3, §10) |
| A4, B4, B6, M6 | using the product instead of the LCM, or the wrong direction of HCF × LCM = product (§4) |
| A5, M5 | counting 2s instead of 5s, or missing the second-order terms ⌊n/25⌋ |
| B3 | not realising an unknown common remainder cancels in the differences |
| C1, C2, M2 | reading a remainder of 0 as the first entry of the cycle rather than the last (§5) |
| C4 | summing all 100 factorials instead of stopping at 4! |
| D1, D3, D6, M3 | brute-forcing the exponent instead of finding the small power ≡ 1 (§6) |
| D2 | not using the ≡ −1 shortcut, which handles odd exponents in one line |
| D5 | reducing modulo the wrong number — 296 is already a multiple of 37 |
| E1, E2, E5, M7 | adding when the question says divide, or stopping before every exponent is fixed (§10) |
| F1, F2 | confusing positive with non-negative solutions — the endpoints are exactly what differ (§11) |
| F4 | using C(n + r − 1, r − 1) where positive solutions need C(n − 1, r − 1) |
| M9 | forgetting the coprimality condition on the co-factors |
