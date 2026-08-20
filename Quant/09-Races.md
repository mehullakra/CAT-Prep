# Races

> CAT quant. Every race statement is a disguised speed ratio. Convert the beat into "when A runs L, B runs L − x", and the whole topic becomes one ratio.

Split out of `08-Time-Speed-Distance.md`. Circular-track races (laps, meeting points) stay there — see TSD §9.

---

## 1. Core idea

A race is two runners covering the **same time**, not the same distance. When time is constant, distance is directly proportional to speed:

**Speed ratio = Distance ratio (same time)**

So the only thing you ever need to extract from a race statement is: *when A covers the full length L, how far has B covered?*

Once you have that pair — say A covers 100 while B covers 80 — you have the speed ratio 100 : 80 = 5 : 4, and every other question about those two runners follows from it.

**The one habit:** rewrite every race statement in the form "A : L, B : (L − x)" before doing anything else. Beats given in seconds, head starts, and dead heats are all just different ways of hiding that same pair.

---

## 2. Reading the language

These four phrases all mean the identical thing:

| Phrase | Meaning |
|---|---|
| "A beats B by 20 m" in a 100 m race | A runs 100 while B runs 80 |
| "A gives B a start of 20 m" | B starts 20 m ahead, so B runs 80 while A runs 100 |
| "A gives B a 20 m head start" | same as above |
| "A can give B 20 points in a game of 100" | when A scores 100, B scores 80 |

All four give speed ratio A : B = 100 : 80 = **5 : 4**.

**"A beats B by t seconds"** is different — it's a time gap, not a distance gap, and must be converted before use. See §4.

**A dead heat** means the race finishes in an exact tie. It's the phrase that tells you a head start has been tuned so both runners arrive together.

---

## 3. Type 1 — Beat given as a distance

**Method:** write the pair, reduce the ratio, answer everything from it.

**Worked example:** In a 100 m race, A beats B by 20 m. If the race were 200 m, by how much would A win?

- A : B = 100 : 80 = 5 : 4
- Over 200 m: when A runs 200, B runs 200 × 4/5 = 160
- A wins by 200 − 160 = **40 m**

Note that the beat scales with race length — it is *not* fixed at 20 m. Assuming it stays 20 m is the standard wrong answer.

**Worked example:** A runs 100 m in 20 s, B in 25 s. By how much does A beat B?

- When A finishes (20 s), B has run 20 s × (100/25) = 20 × 4 = 80 m
- A beats B by **20 m**

---

## 4. Type 2 — Beat given as a time (or both)

**Method: convert the time gap into distance using the LOSER's speed.** The beaten runner is the one still on the track during those extra seconds, so it's their speed that matters.

**Worked example:** In a 100 m race, A beats B by 20 m *or* by 5 seconds.

Read it as: B needs 5 extra seconds to cover the last 20 m.

- B's speed = 20 m / 5 s = 4 m/s
- B's time for the full 100 m = 100/4 = 25 s
- A's time = 25 − 5 = **20 s**

The "or" phrasing is a gift — it hands you both a distance and a time for the same gap, which is exactly what you need to get a speed. Whenever you see "beats by x m or t seconds", compute x/t immediately; that's the loser's speed.

**If only a time is given**, you must find the loser's speed from elsewhere in the question before you can convert.

---

## 5. Type 3 — Chaining three runners

**Worked example:** In a 100 m race, A beats B by 20 m, and B beats C by 10 m. By how much does A beat C?

Do it in the same-distance currency, step by step:

- A : 100 ⟹ B : 80
- B : 100 ⟹ C : 90, so B : 80 ⟹ C : 80 × 90/100 = 72
- When A runs 100, C has run 72 → A beats C by **28 m**

**Shortcut formula** (worth memorising): if A beats B by x and B beats C by y in a race of length L,

**A beats C by x + y − xy/L**

Check: 20 + 10 − (20 × 10)/100 = 30 − 2 = **28** ✓

The naive answer is 30. The −xy/L correction exists because the second beat is measured over B's *full* 100 m, but B only ran 80 m in the real race.

**Same structure, points version:** A can give B 20 points and C 28 points in a game of 100. How many can B give C?

