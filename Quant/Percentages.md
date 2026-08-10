# Percentages

> CAT quant. The most reused topic in the syllabus — profit & loss, interest, data interpretation and mixtures are all percentages wearing different clothes. Speed here compounds everywhere else.

---

## 1. The core idea

A percentage is a fraction with denominator 100. That's it. Everything else is bookkeeping about **which number is the denominator**.

**The one habit that matters: stop adding and subtracting percentages, start multiplying factors.**

- "increases by 20%" → × 1.2
- "decreases by 25%" → × 0.75
- "increases by 20%, then falls 25%" → × 1.2 × 0.75 = × 0.9 → net 10% fall

Chained changes multiply. They never add. Every trap in this topic comes from someone adding.

---

## 2. Fraction ↔ percentage table — memorise cold

This table is non-negotiable. CAT chooses numbers so these cancel; if you're computing 37.5% of 640 by long multiplication you've already lost 40 seconds.

| Fraction | % | Fraction | % |
|---|---|---|---|
| 1/2 | 50 | 1/9 | 11.11 |
| 1/3 | 33.33 | 1/10 | 10 |
| 1/4 | 25 | 1/11 | 9.09 |
| 1/5 | 20 | 1/12 | 8.33 |
| 1/6 | 16.67 | 1/13 | 7.69 |
| 1/7 | 14.28 | 1/14 | 7.14 |
| 1/8 | 12.5 | 1/15 | 6.67 |
| 1/16 | 6.25 | 1/20 | 5 |

Multiples worth knowing on sight: 2/3 = 66.67, 3/4 = 75, 2/5 = 40, 3/5 = 60, 4/5 = 80, 3/8 = 37.5, 5/8 = 62.5, 7/8 = 87.5, 5/6 = 83.33.

**Use in reverse too.** "16.67% of x" → x/6. "Increase by 12.5%" → × 9/8. Fractions divide cleanly; decimals don't.

---

## 3. Percentage change and the base

Percentage change = (New − Old) / **Old** × 100

The denominator is always the *starting* value. Two questions that sound identical:

- "A is what % more than B?" → base is B → (A − B)/B
- "B is what % less than A?" → base is A → (A − B)/A

**Worked example:** A = 120, B = 100.
- A is 20% more than B (20/100).
- B is 16.67% less than A (20/120 = 1/6).

Same pair of numbers, two different answers. Read the "than" — whatever follows it is the base.

---

## 4. The reciprocal relationship (huge time-saver)

If A is x% more than B, then B is less than A by:

**x / (100 + x) × 100 %**

And if A is x% less than B, then B is more than A by x/(100 − x) × 100 %.

Rather than memorising the formula, use fractions:

| A more than B by | B less than A by |
|---|---|
| 25% (1/4) | 20% (1/5) |
| 33.33% (1/3) | 25% (1/4) |
| 50% (1/2) | 33.33% (1/3) |
| 100% (1/1) | 50% (1/2) |
| 20% (1/5) | 16.67% (1/6) |

**The pattern:** if the increase is 1/n, the corresponding decrease is 1/(n+1). Learn the pattern, not the formula.

---

## 5. Successive changes

Net factor = (1 ± a/100)(1 ± b/100)…

**Two-change shortcut:** net % change = a + b + ab/100 (signs included).

**Worked example:** Price rises 20%, then falls 20%.
- Factor = 1.2 × 0.8 = 0.96 → **4% net decrease**
- By formula: 20 − 20 − 400/100 = −4 ✓

**The general result:** a rise of x% followed by a fall of x% always gives a net **decrease** of x²/100 %. Never zero. This shows up in profit & loss identically.

---

## 6. Type 1 — Successive changes on population/price

**Worked example:** A town's population increases 10% in year 1, decreases 20% in year 2, increases 30% in year 3. Net change?

- 1.1 × 0.8 × 1.3 = 1.144 → **14.4% increase**

Do it as fractions when possible: 11/10 × 4/5 × 13/10 = 572/500 = 1.144.

**Order-independence:** the factors commute, so the sequence never affects the final answer. If a question asks "does the order matter?", the answer is no.

---

## 7. Type 2 — Price–consumption (product constant)

Expenditure = Price × Quantity. If expenditure is fixed, the two factors are reciprocals.

**Worked example:** Price of sugar rises 25%. By what % must consumption fall to keep expenditure unchanged?

- Price factor = 5/4, so quantity factor must be 4/5 → a fall of 1/5 = **20%**

**Shortcut:** rise of x% ⟹ reduction of x/(100+x) × 100 %. Same reciprocal table as §4 — 25% up means 20% down.

**Reverse version:** price *falls* 20% ⟹ consumption can rise 25% at the same expenditure.

This exact structure reappears as: speed vs time (distance fixed), men vs days (work fixed), length vs breadth (area fixed). Recognise the shape and reuse the table.

---

## 8. Type 3 — Percentage points vs percentage

If a rate moves from 20% to 25%:
- Change in **percentage points** = 5 pp
- **Percentage** change = 5/20 = **25%**

CAT and DI sets exploit this constantly. "Interest rose by 5%" is ambiguous; "rose by 5 percentage points" is not. When a question mixes them, the intended reading is almost always percentage points for rates, percentage for values.

---

## 9. Type 4 — Successive percentage of a remainder

