# CAT Prep — Index

Master lookup for every concept covered so far. Purpose: when a problem can't be solved, find the concept here instead of re-deriving it or re-explaining it from scratch.

## How to use this (for Mehul, and for Claude in future sessions)

1. Stuck on a problem → identify the sub-topic it belongs to (e.g. "two runners on a track" → circular tracks; "pipe filling and draining" → pipes and cisterns).
2. Look it up in the table below → open that file → jump to that section. The section should already have the formula, the method, a worked example, and the common traps.
3. If the concept genuinely **is not** in the table/file — it's a new sub-topic, not just a new problem using an existing one — add it:
   - Add a new `##` section to the relevant file (or create a new file under `Quant/` if it's a new topic area, e.g. Percentages, TSD, Time & Work are separate files).
   - Use the same format as existing sections: core idea → method/formula → worked example → traps.
   - Add a row to the lookup table below pointing to it.
4. Don't duplicate a formula across files. If a sub-topic connects to another (like Clocks ↔ Circular Tracks), note the connection and cross-reference instead of copy-pasting.

---

## Lookup table

| Topic / keyword | File | Section |
|---|---|---|
| Speed-time inverse ratio trick | Quant/Time-Speed-Distance.md | §1 Core ratio trick |
| km/h ↔ m/s conversion | Quant/Time-Speed-Distance.md | §2 Unit conversions |
| Average speed (equal distance / equal time) | Quant/Time-Speed-Distance.md | §3 Average speed |
| Relative speed, catch-up/overtake | Quant/Time-Speed-Distance.md | §4 Relative speed |
| Trains crossing pole/platform/each other | Quant/Time-Speed-Distance.md | §5 Trains |
| Boats and streams, upstream/downstream | Quant/Time-Speed-Distance.md | §6 Boats and streams |
| Two people bouncing between two points, nth meeting | Quant/Time-Speed-Distance.md | §7 Two-body meeting |
| √(t₁t₂) trick, meeting then continuing to other end | Quant/Time-Speed-Distance.md | §8 The √ trick |
| Races, "beats by x m / x sec" | Quant/Time-Speed-Distance.md | §9 Races |
| Circular track meeting points, same/opposite direction | Quant/Time-Speed-Distance.md | §10 Circular tracks |
| Meeting at the starting point (circular track) | Quant/Time-Speed-Distance.md | §10 Circular tracks |
| Clock angle between hands | Quant/Time-Speed-Distance.md | §11 Clocks |
| Clock hands coincide / 90° / 180° | Quant/Time-Speed-Distance.md | §11 Clocks |
| Faulty / gaining / losing clocks | Quant/Time-Speed-Distance.md | §11 Clocks |
| Mirror image of a clock | Quant/Time-Speed-Distance.md | §11 Clocks |
| LCM method for work problems | Quant/Time-Work-Pipes-Cisterns.md | §1 The LCM method |
| Efficiency vs. time ratio | Quant/Time-Work-Pipes-Cisterns.md | §2 Efficiency is inverse to time |
| Men-Days-Hours (M-D-H) formula | Quant/Time-Work-Pipes-Cisterns.md | §3 The M-D-H formula |
| Alternate-day work schedules | Quant/Time-Work-Pipes-Cisterns.md | §4 Alternate days |
| Splitting wages by work done | Quant/Time-Work-Pipes-Cisterns.md | §5 Wages |
| Pipes filling/emptying, leaks, staggered opening | Quant/Time-Work-Pipes-Cisterns.md | §6 Pipes and cisterns |
| Alligation cross, cheap/dear mixing ratio | Quant/Mixtures-and-Alligation.md | §2 The alligation cross |
| Concentration mixing (alcohol %, milk %, purity) | Quant/Mixtures-and-Alligation.md | §4 Concentration problems |
| Water added to milk / adulteration ratio | Quant/Mixtures-and-Alligation.md | §4 Concentration problems |
| Repeated replacement (remove x litres, replace with water, n times) | Quant/Mixtures-and-Alligation.md | §5 Repeated replacement |
| Alligation with 3+ ingredients | Quant/Mixtures-and-Alligation.md | §6 Three or more ingredients |
| Mixing two existing mixtures together | Quant/Mixtures-and-Alligation.md | §7 Mixing two mixtures |
| Alligation on profit % or interest rates | Quant/Mixtures-and-Alligation.md | §8 Alligation on profit and interest |
| CP/MP/SP chain, multiplying factors | Quant/Profit-Loss-Discount.md | §1–3 Core idea, base relationships, factors |
| Marked price + discount → profit % | Quant/Profit-Loss-Discount.md | §4 Marked price with discount |
| Successive discounts | Quant/Profit-Loss-Discount.md | §5 Successive discounts |
| Same SP, one item at x% profit + one at x% loss | Quant/Profit-Loss-Discount.md | §6 Two classic traps |
| False weight / dishonest dealer gain % | Quant/Profit-Loss-Discount.md | §7 Cheating with false weights |
| Adulteration profit % (P&L version) | Quant/Profit-Loss-Discount.md | §8 Adulteration |
| CP of n articles = SP of m articles | Quant/Profit-Loss-Discount.md | §9 Equating goods |
| "Buy X get Y free" as a discount | Quant/Profit-Loss-Discount.md | §10 Discount on bulk |

---

## Not yet covered (flagged during discussion, still to add)

- **Calendars** — modular arithmetic on 7. Related to Clocks only by exam grouping, not by method. No file yet — create `Quant/Calendars.md` when this comes up.

---

## File map

```
CAT Prep/
├── Index.md                              ← you are here
└── Quant/
    ├── Time-Speed-Distance.md            (TSD, circular tracks, clocks)
    ├── Time-Work-Pipes-Cisterns.md       (work, pipes & cisterns)
    ├── Mixtures-and-Alligation.md        (alligation, concentration, replacement, profit/interest alligation)
    └── Profit-Loss-Discount.md           (CP/MP/SP, discounts, false weight, adulteration, equating goods)
```
