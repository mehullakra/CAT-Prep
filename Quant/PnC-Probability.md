# Permutations, Combinations & Probability (P&C)

> CAT quant. Every question reduces to one decision: am I only *choosing*, or am I choosing *and then arranging*? Probability is the same counting done twice — favourable over total.

---

## 1. Core idea

Order irrelevant → **Combination**, C(n,r). Order relevant → **Permutation**, P(n,r).

The link between them: **P(n,r) = C(n,r) × r!** — a permutation is just a combination followed by arranging the chosen r items.

**The 5-second test:** swap two of your chosen items. Different outcome? Permutation. Same outcome? Combination.

- Team of 3 from 10 → swapping A and B gives the same team → combination
- President, VP, Secretary from 10 → swapping A and B changes who's president → permutation

**The habit that solves most questions without any formula:** break the task into a sequence of independent decisions, count the options for each, multiply. That's the Fundamental Counting Principle, and it handles roughly 70% of CAT P&C on its own.

**And the one rule people get backwards:** separate *cases* are ADDED, sequential *decisions* are MULTIPLIED. More marks are lost here than to any formula.

---

## 2. Formula sheet

| Name | Formula | Use when |
|---|---|---|
| Factorial | n! , with 0! = 1 | Arranging all n distinct things |
| Permutation | P(n,r) = n!/(n−r)! | Pick r from n **and** order them |
| Combination | C(n,r) = n!/(r!(n−r)!) | Pick r from n, order irrelevant |
| Symmetry | C(n,r) = C(n, n−r) | Compute C(20,18) as C(20,2) = 190 |
| Row sum | C(n,0)+…+C(n,n) = 2ⁿ | Subset / "at least one" problems |
| Repeated letters | n! / (p! q! r! …) | Arranging with duplicates |
| Circular | (n−1)! | Round table, rotations identical |
| Circular, flippable | (n−1)!/2 | Necklaces, garlands, beads |
| Identical items → distinct boxes | C(n+r−1, r−1) | Empties allowed |
| Same, no box empty | C(n−1, r−1) | Each box gets ≥ 1 |
| Distinct items → distinct boxes | rⁿ | Each item picks a box independently |
| Repetition allowed | nʳ | r slots, any of n values each |
| Derangement | D(n) | Nobody gets their own item |

Memorise cold: 5! = 120, 6! = 720, 7! = 5040, 8! = 40320.

Derangements: **D(2)=1, D(3)=2, D(4)=9, D(5)=44, D(6)=265.** Recurrence if you forget: D(n) = (n−1)[D(n−1) + D(n−2)].

Common values: C(5,2)=10, C(6,2)=15, C(6,3)=20, C(7,2)=21, C(8,2)=28, C(10,2)=45, C(10,3)=120, C(52,2)=1326.

---

## 3. Arrangements — "must be together"

**Method: glue.** Tie the group into one block, arrange the blocks and loose items, then multiply by the internal arrangements of the block.

Formula: (n − k + 1)! × k!, where k items must stay together.

**Worked example:** 6 people in a row, 2 specific people must sit together.

- Glue the pair → 5 objects to arrange: 5! = 120
- The pair can swap internally: × 2! = 2
- Total = **240**

**Critical exception:** multiply by k! only if the glued items are **distinct**. If you glue two identical R's, there is nothing to swap — see §4.

---

## 4. Arrangements — "must NOT be together"

**Method: complement.** Total − (arrangements where they ARE together). Never count "not together" directly; you will double-count.

**Worked example:** Same 6 people, the 2 must not sit together.

- Total = 6! = 720
- Together = 240 (from §3)
- Answer = 720 − 240 = **480**

**When several items must be mutually non-adjacent, use the gap method instead:** arrange the unrestricted items first, then drop the restricted ones into the gaps between them.

**Worked example:** 4 boys and 3 girls in a row, no two girls adjacent.

