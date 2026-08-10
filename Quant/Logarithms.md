# Logarithms

> CAT quant. A log is just "what power?". Every question is either a law-application, a base change, or a disguised quadratic. Small topic, high accuracy payoff.

---

## 1. The definition and why it settles most doubts

**log_b(x) = y ⟺ bʸ = x**

Read every log statement back as an exponent statement and the ambiguity disappears. log₂32 = 5 because 2⁵ = 32.

**Domain conditions — check these before answering anything:**
- The **argument must be positive**: x > 0
- The **base must be positive and ≠ 1**: b > 0, b ≠ 1

These conditions are not pedantry — CAT builds questions where the algebra yields two roots and one violates a domain condition. Rejecting it is the whole question.

---

## 2. The laws

| Law | Form |
|---|---|
| Product | log(mn) = log m + log n |
| Quotient | log(m/n) = log m − log n |
| Power | log(mᵖ) = p·log m |
| **Base of a power** | log_(bᵖ)(m) = (1/p)·log_b m |
| Change of base | log_b m = log_a m / log_a b |
| Reciprocal | log_b a = 1/log_a b |
| Identity | log_b b = 1, log_b 1 = 0 |
| Exponent–log | b^(log_b x) = x |
| Swap | a^(log_b c) = c^(log_b a) |

**The change-of-base rule is the master key.** When bases differ, convert everything to a single base — usually base 10, base 2, or "log" with no base if it cancels.

**Chain rule for logs:** log_a b × log_b c × log_c d = log_a d. Everything telescopes. Spot a chain and cancel it whole.

**Worked example:** log₂3 × log₃4 × log₄5 × log₅8 = log₂8 = **3**

---

## 3. Values worth knowing

- log₁₀2 ≈ 0.3010, log₁₀3 ≈ 0.4771, log₁₀7 ≈ 0.8451
- From these: log₁₀4 = 0.6020, log₁₀5 = 1 − log2 = 0.6990, log₁₀6 = 0.7781, log₁₀8 = 0.9031, log₁₀9 = 0.9542

**Number-of-digits rule:** the number of digits in N = **⌊log₁₀N⌋ + 1**.

**Worked example:** How many digits does 2¹⁰⁰ have?
- log₁₀(2¹⁰⁰) = 100 × 0.3010 = 30.10 ⟹ digits = 30 + 1 = **31**

**Leading-zeros rule:** for 0 < N < 1, the number of zeros between the decimal point and the first significant digit = **⌈|log₁₀N|⌉ − 1**.

**Worked example:** How many zeros follow the decimal point in 2⁻²⁰ before the first non-zero digit?
- log₁₀(2⁻²⁰) = −20 × 0.3010 = −6.02
- Zeros = ⌈6.02⌉ − 1 = 7 − 1 = **6**
- Check: 2⁻²⁰ = 0.00000095367… ✓

---

## 4. Type 1 — Logs reduce to a quadratic

Whenever the same log expression appears at two powers, **substitute t**.

**Worked example:** Solve (log₂x)² − 3log₂x + 2 = 0.
- Let t = log₂x ⟹ t² − 3t + 2 = 0 ⟹ t = 1 or 2
- x = 2¹ = **2** or x = 2² = **4**
- Both are positive ⟹ both valid.

**Worked example (mixed bases):** Solve log₂x + log_x2 = 5/2.
- Let t = log₂x, so log_x2 = 1/t
- t + 1/t = 5/2 ⟹ 2t² − 5t + 2 = 0 ⟹ t = 2 or 1/2
- x = 4 or x = √2

The t + 1/t shape comes straight from the reciprocal law. Recognising it is worth training — see `Algebra.md` §1.

---

## 5. Type 2 — Nested log equations

"log(log(log x)) = 0" and its relatives. **Work strictly from the outside in**, converting one layer at a time to exponential form.

**Worked example:** Solve log₂(log₃(log₄ x)) = 0.
- Outermost: log₂(…) = 0 ⟹ the inside = 2⁰ = 1
- So log₃(log₄x) = 1 ⟹ log₄x = 3¹ = 3
- ⟹ x = 4³ = **64**

