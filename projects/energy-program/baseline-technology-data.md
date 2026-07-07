# Baseline Technology Data Points (Open-Source Reference)

**Status:** Draft for Daniel's review (step 1 of Daniel's process: gather → review with Daniel → verify with Rafi)
**Date:** 2026-07-06
**Purpose:** First-pass baseline reference points for the tax incentive model, per technology. All figures are international open-source averages — not yet validated against actual Israeli grant-fund installations or Rafi's engineering judgment.

Each technology below uses its own industry-standard efficiency metric (not a blanket COP), and every data point carries a source link. Where a value differs across the two capacity points, or is given as a range, the reasoning is stated explicitly — capacity and efficiency are kept as separate, independent axes unless there's a real documented reason to link them.

---

## 1. משאבות חום (Heat Pumps – Water Heating)

**Efficiency metric used:** COP under EN 14511 at A7/W55 (7°C air source, 55°C water outlet — the relevant test point for water heating, as opposed to A7/W35 which is for low-temp space/underfloor heating and reads notably higher for the same unit).

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 40 kW | Small commercial packaged units cluster in this range | [Sprsun 37-45kW commercial unit](https://sprsunheatpump.com/37KW-45KW-Commercial-Air-Source-Heat-Pump-for-Water-Heater-and-Room-Heating-pd6657665.html) |
| **Capacity point 2 (high)** | 150 kW | Common single-unit ceiling; bigger commercial/industrial loads (hotels, hospitals) are usually met by cascading multiple units of this size rather than one larger unit, so this is the practical top of the "single unit" interpolation range | [Sprsun 42-70kW unit](https://sprsunheatpump.com/42-70KW-Commercial-Air-to-Water-Heat-Pump-Space-Heating-Cooling-System-pd6187665.html); cascading noted for [A.O. Smith CAHP-120](https://www.hotwater.com/products/CAHP-120-SG100.html) |
| **Efficiency (COP, A7/W55)** | 3.5–4.0, single value not tied to capacity | Did not find evidence that COP scales meaningfully with size in the 40-150 kW commercial range — units in this band mostly use the same compressor class (scroll). COP is much more sensitive to test temperature (W35 vs W55) than to unit size, so I kept it flat rather than inventing a size-based split. 3.9-4.3 figures reported are at the milder W35/general-purpose point; expect the true water-heating (W55) number to sit lower within 3.5-4.0 | [A.O. Smith CAHP-120 spec (4.3 COP, mixed conditions)](https://www.hotwater.com/products/CAHP-120-SG100.html); [EHPA official test regulation for A/W heat pumps](https://www.ehpa.org/wp-content/uploads/2022/07/EHPA_TestReg_AW_HP_V2.4a_20210607_.pdf); [COP vs test-point explainer](https://www.goodheatglobal.com/Air-to-Water-Heat-Pump-COP-Ratings-Explained-id47881106.html) |
| **Annual operating hours** | 3,000–4,000 | **No hard source found** — this is a reasoned estimate (hot water demand runs most of the year, less weather-dependent than cooling, but not 24/7 continuous like process steam). Genuinely the weakest number in this file — needs Rafi/real usage data, not just open-source | — (unsourced estimate, flagged) |
| **Power (electrical input)** | ~10-11 kW at 40kW capacity / ~38-43 kW at 150kW capacity | Derived: electrical input = thermal capacity ÷ COP (using COP 3.5-3.9 range above) | Derived, not an independent source |

---

## 2. צ'ילרים (Chillers – Building Air Conditioning)

**Efficiency metric used:** kW/ton at full load, contextualized against AHRI Standard 550/590 IPLV (Integrated Part Load Value — the actual industry standard rating, which weights performance at 100/75/50/25% load rather than full-load kW/ton alone).

| Data point | Value | Reasoning | Source |
|---|---|---|---|
| **Capacity point 1 (low)** | 100 RT (~352 kW cooling) | Popular small-to-mid commercial chiller size | [Chiller efficiency overview](https://aircondlounge.com/chiller-efficiency-calculation-kw-ton-cop-eer-iplv-nplv/) |
| **Capacity point 2 (high)** | 500 RT (~1,758 kW cooling) | Popular large commercial/light-industrial chiller size | Same source |
| **Efficiency at low capacity** | 0.70-0.90 kW/ton | At ~100 RT, chillers are typically screw or scroll/reciprocating compressor machines (centrifugal compressors aren't economical at this scale), and that compressor class runs 0.60-1.20 kW/ton | [Chiller kW/ton by compressor type](https://aircondlounge.com/chiller-efficiency-calculation-kw-ton-cop-eer-iplv-nplv/) |
| **Efficiency at high capacity** | 0.45-0.70 kW/ton | At ~500 RT, centrifugal compressors become the standard choice and are inherently more efficient (0.45-0.70 kW/ton) — so the efficiency difference between the two capacity points is a real, documented consequence of which compressor technology is economical at each scale, not an arbitrary "old vs new" split | Same source; standard rating method is [AHRI 550/590 IPLV](https://www.ahrinet.org/search-standards/ahri-550590-i-p-and-551591-si-performance-rating-water-chilling-and-heat-pump-water-heating-packages) |
| **Annual operating hours** | 1,800 (commonly-cited default) up to ~2,500 | 1,800 hrs/yr is a standard US/European commercial-building energy-audit default. I raised the upper bound to 2,500 as a judgment call for Israel's longer cooling season — **this adjustment is NOT sourced**, it's my own reasoning, and is exactly the kind of number that needs Rafi/local validation before it goes in the model | [Energy-audit chiller hours reference](https://envigilance.com/blog/chiller-plant-optimization/) (1,800 hrs figure); Israel-climate adjustment unsourced |
| **Power** | ~70-90 kW (100 RT × 0.70-0.90) to ~790-1,230 kW (500 RT × 0.45-0.70) | Derived from capacity × kW/ton | Derived |

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
2. **Chiller hours upper bound (2,500)** — the 1,800 hr figure is sourced but is a US/European default; my extension to 2,500 for Israel's climate is my own unsourced judgment call.
3. **Electric steam capacity range (200 kW-3 MW)** — placeholder, not tied to any Israeli project data. Should be replaced with real numbers from `capex_lineitems.csv` (הסבה category) once that CSV is reviewed — this program's own installations are a better source than international averages for this one specifically.
4. **Electric vs. fuel-oil efficiency comparison** — comparing combustion efficiency (fuel-oil, with flue losses) to conversion efficiency (electric, no flue losses) is standard practice in this literature but is a different kind of number under the hood. Worth a sentence in the model documentation so it isn't read as "electric boilers are just better-engineered."
5. **VSD reference pressure** — specific power numbers (15-18 vs 20-23 kW/100cfm) assume ~100 psi / 7 bar. Confirm the model's assumed system pressure matches, or the comparison isn't valid.

## Next Steps (per Daniel's process)

1. ~~Gather average data points from open sources~~ — done, this file
2. Review with Daniel — confirm the technology-specific metrics (IPLV/kW-ton, CAGI specific power, ASME PTC4, EN 14511) are what the model should standardize on
3. Talk with Rafi for verification — especially the 5 flags above
