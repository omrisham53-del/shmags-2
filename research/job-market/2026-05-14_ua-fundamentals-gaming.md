# User Acquisition (UA) Fundamentals for Gaming Studios

**Context:** Junior Acquisition Manager interview prep at MoonActive and similar studios  
**Date:** 2026-05-14  
**Model:** Claude Haiku 4.5  
**For:** Omri Shamgar, economics/policy analyst  

---

## Part 1: Core UA Metrics & Economics

### 1.1 The Unit Economics Foundation

Every UA strategy rests on four interconnected metrics:

| Metric | Formula | What It Tells You |
|--------|---------|-------------------|
| **CPI (Cost Per Install)** | Total spend / # installs | How much you pay per user acquisition |
| **CAC (Customer Acquisition Cost)** | Total marketing spend / # paying users | Cost to acquire one *paying* customer (stricter than CPI) |
| **LTV (Lifetime Value)** | ARPU × Average Lifetime (months) | Total revenue expected from one user |
| **Payback Period** | CAC / (ARPU / LTV months) | Months to recover acquisition cost |
| **ROAS (Return on Ad Spend)** | Revenue within X days / ad spend | ROI on a single campaign (often measured D7 ROAS, D30 ROAS) |

### 1.2 The Golden Rule: CAC < LTV

If CAC exceeds LTV, the game is unprofitable at scale. Healthy studios operate at CAC:LTV ratios of 1:3 to 1:5.

**Example calculation:**
- Game earns $0.80 ARPU over lifetime
- LTV at 6-month avg lifetime = $0.80 × 6 = $4.80
- If CAC is $1.20, CAC:LTV ratio = 1:4 (healthy)
- If CAC is $3.00, CAC:LTV ratio = 1:1.6 (unprofitable, must reduce spend)

### 1.3 Payback Period: The Cash Flow Reality

Payback period = how long until revenue from one user covers their acquisition cost.

**Formula:** CAC / monthly ARPU

- If CAC = $1.20 and monthly ARPU = $0.30, payback = 4 months
- Studios aim for 3-6 month payback (longer = cash flow risk, shorter = more scalable)

**Why it matters:** A game with 8-month payback can't scale fast because you're bleeding cash for 8 months before breaking even per user. A game with 2-month payback can reinvest aggressively.

### 1.4 ROAS and Time-Based Cohorts

ROAS is measured at different time windows:

- **D1 ROAS** = Revenue on day 1 / spend = Usually 0.05-0.15 (5-15% return on day 1)
- **D7 ROAS** = Revenue by day 7 / spend = Usually 0.30-0.70 (30-70% by day 7)
- **D30 ROAS** = Revenue by day 30 / spend = Usually 0.80-2.0+ (fully profitable campaigns are 1.2+)

If your D30 ROAS is under 1.0, the campaign is unprofitable. Studios often use D7 ROAS as an early predictor (learnings within a week vs. waiting 30 days).

---

## Part 2: Marketing Channels for Mobile Games

### 2.1 Primary Channels & Characteristics

| Channel | Typical CPI | Best For | Control Level | Learning Curve |
|---------|------------|----------|----------------|-----------------|
| **Facebook/Instagram** | $0.30-$1.50 | Broad audiences, lookalikes, retargeting | High (native tools) | Medium |
| **Google (App Campaigns, UAC)** | $0.40-$2.00 | Scale, intent-based, iOS post-IDFA | High | Medium |
| **Apple Search Ads** | $0.50-$3.00 | High-intent search users | High | Low (simple bidding) |
| **Programmatic (Demand Side Platform)** | $0.20-$1.00 | Bulk inventory, retargeting, real-time bidding | Medium (auction-based) | Hard |
| **TikTok Ads** | $0.40-$1.80 | Younger audiences, viral potential | High | Medium-Hard |
| **Organic (ASO + word-of-mouth)** | $0 | Long-term, sustainable growth | Very High | Ongoing |
| **IronSource / Unity Mediation** | $0.15-$0.80 | Remnant inventory, lower-CPM users | Low | Low |

### 2.2 The iOS/Android Divide (2026 Context)

