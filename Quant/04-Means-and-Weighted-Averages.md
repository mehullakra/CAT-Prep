# Means & Weighted Averages

> CAT quant. Averaging is easy; averaging *correctly* is the test. The only real question in this topic is "what are the weights?"

---

## 1. The core idea

Average = Sum / Count. Rearranged: **Sum = Average × Count**.

Work with sums, not averages. The moment a question involves a change in the group, convert to totals, adjust, and convert back. Trying to manipulate averages directly is where errors come from.

**Second idea: deviation method.** Pick a convenient reference value A. Then

Average = A + (mean of the deviations from A)

For 68, 71, 74, 69, 73: take A = 70, deviations are −2, +1, +4, −1, +3 ⟹ sum 5 ⟹ mean = 70 + 5/5 = **71**. Far faster than adding four-digit numbers, and it's how you should do every average in the exam.

---

## 2. Properties worth using

- Add a constant c to every term ⟹ average increases by c.
- Multiply every term by c ⟹ average multiplies by c.
- The average of any set lies **between** its minimum and maximum. (Instant option elimination.)
- **Sum of deviations from the mean is always zero.** This is the basis of every "replacement" shortcut below.
- Average of consecutive integers (or any AP) = (first + last)/2 = the middle term.

---

## 3. Weighted average — the central formula

**Weighted average = (w₁x₁ + w₂x₂ + … ) / (w₁ + w₂ + … )**

The plain average is the special case where all weights are equal.

**The single most common mistake in CAT quant** is taking a plain average of things that need weighting: percentages, rates, speeds, profit margins, densities. If the underlying groups have different sizes, the plain mean is wrong.

**Worked example:** A class of 40 boys averages 60 marks; 20 girls average 75. Class average?

- Wrong: (60 + 75)/2 = 67.5
- Right: (40×60 + 20×75)/60 = (2400 + 1500)/60 = **65**

Sanity check: more boys than girls, so the answer must sit closer to 60 than to 75. 65 does. ✓ Run this check on every weighted average.

---

## 4. Weighted average = alligation, backwards

Given the two group values and the blend, alligation recovers the ratio of weights. Given the ratio and values, weighted average gives the blend. Same equation, two directions.

- **Forward (weighted average):** know weights → find mean
- **Backward (alligation):** know mean → find weights

**Worked example (backward):** Boys average 60, girls average 75, class averages 65. Ratio of boys to girls?
- Distances: 75 − 65 = 10, 65 − 60 = 5
- Boys : Girls = 10 : 5 = **2 : 1** ✓ (matches §3)

Full treatment of the cross in `05-Mixtures-and-Alligation.md` §2.

---

## 5. Type 1 — Replacement problems

When one member of a group is replaced, the change in the **total** equals the change in average × number of members.

**Worked example:** The average weight of 8 people increases by 2.5 kg when a new person replaces one weighing 65 kg. Weight of the new person?

- Total increase = 8 × 2.5 = 20 kg
- New person = 65 + 20 = **85 kg**

**The general rule:** new value = old value ± (n × change in average). No algebra needed.

**Variant — adding rather than replacing:** if adding one member changes the average of n members from A to A′, the new member's value = (n+1)A′ − nA.

**Worked example:** Average of 10 numbers is 20. One more number is added and the average becomes 21. The new number = 11×21 − 10×20 = 231 − 200 = **31**.

Note it's 31, not 21 — the new member must also pull up the other ten. This is the trap.

---

## 6. Type 2 — Correction problems

**Worked example:** The average of 20 numbers was computed as 35, but one number was read as 45 instead of 54. Correct average?

- Total was understated by 9 ⟹ correct average = 35 + 9/20 = **35.45**

Always adjust the *sum* by the error, then divide once.

---

## 7. Type 3 — Average speed (the harmonic mean case)

Average speed = Total distance / Total time. **Never** the average of the speeds.

- **Equal distances, two speeds:** average speed = 2ab/(a+b) — the harmonic mean.
- **Equal times, two speeds:** average speed = (a+b)/2 — the arithmetic mean.

**Worked example:** A man travels from A to B at 40 km/h and returns at 60 km/h. Average speed?
- Equal distances ⟹ 2(40)(60)/100 = **48 km/h**, not 50.

**Worked example:** A man drives at 40 km/h for 2 hours and 60 km/h for 2 hours. Average speed?
- Equal times ⟹ (40 + 60)/2 = **50 km/h**

Same numbers, different answers. The question hinges on whether distance or time is equal — read for it explicitly.

