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

**When one factor is a dimension, square (or cube) it first.** A linear dimension changing by x% changes area by the *square* of that factor and volume by the *cube* — see `20-Mensuration.md` §2, the scaling rule (linear ×k ⟹ area ×k², volume ×k³). Only then multiply it into the other factors.

**Worked example:** A square's side rises 10% and the paint used is 10% cheaper. Change in painting cost?
- Cost = Area × Rate. Side factor 1.1 ⟹ **area factor 1.1² = 1.21**; rate factor 0.9
- 1.21 × 0.9 = 1.089 → **8.9% costlier**

Answering "no change" because +10% and −10% cancel is the trap: the dimension gets squared before it meets the price cut, so the increase wins.

---

## 5a. An *absolute* change in a dimension — and recovering the dimension from it

§5 handles a dimension changing by a **percentage**. The other half of the family gives an **absolute** change — "the length increases by 1 cm" — and asks what that does to the area, or runs it backwards.

**Core idea.** Adding 1 to the length multiplies the area by (l + 1)/l = 1 + 1/l. So

**adding 1 cm to a side raises the area by exactly 100/l %** — the reciprocal of that side, as a percentage

Read backwards, this is a **free measurement**: a stated percentage area increase tells you the side directly. 12.5% = 1/8 ⟹ that side is 8. 20% = 1/5 ⟹ that side is 5. No algebra at all.

More generally, adding k to a side of length l raises the area by 100k/l %.

**Method:**
1. Convert each stated area-increase percentage to a fraction in lowest terms.
2. The denominator (times k) **is** the corresponding side.
3. Now that you have actual dimensions, answer whatever was asked — perimeter, area, diagonal — with plain arithmetic.

**Worked example:** A rectangle's area rises by 12.5% when its length grows by 1 cm, and by 20% when its breadth grows by 1 cm. By approximately what percentage does the perimeter rise if the length grows by 2 cm and the breadth by 1 cm?

- 12.5% = 1/8 ⟹ **l = 8**; 20% = 1/5 ⟹ **b = 5**
  - (Check: 9 × 5 = 45 vs 40 ⟹ +12.5% ✓; 8 × 6 = 48 vs 40 ⟹ +20% ✓)
- Old perimeter = 2(8 + 5) = 26. New = 2(10 + 6) = 32.
- Increase = 6/26 = 3/13 ≈ 0.2308 ⟹ **≈ 23%**

**Traps:**
- Applying the two percentage rises together to get the area and stopping there. The question asks about the **perimeter**, which is not a percentage question at all once you have l and b.
- Adding 12.5% + 20% in any form. They are increases on different dimensions and never combine additively for the perimeter.
- Using the "square the factor" rule of §5. That is for *proportional* changes; a fixed +1 cm is not proportional, and it affects a long side far less than a short one.
- Assuming the perimeter rises by the same percentage as a side. Perimeter is linear in both, so its percentage rise is a weighted blend — here (2 + 1)/(8 + 5) = 3/13, which is the whole calculation in one line.

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

## 7a. When expenditure is NOT fixed (generalised price–consumption)

Everything above is the special case "expenditure unchanged", where the price and quantity factors are exact reciprocals. The general statement is just the product rule:

**E-factor = P-factor × Q-factor  ⟹  Q-factor = E-factor ÷ P-factor**

Fixed expenditure is only the case E-factor = 1, which collapses this back to the reciprocal table of §4.

**Worked example:** Wheat rises from ₹24/kg to ₹27/kg. By what % must a family cut consumption so that expenditure falls by 21.25%?

- P-factor = 27/24 = 9/8
- E-factor = 1 − 21.25% = 1 − 17/80 = 63/80
- Q-factor = (63/80) ÷ (9/8) = (63/80) × (8/9) = 7/10 → **30% reduction**

Check (assume 100 kg): 100 × 24 = 2400 → 2400 × 0.7875 = 1890 → 1890 ÷ 27 = 70 kg. 100 → 70 ✓

**Method:** write all three as fractions, divide, then read the resulting factor as a change. Never add or subtract the percentages.

Applying the §7 reciprocal shortcut blindly here (price up 1/8 ⟹ consumption down 1/9 = 11.11%) gives the wrong answer, because expenditure is not fixed this time.

Same shape elsewhere: distance-factor = speed-factor × time-factor, work-factor = men-factor × days-factor, area-factor = length-factor × breadth-factor. One identity, four topics.

