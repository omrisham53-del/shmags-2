# Baseline Technology Data Points (Open-Source Reference)

**Status:** Draft for Daniel's review (step 1 of Daniel's process: gather → review with Daniel → verify with Rafi)
**Date:** 2026-07-06
**Purpose:** First-pass baseline reference points for the tax incentive model, per technology. All figures are international open-source averages — not yet validated against actual Israeli grant-fund installations or Rafi's engineering judgment.

**Capacity collapse (2026-08-12):** each technology below is now modeled at 1 averaged capacity point instead of 2 (plain midpoint of the two points still documented here) -- see `2026-08-12-morning-model-fixes.md` for the computed averaged values (heat pump 55kW, chillers 300RT, VSD 97.5kW) and which parameters carried over flat vs. needed averaging. The 2-point tables below are kept as the sourcing record, not replaced.

**CapEx sourcing (2026-07-12, corrected):** CapEx comes from Omri's own grant-program-rounds extraction, not from this file. An open-source CapEx pass was attempted and then removed once Omri clarified he already has real CapEx data pulled from the grant program rounds and will use that directly — no need to source or estimate CapEx here. This file covers efficiency, capacity, hours, and fuel data only.

Each technology below uses its own industry-standard efficiency metric (not a blanket COP), and every data point carries a source link. Where a value differs across the two capacity points, or is given as a range, the reasoning is stated explicitly — capacity and efficiency are kept as separate, independent axes unless there's a real documented reason to link them.

---

## 1. משאבות חום (Heat Pumps – Water Heating)

**Baseline correction #2 (2026-08-05, Daniel's call at the market-analysis meeting):** the baseline is now a **standard-efficiency heat pump**, not a mazut/diesel-fired oven — same structure as the chiller technology (baseline = less efficient unit of the same type, efficient = higher-efficiency unit of the same type), not a fuel-switching comparison. This supersedes the 2026-07-08 correction below, which is kept for the record, not deleted. Reason given: the fuel-consumption sizing approach this baseline required (CBS national mazut/diesel data, low-temp ceiling, PRTR) was never going to give a reliable *annual installation* figure (a stock, not a flow) — not a reversal on what the heat pump project is, just a recognition that comparing against a fuel-burning baseline was the wrong tool for sizing how many projects happen per year. See section 1c below for the new baseline data. Section 1b (mazut/diesel oven) is no longer the active baseline but is left in place since the fuel-vs-electric efficiency comparison itself may still be useful context for the chapter's narrative.

**Baseline correction #1 (2026-07-08, superseded above):** Originally assumed the baseline was a conventional electric resistance water heater (COP 1.0) — this matched what was hardcoded in `generate_tax_model.py` (`name_baseline: "דוד חשמל קונבנציונלי"`). Omri checked his notes and confirmed Rafi specifically flagged **mazut or diesel-fired ovens/boilers** as what's actually being replaced. This changes the comparison from electric-vs-electric to fuel-combustion-vs-electric — the same structural comparison as the electric steam section (#4) below, not a simple COP-vs-COP ratio. `generate_tax_model.py`'s baseline name still needs updating to match on the work computer (separate task).

**Data correction (2026-07-12):** Omri caught three issues with the original pass: (1) the 150kW "capacity ceiling" wasn't actually supported by the cited source — the Sprsun page cited only goes up to 70kW, 150kW was an unsourced "practical ceiling" argument; (2) the flat 3.5-4.0 COP band ignored that the actual product pages each list a specific COP, and it moves *opposite* capacity within this product line (smaller unit is more efficient); (3) heat pump (efficient) and mazut/diesel oven (baseline) data were interleaved in one table — split into two below so each technology's real numbers stay separate.

**Efficiency metric used:** COP under manufacturer-reported test conditions for the heat pump (efficient) side; fuel-to-heat combustion efficiency (ASME PTC 4 basis) for the mazut/diesel baseline side.

