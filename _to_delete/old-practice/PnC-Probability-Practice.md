# Permutations, Combinations & Probability — Practice Sets

> Companion to `PnC-Probability.md`. Hints point to the section of the notes that contains the intended method — read the hint only after you've been stuck for a minute. Answer key with short solutions is at the bottom.
>
> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.
>
> Suggested timing: 2.0 min/question for Sets A–E, and attempt the Mixed Set in one timed block.
>
> **Ask "does the order matter?" before writing anything.** That single question decides between a permutation and a combination and settles most of the topic (§1).
>
> For "at least one", always count the complement. For "not together", count the total minus the together-case. Both are §4 and §14.

---

## Set A — Basic counting

**A1.** (TITA) In how many ways can the letters of the word CHAIR be arranged?

*Hint: §2 — five distinct letters, so it is simply 5!.*

**A2.** (MCQ) The value of ⁸C₃ is

- (a) 24
- (b) 56
- (c) 112
- (d) 336

*Hint: §2 — (8 × 7 × 6)/(3 × 2 × 1). 336 is ⁸P₃, planted.*

**A3.** (TITA) In how many ways can 3 distinct prizes be given to 5 students if no student may receive more than one?

*Hint: §1 — the prizes are distinct, so order matters: this is ⁵P₃.*

**A4.** (MCQ) The number of ways to select a committee of 3 from 10 people is

- (a) 30
- (b) 120
- (c) 240
- (d) 720

*Hint: §8 — a committee is unordered, so use ¹⁰C₃.*

**A5.** (TITA) How many 3-digit numbers can be formed from the digits 1 to 9 if repetition is allowed?

*Hint: §7 — each of the three places has 9 independent choices. There is no zero to worry about here.*

---

## Set B — Arrangements with constraints

**B1.** (TITA) In how many ways can 6 people be seated in a row if two particular people must sit together?

*Hint: §3 — glue the pair into a single block, arrange 5 objects, then arrange within the block.*

**B2.** (MCQ) In how many ways can the letters of ORANGE be arranged so that the vowels are never all together?

- (a) 144
- (b) 480
- (c) 576
- (d) 600

*Hint: §4 — total minus the together-case. Never count "not together" directly.*

**B3.** (TITA) In how many ways can 5 boys and 3 girls stand in a row so that no two girls are together?

*Hint: §4 — seat the boys first, then place the girls into the gaps between and around them. Five boys create six gaps.*

**B4.** (MCQ) In how many ways can 4 books be arranged on a shelf if one particular book must be first?

- (a) 6
- (b) 12
- (c) 18
- (d) 24

*Hint: §3 — fix the constrained object, then arrange whatever remains freely.*

**B5.** (TITA) In how many ways can the letters of LEADING be arranged so that the vowels always come together?

*Hint: §3 — the three vowels form one block, leaving 5 objects to arrange.*

---

## Set C — Repeated letters and circular arrangements

**C1.** (TITA) Find the number of distinct arrangements of the letters of BANANA.

*Hint: §5 — divide by the factorial of each repeat count: three A's and two N's.*

**C2.** (MCQ) The number of distinct arrangements of the letters of MISSISSIPPI is

- (a) 34,650
- (b) 44,100
- (c) 46,200
- (d) 55,440

*Hint: §5 — four I's, four S's and two P's.*

**C3.** (TITA) In how many ways can 7 people be seated around a circular table?

*Hint: §6 — fix one person to kill the rotational symmetry, giving (n − 1)!.*

**C4.** (MCQ) The number of ways to seat 8 people around a round table with two particular people together is

- (a) 720
- (b) 1440
- (c) 2880
- (d) 5040

*Hint: §6 + §3 — block the pair, then apply the circular rule to the 7 resulting objects.*

**C5.** (TITA) How many different necklaces can be made from 6 distinct beads?

*Hint: §6 — a necklace can be flipped, so divide the circular count by a further 2.*

---

## Set D — Number formation and selections

**D1.** (TITA) How many 4-digit numbers can be formed using the digits 0–9 without repetition?

*Hint: §7 — the leading digit cannot be 0, so handle that place first.*

**D2.** (MCQ) How many 3-digit even numbers can be formed from the digits 1, 2, 3, 4, 5 without repetition?