- Arrange the 4 boys: 4! = 24
- That creates 5 gaps (including the two ends): _ B _ B _ B _ B _
- Place 3 girls into 3 of those 5 gaps, order matters: P(5,3) = 5 × 4 × 3 = 60
- Total = 24 × 60 = **1440**

---

## 4b. Arrangements with a relative-order constraint (not adjacency)

A different beast from "together" and "not together". Here the constraint is on **order**, not position: "A must come before B", "the three books must appear in alphabetical order", "the men must be seated in increasing order of age".

**The core idea:** among the k constrained items there are k! possible internal orders, and the constraint permits exactly **one** of them. By symmetry every order is equally likely, so

**Answer = n! / k!**

The constrained items need **not** be adjacent — that's the whole point, and it's why the gap method of §4 does not apply.

**Worked example:** In how many ways can 6 people stand in a row if A must be somewhere before B?

- Total = 6! = 720
- A-before-B and B-before-A are symmetric halves ⟹ 720/2 = **360**
- Or by formula: 6!/2! = 360

**Worked example:** 7 books arranged on a shelf, with 3 particular books required to appear in a fixed relative order (not necessarily adjacent).

- 7!/3! = 5040/6 = **840**

**Worked example (two independent order constraints):** 8 people in a row, with A before B **and** C before D.

- Divide by 2! for each constrained pair: 8!/(2! × 2!) = 40320/4 = **10,080**

Constraints on **disjoint** sets of items are independent, so their divisors multiply. If the sets overlap (e.g. A before B and B before C), treat them as one chain of 3 items and divide by 3! once.

**The connection to repeated letters (§5):** dividing by k! for a forced order is arithmetically identical to dividing by k! for identical items. In both cases you're collapsing k! equivalent arrangements into one. If you can see them as the same operation, neither will ever confuse you.

**Circular version:** for n people around a table with k in a fixed relative order, the count is (n−1)!/k!.

**Trap:** "A must come before B" is *not* "A and B are together". Adjacency questions divide by nothing and multiply by k!; order questions divide by k! and multiply by nothing. Read which one is being asked.

---

## 5. Words with repeated letters

**Method:** n! divided by the factorial of each repeat count.

**Worked example:** arrangements of ARRANGE, and how many have both R's together.

- 7 letters: A twice, R twice, N/G/E once each
- Total = 7! / (2! × 2!) = 5040 / 4 = **1260**
- Both R's together: glue RR → 6 objects [RR], A, A, N, G, E, with A repeating
- 6! / 2! = 720 / 2 = **360**
- Do **not** multiply by 2! — the two R's are identical, swapping them changes nothing

That last line is the single most common slip in this section.

---

## 6. Circular arrangements

Fix one person to kill the rotational symmetry → **(n−1)!**

- Flipping gives the same object (necklace, garland, beads) → divide by 2 → (n−1)!/2
- Seats are **numbered or otherwise distinguishable** → it's a straight line → n!

**Worked example:** 8 people at a round table, 2 specific people together.

- Glue the pair → 7 objects in a circle → (7−1)! = 6! = 720
- Pair swaps internally: × 2 = **1440**

---

## 7. Number formation

**Method: fill the constrained position FIRST.** For a d-digit number the leading digit cannot be 0 — settle that slot before touching the others.

**Worked example:** 4-digit numbers from digits 0,1,2,3,4,5, no repetition.

- Thousands place: 5 choices (1–5, excluding 0)
- Hundreds: 5 left (0 is available again, minus the one used)
- Tens: 4. Units: 3.
- Total = 5 × 5 × 4 × 3 = **300**

The decoy is 6 × 5 × 4 × 3 = 360, which wrongly allows a leading zero.

**Divisibility versions:**

- By 2 → fix an even last digit; by 5 → last digit 0 or 5
- By 3 → choose the digit *set* first so the digit sum is divisible by 3, then arrange

**Worked example:** 3-digit numbers divisible by 5 from digits 0–5, no repetition.

