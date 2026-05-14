# User Acquisition Manager - Interview Prep Guide

**For:** Junior Acquisition Manager role at gaming studios (MoonActive, Playtika, Scopely, etc.)  
**Created:** 2026-05-14  
**Status:** Practice reference - use before interviews/home tests

---

## Core Metrics You Must Know

### The Golden Ratios

**CAC (Cost of Acquiring a Customer)**
- Formula: `Total Marketing Spend / Number of Paying Users`
- Example: Spent $10,000, got 5,000 users → CAC = $2/user
- Healthy range: Varies by game type, but typically $0.50-$3.00 for mobile

**LTV (Lifetime Value)**
- Formula: `(D30 ARPU × 12 months) + tail revenue`
- OR: `Sum of all revenue from user over their lifetime`
- Example: User spends $0.80 lifetime → LTV = $0.80
- Key insight: LTV must be > CAC (usually 3x-5x better)

**Payback Period**
- Formula: `CAC / Monthly ARPU`
- Example: CAC $2, monthly ARPU $0.20 → Payback = 10 months
- Meaning: Takes 10 months to recoup acquisition cost from this user

**ROAS (Return on Ad Spend)**
- Formula: `Revenue by Day X / Advertising Spend`
- D7 ROAS (first week): 0.30-0.70 is healthy
- D30 ROAS (full month): 0.80-2.0+ is healthy
- Example: Spent $100, earned $35 by D7 → D7 ROAS = 0.35

**CPI (Cost Per Install)**
- Same as CAC but for installs (before monetization)
- Used to track channel efficiency
- Formula: `Total Spend / Number of Installs`

### Cohort Analysis (What You'll Analyze)

**D1/D7/D30 Retention**
- Percentage of Day 0 users who return on Day 1, 7, 30
- Example: D7 retention 25% = 1 in 4 users come back after 1 week
- Healthy: 20-40% D7 for casual games, 40-60% for mid-core

**D1/D7/D30 ARPU**
- Revenue per user on each day
- Example: D1 ARPU $0.05 = average user spends 5¢ on day 1
- Typically: D1 > D7 > D30 (unless monetization improves over time)

**Cohort LTV Calculation**
```
Day 0: 1,000 users install
Day 1: 500 retention, $50 revenue → D1 ARPU = $0.05
Day 7: 250 retention, $30 revenue → D7 ARPU = $0.03
Day 30: 100 retention, $20 revenue → D30 ARPU = $0.02
Estimated LTV ≈ $0.10-0.15 (depending on tail assumptions)
```

---

## Marketing Channels (Where Money Goes)

| Channel | Budget % | Typical CPI | Strengths | Weaknesses |
|---------|----------|-------------|-----------|------------|
| **Facebook/Instagram** | 30-40% | $0.30-1.50 | Best targeting, retargeting, control | iOS tracking limited post-IDFA |
| **Google UAC** | 25-35% | $0.40-2.00 | Scale, intent-based, Android-friendly | Lower LTV users sometimes |
| **Apple Search Ads** | 15-20% | $0.50-3.00 | High-intent, fast payback | iOS only, expensive |
| **Programmatic/DSP** | 5-10% | $0.20-1.00 | Cheap testing, experimentation | Lower quality, less control |
| **Organic/ASO** | 5-10% | $0 | Free, loyal users, high LTV | Slow to scale |

**Key insight:** iOS users (Apple Search Ads) cost more but have higher LTV. Android (Google UAC) is volume. You need both strategies.

---

## Common Take-Home Test Formats

### Format 1: Cohort Diagnosis
**You're given:** A cohort table with retention/ARPU by day  
**You do:**
1. Calculate LTV for each cohort
2. Rank channels by CAC:LTV ratio
3. Identify what's broken (product? creative fatigue? audience quality?)
4. Recommend actions (pause channel, improve creative, optimize onboarding)

**Example problem:**
```
Cohort Table (100 users per cohort):
Channel       | CAC  | D1 Ret | D7 Ret | D30 ARPU | Est. LTV
Facebook      | $0.50| 45%   | 20%   | $0.08    | $0.12
Google UAC    | $0.40| 40%   | 15%   | $0.06    | $0.08
Apple Search  | $1.20| 60%   | 35%   | $0.12    | $0.18

Q: Which channel is most profitable? Which should you pause? Why?
A: Apple Search (1.2:18 = 1:1.5) then Facebook (0.5:12 = 1:2.4) then Google (0.4:8 = 1:2.0).
   Pause Google UAC if budget is tight. Invest in Apple Search ads (best ratio).
```

### Format 2: Campaign Planning
**You're given:** Budget ($50K), game type (match-3 casual), current LTV estimate ($0.15), target CAC  
**You do:**
1. Set target CAC based on LTV (aim for 1:3 to 1:5 ratio)
2. Allocate budget by channel (% per channel)
3. Build 3-month scaling plan (budget growth, CPI assumptions, payback modeling)
4. Identify risks (CPI inflation, retention decline, platform limits)

