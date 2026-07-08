# Baseline Technology Data Points (Open-Source Reference)

**Status:** Draft for Daniel's review (step 1 of Daniel's process: gather → review with Daniel → verify with Rafi)
**Date:** 2026-07-06
**Purpose:** First-pass baseline reference points for the tax incentive model, per technology. All figures are international open-source averages — not yet validated against actual Israeli grant-fund installations or Rafi's engineering judgment.

Each technology below uses its own industry-standard efficiency metric (not a blanket COP), and every data point carries a source link. Where a value differs across the two capacity points, or is given as a range, the reasoning is stated explicitly — capacity and efficiency are kept as separate, independent axes unless there's a real documented reason to link them.

---

## 1. משאבות חום (Heat Pumps – Water Heating)

**Baseline correction (2026-07-08):** Originally assumed the baseline was a conventional electric resistance water heater (COP 1.0) — this matched what was hardcoded in `generate_tax_model.py` (`name_baseline: "דוד חשמל קונבנציונלי"`). Omri checked his notes and confirmed Rafi specifically flagged **mazut or diesel-fired ovens/boilers** as what's actually being replaced. This changes the comparison from electric-vs-electric to fuel-combustion-vs-electric — the same structural comparison as the electric steam section (#4) below, not a simple COP-vs-COP ratio. `generate_tax_model.py`'s baseline name still needs updating to match on the work computer (separate task).

**Efficiency metric used:** COP under EN 14511 at A7/W55 for the heat pump (efficient) side; fuel-to-heat combustion efficiency (ASME PTC 4 basis) for the mazut/diesel baseline side — same metric already sourced for the electric steam section, since ovens/boilers in this size class are the same equipment type.

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 40 kW (thermal) | Small commercial packaged heat pump units cluster here; baseline boiler is sized to the same thermal output | [Sprsun 37-45kW commercial unit](https://sprsunheatpump.com/37KW-45KW-Commercial-Air-Source-Heat-Pump-for-Water-Heater-and-Room-Heating-pd6657665.html) |
| **Capacity point 2 (high)** | 150 kW (thermal) | Common single-unit ceiling; bigger loads usually cascade multiple units rather than one larger one | [Sprsun 42-70kW unit](https://sprsunheatpump.com/42-70KW-Commercial-Air-to-Water-Heat-Pump-Space-Heating-Cooling-System-pd6187665.html); cascading noted for [A.O. Smith CAHP-120](https://www.hotwater.com/products/CAHP-120-SG100.html) |
| **Efficient efficiency (COP, A7/W55)** | 3.5–4.0, flat across capacity | Units in this band mostly use the same (scroll) compressor class, so COP doesn't scale meaningfully with size in this range; more sensitive to test temperature (W35 vs W55) than unit size. 3.9-4.3 figures reported are at the milder W35 point; true water-heating (W55) number expected lower, within 3.5-4.0 | [A.O. Smith CAHP-120 spec](https://www.hotwater.com/products/CAHP-120-SG100.html); [EHPA test regulation for A/W heat pumps](https://www.ehpa.org/wp-content/uploads/2022/07/EHPA_TestReg_AW_HP_V2.4a_20210607_.pdf); [COP vs test-point explainer](https://www.goodheatglobal.com/Air-to-Water-Heat-Pump-COP-Ratings-Explained-id47881106.html) |
| **Baseline efficiency (mazut/diesel oven, fuel-to-heat)** | 82-85% | Reused from the electric steam section's sourcing — standard fire-tube/water-tube fuel-oil-fired units without heat recovery run 80-88% under ASME PTC 4; same equipment class whether producing steam or hot water | [ASME PTC 4](https://www.asme.org/codes-standards/find-codes-standards/fired-steam-generators); [fuel-to-steam efficiency explainer](https://miuraboiler.com/what-is-fuel-to-steam-efficiency-for-boilers/) |
| **Fuel caloric value (energy content)** | Diesel (סולר): 0.085 ton/MWh — Mazut (מזוט): 0.088 ton/MWh | Real MRV-sourced figures from Omri's own Excel model, not open-source. Converts fuel input energy (MWh) to fuel mass (tons) for baseline OPEX (fuel cost = tons × ₪/ton). Inverse gives energy density: ~11.76 MWh/ton diesel, ~11.36 MWh/ton mazut — consistent with published diesel/heavy-fuel-oil calorific values, so the figures check out | Omri's Excel model, MRV reference values (Israel's official Monitoring, Reporting & Verification fuel factors) |
| **Annual operating hours** | 3,000–4,000 | **No hard source found** — reasoned estimate (hot water demand runs most of the year, less weather-dependent than cooling, but not 24/7 continuous like process steam). Still the weakest number in this file — needs Rafi/real usage data | — (unsourced estimate, flagged) |
| **Power (electrical input, heat pump side)** | ~10-11 kW at 40kW capacity / ~38-43 kW at 150kW capacity | Derived: electrical input = thermal capacity ÷ COP (using COP 3.5-3.9) | Derived, not an independent source |
| **Fuel input (baseline side)** | ~0.10-0.11 tons fuel per MWh of thermal output (diesel and mazut land in the same range) | Derived: fuel tons/MWh-output = (1 ÷ combustion efficiency) × caloric ratio. At 82% efficiency: diesel = (1÷0.82)×0.085 ≈ 0.104 tons/MWh; mazut = (1÷0.82)×0.088 ≈ 0.107 tons/MWh. At 85% efficiency both drop slightly (~0.100-0.104). Scales linearly with capacity — same ratio applies at 40kW and 150kW | Derived from the two sourced figures above |

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

## Next Steps (per Daniel's process)

1. ~~Gather average data points from open sources~~ — done, this file
2. Review with Daniel — confirm the technology-specific metrics (IPLV/kW-ton, CAGI specific power, ASME PTC4, EN 14511) are what the model should standardize on
3. Talk with Rafi for verification — especially the 5 flags above