- Case last digit = 0: first digit 5 choices (1–5), middle 4 → 20
- Case last digit = 5: first digit 4 choices (1–4, not 0), middle 4 → 16
- Total = 20 + 16 = **36**

Note the split: two cases, so they're added.

---

## 8. Selections and committees

**"At least one" from n distinct items:** 2ⁿ − 1 (all subsets minus the empty one).
With multiplicities instead of distinct items — say 3 identical apples and 2 identical oranges — it's (3+1)(2+1) − 1 = 11.

**Mixed committees are the standard CAT shape.** Split into cases, multiply within a case, add across cases.

**Worked example:** committee of 5 from 7 men and 5 women, with at least 3 women.

- 3W + 2M = C(5,3) × C(7,2) = 10 × 21 = 210
- 4W + 1M = C(5,4) × C(7,1) = 5 × 7 = 35
- 5W + 0M = C(5,5) × C(7,0) = 1 × 1 = 1
- Total = 210 + 35 + 1 = **246**

If the number of cases exceeds three, check whether the complement is shorter.

---

## 9. Distribution — identical vs distinct

These two look identical in the question and are wildly different in the answer. Read for the word "identical" or "different".

**Identical items into distinct boxes — stars and bars:**

- Empties allowed: C(n + r − 1, r − 1)
- Each box ≥ 1: C(n − 1, r − 1)
- Each box ≥ m: hand out m to everyone first, then apply the empties-allowed formula to the remainder

**Worked example:** 10 identical chocolates among 4 children.

- Any child may get none: C(10 + 4 − 1, 3) = C(13,3) = (13 × 12 × 11)/6 = **286**
- Each child at least one: C(9,3) = (9 × 8 × 7)/6 = **84**

**Distinct items into distinct boxes:** each item independently picks a box → rⁿ. Ten *different* books among 4 children = 4¹⁰, not 286.

**Dividing people into groups** — watch the naming:

- Into 3 **named** groups of 4 (Group A, B, C): 12!/(4! 4! 4!) = 34,650
- Into 3 **unnamed** groups of 4: divide by 3! → 5,775

---

## 9a. Monotone sequences — "digits are non-decreasing"

**The recognition cue:** the question fixes the *order* of the slots, so once you know which values are used and how often, the sequence is completely determined. There is exactly **one** valid arrangement per multiset — so don't arrange at all, just **choose with repetition**.

**Core idea.** Choosing r items from n types, repetition allowed, order irrelevant:

**C(n + r − 1, r)**

This is §9's stars and bars read the other way round: "how many of each type" *is* a distribution of r identical stars into n distinct boxes, so C(n + r − 1, n − 1) = C(n + r − 1, r). Use whichever form has the smaller lower index.

**Method:**
1. Confirm the wording forces a unique order — "non-decreasing", "non-increasing", "in increasing order", "in alphabetical order".
2. Fix the **value pool**. This is where the leading-digit rule bites.
3. Weakly monotone (repeats allowed) → C(n + r − 1, r). Strictly monotone (no repeats) → C(n, r).

**Worked example:** How many 7-digit numbers have non-decreasing digits?

- d₁ ≤ d₂ ≤ … ≤ d₇. If d₁ = 0 the number has a leading zero, so d₁ ≥ 1 — and because the sequence never decreases, **every** digit is ≥ 1. Pool = {1,…,9}, so n = 9, r = 7.
- C(9 + 7 − 1, 7) = C(15, 7) = 6435
- Answer: **6435**

**The non-increasing version is not symmetric.** For d₁ ≥ d₂ ≥ … ≥ d₇ the *later* digits may be 0, so the pool is all ten digits and only d₁ ≥ 1 restricts anything. Count = C(16, 7) − 1 = 11440 − 1 = **11439** (the −1 removes the all-zeros multiset, the only one whose leading digit is 0).