**iOS (Apple):**
- Apple's Privacy Tracking Transparency (ATT) framework limits device-level tracking
- Advertisers can't see which specific user converted (aggregate conversion optimization only)
- Higher CPI due to less optimization data, but higher quality users (wealthier, higher LTV)
- Apple Search Ads + Facebook still effective via aggregate data

**Android:**
- Google Play Services allow more granular tracking (AAID)
- Better optimization possible, lower CPI
- Higher volume, lower average user value
- Programmatic and Facebook more effective

**Strategic implication:** Many studios now run separate campaigns for iOS/Android with different budgets and expectations.

### 2.3 Channel Mix Strategy

Healthy portfolio (mature game):
- 30-40% Facebook/Instagram (stable, retargeting)
- 25-35% Google UAC (scale)
- 15-20% Apple Search Ads (high-intent)
- 5-10% TikTok or programmatic (experimentation)
- 5-10% Organic/ASO (long-term)

Early-stage or limited budget:
- 50% Facebook (familiarity, ease of setup)
- 30% Google UAC
- 20% organic push (word-of-mouth, streamer seeding)

---

## Part 3: UA Strategy & Planning

### 3.1 Target CAC Setting (The Planning Exercise)

This is the core planning skill. Given a game, you work backwards from LTV to set a target CAC, then budget accordingly.

**Example:** You're launching a new match-3 puzzle game.

**Step 1:** Estimate LTV
- Benchmark: Similar match-3 games have 35% D1 retention, 15% D7 retention, 5% D30 retention
- Your game targets 40% D1, 18% D7, 6% D30 (slightly better)
- Assume 40% of D30 users remain active in months 2-3 (churn curve flattens)
- Average revenue per user: $0.05 D1, $0.08 by D7, $0.25 by D30
- Month 2-3 average $0.05/user/month
- **LTV estimate:** $0.25 + ($0.05 × 2 × 0.4) = $0.25 + $0.04 = **$0.29**

**Step 2:** Set target CAC
- Healthy CAC:LTV ratio for match-3 = 1:3 to 1:4
- Target CAC = $0.29 / 3.5 = **~$0.08 per install**

**Step 3:** Budget calculation
- Launch phase: Acquire 500K users
- Total UA spend: 500K × $0.08 = **$40,000 for launch month**
- Phased scaling: Month 2-3 at 300K/month if profitable

**Step 4:** Monitor and adjust
- Track actual D7 ROAS within 7-10 days
- If D7 ROAS > 0.40, you're on track for profitable acquisition
- If D7 ROAS < 0.25, likely missing LTV target; reduce spend or pause

### 3.2 Scaling Strategy

**Early scaling (CAC is proven profitable):**
1. Increase budget on best-performing channels (usually 30-50% weekly)
2. Widen audience parameters (lookalike audiences, interest expansion)
3. Test new channels (if core channels are maxed out)
4. Expect CPI to rise slightly as you scale (law of diminishing returns)

**Rule of thumb:** You can typically scale 2-3x before CPI rises 20-30%. Beyond that, new channels or creative refreshes needed.

**Creative fatigue:** Ad creative loses effectiveness after ~2-3 weeks. Studios rotate new creative (video, static, gameplay clips) constantly.

---

## Part 4: Analytics & Retention Metrics

### 4.1 Cohort Analysis (Essential Skill)

Cohort analysis groups users by acquisition date and tracks their behavior over time.

**Example cohort table (fictional game):**

| Cohort | Install Count | D1 Retention | D7 Retention | D30 Retention | D1 ARPU | D7 ARPU | D30 ARPU |
|--------|---------------|--------------|--------------|----------------|---------|---------|----------|
| May 1  | 50,000        | 52%          | 18%          | 5%             | $0.08   | $0.25   | $0.42    |
| May 8  | 65,000        | 50%          | 16%          | 4%             | $0.06   | $0.22   | $0.35    |
| May 15 | 72,000        | 48%          | 14%          | 3.5%           | $0.05   | $0.18   | $0.28    |

**Interpretation:**
- D1 retention dropping (52% → 48%) suggests onboarding issues
- D7 ARPU declining (0.25 → 0.18) suggests monetization funnel problems
- Later cohorts are weaker; likely caused by creative fatigue or channel saturation

**Action:** Pause scaling, refresh creative, or optimize onboarding.

