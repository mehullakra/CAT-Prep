# Calendars

> CAT quant. Every calendar question is arithmetic mod 7. Convert any span of time into "odd days" — the remainder left after removing whole weeks — and the day of the week falls out.

Grouped with Clocks in most textbooks, but it shares no machinery with it. Clocks are relative speed; calendars are modular arithmetic. Learn them separately.

---

## 1. Core idea — odd days

**Odd days = the remainder when a number of days is divided by 7.**

Weeks don't change the day of the week, so only the remainder matters. 100 days later is the same weekday as 2 days later, because 100 = 14×7 + 2.

The day code, counting from Sunday:

| Odd days | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Day | Sun | Mon | Tue | Wed | Thu | Fri | Sat |

Every question reduces to: **total odd days → look up this row**.

**The one thing to internalise:** you never count days. You count remainders, and you reduce mod 7 at every step so the numbers stay small.

---

## 2. Odd days in a year

- Ordinary year = 365 days = 52 weeks + **1 odd day**
- Leap year = 366 days = 52 weeks + **2 odd days**

So the same date moves forward 1 weekday each ordinary year, 2 across a leap year.

**Leap year rule:** divisible by 4 → leap; but a century year must be divisible by 400. So 1900, 1800, 2100 are **not** leap; 1600, 2000, 2400 **are**.

**Odd days in centuries** (derive once, then memorise the last row):

- 100 years = 76 ordinary + 24 leap = 76 + 48 = 124 days ≡ 124 − 119 = **5 odd days**
- 200 years = 10 ≡ **3 odd days**
- 300 years = 15 ≡ **1 odd day**
- 400 years = 20 + 1 (the extra leap day of the 400th year) = 21 ≡ **0 odd days**

| Period | 100 yrs | 200 yrs | 300 yrs | 400 yrs |
|---|---|---|---|---|
| Odd days | 5 | 3 | 1 | 0 |

**400 years = 0 odd days** is the most useful fact in the topic. It means the whole calendar repeats identically every 400 years, and it lets you strip 1600 or 2000 off any year for free.

---

## 3. Odd days in a month

Take each month's length mod 7:

| Month | Days | Odd days |
|---|---|---|
| Jan | 31 | 3 |
| Feb | 28 / 29 | 0 / 1 |
| Mar | 31 | 3 |
| Apr | 30 | 2 |
| May | 31 | 3 |
| Jun | 30 | 2 |
| Jul | 31 | 3 |
| Aug | 31 | 3 |
| Sep | 30 | 2 |
| Oct | 31 | 3 |
| Nov | 30 | 2 |
| Dec | 31 | 3 |

You don't need to memorise this column — it's just 31 → 3, 30 → 2, 28 → 0, 29 → 1. Knowing which months have 31 days is enough.

---

## 4. Type 1 — Day of the week for a given date

**Method (four steps, always the same):**

1. Split the date as (year − 1) complete years + days elapsed in the current year.
2. Break the complete years into the largest multiple of 400 (0 odd days), then leftover centuries, then leftover years.
3. For the leftover years, count leap years L and ordinary years O: odd days = 2L + O, reduced mod 7.
4. Add the days elapsed in the current year up to and including the date, mod 7. Total mod 7 → day code.

**Worked example: what day was 15 August 1947?**

Step 1 — complete years = 1946, plus days in 1947 up to 15 Aug.

Step 2 — 1946 = 1600 + 300 + 46.

- 1600 → 0 odd days
- 300 → 1 odd day

Step 3 — the 46 years 1901–1946:

- Leap years: 1904, 1908, …, 1944 → (1944 − 1904)/4 + 1 = 11
- Ordinary years: 46 − 11 = 35
- Odd days = 2(11) + 35 = 57 ≡ 57 − 56 = 1

Running total: 0 + 1 + 1 = 2.

Step 4 — days in 1947 up to 15 Aug (1947 is not a leap year):

- 31 + 28 + 31 + 30 + 31 + 30 + 31 + 15 = 227
- 227 ≡ 227 − 224 = 3

Total odd days = 2 + 3 = 5 → **Friday**.

**Worked example: what day was 26 January 1950?**

- 1949 = 1600 + 300 + 49 → 0 + 1 + [leaps 1904…1948 = 12, ordinary = 37 → 2(12) + 37 = 61 ≡ 5] = 6
- Days in 1950 up to 26 Jan = 26 ≡ 5
- Total = 6 + 5 = 11 ≡ 4 → **Thursday**

**Shortcut when a reference day is given.** If the question says "1 Jan 2024 was a Monday, what day is 1 Jan 2027?", skip all of the above. Just count odd days of the years *in between*: 2024 is a leap year (2 odd days, because 29 Feb lies between the two dates), 2025 → 1, 2026 → 1. Total 4 → Monday + 4 = **Friday**. This is faster and far less error-prone, so always check whether a reference date was supplied.

---

## 5. Type 2 — Repeating calendars

**Question form:** "Which year has the same calendar as 2005?"

For two years to share a calendar, two conditions must hold:

1. The total odd days between them ≡ 0 mod 7
2. Both years are the same type — both leap, or both ordinary

**Method:** start from the given year and accumulate odd days (1 per ordinary year, 2 per leap year) until the running total is a multiple of 7. The **next** year is the answer.

**Worked example: same calendar as 2005?**

| Year | Odd days | Running total |
|---|---|---|
| 2005 | 1 | 1 |
| 2006 | 1 | 2 |
| 2007 | 1 | 3 |
| 2008 (leap) | 2 | 5 |
| 2009 | 1 | 6 |
| 2010 | 1 | 7 ≡ 0 |

