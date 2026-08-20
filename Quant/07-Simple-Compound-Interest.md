# Simple Interest & Compound Interest

> CAT quant. SI is linear, CI is exponential. Almost every question is about the gap between the two — and that gap has clean closed forms worth memorising.

---

## 1. The core idea

- **Simple interest:** interest is computed on the original principal every year. The interest per year is a **constant**.
- **Compound interest:** interest is computed on principal + accumulated interest. The amount grows by a **constant factor** every year.

That's the entire conceptual content. SI is an AP; CI is a GP.

| | Amount after n years | Interest |
|---|---|---|
| SI | P(1 + rn/100) | Prn/100 |
| CI | P(1 + r/100)ⁿ | P[(1 + r/100)ⁿ − 1] |

**Use the factor form for CI, not the formula.** At 10% for 3 years, the amount is P × 1.1³. Treat it exactly like successive percentage changes (see `02-Percentages.md` §5) — it *is* that.

---

## 2. Terminology to keep straight

- **Principal (P):** the amount borrowed/invested.
- **Amount (A):** P + interest. Questions often give A and ask for P — divide, don't subtract.
- **Rate (r):** per annum unless stated otherwise.
- **CI is never asked directly by "amount"** — read carefully whether the question wants the interest or the total amount. This single misread costs more marks than any formula error in the topic.

---

## 3. Compounding more than once a year

If compounded k times a year at annual rate r for n years:

**A = P(1 + r/(100k))^(nk)**

| Frequency | Rate per period | Number of periods |
|---|---|---|
| Annually | r | n |
| Half-yearly | r/2 | 2n |
| Quarterly | r/4 | 4n |
| Monthly | r/12 | 12n |

**Rule:** more frequent compounding ⟹ larger amount, always. If a question asks which option earns more, half-yearly beats annual without any computation.

**Worked example:** ₹10,000 at 20% p.a. compounded half-yearly for 1 year.
- Rate per half = 10%, periods = 2 ⟹ A = 10000 × 1.1² = **₹12,100**
- Compare with annual compounding: 10000 × 1.2 = ₹12,000. The half-yearly edge is ₹100.

---

## 4. The SI–CI difference formulas (memorise)

For the same P, r, and t:

- **2 years:** CI − SI = P(r/100)²  
- **3 years:** CI − SI = P(r/100)²·(3 + r/100) = P(r²(300 + r))/100³

The 2-year formula is by far the most tested. Derive it once and you'll never forget it: in year 2, CI earns extra interest only on year-1's interest, which is Pr/100. Interest on that = (Pr/100)(r/100) = Pr²/10000.

**Worked example:** The difference between CI and SI on a sum for 2 years at 10% is ₹50. Find the sum.
- P(10/100)² = 50 ⟹ P(0.01) = 50 ⟹ P = **₹5,000**

**Worked example (3 years):** Difference at 5% for 3 years is ₹122. Find P.
- P·(25)(305)/1,000,000 = 122 ⟹ P·7625/1,000,000 = 122 ⟹ P = **₹16,000**

**Also useful:** for 2 years, CI − SI = (SI for 1 year) × r/100. And the difference between the CI of consecutive years = previous year's CI × r/100.

---

## 5. Type 1 — Finding rate or time from amounts

**CI, amounts at two times:** if the amount is A₁ after m years and A₂ after n years (n > m), then

A₂/A₁ = (1 + r/100)^(n−m)

**Worked example:** A sum becomes ₹1,331 in 3 years and ₹1,464.10 in 4 years under CI. Find r.
- 1464.10/1331 = 1.1 ⟹ r = **10%**
- And P = 1331/1.1³ = ₹1,000.

**SI, amounts at two times:** the yearly interest is constant, so
- Interest per year = (A₂ − A₁)/(n − m)
- Then P = A₁ − m × (interest per year)

**Worked example:** Under SI a sum amounts to ₹1,200 in 2 years and ₹1,350 in 5 years.
- Per year = (1350 − 1200)/3 = 50
- P = 1200 − 2(50) = **₹1,100**, r = 50/1100 × 100 = 4.55%