For three equal distances at a, b, c: average = 3/(1/a + 1/b + 1/c).

*Kept here because average-speed items appear in averages sets. The full treatment, including multi-sector journeys and unequal legs, is in `08-Time-Speed-Distance.md` §3 and §3b.*

---

## 8. The three means — AM, GM, HM

For two positive numbers a and b:

| Mean | Formula | Use case |
|---|---|---|
| AM | (a+b)/2 | totals, equal weights |
| GM | √(ab) | growth rates, ratios, multiplicative processes |
| HM | 2ab/(a+b) | rates over a fixed quantity (speed, work) |

**AM ≥ GM ≥ HM**, with equality only when a = b. This inequality is itself a CAT tool — many "find the minimum value" questions are AM–GM in disguise.

**Also true for two numbers: GM² = AM × HM.**

**Classic AM–GM application:** for positive x, x + 1/x ≥ 2, since AM ≥ GM gives (x + 1/x)/2 ≥ √(x·1/x) = 1. Minimum is 2, attained at x = 1.

**Worked example:** If a + b = 20 and a, b > 0, find the maximum of ab.
- AM ≥ GM ⟹ 10 ≥ √(ab) ⟹ ab ≤ 100, maximum **100** at a = b = 10.

**General principle:** for a fixed sum, the product is maximised when the terms are equal. For a fixed product, the sum is minimised when the terms are equal. Almost every maxima–minima question in CAT arithmetic reduces to one of these two.

---

## 9. Type 4 — When to use GM: average growth rate

If a quantity grows by 20% one year and 50% the next, the average annual growth is **not** 35%.

- Factors: 1.2 and 1.5 ⟹ total 1.8
- Average factor = √1.8 ≈ 1.3416 ⟹ **≈ 34.16% per year**

CAGR is exactly this: the geometric mean of the annual growth factors. Whenever the quantities *multiply* rather than add, the correct mean is geometric.

---

## 10. Type 5 — Averages of AP-like sequences

- First n natural numbers: average = (n+1)/2
- First n odd numbers: sum = n², average = **n**
- First n even numbers: sum = n(n+1), average = **n + 1**
- Squares of first n naturals: average = (n+1)(2n+1)/6
- Any AP: average = (first + last)/2 = middle term (for odd count)

**Worked example:** Average of the first 50 natural numbers = 51/2 = **25.5**

For consecutive integers, the median equals the mean — so questions asking for either are the same question.

---

## 11. Type 6 — Median, mode and when the mean lies

- **Mean:** sensitive to outliers.
- **Median:** middle value when sorted; robust.
- **Mode:** most frequent.

For n even, median = average of the two middle terms.

CAT (especially in LR-DI and reading-based quant) tests whether you notice that a mean can be dragged by one extreme value. If a data set has an obvious outlier and the question asks about "typical", the intended answer involves the median.

**Relationship for a moderately skewed distribution:** Mean − Mode ≈ 3(Mean − Median). Rarely needed, occasionally asked.

---

## 12. Type 7 — Averages with unknown counts

**Worked example:** The average age of a group of people is 30. When 5 people of average age 20 join, the group average becomes 28. Original number of people?

- Let original count = n. Then (30n + 100)/(n + 5) = 28
- 30n + 100 = 28n + 140 ⟹ 2n = 40 ⟹ n = **20**

**Alligation shortcut:** the two groups average 30 and 20, blend is 28 ⟹ ratio = (28−20) : (30−28) = 8 : 2 = 4 : 1 ⟹ original : new = 4 : 1 ⟹ original = 4 × 5 = 20. ✓ Faster, and worth training.

---

## 13. Type 8 — Reconstructing sub-group values from group averages

The reverse direction: you're given the overall average and some of the parts, and asked for a missing part. **Always go through totals.**

**Master relation:** Total = Σ (group size × group average). One unknown, one equation.

**Worked example (missing sub-group average):** A company has 3 departments. Dept A: 10 people averaging ₹40k. Dept B: 15 people averaging ₹50k. The company's 30 employees average ₹46k. Find Dept C's average.
- Company total = 30 × 46 = 1380
- A + B = 400 + 750 = 1150 ⟹ C total = 230 over 5 people ⟹ **₹46k**

**Worked example (missing sub-group size):** A class averages 68. The 12 girls average 80 and the boys average 62. How many boys?
- Alligation on 62 and 80 about 68: boys : girls = (80 − 68) : (68 − 62) = 12 : 6 = **2 : 1**
- Girls = 12 ⟹ boys = **24**

