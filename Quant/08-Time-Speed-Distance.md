# Time, Speed & Distance (TSD)

> CAT quant. Every sub-topic traces back to one idea: with distance held constant, speed and time are inversely proportional.

Two sub-topics now live in their own files: `09-Races.md` and `10-Clocks.md`.

---

## 1. Core ratio trick

**Distance constant → Speed and Time are inversely proportional.**

Speed ratio a : b ⟹ Time ratio b : a

Roughly 60% of CAT TSD questions fall to this one line. Train yourself to flip the ratio instantly, without writing an equation.

**Worked example:** Walking at 3/4 of his usual speed, a man reaches office 20 minutes late. Find his usual time.

- Speed ratio (new : usual) = 3 : 4
- Time ratio (new : usual) = 4 : 3
- The difference of 1 part is the 20 minutes he lost
- Usual time = 3 parts = **60 minutes**

No equations, 15 seconds.

**Worked example:** Increasing his speed by 25%, a man reaches 10 minutes early. Find his usual time.

- New speed = 5/4 of usual → speed ratio new : usual = 5 : 4
- Time ratio new : usual = 4 : 5
- Difference of 1 part = 10 minutes
- Usual time = 5 parts = **50 minutes**

**The pattern to internalise:** convert the speed change into a ratio, invert it, and the given time difference is always the difference between the two parts. Which part is the answer depends on whether the question asks for the usual or the new time — read that carefully.

---

## 2. Unit conversions

- km/hr → m/s: multiply by **5/18**
- m/s → km/hr: multiply by **18/5**

Memorise the clean pairs, because CAT picks its numbers from this set: 36 km/hr = 10 m/s, 54 = 15, 72 = 20, 90 = 25, 18 = 5.

If a train question gives speed in km/hr and lengths in metres, convert first. Mixing units mid-solution is a silent error — the arithmetic looks fine and the answer is off by 3.6.

---

## 3. Average speed

| Situation | Formula |
|---|---|
| Equal distances, two speeds | 2ab / (a + b) — harmonic mean |
| Equal distances, three speeds | 3abc / (ab + bc + ca) |
| Equal **times** | ordinary average (a + b)/2 |

**The distinction is the whole point.** "Went at 40, returned at 60" is equal distance → 2(40)(60)/100 = **48 km/hr**. "Drove at 40 for an hour, then 60 for an hour" is equal time → **50 km/hr**.

**Trap:** for equal distances the answer is never the arithmetic mean. If (a+b)/2 appears among the options in an equal-distance question, it is the decoy — CAT includes it deliberately.

**When neither is equal**, fall back to the definition: total distance ÷ total time. Never average the speeds.

**Worked example:** A man covers the first 20 km at 40 km/hr and the next 30 km at 60 km/hr. Average speed?

- Time 1 = 20/40 = 0.5 hr, Time 2 = 30/60 = 0.5 hr
- Total = 50 km in 1 hr → **50 km/hr**

Here the times happened to be equal, so the arithmetic mean is right — but you should discover that, not assume it.

---

## 3b. Multi-sector journeys — average speed vs average time

A "multi-sector" journey is one broken into legs with different speeds. Two distinct questions get confused here:

- **Average speed** = total distance / total time. Weighted by **distance**, so it is a harmonic-type mean.
- **Average time per sector** = total time / number of sectors. Weighted by nothing — a plain mean of the leg times.

They answer different questions and are almost never numerically equal. Read which one is wanted.

**Method for any multi-sector problem:**
1. Tabulate each leg: distance, speed, time = d/s.
2. Sum the distances and sum the times **separately**.
3. Divide once, at the end.

**Worked example:** A journey has three legs: 60 km at 30 km/h, 60 km at 60 km/h, 60 km at 20 km/h.
- Times: 2, 1, 3 hours ⟹ total 6 hours for 180 km
- Average speed = 180/6 = **30 km/h**
- Average time per leg = 6/3 = **2 hours** — a different quantity entirely
- (Check against the §3 table: three equal distances ⟹ 3abc/(ab+bc+ca) = 108000/3600 = 30 ✓)

### Algebraic speed constraints

The harder CAT variant fixes the total time or total distance and asks for an unknown speed.