---

## 6. Type 2 — Doubling and multiplying

**Under SI**, if a sum doubles in t years, it triples in 2t years, quadruples in 3t. Interest is linear, so the *added* multiples are evenly spaced.
- Doubling in t years ⟹ rt = 100.

**Under CI**, multiples compound. If a sum doubles in t years, it becomes 4× in 2t, 8× in 3t.
- Becoming n times in t years ⟹ becoming n^k times in kt years.

**Worked example:** A sum doubles in 5 years under CI. In how many years does it become 8 times?
- 8 = 2³ ⟹ 3 × 5 = **15 years**

**Worked example (SI version):** A sum doubles in 5 years under SI. When does it become 8 times?
- Doubling means interest earned = P in 5 years, so P earns P every 5 years.
- 8× means interest = 7P ⟹ 7 × 5 = **35 years**

Getting SI and CI mixed up here is the single most common error in this topic. SI adds, CI multiplies.

**Rule of 72 (estimation for CI):** doubling time ≈ 72/r years. At 8%, about 9 years. Good enough for eliminating options.

---

## 7. Type 3 — Instalments

**Under CI, equal annual instalments of value X to repay a loan P over n years:**

P = X/(1+r) + X/(1+r)² + … + X/(1+r)ⁿ  (where r is the decimal rate)

Each instalment is discounted back by the number of years it's outstanding.

**Worked example:** A loan of ₹1,275 is repaid in 2 equal annual instalments at 4% CI. Find each instalment.
- 1275 = X/1.04 + X/1.04² = X(1/1.04 + 1/1.0816)
- Multiply through by 1.0816: 1275 × 1.0816 = 1.04X + X = 2.04X
- 1379.04 = 2.04X ⟹ X = **₹676**

**Under SI**, instead accumulate each instalment forward to the end:
Amount owed at end = sum of each instalment grown by SI for its remaining term.

**Practical shortcut:** for 2 instalments at rate r, X = P(1+r)²/(2 + r) with r as a decimal. Check: 1275(1.0816)/2.04 = 676. ✓

---

## 8. Type 4 — Different rates in different years

Just chain the factors — this is the biggest reason to think in factors.

**Worked example:** ₹8,000 at 5% in year 1, 10% in year 2, 20% in year 3.
- A = 8000 × 1.05 × 1.10 × 1.20 = **₹11,088**
- CI = 11088 − 8000 = ₹3,088

Order doesn't matter (factors commute). If a question asks whether it's better to have the high rate first, the answer is: no difference.

---

## 9. Type 5 — Depreciation and population

Same machinery, negative direction.

- Depreciated value = P(1 − r/100)ⁿ
- Population growth = P(1 + r/100)ⁿ
- **Population n years *ago*** = P/(1 + r/100)ⁿ — divide, don't subtract

**Worked example:** A machine costing ₹1,00,000 depreciates 10% per year. Value after 3 years?
- 100000 × 0.9³ = 100000 × 0.729 = **₹72,900**

**Mixed direction:** "population rises 10% in year 1, falls 10% in year 2" ⟹ 1.1 × 0.9 = 0.99 ⟹ net 1% fall, not zero.

---

## 9a. Type 5b — Growth stated as a percentage *of the initial value*

**The trap in one line:** "increases by g% **of X** every month", where X is the *initial* value, is **simple** growth, not compound. The base never moves, so the increments are equal and the totals form an AP (§1). Contrast "increases by g% every month", which does compound.

After m periods: **value = X(1 + mg/100)**, so "becomes t times the initial value" means

**t = 1 + mg/100**

**When t and g are forced to be integers**, that equation becomes a divisibility condition, and it usually pins g down to one or two values — which is the actual work in these questions. Handle it exactly as in `01-Number-System.md` §11: write the condition, then find which integers satisfy it.

**Method:**
1. Decide simple or compound from whether the percentage is "of X" or unqualified.
2. Write t = 1 + mg/100 and reduce the fraction.
3. Impose integrality, cancelling common factors first, to get the divisibility condition on g.
4. Apply the stated range on t to list the candidate (g, t) pairs, then pick the one the question wants.

