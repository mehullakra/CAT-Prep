# Ratio, Proportion & Variation

> CAT quant. Ratios let you replace unknowns with a single variable k. Most "hard" questions here are easy once the right thing is called k.

---

## 1. The core idea

A ratio a : b is the fraction a/b. It carries **relative** size only — never absolute size.

**The k-trick, which is the whole topic:** if a : b : c = 3 : 4 : 5, write a = 3k, b = 4k, c = 5k. Three unknowns collapse to one. Every ratio problem should start this way.

Corollary: ratios are unit-free, so both terms must be in the *same* unit before you form the ratio. Mixing ₹ with paise or hours with minutes is the most common careless error in the topic.

---

## 2. Basic manipulations

For a : b,

| Operation | Effect |
|---|---|
| Multiply both terms by same k | ratio unchanged |
| Add same number to both terms | ratio moves **towards 1 : 1** |
| Subtract same number from both | ratio moves **away from 1 : 1** |

That second row is a genuine shortcut. If 3 : 5 becomes (3+x) : (5+x), the new ratio is always closer to 1. If an option is further from 1, eliminate it without computing.

**Duplicate ratios** (occasionally asked by name):
- Duplicate of a : b = a² : b²
- Sub-duplicate = √a : √b
- Triplicate = a³ : b³
- Inverse = b : a

---

## 3. Combining ratios

Given A : B = 2 : 3 and B : C = 4 : 5, find A : B : C.

Make B common — LCM of 3 and 4 is 12:
- A : B = 8 : 12
- B : C = 12 : 15
- **A : B : C = 8 : 12 : 15**

**Shortcut for two ratios** a:b and c:d → ac : bc : bd. Here 2·4 : 3·4 : 3·5 = 8 : 12 : 15. ✓

For three or more chained ratios, just extend the LCM method one link at a time. Don't try to do it in one step.

---

## 4. Proportion

a : b = c : d, written a : b :: c : d.

- **Cross-product rule:** ad = bc. This is all you need for most questions.
- a and d are **extremes**, b and c are **means**.
- **Mean proportional** between a and b = √(ab) (geometric mean).
- **Third proportional** to a, b: a : b = b : x ⟹ x = b²/a.
- **Fourth proportional** to a, b, c: a : b = c : x ⟹ x = bc/a.

**Continued proportion:** a : b = b : c ⟹ b² = ac ⟹ a, b, c are in GP.

---

## 5. Componendo and dividendo

If a/b = c/d, then:

- **Componendo:** (a+b)/b = (c+d)/d
- **Dividendo:** (a−b)/b = (c−d)/d
- **Componendo–dividendo:** **(a+b)/(a−b) = (c+d)/(c−d)**

The third one is the useful one. It turns messy algebra into one line.

**Worked example:** If (3x + 2y)/(3x − 2y) = 7/3, find x : y.

- Treat 3x = a, 2y = b. Then (a+b)/(a−b) = 7/3.
- Reversing componendo–dividendo: a/b = (7+3)/(7−3) = 10/4 = 5/2.
- So 3x/2y = 5/2 ⟹ 6x = 10y ⟹ x : y = **10 : 6 = 5 : 3**

**Reverse form worth memorising:** if (a+b)/(a−b) = m/n, then a/b = (m+n)/(m−n).

---

## 6. Type 1 — Ratio changes after adding/removing

**Worked example:** The ratio of boys to girls in a class is 5 : 3. If 10 more girls join, the ratio becomes 5 : 4. Find the original number of boys.

- Boys = 5k, Girls = 3k
- 5k / (3k + 10) = 5/4 ⟹ 20k = 15k + 50 ⟹ k = 10
- Boys = **50**, girls originally 30.

**Key point:** the quantity that *doesn't* change (boys here) must keep the same k. If both change, you need two equations.

**Age problems are this exact structure.** "Ratio of ages is 4:3 now, will be 5:4 in 6 years" — add the same number to both terms, solve for k. Note ages move the ratio towards 1:1, consistent with §2.

---

## 7. Type 2 — Dividing a sum in a ratio

Divide ₹X in ratio a : b : c → shares are X·a/(a+b+c), etc.

**Worked example:** ₹5,600 divided among A, B, C such that A : B = 2 : 3 and B : C = 4 : 5.

- Combine: A : B : C = 8 : 12 : 15, sum = 35
- Each part = 5600/35 = 160
- A = 1280, B = 1920, C = **2400**

**Inverse ratio division** — "divide in the ratio of the reciprocals": divide ₹X in the inverse ratio 2 : 3 : 4 means using 1/2 : 1/3 : 1/4 = 6 : 4 : 3 (multiply by LCM 12). Common in partnership and work problems.

---

## 8. Type 3 — Variation

| Type | Statement | Equation |
|---|---|---|
| Direct | a ∝ b | a = kb |
| Inverse | a ∝ 1/b | ab = k |
| Joint | a ∝ bc | a = kbc |
| Combined | a ∝ b/c | a = kb/c |