**Worked example:** A man covers 120 km in 4 hours, travelling part of the way at 20 km/h and the rest at 40 km/h. How far did he travel at 20 km/h?
- Let that distance be x ⟹ x/20 + (120 − x)/40 = 4
- Multiply by 40: 2x + 120 − x = 160 ⟹ x = **40 km**

**Worked example (a leg defined as a fraction):** A man travels the first third of a distance at 20 km/h, the next third at 30 km/h, and the rest at 60 km/h. Find his average speed.
- Let the total be 3d. Times = d/20 + d/30 + d/60 = (3d + 2d + d)/60 = 6d/60 = d/10
- Average = 3d/(d/10) = **30 km/h**

**The habit:** assume the total distance to be the LCM of the given speeds (or of the denominators). Here 60 makes every leg time an integer. This is the same LCM discipline as `11-Time-Work-Pipes-Cisterns.md` §1, and it removes fractions from the entire calculation.

---

## 3c. Relative motion with bearings — Pythagoras on positions

When two bodies move along **perpendicular** directions (north and east, or any right angle), do not use relative speed. Instead:

1. Write each body's **position** as a function of time.
2. Take the difference in each coordinate.
3. Apply **Pythagoras** to get the separation.

**Separation formula for perpendicular motion from the same point:** after time t at speeds u and v,

**distance apart = t·√(u² + v²)**

**Worked example:** A cyclist rides north at 15 km/h and another rides east at 20 km/h from the same point at the same time. How far apart are they after 2 hours?
- Distances = 30 km and 40 km ⟹ separation = √(900 + 1600) = **50 km**
- (Or 2 × √(225 + 400) = 2 × 25 = 50 ✓ — and note the 3-4-5 triple.)

**Worked example (different start points):** A is at the origin moving north at 10 km/h. B starts 30 km east of A and moves north at 4 km/h. Find their separation after 3 hours.
- After 3 h: A is at (0, 30), B is at (30, 12)
- Separation = √(30² + 18²) = √(900 + 324) = √1224 ≈ **34.99 km**

**Worked example (minimum separation — the hard variant):** Two ships: P at (0,0) sailing east at 10 km/h, Q at (0, 40) sailing south at 30 km/h. When are they closest?
- Positions at time t: P = (10t, 0), Q = (0, 40 − 30t)
- D² = 100t² + (40 − 30t)² = 100t² + 1600 − 2400t + 900t² = 1000t² − 2400t + 1600
- Minimum of a quadratic at t = 2400/(2·1000) = **1.2 hours**
- D² = 1000(1.44) − 2400(1.2) + 1600 = 1440 − 2880 + 1600 = 160 ⟹ D = **4√10 ≈ 12.65 km**

**The habit:** for "closest approach" questions, write D² (never D) as a quadratic in t and use the vertex formula t = −b/2a. Squaring keeps everything polynomial, and D is minimised exactly where D² is. See `13-Algebra.md` §2.

**Non-perpendicular bearings:** if the angle between the paths is θ rather than 90°, use the cosine rule instead: D² = a² + b² − 2ab·cosθ, with a and b the distances covered. The 60° and 120° cases (cos = ½ and −½) are the ones CAT picks.

---

## 4. Relative speed

- Same direction: |a − b|
- Opposite directions: a + b

Every "catch up", "overtake", "meet", or "gap closes" question is just **distance ÷ relative speed**.

**Worked example:** A thief is 200 m ahead, running at 8 km/hr. A policeman chases at 10 km/hr. How long to catch him?

- Relative speed = 10 − 8 = 2 km/hr = 2 × 5/18 = 5/9 m/s
- Time = 200 ÷ 5/9 = **360 seconds = 6 minutes**

**Worked example:** Two people start 100 km apart and walk toward each other at 4 and 6 km/hr. When do they meet?

- Relative speed = 4 + 6 = 10 km/hr
- Time = 100/10 = **10 hours**

---

## 5. Trains

| Situation | Distance covered |
|---|---|
| Crossing a pole, man, pillar, signal | length of train |
| Crossing a platform, bridge, tunnel | train + platform |
| Two trains crossing each other | sum of both lengths |
| Train overtaking a walking man | length of train, at relative speed |

Whenever both objects move, use relative speed. Whenever the object is stationary and has no length (pole, man), the distance is just the train's own length.

**Worked example:** A 150 m train crosses a 350 m platform in 25 s. Find its speed.

