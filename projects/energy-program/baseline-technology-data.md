# Baseline Technology Data Points (Open-Source Reference)

**Status:** Draft for Daniel's review (step 1 of Daniel's process: gather → review with Daniel → verify with Rafi)
**Date:** 2026-07-06
**Purpose:** First-pass baseline reference points for the tax incentive model, per technology. All figures are international open-source averages — not yet validated against actual Israeli grant-fund installations or Rafi's engineering judgment.

**CapEx sourcing correction (2026-07-12):** CapEx (baseline + efficient, all 4 technologies) is sourced from open data below, same as everything else in this file — not pulled from the grant fund's own CapEx data. This corrects Daniel's original 2026-06-01 feedback ("find it in the fund data, don't estimate"); Omri clarified the fund data isn't broad enough and is hard to translate across all the data points the model needs, which is in fact why this whole open-source gathering effort started. See `decisions/log.md`.

Each technology below uses its own industry-standard efficiency metric (not a blanket COP), and every data point carries a source link. Where a value differs across the two capacity points, or is given as a range, the reasoning is stated explicitly — capacity and efficiency are kept as separate, independent axes unless there's a real documented reason to link them.

---

## 1. משאבות חום (Heat Pumps – Water Heating)

**Baseline correction (2026-07-08):** Originally assumed the baseline was a conventional electric resistance water heater (COP 1.0) — this matched what was hardcoded in `generate_tax_model.py` (`name_baseline: "דוד חשמל קונבנציונלי"`). Omri checked his notes and confirmed Rafi specifically flagged **mazut or diesel-fired ovens/boilers** as what's actually being replaced. This changes the comparison from electric-vs-electric to fuel-combustion-vs-electric — the same structural comparison as the electric steam section (#4) below, not a simple COP-vs-COP ratio. `generate_tax_model.py`'s baseline name still needs updating to match on the work computer (separate task).

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
| **CapEx — efficient (heat pump)** | **NOT FOUND** | Web search turned up only "contact for quote" B2B listings (Alibaba, Made-in-China) with no visible pricing at either capacity point. The only real number found was a generic European €250-2,000/kW installed rule of thumb, which is residential-skewed and too wide to use as-is | Open flag — needs a distributor quote, a spec-sheet PDF with list price, or acceptance of the wide European range as a placeholder |