- (a) 12
- (b) 24
- (c) 36
- (d) 48

*Hint: §7 — fix the unit digit first, since that is where the constraint lives.*

**D3.** (TITA) From 7 men and 5 women, in how many ways can a committee of 5 be formed containing exactly 3 men?

*Hint: §8 — choose each group separately and multiply.*

**D4.** (MCQ) In how many ways can a team of 4 be chosen from 6 boys and 4 girls if it must include at least one girl?

- (a) 185
- (b) 195
- (c) 200
- (d) 209

*Hint: §14 — "at least one" means total minus the all-boys case.*

**D5.** (TITA) How many 5-digit numbers divisible by 5 can be formed from the digits 0–9 without repetition?

*Hint: §7 — split into two cases by the unit digit, because a unit digit of 5 restricts the leading digit further.*

---

## Set E — Probability

**E1.** (TITA) A fair die is rolled twice. Find the probability that the sum is 7 (as a fraction).

*Hint: §13 — count the favourable ordered pairs over 36.*

**E2.** (MCQ) Two cards are drawn from a standard pack. The probability that both are aces is

- (a) 1/221
- (b) 1/169
- (c) 1/13
- (d) 2/221

*Hint: §13 — ⁴C₂/⁵²C₂, or sequentially (4/52)(3/51). The second card's denominator changes.*

**E3.** (TITA) A bag holds 5 red and 3 blue balls. Two are drawn at random. Find the probability that both are red (as a fraction).

*Hint: §13 — ⁵C₂ over ⁸C₂.*

**E4.** (MCQ) A coin is tossed 4 times. The probability of getting at least one head is

- (a) 1/16
- (b) 1/2
- (c) 15/16
- (d) 4/16

*Hint: §14 — take the complement: no head at all.*

**E5.** (TITA) The probability that A solves a problem is 1/3 and that B solves it is 1/4. Find the probability that the problem is solved (as a fraction).

*Hint: §14 — the complement of "neither solves it". Adding 1/3 and 1/4 double-counts the overlap.*

**E6.** (MCQ) Three fair coins are tossed. Given that at least one shows heads, the probability that all three are heads is

- (a) 1/8
- (b) 1/7
- (c) 3/8
- (d) 1/2

*Hint: §15 — conditioning shrinks the sample space from 8 outcomes to 7.*

---

## Mixed Set — exam feel (17 minutes)

**M1.** (TITA) Find the number of distinct arrangements of the letters of SUCCESS.

**M2.** (MCQ) The number of diagonals of a polygon with 12 sides is

- (a) 44
- (b) 54
- (c) 60
- (d) 66

**M3.** (TITA) In how many ways can 5 distinct letters be posted into 3 letter boxes?

**M4.** (MCQ) The number of handshakes among 15 people, each shaking hands once with every other, is

- (a) 90
- (b) 105
- (c) 210
- (d) 225

**M5.** (TITA) In how many ways can 4 identical balls be placed in 3 distinct boxes?

**M6.** (MCQ) A number is chosen at random from 1 to 100. The probability that it is divisible by 3 or 5 is

- (a) 47/100
- (b) 1/2
- (c) 53/100
- (d) 8/15

**M7.** (TITA) In how many ways can a person go from the bottom-left to the top-right corner of a 4 × 3 grid, moving only right or up?

**M8.** (MCQ) The rank of the word RANK among all arrangements of its letters in dictionary order is

- (a) 18
- (b) 19
- (c) 20
- (d) 21

**M9.** (TITA) Five letters are placed at random into five addressed envelopes. In how many ways does no letter reach its correct envelope?

**M10.** (MCQ) Two dice are thrown. The probability that the product of the numbers is even is

- (a) 1/2
- (b) 2/3
- (c) 3/4
- (d) 5/6

---

# Answer key

## Set A

**A1 — 120.** 5! = **120**.

**A2 — (b) 56.** 336/6 = **56**.

**A3 — 60.** 5 × 4 × 3 = **60**.

**A4 — (b) 120.** ¹⁰C₃ = **120**. (720 = ¹⁰P₃, the ordered count.)

**A5 — 729.** 9³ = **729**.