### 4.2 Retention Curves

Classic retention curves for mobile games:

```
Day 1-3:  Steep drop (50-70% lose interest immediately)
Day 3-7:  Moderate drop (slow exit of casuals)
Day 7-30: Gentle slope (engaged players settle)
Day 30+:  Flat line (whales + addicted players)
```

**Target benchmarks (industry):**
- D1 retention: 40-50% (good), 30-40% (average), <30% (poor)
- D7 retention: 15-25% (good), 10-15% (average), <10% (poor)
- D30 retention: 5-10% (good), 3-5% (average), <3% (poor)

Hyper-casual games see much lower retention (D1: 20-30%, D7: 5-10%). Core games see higher (D1: 60%+, D7: 30%+).

### 4.3 Churn and Cohort LTV Calculation

**Churn rate** = % of users who stop engaging each period.

If D7 retention is 15%, churn from day 7 is 85%.

**LTV with churn:**

```
LTV = ARPU_D1 + (ARPU_D2-7 × Retention_D7) + (ARPU_D8-30 × Retention_D30) + ...
```

Simpler version (approximation):
```
LTV ≈ D30 ARPU / (1 - Retention_D30)
```

This accounts for tail revenue beyond day 30 assuming churn rate stabilizes.

---

## Part 5: Take-Home Test Formats & Case Studies

### 5.1 Typical MoonActive / Playtika Format

**Time:** 1-2 hours  
**Tools:** Excel, Google Sheets  
**Scenarios:** 2-3 real or realistic game scenarios

#### **Test Type 1: Unit Economics Diagnosis**

**Prompt:** "Here's a cohort table for a casual game launched 30 days ago. Analyze and recommend next steps."

Given table:
- Installs, D1/D7/D30 retention, D1/D7/D30 ARPU
- UA spend per channel (Facebook, Google, Apple Search Ads)
- Current CAC by channel

**What they're testing:**
1. Can you calculate LTV?
2. Can you identify which channels are profitable?
3. Can you spot trends (churn acceleration, ARPU drop)?
4. Can you recommend budget reallocation?

**Example answer structure:**
```
LTV Calculation:
- Estimated LTV (using D30 ARPU / 1-churn): ~$0.45
- Target CAC (1:3 ratio): $0.15

Channel Performance:
- Facebook: CPI $0.12, D7 ROAS 0.35 → Profitable, scale 20%
- Google: CPI $0.25, D7 ROAS 0.22 → Unprofitable, pause
- Apple Search: CPI $0.08, D7 ROAS 0.50 → Highly profitable, increase budget 50%

Recommendation:
- Shift 30% of Google spend to Apple Search Ads
- Increase Facebook by 20% week-over-week
- Pause underperforming Facebook segments
```

#### **Test Type 2: Campaign Planning & Budgeting**

**Prompt:** "You have $50K to acquire users for a new hyper-casual game. Design a UA strategy for months 1-3."

**What you need to deliver:**
1. Target LTV estimate (with assumptions about benchmarks)
2. Target CAC and CAC:LTV ratio
3. Monthly budget breakdown by channel
4. Scaling assumptions (how much CPI rises as you scale)
5. Break-even and payback calculations
6. Success metrics (what D7 ROAS do you need to hit?)

**Example framework:**

```
Assumptions:
- Hyper-casual game: D1 retention 25%, D7 10%, D30 2%
- Monetization: D1 ARPU $0.04, D7 $0.10, D30 $0.14
- LTV estimate: $0.14 / (1 - 0.02) = $0.14

Target CAC (1:3.5 ratio): $0.04
Budget Plan:
- Month 1: $50K → 1.25M installs (target 50% channel distribution)
  - Facebook: $15K (30%)
  - Google: $20K (40%)
  - Apple Search: $10K (20%)
  - Organic: $5K (10%)

Month 1 Projections:
- Expected D7 ROAS: 0.35-0.40 (viable for hyper-casual)
- Expected payback: 5-7 months (longer than core games, acceptable for casual)
- Month 2: If D7 ROAS > 0.35, scale to $75K budget
```

#### **Test Type 3: Retention Problem Diagnosis**

**Prompt:** "Your game's D7 retention dropped from 18% to 12% over two weeks while ARPU stayed flat. Diagnose."

