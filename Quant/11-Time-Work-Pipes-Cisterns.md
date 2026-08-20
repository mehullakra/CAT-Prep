# Time & Work, and Pipes & Cisterns

> CAT quant. Pipes & cisterns is Time & Work with negative rates for outlets. One method — the LCM method — handles both entirely.

---

## 1. Core idea

**Work is not a fraction. Make it a whole number.**

Never add 1/12 + 1/18. Instead:

1. Set total work = **LCM of the given days**
2. Rate = total work ÷ days
3. Add or subtract rates as whole numbers
4. Answer = total work ÷ combined rate

Every variant in this file — alternate days, wages, leaks, staggered pipes, people leaving midway — works without modification once the total is an LCM. This is the single highest-value habit in the topic, and there is no situation where fractions are better.

**Worked example:** A does a job in 12 days, B in 18 days. Together?

- Total work = LCM(12, 18) = 36 units
- A's rate = 36/12 = 3 units/day; B's rate = 36/18 = 2 units/day
- Together = 5 units/day
- Time = 36/5 = **7.2 days**

Clean integers the whole way.

**Choosing the total when days aren't given directly:** if the question gives ratios or efficiencies rather than days, pick any convenient total — 100 units usually works. The method doesn't require the LCM specifically; it requires a total that makes the rates integers.

---

## 2. Efficiency is inverse to time

- A is twice as efficient as B ⟹ A takes **half** the time
- Time ratio 3 : 5 ⟹ Efficiency ratio 5 : 3

**Worked example:** A is 50% more efficient than B. If B takes 30 days, how long does A take?

- Efficiency ratio A : B = 3 : 2 (50% more means 1.5×)
- Time ratio A : B = 2 : 3
- B takes 30 ⟹ A takes 30 × 2/3 = **20 days**

**Worked example:** A and B together finish a job in 12 days; A alone in 20 days. How long for B alone?

- Total = LCM(12, 20) = 60 units
- Combined rate = 60/12 = 5; A's rate = 60/20 = 3
- B's rate = 5 − 3 = 2 → B alone = 60/2 = **30 days**

Rates subtract cleanly. Times never do — "12 and 20 gives 8 days" is the classic wrong move.

---

## 3. The M-D-H formula

**M₁ × D₁ × H₁ / W₁ = M₂ × D₂ × H₂ / W₂**

(Men × Days × Hours ÷ Work.) Plug in and cross-multiply. This handles every "if 15 men build 3 walls in 8 days working 6 hours a day…" question.

**Worked example:** 15 men build 3 walls in 8 days working 6 hrs/day. How many days for 20 men to build 5 walls working 9 hrs/day?

- 15 × 8 × 6 / 3 = 20 × D × 9 / 5
- 720/3 = 240; and 180D/5 = 36D
- 240 = 36D ⟹ D = **6 2/3 days**

**Read the direction of each variable:** more men → fewer days (inverse), more work → more days (direct). If your answer moved the wrong way, you've flipped a term. That check takes three seconds and catches almost every M-D-H error.

---

## 4. Alternate days — the cycle method

1. Compute the work done in one full cycle (usually 2 days)
2. Divide total work by cycle work to get the number of complete cycles
3. Handle the leftover day by day, in order

**Worked example:** A alone in 10 days, B alone in 15 days, working on alternate days with A starting.

- Total = LCM(10, 15) = 30 units; A = 3/day, B = 2/day
- One cycle (2 days) = 5 units
- 30 ÷ 5 = 6 complete cycles = **12 days** exactly

**Worked example with a remainder:** A alone in 8 days, B alone in 12 days, alternate days, A starting.

- Total = LCM(8, 12) = 24; A = 3/day, B = 2/day; cycle = 5 units per 2 days
- 4 complete cycles = 20 units in 8 days, leaving 4 units
- Day 9 is A's turn: he does 3 → 1 unit left after 9 days
- Day 10 is B's turn at 2 units/day: needs 1/2 day
- Total = **9.5 days**

**Who starts matters when there's a remainder.** If B had started, the leftover would be consumed at different rates and the answer changes. Always note the starter before computing.

---

## 5. People joining or leaving midway

