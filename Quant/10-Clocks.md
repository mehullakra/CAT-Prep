# Clocks

> CAT quant. A clock is a circular track with two runners moving in the same direction at a 12 : 1 speed ratio. Every question is relative speed at 5.5° per minute.

Split out of `08-Time-Speed-Distance.md`. The circular-track machinery it builds on is in TSD §9.

---

## 1. Core idea

The minute hand and the hour hand are two runners on a 360° circular track, going the same way.

- Minute hand: 360° in 60 min = **6° per minute**
- Hour hand: 360° in 12 hours = **0.5° per minute**
- **Relative speed = 6 − 0.5 = 5.5° per minute**

That last number is the only thing you must memorise. Everything else in this file is derived from it.

**The one mistake that costs the most marks:** treating the hour hand as parked on its number. At 4:20 the hour hand is *not* at 4 — it has crept 20 × 0.5 = 10° past it. Assume otherwise and every angle answer is wrong.

---

## 2. Master formula

**Angle between the hands = |30H − 5.5M|**

where H = the hour, M = minutes past that hour.

Where it comes from:

- Hour-hand position measured clockwise from 12 = 30H + 0.5M
- Minute-hand position from 12 = 6M
- Difference = |30H + 0.5M − 6M| = |30H − 5.5M|

**If the result exceeds 180°, subtract from 360°** — the angle between two hands is always the smaller one.

**Worked example:** angle at 4:20.

- |30(4) − 5.5(20)| = |120 − 110| = **10°**

The decoy answer is 0°, which comes from assuming the hour hand sits exactly at 4 while the minute hand points at 4 as well.

**Worked example:** angle at 7:35.

- |30(7) − 5.5(35)| = |210 − 192.5| = **17.5°**

---

## 3. The four standard configurations

| Configuration | Angle | Per 12 hrs | Per 24 hrs |
|---|---|---|---|
| Coincide (overlap) | 0° | 11 | 22 |
| Opposite (straight line) | 180° | 11 | 22 |
| Straight line (either case) | 0° or 180° | 22 | 44 |
| Right angle | 90° | 22 | 44 |

**Why 11 and not 12:** in 12 hours the minute hand gains exactly 11 full laps on the hour hand, so there are 11 overtakes, not 12. This is the same result the circular-track formula gives — speed ratio 12 : 1 is already coprime, same direction, so meeting points = 12 − 1 = 11.

**Consequence:** the interval between successive coincidences is 720/11 = **65 5/11 minutes**, not 65. A clock whose hands coincide every 65 minutes is running fast — that's a standard question, not a typo.

---

## 4. Type 1 — When do the hands form a given angle?

**Method:** set the master formula equal to the target angle and solve for M. Because of the absolute value, expect **two answers per hour** for any non-zero angle.

**Worked example:** when do the hands coincide between 3 and 4 o'clock?

- |30(3) − 5.5M| = 0 ⟹ 90 = 5.5M ⟹ M = 90/5.5 = 180/11 = 16 4/11
- Answer: **3:16 4/11**

**Worked example:** when are the hands at 90° between 3 and 4?

- |90 − 5.5M| = 90 splits into two cases:
- 90 − 5.5M = 90 ⟹ M = 0 → **3:00 exactly**
- 90 − 5.5M = −90 ⟹ 5.5M = 180 ⟹ M = 360/11 = 32 8/11 → **3:32 8/11**

Always solve both signs. Reporting only one is the most common half-mark loss in this topic.

**Worked example:** when are the hands opposite between 5 and 6?

- |150 − 5.5M| = 180 ⟹ 150 − 5.5M = −180 ⟹ 5.5M = 330 ⟹ M = 60

M = 60 means it happens exactly at 6:00, i.e. at the boundary. The other case gives 5.5M = −30, negative and therefore invalid. **Some hours contain only one occurrence** — check that your M lands in [0, 60).

---

## 5. Type 2 — Faulty clocks (gaining or losing)

**Method:** treat it as a proportion between the time the clock *shows* and the true time elapsed. Set up the ratio once, then read the question to see which direction you're converting.

A clock gaining 5 min/hr advances 65 minutes for every 60 true minutes → ratio shown : true = 65 : 60.

**Worked example:** a clock gains 5 min/hr, set correctly at 8 a.m. What does it show at 3 p.m.?

- True elapsed = 7 hours
- Clock advances 65 min per true hour → 7 × 65 = 455 min = 7 hr 35 min
- It shows **3:35 p.m.**

**Reverse version — read the direction carefully:** "The clock shows 3 p.m. What is the true time?" Now flip the ratio: true elapsed = 7 × (60/65) = 6 hr 27 9/13 min, so the true time is about 2:28 p.m. Marks are lost here purely from converting the wrong way.

**Worked example — when is it correct again?** A clock loses 3 min/hr. When does it next show the correct time?

- To show the correct time again it must drift a full 12 hours = 720 minutes
- At 3 min lost per hour: 720/3 = 240 hours = **10 days**

The 720 is the key: a clock face repeats every 12 hours, not 24, so the drift needed is 720 minutes.

---

## 6. Type 3 — Mirror images

**Mirror time = 11:60 − given time.** Use 12:60 if the given time is between 12:00 and 1:00.

**Worked example:** mirror image of 4:35.

- 11:60 − 4:35 = **7:25**
- Sanity check: the two times should add to 12:00. 4:35 + 7:25 = 12:00 ✓

That check takes two seconds and catches every arithmetic slip in this type.

**Water-image (reflection in a horizontal surface) is a different question** — it's 12:60 minus the time only for a vertical mirror. CAT almost always means the vertical mirror; if it specifies water image, redraw rather than reuse this formula.

---

## 7. Type 4 — Hands overlapping in a given window

**Worked example:** how many times do the hands form a right angle between 2 p.m. and 6 p.m.?

- Right angles occur 22 times per 12 hours, i.e. on average once every 720/22 = 32 8/11 minutes
- Over a 4-hour window that's 4 × (22/12) = 7.33 → **7 times**, not 8

Don't just multiply hours by 2. The right angles are not evenly distributed across the hour boundaries — in each 12-hour cycle two of the expected 24 go missing (around 3 and 9 o'clock, where consecutive occurrences merge). When a window straddles those hours, count carefully rather than scaling.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Hour hand position | assumed parked at H | it moves 0.5° per minute, always |
| Angle at 4:20 | 0° | 10° |
| Coincidences in 12 hrs | 12 | 11 |
| Interval between coincidences | 65 min | 65 5/11 min |
| Right angles in 12 hrs | 24 | 22 |
| Solving \|30H − 5.5M\| = θ | one answer | usually two — solve both signs |
| M outside [0, 60) | accepted | invalid; that occurrence is in a different hour |
| Angle above 180° | reported as is | subtract from 360° |
| Faulty clock direction | same ratio both ways | shown→true and true→shown are reciprocals |
| "Correct time again" | drift of 24 hrs | drift of 12 hrs = 720 min |
| Counting angles in a window | hours × 2 | scale by 22 per 12 hrs and check boundaries |

---

**The one habit that fixes most errors:** write down the hour-hand position as 30H + 0.5M before anything else. The moment that 0.5M term is on the page, the "hour hand is parked" error becomes impossible — and that single error accounts for most wrong answers in this topic.

**Connection back to circular tracks:** speed ratio 12 : 1 is coprime, so the same-direction formula gives 12 − 1 = 11 meeting points — exactly the 11 coincidences per 12 hours. If circular tracks are solid, clocks cost almost nothing extra.

*Companion topic not yet covered: Calendars — pure modular arithmetic on 7, sharing no machinery with this file despite the surface similarity.*
