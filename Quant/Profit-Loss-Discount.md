# Profit, Loss & Discount

> CAT quant. Everything is a percentage of a base — get the base right and 80% of errors disappear.

---

## 1. Core idea

- **Profit % and Loss % are always on CP**
- **Discount % is always on MP**
- Margin % (rare in CAT, common in DI) is on SP

**Second core idea: stop using formulas, use multiplying factors.** A 20% profit is not "add 20%" — it's × 1.2. A 25% discount is × 0.75. Chain them and the whole problem becomes one line of multiplication. This single habit is the biggest speed gain in the topic.

**Why factors beat formulas:** they compose. Markup, discount, false weight, and adulteration are all just factors multiplied together in any order, so a four-step question becomes one product instead of four separate percentage calculations, each with its own chance of a base error.

---

## 2. Base relationships

| Quantity | Meaning |
|---|---|
| CP | Cost Price — what you paid |
| MP | Marked Price / List Price — the tag |
| SP | Selling Price — what the customer actually paid |
| Discount | MP − SP |
| Profit | SP − CP |

**The master chain:** CP × (1 + profit%) = SP = MP × (1 − discount%)

Almost every question in this topic is that equation with one unknown. Write the chain before touching numbers; it prevents base confusion structurally rather than by vigilance.

---

## 3. Multiplying factors — memorise these

| Percentage | As profit/increase | As discount/decrease |
|---|---|---|
| 10% | 1.1 | 0.9 |
| 12.5% (1/8) | 1.125 | 0.875 |
| 16.67% (1/6) | 7/6 | 5/6 |
| 20% (1/5) | 1.2 | 0.8 |
| 25% (1/4) | 1.25 | 0.75 |
| 33.33% (1/3) | 4/3 | 2/3 |
| 50% (1/2) | 1.5 | 0.5 |

The **fraction forms matter more than the decimals** — CAT picks numbers so the fractions cancel. A 16.67% markup followed by a 14.28% (1/7) discount is 7/6 × 6/7 = 1, i.e. no profit. In decimals that's invisible; in fractions it's instant.

**The reciprocal pairs worth knowing:** an x% increase is exactly cancelled by a decrease of x/(100+x) %. So +25% is undone by −20%, +50% by −33.33%, +100% by −50%.

---

## 4. Type 1 — Marked price with discount

**Worked example:** A shopkeeper marks goods 40% above cost and offers a 25% discount. Find the profit %.