**Method:** compute the work done in each phase separately and subtract from the total. Never try to average the rates.

**Worked example:** A can do a job in 20 days and B in 30 days. They start together but A leaves after 5 days. How long does the whole job take?

- Total = LCM(20, 30) = 60; A = 3/day, B = 2/day
- First 5 days together: 5 × 5 = 25 units done, 35 remaining
- B alone at 2/day: 35/2 = 17.5 days
- Total = 5 + 17.5 = **22.5 days**

**Worked example (reverse phrasing):** the same pair finish the job in 15 days total, with A leaving at some point. When did A leave?

- Let A work d days; B works all 15 days
- 3d + 2(15) = 60 ⟹ 3d = 30 ⟹ d = **10 days**

The reverse phrasing is more common in CAT than the forward one. Set the unknown as the number of days the departing person worked, and write one equation in units.

---

## 5a. Departures defined *backwards* from the finish

§5 handles "A leaves after 5 days" — a phase boundary you can count forwards from day 1. CAT prefers the harder phrasing: "**A leaves 3 days before the project is completed**." The boundary is measured from an end you do not yet know, so you cannot split into phases until you have the answer.

**Core idea — assume the total D, express every worker's days in terms of D, and solve or test.**

For a total of D days:
- someone who works throughout contributes D days
- someone who leaves k days before the end contributes **D − k** days
- someone on alternate days from day 1 contributes **⌈(their last day)/2⌉** days — count the odd-numbered days only, not half of them

Because D must be a whole number and the options are few, **testing D is usually faster than solving** — one substitution per candidate, and the totals bracket the answer immediately.

**Method:**
1. Set the total work as the LCM of the individual times (§1) and get each rate.
2. Write each person's number of working days as an expression in D.
3. Test the candidate values of D from the options, or solve if the expression is clean. Check that the total lands on exactly the full work — under means D is too small, over means too large.

**Worked example:** Rohan alone takes 15 days, Suman 10, Tarun 20. All three start together, but Tarun works only on alternate days starting from day 1. Tarun leaves 3 days before completion and Suman leaves 1 day before completion. In how many days is the project completed?

- Total = LCM(15, 10, 20) = **60 units**. Rates: Rohan **4**/day, Suman **6**/day, Tarun **3**/day.
- Days worked: Rohan D; Suman D − 1; Tarun works the odd-numbered days up to day D − 3.
- **Test D = 6:** Rohan 6 days ⟹ 24. Suman days 1–5 ⟹ 5 × 6 = 30. Tarun's last possible day is day 3, so he works days 1 and 3 ⟹ 2 × 3 = 6.
- Total = 24 + 30 + 6 = **60** ✓ exactly ⟹ **D = 6**
- Bracketing check: D = 5 gives 20 + 24 + 3 = 47 (short), D = 7 gives 28 + 36 + 6 = 70 (over). 6 is the only fit.

**Traps:**
- Halving Tarun's span. Over days 1–3 he works **2** days (1 and 3), not 1.5. Alternate-day counts are ceilings, not halves — §4.
- Reading "leaves 3 days before completion" as "works for 3 days" or "leaves on day 3".
- Splitting into forward phases. You cannot, until D is known; that is exactly what makes this harder than §5.
- Accepting a fractional D. Here the departures are pegged to whole days from the end, so a non-integer D is a signal you have miscounted somebody's days, not a valid answer.

---

## 6. Wages

**Wages are split in the ratio of work actually done** — that is, efficiency × days worked. **Not** in the ratio of days worked alone, and not in the ratio of efficiencies alone.

**Worked example:** A can do a job in 6 days, B in 12 days. They work together and earn ₹900. Find each share.

- Total = 12 units; A = 2/day, B = 1/day
- Working together throughout, they contribute in the ratio of their rates = 2 : 1
- A gets ₹600, B gets ₹300

**Worked example where days differ:** A works 4 days at 3 units/day, B works 6 days at 2 units/day, total wage ₹720.

- Work done: A = 12 units, B = 12 units → ratio 1 : 1
- Each gets **₹360**, despite B working longer

That second example is exactly the trap: B worked more days but earned the same, because wages follow units of work, not attendance.

---

