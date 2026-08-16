# Extension Prompt: Symmetric Degradation + 3% Social Rate on Fiscal Cost

Paste into the Claude-in-Excel extension, running on the live formatted model (`מודל פחת מואץ 0.3`, sheet `ניתוח פחת מואץ`).

Row/cell references below were read off the v0.3 file. If the sheet has shifted since, locate the rows by their Hebrew labels rather than trusting the numbers.

---

Two independent corrections. Please make both, then run the verification checks at the end.

## Change 1 — apply the performance-degradation factor to the baseline equipment too

Right now the degradation factor is applied only to the **efficient** equipment. The baseline equipment's consumption is held flat. Since the Aug 5 baseline change, both sides of every comparison are the **same technology class** (heat pump vs. heat pump, chiller vs. chiller, VSD vs. fixed-speed compressor), so there is no basis for degrading only one side. The current asymmetry makes modelled savings shrink year over year when they should stay roughly flat, which biases the results against the efficient technology.

### 1a. Scenario A energy-OPEX rows (currently flat, need the degradation factor added)

Apply across columns G:AE. Note each technology uses its own year-index row, horizon cell, OPEX cell and degradation cell — do not cross-reference them.

| Technology | Row | Current formula (col G) | Change to |
|---|---|---|---|
| Heat pump | **117** | `=IF(AND(G$105>=1,G$105<=$F$53),-$F$55,0)` | `=IF(AND(G$105>=1,G$105<=$F$53),-$F$55*(1+$F$54)^(G$105-1),0)` |
| Chiller | **182** | `=IF(AND(G$170>=1,G$170<=$F$73),-$F$75,0)` | `=IF(AND(G$170>=1,G$170<=$F$73),-$F$75*(1+$F$74)^(G$170-1),0)` |
| VSD | **247** | `=IF(AND(G$235>=1,G$235<=$F$93),-$F$95,0)` | `=IF(AND(G$235>=1,G$235<=$F$93),-$F$95*(1+$F$94)^(G$235-1),0)` |

This mirrors exactly what the Scenario B rows (123, 188, 253) already do. VSD's degradation factor is 0, so its numbers will not move — apply it anyway so the three blocks stay structurally identical.

### 1b. Cohort savings rows (the `מחזור התקנה` blocks)

Same issue: baseline consumption is flat inside the bracket while efficient consumption is degraded. With symmetric degradation, the whole *difference* degrades together, so the factor moves outside the parentheses.

| Technology | Rows | Current (col G) | Change to |
|---|---|---|---|
| Heat pump | **149:163** | `...,$F$58*($F$46-$F$47*(1+$F$54)^(G$105-$F149-1)),0)` | `...,$F$58*($F$46-$F$47)*(1+$F$54)^(G$105-$F149-1),0)` |
| Chiller | **214:228** | `...,$F$78*($F$66-$F$67*(1+$F$74)^(G$170-$F214-1)),0)` | `...,$F$78*($F$66-$F$67)*(1+$F$74)^(G$170-$F214-1),0)` |
| VSD | **279:290** | `...,$F$98*($F$86-$F$87*(1+$F$94)^(G$235-$F279-1)),0)` | `...,$F$98*($F$86-$F$87)*(1+$F$94)^(G$235-$F279-1),0)` |

Keep the `IF(AND(...))` guard and the relative `$F149` / `$F214` / `$F279` cohort-index reference exactly as they are — only the expression inside changes. The cohort index must keep stepping down the rows (`$F149`, `$F150`, … `$F163`).

---

## Change 2 — fiscal cost moves to the 3% social discount rate

The firm's decision correctly stays at the private rate (6%, `$F$31`). But the fiscal cost is the **state's** money — deferred tax revenue — so it takes the government's social rate (3%, `$F$32`). `$F$32` is currently defined in the sheet but never referenced by any formula.

**Important structural point:** the fiscal cost is currently just a pointer to the C−B row (`=F136` etc.). That worked only because the firm's gain and the state's loss were identical under a single shared rate. Once the two rates differ, that identity breaks and the fiscal cost has to be computed as its own stream.

### 2a. Replace the three "עלות פיסקלית ליחידה" cells with a real calculation

The state's cost is the year-by-year difference between the accelerated and standard tax shields, discounted at 3%. Both rows already exist in every block.

| Technology | Cell | Current | Change to |
|---|---|---|---|
| Heat pump | **F145** | `=F136` | `=SUMPRODUCT((G112:AE112-G110:AE110)/(1+$F$32)^G105:AE105)` |
| Chiller | **F210** | `=F201` | `=SUMPRODUCT((G177:AE177-G175:AE175)/(1+$F$32)^G170:AE170)` |
| VSD | **F275** | `=F266` | `=SUMPRODUCT((G242:AE242-G240:AE240)/(1+$F$32)^G235:AE235)` |