| Trap | Wrong | Right |
|---|---|---|
| Price up x%, expenditure also changes | use the §4 reciprocal, x/(100+x) | divide E-factor by P-factor |
| "decrease expenditure by 21.25%" | subtract 21.25% from the price rise | multiply by 0.7875 |

## 7b. "n more/fewer items for the same money" — recovering the actual price

§7 answers in percentages. This variant gives you a **count** instead and asks for the rupee price. The bridge is one sentence: **the % change in quantity, applied to the original quantity, equals the given extra count.**

**Method:**
1. Price factor from the stated change (drop of 25% → ×3/4).
2. Quantity factor = its reciprocal, since the money spent is fixed (→ ×4/3).
3. Read the quantity factor as a **change**: ×4/3 means quantity rose by 1/3 of the original.
4. Set that fraction of the original quantity equal to the given count ⟹ original quantity Q.
5. Original price = Money ÷ Q.

**Worked example:** When the price of eggs dropped 25%, 25 more eggs could be bought for ₹30. Find the original price of one egg.

- Price factor = 3/4 ⟹ quantity factor = 4/3
- Quantity rose by 4/3 − 1 = **1/3** of the original
- (1/3)·Q = 25 ⟹ **Q = 75 eggs** originally
- Original price = 30/75 = **₹0.40** (40 paise)
- Check: at ₹0.40 → 75 eggs; new price ₹0.30 → 100 eggs; 25 more ✓

**The direction rule:** the extra count sits on the **original** quantity when the price *falls*, because you're measuring the gain from the old baseline. Price drop of 1/n ⟹ quantity gain of 1/(n−1) of the original (§4's pattern, run backwards).

| Trap | Wrong | Right |
|---|---|---|
| Price drops 25% | quantity rises 25% | rises 33.33% (×4/3) |
| The 25 extra eggs | 25 = 1/4 of Q | 25 = 1/3 of Q |
| Final answer | the quantity 75 | the price 30/75 = ₹0.40 |
| Units | leave it as 40 | question says "in Rs" → 0.40 |

Same skeleton with a rise instead: "price rose 25%, 10 *fewer* items for ₹50" → quantity factor 4/5, fall of 1/5 of the original, so Q = 50.

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

## 9a. Chains with money added back, closed by an equation

Two extensions that turn §9 into a full CAT question.

**First: money coming *in* is also a multiplier.** "X gives him 66.66% of the money in his hand" adds 2/3 of the *current* holding, so the holding goes ×(1 + 2/3) = **×5/3**. Any inflow or outflow stated as a percentage of the current amount is a factor — write it in the same row as the others. Only a *flat* rupee amount breaks the chain and forces an equation mid-way.

**Second: the closing condition gives you the initial amount.** If the final amount is stated in terms of the initial (a square root, a difference, a ratio), set the chain product equal to it and solve.

**Method:**
1. Write every step as a fraction factor in one row. Outflow of 1/n → ×(1 − 1/n). Inflow of m/n of current → ×(1 + m/n).
2. Multiply them into a single factor k, so Final = k·A.
3. Impose the closing condition and solve for A.
4. Back-substitute for whatever specific amount is asked.

**Worked example:** Vinod gives 25% of his money to Suresh, spends 1/3 of the remainder on a ticket, spends 40% of the remainder shopping, then Gita gives him 66.66% of the money in his hand, after which he gives 4/5 of what he holds to his mother. He is left with the square root of his initial amount. How much did Gita give him?

- Factors in a row: 3/4 × 2/3 × 3/5 × 5/3 × 1/5
- Multiply: 3/4 × 2/3 = 1/2; × 3/5 = 3/10; × 5/3 = 1/2; × 1/5 = **1/10**
- So Final = A/10, and the condition says Final = √A:
  A/10 = √A ⟹ √A = 10 ⟹ **A = 100**
- Gita's gift = 2/3 of the holding just before she arrived. That holding is 3/4 × 2/3 × 3/5 = 3/10 of A = 30, so she gave 2/3 × 30 = **₹20**
- Check: 100 → 75 → 50 → 30 → +20 = 50 → gives 40 to mother → left 10 = √100 ✓

**Traps**

| Trap | Wrong | Right |
|---|---|---|
| "gives him 66.66% of the money in his hand" | ×2/3 | ×5/3 (he *keeps* his money and gains 2/3 more) |
| Whose hand "in his hand" means | the giver's money | the receiver's current holding |
| A/10 = √A | A = 10 | √A = 10, so A = 100 |
| The question asked | the initial amount, 100 | Gita's gift, 20 — re-read the last line |

