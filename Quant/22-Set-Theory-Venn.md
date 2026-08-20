# Set Theory & Venn Diagrams

> CAT quant and DI. Every "how many students study both / neither / exactly one" question, plus the maximise-the-overlap questions that look impossible until you notice only one number is actually free. Percentages arrive here constantly — the trick is to stop treating them as percentages.

---

## 1. The core idea

You are not computing. You are **filling in a picture whose totals are already fixed**.

Two things do all the work:

1. **Every element is counted exactly once.** Overlaps get double-counted by naive addition, so you subtract them back out.
2. **Row and column totals are given.** That means far fewer unknowns than the question appears to have — usually exactly one.

Draw the diagram or the grid before writing a single equation. The structure tells you how many degrees of freedom you have, and that number decides whether the question is a computation or an optimisation.

---

## 2. Two sets

**n(A ∪ B) = n(A) + n(B) − n(A ∩ B)**

| Quantity | Expression |
|---|---|
| At least one (union) | n(A) + n(B) − n(A∩B) |
| Both | n(A∩B) |
| Exactly one | n(A) + n(B) − 2·n(A∩B) |
| Only A | n(A) − n(A∩B) |
| Neither | Total − n(A∪B) |

**Note the 2 in "exactly one".** You remove the overlap once to stop double-counting, and a second time to exclude it. Forgetting the second subtraction is the single most common error in this topic.

**Worked example:** Of 100 people, 70 read the Times, 55 read the Express, 20 read neither. How many read both?

- At least one = 100 − 20 = 80
- 80 = 70 + 55 − both ⟹ **both = 45**
- Exactly one = 70 + 55 − 90 = 35. Check: 35 + 45 + 20 = 100 ✓

Always close with that total check. It costs three seconds and catches sign errors.

---

## 3. Three sets

**n(A∪B∪C) = n(A) + n(B) + n(C) − n(A∩B) − n(B∩C) − n(C∩A) + n(A∩B∩C)**

Write ΣS for the sum of the three singles, ΣP for the sum of the three pairwise intersections, and T for the triple intersection.

| Quantity | Expression |
|---|---|
| At least one | ΣS − ΣP + T |
| Exactly one | ΣS − 2·ΣP + 3·T |
| Exactly two | ΣP − 3·T |
| At least two | ΣP − 2·T |
| Exactly three | T |

**The pattern:** each region gets counted a predictable number of times by ΣS and ΣP, and the coefficients above are just the corrections. If you can't recall them, derive from the diagram — the seven regions are quick to label.

**Careful with wording.** n(A∩B) means "in A and B, *whether or not* in C". "In exactly A and B" means n(A∩B) − T. CAT alternates between the two deliberately, so underline "only" and "exactly" on first read.

**Worked example:** In a group of 60, 25 play cricket, 30 play football, 27 play tennis; 12 play cricket and football, 9 football and tennis, 8 cricket and tennis, and 5 play all three. How many play none?

- At least one = (25+30+27) − (12+9+8) + 5 = 82 − 29 + 5 = 58
- None = 60 − 58 = **2**
- Cross-check via regions: exactly one = 82 − 58 + 15 = 39; exactly two = 29 − 15 = 14; exactly three = 5. Total 39+14+5 = 58 ✓

---

## 4. The 2×2 classification table

When elements are split by **two independent yes/no attributes** — male/female × engineer/non-engineer, women/men × above-30/below-30 — a Venn diagram is the wrong tool. Use a grid.

|  | Engineer | Non-engineer | Total |
|---|---|---|---|
| **Male** | a | b | M |
| **Female** | c | d | F |
| **Total** | E | N | T |

**The key structural fact: one interior cell fixes all four.** Given the four margins (M, F, E, N), choosing a forces b = M − a, c = E − a, d = N − b. So a two-attribute question has exactly **one degree of freedom**, no matter how many numbers it quotes.

That single fact decides the question type:

- The question pins that one cell ⟹ pure arithmetic (§5).
- The question only *bounds* it ("at least", "at most") ⟹ optimisation (§6).

**Feasibility bound.** Every cell must be ≥ 0, which constrains any interior cell to