**Method (use this every time):**
1. Write the proportionality with a constant k.
2. Plug in the given data point to find k.
3. Plug in the new data to get the answer.

**Worked example:** The cost of a diamond varies as the square of its weight. A diamond weighing 10 g costs ₹8,000. It breaks into pieces of weight ratio 2 : 3. Find the loss.

- C = kw², so 8000 = k(100) ⟹ k = 80
- Pieces: 4 g and 6 g ⟹ costs 80(16) = 1280 and 80(36) = 2880 ⟹ total 4160
- Loss = 8000 − 4160 = **₹3,840**

**Generalisation worth knowing:** when something varying as w² breaks in ratio a : b, the loss fraction = 2ab/(a+b)². Here 2·2·3/25 = 12/25 of 8000 = 3840. ✓

**Partial variation:** "a is partly constant and partly varies as b" ⟹ a = m + nb. Two data points give m and n. Fixed-cost-plus-variable-cost questions are always this.

---

## 9. Type 4 — Equal ratios (the k-theorem)

If a/p = b/q = c/r = k, then:

- (a + b + c)/(p + q + r) = k
- More generally (xa + yb + zc)/(xp + yq + zr) = k for any weights

**Worked example:** If a/2 = b/3 = c/4, find (a + b + c)/c.

- a = 2k, b = 3k, c = 4k ⟹ (9k)/(4k) = **9/4**

Any expression that's homogeneous of the same degree in numerator and denominator becomes instantly computable with k. This is the fastest tool for the "if a:b:c = … find the value of …" family.

---

## 10. Type 5 — Ratio in partnership

Profit share ∝ (Capital × Time).

**Worked example:** A invests ₹12,000 for 8 months, B invests ₹9,000 for 12 months. Divide a profit of ₹8,500.

- Ratio = 12000×8 : 9000×12 = 96 : 108 = 8 : 9
- Sum = 17 ⟹ A = 8500 × 8/17 = **₹4,000**, B = 8500 × 9/17 = **₹4,500**

CAT normally picks numbers so the sum of ratio terms divides the total cleanly; an ugly answer usually means you've mis-set the ratio.

**Working vs sleeping partner:** the working partner's salary/commission comes off the top *first*, then the remainder splits by capital×time.

---

## 11. Type 6 — Ratio of ratios (chained comparisons)

If A is to B as 3 : 4 and B is to C as 5 : 6, and someone asks for A : C directly — **do not** just multiply 3×5 : 4×6. First equalise B (LCM 20): A : B = 15 : 20, B : C = 20 : 24 ⟹ A : C = 15 : 24 = 5 : 8.

