# Cohort Diagnosis Guide - MoonActive UA Prep

## What Is A Cohort Diagnosis Problem?

You're given a table of user cohorts (grouped by install date or channel) with:
- Cost of acquiring users (CAC)
- Retention rates (D1, D7, D30)
- ARPU by day (revenue per user)
- Your job: identify what's broken and recommend fixes

## The Analysis Framework

### Step 1: Calculate LTV for Each Cohort

LTV = (D30 ARPU × 12 months) + tail revenue estimate

**In Excel:**
```
=($D_ARPU * 12) + $tail_estimate
```

**Example:**
- D30 ARPU: $0.08
- Tail estimate: $0.04 (conservative)
- LTV = ($0.08 × 12) + $0.04 = $1.00
```

### Step 2: Calculate CAC:LTV Ratio

**Healthy range:** 1:3 to 1:5 (CAC is 1/3 to 1/5 of LTV)

**In Excel:**
```
=CAC / LTV
```

**Interpretation:**
- Ratio 1:2.0 = For every $1 spent, you get $2 back (marginal)
- Ratio 1:3.0 = For every $1 spent, you get $3 back (healthy)
- Ratio 1:5.0 = For every $1 spent, you get $5 back (excellent)

### Step 3: Rank Channels by Profitability

Sort cohorts by CAC:LTV ratio (best first). This shows which channel is most efficient.

### Step 4: Diagnose the Problem

Ask these questions about worst-performing cohorts:

**If CAC is high but LTV is good:**
- Channel is expensive but attracts quality users
- Decision: Pay premium or find cheaper channel?

**If CAC is low but LTV is terrible:**
- Cheap users, but they don't monetize
- Problem: Audience quality OR product issue
- Test: Compare D1 retention. If it's already low → product issue. If D1 is good but D7 drops → creative fatigue

**If both CAC and LTV are bad:**
- Worst scenario. Consider pausing channel entirely.

**If retention drops sharply (D1→D7 or D7→D30):**
- Likely: Product bug, bad onboarding, or audience mismatch
- Test: Check crash logs, session duration, feature usage

## The Diagnosis Template

Use this structure in your answer:

```
**Problem Identified:**
[Cohort X has CAC:LTV ratio of 1:1.8, below healthy 1:3 threshold]

**Root Cause Hypothesis:**
[Low LTV driven by poor D7 retention (15% vs. 25% benchmark)]

**Evidence:**
[D1 retention is 45%, suggesting good onboarding, but D7 drops sharply]

**Recommendation:**
[Likely audience mismatch or creative fatigue. Test: Pause 30% of audience expansion, refresh creative. Measure D7 in 1 week.]

**Alternative Hypothesis:**
[If creative refresh doesn't fix it, investigate product issue in weeks 2-7 of user lifecycle]
```

## Common Patterns

| Pattern | Cause | Fix |
|---------|-------|-----|
| D1 low, D7 also low | Product issue (crash, bad UX) | Fix product |
| D1 good, D7 bad | Creative fatigue OR audience saturation | Refresh creative, narrow targeting |
| D1 good, D7 good, D30 collapses | Late-game monetization issue | Check monetization events after day 7 |
| All retention high, LTV low | Audience isn't spending | Adjust targeting for higher-LTV users OR improve monetization |

## Example Problem

**Given:**
```
Cohort Table (1000 users per cohort):
Channel       | CAC  | D1 Ret | D7 Ret | D30 ARPU | 
Facebook      | $0.50| 45%   | 20%   | $0.08    |
Google UAC    | $0.40| 40%   | 15%   | $0.06    |
Apple Search  | $1.20| 60%   | 35%   | $0.12    |
```

**Your Analysis:**

1. **Calculate LTV** (assume $0.02 tail):
   - Facebook: ($0.08 × 12) + $0.02 = $0.98
   - Google: ($0.06 × 12) + $0.02 = $0.74
   - Apple: ($0.12 × 12) + $0.02 = $1.46

2. **Calculate Ratios:**
   - Facebook: $0.50 / $0.98 = 1:1.96 (marginal)
   - Google: $0.40 / $0.74 = 1:1.85 (marginal)
   - Apple: $1.20 / $1.46 = 1:1.22 (weak)

3. **Rank:** Apple Search > Facebook > Google UAC

4. **Diagnosis:**
   - Apple has best ratio (1:1.22) despite highest CAC
   - Facebook and Google are below healthy threshold (1:3)
   - Problem: Poor retention on Facebook/Google (D7 is 20% and 15% vs. Apple's 35%)
   - Root cause: Likely audience quality declining or creative fatigue
   - Recommendation: Pause Google (lowest ratio), refresh creative on Facebook, invest in Apple Search

---

**Use the COHORT_DIAGNOSIS_EXCEL.xlsx template to practice this framework.**