**Traps:**
- Multiplying by 7!, or computing 9⁷. There is nothing to arrange — the order is forced by the constraint.
- Using n = 10 for the non-decreasing case. One leading-zero check kills the entire 0 branch, because 0 can only sit first.
- Confusing "non-decreasing" (repeats allowed, C(15,7) = 6435) with "strictly increasing" (no repeats, C(9,7) = 36).
- Assuming the non-increasing count equals the non-decreasing count. The zero is available at the back but not at the front, so they differ.

---

## 10. Derangements

Recognise the phrasing: "nobody gets their own", "no letter into its correct envelope", "no one sits in their assigned seat". Then read D(n) off the memorised list.

**Exactly k correct = C(n,k) × D(n−k)** — choose who lands correctly, derange the rest.

**Worked example:** 5 letters into 5 addressed envelopes at random, exactly 2 correct.

- Choose the 2 that go right: C(5,2) = 10
- The other 3 must all be wrong: D(3) = 2
- Total = 10 × 2 = **20**

**Do not confuse** "all wrong" (= D(n)) with "at least one wrong" (= n! − 1, since only one arrangement has everything correct).

---

## 11. Grid paths, handshakes, diagonals

All of these collapse to a single C(n,r).

**Grid paths:** a shortest path is just an arrangement of R's and U's.

- 4 blocks right, 3 blocks up → 7 moves, choose which 3 are up → C(7,3) = **35**

**Geometry counting** (n points, no 3 collinear):

| Asked for | Count |
|---|---|
| Handshakes among n people | C(n,2) |
| Lines through n points | C(n,2) |
| Triangles from n points | C(n,3) |
| Diagonals of an n-gon | C(n,2) − n |

**Worked example:** diagonals of a 12-sided polygon.

- All vertex pairs: C(12,2) = (12 × 11)/2 = 66
- Subtract the 12 sides: 66 − 12 = **54**

C(n,2) itself always appears as a decoy option here.

---

## 12. Dictionary rank of a word

**Method:** count the words that come strictly before it, then add 1.

Go position by position. At each position, count how many unused letters are alphabetically smaller than the actual letter, and multiply by the arrangements of everything still left. Sum, then +1.

**Worked example:** rank of CAT among arrangements of C, A, T. Sorted pool: A, C, T.

- Position 1 is C. Smaller unused letters: just A → 1 × 2! = 2 words come first
- Position 2 is A. Pool now {A, T}. Smaller than A: none → 0
- Position 3 is T. Pool {T}. Smaller: none → 0
- Words before = 2, so rank = 2 + 1 = **3**

Check: ACT, ATC, CAT, CTA, TAC, TCA. ✓

Read the wording carefully — "rank" needs the +1, "how many words come before it" does not.

---

## 13. Probability — the same counting, divided

**P(event) = favourable / total**, with both counted the **same way**. Both as combinations, or both as permutations. Mixing modes is the number-one error in this section.

**Worked example:** two cards from a standard deck, both aces.

- Total = C(52,2) = (52 × 51)/2 = 1326
- Favourable = C(4,2) = 6
- P = 6/1326 = **1/221**

(Counting both as ordered — 4×3 over 52×51 — gives 12/2652 = 1/221 too. Consistency is what matters, not which mode.)

**Worked example:** bag with 5 red and 3 blue balls, 2 drawn, both red.

- C(5,2)/C(8,2) = 10/28 = **5/14**

**Deck and dice facts, asked constantly:**

- 52 cards = 4 suits × 13. Red 26, black 26, face cards 12, aces 4.
- Two dice = 36 outcomes. Ways to make sum s for s = 2…12: 1, 2, 3, 4, 5, **6**, 5, 4, 3, 2, 1. Sum 7 is the most likely.
- n coin tosses = 2ⁿ outcomes.

---

## 14. "At least one" — always the complement

P(at least one) = 1 − P(none). Counting directly means summing many cases; the complement is one case.

**Worked example:** 3 fair coins, probability of at least one head.