**Worked example (different bases and a non-zero value):** Solve log₃(log₂(log₃ x)) = 1.
- log₂(log₃x) = 3¹ = 3
- log₃x = 2³ = 8
- x = 3⁸ = **6561**

**Domain check for nested logs:** every layer's argument must be positive, which forces increasing lower bounds as you go outward. For log₂(log₃(log₄x)) to be defined you need log₄x > 1, i.e. x > 4. Any candidate root failing this is rejected.

**The habit:** peel one layer per line. Trying to collapse two layers at once is where sign and base errors enter.

---

## 6. Type 3 — Product-zero conditions

CAT frequently sets up an equation that factors into a product equal to zero, and the real work is deciding **which factors give valid values**.

**The principle:** if AB = 0 then A = 0 or B = 0 — but each branch must then be checked against the log domain conditions.

**Worked example:** Solve (log₂x)(log₂x − 3) = 0.
- Branch 1: log₂x = 0 ⟹ x = 1
- Branch 2: log₂x = 3 ⟹ x = 8
- Both positive ⟹ **x = 1 or 8**

**Worked example with a rejected branch:** Solve (x − 2)·log₃(x − 2) = 0 for real x.
- Branch 1: x − 2 = 0 ⟹ x = 2. But then log₃(0) is undefined ⟹ **rejected**
- Branch 2: log₃(x − 2) = 0 ⟹ x − 2 = 1 ⟹ x = **3** ✓
- Only one valid solution.

That rejection is the entire point of the question type. Whenever a factor sets a log's *argument* to zero, discard it.

**Variable-base version:** equations like log_x(something) = k also require **x > 0 and x ≠ 1**. So a root of x = 1 is always rejected, however clean it looks.

**Worked example:** Solve log_x(x² − 3x + 3) = 1.
- ⟹ x² − 3x + 3 = x ⟹ x² − 4x + 3 = 0 ⟹ x = 1 or 3
- x = 1 is an invalid base ⟹ **x = 3** only.

---

## 7. Type 4 — Inequalities

log_b x is **increasing when b > 1** and **decreasing when 0 < b < 1**.

So when you drop the logs in an inequality:
- Base > 1 ⟹ the inequality direction is preserved
- Base < 1 ⟹ the inequality **flips**

And always intersect the result with the domain (argument > 0).

**Worked example:** Solve log₀.₅(x − 1) > 2.
- Base 0.5 < 1 ⟹ flip: x − 1 < (0.5)² = 0.25
- Domain: x − 1 > 0 ⟹ x > 1
- Answer: **1 < x < 1.25**

Forgetting the flip is the standard error; forgetting the domain is the second.

---

## 8. Logs and progressions

If a, b, c are in **GP**, then log a, log b, log c are in **AP** (a log turns multiplication into addition). CAT uses this to disguise GP questions as log questions and vice versa. See `Progressions-AP-GP.md` §5.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| log(m + n) | log m + log n | no such law — only log(mn) splits |
| (log x)² | 2 log x | that's log(x²); (log x)² is the square |
| Base of a power | log_(b²)m = 2 log_b m | it's ½ log_b m |
| Product-zero branch | accept both roots | reject any making an argument 0 or a base 1 |
| Inequality with base < 1 | keep the direction | **flip** it |
| Nested logs | collapse two layers at once | peel one layer per line |
| Negative argument | accepted | domain violation — reject |
| log_x with x = 1 | valid | base can never be 1 |

---

## Practical exam habits

- Convert every log to exponential form the moment you're unsure. It resolves nearly every doubt in this topic.
- Bring all logs to a common base before doing anything else.
- Substitute t for the repeated log expression — most "hard" log questions are quadratics wearing a costume.
- After solving, **check every root against the domain**. In this topic, checking is not optional; it is frequently where the marks are.
- Memorise log₁₀2 and log₁₀3. Almost every numeric log question in CAT is built from those two.

**Where this feeds forward:** `Algebra.md` §1 and §6 (t + 1/t, quadratics, extraneous roots), `Progressions-AP-GP.md` §5 (GP ↔ AP under logs), `Number-System.md` §5 (digit counts and powers).
