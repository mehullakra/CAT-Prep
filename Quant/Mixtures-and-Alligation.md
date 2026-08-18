# Mixtures & Alligation

> CAT quant. Alligation is a weighted average run backwards: given two ingredient values and the blend value, find the mixing ratio.

---

## 1. Core idea

**Ratio of quantities = inverse of the distances from the mean.**

That inversion is the whole topic. The cheaper ingredient gets the larger share when the mean sits closer to it — and "closer to cheap" means a *small* distance on the cheap side, so that small distance must belong to the *other* quantity. Getting this crossover right is the only real skill here.

**Why the inversion happens:** the mean is a see-saw balance point. Whichever ingredient you have more of pulls the mean toward itself, so it ends up with the shorter lever arm. Quantity and distance are inversely related, exactly as speed and time are in TSD.

---

## 2. The alligation cross

```
   Cheaper (c)          Dearer (d)
          \               /
           \             /
            Mean (m)
           /             \
          /               \
      (d − m)          (m − c)
```

**Quantity of cheaper : Quantity of dearer = (d − m) : (m − c)**

Read it diagonally — the difference computed on the *dearer* side belongs to the *cheaper* quantity.

**Worked example:** In what ratio must rice at ₹30/kg be mixed with rice at ₹40/kg to get a mixture worth ₹34/kg?

- c = 30, d = 40, m = 34
- d − m = 6, m − c = 4
- Cheap : Dear = 6 : 4 = **3 : 2**

**Sanity check** (run this every time — it catches an inverted answer in two seconds): 34 is closer to 30, so there must be more cheap rice. 3 > 2 ✓

---

## 3. What alligation works on

It applies to any quantity that behaves as a **weighted average per unit**:

- Price per kg or per litre
- Concentration or percentage (milk %, alcohol %, purity)
- Average speed — **only when times are equal**, not distances
- Average marks, average age
- Profit % — weighted by cost price
- Interest rates — weighted by principal

**Does not apply** to average speed over equal *distances*. That's the harmonic mean, 2ab/(a+b), not a weighted average. Applying the cross there is a classic misfire — see `Time-Speed-Distance.md` §3.

**The recognition skill matters more than the formula.** CAT almost never says "alligation". It says "in what ratio", or gives you two groups and a combined average and asks for a group size. Any question with two sub-groups and one overall average is an alligation question.

---

## 4. Type 1 — Concentration problems

Treat the concentration exactly as you would a price.

**Worked example:** Solution A is 20% alcohol, solution B is 50% alcohol. In what ratio to get a 30% solution?

- c = 20, d = 50, m = 30
- d − m = 20, m − c = 10
- A : B = 20 : 10 = **2 : 1**

**Water as an ingredient:** water is 0% of whatever you're measuring. Set c = 0.

**Worked example:** In what ratio must water be mixed with milk costing ₹36/litre so the seller gains 20% selling the mixture at ₹36/litre?

- SP = 36 at 20% gain ⟹ effective CP of the mixture = 36/1.2 = 30
- c = 0 (water), d = 36 (milk), m = 30
- Water : Milk = (36 − 30) : (30 − 0) = 6 : 30 = **1 : 5**

This is the adulteration case from profit & loss, solved with the general tool. See `Profit-Loss-Discount.md` §8 for the direct method.

**Worked example (finding a quantity, not a ratio):** How much water must be added to 40 litres of a 15% alcohol solution to bring it down to 10%?

- c = 0 (water), d = 15, m = 10
- Water : Solution = (15 − 10) : (10 − 0) = 5 : 10 = 1 : 2
- The solution is 40 litres = 2 parts ⟹ 1 part = 20 ⟹ add **20 litres of water**

Ratios are the output of the cross; converting a ratio to a quantity always needs one given absolute amount to anchor it.

---

## 5. Type 2 — Repeated replacement (memorise this)

A vessel holds L litres of pure liquid. Remove x litres, replace with water. Repeat n times.

**Final pure liquid = L × (1 − x/L)ⁿ**

