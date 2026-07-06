# Baseline Technology Data Points (Open-Source Reference)

**Status:** Draft for Daniel's review (step 1 of Daniel's process: gather → review with Daniel → verify with Rafi)
**Date:** 2026-07-06
**Purpose:** First-pass baseline reference points for the tax incentive model, per technology. All figures are international open-source averages (ASHRAE/AHRI/DOE-adjacent industry references) — not yet validated against actual Israeli grant-fund installations or Rafi's engineering judgment.

For each of the 4 model technologies: two capacity points on the popular spectrum (for linear interpolation), an efficiency indicator, typical annual operating hours, and a representative power point.

---

## 1. משאבות חום (Heat Pumps – Water Heating)

| Data point | Low | High | Source / basis |
|---|---|---|---|
| **Capacity (2 pts for interpolation)** | 40 kW | 150 kW | Popular range for single packaged commercial air-to-water heat pump units (small commercial units run 37-45 kW; mid/large commercial units 42-70 kW; bigger loads are typically met by cascading multiple units rather than one large unit, so 150 kW represents a common single-unit ceiling before cascading) |
| **Efficiency indicator** | COP 3.5 | COP 4.3 | Electrically-driven heat pump water heaters with conventional refrigerants (R410A etc.) typically run COP 3-5; commercial units documented at COP 3.9-4.3 |
| **Annual operating hours** | ~3,000 | ~4,000 | **Estimate, not sourced to a hard reference** — hot water demand in commercial/industrial settings (hotels, food processing, laundries) runs most of the year but not continuously like process steam. Flag for Rafi. |
| **Power** | ~10 kW (elec. input at 40kW capacity, COP 4) | ~37 kW (elec. input at 150kW capacity, COP 4) | Derived: electrical input = thermal capacity ÷ COP. Confirm with Rafi whether the model wants thermal output or electrical input as "Power." |

---

## 2. צ'ילרים (Chillers – Building Air Conditioning)

| Data point | Low | High | Source / basis |
|---|---|---|---|
| **Capacity (2 pts for interpolation)** | 100 RT (~352 kW cooling) | 500 RT (~1,758 kW cooling) | Common bracket for water-cooled screw/centrifugal chillers in commercial and light-industrial buildings (the grant category is אקלום מבנים, i.e. building-scale, not residential split units) |
| **Efficiency indicator** | 0.85 kW/ton (COP ~4.1, baseline/older) | 0.55 kW/ton (COP ~6.4, efficient upgrade) | Centrifugal chillers range 0.45-0.70 kW/ton, screw chillers 0.60-0.90 kW/ton; reciprocating/scroll 0.70-1.20 kW/ton. 0.85 represents an aging baseline unit, 0.55 a high-efficiency replacement |
| **Annual operating hours** | 1,800 | 2,500 | 1,800 hrs/yr is the standard energy-audit assumption for commercial building chillers; upper bound raised to 2,500 to account for Israel's longer cooling season vs. the (likely US/European) source data. **Flag for Rafi** — Israel-specific hours are the biggest open question here. |
| **Power** | ~85 kW (100 RT × 0.85 kW/ton) | ~967 kW (500 RT × ~0.55–1.2 depending on match) | Derived from capacity × kW/ton; pick matching efficiency pair when building the interpolation |

---

## 3. מדחסי VSD (VSD Compressors)

| Data point | Low | High | Source / basis |
|---|---|---|---|
| **Capacity (2 pts for interpolation)** | 45 kW (60 HP) | 150 kW (200 HP) | Common industrial compressed-air range cited across VSD retrofit case studies (45 kW, 75 kW, 100 HP, 200 HP examples) |
| **Efficiency indicator** | 20% energy savings vs. fixed-speed | 35% energy savings vs. fixed-speed | VSD compressors report 20-50% savings vs. fixed-speed depending on load variability; 20-35% is the commonly-cited working range (vs. up to 70% in best-case variable-demand applications) |
| **Annual operating hours** | 6,000 | 6,800 | 6,800 hrs/yr cited as a real example for 2-shift industrial operation; continuous (3-shift/24-7) plants can reach 8,000+. **Flag for Rafi** — need to know if grant applicants run 2-shift or continuous. |
| **Power** | 45 kW | 150 kW | Same as capacity — compressor motor nameplate power is the natural "power" data point here |

---

## 4. מערכות קיטור חשמליות (Electric Steam Systems – Conversion from Fuel Oil)

| Data point | Low | High | Source / basis |
|---|---|---|---|
| **Capacity (2 pts for interpolation)** | 200 kW | 3,000 kW (3 MW) | Electric resistance boilers are typically <5 MW; electrode boilers cover 3-70 MW. 200 kW-3 MW represents the popular range for mid-size industrial fuel-oil-to-electric conversions (matches the "הסבה לחשמל" grant category scale) — **should be cross-checked against the actual capex_lineitems.csv sizes once that data is reviewed**, since this is literally the category the CapEx pipeline extracts |
| **Efficiency indicator (thermal)** | 82% (fuel-oil baseline being replaced) | 98% (electric) | Fuel-to-steam efficiency for standard fire-tube/water-tube oil boilers runs 80-88%; electric boilers run 95-99.9% (point-of-use). 82%/98% is a reasonable baseline/upgrade pair |
| **Annual operating hours** | 6,000 | 8,000 | Cited range for continuous-process industries (food processing, chemicals); many industrial boilers run 24/7 between scheduled shutdowns |
| **Power** | 200 kW | 3,000 kW | Same as capacity |

---

## Open Flags for Rafi (engineering verification needed)

1. **Heat pump hours** — no solid open-source figure found; 3,000-4,000 hrs is an estimate based on demand pattern reasoning, not a citable reference.
2. **Chiller hours in Israel** — 1,800 hrs is a US/European commercial-building energy-audit default; Israel's longer cooling season likely pushes this higher. Needs local validation.
3. **Compressor shift pattern** — savings % and hours both depend heavily on whether grant applicants run 2-shift or continuous operations. May be worth a technology-specific hours assumption once real grant data is reviewed.
4. **Electric steam capacity range** — should be replaced with real numbers from `capex_lineitems.csv` (הסבה category) once that CSV is reviewed/cleaned, since this program's actual installations are the best source, not international averages.
5. **"Power" definition** — for heat pumps and chillers, need to confirm the model wants electrical input power (kW drawn) vs. thermal capacity (kW delivered) — they differ by the efficiency indicator (COP / kW-per-ton).

## Next Steps (per Daniel's process)

1. ~~Gather average data points from open sources~~ — done, this file
2. Review with Daniel — confirm the "popular spectrum" picks and efficiency indicator choices make sense for the model
3. Talk with Rafi for verification — especially the 5 flags above