### 1a. Heat pump (efficient technology)

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 40 kW (37/45kW model) | Real product, not an estimate | [Sprsun 37-45kW commercial unit](https://sprsunheatpump.com/37KW-45KW-Commercial-Air-Source-Heat-Pump-for-Water-Heater-and-Room-Heating-pd6657665.html) |
| **Capacity point 2 (high)** | 70 kW (top of the 42/57.6/70kW model's range) | Real product ceiling — corrects the earlier 150kW figure, which this same source does not actually support | [Sprsun 42-70kW unit](https://sprsunheatpump.com/42-70KW-Commercial-Air-to-Water-Heat-Pump-Space-Heating-Cooling-System-pd6187665.html) |
| **COP — at 40kW capacity** | 4.13 (manufacturer-reported) | Actual spec-sheet value for the 37/45kW unit | [Sprsun 37-45kW product page](https://sprsunheatpump.com/37KW-45KW-Commercial-Air-Source-Heat-Pump-for-Water-Heater-and-Room-Heating-pd6657665.html) |
| **COP — at 70kW capacity** | 3.23-3.24 (manufacturer-reported) | Actual spec-sheet value for the 42/57.6/70kW unit at its top point — notably *lower* than the smaller unit. Real inverse capacity-COP relationship within this product line, contradicting the earlier "flat across capacity" assumption | [Sprsun 42-70kW product page](https://sprsunheatpump.com/42-70KW-Commercial-Air-to-Water-Heat-Pump-Space-Heating-Cooling-System-pd6187665.html) |
| **Power (electrical input)** | ~9.7 kW at 40kW capacity (40÷4.13) — ~21.6 kW at 70kW capacity (70÷3.235) | Derived using the real capacity-matched COP figures above, not a generic band | Derived from the two sourced spec pages |

### 1b. Mazut/diesel oven (baseline technology)

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity points** | 40 kW / 70 kW (thermal) | Sized to match the heat pump's real capacity points above, not independently sourced | Matched to 1a |
| **Baseline efficiency (fuel-to-heat)** | 82-85% | Reused from the electric steam section's sourcing — standard fire-tube/water-tube fuel-oil-fired units without heat recovery run 80-88% under ASME PTC 4; same equipment class whether producing steam or hot water | [ASME PTC 4](https://www.asme.org/codes-standards/find-codes-standards/fired-steam-generators); [fuel-to-steam efficiency explainer](https://miuraboiler.com/what-is-fuel-to-steam-efficiency-for-boilers/) |
| **Fuel caloric value (energy content)** | Diesel (סולר): 0.085 ton/MWh — Mazut (מזוט): 0.088 ton/MWh | Real MRV-sourced figures from Omri's own Excel model, not open-source. Converts fuel input energy (MWh) to fuel mass (tons) for baseline OPEX (fuel cost = tons × ₪/ton). Inverse gives energy density: ~11.76 MWh/ton diesel, ~11.36 MWh/ton mazut — consistent with published diesel/heavy-fuel-oil calorific values, so the figures check out | Omri's Excel model, MRV reference values (Israel's official Monitoring, Reporting & Verification fuel factors) |
| **Fuel input** | ~0.10-0.11 tons fuel per MWh of thermal output (diesel and mazut land in the same range) | Derived: fuel tons/MWh-output = (1 ÷ combustion efficiency) × caloric ratio. At 82% efficiency: diesel = (1÷0.82)×0.085 ≈ 0.104 tons/MWh; mazut = (1÷0.82)×0.088 ≈ 0.107 tons/MWh. At 85% efficiency both drop slightly (~0.100-0.104). Scales linearly with capacity — same ratio applies at both points | Derived from the two sourced figures above |

### 1c. Standard-efficiency heat pump (new baseline, 2026-08-05)

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity points** | 40 kW / 70 kW (thermal) | Matched to 1a so both blocks compare the same capacity, efficient vs. standard | Matched to 1a |
| **Minimum COP (heating), both capacity points** | 3.3 at 47°F | Real code-minimum requirement for air-cooled unitary heat pumps, size category ≥135,000 and <240,000 Btu/h -- both 40kW (136,486 Btu/h) and 70kW (238,850 Btu/h) fall in this one bracket, so the same minimum applies at both points | [DOE FEMP Minimum Efficiency Requirements Tables](https://www.energy.gov/femp/articles/minimum-efficiency-requirements-tables-heating-and-cooling-product-categories) (mirrors ASHRAE 90.1-2019 Table 6.8.1-2) |
| **CapEx** | Not cleanly sourced -- flagged, not estimated with false precision | No commercial-scale efficiency-premium percentage found (residential DOE FEMP data gives a dollar premium, ~$728, that doesn't convert cleanly to our capacity/currency; general HVAC commentary suggests efficiency premiums in the 15-30% range across equipment types generally, the same ballpark as the chiller's 17.5%, but this is an extrapolation from a different technology, not a heat-pump-specific source). If a similar ~15-25% premium applied, that would put standard-tier CapEx around 840-915 ILS/kW (efficient CapEx of 1,050 ILS/kW divided by 1.15-1.25) -- stated as an illustrative range only, not a number to use in the model without a better source or Rafi's input | No direct source found this pass |

**Real tension worth flagging to Daniel/Rafi directly:** the sourced "efficient" 70kW unit (1a, COP 3.23-3.24) is at or slightly below this new code-minimum baseline (3.3) for the same capacity bracket. If both numbers are taken at face value, the 70kW block's "efficient" choice isn't actually more efficient than baseline -- which would break the B-vs-C comparison for that block (no incentive effect to measure if efficient doesn't beat baseline). Possible explanations, not yet resolved: the Sprsun spec sheet may be rated at different test conditions than AHRI's standard 47&deg;F point (colder ambient or higher water temp would lower COP relative to the standard rating, making this not a true apples-to-apples read), or the currently-sourced "efficient" product simply isn't a strong enough example for the 70kW point and a better one should be sourced. Needs resolving before this baseline change is usable in the live model -- flagged as the top open item from today's heat pump work.

**Annual operating hours (shared assumption, applies to 1a and 1c):** 3,000-4,000 (NOT locked — pending engineer consult). No hard source found — reasoned estimate (hot water demand runs most of the year, less weather-dependent than cooling, but not 24/7 continuous like process steam). Unlike chillers, deliberately left open rather than set to a working placeholder — Omri is consulting the EcoTraders engineer directly on this one before locking a number. Blocks the annual fuel-consumption (tons/year) calc until resolved. This is a building-usage characteristic, not tech-dependent, so one number applies to both the heat pump and its boiler baseline.

### Efficiency comparison (point-of-use vs. well-to-heat)

COP and combustion efficiency aren't directly comparable as raw numbers — different units. Converting to a common basis, using the real capacity-matched COP range (3.23-4.13) rather than the old flat band:

| Basis | Heat pump | Mazut/diesel boiler | Read |
|---|---|---|---|
| **Point-of-use** (energy actually consumed at the site) | COP 3.23-4.13 = 323-413% | 82-85% | Heat pump ~4-5x more efficient per unit of energy it consumes |
| **Well-to-heat** (accounts for the ~50% loss generating grid electricity from fuel, per Rafi's factor used in the electric steam section) | 50% × 3.23-4.13 = 162-207% | 82-85% (no grid step — fuel is burned on-site) | Heat pump still ~2x more efficient, even after the same primary-energy correction that hurt electric steam's case |

Point-of-use is what actually drives OPEX ₪ savings (the site pays its own electricity/fuel bill, not the grid's generation losses) — well-to-heat is the more honest efficiency/policy-impact story. Both numbers should probably appear in the model documentation, same reasoning as the electric steam section.

**Important — efficiency ratio alone doesn't give ₪ cost savings.** Fuel and electricity are priced differently per unit of energy, so a 4-5x efficiency gain does not translate to a 4-5x cost reduction. The actual OPEX comparison needs:
- Baseline annual fuel cost = fuel tons/year (from the Fuel input row in 1b × annual output) × ₪/ton fuel price
- Efficient annual electricity cost = electrical kWh/year (from the Power row in 1a × annual hours) × ₪/kWh electricity price
- **Still missing:** ₪/ton price for diesel and mazut. Electricity price is a shared model assumption already flagged by Daniel (תעו"ז time-band average, not heat-pump-specific) — see `next-steps.md`.

---

## 2. צ'ילרים (Chillers – Building Air Conditioning)

**Efficiency metric used:** kW/ton at full load, contextualized against AHRI Standard 550/590 IPLV (Integrated Part Load Value — the actual industry standard rating, which weights performance at 100/75/50/25% load rather than full-load kW/ton alone).

**Baseline vs. efficient split:** Original draft only had one "efficient" range per capacity point (driven by compressor class), with no explicit conventional/baseline comparison. Revised to a real baseline-vs-incented split so the model can compute savings directly.

**CapEx exception for chillers (2026-07-12):** CapEx is out of scope for the rest of this file (Omri's grant-program-rounds extraction covers it directly), but chillers are the strongest-represented technology in that extraction — 96 line items across the 2017-2022 rounds, vs. 49 for heat pumps, 5 for VSD, 1 for the boiler category. Real chiller CapEx is included below as a deliberate exception.

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 100 RT (~352 kW cooling) | Popular small-to-mid commercial chiller size | [Chiller efficiency overview](https://aircondlounge.com/chiller-efficiency-calculation-kw-ton-cop-eer-iplv-nplv/) |
| **Capacity point 2 (high)** | 500 RT (~1,758 kW cooling) | Popular large commercial/light-industrial chiller size | Same source |
| **Baseline efficiency — 100 RT** | 0.95 kW/ton (avg of 0.70-1.20) | Older/lower-tier reciprocating compressor class at this size — the conventional equipment being displaced | [Chiller kW/ton by compressor type](https://aircondlounge.com/chiller-efficiency-calculation-kw-ton-cop-eer-iplv-nplv/) — weakest-sourced bracket in this table, general market range, not a pinned code-minimum table value |
| **Efficient efficiency — 100 RT** | 0.80 kW/ton (avg of 0.70-0.90) | Screw/scroll compressor class, incented tier | Same source |
| **Baseline efficiency — 500 RT** | 0.60 kW/ton (avg of 0.56-0.63) | ASHRAE 90.1 Table 6.8.1-3 code-minimum for a ~500-600 ton water-cooled centrifugal chiller (Path A, 2013 edition, effective 2015) — this is an actual code-baseline table value, well sourced | [ASHRAE 90.1 Table 6.8.1-3 reference](https://up.codes/s/minimum-efficiency-requirement-listed-equipment-standard-rating-and-operating-co) |
| **Efficient efficiency — 500 RT** | 0.48 kW/ton (avg of 0.45-0.50) | FEMP-designated efficient level for a 500-ton water-cooled centrifugal chiller (0.541 kW/ton) confirms this tier beats code minimum; used as the incented reference point | [DOE FEMP water-cooled electric chillers](https://www.energy.gov/femp/purchasing-energy-efficient-water-cooled-electric-chillers) |
| **Annual operating hours** | 3,000 (locked working number) | Working number for the first-pass model, per Omri: above the ~2,080-8,760 range given by an EcoTraders engineer (verbal consult), and above the 1,800 hr US/EU energy-audit default sourced earlier. Treated as a first-pass point estimate, to be run as a sensitivity range later rather than refined to a single "correct" number now | Working assumption — not independently sourced at 3,000 specifically; supersedes the earlier 1,800-2,500 estimate |
| **Power** | Baseline: ~95 kW (100 RT) / ~300 kW (500 RT). Efficient: ~80 kW (100 RT) / ~240 kW (500 RT) | Derived from capacity × kW/ton for each baseline/efficient pair | Derived |
| **CapEx — efficient (real grant program data)** | **₪4,186/ton (median)** — 100 RT ≈ ₪418,600 — 500 RT ≈ ₪2,093,000 | From `capex_all_rounds_annotated.xlsx`, sheet "עלות לטון קירור": 96 chiller line items across the 2017-2022 grant rounds, 27 of which had usable capacity data in the text (the rest were excluded — no ton figure in the project description). Median used over mean (₪4,440/ton) because several rows are flagged as unusually low/high outliers; the source sheet itself recommends the median for the model. Both 100 RT and 500 RT are directly represented in the real data (e.g. 2×100RT units at ₪3,000/ton; 500RT units ranging ₪1,875-4,800/ton depending on features like heat recovery) — no clean capacity-based pricing trend emerged (huge scatter even at fixed capacity), so one blended ₪/ton figure is applied across both points rather than inventing a false split | Omri's grant-program CapEx extraction, `capex_all_rounds_annotated.xlsx` |
| **CapEx — baseline (estimated via efficiency premium)** | **₪3,562/ton (working estimate)** — 100 RT ≈ ₪356,200 — 500 RT ≈ ₪1,781,000 | Grant data has no baseline/conventional chiller cost by definition (it only covers what the program funded — the efficient tier). Estimated instead by dividing the real efficient CapEx (₪4,186/ton) back out through a sourced efficiency cost premium: DOE FEMP publishes a real cost-effectiveness data point — a 175-ton air-cooled chiller's efficient tier could cost up to $74,491 more than the standard tier and still be cost-effective (~$426/ton, though this is a "should not exceed" ceiling, not necessarily the actual market premium); separately, general market commentary across several HVAC cost-guide sources puts premium-efficiency chillers at roughly 10-25% more than standard efficiency for the same capacity (one weaker source cited up to 50%, treated as an outlier, not used). Took the midpoint of the 10-25% range (~17.5%) and divided it out: ₪4,186 ÷ 1.175 ≈ ₪3,562/ton. Range if a spread is wanted instead: ₪3,349/ton (25% premium) to ₪3,805/ton (10% premium) | [DOE FEMP purchasing energy-efficient electric chillers](https://www.energy.gov/cmei/femp/purchasing-energy-efficient-electric-chillers) (cost-effectiveness ceiling data point); general market efficiency-premium commentary (multiple HVAC cost-guide sources, 10-25% range) — derived estimate, not a directly-sourced baseline price |

---

## 3. מדחסי VSD (VSD Compressors)

**Efficiency metric used:** Specific power in kW/100 cfm at full load and rated pressure, tested to ISO 1217 and published on CAGI data sheets — this is the actual industry-standard metric (not a generic "% savings" figure, which conflates equipment efficiency with load-profile assumptions).

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 45 kW (60 HP) | Common small-to-mid industrial compressor size | [VSD compressor sizing examples](https://jhfoster.com/automation-blogs/what-is-a-variable-speed-drive-compressor/) |
| **Capacity point 2 (high)** | 150 kW (200 HP) | Common larger industrial compressor size | [200 HP example](https://www.idahopower.com/energy-environment/ways-to-save/savings-for-your-business/new-construction-major-renovations/air-compressor-variable-frequency-drive-vfd/) |
| **Specific power — fixed-speed baseline** | 20-23 kW/100 cfm at 100 psi | Older or lower-quality fixed-speed units; this is the baseline being replaced | [CAGI-based specific power ranges](https://aircompressorzone.com/blogs/resources/air-compressor-efficiency) |
| **Specific power — VSD (incented)** | 15-18 kW/100 cfm at 100 psi | Well-designed VSD rotary screw units at full load — this is a technology comparison (fixed-speed vs. VSD), held constant across the capacity range, not a size-dependent figure | Same source; [CAGI performance verification program](https://www.cagi.org/performance-verification/) (ISO 1217 test basis) |
| **Annual operating hours** | 6,000-6,800 (2-shift) | 6,800 hrs/yr is a cited real example for 2-shift industrial operation; continuous (3-shift/24-7) plants can reach ~8,000+. Range reflects shift-pattern uncertainty, not capacity | [Air compressor energy cost calculator](https://www.industrialairpower.com/blog/air-compressor-energy-calculator-calculate-your-true-operating-costs/) |
| **Power** | 45 kW / 150 kW | Same as capacity — compressor motor nameplate rating is the natural "power" figure here | Same as capacity sources |

**Important note on specific power vs. pressure:** specific power figures are only comparable at the same discharge pressure — a unit rated 17 kW/100cfm at 100 psi will read higher at 125 psi. The model should fix a reference pressure (e.g. 100 psi / 7 bar, standard in these sources) when using these numbers.

---

## 4. מערכות קיטור חשמליות (Electric Steam Systems – Conversion from Fuel Oil)

**Efficiency metric used:** Fuel-to-steam efficiency per ASME PTC 4 (input/output method) for the fuel-oil baseline; point-of-use conversion efficiency for the electric replacement (electric boilers have no combustion/flue losses, so the comparison is somewhat apples-to-oranges — flagged below).

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 200 kW | Lower end of mid-size industrial conversion projects | Placeholder pending real data (see flag below) |
| **Capacity point 2 (high)** | 3,000 kW (3 MW) | Electric resistance boilers are typically capped under 5 MW; this sits comfortably inside that band for a "large industrial" reference point | [Power-to-heat and electric boiler review (arXiv)](https://arxiv.org/pdf/2107.03960) |
| **Efficiency — fuel-oil baseline** | 82-85% | Standard fire-tube/water-tube boilers without heat recovery run 80-88% fuel-to-steam efficiency under ASME PTC 4; oil-fired units sit in the same band as gas absent a condensing economizer | [ASME PTC 4 (official standard)](https://www.asme.org/codes-standards/find-codes-standards/fired-steam-generators); [fuel-to-steam efficiency explainer](https://miuraboiler.com/what-is-fuel-to-steam-efficiency-for-boilers/); [industrial steam boiler efficiency ranges](https://coalbiomassboiler.com/industrial-steam-boiler-efficiency/) |
| **Efficiency — electric (incented)** | 95-99% (used 98% as representative) | Electric resistance/electrode boilers convert electricity to heat with no flue-gas loss; this is a genuinely different efficiency concept (near-total electrical-to-thermal conversion) rather than a "better combustion" story, which matters when explaining the comparison to Daniel | [Power-to-heat review (arXiv)](https://arxiv.org/pdf/2107.03960); [electric vs. gas boiler comparison](https://epcbsteamboiler.com/ultimate-comparison-of-electric-steam-boiler-vs-gas-steam-boiler/) |
| **Annual operating hours** | 6,000-8,000 | Cited range for continuous-process industries (food processing, chemicals); many industrial boilers run near-continuously between scheduled shutdowns | [Industrial boiler continuous operation](https://coalbiomassboiler.com/industrial-steam-boilers-continuous-operation/); [boiler ROI/hours reference](https://coalbiomassboiler.com/industrial-steam-boiler-costs-and-roi/) |
| **Power** | 200 kW / 3,000 kW | Same as capacity | Same as capacity |

---

## Open Flags for Rafi / Daniel (unresolved even after sourcing)

1. **Heat pump hours (3,000-4,000)** — genuinely unsourced, reasoned estimate only. Highest priority to replace with real data.
2. **Chiller hours (3,000, locked working number)** — not independently sourced at this value; set by Omri above both the 1,800 hr US/EU default and inside the low end of a 2,080-8,760 range given verbally by an EcoTraders engineer. Flagged for a sensitivity analysis pass later rather than further refinement now.
3. **Chiller 100 RT baseline (0.95 kW/ton)** — general reciprocating-compressor market range, not a pinned ASHRAE 90.1 code-minimum table value like the 500 RT bracket has. Weaker of the two chiller capacity points.
4. **Electric steam capacity range (200 kW-3 MW)** — placeholder, not tied to any Israeli project data. Should be replaced with real numbers from `capex_lineitems.csv` (הסבה category) once that CSV is reviewed — this program's own installations are a better source than international averages for this one specifically.
5. **Electric vs. fuel-oil efficiency comparison** — comparing combustion efficiency (fuel-oil, with flue losses) to conversion efficiency (electric, no flue losses) is standard practice in this literature but is a different kind of number under the hood. Worth a sentence in the model documentation so it isn't read as "electric boilers are just better-engineered."
6. **VSD reference pressure** — specific power numbers (15-18 vs 20-23 kW/100cfm) assume ~100 psi / 7 bar. Confirm the model's assumed system pressure matches, or the comparison isn't valid.
7. **`generate_tax_model.py` baseline name outdated** — still hardcodes heat pump baseline as `"דוד חשמל קונבנציונלי"` (electric resistance); needs updating to a mazut/diesel oven/boiler baseline to match the corrected comparison type. Work-computer task.
8. **Heat pump vs. fuel baseline comparison type** — same electric-vs-combustion caveat as electric steam (#5 above): COP (electric) and combustion efficiency (fuel) aren't the same kind of number, worth a documentation sentence so it doesn't read as a straight efficiency comparison.
9. **Chiller baseline CapEx (₪3,562/ton) is a derived estimate, not a directly-sourced price** — the real grant-program data only covers the efficient/incented tier, so this was backed out from the real efficient figure via a sourced 10-25% efficiency cost premium (DOE FEMP + general market commentary), using the midpoint. Genuinely an estimate, not a quote — flag for Daniel/Rafi if a firmer number is needed.
10. **Chiller CapEx median (₪4,186/ton) is a blended figure across the full 35-500 ton range** — the underlying data showed no clean capacity-based pricing trend (huge scatter even at fixed capacity, e.g. ₪1,875-4,800/ton at 500 RT alone), so this single figure is applied at both 100 RT and 500 RT rather than a false split. Only 27 of 96 chiller line items had usable capacity data.

**CapEx is out of scope for this file for the other 3 technologies (2026-07-12)** — Omri has CapEx extracted from the grant program rounds and uses that directly for heat pumps, VSD, and electric steam. Chillers are the one exception (see the CapEx rows above), since that technology has by far the strongest real data in the extraction (96 line items vs. 49/5/1 for the others).

## Next Steps (per Daniel's process)

1. ~~Gather average data points from open sources~~ — done, this file (efficiency, capacity, hours, fuel data — not CapEx, see above)
2. Review with Daniel — confirm the technology-specific metrics (IPLV/kW-ton, CAGI specific power, ASME PTC4, EN 14511) are what the model should standardize on
3. Talk with Rafi for verification — especially the flags above