- Assume CP = 100 (always assume 100 for the base you're taking percentages of)
- MP = 100 × 1.4 = 140
- SP = 140 × 0.75 = 105
- Profit = 5 → **5%**

The whole thing collapses to 1.4 × 0.75 = 1.05. That's the entire solution — one multiplication.

**Reverse version:** "What should he mark above cost to still make 20% profit after a 20% discount?"

- MP × 0.8 = 100 × 1.2 ⟹ MP = 150 ⟹ mark up **50%**

**Note the asymmetry:** a 20% markup does not survive a 20% discount. Markup and discount are on different bases, so they never cancel at equal percentages. Expecting them to is a standard misconception.

---

## 5. Type 2 — Successive discounts

Two successive discounts of a% and b% are **not** (a + b)%. They multiply.

- Net factor = (1 − a)(1 − b)
- Shortcut: net discount = a + b − ab/100

**Worked example:** Successive discounts of 20% and 10%.

- Factor = 0.8 × 0.9 = 0.72 ⟹ net discount = **28%**

Not 30% — that is always among the options, and it is always the decoy.

**Successive discounts are order-independent.** 20% then 10% equals 10% then 20%. CAT sometimes asks which order the customer should prefer; the answer is "no difference". Don't overthink it.

**Worked example (three discounts):** 10%, 20% and 25% successively.

- Factor = 0.9 × 0.8 × 0.75 = 0.54 ⟹ net discount = **46%**

**Worked example (finding a missing discount):** After a 20% discount, a further discount brings the net to 32%. Find the second discount.

- 0.8 × (1 − x) = 0.68 ⟹ 1 − x = 0.85 ⟹ x = **15%**

---

## 6. Type 3 — Two classic traps

**Trap A — two items sold at the same SP, one at x% profit, one at x% loss.**

There is always a net **loss**, equal to **x²/100 %**.

**Worked example:** Two articles sold at ₹990 each, one at 10% gain and one at 10% loss.

- Loss % = 10²/100 = **1%**
- Check: CP₁ = 990/1.1 = 900, CP₂ = 990/0.9 = 1100. Total CP = 2000, total SP = 1980. Loss of 20 on 2000 = 1% ✓

Never answer "no profit no loss" — that is the decoy, and it appears every time. The reason there's a loss: the item sold at a loss had the *higher* cost price, so the loss is computed on a bigger base than the gain.

**Trap B — a percentage increase followed by a decrease of the same x%.**

Net = x²/100 % **decrease**. Same structure, same reasoning. A 20% rise then a 20% fall leaves you at 0.96, down 4%.

---

## 7. Type 4 — Cheating with false weights

The seller sells less than the claimed quantity; the gain comes from the shortfall.

**Gain % = (True weight − Weight given) / (Weight given) × 100**

**Worked example:** A dealer claims to sell at cost price but uses a 900 g weight for 1 kg. Find the gain %.

- He charges for 1000 g and delivers 900 g
- Let CP = ₹1/gram. His cost = ₹900, his revenue = ₹1000
- Gain = 100 on 900 = **11.11%** (1/9)

**Key insight:** the base is what he actually gave up (900), not what he charged for (1000). Dividing by 1000 gives the standard wrong answer of 10%.

**Combined case — false weight AND markup: multiply the factors.**

- Uses an 800 g weight for 1 kg and sells at 15% above cost
- Weight factor = 1000/800 = 1.25; markup factor = 1.15
- Net = 1.25 × 1.15 = 1.4375 ⟹ **43.75% profit**

**Dishonest on both sides:** buys using an 1100 g weight for 1 kg and sells using a 900 g weight.

- Factors compound: (1100/1000) × (1000/900) = 11/9 ⟹ **22.22% gain**

**Worked example (false weight with a discount):** Uses a 900 g weight for 1 kg and also gives a 10% discount on cost price.

- Weight factor = 1000/900 = 10/9; discount factor = 0.9
- Net = 10/9 × 0.9 = 1.0 ⟹ **no profit, no loss**

That last one is a favourite because the two effects cancel exactly, and the factor method reveals it in one line.

---

## 8. Type 5 — Adulteration

The adulterant is free — usually water, sand, or a zero-cost substitute. The profit is pure gain on the added quantity.

**Gain % = (Quantity of adulterant / Quantity of pure substance) × 100**

**Worked example:** A milkman mixes 1 litre of water with 4 litres of milk and sells the mixture at the cost price of pure milk. Find the gain %.

- He paid for 4 litres and sells 5
- Let milk CP = ₹10/litre. Cost = ₹40, revenue = 5 × 10 = ₹50
- Gain = 10 on 40 = **25%**

The base is the pure quantity — what he paid for — not the mixture.

**If the adulterant has a cost**, this becomes an alligation problem. Use the cross in `Mixtures-and-Alligation.md` §2 to find the mixing ratio, then compute profit on the blended CP.

**Read carefully — percentage of adulterant vs ratio:**

- "20% water **in the mixture**" ⟹ water : milk = 1 : 4 ⟹ gain **25%**
- "Water is 20% **of the milk**" ⟹ water : milk = 1 : 5 ⟹ gain **20%**

CAT exploits this distinction routinely. Underline the word "of" and identify what follows it.

---

## 9. Type 6 — Equating goods

"CP of 20 articles = SP of 16 articles. Find the profit %."

- Shortcut: Profit % = (Goods on the left − Goods on the right) / (Goods on the right) × 100 = (20 − 16)/16 = **25%**
- By assumption: let CP of each = ₹1. CP of 20 = ₹20 = SP of 16 ⟹ SP each = 1.25 ⟹ 25% profit

**Rule of thumb:** if the larger number sits on the CP side, it's a profit. If it sits on the SP side, it's a loss.

**Worked example (loss side):** SP of 15 articles = CP of 12 articles.

- Rewrite as CP of 12 = SP of 15 ⟹ (12 − 15)/15 = −20% ⟹ a **20% loss**

---

## 10. Type 7 — Bulk offers and "buy X get Y free"

- "Buy 3 get 1 free" = pay for 3, receive 4 ⟹ discount = 1/4 = **25%**
- "Buy 2 get 1 free" = pay for 2, receive 3 ⟹ discount = 1/3 = **33.33%**

**The base is what you receive, not what you pay for.** "Buy 3 get 1 free" is not 33.33%.

**Worked example (offer plus discount):** "Buy 4 get 1 free" alongside a 10% discount on the marked price.

- Offer factor = pay 4, get 5 ⟹ 4/5 = 0.8; discount factor = 0.9
- Net = 0.8 × 0.9 = 0.72 ⟹ **28% total discount**

---

## 11. Type 8 — Comparing profit across items

Profit percentages **cannot be averaged**. They must be weighted by cost price.

**Worked example:** An item costing ₹200 is sold at 20% profit and another costing ₹800 at 10% profit. Overall profit %?

- Total CP = 1000; profits = 40 and 80 → total profit = 120
- Overall = 120/1000 = **12%**, not the arithmetic mean of 15%

This is an alligation setup in disguise — see `Mixtures-and-Alligation.md` §8. The mean sits closer to 10% because the ₹800 item dominates.

---

## 12. Type 9 — Markup + discount + wastage/spoilage combined

The full CAT version stacks three effects. Treat each as a **factor** and multiply. The only skill is knowing which base each factor sits on.

| Effect | Factor | Acts on |
|---|---|---|
| Markup of m% | (1 + m/100) | CP → MP |
| Discount of d% | (1 − d/100) | MP → SP |
| Wastage/spoilage of w% of stock | (1 − w/100) | quantity actually sold |

**Key insight: wastage reduces revenue, not cost.** You paid for the whole stock but sell only (1 − w) of it. So

**Overall factor = (1 + m)(1 − d)(1 − w)**, and profit % = that factor − 1.

**Worked example:** A trader marks goods 60% above cost, gives a 20% discount, and 10% of his stock spoils and is discarded. Find his profit %.

- Take 100 units at CP ₹1 each ⟹ total cost = ₹100
- MP = ₹1.60/unit; SP after discount = 1.60 × 0.8 = ₹1.28/unit
- Units sold = 90 ⟹ revenue = 90 × 1.28 = ₹115.20
- Profit = 15.20 on 100 ⟹ **15.2%**
- One line: 1.6 × 0.8 × 0.9 = 1.152 ✓

**Reverse phrasing (the common CAT form):** "What markup gives a 20% profit after a 20% discount and 10% spoilage?"

- (1 + m) × 0.8 × 0.9 = 1.2 ⟹ 1 + m = 1.2/0.72 = 5/3 ⟹ markup = **66.67%**

**The base trap:** "10% of the stock spoils" multiplies revenue by 0.9. "Spoilage equals 10% of what he sells" is a different base — then sold = S, spoiled = 0.1S, stock = 1.1S, so the factor is 1/1.1. Identify what the percentage is *of* before writing the factor.

**Combining with false weights (§7):** every effect is an independent factor, so they simply multiply. Markup 1.15 × discount 0.90 × spoilage 0.95 × false weight (1000/900 = 1.111) = 1.0922 ⟹ **9.22% profit**. No new theory — just one more term in the chain.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Successive discounts 20% + 10% | 30% | 28% |
| Same SP, ±x% | no profit no loss | x²/100 % **loss** |
| 900 g weight for 1 kg | 10% | 11.11% |
| Averaging profit % across items | arithmetic mean | weighted by CP |
| Markup vs discount at equal % | they cancel | different bases — they never cancel |
| "Discount on marked price" | applied to CP | discount is always on MP |
| Adulteration base | the mixture quantity | the pure quantity |
| "Buy 3 get 1 free" | 33.33% | 25% — base is what you receive |
| "20% of the mixture" vs "20% of the milk" | same thing | 1 : 4 vs 1 : 5 |
| Equating goods, direction | always a profit | larger number on the SP side means a loss |
| Loss % above 100 | accepted | impossible — you've made an error |

---

**The one habit that fixes most errors:** write the chain CP → MP → SP as bare multiplying factors before any arithmetic. Once the problem is a product of factors, base confusion — which causes nearly every wrong answer here — cannot occur, because each factor carries its own base with it.

**Practical exam habits:**

- Assume CP = 100 unless another value is more convenient (e.g. the LCM of the given fractions)
- If the answer options are ugly fractions, you've probably used the wrong base
- Profit % above 100% is possible and legitimate; loss % above 100% is not
- When two effects are given as fractions, look for cancellation before multiplying — CAT builds these in

*Related file: `Mixtures-and-Alligation.md` — adulteration (§8) and weighted profit (§11) are both alligation problems wearing different clothes.*