## 7. Pipes and cisterns

Identical to time and work, with one change: **an outlet pipe has a negative rate.**

**Worked example:** Pipe A fills in 6 hrs, pipe B fills in 8 hrs, pipe C empties in 12 hrs. All open together?

- Total = LCM(6, 8, 12) = 24 units
- A = +4, B = +3, C = −2
- Net = 5 units/hr → time = 24/5 = **4.8 hours**

**If the net rate comes out negative**, the tank never fills — and if it starts full, it empties. CAT does ask this; the answer is "the tank will never fill", not a negative time.

**Leak questions — the rate is a difference, not a fraction.**

**Worked example:** A cistern fills in 6 hrs but takes 8 hrs because of a leak. How long would the leak alone empty a full cistern?

- Total = LCM(6, 8) = 24; fill rate = 4/hr; effective rate with leak = 3/hr
- Leak rate = 4 − 3 = 1 unit/hr → leak alone empties in 24/1 = **24 hours**

Reading the leak's rate as 24/8 = 3 is the standard error. The leak is the *difference* between the clean rate and the observed rate.

**Staggered opening — phase it.**

**Worked example:** Pipe A fills in 10 hrs, pipe B in 15 hrs. Both are opened, but A is closed after 4 hours. Total time to fill?

- Total = 30; A = 3/hr, B = 2/hr
- First 4 hours at 5/hr = 20 units, leaving 10
- B alone at 2/hr → 5 more hours
- Total = 4 + 5 = **9 hours**

**"Closed x hours before the tank fills"** is the harder phrasing. Let T be the total time; B runs for all T hours and A runs for (T − x). Write one equation in units and solve.

**Worked example:** A fills in 12 hrs, B in 16 hrs. Both opened together, but A is closed some time before the tank fills, and the tank fills in 9 hours. When was A closed?

- Total = LCM(12, 16) = 48; A = 4/hr, B = 3/hr
- B runs all 9 hours: 27 units. Remaining 21 units from A at 4/hr → A ran 5.25 hours
- A was closed after **5.25 hours**, i.e. 3.75 hours before the tank filled

---

## 8. Fractions of the work

If the question gives days for individuals but asks about *part* of the job, still set the total to the LCM and take that fraction of it. Do not switch to fractional rates mid-solution — that discards the entire advantage of the method.

**Worked example:** A and B together take 12 days for a full job. How long for 2/3 of it?

- Whatever the total is, 2/3 of the work takes 2/3 of the time = **8 days**

For a single combined rate this is trivial; the LCM discipline matters when different people do different fractions, where the units keep everything integer.

---

## 9. Individual rates from pairwise or average completion times

The classic three-worker setup: you're given how long each **pair** takes, and asked for the individuals.

**The key relation:**

(A+B) + (B+C) + (C+A) = **2 × (A + B + C)** in rates.

So add the three pairwise rates and halve to get the combined rate. Then subtract each pairwise rate to isolate the missing person.

**Worked example:** A and B together finish in 12 days, B and C in 15 days, A and C in 20 days. How long does each take alone?

- Total = LCM(12, 15, 20) = 60 units
- Rates: A+B = 5, B+C = 4, A+C = 3 ⟹ sum = 12 = 2(A+B+C) ⟹ **A+B+C = 6 units/day**
- Each individual = 6 − (the pair that excludes them):
- A = 6 − 4 = 2 ⟹ **30 days**; B = 6 − 3 = 3 ⟹ **20 days**; C = 6 − 5 = 1 ⟹ **60 days**
- All three together = 60/6 = **10 days**