- A : 100 ⟹ B : 80 and C : 72
- So when B scores 80, C scores 72 → when B scores 100, C scores 72 × 100/80 = 90
- B can give C **10 points**

---

## 6. Type 4 — Dead heat

A dead heat is a tie. The question is usually "what head start makes it a tie?"

**Method:** both runners take the same total time. Give the slower runner a start of d metres so they only need to run (L − d).

**Worked example:** A runs 100 m in 20 s, B in 25 s. What start must A give B for a dead heat over 100 m?

- B's speed = 100/25 = 4 m/s
- The race must last 20 s (A's time)
- In 20 s, B covers 4 × 20 = 80 m
- So B needs a start of 100 − 80 = **20 m**

Notice this is numerically the same as "A beats B by 20 m" — because a head start of exactly the beat distance converts a win into a tie. That equivalence is the fastest way to check a dead-heat answer.

---

## 7. Type 5 — Head starts in time

"A gives B a start of 5 seconds" means B begins running 5 seconds earlier. This is **not** the same as a distance start — B still runs the full length L, just with a head start on the clock.

**Method:** put both runners on one common clock, started when the *first* runner moves. Compute each finishing time on that clock and compare.

**Worked example:** A's speed is 5 m/s, B's is 4 m/s. A gives B a 4-second start in a 100 m race. Who wins, and by how much?

- Common clock starts when B moves, at t = 0
- B runs the full 100 m at 4 m/s → finishes at t = 100/4 = 25 s
- A starts at t = 4 and takes 100/5 = 20 s → finishes at t = 4 + 20 = **24 s**
- A wins by 25 − 24 = **1 second**
- In distance: at t = 24, B has covered 4 × 24 = 96 m, so A wins by **4 m**

**Watch the boundary:** with a 5-second start instead of 4, B finishes at 25 s and A at 5 + 20 = 25 s — a dead heat. Time starts are sensitive; always compute both finishing times rather than estimating.

Mixing the two runners' personal clocks is where this type goes wrong. One clock, both finish times, compare.

---

## 8. Type 6 — Games of points

Identical machinery, different noun. "A game of 100" means the winner is the first to 100 points.

- "A can give B 20 points in a game of 100" → A : B = 100 : 80 = 5 : 4
- All chaining, dead-heat, and scaling logic carries over unchanged

**Worked example:** A can give B 10 points in a game of 60. How many points can A give B in a game of 90?

- Ratio A : B = 60 : 50 = 6 : 5
- In a game of 90: when A scores 90, B scores 90 × 5/6 = 75
- A can give B 90 − 75 = **15 points**

The beat scales with the game length, exactly as it does with race length.

---

## 9. Type 7 — Multiple laps and overtaking

If the race is several laps on a circular track, it stops being a pure ratio question and becomes a relative-speed question. Use the circular-track machinery in `08-Time-Speed-Distance.md` §9 instead:

- "A laps B" = A has gained one full circumference on B
- Time to lap = circumference / (difference of speeds)

The tell: any mention of laps, rounds, or "meets again" means circular tracks, not this file.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Beat assumed constant across race lengths | 20 m beat in 100 m stays 20 m in 200 m | it scales: 40 m |
| Chaining two beats | 20 + 10 = 30 m | x + y − xy/L = 28 m |
| Converting a time beat | uses the winner's speed | use the **loser's** speed |
| Head start direction | B runs the full L | B runs L − x |
| "Beats by x m or t s" | treated as two separate facts | it's one gap — x/t is the loser's speed |
| Dead heat | assumed to need more start than the beat | start = the beat distance exactly |
| Time head start | runners' personal clocks mixed | put everything on one common clock |
| Points game treated as new topic | fresh formulas | identical to distance races |
| Laps/rounds solved by ratio | distance ratio | relative speed — go to circular tracks |

---

**The one habit that fixes most errors:** before computing anything, write the single line "when A does L, B does ___". If you cannot fill that blank from the question, you have not finished reading it. Every race question in CAT is solvable the moment that line exists.

**Sanity check:** the faster runner must always have the larger number in the ratio. If your ratio says otherwise, you've inverted a head start — the most common inversion in this topic.