### 1b. Mazut/diesel oven (baseline technology)

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity points** | 40 kW / 70 kW (thermal) | Sized to match the heat pump's real capacity points above, not independently sourced | Matched to 1a |
| **Baseline efficiency (fuel-to-heat)** | 82-85% | Reused from the electric steam section's sourcing — standard fire-tube/water-tube fuel-oil-fired units without heat recovery run 80-88% under ASME PTC 4; same equipment class whether producing steam or hot water | [ASME PTC 4](https://www.asme.org/codes-standards/find-codes-standards/fired-steam-generators); [fuel-to-steam efficiency explainer](https://miuraboiler.com/what-is-fuel-to-steam-efficiency-for-boilers/) |
| **Fuel caloric value (energy content)** | Diesel (סולר): 0.085 ton/MWh — Mazut (מזוט): 0.088 ton/MWh | Real MRV-sourced figures from Omri's own Excel model, not open-source. Converts fuel input energy (MWh) to fuel mass (tons) for baseline OPEX (fuel cost = tons × ₪/ton). Inverse gives energy density: ~11.76 MWh/ton diesel, ~11.36 MWh/ton mazut — consistent with published diesel/heavy-fuel-oil calorific values, so the figures check out | Omri's Excel model, MRV reference values (Israel's official Monitoring, Reporting & Verification fuel factors) |
| **Fuel input** | ~0.10-0.11 tons fuel per MWh of thermal output (diesel and mazut land in the same range) | Derived: fuel tons/MWh-output = (1 ÷ combustion efficiency) × caloric ratio. At 82% efficiency: diesel = (1÷0.82)×0.085 ≈ 0.104 tons/MWh; mazut = (1÷0.82)×0.088 ≈ 0.107 tons/MWh. At 85% efficiency both drop slightly (~0.100-0.104). Scales linearly with capacity — same ratio applies at both points | Derived from the two sourced figures above |
| **CapEx — baseline (mazut/diesel oven)** | **NOT FOUND** | Search results were either small residential single units or large multi-MW industrial boilers, nothing at this specific 40-70kW commercial scale | Open flag — same problem as 1a's CapEx gap |

**Annual operating hours (shared assumption, applies to both 1a and 1b):** 3,000-4,000 (NOT locked — pending engineer consult). No hard source found — reasoned estimate (hot water demand runs most of the year, less weather-dependent than cooling, but not 24/7 continuous like process steam). Unlike chillers, deliberately left open rather than set to a working placeholder — Omri is consulting the EcoTraders engineer directly on this one before locking a number. Blocks the annual fuel-consumption (tons/year) calc until resolved. This is a building-usage characteristic, not tech-dependent, so one number applies to both the heat pump and its boiler baseline.

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
| **CapEx — 100 RT (baseline vs. efficient, undifferentiated)** | $130,000-210,000 installed (~$1,300-2,100/ton) | Multiple sources agree on this range, but none split it into baseline-vs-efficient at 100 RT specifically — treat as a rough all-in figure for now, not a clean baseline/efficient pair | [ChillerOne 100-ton chiller cost](https://chillerone.com/100-ton-chiller-cost/); [Chiller cost per ton guide](https://www.pickcomfort.com/chilled-water-cost-per-ton-typical-price-ranges-what-drives/) |
| **CapEx — 500 RT** | **Inconsistent — flagged, not usable as-is** | Sources split 6-9x: one gives $180K equipment + ~$70K install/permits (~$250-270K total, "mid-efficiency, integrated controls") vs. another quoting $1.6M-2.4M for "high-efficiency with energy recovery and advanced controls." The gap is almost certainly scope (bare unit vs. a full chiller-plant project with recovery systems bundled in), not a real baseline-vs-efficient spread. Needs a tighter source or Rafi's judgment on which scope matches what the grant fund actually installs | Conflicting sources — see reasoning |

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
| **CapEx — fixed-speed baseline** | 45kW (60 HP): $18,150-19,800 — 150kW (200 HP): $65,999.99 | Strongest-sourced CapEx numbers in this file — real listed prices from the same vendor (US Air Compressor) at both capacity points, not a generic range | [60 HP fixed-speed](https://usaircompressor.com/product/60-hp-fixed-speed-air-compressor/); [200 HP fixed-speed](https://usaircompressor.com/product/200-hp-fixed-speed-air-compressor/) |
| **CapEx — VSD (incented)** | Not directly listed — estimate 15-30% premium over fixed-speed (≈$21,000-25,700 at 45kW, ≈$76,000-85,800 at 150kW) | Same vendor sells both fixed-speed and VSD versions of these frame sizes but didn't surface an exact VSD price in search; 15-30% is a commonly-cited industry premium for VSD over fixed-speed at the same frame, not vendor-confirmed for this specific listing | Estimated from a sourced baseline + an industry rule of thumb — flagged, not a hard number |

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
| **CapEx — electric (incented)** | General industrial range $30K-500K+ depending on capacity/pressure; one closer data point (10 TPH oil-fired, larger than our 3MW point) landed ~$680K fully installed | Not capacity-matched cleanly to the 200kW/3MW points used here — same issue as the capacity range itself (flag #4 below), this program's own installations from `capex_lineitems.csv` would be a better source | [Industrial electric boiler price guide](https://www.makeboiler.com/industrial-electric-boiler-price-guide/); [Industrial steam boiler cost guide](https://coalbiomassboiler.com/industrial-steam-boiler-cost/) |
| **CapEx — fuel-oil baseline** | **NOT FOUND** — not separately searched this pass | Ran out of search budget before reaching this one; the general boiler cost ranges above are mixed fuel-type and don't isolate an oil-fired baseline figure | Open flag |

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
9. **Heat pump CapEx (both baseline and efficient) — not found.** Web search only turned up "contact for quote" listings, no visible pricing at 40kW/70kW for either the heat pump or the mazut/diesel oven baseline. Weakest CapEx gap in the file — needs a distributor quote or spec-sheet price, not just more general search.
10. **Chiller 500 RT CapEx — sources conflict 6-9x** ($250-270K vs. $1.6-2.4M), almost certainly a scope mismatch (bare equipment vs. full plant with energy recovery) rather than a real baseline-vs-efficient spread. Needs a tighter source or Rafi's call on which scope matches actual grant-fund installations.
11. **VSD CapEx premium (15-30%) is an industry rule of thumb, not vendor-confirmed** — the fixed-speed baseline prices are real listed prices from the same vendor, but the VSD price wasn't directly found; the premium applied to get an estimate is a general industry figure.
12. **Electric steam CapEx not capacity-matched** — general industrial boiler cost ranges found aren't isolated to the 200kW/3MW points or to oil-fired specifically; fuel-oil baseline CapEx wasn't searched yet this pass.

## Next Steps (per Daniel's process)

1. ~~Gather average data points from open sources~~ — done, this file
2. Review with Daniel — confirm the technology-specific metrics (IPLV/kW-ton, CAGI specific power, ASME PTC4, EN 14511) are what the model should standardize on
3. Talk with Rafi for verification — especially the 5 flags above