As a ratio: pure remaining / original = ((L − x)/L)ⁿ

**Worked example:** A 40-litre vessel of pure milk. 8 litres removed and replaced with water, three times over. Final milk quantity?

- L = 40, x = 8, n = 3
- (1 − 8/40) = 4/5
- Milk = 40 × (4/5)³ = 40 × 64/125 = **20.48 litres**
- Water = 40 − 20.48 = 19.52 litres

**Worked example (solving for n):** From 81 litres of pure milk, 27 litres are drawn off and replaced with water each time. After how many operations is the milk down to 24 litres?

- Factor per operation = (81 − 27)/81 = 2/3
- 81 × (2/3)ⁿ = 24 ⟹ (2/3)ⁿ = 24/81 = 8/27 = (2/3)³ ⟹ n = **3**

CAT chooses numbers so the ratio is a clean power. If your factor doesn't produce a recognisable cube or square, re-read the question — you've probably misidentified L or x.

**Critical conditions for the formula:**

- You must remove from the **mixture** each time (after the first round), not pure liquid
- The vessel volume must stay constant

If the question removes pure milk each round, or the volume changes, the formula fails — do it round by round instead.

**Variant — mixture already impure at the start:** apply the factor to the milk you actually have, not to the vessel's capacity.

---

## 6. Type 3 — Three or more ingredients

Alligation is a two-ingredient tool. For three, pair them up:

1. Take two ingredients, apply the cross to get a sub-ratio
2. Treat that blend as one new ingredient with the blended value
3. Alligate that against the third

Alternatively, if the question already gives the final ratio and asks for a value, set up the weighted-average equation directly — usually faster than forcing the cross.

**Rule:** for three ingredients where two sit on the same side of the mean, the answer is **not unique** unless the question constrains it further. Watch for "minimum quantity of X" or "maximum possible" phrasing — that signals a boundary case rather than a single answer.

---

## 7. Type 4 — Mixing two mixtures

Do not work with the mixtures as objects. **Convert each to a single concentration number first**, then alligate on that number. Always convert ratios to fractions of the whole — never put raw ratio numbers into the cross.

**Worked example:** Vessel A has milk : water = 4 : 1. Vessel B has milk : water = 2 : 3. In what ratio to mix so the result is milk : water = 3 : 2?

- Convert to milk fractions: A = 4/5 = 80%, B = 2/5 = 40%, target = 3/5 = 60%
- c = 40 (that's B), d = 80 (that's A), m = 60
- B : A = (80 − 60) : (60 − 40) = 20 : 20 = **1 : 1**

Note the labelling: B is the *cheaper* (lower concentration) one, so B receives the (d − m) branch. Mislabelling which vessel is "cheap" is the most frequent error in this type.

**Worked example:** A 60-litre mixture has milk and water in the ratio 2 : 1. How much water must be added to make it 1 : 2?

- Milk = 40 litres, water = 20 litres. Milk stays fixed at 40.
- For a final ratio 1 : 2, milk is 1/3 of the total ⟹ total = 120
- Water to add = 120 − 60 = **60 litres**

When one component is unchanged, anchor on that component rather than using the cross. Faster and less error-prone.

---

## 7a. Type 4b — Component accounting: reading the answer off what is *left behind*

Not every two-mixture question is an alligation. When the question tells you something about the **residue** — what stays in the dispenser, the vessel, the tank — that fact is usually the fastest way in, because the residue keeps the parent mixture's ratio exactly.

**Core idea.** Pouring out part of a uniform mixture changes the *quantity* of every component but not the *ratio*. So if B is 2 : 3 apple : orange, then whatever volume remains in B is still 2/5 apple. One sentence about the residue therefore fixes the poured volume in one step.

**Method:**
1. Convert each source to litres of each component (never leave it as a ratio).
2. Find the statement about a **residue** and use it first — it involves one unknown, so it solves immediately.
3. Substitute into the statement about the **mixture** to get the second unknown.
4. Build the final answer from component totals, not from percentages of percentages.