**Worked example:** A creator's subscriber count grows each month by g% of his initial count X, and after 24 months equals exactly t times the initial count, with g and t natural numbers and 3 ≤ t ≤ 15. A second creator starts with 16,000 and grows at g% per annum **compounded annually** for 2 years. Find his maximum possible final count.

- Simple growth: t = 1 + 24g/100 = 1 + 6g/25
- t integer ⟹ 25 divides 6g. Since gcd(6, 25) = 1, **25 divides g**. Write g = 25k ⟹ t = 1 + 6k.
- 3 ≤ t ≤ 15 ⟹ 2 ≤ 6k ≤ 14 ⟹ k ∈ {1, 2} ⟹ **(g, t) = (25, 7) or (50, 13)**
- Maximising the second creator's total means maximising g ⟹ **g = 50**
- Compound, 2 years: 16,000 × (1.5)² = 16,000 × 2.25 = **36,000**

**Traps:**
- Compounding the first creator. "g% of X" nails the base at X — that is simple growth. Compounding would give 1.25²⁴, nowhere near an integer multiple.
- Simple-growing the second creator. The question says *compounded annually*; 16,000 × (1 + 2 × 0.5) = 32,000 is the planted wrong answer.
- Treating g% per **month** and g% per **annum** as one rate. The two creators share the number g, not the time unit.
- Cancelling carelessly: 25 | 6g reduces to 25 | g only because 6 and 25 are coprime. Check the gcd before dividing.
- Taking g = 25 because it appears first. The question asks for the **maximum**.

---

## 10. Type 6 — Splitting a sum between two rates

This is an alligation question in disguise. Weight by the principal.

**Worked example:** ₹12,000 is split between two schemes at 8% and 12% SI, giving total interest of ₹1,200 in one year (i.e. 10% overall).
- Alligation: (12 − 10) : (10 − 8) = 1 : 1 ⟹ ₹6,000 each.

See `05-Mixtures-and-Alligation.md` §8 for the general treatment. Note the weighting is by principal, and this only works cleanly for SI or for one CI period.

---

## 11. Useful approximation for CI

For small r and small n, CI ≈ SI + the pairwise correction:

(1 + x)ⁿ ≈ 1 + nx + [n(n−1)/2]x²

At 5% for 3 years: 1 + 0.15 + 3(0.0025) = 1.1575 vs exact 1.157625. Accurate to two decimals — enough for option elimination in the exam.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Half-yearly compounding | r/2 for n periods | r/2 for 2n periods |
| Sum doubles in 5 yrs, when 8×? | 15 yrs assumed for SI too | CI: 15 yrs; SI: 35 yrs |
| Question asks interest, you compute amount | A | A − P |
| Population n years ago | subtract r% n times | divide by (1+r/100)ⁿ |
| CI − SI for 3 years | using the 2-year formula | Pr²(300+r)/10⁶ |
| Rate given per annum, time in months | use months directly | convert: 6 months = ½ year |
| SI where "interest also earns interest" is stated | SI | it's CI |
| "increases by g% of the initial value" | compound it | base is fixed ⟹ simple growth |

---

## Practical exam habits

- Convert every rate to a fraction: 12.5% → 9/8 as a growth factor, 6.25% → 17/16. CAT chooses rates like 6.25%, 12.5%, 16.67% precisely so the factors are clean.
- For CI over 2–3 years, expanding by hand (P, then interest on interest) is often faster than the formula and less error-prone.
- Check whether interest is per annum but the period is in months or the compounding is sub-annual — that's the most-planted trap.
- CI > SI always for t > 1 year; they're equal at t = 1. If your CI comes out lower, you've made an error.

**Where this feeds forward:** `02-Percentages.md` (successive change is the same operation), `05-Mixtures-and-Alligation.md` (splitting principal between rates), `04-Means-and-Weighted-Averages.md` (average rate of return is a weighted mean, and for multi-year growth it's a *geometric* mean).
