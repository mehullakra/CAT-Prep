# CAT Prep — Index

Master lookup for every concept covered so far. Purpose: when a problem can't be solved, find the concept here instead of re-deriving it or re-explaining it from scratch.

## How to use this (for Mehul, and for Claude in future sessions)

1. Stuck on a problem → identify the sub-topic it belongs to (e.g. "two runners on a track" → circular tracks; "pipe filling and draining" → pipes and cisterns).
2. Look it up in the tables below → open that file → jump to that section. The section should already have the formula, the method, a worked example, and the common traps.
3. If the concept genuinely **is not** in the table/file — it's a new sub-topic, not just a new problem using an existing one — add it:
   - Add a new `##` section to the relevant file (or create a new file under `Quant/` if it's a new topic area).
   - Use the same format as existing sections: core idea → method/formula → worked example → traps.
   - Add a row to the lookup table below pointing to it.
4. Don't duplicate a formula across files. If a sub-topic connects to another (like Clocks ↔ Circular Tracks), note the connection and cross-reference instead of copy-pasting.

Every topic file ends with a **Traps** table; most also end with **Practical exam habits**. Check those before re-reading the theory.

---

## Quick file directory

| File | Covers |
|---|---|
| `Quant/01-Number-System.md` | divisibility, primes, HCF/LCM, remainders, digit sums, Diophantine |
| `Quant/02-Percentages.md` | % change, reciprocal trick, successive change, DI growth |
| `Quant/03-Ratio-Proportion-Variation.md` | ratios, proportion, variation, partnership |
| `Quant/04-Means-and-Weighted-Averages.md` | averages, weighted average, AM/GM/HM |
| `Quant/05-Mixtures-and-Alligation.md` | alligation cross, concentration, replacement |
| `Quant/06-Profit-Loss-Discount.md` | CP/MP/SP, discounts, false weights, adulteration |
| `Quant/07-Simple-Compound-Interest.md` | SI, CI, instalments, depreciation |
| `Quant/08-Time-Speed-Distance.md` | TSD, trains, boats, circular tracks |
| `Quant/09-Races.md` | beats, dead heats, head starts, games of points |
| `Quant/10-Clocks.md` | angle formula, faulty clocks, mirror images |
| `Quant/11-Time-Work-Pipes-Cisterns.md` | LCM method, M-D-H, wages, pipes |
| `Quant/12-Calendars.md` | odd days, day of the week, repeating calendars |
| `Quant/13-Algebra.md` | identities, quadratics, surds, inequalities, functions |
| `Quant/14-Logarithms.md` | laws, log equations, nested logs, log inequalities |
| `Quant/15-Progressions-AP-GP.md` | AP, GP, HP, AGP, telescoping |
| `Quant/16-Functions-and-Graphs.md` | domain and range, [x] and {x}, transformations, counting solutions, maxima–minima |
| `Quant/17-Triangles.md` | angles, triangle essentials, similarity and area ratios, centres, trigonometry, folding |
| `Quant/18-Circles.md` | chords, tangents, segments, cyclic quadrilaterals, two-circle configurations |
| `Quant/19-Quadrilaterals-and-Polygons.md` | parallelograms, trapezium, kites, polygons, regular-polygon metrics, optimisation |
| `Quant/20-Mensuration.md` | solids, scaling, recasting, combined solids, painted cube, unfolding |
| `Quant/21-Coordinate-Geometry.md` | distance, section formula, lines, shoelace area, circles on axes |
| `Quant/22-Set-Theory-Venn.md` | two/three-set formulas, 2×2 tables, max–min of overlaps |
| `Quant/23-PnC-Probability.md` | arrangements, selections, probability, expected value |
| `Quant/Reference/Calculation-Toolkit.md` | tables, squares, cubes, fast arithmetic |
| `VARC/Vocabulary.md` | 127 words grouped by meaning, with synonyms and antonyms |

**The two-digit prefix is the study order** — read them 01 → 23. It follows the prerequisite chain: Number System first because Time & Work and Calendars need it, arithmetic next, then algebra, then Functions & Graphs (which needs Algebra §2 and §6), then geometry (Triangles before Circles, since a diameter turns a circle question into a triangle one), then Set Theory before PnC. Practice files and the topic order inside `CAT-Quant-Test.html` use the same numbers.

Every topic file above has a companion set at `Quant/Practice/<same name>-Practice.md`, except `22-Set-Theory-Venn.md`, `21-Coordinate-Geometry.md` and `16-Functions-and-Graphs.md`, which have notes but no practice set yet.

---

## Lookup table

### Number System — `Quant/01-Number-System.md`

| Topic / keyword | Section |
|---|---|
| The three core tools (factorise, mod, bound) | §1 The three tools |
| Divisibility rules (7, 11, 13, composite divisors) | §2 Divisibility rules |
| Terminating vs recurring decimals; length of the recurring block | §2a Terminating and recurring decimals |
| Parity arguments; "no integer solution exists" | §2b Parity — the even/odd test |
| Number of factors, sum of factors, product of factors | §3 Prime factorisation |
| HCF and LCM, HCF×LCM = product | §4 HCF and LCM |
| Bells tolling, largest tile, least number leaving remainder r | §4a HCF and LCM word problems |
| Unit digit, cyclicity of powers | §5 Unit digit and cyclicity |
| Last two digits of a power; the …76 fixed point | §5a Last two digits |
| Remainder theorems (Fermat, Wilson, negative remainders) | §6 Remainder theorems |
| Digit sum of Nᵏ, F(N) functions | §7 Digit-sum functions on powers |
| Counting numbers under divisibility + digit-sum constraints | §8 Divisibility + digit-sum counting |
| Surd and exponent ratio simplification | §9 Surd and exponent ratios |
| Perfect squares/cubes, smallest n to make a perfect power | §10 Perfect squares, cubes, least n |
| Perfect square / cube / 6th power deduced from the factor count | §10a Reading N's structure back from its factor count |
| Equation between products of prime powers; equate exponents per prime | §9a Equations in exponents |
| Integer solutions of ax + by = c | §11 Diophantine equations |
| Highest power of a prime in n! (Legendre) | §12 Factorials — highest powers and trailing zeros |
| Highest power of a *composite* in n!; trailing zeros in any base | §12 Factorials — highest powers and trailing zeros |
| Base conversion, arithmetic inside a base, valid digits | §13 Base systems |
| Digit-sum divisibility in base b ((b−1) plays the role of 9) | §13 Base systems |
| Repunits Rₓ = (10ˣ − 1)/9, digit-pattern numbers | §13a Repunits and digit-pattern numbers |

### Percentages — `Quant/02-Percentages.md`

| Topic / keyword | Section |
|---|---|
| Percentage as a multiplier | §1 The core idea |
| Fraction ↔ percentage table | §2 Fraction ↔ percentage table |
| Percentage change and which base to use | §3 Percentage change and the base |
| Reciprocal relationship (x% increase ↔ y% decrease) | §4 The reciprocal relationship |
| Successive percentage changes | §5 Successive changes |
| % change in a dimension → area/volume (square/cube it) | §5 Successive changes |
| Absolute +1 cm to a side ⟹ area up 100/l %; recovering l from the % | §5a An absolute change in a dimension |
| Population/price after successive changes | §6 Type 1 |
| Price–consumption, expenditure constant | §7 Type 2 |
| Price–consumption when expenditure also changes | §7a Generalised price–consumption |
| "n more/fewer items for the same money" → find the price | §7b Recovering the actual price |
| Percentage points vs percentage | §8 Type 3 |
| Successive percentage of a remainder | §9 Type 4 |
| Remainder chain with money added back; closing equation | §9a Chains with money added back |
| Election, exam and pass-mark problems | §10 Type 5 |
| Growth rates in DI | §11 Type 6 |
| Percentage of a percentage | §12 Percentage of a percentage |
| Overall % change of a composite/portfolio; swapped rates | §13 Type 7 |

### Ratio, Proportion & Variation — `Quant/03-Ratio-Proportion-Variation.md`

| Topic / keyword | Section |
|---|---|
| Ratio as a multiplier k | §1 The core idea |
| Manipulating ratios, adding/subtracting terms | §2 Basic manipulations |
| Combining a : b and b : c | §3 Combining ratios |
| Proportion, mean proportional | §4 Proportion |
| Componendo and dividendo | §5 Componendo and dividendo |
| Ratio changes after adding/removing quantity | §6 Type 1 |
| Dividing a sum in a ratio | §7 Type 2 |
| Direct, inverse, joint variation | §8 Type 3 |
| Equal ratios / k-theorem | §9 Type 4 |
| Partnership profit sharing | §10 Type 5 |
| Ratio of ratios, chained comparisons | §11 Type 6 |
| Redistribution and exchange word problems | §12 Type 7 |
| Incomes in a band, multiples of 100, whole expenditures — "which cannot be" | §12a Type 8 — Ratios pinned by integrality and a range |

### Means & Weighted Averages — `Quant/04-Means-and-Weighted-Averages.md`

| Topic / keyword | Section |
|---|---|
| Average as a balance point, deviation method | §1 The core idea |
| Adding a constant, scaling, properties | §2 Properties worth using |
| Weighted average formula | §3 Weighted average |
| Weighted average = alligation backwards | §4 Weighted average = alligation |
| Replacement problems (one member swapped) | §5 Type 1 |
| Correction problems (wrong value recorded) | §6 Type 2 |
| Average speed as harmonic mean | §7 Type 3 |
| AM, GM, HM and AM ≥ GM ≥ HM | §8 The three means |
| Average growth rate (GM) | §9 Type 4 |
| Averages of AP-like sequences | §10 Type 5 |
| Median, mode, when the mean misleads | §11 Type 6 |
| Averages with unknown counts | §12 Type 7 |
| Reconstructing sub-group values from group averages | §13 Type 8 |
| Average shifts by d when a sub-group is removed; solving for n and A | §13a Type 9 — When removing a sub-group shifts the average |

### Mixtures & Alligation — `Quant/05-Mixtures-and-Alligation.md`

| Topic / keyword | Section |
|---|---|
| Why quantities are the *inverse* of the distances from the mean | §1 Core idea |
| Alligation cross, cheap/dear mixing ratio | §2 The alligation cross |
| What alligation can and can't be applied to | §3 What alligation works on |
| Concentration (alcohol %, milk %, purity), adulteration ratio | §4 Type 1 |
| Repeated replacement, (1 − x/V)ⁿ | §5 Type 2 |
| Three or more ingredients | §6 Type 3 |
| Mixing two existing mixtures | §7 Type 4 |
| Solving for the poured amounts from what is left in the vessel | §7a Type 4b — Component accounting |
| Alligation on profit %, interest rates, ages, speeds | §8 Type 5 |

### Profit, Loss & Discount — `Quant/06-Profit-Loss-Discount.md`

| Topic / keyword | Section |
|---|---|
| CP/MP/SP chain | §1–2 Core idea, base relationships |
| Multiplying factors | §3 Multiplying factors |
| Marked price with discount → profit % | §4 Type 1 |
| Successive discounts | §5 Type 2 |
| Same SP, one at x% profit + one at x% loss | §6 Type 3 |
| False weights, dishonest dealer gain % | §7 Type 4 |
| Adulteration (P&L version) | §8 Type 5 |
| CP of n articles = SP of m articles | §9 Type 6 |
| "Buy X get Y free", bulk offers | §10 Type 7 |
| Comparing profit across items | §11 Type 8 |
| Markup + discount + wastage combined | §12 Type 9 |

### Simple & Compound Interest — `Quant/07-Simple-Compound-Interest.md`

| Topic / keyword | Section |
|---|---|
| SI and CI formulas | §1 The core idea |
| Principal, amount, rate, terminology | §2 Terminology |
| Half-yearly, quarterly compounding | §3 Compounding more than once a year |
| CI − SI for 2 and 3 years | §4 The SI–CI difference formulas |
| Finding rate or time from two amounts | §5 Type 1 |
| Doubling, tripling, rule of 72 | §6 Type 2 |
| Instalments and EMIs | §7 Type 3 |
| Different rates in different years | §8 Type 4 |
| Depreciation and population growth | §9 Type 5 |
| "g% of the initial value" = simple growth; integrality pinning the rate | §9a Type 5b — Growth as a percentage of the initial value |
| Splitting a sum between two rates | §10 Type 6 |
| Fast CI approximation | §11 Useful approximation |

### Time, Speed & Distance — `Quant/08-Time-Speed-Distance.md`

| Topic / keyword | Section |
|---|---|
| Speed–time inverse ratio trick | §1 Core ratio trick |
| km/h ↔ m/s conversion | §2 Unit conversions |
| Average speed (equal distance / equal time) | §3 Average speed |
| Multi-sector journeys, average speed vs average time | §3b Multi-sector journeys |
| Relative motion with bearings, Pythagoras on positions | §3c Relative motion with bearings |
| Relative speed, catch-up and overtake | §4 Relative speed |
| Trains crossing pole/platform/each other | §5 Trains |
| Boats and streams, upstream/downstream | §6 Boats and streams |
| Escalators: distance type vs steps-counted type | §6a Escalators — the two different questions |
| Two people bouncing between two points, nth meeting | §7 Two-body meeting |
| Same, but the two swap speeds on meeting | §7a Two-body meeting when the speeds are swapped |
| √(t₁t₂) trick | §8 The √ trick |
| Circular tracks, meeting points, meeting at start | §9 Circular tracks |

### Races — `Quant/09-Races.md`

| Topic / keyword | Section |
|---|---|
| Same time ⟹ speed ratio = distance ratio; rewrite as "A : L, B : (L − x)" | §1 Core idea |
| "Beats by x m / x sec" language | §2 Reading the language |
| Beat given as a distance | §3 Type 1 |
| Beat given as a time (or both) | §4 Type 2 |
| Chaining three runners | §5 Type 3 |
| Dead heat | §6 Type 4 |
| Head starts in time | §7 Type 5 |
| Games of points (billiards-style) | §8 Type 6 |
| Multiple laps and overtaking | §9 Type 7 |

### Clocks — `Quant/10-Clocks.md`

| Topic / keyword | Section |
|---|---|
| 5.5° per minute relative speed | §1 Core idea |
| Angle between hands, \|30H − 5.5M\| | §2 Master formula |
| Coincide / opposite / right angle counts per 12 hrs | §3 The four standard configurations |
| When do hands form a given angle | §4 Type 1 |
| Faulty clocks, gaining/losing, correct again | §5 Type 2 |
| Mirror images | §6 Type 3 |
| Counting configurations in a time window | §7 Type 4 |

### Time & Work, Pipes & Cisterns — `Quant/11-Time-Work-Pipes-Cisterns.md`

| Topic / keyword | Section |
|---|---|
| LCM method for work problems | §1 Core idea |
| Efficiency inverse to time | §2 Efficiency is inverse to time |
| Men-Days-Hours (M-D-H) formula | §3 The M-D-H formula |
| Alternate-day work, cycle method | §4 Alternate days |
| People joining or leaving midway | §5 People joining or leaving |
| "Leaves k days before completion" — departure pegged to an unknown finish | §5a Departures defined backwards from the finish |
| Splitting wages by work done | §6 Wages |
| Pipes filling/emptying, leaks, staggered opening | §7 Pipes and cisterns |
| Fractions of the work | §8 Fractions of the work |
| Individual rates from pairwise completion times | §9 Individual rates |
| Ratio of work rates | §10 Ratio of work rates |
| Partial work then remainder by one worker | §11 Partial work |

### Calendars — `Quant/12-Calendars.md`

| Topic / keyword | Section |
|---|---|
| Odd days, day codes (0 = Sunday) | §1 Core idea — odd days |
| Leap year rule, odd days per year and per century | §2 Odd days in a year |
| Odd days per month | §3 Odd days in a month |
| Day of the week for a given date | §4 Type 1 |
| Day of the week from a given reference date | §4 Type 1 (shortcut) |
| Which year repeats a given year's calendar | §5 Type 2 |
| 53 Sundays, probability questions | §6 Type 3 |
| 5 Mondays in a month, weekday counting | §6 Type 3 |
| Days between two dates | §7 Type 4 |

### Algebra — `Quant/13-Algebra.md`

| Topic / keyword | Section |
|---|---|
| Standard identities, x + 1/x chain | §1 The identities that actually appear |
| Binomial theorem: general term, middle term, coefficient of xᵏ, sum of coefficients | §1a The binomial theorem |
| Roots, discriminant, sum/product of roots | §2 Quadratics |
| Location of roots: both > k, opposite signs, one root in an interval | §2a Location of the roots |
| Biquadratic, aˣ substitution, palindromic, √x substitution | §2b Equations reducible to a quadratic |
| Symmetric systems, cubics | §3 Higher-degree and symmetric systems |
| Remainder theorem, factor theorem, rational roots, quadratic-divisor remainder | §3b Remainder and factor theorem |
| Finite differences P(x+1) − P(x), telescoping to P(b) − P(a) | §3a Finite differences |
| Rationalisation, surd equations | §4 Surds |
| Comparing surds and large powers (2¹⁰⁰ vs 3⁷⁰) | §4a Comparing surds and large powers |
| a + b + c = 0 ⟹ a³ + b³ + c³ = 3abc | §5 The a + b + c = 0 identity |
| AM–GM, maxima and minima, modulus inequalities | §6 Inequalities and maxima–minima |
| Maximise xᵃyᵇzᶜ under a linear constraint (split by exponents) | §6a AM–GM with split terms |
| Sum-of-moduli inequality, counting integer solutions | §6b Inequalities with a sum of moduli |
| Wavy curve / sign scheme; rational and higher-degree inequalities | §6c The wavy curve |
| Functions and graphs (moved out of this file) | §7 → `16-Functions-and-Graphs.md` |
| Word problems into linear equations | §8 Linear equations in word problems |
| "Needs ₹x more to buy one" — name the leftover, not the prices | §8b The shortfall trick |
| Symmetric system ax+by=k, bx+ay=k with a parameter; sign constraints | §8a Symmetric linear systems with a parameter |

### Logarithms — `Quant/14-Logarithms.md`

| Topic / keyword | Section |
|---|---|
| Definition, why logs behave the way they do | §1 The definition |
| Product, quotient, power, base-change laws | §2 The laws |
| log 2, log 3, log 7 values worth knowing | §3 Values worth knowing |
| Log equation reducing to a quadratic | §4 Type 1 |
| Nested log equations | §5 Type 2 |
| Product-zero conditions | §6 Type 3 |
| Log inequalities (base < 1 flips the sign) | §7 Type 4 |
| Logs of terms in AP/GP | §8 Logs and progressions |

### Progressions — `Quant/15-Progressions-AP-GP.md`

| Topic / keyword | Section |
|---|---|
| AP: nth term, sum, common difference | §1 Arithmetic Progression |
| Sum of a range of terms (Sₙ − Sₘ) | §2 Type 1 |
| Counting/locating integer terms in a subsequence | §3 Type 2 |
| Middle term, symmetric-term tricks | §4 Useful AP facts |
| GP: nth term, finite and infinite sum | §5 Geometric Progression |
| HP and its AP reciprocal | §6 Harmonic Progression |
| AGP and telescoping series | §7 Type 3 |
| Σ n·n!, Σ n(n+1); recovering Tₙ from Sₙ | §8 Special series worth recognising |
| Recurrences: telescoping, the fixed-point method, periodicity | §9 Recursively defined sequences |
| Telescoping 1/(n(n+1)(n+2)) — the ½ factor | §7a Telescoping with three consecutive factors |

### Functions & Graphs — `Quant/16-Functions-and-Graphs.md`

| Topic / keyword | Section |
|---|---|
| Which of the four question shapes this is | §1 What CAT actually asks |
| Domain and range; the four illegal structures | §2 Domain and range |
| Range by solving for x in terms of y | §2 Domain and range |
| One-one, onto, even, odd, periodic | §3 Classifying a function |
| Composition, inverse, self-inverse, iterated functions | §4 Composition and inverse |
| f(x) + f(1/x); f(x+y) = f(x)+f(y) and its family | §5 Type 1 — Functional equations |
| Greatest integer [x] and fractional part {x} | §6 Greatest integer and fractional part |
| The standard graph shapes | §7 The standard graphs |
| Shifts, stretches, reflections; \|f(x)\| vs f(\|x\|) | §8 Transformations |
| How many solutions — sketch both sides | §9 Type 2 — Counting solutions graphically |
| Regions of a two-variable inequality; \|x\|+\|y\| ≤ a | §10 Type 3 — Regions |
| Which maxima–minima tool to use | §11 Maxima and minima |
| Range of a rational function via the discriminant | §11 Maxima and minima |

### Triangles — `Quant/17-Triangles.md`

| Topic / keyword | Section |
|---|---|
| How to approach any plane-geometry question | §1 How to approach |
| Parallel lines, transversals, angle chasing | §2 Lines and angles |
| Area formulas, Heron, Pythagorean triples, 13-14-15 | §3 Triangles — the essential set |
| Acute / right / obtuse from the largest side | §3 Triangles — the essential set |
| Similarity, AA, areas in ratio k² | §4 Similarity, congruence and area ratios |
| Line parallel to a side (BPT / Thales) | §4 Similarity, congruence and area ratios |
| Same height ⟹ area ratio = base ratio | §4 Similarity, congruence and area ratios |
| Centroid, incentre, circumcentre, orthocentre; where each sits | §5 The four centres |
| r and R for a right triangle | §5 The four centres |
| Angle bisector theorem, midpoint theorem, medial triangle | §6 Medians, bisectors and the midpoint theorem |
| Median length (Apollonius) | §6 Medians, bisectors and the midpoint theorem |
| Obtuse triangle: altitude foot outside the base, X–M–N ordering | §7 Type 1 — Altitudes |
| Altitude on the hypotenuse, CD² = AD·DB, geometric means | §7 Type 1 — Altitudes |
| Point on a circle, perpendicular to the diameter | §7 Type 1 — Altitudes |
| Cevians and area splitting | §8 Type 2 — Splitting area with cevians |
| Sine rule (and = 2R), cosine rule | §9 Sine rule and cosine rule |
| Trig identities, quadrant signs, max/min of a·sin x + b·cos x | §9a Trigonometric identities and maxima |
| Angles of elevation and depression | §10 Type 3 — Heights and distances |
| Folding and crease problems | §11 Type 4 — Folding and creases |

### Circles — `Quant/18-Circles.md`

| Topic / keyword | Section |
|---|---|
| Circumference, area, arc, sector | §1 The essential set |
| Segment area = sector − triangle | §1 The essential set |
| Angle at the centre, angle in a semicircle, same segment | §2 Chords and angles |
| Chord length from the distance to the centre | §2 Chords and angles |
| Tangent length, equal tangents, power of a point | §3 Tangents |
| Tangent–chord (alternate segment) theorem | §3 Tangents |
| Cyclic quadrilaterals, Brahmagupta, Ptolemy | §4 Cyclic quadrilaterals |
| Shaded regions, overlapping areas, leaf/petal | §5 Type 1 — Segments and shaded regions |
| Two circles: touching, intersecting, common tangents, common chord | §6 Type 2 — Two circles |
| Circles inscribed in and circumscribing figures; packed circles | §7 Type 3 — Inscribed and circumscribing |

### Quadrilaterals & Polygons — `Quant/19-Quadrilaterals-and-Polygons.md`

| Topic / keyword | Section |
|---|---|
| Which shape has which property | §1 The quadrilateral family |
| Perpendicular diagonals ⟹ area ½d₁d₂; Varignon midpoint parallelogram | §1 The quadrilateral family |
| Parallelogram law, rhombus and square relations | §2 Parallelogram, rhombus, rectangle, square |
| Trapezium area, midsegment, isosceles trapezium | §3 Trapezium |
| Tangential quadrilaterals (Pitot), incircle radius, kites | §4 Type 1 — Tangential quadrilaterals |
| Interior/exterior angles, number of diagonals | §5 Polygons — angles and diagonals |
| Regular polygon inradius, circumradius, area | §6 Regular polygons — the metric formulas |
| Optimisation: fixed area or perimeter; the wall variant | §7 Type 2 — Optimisation |

### Mensuration — `Quant/20-Mensuration.md`

| Topic / keyword | Section |
|---|---|
| Volume and surface area of every standard solid | §1 The solid formula table |
| Cone : sphere : cylinder = 1 : 2 : 3 | §1 The solid formula table |
| Linear ×k ⟹ area ×k², volume ×k³ | §2 The scaling rule |
| Melting and recasting, wire drawing, volume conservation | §3 Type 1 — Recasting |
| Combined solids and the faces that disappear | §4 Type 2 — Combined solids |
| Hollow cylinders, pipes, shells, open tanks | §5 Type 3 — Hollow solids |
| Frustum; cone cut parallel to the base (1 : 7 halfway) | §6 Frustum and cones cut parallel |
| Painted cube cut into n³ pieces | §7 Type 4 — The painted cube |
| Cube/cuboid cut by a plane, volume ratio of the two parts | §8 Type 5 — Cutting a solid with a plane |
| Ant on a box, shortest path across a surface | §9 Type 6 — Unfolding |
| Sphere in a cube, cube in a sphere, sphere in a cylinder | §10 Inscribed and circumscribed solids |
| Liquid level, immersion, partly filled cone | §11 Type 7 — Liquid level and immersion |

### Coordinate Geometry — `Quant/21-Coordinate-Geometry.md`

| Topic / keyword | Section |
|---|---|
| When coordinates beat a synthetic argument; choosing the origin | §1 When to reach for coordinates |
| Distance, midpoint, section formula, centroid | §2 Points |
| Slope, the five forms of a line, axis intercepts | §3 Straight lines |
| Parallel, perpendicular, angle, distance from a point to a line | §4 Parallel, perpendicular, angle, distance |
| Missing vertex of a parallelogram, D = A + C − B | §5 Type 1 — Quadrilaterals from their vertices |
| Identifying rhombus / rectangle / square from vertices | §5 Type 1 |
| Where a diagonal meets an axis | §5 Type 1 |
| Shoelace area, collinearity test | §6 Area from coordinates |
| Circle equations, centre and radius, tangency | §7 Circles in coordinates |
| Reflections and shortest-path-touching-a-line | §8 Type 2 — Reflections and shortest paths |

### Set Theory & Venn Diagrams — `Quant/22-Set-Theory-Venn.md`

| Topic / keyword | Section |
|---|---|
| Fixed totals, degrees of freedom | §1 The core idea |
| Two sets: union, both, exactly one, neither | §2 Two sets |
| Three sets: inclusion–exclusion, exactly one/two/three | §3 Three sets |
| Two independent attributes → 2×2 grid, one free cell | §4 The 2×2 classification table |
| Percentages in a 2×2 table, choosing the total | §5 Type 1 |
| Checking a question is self-consistent | §5 Type 1 (consistency trap) |
| "At least / at most" → maximise or minimise a cell | §6 Type 2 |
| Max and min of an overlap | §7 Type 3 |
| Set questions inside DI caselets | §8 Type 4 |

### Permutations, Combinations & Probability — `Quant/23-PnC-Probability.md`

| Topic / keyword | Section |
|---|---|
| Fundamental counting, when to use P vs C | §1 Core idea |
| Formula sheet | §2 Formula sheet |
| "Must be together" arrangements | §3 Must be together |
| "Must NOT be together" (gap method) | §4 Must not be together |
| Relative-order constraints | §4b Relative-order constraint |
| Words with repeated letters | §5 Repeated letters |
| Circular arrangements, necklaces | §6 Circular arrangements |
| Number formation | §7 Number formation |
| Selections and committees | §8 Selections and committees |
| Distribution: identical vs distinct objects | §9 Distribution |
| Non-decreasing / non-increasing digit sequences, choosing with repetition | §9a Monotone sequences |
| Derangements | §10 Derangements |
| Grid paths, handshakes, diagonals | §11 Grid paths, handshakes |
| Dictionary rank of a word | §12 Dictionary rank |
| Probability as counting divided | §13 Probability |
| "At least one" via complement | §14 At least one |
| Conditional probability | §15 Conditional probability |
| Repeated trials, expected value | §16 Repeated trials |

### Reference and practice

| Resource | File |
|---|---|
| Tables 11–25, squares, cubes, roots, powers | `Quant/Reference/Calculation-Toolkit.md` §1–5 |
| Fraction ↔ percentage table | `Quant/Reference/Calculation-Toolkit.md` §6 |
| Primes, divisibility, cyclicity, factorials | `Quant/Reference/Calculation-Toolkit.md` §7–9 |
| Reciprocal decimals (1/7, 1/13 families) worth recognising | `Quant/Reference/Calculation-Toolkit.md` §10 |
| Constants and unit conversions | `Quant/Reference/Calculation-Toolkit.md` §11 |
| Fast-arithmetic techniques, % shortcuts, growth multipliers, series sums | `Quant/Reference/Calculation-Toolkit.md` §12–15 |
| Interactive calculation drill | `Quant/Reference/Flashcard-Drill.html` |
| Practice set for any topic (all 20) | `Quant/Practice/<NN>-<Topic>-Practice.md` |
| Interactive mock test (692 questions, all 20 topics) | `Quant/Practice/CAT-Quant-Test.html` |
| Is a syllabus module ready to revise from? | `Syllabus-Coverage.md` |

---

## Cross-topic connections

| Link | Why |
|---|---|
| Clocks ↔ Circular tracks | a clock is two runners at a 12 : 1 speed ratio (Clocks §1, TSD §9) |
| Races ↔ TSD | races are relative speed with a distance or time offset |
| Alligation ↔ Weighted averages | the same equation, solved in opposite directions |
| Mixtures ↔ Profit & Loss | adulteration appears in both, with different bases |
| Average speed ↔ Harmonic mean | equal-distance average speed *is* the HM |
| Calendars ↔ Remainders | odd days are just mod 7 (Number System §6) |
| Percentages ↔ CI | successive % change and compound interest are the same multiplier |
| Progressions ↔ Logarithms | logs of a GP form an AP |
| Set theory ↔ Percentages | survey percentages become whole numbers once the total is the LCM (Set Theory §5) |
| Set theory ↔ PnC | inclusion–exclusion is one identity used for both counting and P(A∪B) |
| Algebra ↔ Progressions | polynomial differences telescope, so P(b) − P(a) is a series sum (Algebra §3a, Progressions §7) |
| Coordinate ↔ Triangles | folding is reflection; the same figure is often faster on axes (Coordinate §8, Triangles §11) |
| Triangles ↔ Circles | a diameter creates a right angle, so circle questions become triangle questions (Circles §2, Triangles §7) |
| Mensuration ↔ Percentages | a % change in a dimension cubes for volume (Mensuration §2, Percentages §5) |
| Coordinate ↔ Weighted averages | the section formula *is* a weighted average (Coordinate §2) |
| Interest ↔ Number System | integer-rate questions become divisibility conditions (SCI §9a, Number System §11) |
| Number System ↔ Progressions | repunits and digit patterns are geometric sums (Number System §13a, Progressions §5) |
| Ratio ↔ Number System | "whole rupees" turns a ratio into a divisibility condition (Ratio §12a, Number System §11) |

---

## Practice — where to drill each topic

Every topic file has a matching set in `Quant/Practice/`. Hints in those sets cite the section number of the notes that holds the intended method, so a wrong answer points you straight back to the right paragraph. Each set ends with an **error-audit table** mapping question numbers to the specific mistake each one is built to catch — read that before re-reading theory.

| To drill | Open |
|---|---|
| any single topic | `Quant/Practice/<NN>-<Topic>-Practice.md` |
| under time, with scoring | `Quant/Practice/CAT-Quant-Test.html` — 692 questions across all 20 topics |
| only the exam-feel sets | the same file → **Mixed sets only** |
| mental calculation speed | `Quant/Reference/Flashcard-Drill.html` |
| vocabulary | `VARC/Practice/Vocab-Trainer.html` — definition, synonym and antonym MCQs |

All of it is **generated from JSON** in `_build/`, never written by hand — the `.md` and the interactive test come from the same source, so they cannot disagree. See the README section "How the generated files work" before editing anything under `Practice/`.

---

## VARC

| File | Covers |
|---|---|
| `VARC/Vocabulary.md` | 127 words in 28 meaning-groups, with synonyms, antonyms and usage |
| `VARC/Practice/Vocab-Trainer.html` | interactive definition / synonym / antonym MCQs; tracks the words you keep missing |

Words are grouped **by meaning**, not alphabetically, because CAT tests discrimination between near-synonyms far more often than raw recall. The trainer exploits this: a synonym question always plants one antonym of the same word among the options, and an antonym question plants one synonym.

### Meaning-group lookup — `VARC/Vocabulary.md`

Find the sense you want here, then open that `##` section in `VARC/Vocabulary.md`. The full word list per group lives in that file's own **Groups** table at the top — not duplicated here.

| Sense | Section | Sense | Section |
|---|---|---|---|
| praising, revering | Praise and reverence | criticising, attacking | Criticism and attack |
| lying, misleading | Deception and insincerity | talking too much | Excessive speech |
| terse, tight-lipped | Brevity and reserve | refusing to budge | Stubbornness |
| yielding, fawning | Submission and flattery | angry, aggressive | Anger and hostility |
| soothing, unruffled | Calming and composure | too much of something | Excess and abundance |
| too little, sparing | Scarcity and thrift | open-handed | Generosity |
| fading, short-lived | Decline and impermanence | lasting, unchanging | Permanence |
| hard vs easy to understand | Obscurity and clarity | careful, sound judgement | Caution and judgement |
| daring, reckless | Boldness and rashness | fearful, hesitant | Timidity |
| overbearing pride | Arrogance | modest, self-lowering | Humility |
| hardworking, exacting | Diligence | idle, drifting | Laziness and aimlessness |
| wise, well-read | Insight and learning | slow-witted, easily fooled | Dullness and gullibility |
| agreement, peace-making | Harmony and reconciliation | disagreement, splitting | Conflict and division |
| starting, emerging | Beginning and growth | confirming or disputing a claim | Appeasement of doubt and proof |

---

## Gaps — not yet covered

**For Quant, `Syllabus-Coverage.md` is the authoritative list** — it maps every coaching module to its file and section, marks it full / partial / thin, names the specific missing piece, and carries the priority queue. It also owns practice-set coverage. Only the non-Quant gaps are listed here.

- **Data Interpretation** — no file yet. Percentages §11 covers growth rates in a DI context, but nothing on caselets, tables or graph reading.
- **Logical Reasoning** — no file yet.
- **VARC beyond vocabulary** — no file yet on reading comprehension, para-jumbles, para-summary or odd-one-out.

---

## File map

```
CAT Prep/
├── Index.md                              ← you are here
├── README.md
├── Syllabus-Coverage.md                  ← module-by-module readiness
├── Quant/
│   ├── 01-Number-System.md
│   ├── 02-Percentages.md
│   ├── 03-Ratio-Proportion-Variation.md
│   ├── 04-Means-and-Weighted-Averages.md
│   ├── 05-Mixtures-and-Alligation.md
│   ├── 06-Profit-Loss-Discount.md
│   ├── 07-Simple-Compound-Interest.md
│   ├── 08-Time-Speed-Distance.md
│   ├── 09-Races.md
│   ├── 10-Clocks.md
│   ├── 11-Time-Work-Pipes-Cisterns.md
│   ├── 12-Calendars.md
│   ├── 13-Algebra.md
│   ├── 14-Logarithms.md
│   ├── 15-Progressions-AP-GP.md
│   ├── 16-Functions-and-Graphs.md
│   ├── 17-Triangles.md
│   ├── 18-Circles.md
│   ├── 19-Quadrilaterals-and-Polygons.md
│   ├── 20-Mensuration.md
│   ├── 21-Coordinate-Geometry.md
│   ├── 22-Set-Theory-Venn.md
│   ├── 23-PnC-Probability.md
│   ├── Practice/
│   │   ├── <NN>-<Topic>-Practice.md   ← one per topic, all 20
│   │   ├── CAT-Quant-Test.html        ← interactive, 692 questions
│   │   └── _build/
│   │       ├── gen_practice.py        ← generator
│   │       └── topics/*.json          ← question data (source of truth)
│   └── Reference/
│       ├── Calculation-Toolkit.md
│       └── Flashcard-Drill.html
└── VARC/
    ├── Vocabulary.md
    └── Practice/
        ├── Vocab-Trainer.html
        └── _build/
            ├── gen_vocab.py           ← generator
            ├── trainer_template.html
            └── words.json             ← word data (source of truth)
```