**Sanity check built into the method:** each individual rate must be positive and smaller than every pair rate containing that person. If one comes out ≤ 0, the given data is inconsistent (or you've mis-copied a number).

**"Average completion time" phrasing:** if a question says three workers take an average of t days individually, that constrains the **sum of the times**, not the sum of the rates — Σdays = 3t. Times and rates are reciprocals, so you cannot average one and read off the other. This is the planted trap: the average of the times is *not* the time of an "average worker".

**Worked example:** Three workers take 10, 15, and 20 days. Average time = 15 days. But working together they take 60/(6+4+3) = 60/13 ≈ 4.6 days, and a hypothetical "average" worker at 15 days each would give 15/3 = 5 days. Different numbers — the combined answer must come from rates.

---

## 10. Ratio of work rates between workers

Everything about ratios in this topic follows one line: **rate ratio = inverse of the time ratio** (§2). Two further points CAT tests directly:

- **Work done in a fixed period is in the ratio of rates.** If A : B rates are 3 : 2 and both work 5 days, they complete 15 : 10 = 3 : 2 of the work. Wages follow this same ratio (§6).
- **Time taken for a fixed amount of work is in the inverse ratio.** A does a given job in 2/3 the time B needs.

**Worked example:** A is thrice as good a workman as B, and together they finish a job in 15 days. How long does each take alone?

- Rate ratio A : B = 3 : 1 ⟹ combined = 4 parts
- Combined takes 15 days ⟹ 4 parts × 15 = 60 part-days of work
- A alone: 60/3 = **20 days**; B alone: 60/1 = **60 days**

**Worked example (rate ratio from time difference):** A is twice as efficient as B and finishes a job 30 days sooner. Find B's time alone.

- Times are in ratio 1 : 2 ⟹ the difference of 1 part = 30 days ⟹ A = 30, **B = 60 days**

**The habit:** convert every "twice as efficient", "50% more efficient", "takes 40% longer" into a clean rate ratio *first*. Do not carry percentages into the rate arithmetic.

---

## 11. Partial work, then the remainder by one worker

The most common exam shape in this topic. **Method: units done, units remaining, remaining ÷ rate.**

**Worked example:** A can do a job in 15 days and B in 20 days. They work together for 4 days, after which A leaves. How long does B take to finish?

- Total = LCM(15, 20) = 60; A = 4/day, B = 3/day
- 4 days together: 4 × 7 = 28 units ⟹ 32 units remain
- B alone at 3/day: 32/3 = **10⅔ days**
- Total elapsed = 4 + 10⅔ = 14⅔ days

**Worked example (fraction-of-work phrasing):** A completes 2/5 of a job in 6 days, then B finishes the rest in 9 days. How long would B take for the whole job alone?

- B does 3/5 of the job in 9 days ⟹ the whole job takes 9 × 5/3 = **15 days**
- (And A's rate: 2/5 in 6 days ⟹ full job in 15 days too.)

**Worked example (find when the switch happened):** A (12 days) and B (18 days) start together; B leaves partway and A finishes, taking 9 days in total. When did B leave?

- Total = 36; A = 3/day, B = 2/day
- A works all 9 days: 27 units. Remaining 9 units came from B at 2/day ⟹ B worked **4.5 days**

**The one rule:** never convert back to "fraction of work per day" mid-solution. Stay in units, and the remainder is always a subtraction.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Combining times | 12 and 20 give 8 days | subtract *rates*, not times |
| Adding fractions | 1/12 + 1/18 | LCM method, integers only |
| Leak rate | 1/8 of the tank per hour | difference of rates: 4 − 3 = 1 |
| Wages | split by days worked | split by units of work done |
| Alternate days, remainder | ignore who starts | the starter changes the leftover |
| M-D-H direction | more men → more days | more men → fewer days |
| Net rate negative | reported as a negative time | the tank never fills |
| Person leaves midway | average the rates | phase it: work done, then remainder |
| Efficiency percentage | "50% more efficient" → time × 1.5 | efficiency 3:2 → time 2:3, so × 2/3 |
| Fraction of work | new LCM computed | take the fraction of the same total |
| "Leaves 3 days before completion" | works 3 days, or leaves on day 3 | works D − 3 days; test integer D |

---

**The one habit that fixes most errors:** write the total as an LCM before reading the rest of the question. Once every rate is an integer, adding a leak, removing a worker, or splitting wages is arithmetic rather than algebra — and nearly every error in this topic comes from working in fractions or from combining times instead of rates.

**Sanity check:** the combined time must always be shorter than the fastest individual time. If your answer for "A and B together" exceeds A's solo time, you've added times instead of rates.

*Related file: `05-Mixtures-and-Alligation.md` — the rate-blending logic there is the same weighted-average idea seen from the other side.*