**Why the chain product is worth computing even when you don't need it:** here it collapses to a clean 1/10, which is the signal that the setter chose the percentages to cancel. If your product is ugly, re-check a factor before continuing.

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

## 13. Type 7 — Overall % change of a composite (weighted % change)

**Core idea:** when a total is made of parts that change at *different* rates, the overall % change is the **weighted average of the parts' % changes, weighted by their original values** — not the plain average.

Two parts of value V₁ and V₂ changing by a% and b%:

**Overall % = (V₁·a + V₂·b) / (V₁ + V₂)**

This is `04-Means-and-Weighted-Averages.md` §3 applied to percentages; the alligation cross of §4 there works in reverse if you need the ratio of the parts. Note this is *addition* of weighted rates, not multiplication — §5's multiplying factors are for changes applied one after another to the **same** quantity. Different parts → weighted average. Same quantity, repeated → multiply.

### The swap trick

CAT's favourite dressing: give the overall change once, then **swap the two rates** and give it again. Never solve the two equations by substitution — add and subtract them.

With weights V₁ : V₂ = m : n (total m + n), overall changes p% and q% before/after the swap:

- (m·a + n·b) = (m+n)·p
- (m·b + n·a) = (m+n)·q

**Add:** (m+n)(a+b) = (m+n)(p+q) ⟹ **a + b = p + q** (weights vanish)
**Subtract:** (m−n)(a−b) = (m+n)(p−q) ⟹ **a − b = (p−q)·(m+n)/(m−n)**

Sum and difference give a and b in one line each.

**Worked example:** A portfolio holds gold worth 4× the silver. If gold rises a% and silver rises b%, the portfolio rises 7%. If gold rises b% and silver rises a%, it rises 4%. Find a and b.

- Weights 4 : 1, total 5. p = 7, q = 4.
- a + b = 7 + 4 = **11**
- a − b = (7 − 4) × 5/3 = **5**
- ⟹ a = 8, b = 3
- Check: (4×8 + 1×3)/5 = 35/5 = 7 ✓  and (4×3 + 1×8)/5 = 20/5 = 4 ✓

**Traps**

| Trap | Wrong | Right |
|---|---|---|
| Parts changing at different rates | multiply the factors, as in §5 | weighted average of the rates |
| Weights 3 : 1 | overall change is (a+b)/2 | (3a + b)/4 |
| Swap version | substitute and grind | add for a+b, subtract for a−b |
| Final answer "a vs b" | report a − b as the answer | if asked "% more", it's (a−b)/b — see §3 |

---

## Traps, consolidated

| Trap | Wrong | Right |
|---|---|---|
| +20% then −20% | back to original | 4% net loss |
| "A is 20% more than B" reversed | B is 20% less | B is 16.67% less |
| Price up 25%, consumption cut | 25% | 20% |
| Price up, expenditure down by a stated % | treat as the fixed-expenditure case (§7) | use §7a: Q-factor = E-factor ÷ P-factor |
| "20% of the remainder" | 20% of the original | 20% of what's left |
| Rate 20% → 25% | "5% increase" | 5 pp, or 25% increase |
| Averaging two percentages | plain mean | weight by the bases |
| Composite/portfolio changing at two rates | multiply factors (§5) | weighted average of rates (§13) |
| Loss % > 100 | accepted | impossible — recheck |
| "+1 cm raises area by 12.5%" | square the factor | +1 on side l ⟹ +100/l %, so l = 8 |

---

## Practical exam habits

- Assume the unknown base = 100 whenever the question is purely in percentages. If fractions like 1/3 and 1/8 appear, assume the LCM (e.g. 24 or 120) instead.
- Write the multiplying factors in a row before computing anything.
- Convert every percentage to a fraction before multiplying. 87.5% × 64 is painful; 7/8 × 64 = 56 is instant.
- After any percentage-change answer, sanity-check the direction: should the result be bigger or smaller than what you started with?

**Where this feeds forward:** `06-Profit-Loss-Discount.md` (all bases), `07-Simple-Compound-Interest.md` (CI is repeated percentage change), `04-Means-and-Weighted-Averages.md` (averaging percentages correctly), `05-Mixtures-and-Alligation.md` (concentrations).