**Worked example (three groups, one unknown, nested):** The average of a group of 50 is 30. A sub-group of 20 averages 24. What does the remaining 30 average?
- Total = 1500; sub-group total = 480 ⟹ remainder = 1020 over 30 = **34**

**Nested-group version — the harder CAT phrasing.** "The average of the first 3 of 5 numbers is 12, and the average of the last 3 is 16. If the third number is 14, find the average of all five."
- First three sum = 36, last three sum = 48; their total = 84, but this counts the **third number twice**
- Sum of all five = 84 − 14 = 70 ⟹ average = **14**

That double-counting correction is the entire question. Whenever two stated groups overlap, add the sums and subtract the overlap once.

**The two-line method to carry away:**
1. Convert every stated average to a **sum**.
2. Add and subtract sums, accounting for any overlap, then divide once at the end.

---

## 13a. Type 9 — When removing a sub-group shifts the average

**The shape:** "the class average drops by 2 if the top 4 (totalling 312) are excluded." There are **two** unknowns — the group size n and the group average A — and each such statement gives exactly one equation. Two statements, and the system is determined.

**Core idea.** Remove k members whose total is S from a group of n averaging A:

**(nA − S)/(n − k) = A + d**

where d is the stated shift (negative if the average drops). Clear the denominator and the **nA terms cancel on both sides**, leaving a linear equation:

**S = kA − d(n − k)**

That cancellation is the whole trick — the awkward product nA never survives, so you are always solving a plain 2 × 2 linear system.

**Method:**
1. Name n and A; write one equation per statement.
2. Solve the linear system for A and n, then get the total nA.
3. Answer via **totals**, never by combining averages.

**Worked example:** Excluding the 4 highest scorers (combined 312) drops the class average by 2. Excluding instead the 6 lowest scorers (combined 258) raises it by 3. What is the average when both groups are excluded?

- Top 4 out: (nA − 312)/(n − 4) = A − 2 ⟹ nA − 312 = nA − 4A − 2n + 8 ⟹ 4A + 2n = 320 ⟹ **2A + n = 160**
- Bottom 6 out: (nA − 258)/(n − 6) = A + 3 ⟹ nA − 258 = nA − 6A + 3n − 18 ⟹ 6A − 3n = 240 ⟹ **2A − n = 80**
- Add: 4A = 240 ⟹ **A = 60**. Subtract: **n = 40**. Total = 2400.
- Both out: (2400 − 312 − 258)/(40 − 4 − 6) = 1830/30 = **61**

**Traps:**
- Adding the two shifts. The shifts sit over *different* denominators and do not combine. (Here −2 + 3 = +1 happens to land on the right answer of 61 — a coincidence of these particular numbers, not a method. Change 312 to 300 and it breaks.)
- Using n − 4 or n − 6 as the final size. Both groups go, so it is n − 10 = 30.
- Averaging the two given averages. Rebuild the total first, every time (§13).
- Reading "drops by 2 points" as a percentage, or as "drops to 2". It is an absolute shift.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Averaging percentages of unequal groups | plain mean | weight by group size |
| Overlapping sub-groups | add both sums | subtract the overlap once |
| Average speed, equal distances | (a+b)/2 | 2ab/(a+b) |
| Average growth over years | arithmetic mean of rates | geometric mean of factors |
| New member's value when average rises | equals the new average | (n+1)A′ − nA |
| Averaging profit percentages | plain mean | weight by cost price |
| Average of averages | average them again | recombine the sums |
| Median assumed equal to mean | always | only for symmetric data |
| Two sub-groups removed | add the two average shifts | shifts have different denominators — solve for n and A |

---

## Practical exam habits

- Convert to sums immediately. Sum = average × count is the workhorse.
- Use the deviation method for any set of similar-sized numbers — it removes almost all arithmetic risk.
- Before answering any weighted average, check the answer sits nearer the heavier group. Three seconds, catches inversion errors.
- Ask "are these things being added, or multiplied?" Added ⟹ AM. Multiplied ⟹ GM. Rates over a fixed quantity ⟹ HM.
- If a question gives you a blend and asks for a ratio, stop and use alligation — it's always faster than setting up an equation.

**Where this feeds forward:** `05-Mixtures-and-Alligation.md` (the backward direction), `02-Percentages.md` (weighting percentages), `08-Time-Speed-Distance.md` (harmonic mean speeds), `07-Simple-Compound-Interest.md` (GM for average growth).