**Worked example:** Dispenser A holds 40 L of apple : orange = 3 : 1; dispenser B holds 60 L of 2 : 3. X litres are drawn from A and Y from B into a jug. The jug then holds exactly 14 L of orange, and what remains in B holds exactly 18 L of apple. What percentage of the jug is apple?

- Convert: **A** = 30 apple + 10 orange. **B** = 24 apple + 36 orange.
- **Residue first.** What is left in B is (60 − Y) litres, still 2/5 apple: (2/5)(60 − Y) = 18 ⟹ 60 − Y = 45 ⟹ **Y = 15**
- **Then the jug.** Orange in the jug = X/4 + (3/5)Y = 14 ⟹ X/4 + 9 = 14 ⟹ **X = 20**
- Jug apple = (3/4)(20) + (2/5)(15) = 15 + 6 = **21**; jug total = 20 + 15 = **35**
- Percentage = 21/35 = **60%**

**Traps:**
- Starting with the 14-litre orange equation. It has two unknowns; the residue statement has one. Always open with the sentence that mentions only one quantity.
- Alligating. There is no target concentration given here, so the cross has nothing to work with — this is bookkeeping, not alligation.
- Averaging the two source percentages (75% and 40%) to get 57.5%. The pour volumes are unequal, so it must be weighted — and once you have the component totals you never need the weighting at all.
- Forgetting that the residue keeps the parent ratio. Drawing off a uniform mixture cannot change its concentration; only adding a pure component can (§4).

---

## 8. Type 5 — Alligation on profit, interest and averages

Same machinery, different label. Recognising that a question *is* an alligation question is worth more than the formula.

**Worked example:** A trader has ₹10,000. He lends part at 8% and the rest at 12%, earning 9% overall. How much at each rate?

- c = 8, d = 12, m = 9
- Ratio = (12 − 9) : (9 − 8) = 3 : 1
- **₹7,500 at 8% and ₹2,500 at 12%**

**Worked example (averages):** The average age of a class of 45 is 15 years. The boys average 16 and the girls average 13. How many boys?

- c = 13 (girls), d = 16 (boys), m = 15
- Girls : Boys = (16 − 15) : (15 − 13) = 1 : 2
- Total 45 = 3 parts ⟹ girls = 15, boys = **30**
- Check: (15 × 13 + 30 × 16)/45 = 675/45 = 15 ✓

**Integer check:** when the question counts people or objects, the parts must divide the total evenly. A fractional count means you inverted the cross or swapped which group has which average — treat it as a red flag, not an answer.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Direction of the cross | ratio read straight off the distances | the ratio is **inverted** relative to the distances |
| Mixing two mixtures | alligate on raw ratios (4:1, 2:3) | convert to fractions (80%, 40%) first |
| Which one is "cheaper" | the first one named | the one with the **lower** value |
| Replacement formula | used when pure liquid is removed each time | only valid when the **mixture** is removed |
| Replacement with changing volume | formula applied anyway | do it round by round |
| Average speed | alligated over equal distances | alligation needs equal **times** |
| Water in the mix | given some cost | water = 0 |
| "20% water in mixture" vs "water is 20% of milk" | treated as the same | 1 : 4 vs 1 : 5 — different ratios |
| Ratio vs quantity | ratio reported as the answer | anchor with a given absolute amount |
| Three ingredients | one unique answer assumed | often a range; look for "minimum/maximum" |
| Non-integer people or items | reported as the answer | red flag — recheck the cross |
| A fact about what is left in the vessel | ignored, or alligated | residue keeps the parent ratio — use it first |

---

**The one habit that fixes most errors:** after getting a ratio, ask which ingredient there should be more of. The mean is always closer to whichever ingredient dominates. If the ratio says otherwise, the cross was inverted. Three seconds, and it catches the single most common mistake in the topic.

*Related files: `Profit-Loss-Discount.md` §8 (adulteration is alligation with a zero-cost ingredient), `Time-Speed-Distance.md` §3 (where alligation must **not** be used).*