**max(0, R + C − T) ≤ cell ≤ min(R, C)**

where R and C are its row and column totals. This is the same bound as the two-set min/max in §7 — a 2×2 table *is* two sets over a universe. Use it to sanity-check a question before trusting it (see the trap in §5).

---

## 5. Type 1 — Percentages in a 2×2 table (choose the total)

Percentages here are a disguise. **Convert each to a fraction, then set the total to the LCM of the denominators** — every cell comes out a whole number and the arithmetic becomes trivial. The fraction table in `02-Percentages.md` §2 is the lookup you need; awkward-looking decimals are almost always friendly fractions.

Common CAT disguises: 27.27% = 3/11, 28.57% = 2/7, 71.43% = 5/7, 37.5% = 3/8, 87.5% = 7/8, 16.67% = 1/6, 8.33% = 1/12.

**Method:**
1. Rewrite every percentage as a fraction.
2. Total = LCM of the denominators.
3. Fill the four margins, then the one cell the question gives you.
4. Subtract to get the rest.
5. Answer the question — checking which base it wants (`02-Percentages.md` §3).

**Worked example:** In a factory 40% of employees are women and 75% are above 30, of whom half are men. What percentage of the women are above 30?

- 40% = 2/5, 75% = 3/4, and "half of the above-30 group" adds a denominator of 2 ⟹ take T = **40**. Women 16, men 24, above-30 = 30, below-30 = 10.
- Men above 30 = half of 30 = 15 ⟹ women above 30 = 30 − 15 = 15
- As a % of all women: 15/16 = **93.75%**

Take the LCM of *every* denominator in the question, including ones introduced by phrases like "half of whom" — otherwise you land on fractions again and lose the benefit.

Note the base: the question asks % *of the women*, not of the total. Getting 15/40 = 37.5% means you answered a different question.

**The consistency trap — check before you trust.** If a question's numbers force a cell outside the §4 bound, the question is broken, and a wrong answer will still *look* computable. Signal: you get a subset larger than the set containing it, or a percentage above 100 for a "what fraction of" question.

Worked check: "37.5% are women, 87.5% are above 30, of whom 50% are men." Take T = 100: women 37.5, above-30 87.5, so women above 30 = 43.75. But there are only 37.5 women. The bound says this cell must sit in [max(0, 37.5+87.5−100), min(37.5, 87.5)] = **[25, 37.5]**, and 43.75 is outside it. No such factory exists. Say so rather than reporting 43.75/37.5 = 116.67%.

---

## 6. Type 2 — Maximise or minimise a cell ("at least", "at most")

When the question bounds the free cell instead of fixing it, you are optimising over that one degree of freedom.

**Method:**
1. Build the table in whole numbers (§5, steps 1–3).
2. Identify **which cell the constraint acts on** and which cell the question asks about.
3. Because the margins are fixed, those two cells move in opposite directions along the row or column they share. So maximising one means pushing the other to its constrained extreme.
4. Push it there, fill the table by subtraction, and **verify all four cells are ≥ 0**.
5. Compute the requested ratio, on the base the question names.

**Worked example:** In an MBA college, 27.27% of students are male and 28.56% are engineers. At least 71.42% of the male students are non-engineers. What is the maximum value of female non-engineers as a percentage of all non-engineers?

- 27.27% = 3/11, 28.56% ≈ 2/7, 71.42% ≈ 5/7 ⟹ T = LCM(11, 7) = **77**
- Males = 3/11 × 77 = 21, females = 56. Engineers = 2/7 × 77 = 22, non-engineers = 55.

|  | Engineer | Non-engineer | Total |
|---|---|---|---|
| Male | 6 | **15** | 21 |
| Female | 16 | **40** | 56 |
| Total | 22 | 55 | 77 |

- Constraint: male non-engineers ≥ 5/7 × 21 = **15**
- Total non-engineers is fixed at 55, so female non-engineers = 55 − (male non-engineers). To **maximise** the female count, **minimise** the male one ⟹ take it at its floor, 15.
- Female non-engineers = 55 − 15 = 40
- Feasibility: male engineers = 21 − 15 = 6 ≥ 0; female engineers = 22 − 6 = 16 ≥ 0; females 16 + 40 = 56 ✓
- Answer = 40/55 = 8/11 = **72.72%**