Total hits a multiple of 7 after 2010, so **2011** repeats 2005's calendar.

**The pattern worth memorising** (holds when no century-year irregularity intervenes):

- **Ordinary year** → repeats after **6 or 11 years** (11 if the year is just after a leap year, 6 otherwise)
- **Leap year** → repeats after **28 years**

So 2008 repeats in 2036; 1996 repeats in 2024.

**When 28 fails:** the 28-year rule assumes every 4th year in the gap is a leap year. Crossing a non-leap century year (1900, 2100) breaks it. 1896's calendar does not repeat in 1924 — count odd days manually whenever the span crosses a year like 1900.

---

## 6. Type 3 — Counting a weekday in a period

**Question form:** "What is the probability that a leap year has 53 Sundays?"

**Method:** any year contains 52 complete weeks — so 52 of each weekday guaranteed. The *odd days* are the extra ones, and only those can create a 53rd.

- **Ordinary year:** 1 odd day. It's equally likely to be any of the 7 days → P(53 Sundays) = **1/7**
- **Leap year:** 2 odd days, and they are consecutive. The 7 possible pairs are (Sun,Mon), (Mon,Tue), …, (Sat,Sun). Two of them contain a Sunday → P(53 Sundays) = **2/7**

**Worked example:** probability that a leap year has 53 Saturdays **and** 53 Sundays.

- Only one pair out of 7 is (Sat, Sun) → **1/7**

**The general rule for months.** A month is 4 complete weeks plus its odd days, and the weekdays that occur 5 times are exactly the weekdays of the *first* few dates:

| Month length | Odd days | Weekdays occurring 5 times |
|---|---|---|
| 31 days | 3 | weekdays of the 1st, 2nd, 3rd |
| 30 days | 2 | weekdays of the 1st, 2nd |
| 29 days (Feb) | 1 | weekday of the 1st |
| 28 days (Feb) | 0 | none — all seven occur 4 times |

So the 5-times weekdays are always a **consecutive block** starting from the day the month begins on.

**Worked example:** a month has 5 Mondays and 5 Tuesdays. What could it be?

- Mon and Tue must both sit in the block, so the block is at least 2 long → the month has 30 or 31 days
- 30 days: block = {1st, 2nd} = {Mon, Tue} → month starts on **Monday**
- 31 days: block = three consecutive days containing Mon and Tue → {Sun, Mon, Tue} or {Mon, Tue, Wed} → month starts on **Sunday or Monday**

**Worked example:** a month has 5 Mondays and 5 Thursdays. What could it be?

- Mon and Thu are 3 apart, so the block would have to be at least 4 long
- The largest block is 3 (a 31-day month) → **impossible**, no such month exists

That's the whole value of the block idea: it turns a fiddly counting question into "is the gap small enough?"

---

## 7. Type 4 — Days between two dates

**Method:** count forward month by month using the odd-day column, or subtract day-of-year numbers. Decide the convention first: "days between 3 March and 10 March" is normally 7, but "the 10th is how many days after the 3rd" is also 7. If the question says *inclusive of both days*, add 1.

**Worked example:** 15 March 2024 was a Friday. What day is 15 September 2024?

Go same-date to same-date and add the odd days of each month you leave:

- 15 Mar → 15 Apr: March has 31 days ≡ 3
- 15 Apr → 15 May: April 30 ≡ 2
- 15 May → 15 Jun: May 31 ≡ 3
- 15 Jun → 15 Jul: June 30 ≡ 2
- 15 Jul → 15 Aug: July 31 ≡ 3
- 15 Aug → 15 Sep: August 31 ≡ 3
- Total = 3 + 2 + 3 + 2 + 3 + 3 = 16 ≡ 2
- Friday + 2 = **Sunday**

Going same-date-to-same-date and summing the odd days of the months you pass through is the fastest route. Note it's the *starting* month's length each time, not the ending month's.

---

## Traps

| Trap | Wrong | Right |
|---|---|---|
| Century leap years | 1900 is leap (÷4) | century year must be ÷400 → 1900 is not, 2000 is |
| Odd days in a leap year | 1 | 2 |
| 100 years | 0 odd days | 5 odd days |
| Day code | 1 = Sunday | 0 = Sunday, 1 = Monday |
| Counting complete years | uses the given year | uses (year − 1) complete years |
| Feb in the current year | counted as 28 always | 29 if the *current* year is leap and the date is after Feb |
| Repeating calendar | always +11 or +28 | verify by summing odd days; century years break the pattern |
| Leap-year repeat crossing 1900/2100 | +28 | count manually |
| 53 Sundays in an ordinary year | 2/7 | 1/7 (only 1 odd day) |
| Month-to-month day shift | uses target month's length | uses the starting month's length |
| Reducing at the end only | 227 + 61 + … then mod 7 | reduce mod 7 at every step |

---

**The one habit that fixes most errors:** reduce mod 7 immediately at each step. If any number on your page is bigger than 6, you're carrying arithmetic you don't need — and large numbers are where the slips happen.

**Sanity check that costs 3 seconds:** the answer must be one of seven days, and shifting one calendar year forward moves it by exactly 1 (or 2 across a leap day). If your answer for "same date next year" isn't one day later, recheck the leap-year handling first.

**Connection:** none to Clocks, despite the exam grouping. The real neighbour is remainders — see `Number-System.md` §6 for the modular arithmetic this file leans on.
