# MoonActive UA Prep - Practice Problems

## Problem 1: Cohort Diagnosis (Easy)

**Scenario:** You're reviewing Q1 performance for Coin Master. Three channels are active.

**Given Data:**
```
Channel       | Spend  | Installs | D1 Ret | D7 Ret | D30 ARPU | Budget Next Q
Facebook      | $20K   | 50K      | 50%    | 25%    | $0.12    | $25K
Google UAC    | $15K   | 30K      | 45%    | 18%    | $0.08    | $20K
Apple Search  | $10K   | 5K       | 65%    | 40%    | $0.18    | $15K
```

**What You Need to Do:**

1. **Calculate CAC** for each channel (Spend / Installs)
2. **Calculate D30 LTV** (assume $0.05 tail)
3. **Calculate CAC:LTV Ratio** (show as both decimal and 1:X format)
4. **Rank channels** by profitability
5. **Diagnose issues:**
   - Which channel should you pause?
   - Which should you scale?
   - Why?

**Expected Analysis:**
- Facebook: CAC $0.40, LTV $1.49, Ratio 0.27 (1:3.7) → Scale, healthy
- Google: CAC $0.50, LTV $1.01, Ratio 0.50 (1:2.0) → Marginal, consider pausing
- Apple: CAC $2.00, LTV $2.21, Ratio 0.90 (1:1.1) → Expensive but quality, small scale

**Your Answer:**
```
[Write your diagnosis here]
```

---

## Problem 2: Cohort Diagnosis (Medium) - Retention Issue

**Scenario:** Your D7 retention just dropped across all channels. Same channels, but D7 fell from 25% to 15%.

**Given Data:**
```
Updated cohorts (same spend, installs, D1):
Channel       | D1 Ret | D7 Ret (NEW) | D30 ARPU | Notes
Facebook      | 50%    | 15% ↓       | $0.12    | Was 25%
Google UAC    | 45%    | 12% ↓       | $0.08    | Was 18%
Apple Search  | 65%    | 30% ↓       | $0.18    | Was 40%
```

**What Changed:**
- D1 retention stayed the same (good onboarding)
- D7 retention dropped (user leaves after first week)
- D30 ARPU unchanged

**What You Need to Do:**

1. **Recalculate CAC:LTV Ratios** with new D7 retention
2. **Identify what happened:**
   - Is this a product issue?
   - Audience fatigue?
   - Competitive pressure?
3. **Recommend one action** for each channel

**Hint:** D1 is good, so onboarding works. Problem is weeks 2-7 of gameplay.

---

## Problem 3: Campaign Planning (Medium)

**Scenario:** You have a new game launching. $50K monthly budget. Historical benchmarks for similar games:
- Target CAC: $0.50
- Expected D30 LTV: $1.25
- D7 Retention: 25%

**Given:**
- Current estimate: 25% users will pay
- Average D30 ARPU for payers: $0.50
- CPI increases ~15% per 50% budget increase (saturation)

**What You Need to Do:**

1. **Calculate initial user target:**
   - How many installs at $0.50 CAC?
   - How many paying users?
   - Expected revenue by D30?

2. **Build a 3-month scaling plan:**
   - Month 1: $50K budget
   - Month 2: Increase to $75K (expect CPI to rise 15%)
   - Month 3: Increase to $100K (expect another 15% rise)
   
3. **Track payback period:**
   - Each month, when do you recoup CAC?
   - By month 3, is it still healthy?

4. **Risk:** What if D30 LTV drops to $0.90 due to market saturation?

---

## Problem 4: Retention Diagnosis (Hard)

**Scenario:** Your game's D7 retention has been declining for 3 weeks:

```
Week 1 Cohort: D7 = 28%
Week 2 Cohort: D7 = 23% (↓ 5%)
Week 3 Cohort: D7 = 18% (↓ 10%)

Meanwhile:
- D1 retention steady at 48%
- D30 ARPU unchanged at $0.15
- Creative hasn't changed
- No major app updates
```

**What You Need to Do:**

1. **Form three hypotheses** for why D7 is declining
2. **For each hypothesis, propose an A/B test**
3. **Prioritize:** Which test would you run first and why?

**Hint Questions:**
- Is this a product issue? (Check crash logs, session duration)
- Is this audience degradation? (Compare audience size/quality over weeks)
- Is this competitive? (Did competitors launch?)

---

## How to Use These Problems

### For Self-Study:
1. **Don't look at solutions first**
2. **Use the Excel templates** to calculate metrics
3. **Write your analysis** as if presenting to a manager
4. **Then check solutions** and see where you diverged

### Expected Time:
- Problem 1: 15 minutes
- Problem 2: 20 minutes
- Problem 3: 30 minutes
- Problem 4: 30 minutes

### Structure Your Answer:
```
**Problem:** [What's broken or being asked]

**Data:** [Key metrics you calculated]

**Analysis:** [What you found]

**Recommendation:** [What should you do]

**Rationale:** [Why you chose this]
```

---

## Solution Guide (Hidden - Reveal After Attempting)

### Problem 1 Solution

**Calculations:**
- Facebook: CAC = $0.40, LTV = ($0.12×12)+$0.05 = $1.49, Ratio = 0.27 (1:3.7)
- Google: CAC = $0.50, LTV = ($0.08×12)+$0.05 = $1.01, Ratio = 0.50 (1:2.0)
- Apple: CAC = $2.00, LTV = ($0.18×12)+$0.05 = $2.21, Ratio = 0.90 (1:1.1)

**Ranking:**
1. Facebook (1:3.7) - Profitable, scale to $25K
2. Apple (1:1.1) - High CAC, but premium users, maintain at $15K
3. Google (1:2.0) - Below healthy, consider pausing or reducing

**Recommendation:**
- **Scale Facebook:** Best ratio, healthy payback, good retention
- **Maintain Apple:** Expensive but quality. Don't scale yet unless LTV improves
- **Reduce or Pause Google:** CAC is too close to LTV. Investigate why D7 is lower than Facebook despite similar spend

---

## Tips for Interview

**When you solve these:**
1. Always calculate CAC first (most common mistake: forgetting this)
2. Always calculate LTV (D30 ARPU × 12 + tail)
3. Always compare to benchmarks (1:3 is healthy)
4. Always explain the "so what" (not just numbers, but action)
5. Always consider: Is this audience/creative/product problem?
