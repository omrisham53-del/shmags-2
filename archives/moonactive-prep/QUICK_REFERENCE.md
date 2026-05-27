# MoonActive UA - Quick Reference Card

Print this out or keep it open while practicing.

## Key Term: ARPU

**ARPU = Average Revenue Per User**

The average amount of money each user generates by a specific day (D1, D7, D30, etc.).

**Example:**
- 100 users installed on Day 0
- Total revenue from those 100 users by Day 7: $12
- D7 ARPU = $12 ÷ 100 = $0.12 per user

**Why it matters:**
- D1 ARPU tells you early monetization (how quickly users spend)
- D7 ARPU tells you if users stick around and spend
- D30 ARPU predicts lifetime value

**Pattern:** D1 > D7 > D30 (users spend more early, then taper off)

## Core Formulas

| Metric | Formula | What It Means |
|--------|---------|---------------|
| **CAC** | Total Spend ÷ Paying Users | How much did you pay per customer? |
| **CPI** | Total Spend ÷ Total Installs | Cost per install (before monetization) |
| **LTV** | (D30 ARPU × 12) + Tail | Total revenue from user over lifetime |
| **Payback** | CAC ÷ (D30 ARPU ÷ 30) | Months to recoup acquisition cost |
| **ROAS** | Revenue by Day X ÷ Spend | Return on ad spend (D7, D30) |
| **CAC:LTV Ratio** | CAC ÷ LTV | How much CAC costs vs. LTV (1:3 is healthy) |

## Healthy Benchmarks

| Metric | Healthy Range | What's Wrong |
|--------|---------------|-------------|
| CAC:LTV Ratio | 1:3 to 1:5 (0.20-0.33) | <0.33 = Excellent | 0.33-0.50 = Good | >1.0 = Pause |
| D1 Retention | 30-60% | <20% = Product issue or bad targeting |
| D7 Retention | Casual 20-40%, Core 40-60% | <15% = Creative fatigue or product bug |
| D30 Retention | 5-15% (steep drop expected) | If flat = no long-term engagement |
| Payback Period | <12 months | >12 months = Taking too long to profit |
| D7 ROAS | 0.30-0.70 | <0.20 = Unprofitable channel |
| D30 ROAS | 0.80-2.0+ | <0.50 = Marginal, >2.0 = Excellent |

## Retention Curve Pattern

Healthy retention usually looks like:
```
D1: 50% → D7: 25% → D30: 10% → D90: 5%
(Steep drop, then flattens)
```

Red flags:
- **Flat D1-D7:** Product is broken
- **Cliff at D7-D14:** Creative fatigue or audience mismatch
- **Plateau at D30:** Maybe monetization issue or churn cliff

## Channel Characteristics

| Channel | Typical CPI | Typical LTV Users | Strengths | Weaknesses |
|---------|------------|-------------------|-----------|-----------|
| **Facebook** | $0.30-1.50 | Mid LTV | Targeting, retargeting, scale | iOS tracking limited |
| **Google UAC** | $0.40-2.00 | Lower LTV | Scale, intent, Android | Less control |
| **Apple Search** | $0.50-3.00 | High LTV | High intent, quality | Expensive, iOS only |
| **Programmatic** | $0.20-1.00 | Variable | Cheap testing | Low quality, no control |
| **Organic** | $0 | High LTV | Free, loyal users | Slow to scale |

## Common Interview Questions

### Question: "We're at $0.50 CAC with $1.50 LTV. Should we scale?"
**Answer:** Yes. Ratio is 1:3, which is healthy. Plan scaling with 15% CPI inflation per 50% budget increase.

### Question: "D7 retention just dropped from 30% to 15%. Why?"
**Answer:** 
- Check D1 (if high, product OK) 
- Check creative spend (saturation?)
- Check targeting (audience quality?)
- Most likely: Creative fatigue or audience saturation

### Question: "Which channel should I pause?"
**Answer:** 
- CAC:LTV ratio > 0.50 with no improvements coming = Pause
- Or: If ROAS at D7 < 0.20, not enough early monetization

### Question: "How do you think about iOS vs Android?"
**Answer:** 
- iOS users are expensive (Apple Search CPI $2+) but high LTV
- Android users are cheaper (Google UAC $0.40-1) but lower LTV
- Need both strategies: Premium path (iOS) + Volume path (Android)

## Tricks & Common Mistakes

❌ **Don't:**
- Forget to include tail revenue in LTV (assume +$0.05-0.10)
- Confuse CAC with CPI (CPI is before monetization, CAC is per payer)
- Ignore payback period (some channels take 24+ months)
- Use only D30 metrics (D7 tells you early health)

✅ **Do:**
- Always compare channels side-by-side with ratio
- Check D1 first to diagnose product vs. audience
- Track both ROAS and CAC:LTV (tells different stories)
- Build 3-month scaling models (saturation hits fast)
- Ask: "Is this scalable?" not just "Is this profitable?"

## Excel Tips

**Must-have functions:**
- `=A1/B1` (division for CAC, ROAS)
- `=A1*12` (annualize D30)
- `=IF(condition, yes, no)` (status flags)
- `=TEXT(1/C1, "1:0.00")` (format as 1:X ratio)
- `=CONCATENATE()` (combine metrics in analysis)

**Column setup (template in Excel files):**
- Col A: Metric name
- Col B: Input value (yellow fill)
- Col C: Formula result (blue fill)
- Col D: Benchmark or notes

## Interview Checklist

Before you answer a question:
- [ ] Did I calculate CAC correctly?
- [ ] Did I calculate LTV with both D30 ARPU and tail?
- [ ] Did I compare to healthy benchmarks?
- [ ] Did I identify root cause (audience/creative/product)?
- [ ] Did I recommend a specific action?
- [ ] Did I explain the business impact?

## Formulas to Memorize

```
CAC = Spend ÷ Paying Users
LTV = (D30 ARPU × 12) + Tail
Ratio = CAC ÷ LTV
ROAS D7 = Revenue by Day 7 ÷ Spend
Payback = CAC ÷ Monthly ARPU
```

---

**Keep this page open while practicing. Reference it until the formulas feel automatic.**