**Example problem:**
```
Game: Candy Match (casual match-3)
Budget: $50K/month
Estimated LTV: $0.15
Target CAC: $0.05 (gives 1:3 ratio)

Q: How many installs can you buy? How does CPI inflation affect this?
A: $50K / $0.05 = 1M installs at target CAC.
   But CPI rises ~15-20% per 50% budget increase.
   Month 1: 1M users, Month 2: ~800K users (CPI rose to $0.06), Month 3: ~600K users.
   Plan scaling carefully. Consider platform saturation.
```

### Format 3: Retention Problem
**You're given:** D7 retention dropped from 30% to 18%, ARPU is flat  
**You do:**
1. Diagnose root cause: Product issue? Creative saturation? Audience quality declining?
2. Propose A/B tests or changes to test hypothesis
3. Prioritize actions (quick wins vs. long-term)

**Example problem:**
```
Problem: D7 retention dropped 30% → 18% in 2 weeks. Everything else flat.
Possible causes:
- Product bug (check crash logs, session duration)
- Creative fatigue (audiences saw same ad too many times)
- Audience quality declining (expanded targeting too broad)
- Seasonality (unlikely if ARPU flat)

First test: Pause 30% of audience expansion, refresh creative.
Measure: Does D7 return to 25%+? If yes → was audience/creative. If no → product issue.
```

---

## Excel Skills Checklist

You MUST be comfortable with these in Excel:

- [ ] Pivot tables (aggregate data by channel/cohort)
- [ ] VLOOKUP / INDEX-MATCH (look up LTV from table)
- [ ] Formulas for CAC, LTV, payback (use absolute/relative references correctly)
- [ ] Scenario modeling (what-if: if CPI rises 20%, what happens to profitability?)
- [ ] Charting (line chart showing cohort curves, bar chart by channel)
- [ ] Data validation (dropdowns for channel selection)
- [ ] Conditional formatting (highlight profitable vs. unprofitable cohorts)

**Pro tip:** Build ONE master template. Use it for every problem so you're fast and consistent.

---

## MoonActive-Specific Research

**Games they make:**
- World War Doh (strategy/casual)
- Coin Master (slots/collection)
- Merge Magic! (match/merge)
- Multiple mid-core strategy titles

**UA strategy clues:**
- Heavy Facebook/Instagram spend (visible in ads library)
- Strong casual audience focus (not hardcore gamers)
- Cross-promotion between titles (UA efficiency play)
- Known for aggressive scaling in hot markets

**What to mention in interview:**
- "I've looked at your portfolio — World War Doh scaled well in LATAM. How did you approach that market's specific unit economics?"
- Shows you did your homework, speaks their language

---

## Practice Plan

### Week 1: Foundations
- [ ] Read research report (2h)
- [ ] Build Excel LTV/CAC calculator (2h)
- [ ] Solve 2 cohort diagnosis problems (2h each = 4h)

### Week 2: Applied Skills
- [ ] Solve 2 campaign planning problems (3h each = 6h)
- [ ] Build your own 3-month scaling model (2h)
- [ ] Mock take-home test under time pressure (90 min)

### Week 3: Polish
- [ ] Deep dive on MoonActive's games (1h)
- [ ] Practice articulating your reasoning aloud (1h)
- [ ] Solve 1 retention diagnosis problem (2h)
- [ ] Review all Excel formulas (1h)

---

## Interview Talking Points

**Why you're good for this role:**
- Economics background = you understand unit economics instinctively
- Policy analysis = you're used to data-driven optimization under constraints
- Excel mastery = you move fast on modeling

**Questions to ask them:**
- "What's your current D7 retention and LTV? How does that inform your CAC targets?"
- "How do you think about iOS vs. Android strategy post-IDFA?"
- "What surprised you about UA in your first month?"

**Red flags to avoid:**
- Don't claim expertise you don't have (learn fundamentals first)
- Don't ignore the business impact (it's not just about installs; it's about profitability)
- Don't forget to stress-test your models (what if retention drops 20%?)

---

## Resources

**Research report:** `research/job-market/20260514_ua-fundamentals-gaming.md`  
**Job tracker:** `projects/job-search/tracker.md` — track your MoonActive progress here

**External learning (when ready):**
- Mobile game monetization blogs (Adjust, App Annie/data.ai)
- YouTube: "Mobile UA strategy" talks from GDC/conferences
- Case studies: Check how games you play handle monetization/UA

---

## Quick Reference: Formulas to Memorize

```
CAC = Total Spend / Paying Users
LTV = (D30 ARPU × 12) + tail
Payback = CAC / Monthly ARPU
ROAS = Revenue by Day X / Spend
CPI = Spend / Installs
CAC:LTV Ratio = CAC / LTV (aim for 1:3 to 1:5)
```

Good luck! You've got this. 🎮