- Distance = 150 + 350 = 500 m, time = 25 s
- Speed = 20 m/s = 20 × 18/5 = **72 km/hr**

**Worked example:** Two trains of length 120 m and 180 m run in opposite directions at 40 and 50 km/hr. Time to cross each other?

- Relative speed = 90 km/hr = 90 × 5/18 = 25 m/s
- Distance = 120 + 180 = 300 m
- Time = 300/25 = **12 seconds**

Same trains in the same direction: relative speed = 10 km/hr = 25/9 m/s, time = 300 ÷ 25/9 = **108 seconds**. The nine-fold difference is why direction must be read before anything else.

---

## 6. Boats and streams

- Downstream D = b + s, Upstream U = b − s
- **b = (D + U)/2, s = (D − U)/2** — memorise these two
- If time upstream : time downstream = m : n, then b : s = (m + n) : (m − n)
- Round-trip average speed = (b² − s²)/b, always less than b

**Moving walkways and wind-assisted flights** are this exact structure with different nouns — same two formulas. **Escalators are only sometimes this structure**; see §6a before assuming.

**Worked example:** A boat covers 24 km downstream in 3 hrs and returns in 4 hrs. Find the speed of the boat and the stream.

- D = 24/3 = 8 km/hr, U = 24/4 = 6 km/hr
- b = (8 + 6)/2 = **7 km/hr**, s = (8 − 6)/2 = **1 km/hr**

**Worked example:** A man rows upstream in twice the time he takes downstream. If the stream flows at 2 km/hr, find his speed in still water.

- Time ratio up : down = 2 : 1 ⟹ b : s = (2 + 1) : (2 − 1) = 3 : 1
- s = 2 ⟹ b = **6 km/hr**

**The round-trip trap:** the average speed for a there-and-back river trip is never b. It's (b² − s²)/b, which is strictly less, because more time is spent in the slow direction. With b = 7, s = 1: average = (49 − 1)/7 = 48/7 ≈ 6.86, not 7.

---

## 6a. Escalators — the two different questions

An escalator question is one of two things, and using the wrong one is the standard way to lose it.

**If the question is about distance or time**, it *is* boats and streams (§6): the escalator is the stream, the person is the boat, effective speed = own speed ± escalator speed.

**If the question counts steps, it is not.** "Walking up a moving escalator a man takes 30 steps; running he takes 40; how many steps are visible when it is stopped?" — nobody's speed in metres is given, and there is no distance. This is a **rate problem in units of steps** (`11-Time-Work-Pipes-Cisterns.md` §1 is the same machinery).

**Core idea.** The staircase has a fixed number of visible steps N. While the person climbs, the escalator also delivers steps. So

**N = (steps the person takes) + (steps the escalator contributes during the same time)**

The escalator's contribution is (escalator rate) × (time taken), and time = (steps taken) / (person's rate). Everything is in steps per unit time, so no distance is ever needed.

**Method:**
1. Let the escalator move e steps in the time the person takes **one** step.
2. For each scenario, time ∝ number of steps the person took, so the escalator adds e × (that number).
3. Set the two expressions for N equal and solve for e, then for N.

**Worked example:** Walking, a man takes 30 steps to reach the top; running at twice the rate he takes 40. How many steps are visible?

- Let the escalator deliver e steps per one of his walking steps.
- **Walking:** he takes 30 steps, in that time the escalator gives 30e ⟹ N = 30 + 30e
- **Running:** he is twice as fast, so 40 running steps take the time of 20 walking steps ⟹ escalator gives 20e ⟹ N = 40 + 20e
- 30 + 30e = 40 + 20e ⟹ 10e = 10 ⟹ e = 1 ⟹ **N = 60**

**The rate-conversion step in bold, because it is the whole question:** taking 40 steps at double speed occupies the time of only 20 normal steps. Multiplying 40 by e instead of 20 is the planted error and gives 70.