- Total = 2³ = 8
- No heads at all = TTT = 1 outcome → P = 1/8
- Answer = 1 − 1/8 = **7/8**

**Related rules:**

- P(A or B) = P(A) + P(B) − P(A and B). Only drop the last term if you have *checked* the events are disjoint.
- P(A and B) = P(A) × P(B) only when the events are genuinely independent. Drawing without replacement is not independent.

---

## 15. Conditional probability

The condition shrinks the denominator. Recount the total *inside* the given condition, then count favourables within that smaller space.

Formula: P(A | B) = P(A and B) / P(B)

**Worked example:** a die is rolled; given the outcome is even, find P(outcome > 3).

- The condition restricts the sample space to {2, 4, 6} → 3 outcomes
- Of those, greater than 3: {4, 6} → 2 outcomes
- P = **2/3**

Using the original denominator of 6 gives 2/6 = 1/3, which is the decoy.

---

## 16. Repeated trials and expected value

**Binomial** — n independent trials, same success probability p each time, exactly r successes:

P = C(n,r) · pʳ · (1−p)ⁿ⁻ʳ

**Worked example:** a coin shows heads with probability 1/3, tossed 4 times, exactly 2 heads.

- Choose which 2 tosses are heads: C(4,2) = 6
- One such specific sequence: (1/3)² × (2/3)² = (1/9)(4/9) = 4/81
- Total = 6 × 4/81 = 24/81 = **8/27**

**Expected value** = Σ (value × probability).

**Worked example:** you win ₹10 if a die shows 6, otherwise you lose ₹2.

- E = (1/6)(10) + (5/6)(−2) = 10/6 − 10/6 = **0** — a fair game

Expected value of one die roll = (1+2+3+4+5+6)/6 = 3.5. Worth remembering.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Cases vs decisions | 210 × 35 × 1 | separate cases are added: 210 + 35 + 1 = 246 |
| Gluing identical letters | RR block × 2! | identical items don't swap — no × 2! |
| Leading zero | 6 × 5 × 4 × 3 = 360 | fix the first slot first: 300 |
| Numbered seats at a round table | (n−1)! | numbered = linear = n! |
| Necklace vs table | (n−1)! | flippable → (n−1)!/2 |
| Identical vs distinct items | one formula for both | 10 identical → C(13,3) = 286; 10 distinct → 4¹⁰ |
| Groups of equal size | 12!/(4!4!4!) always | unnamed groups need ÷ 3! → 5775 |
| "At least one" | sum all the cases | 1 − P(none) |
| Probability counting mode | favourable as C, total as P | use the same mode top and bottom |
| Conditional probability | original denominator | denominator shrinks to the given condition |
| With vs without replacement | multiply the same probability twice | denominator drops by 1 each draw |
| Independence assumed | P(A)×P(B) by default | only when genuinely independent |
| P(A or B) | always P(A) + P(B) | subtract P(A and B) unless disjoint |
| Derangement phrasing | "at least one wrong" = D(n) | all wrong = D(n); at least one wrong = n! − 1 |
| Diagonals of an n-gon | C(n,2) | C(n,2) − n |
| C(n,r) computed the long way | expand C(20,18) | C(20,18) = C(20,2) = 190 |
| Dictionary rank | words counted before it | rank = that count + 1 |
| Non-decreasing digits | arrange after choosing | order is forced — choose with repetition only |

---

**The one habit that fixes most errors:** before writing a single factorial, say out loud whether you are *choosing* or *choosing and arranging*, and whether the parts of the answer are *cases* (add) or *decisions* (multiply). Almost every wrong answer in this topic comes from getting one of those two labels wrong, not from arithmetic.

**Timing rule:** if the structure isn't visible within 20 seconds, it isn't a 2-minute question. Mark it and move on — P&C rewards recognition, not grinding.

*Connection to other topics: the "at least one → complement" move and the case-splitting discipline are the same ones used in Mixtures and in set-theory LR questions. Companion topic not yet covered: Calendars.*