(Multiplying 3·5 : 4·6 = 15 : 24 happens to give the same answer here, and in fact always does for A : C. But it fails for the three-term A : B : C, which is what's usually asked — so build the chain properly.)

---

## 12. Type 7 — Redistribution and exchange word problems

The shape: two or more people hold amounts in a given ratio; something is transferred; a **new** ratio results. Find the original amounts.

**Method — this is a linear-equations question wearing a ratio costume:**

1. Write the *before* amounts using **one** variable: ak, bk.
2. Apply the transfer literally — what one gains, the other loses.
3. Set the *after* amounts equal to the new ratio, cross-multiply.
4. Solve for k, then answer whichever quantity was asked.

**Worked example:** A and B have money in the ratio 5 : 3. If A gives ₹40 to B, the ratio becomes 3 : 2. Find the original amounts.

- Before: A = 5k, B = 3k
- After: A = 5k − 40, B = 3k + 40
- (5k − 40)/(3k + 40) = 3/2 ⟹ 10k − 80 = 9k + 120 ⟹ k = 200
- A = **₹1,000**, B = **₹600**

**Sanity check:** the total must be unchanged by a transfer. Before 8k = 1600; after 960 + 640 = 1600 ✓. Run this every time — it catches sign errors in one step.

**Worked example (both amounts change independently):** The ratio of A's to B's salary is 4 : 3. A's salary rises by 20% and B's by ₹1,500, after which the ratio is 8 : 7. Find B's original salary.

- Before: A = 4k, B = 3k
- After: A = 4.8k, B = 3k + 1500
- 4.8k/(3k + 1500) = 8/7 ⟹ 33.6k = 24k + 12000 ⟹ 9.6k = 12000 ⟹ k = 1250
- B = 3(1250) = **₹3,750**

**Worked example (three-way transfer):** A, B, C have amounts in the ratio 3 : 4 : 5. A gives ₹30 to B, and B gives ₹50 to C. The final ratio is 2 : 3 : 5. Find the total.

- After: A = 3k − 30, B = 4k + 30 − 50 = 4k − 20, C = 5k + 50
- Use one pair: (3k − 30)/(4k − 20) = 2/3 ⟹ 9k − 90 = 8k − 40 ⟹ k = 50
- Amounts: A = 120, B = 180, C = 300 ⟹ total **₹600**
- **Verify with the unused pair:** B : C = 180 : 300 = 3 : 5 ✓. Total before = 12k = 600 = total after ✓

Note that B both receives and gives — write both movements before forming the equation. Missing one of them is the standard error in three-way transfers.

**The two habits that matter here:**

- **Conservation:** a pure transfer leaves the total constant. An increase/decrease does not. Know which one the question describes.
- **Redundancy check:** with three quantities you get two independent equations from the new ratio but only one unknown k — so the third comparison is a free consistency check. Use it.

---

## 12a. Type 8 — Ratios pinned down by integrality and a range

**The shape:** several people each have income : expenditure in a given ratio; incomes lie in a stated band and are multiples of 100; one extra condition links two of them; and the question asks which value is **impossible**. It reads like a data puzzle and it is really a divisibility exercise.

**Core idea — the ratio plus "both amounts are whole" forces the multiplier.**

If income : expenditure = a : c, write income = ak and expenditure = ck. For the expenditure to be a whole number of rupees when the income is a multiple of 100, you need **a to divide the income** — so the income must be a multiple of **lcm(a, 100)**. That single step usually cuts each person to two or three candidate incomes, and the puzzle becomes finite.

| Ratio a : c | income must be a multiple of | candidates in ₹8,000–₹11,000 |
|---|---|---|
| 7 : 5 | 700 | 8400, 9100, 9800, 10500 |
| 11 : 9 | 1100 | 8800, 9900, 11000 |
| 9 : 8 | 900 | 8100, 9000, 9900, 10800 |
| 13 : 10 | 1300 | 9100, 10400 |

**Method:**
1. List each person's candidate incomes from the divisibility rule and the range.
2. Apply the **linking condition** (here "Jaya spends ₹600 more than Rekha") to the short lists. It normally leaves one pair.
3. Apply the **global condition** ("the highest expenditure is below the lowest income") to prune the rest.
4. Read off which of the offered values survives — and remember a "cannot be" question needs you to show a value is *unreachable*, not merely awkward.

**Worked example:** Hema, Rekha, Jaya and Sushma have income : expenditure of 7 : 5, 11 : 9, 9 : 8 and 13 : 10. Each income is between ₹8,000 and ₹11,000 and is a multiple of ₹100. The highest expenditure is lower than the lowest income. Jaya spends ₹600 more than Rekha. Which of ₹20,200, ₹20,500, ₹20,900 cannot be Hema + Sushma?

- Candidate incomes are the table above; the matching expenditures are
  - Hema (5/7 of income): 6000, 6500, 7000, 7500
  - Rekha (9/11): 7200, 8100, 9000
  - Jaya (8/9): 7200, 8000, 8800, 9600
  - Sushma (10/13): 7000, 8000
- **Link:** Jaya − Rekha = 600. Scanning the two lists, only **9600 − 9000 = 600** works ⟹ Jaya's income **10800**, Rekha's **11000**.
- **Global condition:** the largest expenditure is now Jaya's 9600, so every income must exceed 9600.
  - Hema: 9800 or 10500 (8400 and 9100 are out)
  - Sushma: 10400 only (9100 is out)
- Hema + Sushma ∈ {9800 + 10400, 10500 + 10400} = **{20200, 20900}**
- So **₹20,500 cannot be** the combined income.

**Traps:**
- Skipping the integrality step and treating any multiple of 100 as a valid income. Sushma at 13 : 10 can only be 9100 or 10400 in the whole band — that alone nearly finishes the question.
- Applying "highest expenditure < lowest income" before the linking condition. Do the link first; it fixes the highest expenditure, and only then does the inequality have teeth.
- Comparing each person's own expenditure to their own income. The condition is across all four — the highest expenditure of anyone against the lowest income of anyone.
- Answering "all of the above are possible" from the range alone. The range permits many sums; the constraints do not.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Different units in a ratio | ₹2 : 50 paise = 2 : 50 | convert first → 4 : 1 |
| Adding ratios | 2:3 + 3:4 = 5:7 | ratios don't add; combine via common term |
| Assuming ratio gives actual values | 3:4 means 3 and 4 | means 3k and 4k |
| Inverse variation treated as direct | a = kb | ab = k |
| Ratio of areas from ratio of sides | same ratio | squared ratio (volumes: cubed) |
| Splitting in "inverse ratio 2:3:4" | as 2:3:4 | as 6:4:3 |
| Ratio a : c with whole amounts | any multiple of 100 | income must be a multiple of lcm(a, 100) |

---

## Practical exam habits

- Write everything as k the moment a ratio appears. Solving for k is usually the whole problem.
- For "areas / volumes / costs vary as the square/cube", state the constant explicitly before plugging in — skipping k is where sign and power errors creep in.
- If a question gives a ratio and one absolute value, that value determines k. Find k first, always.
- For variation, verify direction with a sanity check: as b doubles, should a double or halve?

**Where this feeds forward:** `Mixtures-and-Alligation.md` (ratios of quantities), `Time-Work-Pipes-Cisterns.md` (inverse variation of men and days), `Time-Speed-Distance.md` (speed ratios ⟹ inverse time ratios), `Means-and-Weighted-Averages.md` (weights are ratios).