**Why the opposite-direction step is the whole question.** "Maximum female non-engineers" sounds like it needs its own optimisation, but the column total is frozen, so it is purely the mirror of "minimum male non-engineers" — and *that* is what the constraint hands you directly. Spotting the mirror turns a two-minute problem into a twenty-second one.

**Directional check:** "at least" on a quantity you want to *subtract* means take its lower bound; "at most" means take its upper bound. Read which side of the subtraction the constrained cell sits on before choosing.

---

## 7. Type 3 — Max and min of an overlap (no table given)

For two sets inside a universe of size T:

- **n(A∩B) is largest** when the smaller set sits entirely inside the larger: max = **min(n(A), n(B))**
- **n(A∩B) is smallest** when the sets are spread as far apart as the universe allows: min = **max(0, n(A) + n(B) − T)**

**Worked example:** In a class of 100, 75 passed Maths and 65 passed English. Range of the number who passed both?

- Max = min(75, 65) = **65** (every English-passer also passed Maths)
- Min = 75 + 65 − 100 = **40**

For three sets, apply it in stages: intersect two, then intersect that result with the third. The minimum of n(A∩B∩C) is max(0, ΣS − 2T) for three sets over universe T.

**Worked example:** Of 100 people, 80 like tea, 70 like coffee, 60 like milk. Minimum who like all three?

- 80 + 70 + 60 − 2(100) = 210 − 200 = **10**

**The reasoning behind the formula (worth holding, since the formula is easy to misremember):** the people *outside* each set number 20, 30 and 40 — at most 90 distinct people fail at least one drink, so at least 10 fail none.

---

## 8. Type 4 — Set questions inside DI caselets

CAT's DI sets often hide a Venn or a 2×2 grid in a table of survey responses. Two habits:

- **Total the rows and columns first.** A missing margin is usually recoverable and often the key.
- **Watch for a third attribute.** If respondents are split by two attributes *and* the caselet mentions a third, you need a 2×2×2 (eight cells) — not a bigger Venn. Build it as two stacked 2×2 tables.

Growth-rate and percentage-share questions on the same caselet are `02-Percentages.md` §11.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| "Exactly one" | n(A) + n(B) − n(A∩B) | n(A) + n(B) − 2·n(A∩B) |
| "n(A∩B)" vs "only A and B" | treat as the same | "only" excludes the triple: n(A∩B) − T |
| Percentages with ugly decimals | long division | convert to fractions, set T = LCM |
| Two independent attributes | draw a Venn diagram | draw a 2×2 grid |
| "At least 71.42% are X" | treat as exactly 71.42% | it's a bound — the question is an optimisation |
| Maximising a cell | optimise it directly | minimise its partner in the fixed row/column |
| Answer asked "as a % of non-engineers" | divide by the total | divide by the non-engineer count |
| A cell that exceeds its row or column total | report the number anyway | the question is inconsistent — check the §4 bound |
| Optimum found | stop | verify every cell is ≥ 0 |

---

## Practical exam habits

- **Draw the grid or the diagram first, always.** Ten seconds of structure prevents the most expensive error in this topic, which is solving for the wrong region.
- **Count the degrees of freedom.** Two attributes with all margins given = one free cell. If you find yourself with two unknowns, you've missed a given.
- Choose the universe as the LCM of the percentage denominators, never 100, unless 100 happens to be that LCM.
- Label regions with letters and fill the **innermost region first** (the triple intersection), then work outwards. Outside-in forces guesswork; inside-out is deterministic.
- Close every problem by summing all disjoint regions back to the total.
- If a subset comes out bigger than its parent set, don't hunt for your arithmetic slip more than once — check whether the question is self-consistent.

**Where this feeds forward:** `02-Percentages.md` (§2 fraction table, §3 which base), `23-PnC-Probability.md` (inclusion–exclusion is the same identity used for counting and for P(A∪B)), `04-Means-and-Weighted-Averages.md` §3 (a 2×2 table's column percentages are a weighted average of its row percentages).