**Downward on an upward escalator:** the escalator now works against him, so N = (steps taken) − (escalator's contribution), and the step count he needs is larger than N. Same equation, one sign flipped.

**Traps:**
- Treating a steps question as boats and streams. There is no distance, so b ± s has nothing to attach to.
- Forgetting to convert step counts into equal *times* before adding the escalator's share.
- Assuming the answer is the average of the two step counts. Here that gives 35, not 60.

---

## 7. Two-body meeting (bouncing between endpoints)

Two people start from A and B moving toward each other and keep bouncing back and forth between the ends.

- 1st meeting: combined distance = D
- 2nd meeting: combined distance = 3D
- **nth meeting: combined distance = (2n − 1)D**

**Worked example:** Two runners start from opposite ends of a 300 m stretch at 5 and 10 m/s, bouncing back and forth. When and where do they meet the 3rd time?

- Combined distance for the 3rd meeting = 5 × 300 = 1500 m
- Combined speed = 15 m/s → time = 1500/15 = **100 s**
- In 100 s the slower runner covers 500 m: from A he goes 300 to B, then 200 back → he is **200 m from B**, i.e. 100 m from A

Compute the position from the *slower* runner's total distance and fold it back and forth along the track. Doing this for both runners is a free consistency check.

---

## 7a. Two-body meeting when the speeds are swapped at the meeting point

A CAT variant of §7: "on meeting they immediately interchange their speeds and directions." The standard machinery half-survives, and knowing exactly which half is the whole point.

**What still holds:** the **combined speed never changes** (the same two speeds are in play, just attached to different people). So the timing rule of §7 is untouched — the nth meeting still happens when the pair has covered a **combined (2n − 1)D**, at time (2n − 1)D / (v₁ + v₂).

**What breaks:** the split of that combined distance. In §7 the slower runner always covers v₁/(v₁+v₂) of it; once the speeds swap, that ratio is no longer valid and **you cannot locate the meeting point from the combined distance**. You must walk the timeline leg by leg.

**Method:**
1. Get the first meeting point from the original speeds — nothing has swapped yet.
2. Swap the speeds, reverse both directions, and compute when each reaches their home city. These are usually *different* times, so handle them in order.
3. Between the two turnarounds, one is heading out and the other is still heading home — check whether they meet in that window before assuming they don't.
4. After both have turned, close the remaining gap at the combined speed.
5. Use total combined distance = (2n − 1)D as a **check** at the end, not as the method.

**Worked example:** X and Y are 1000 km apart. Ravi leaves X at 20 kmph and Mohan leaves Y at 30 kmph, towards each other. On meeting they interchange both speeds and directions; on reaching their own starting cities they turn round and continue at those speeds until they meet again. How far apart are the two meeting points?

- **First meeting:** combined 1000 at 50 kmph ⟹ t = 20 h. Ravi has done 400, so **M₁ is 400 km from X**.
- **Swap:** Ravi now 30 kmph heading back to X (400 km away); Mohan now 20 kmph heading back to Y (600 km away).
- Ravi reaches X at t = 20 + 400/30 = 33⅓ h. Mohan reaches Y at t = 20 + 600/20 = 50 h.
- **The gap window (33⅓ → 50 h):** Ravi is now going X → Y at 30, and Mohan is *still* going toward Y at 20 — same direction, Ravi behind. Ravi gains only 10 kmph on a 666⅔ km gap, so no meeting here. At t = 50, Ravi is at 500 and Mohan is at 1000.
- **After both turn:** gap 500, combined 50 ⟹ 10 h ⟹ t = 60 h, both at **M₂ = 800 km from X**.
- Distance between meeting points = 800 − 400 = **400 km**
- Check: combined distance by t = 60 is 1600 + 1400 = 3000 = 3D ✓ (the 2nd meeting, as expected)

**Traps:**
- Using the §7 position rule. Ravi actually covers 1600 of the 3000, not 20/50 × 3000 = 1200 — the swap changes the split even though the total is unchanged.
- Assuming both reach home at the same moment. They almost never do; the interval between the two turnarounds is where the question hides.
- Skipping the same-direction window. If the trailing runner were fast enough, the meeting would happen there and the answer would change completely.
- Answering with a single meeting point instead of the **distance between** the two.

---

## 8. The √ trick (high frequency)

A starts from P, B starts from Q, moving toward each other. They meet after time t. A then takes t₁ more to reach Q, B takes t₂ more to reach P.

- **t = √(t₁ × t₂)**
- Speed of A : Speed of B = √t₂ : √t₁

**Worked example:** After meeting, A takes 4 hrs to finish and B takes 9 hrs.

- t = √(4 × 9) = √36 = **6 hours** before the meeting
- Speed ratio A : B = √9 : √4 = **3 : 2**

Note the inversion in the ratio: the runner with the *shorter* remaining time is the faster one, so t₂ sits over A. Getting this upside down is the only real risk in an otherwise free question.

---

## 9. Circular tracks

**Core idea:** every time two runners meet, one has gained a full lap (same direction) or together they have covered a full lap (opposite directions). Meeting points are always equally spaced around the track, and how many there are depends only on the speed ratio, not on the track length.

**Method**

1. **Reduce the speed ratio to lowest terms**: a : b, coprime. Non-negotiable — the formula fails if you skip it.
2. Count the distinct meeting points:

   | Direction | Meeting points |
   |---|---|
   | Opposite directions | a + b |
   | Same direction | a − b (larger minus smaller) |

3. Space them equally: circumference ÷ number of points. If both start together from the same point, the start is always one of them.
4. First meeting time:
   - Opposite: L / (sum of speeds)
   - Same: L / (difference of speeds)

   Subsequent meetings repeat at that same interval.

**Two different questions — do not confuse them:**

- "When do they meet **anywhere** on the track?" → step 4 above.
- "When do they meet **at the starting point**?" → LCM of the individual lap times, LCM(L/a, L/b). Completely different formula.

**Worked example:** 900 m circular track, speeds 15 m/s and 25 m/s, starting together.

- Ratio 15 : 25 = 3 : 5 (coprime)
- Opposite directions: 3 + 5 = **8 meeting points**, spaced 900/8 = 112.5 m apart; first meeting at 900/(15+25) = **22.5 s**
- Same direction: 5 − 3 = **2 meeting points**, spaced 900/2 = 450 m apart; first meeting at 900/(25−15) = **90 s**
- Meeting at the start: lap times 60 s and 36 s → LCM(60, 36) = **180 s**

**Worked example (ratio difference of 1):** 600 m track, A at 10 m/s, B at 15 m/s, same direction, starting together.

- Ratio 10 : 15 = 2 : 3 (coprime) → meeting points = 3 − 2 = **1**, so they only ever meet at the start
- First meeting = 600/(15 − 10) = **120 s**
- Lap times 60 s and 40 s → LCM = 120 s. Matches, exactly because there is only one meeting point.

**Three or more runners:** compute the pairwise meeting times, then take the LCM of those.

**Traps specific to circular tracks:**

- Forgetting to reduce the ratio, opposite direction: 15 + 25 = 40 points (wrong) vs 3 + 5 = 8 (correct)
- Forgetting to reduce, same direction: 25 − 15 = 10 (wrong) vs 5 − 3 = 2 (correct)
- Ratio difference of 1 in the same direction gives exactly 1 meeting point — students assume there must be more
- If runners start from *different* points, the count of meeting points is unchanged, but the start is no longer guaranteed to be one of them; the locations shift

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Average speed, equal distances | (a + b)/2 | 2ab/(a + b) |
| Average speed, equal times | 2ab/(a + b) | (a + b)/2 |
| Mixed units | km/hr with metres | convert with 5/18 first |
| Train crossing a platform | train length only | train + platform |
| Two trains, direction ignored | one relative speed | same dir → \|a − b\|, opposite → a + b |
| River round trip | average = b | (b² − s²)/b, always less |
| Circular ratio not reduced | 15 + 25 = 40 points | reduce first → 8 points |
| Meet anywhere vs at start | same formula | L/(sum or difference) vs LCM of lap times |
| √ trick ratio | √t₁ : √t₂ | A : B = √t₂ : √t₁ |
| nth bounce meeting | nD | (2n − 1)D |
| Ratio inverted | speed ratio used as time ratio | invert it — they're inverse |
| Speeds swapped at the meeting | (2n−1)D split by original speeds | timing survives, the split does not — walk the timeline |

---

**The one habit that fixes most errors:** before computing, write down which of the three quantities is being held constant. Distance constant → invert the ratio. Time constant → distances are proportional to speeds. Speed constant → it's a plain proportion. Naming the constant first makes the right tool obvious and eliminates the average-speed and ratio-inversion errors in one move.

*Related files: `09-Races.md` (beats, head starts, dead heats), `10-Clocks.md` (the 12 : 1 same-direction case of §9). Companion topic not yet covered: Calendars — pure modular arithmetic on 7, sharing no machinery with TSD.*