(In each case the first row is `מגן מס מואץ`, the second is `מגן מס סטנדרטי`, and the third is `שנה ביחס להשקעה`.)

Please also update these three row labels to make the rate explicit, e.g. `עלות פיסקלית ליחידה (NPV, מהוון בשיעור חברתי 3%)`.

### 2b. Repoint everything that consumes the fiscal cost

These currently read the 6% C−B cells (`$F$136`, `$F$201`, `$F$266`) and must now read the new 3% cells (`$F$145`, `$F$210`, `$F$275`).

**Annual streams (columns G:AE):**

| Row | What | Change |
|---|---|---|
| **166** | heat pump, fiscal cost per year | `$F$136` → `$F$145` |
| **231** | chiller, fiscal cost per year | `$F$201` → `$F$210` |
| **293** | VSD, fiscal cost per year | `$F$266` → `$F$275` |
| **165** | heat pump, economic value | in the `IF($F$144=1,$F$135,-$F$136)` branch: `-$F$136` → `-$F$145` |
| **230** | chiller, economic value | `-$F$201` → `-$F$210` |
| **292** | VSD, economic value | `-$F$266` → `-$F$275` |

**Per-1,000-units summary table (columns AN:AR, rows 297-299) — easy to miss, please don't:**

| Cell | Current | Change to |
|---|---|---|
| **AQ297** | `=$F$136*$F$36` | `=$F$145*$F$36` |
| **AQ298** | `=$F$201*$F$36` | `=$F$210*$F$36` |
| **AQ299** | `=$F$266*$F$36` | `=$F$275*$F$36` |
| **AR297** | `=IF($F$144=1,$F$135,-$F$136)*$F$36` | `…,-$F$145)*$F$36` |
| **AR298** | `=IF($F$209=1,$F$200,-$F$201)*$F$36` | `…,-$F$210)*$F$36` |
| **AR299** | `=IF($F$274=1,$F$265,-$F$266)*$F$36` | `…,-$F$275)*$F$36` |

### 2c. Do NOT change these

`F136`, `F201`, `F266` — the `ערך התמריץ - תועלת הפחת המואץ (C−B)` rows — must stay exactly as they are, discounted at 6%. They represent the **firm's** benefit from the incentive, which correctly uses the firm's own rate. After this change the firm's benefit and the state's cost are deliberately different numbers; that is the intended result, not an inconsistency to reconcile.

Likewise leave the payback rows (141/142, 206/207, 271/272), the verdict rows and the additionality factors on the 6% private rate. The adoption decision is the firm's, so it must use the firm's rate.

---

## Verification — expected values after both changes

Computed independently outside Excel. If the live file disagrees materially, stop and flag it rather than adjusting these numbers to match.

**Paybacks and verdicts — no verdict should flip:**

| Technology | Payback B (was) | Payback B (expect) | Payback C (expect) | Verdict |
|---|---|---|---|---|
| Heat pump | 3.374 | **3.179** | 2.234 | incentive flips the decision (unchanged) |
| Chiller | 4.652 | **4.414** | 2.664 | incentive flips the decision (unchanged) |
| VSD | 0.671 | **0.671** (no change) | 0.621 | worth it anyway (unchanged) |

**Fiscal cost per unit — expect a uniform −41% across all three:**

| Technology | Was (6%) | Expect (3%) |
|---|---|---|
| Heat pump | 1,414 | **836** |
| Chiller | 30,750 | **18,174** |
| VSD | 3,581 | **2,117** |
| **Total × 1,000 units** | 35,745,731 | **21,126,029** |

The −41% is expected: a lower discount rate discounts the state's later tax recoupment less, so the net timing cost shrinks.

**Energy and emissions (from change 1 — savings now grow slightly instead of shrinking):**

| | Was | Expect |
|---|---|---|
| Electricity saved, 2026-2050 | 1,514,774,236 kWh | **~1,882,791,244 kWh** |
| CO2e avoided | ~660,442 t | **~820,897 t** |

**Also please check and report:**
- No `#REF!`, `#NAME?`, `#VALUE!` or `#DIV/0!` anywhere after the edits.
- `$F$32` is now actually referenced by formulas (it was previously defined but unused).
- The heat pump payback B (3.179) still sits above the 3-year threshold in `$F$34`. It is the closest of the three to flipping, so confirm it explicitly rather than assuming.