**Worked example:** A man spends 30% of income on rent, 20% of the *remainder* on food, and saves the rest — ₹5,600. Find income.

- After rent: 0.7
- After food: 0.7 × 0.8 = 0.56
- Savings = 0.56 × Income = 5600 ⟹ Income = **₹10,000**

**The trap:** "20% of the remainder" ≠ 20% of income. Track what each percentage sits on. Underline the base word ("remainder", "the rest", "what was left") on first read.

---

## 10. Type 5 — Election, exam and pass-mark problems

**Worked example:** In a two-candidate election, the winner gets 56% of the votes and wins by 1,440 votes. Total votes?

- Winner 56%, loser 44%, gap = 12%
- 12% of T = 1440 ⟹ T = **12,000**

**Pass-mark type:** "A student scores 30% and fails by 20 marks; another scores 40% and gets 10 marks more than the pass mark. Find total marks."
- 0.3T + 20 = pass = 0.4T − 10 ⟹ 0.1T = 30 ⟹ T = **300**, pass mark = 110.

Always convert to an equation on the *total*. Don't chase individual marks.

### Weighted marking schemes — reconstructing the total

The CAT-style version: marks are awarded and deducted at different rates, and you must recover the number of questions or the total marks.

**Method:**
1. Let c = correct, w = wrong, u = unattempted, with **c + w + u = N** (total questions).
2. Score = (marks per correct)·c − (penalty)·w.
3. Two equations, two unknowns — or use the "all-correct benchmark" shortcut below.

**The benchmark shortcut:** if every question were correct the score would be 3N (for +3 marking). Each wrong answer costs the 3 you didn't gain **plus** the 1 penalty = 4 marks. Each unattempted costs 3.

**Worked example:** A test has 100 questions, +3 for correct and −1 for wrong. A student attempts all and scores 160. How many were correct?
- All correct = 300. Each wrong costs 4 ⟹ 300 − 4w = 160 ⟹ w = 35 ⟹ correct = **65**
- Check: 65(3) − 35(1) = 195 − 35 = 160 ✓

**Worked example (with unattempted):** 80 questions, +4 correct, −1 wrong. A student attempts 60 and scores 180.
- All-attempted-correct = 240. Each wrong within the 60 costs 5 ⟹ 240 − 5w = 180 ⟹ w = 12 ⟹ correct = **48**

**Worked example (percentage pass condition):** In an exam of 200 marks with +5 and −2, a student needs 40% to pass. She attempts 50 questions and just passes. How many did she get right?
- Pass mark = 0.4 × 200 = 80
- 5c − 2(50 − c) = 80 ⟹ 7c = 180 ⟹ c = 25.71 — not an integer, so *just* passing is impossible; the smallest integer clearing 80 is c = **26** (score 5·26 − 2·24 = 82)

That last step matters: **the answer must be a whole number of questions.** If your equation gives a fraction, round in the direction the inequality demands and state the achievable score. CAT sets these deliberately.

**The trap:** "total marks" and "total questions" are different quantities. A 100-question paper marked +3/−1 has a maximum of 300 marks, and a percentage in the question could refer to either. Read which base the percentage sits on — the same base discipline as §3.

---

## 11. Type 6 — Percentage in DI: growth rates

- **Absolute growth** = later − earlier
- **Growth rate** = absolute growth / earlier value
- **CAGR** over n years = (Final/Initial)^(1/n) − 1

For quick DI estimation, don't compute CAGR exactly. If a value roughly doubles in n years, CAGR ≈ 70/n % (rule of 70). Triples ≈ 110/n %.

**Comparing growth rates without dividing:** to compare a/b vs c/d, cross-multiply — ad vs cb. Faster than two divisions and enough for ranking questions.

---

## 12. Percentage of a percentage

"x% of y% of z" = (x/100)(y/100)z. And critically, **x% of y = y% of x**.

**Worked example:** 16% of 25 = 25% of 16 = 4. Instant.

Use this every time one of the two numbers is a friendly fraction — swap them.

---

## Traps, consolidated

| Trap | Wrong | Right |
|---|---|---|
| +20% then −20% | back to original | 4% net loss |
| "A is 20% more than B" reversed | B is 20% less | B is 16.67% less |
| Price up 25%, consumption cut | 25% | 20% |
| "20% of the remainder" | 20% of the original | 20% of what's left |
| Rate 20% → 25% | "5% increase" | 5 pp, or 25% increase |
| Averaging two percentages | plain mean | weight by the bases |
| Loss % > 100 | accepted | impossible — recheck |

---

## Practical exam habits

- Assume the unknown base = 100 whenever the question is purely in percentages. If fractions like 1/3 and 1/8 appear, assume the LCM (e.g. 24 or 120) instead.
- Write the multiplying factors in a row before computing anything.
- Convert every percentage to a fraction before multiplying. 87.5% × 64 is painful; 7/8 × 64 = 56 is instant.
- After any percentage-change answer, sanity-check the direction: should the result be bigger or smaller than what you started with?

**Where this feeds forward:** `Profit-Loss-Discount.md` (all bases), `Simple-Compound-Interest.md` (CI is repeated percentage change), `Means-and-Weighted-Averages.md` (averaging percentages correctly), `Mixtures-and-Alligation.md` (concentrations).