**What they're testing:** Root cause analysis, not just spreadsheets.

**Framework:**
1. **Is it cohort-specific?** (Did only recent cohorts drop, or all cohorts?)
   - If recent cohorts: likely new creative performing worse or channel quality change
   - If all cohorts: likely game change (update, bug, monetization change)

2. **Is it channel-specific?** (Did one channel's cohort drop while others held?)
   - If Facebook cohorts dropped: creative fatigue, audience saturation
   - If all channels dropped: product issue

3. **Correlate with events:** Did you launch an update? Change monetization? Release new creative?

**Example answer:**
```
Root Cause: Likely creative fatigue on Facebook (70% of traffic)
Evidence: All cohorts show drop, but Feb 15-28 cohorts (new creative) show recovery
Solution:
1. Pause bottom-50% Facebook creative by performance
2. Launch 2-3 new creative variations (gameplay footage, user testimonials)
3. Test new lookalike audiences
4. Monitor D7 metric within 7 days of new creative launch
Expected outcome: Recovery to 15-16% within 10 days
```

### 5.2 Real-World Case Examples

#### **Case 1: Mid-Core Game Scaling Issue**

**Scenario:** RPG game has achieved PMF (product-market fit). D7 retention steady at 22%. Current CAC $1.20, LTV $4.50 (1:3.75 ratio, healthy). But CPI rising sharply as budget scales.

- Month 1: $100K spend, CPI $0.80
- Month 2: $150K spend, CPI $1.05
- Month 3: $200K spend, CPI $1.20
- Month 4: $250K spend, CPI $1.35 (approaching LTV limit)

**Analysis:**
- Each 20-25% budget increase raises CPI ~15-20% (law of diminishing returns)
- At $300K spend, projected CPI $1.50 (exceeds LTV)
- Channel saturation: Facebook has ~80% reach, Google hitting limits

**Recommendations:**
1. **Pause scaling on Facebook/Google.** Invest in new channels:
   - Launch TikTok campaigns (untapped inventory, lower CPI $0.60-0.80)
   - Test programmatic DSP (can be $0.50-0.70 CPI)
2. **Optimize creative.** Refresh top 10 underperforming creatives.
3. **Focus on retention.** Each 1% improvement in D7 retention = 3-4% LTV increase.
   - Implement mid-game content updates every 2 weeks
   - A/B test monetization timing (earlier/later first IAP offer)
4. **Target new segments.** Use lookalike audiences for high-LTV cohorts (whales).

**Expected outcome:** Stabilize CPI at $1.10-1.20, achieve $300K/month sustainable spend.

#### **Case 2: Hyper-Casual Game with High Churn**

**Scenario:** Casual game with 30% D1 retention but only 8% D7. D1 ARPU decent at $0.06, but D7 ARPU drops to $0.09 (not growing much after day 1). Estimated LTV only $0.12. Current CAC $0.05 (1:2.4 ratio, below healthy 1:3).

**Problem:** Even though acquisition is cheap, retention is so bad that LTV is low and scaling headroom is limited.

**Analysis:**
- Can scale to CAC $0.04 maximum (LTV / 3)
- Current CAC $0.05 leaves little margin
- D7 drop suggests onboarding or game design issue

**Recommendations:**
1. **Fix day 1-7 experience (primary lever).** Invest in game design:
   - Simplify tutorials (top cause of D1 drop)
   - Add progression/milestones to day 7 (engagement hooks)
   - A/B test different onboarding flows
   - Goal: Push D7 retention from 8% to 12-15%
   
2. **Only after retention improves, scale UA.** Increasing spend now amplifies a bad product.
   
3. **Monetization timing.** If D7 ARPU isn't growing, first IAP may be too early or poorly designed.
   - Test moving first offer from day 3 to day 5 or day 7
   - Test lower price point (higher conversion, lower ARPU but higher LTV)

**Expected outcome (if retention improves):** D7 retention 12% → LTV $0.16 → CAC headroom to $0.04 → sustainable scaling.

---

## Part 6: What Studios Like MoonActive Look For in UA Managers

### 6.1 Technical Skills (In Order of Priority)

1. **Excel proficiency (highest priority)**
   - Pivot tables, VLOOKUP, INDEX/MATCH
   - Charting and trend analysis
   - Unit economics modeling
   - Scenario planning (what-if analysis)
   - **Why:** Every decision is made with a spreadsheet. This is non-negotiable.

2. **Data literacy & SQL (secondary)**
   - Understand joins, filtering, aggregation
   - Can pull cohort data independently
   - Can validate numbers from analytics platform
   - **Why:** You'll need to QA reported metrics and understand data pipelines.

3. **Analytics platforms (tertiary)**
   - Adjust, AppsFlyer, or similar (2-3 weeks learning curve)
   - Understand attribution, cohort tables, retention curves
   - Read dashboards critically

### 6.2 Soft Skills (Equally Important)

1. **Problem-solving & logical thinking**
   - Root cause analysis (from diagnose-the-problem tests)
   - Decision-making under uncertainty
   - Prioritization (which channel to invest in, what to fix first)

2. **Communication**
   - Explain trade-offs clearly (higher ROAS vs. volume)
   - Present findings to non-technical stakeholders (game designers, C-suite)
   - Write clear recommendations

3. **Analytical mindset**
   - Hypothesis testing (predict what will happen, validate)
   - Comfort with iteration and testing
   - Continuous learning (gaming trends, new platforms)

### 6.3 Red Flags (What Disqualifies You)

- Weak Excel skills (pivot tables, formulas not working)
- Can't calculate LTV or CAC (fundamental misunderstanding)
- Confusing CAC with CPI
- Can't read or interpret a cohort table
- No reasoning for trade-offs ("Just increase budget because ROAS is good")
- Doesn't know iOS vs. Android differences (especially post-IDFA)

---

## Part 7: Common Interview Questions & Frameworks

### 7.1 Strategy Questions

**Q: "How would you scale a profitable casual game from $100K/month spend to $500K/month?"**

Framework:
1. Check product health (retention, LTV stable?)
2. Identify channel saturation points
3. Plan channel diversification (Facebook → Google → Apple → TikTok → DSP)
4. Set CPI limit for each channel (work backwards from LTV)
5. Plan creative refresh cadence
6. Monitor cohort quality (don't let ARPU drop as volume rises)

**Q: "Our D7 ROAS is 0.25 but our D30 ROAS is 0.95. Should we scale?"**

Framework:
1. D7 ROAS 0.25 suggests breakeven at D7, but positive at D30
2. Payback period: long (likely 6-8 months)
3. Risk: User behavior could change; D30 projections unreliable
4. Recommendation: Only scale if LTV model is backed by historical cohort data (not projection)
5. Test scaling small (10-20% budget increase) and monitor actual D30 ROAS

### 7.2 Diagnosis Questions

**Q: "A Facebook campaign had CPI $0.50 on Day 1, CPI $0.80 on Day 2, and CPI $1.20 on Day 3. What happened?"**

Framework:
1. CPI rising sharply suggests budget scaling (Facebook throttling / bidding up)
2. Steep curve (50% day-to-day increase) is unusual; check for technical issues first
   - Did auction demand spike (competitor ads)?
   - Did targeting get too narrow (budget exhausting small audience)?
   - Did bid strategy change?
3. If normal scaling, this is expected (smaller audiences have higher cost)
4. Diagnosis: Likely audience saturation; widen targeting, test lookalike, or pause

**Q: "Your ARPU dropped 40% week-over-week. Debug."**

Framework:
1. Is it cohort-specific or all cohorts?
   - All cohorts: Likely monetization change (update, disabled IAP, price change)
   - Specific cohorts: Likely channel/audience quality change
2. Check for product changes
   - Release notes? Monetization tuning? Ad frequency changes?
3. Check channel mix changes
   - Did you shift spend from high-LTV to low-LTV channel?
4. Check user demographics
   - Did geographic targeting shift (e.g., from US/EU to lower-income regions)?
5. Quick fix: Revert recent changes; root cause analysis if persists

### 7.3 Trade-off Questions

**Q: "Channel A has CPI $0.40 and D7 ROAS 0.35. Channel B has CPI $0.70 and D7 ROAS 0.55. Where should you allocate the next $10K?"**

Framework:
1. Calculate profitability per channel
   - Channel A: For every $1 spend, get $0.35 back by D7 = Net -$0.65 (losing money early)
   - Channel B: For every $1 spend, get $0.55 back by D7 = Net -$0.45 (less bad, but still negative)
2. But look at D30 ROAS (not given; probe for data)
   - If Channel A's D30 ROAS is 0.90+ but Channel B's is 0.60, A is better long-term
3. If forced to choose with only D7 data, choose Channel B (higher ROAS = better D30 trajectory likely)
4. Real answer: "I need D30 data. If not available, run small test ($1K) on each to gather 7-day cohorts, compare"

---

## Part 8: Excel Modeling for Unit Economics

### 8.1 Template: UA Campaign ROI Model

```
INPUT ASSUMPTIONS:
Installs                    100,000
D1 Retention %              45%
D7 Retention %              18%
D30 Retention %             5%
D1 ARPU                     $0.05
D7 ARPU                     $0.12
D30 ARPU                    $0.18
Estimated Tail LTV (beyond D30)  $0.08
Total Spend                 $15,000

CALCULATIONS:
CPI                         = Total Spend / Installs         = $0.15
D1 Paying Users             = Installs × 20% (monetization %)= 20,000
D7 Paying Users             = Installs × D7 Retention × 15% = 2,700
D30 Revenue                 = Installs × D30 ARPU            = $1,800
LTV                         = D30 ARPU + Tail LTV            = $0.26
Payback Period (months)     = CPI / (ARPU per month)         = 2.5 months
ROAS D7                     = (Installs × D7 ARPU) / Spend   = 0.36
ROAS D30                    = (Installs × D30 ARPU) / Spend  = 0.36 (if no tail)
Profit (30-day window)      = Revenue - Spend                = $1,800 - $15,000 = -$13,200
Break-even at LTV           = (Installs × LTV) - Spend       = $26,000 - $15,000 = +$11,000
```

### 8.2 Scaling Scenario Model

For each budget increase, CPI rises (diminishing returns). Template:

```
Week 1: Spend $5K   → Installs 50,000  → CPI $0.10
Week 2: Spend $7K   → Installs 58,000  → CPI $0.12  (14% CPI increase)
Week 3: Spend $10K  → Installs 62,000  → CPI $0.16  (33% CPI increase)
Week 4: Spend $15K  → Installs 65,000  → CPI $0.23  (44% CPI increase)

Rule: Every 50% budget increase = ~15-20% CPI increase (for healthy channels)
```

Scaling stops when CPI reaches your CAC limit (LTV / 3).

---

## Part 9: Real Interview Take-Home: Example Problem

*This is a simplified version of what MoonActive might ask.*

**Scenario:**

You're given a spreadsheet with cohort data for a match-3 game launched 45 days ago:

| Cohort | Installs | D1 Ret. | D7 Ret. | D30 Ret. | D1 ARPU | D7 ARPU | D30 ARPU | Spend | Channel |
|--------|----------|---------|---------|----------|---------|---------|----------|-------|---------|
| Apr 15 | 80,000   | 50%     | 20%     | 6%       | $0.06   | $0.18   | $0.35    | $8K   | FB      |
| Apr 22 | 95,000   | 48%     | 18%     | 5.5%     | $0.05   | $0.16   | $0.30    | $12K  | FB      |
| Apr 29 | 110,000  | 45%     | 15%     | 4%       | $0.04   | $0.12   | $0.22    | $16K  | Google  |
| May 6  | 85,000   | 46%     | 14%     | 3%       | $0.03   | $0.09   | $0.15    | $14K  | Apple   |

**Questions:**

1. **Calculate LTV for each cohort** (assume 2-3 month tail revenue of $0.05/month)

2. **Calculate CAC and ROAS D7 / D30 for each cohort**

3. **Rank channels by profitability.** Which should you scale? Which should you pause?

4. **Identify trends.** What's happening to your game? (Hint: Retention and ARPU both declining)

5. **Recommend next steps** (3-5 actions with rationale)

---

## Expected Solution Outline

**1. LTV Calculation:**
```
Cohort Apr 15: $0.35 + ($0.05 × 2) = $0.45
Cohort Apr 22: $0.30 + ($0.05 × 2) = $0.40
Cohort Apr 29: $0.22 + ($0.05 × 2) = $0.32
Cohort May 6:  $0.15 + ($0.05 × 2) = $0.25
```

**2. CAC & ROAS:**
```
Cohort Apr 15: CAC = $8K/80K = $0.10, ROAS D7 = ($80K × $0.18)/$8K = 1.8
Cohort Apr 22: CAC = $12K/95K = $0.126, ROAS D7 = ($95K × $0.16)/$12K = 1.27
Cohort Apr 29: CAC = $16K/110K = $0.145, ROAS D7 = ($110K × $0.12)/$16K = 0.83
Cohort May 6:  CAC = $14K/85K = $0.165, ROAS D7 = ($85K × $0.09)/$14K = 0.55
```

**3. Channel Ranking:**
```
Facebook (Apr 15): LTV $0.45, CAC $0.10, Ratio 1:4.5 ✓ Profitable, scale
Facebook (Apr 22): LTV $0.40, CAC $0.126, Ratio 1:3.2 ✓ Profitable, scale
Google (Apr 29):   LTV $0.32, CAC $0.145, Ratio 1:2.2 ✗ Marginal, monitor
Apple (May 6):     LTV $0.25, CAC $0.165, Ratio 1:1.5 ✗ Unprofitable, pause
```

**4. Trend Analysis:**
- Retention declining across all cohorts (creative fatigue, saturation)
- ARPU declining (monetization friction or audience quality drops)
- Later cohorts (Google, Apple) performing significantly worse
- Likely: Facebook saturation; later channels getting lower-quality users

**5. Recommendations:**
1. **Pause Apple Search Ads immediately.** CAC exceeds LTV; bleeding money.
2. **Reduce Google spend by 50%.** ROAS 0.83 is break-even at D7; D30 likely unprofitable.
3. **Double down on Facebook,** but refresh creative. Launch 3-4 new ad variations to combat fatigue.
4. **Investigate monetization.** D1 ARPU down to $0.03 suggests fewer users engaging with shop. Test price reductions or new offer timing.
5. **Pause scaling pending improvements.** Monitor new creative cohorts; if D7 ARPU recovers to $0.14+, resume scaling.

---

## Part 10: Resources & Tools for Interview Prep

### Tools You Should Know
- **Excel:** Pivot tables, VLOOKUP, INDEX/MATCH, charting, data validation
- **Google Sheets:** Same as Excel (easier for interviews, cloud-based)
- **Analytics platforms:** Adjust, AppsFlyer (free accounts available)
- **Market research:** Sensor Tower (app rankings, install estimates), App Annie

### Key Formulas to Memorize
```
CAC = Total Spend / Paying Users
CPI = Total Spend / Installs
LTV = D30 ARPU + (Tail Monthly ARPU × Months)
Payback = CAC / Monthly ARPU
ROAS Dx = (Revenue by day X / Total Spend)
Retention D7 = (Active Users on D7 / Installs on D1) × 100%
Churn Rate = 1 - Retention Rate
```

### Practice Case Studies
- Research published UA strategies from mobile games (Clash of Clans post-mortem, Candy Crush strategy breakdowns)
- Analyze public app store data (download trends, rating changes correlate with updates)
- Build your own spreadsheet model (pick a game, estimate cohorts, model scaling scenarios)

---

## Summary for Omri

This is a specialist role. You're not building data pipelines; you're optimizing customer acquisition economics. Key interview signals:

1. **Can you calculate and interpret LTV / CAC?** (Core metric literacy)
2. **Can you diagnose why a cohort underperformed?** (Root cause analysis)
3. **Can you build a scalable budget plan?** (Strategic thinking)
4. **Do you understand channel trade-offs?** (Business judgment)
5. **Can you model unit economics in Excel?** (Tool proficiency)

Your policy/economics background is a genuine advantage here. You already think in terms of incentives, optimization, and trade-offs. Gaming terminology is learnable in 2-3 weeks. Focus interview prep on #1, #2, #3 above.

**Next steps:** Build one comprehensive Excel model (LTV, CAC, scaling scenarios), practice 2-3 cohort diagnosis problems, and interview a few UA folks at gaming studios to understand current best practices.