## Set B

**B1 — 240.** 5! × 2! = 120 × 2 = **240**.

**B2 — (c) 576.** 6! − (4! × 3!) = 720 − 144 = **576**.

**B3 — 14400.** 5! × ⁶C₃ × 3! = 120 × 20 × 6 = **14,400**.

**B4 — (a) 6.** 3! = **6**.

**B5 — 720.** 5! × 3! = 120 × 6 = **720**.

## Set C

**C1 — 60.** 6!/(3! 2!) = 720/12 = **60**.

**C2 — (a) 34,650.** 11!/(4! 4! 2!) = **34,650**.

**C3 — 720.** 6! = **720**. (7! = 5040 counts every arrangement 7 times over.)

**C4 — (b) 1440.** (7 − 1)! × 2! = 720 × 2 = **1440**.

**C5 — 60.** (6 − 1)!/2 = 120/2 = **60**.

## Set D

**D1 — 4536.** 9 × 9 × 8 × 7 = **4536**.

**D2 — (b) 24.** Unit digit ∈ {2, 4} ⟹ 2 × 4 × 3 = **24**.

**D3 — 350.** ⁷C₃ × ⁵C₂ = 35 × 10 = **350**.

**D4 — (b) 195.** ¹⁰C₄ − ⁶C₄ = 210 − 15 = **195**.

**D5 — 5712.** Unit 0: 9 × 8 × 7 × 6 = 3024. Unit 5: the leading digit has 8 choices ⟹ 8 × 8 × 7 × 6 = 2688. Total = **5712**.

## Set E

**E1 — 1/6.** 6 of the 36 ordered pairs sum to 7 ⟹ **1/6**.

**E2 — (a) 1/221.** (4/52)(3/51) = 12/2652 = **1/221**. (1/169 treats the draws as independent — the planted error.)

**E3 — 5/14.** 10/28 = **5/14**.

**E4 — (c) 15/16.** 1 − (1/2)⁴ = **15/16**.

**E5 — 1/2.** 1 − (2/3)(3/4) = 1 − 1/2 = **1/2**.

**E6 — (b) 1/7.** (1/8)/(7/8) = **1/7**.

## Mixed Set

**M1 — 420.** 7!/(3! 2!) = 5040/12 = **420**.

**M2 — (b) 54.** 66 − 12 = **54**.

**M3 — 243.** 3⁵ = **243**. (5³ answers a different question — boxes picking letters.)

**M4 — (b) 105.** 15 × 14/2 = **105**.

**M5 — 15.** ⁶C₂ = **15**.

**M6 — (a) 47/100.** 33 + 20 − 6 = 47 ⟹ **47/100**.

**M7 — 35.** ⁷C₃ = **35**.

**M8 — (c) 20.** Words starting A, K or N: 3 × 3! = 18. Then RAKN is 19th and RANK is **20th**.

**M9 — 44.** D₅ = 5!(1 − 1 + ½ − 1/6 + 1/24 − 1/120) = **44**.

**M10 — (c) 3/4.** 1 − (3/6)(3/6) = 1 − 1/4 = **3/4**.

---

**Common error audit** — if you got a question wrong, find it here before moving on:

| Question | The error it is designed to catch |
|---|---|
| A2, A3, A4, M4 | using a permutation where the selection is unordered, or vice versa (§1) |
| B2, D4, E4, E5, M10 | counting the restricted case directly instead of taking the complement (§4, §14) |
| B3 | placing the constrained group first — always seat the unconstrained items and use the gaps |
| C1, C2, M1 | not dividing by the factorials of the repeat counts (§5) |
| C3, C4, C5 | using n! for a circular arrangement, or forgetting the extra ÷2 for a necklace (§6) |
| D1, D5 | letting 0 occupy the leading position (§7) |
| D2 | filling the free places before the constrained one |
| E2 | treating draws without replacement as independent (§13) |
| E6 | using the unconditional probability where the sample space has already shrunk (§15) |
| M3 | raising the wrong quantity to the wrong power in a distribution problem (§9) |
| M5 | using distinct-object logic for identical balls |
| M8 | miscounting the blocks of words that precede the target (§12) |
| M9 | computing arrangements rather than derangements (§10) |
