# HW Assignment #3 – LCA Exercise
## Option B: Single-Use Cup vs. Reusable Steel Cup at Karnaf Store

**By:** Omri Shamgar

---

## 1. Functional Unit

The functional unit is: **serving one hot drink per day over 20 consecutive days at the Karnaf store, Reichman University** (20 servings total).

This allows direct comparison between the two systems: 20 single-use paper cups with PS lids (Product A) vs. one reusable stainless steel cup with silicone lid, used 20 times (Product B).

---

## 2. System Boundaries Type

Both products are assessed using a **cradle-to-grave** system boundary, with the following stage coverage:

**Product A (Single-Use Cup):** Raw material production → transport to production site → manufacturing → disposal. Coffee production, filling, storing, and store operations are excluded.

**Product B (Reusable Steel Cup):** Raw material production → transport to production site → manufacturing → transport to Reichman University → use phase (20 washes). End-of-life is excluded per the assignment scope. Coffee production, store operations, and transport from store to user are also excluded.

The main structural difference between the two products is that Product A includes disposal (the cups are discarded after each use) while Product B excludes end-of-life (as specified in the assignment). This is noted as a limitation in comparing the two results on a fully equivalent basis.

---

## 3. System Boundary Diagram

### Product A – Single-Use Cup

```
[Raw Material Production]
       |
  Paper (Hedera)  -->  [Transport: lorry, ~38 km]  -->  [Cup Production Site, Natanya]
  LDPE (Haifa)    -->  [Transport: lorry, ~63 km]  -->        |
  PS (Haifa)      -->  [Transport: lorry, ~63 km]  -->        |
                                                         [Processes:]
                                                         - Cup forming (0.04 kWh/cup, IL grid)
                                                         - LDPE coating application
                                                              |
                                                         [Use: 20 cups × 1 drink/day]
                                                              |
                                                    [Disposal: municipal incineration]
                                                    (paper cup body + LDPE coating + PS lid)

EXCLUDED: coffee production, filling, store operations, transport Natanya → RU
```

### Product B – Reusable Steel Cup

```
[Raw Material Production]
       |
  Steel (Espoo, FI)   -->  [Transport: lorry, ~20 km]  -->  [Production Site, Helsinki]
  Silicone (Espoo, FI) -->  [Transport: lorry, ~20 km] -->        |
                                                            [Processes:]
                                                            - Cold impact extrusion (steel cup)
                                                            - Silicone lid shaping (0.4 kWh/kg, FI grid)
                                                            - Silicone wrapper shaping (0.4 kWh/kg, FI grid)
                                                                  |
                                               [Transport: container ship, Helsinki → Herzliya, ~7,500 km]
                                                                  |
                                                    [Use Phase: 20 washes]
                                                    - Water: 0.7 L/wash × 20 = 14 L
                                                    - Soap: 5 g/wash × 20 = 100 g

EXCLUDED: coffee production, store operations, transport store → user, end-of-life
```

---

## 4. Main Assumptions

1. **Transport distances:** Estimated using general geographic knowledge. Hedera to Natanya: ~38 km; Haifa to Natanya: ~63 km; Espoo to Helsinki: ~20 km; Helsinki to Herzliya by sea: ~7,500 km (via Baltic Sea, North Sea, English Channel, Strait of Gibraltar, Mediterranean). All land transport modeled as lorry (16t–32t, fleet average, {RER}).

2. **Geography proxy for lorry in Israel:** No Israel-specific lorry transport dataset exists in the BAFU database. The European average (RER) fleet average is used as a proxy. This is a standard assumption in LCA when the exact country is not available.

3. **Paper type:** Kraft paper, unbleached {RER} was selected as the closest proxy for the paper cup body material. No dedicated "paper cup" or foodservice board dataset was available in the BAFU 2025 database.

4. **Polystyrene:** General Purpose Polystyrene (GPPS) {RER} was selected for the injection-molded PS lid, as it is the standard grade used for rigid food packaging applications.

5. **Steel:** Chromium steel 18/8 {RER} (i.e., 304 stainless steel) was selected for the reusable cup body. This is the industry-standard grade for reusable drinkware.

6. **Finland electricity:** The production mix {FI} dataset was used (0.102 kgCO2eq/kWh), representing the national grid average. Finland's grid is predominantly nuclear and hydropower, which explains the low emission factor.

7. **Tap water:** The RER (European average) tap water dataset was used as no Israel-specific dataset exists. Israel relies heavily on desalinated water, which has higher energy intensity (~0.968 × 10⁻³ kgCO2eq/kg for desalinated water vs. 2.03 × 10⁻⁴ kgCO2eq/kg for RER). Given the small contribution of water to overall GWP, the difference is negligible.

8. **LDPE coating emission:** The coating process emission (0.002 kgCO2eq/cup) was provided directly in the assignment and applied as a direct emission, not linked to a BAFU dataset.

9. **Disposal (Product A):** All single-use cups and lids are assumed to be sent to municipal incineration, consistent with Israeli waste management practice for contaminated food-contact packaging (paper cups with plastic coating cannot be recycled via standard paper streams).

10. **No processing losses (Product A):** The assignment explicitly states no waste is generated in the production process for the single-use cup.

11. **Cold impact extrusion energy (Product B):** The BAFU "Deformation stroke, cold impact extrusion, steel {RER}" dataset was applied per kg of steel formed. This covers the forming energy only; the steel material itself is accounted for separately.

12. **Transport from Natanya to RU (Product A):** The assignment defines Product A's system as including transport to the production site only; transport from the production site (Natanya) to the Karnaf store is not listed among the included processes and is therefore excluded. For Product B, transport from Helsinki to RU is explicitly included in the assignment scope. The resulting asymmetry has negligible impact on the results: Natanya to Herzliya (~30 km) carrying 0.34 kg of cups would contribute approximately 0.002 kgCO2eq (0.2% of Product A total).

---

## 5. Total GWP Results

### Product A – Single-Use Cup (20 cups, 20 lids)

| Life Cycle Stage | GWP [kgCO2eq] | Contribution [%] |
|-----------------|----------------|-----------------|
| Raw materials | 0.510 | 42.6% |
| Transport (to production site) | 0.003 | 0.3% |
| Processing (cup forming + LDPE coating) | 0.358 | 29.9% |
| Disposal (incineration) | 0.327 | 27.3% |
| **TOTAL** | **1.197** | **100%** |

### Product B – Reusable Steel Cup (1 cup, 20 uses)

| Life Cycle Stage | GWP [kgCO2eq] | Contribution [%] |
|-----------------|----------------|-----------------|
| Raw materials | 0.775 | 79.6% |
| Transport (Espoo→Helsinki + Helsinki→Herzliya) | 0.024 | 2.4% |
| Processing (shaping + cold impact extrusion) | 0.007 | 0.7% |
| Use phase (20 washes: water + soap) | 0.169 | 17.3% |
| **TOTAL** | **0.974** | **100%** |

**Comparison:** The reusable steel cup has approximately 19% lower GWP than 20 single-use cups over the same 20-day period (0.974 vs. 1.197 kgCO2eq). The reusable cup's advantage increases with continued use, since its manufacturing emissions are fixed regardless of how many times it is used.

---

## 6. Largest GWP Contributor

**Product A:** The single largest contributor is **polystyrene (PS)**, accounting for 24.4% of total GWP through raw material production (0.292 kgCO2eq) and an additional 21.4% through disposal by incineration (0.256 kgCO2eq). Combined, the PS lid represents 45.8% of Product A's total GWP. Cup forming electricity is the next largest single line item at 26.5%, driven by Israel's relatively carbon-intensive grid (0.397 kgCO2eq/kWh).

**Product B:** Steel production dominates overwhelmingly at **68.1%** of total GWP (0.663 out of 0.974 kgCO2eq). This reflects the energy-intensive production of stainless steel. Soap consumption over 20 washes is the second contributor at 17.0%, which is notable relative to the small mass involved (100 g total).

---

## Appendix – Inventory Table

### Product A – Single-Use Cup

| Material, energy flow, or activity | Quantity | Unit | Dataset used from BAFU | Dataset geography | IPCC 2021 GWP factor [kgCO2eq/unit] | GWP value [kgCO2eq] | GWP contribution [%] | Notes/Assumptions |
|------------------------------------|----------|------|------------------------|-------------------|--------------------------------------|----------------------|----------------------|-------------------|
| Paper (cup body) | 0.240 | kg | Kraft paper, unbleached, at plant | {RER} | 7.11E-01 | 0.1707 | 14.3% | 20 cups × 0.0120 kg. No paper cup-specific dataset in BAFU; unbleached kraft used as proxy. |
| LDPE (coating) | 0.020 | kg | Polyethylene, LDPE, granulate, at plant | {RER} | 2.35E+00 | 0.0470 | 3.9% | 20 cups × 0.0010 kg. |
| Polystyrene (lid) | 0.080 | kg | Polystyrene, general purpose, GPPS, at plant | {RER} | 3.65E+00 | 0.2920 | 24.4% | 20 lids × 0.0040 kg. GPPS selected for rigid injection-molded lid. |
| Transport – Paper: Hedera→Natanya | 0.00912 | tkm | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 | 0.0020 | 0.2% | 0.240 kg × 0.038 km. RER used as proxy for Israel (no IL-specific dataset). |
| Transport – LDPE: Haifa→Natanya | 0.00126 | tkm | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 | 0.0003 | 0.0% | 0.020 kg × 0.063 km. |
| Transport – PS: Haifa→Natanya | 0.00504 | tkm | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 | 0.0011 | 0.1% | 0.080 kg × 0.063 km. |
| Cup forming (electricity, Israel) | 0.800 | kWh | — (given in assignment) | IL | 3.97E-01 | 0.3176 | 26.5% | 20 cups × 0.04 kWh. Israel grid emission factor given directly. |
| LDPE coating process | 20 | cups | — (given in assignment) | IL | 2.00E-03 per cup | 0.0400 | 3.3% | Direct process emission given in assignment. |
| Disposal – Paper | 0.240 | kg | Disposal, packaging paper, 13.7% water, to municipal incineration | {CH} | 4.33E-02 | 0.0104 | 0.9% | Paper cup body; coated paper cannot be recycled, sent to incineration. CH proxy for IL. |
| Disposal – LDPE | 0.020 | kg | Disposal, polyethylene, 0.4% water, to municipal incineration | {CH} | 3.03E+00 | 0.0606 | 5.1% | LDPE coating disposed with cup. CH proxy for IL. |
| Disposal – Polystyrene | 0.080 | kg | Disposal, polystyrene, 0.2% water, to municipal incineration | {CH} | 3.20E+00 | 0.2560 | 21.4% | 20 PS lids. CH proxy for IL. |
| **TOTAL** | | | | | | **1.197** | **100%** | |

---

### Product B – Reusable Steel Cup

| Material, energy flow, or activity | Quantity | Unit | Dataset used from BAFU | Dataset geography | IPCC 2021 GWP factor [kgCO2eq/unit] | GWP value [kgCO2eq] | GWP contribution [%] | Notes/Assumptions |
|------------------------------------|----------|------|------------------------|-------------------|--------------------------------------|----------------------|----------------------|-------------------|
| Steel (cup body) | 0.150 | kg | Chromium steel 18/8, at plant | {RER} | 4.42E+00 | 0.6630 | 68.1% | 304 stainless steel (18/8 chromium-nickel), standard grade for reusable drinkware. RER used; closest to Finnish production. |
| Silicone (lid) | 0.025 | kg | Silicone product, at plant | {RER} | 2.79E+00 | 0.0698 | 7.2% | |
| Silicone (heat-resistant wrapper) | 0.015 | kg | Silicone product, at plant | {RER} | 2.79E+00 | 0.0419 | 4.3% | |
| Transport – Espoo→Helsinki (lorry) | 0.00380 | tkm | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 | 0.0008 | 0.1% | 0.190 kg total × 0.020 km. |
| Transport – Helsinki→Herzliya (sea) | 1.4250 | tkm | Transport, transoceanic container ship | {OCE} | 1.60E-02 | 0.0228 | 2.3% | 0.190 kg × 7,500 km. Route via North Sea, English Channel, Mediterranean. |
| Silicone lid shaping (Finland electricity) | 0.0100 | kWh | Electricity, production mix | {FI} | 1.02E-01 | 0.0010 | 0.1% | 0.4 kWh/kg × 0.025 kg. |
| Silicone wrapper shaping (Finland electricity) | 0.0060 | kWh | Electricity, production mix | {FI} | 1.02E-01 | 0.0006 | 0.1% | 0.4 kWh/kg × 0.015 kg. |
| Cold impact extrusion – steel | 0.150 | kg | Deformation stroke, cold impact extrusion, steel | {RER} | 3.36E-02 | 0.0050 | 0.5% | Forming process for steel cup body only; steel material accounted separately above. |
| Tap water (20 washes) | 14.00 | kg | Tap water, at user | {RER} | 2.03E-04 | 0.0028 | 0.3% | 14 L ≈ 14 kg. RER proxy used; IL desalination would yield slightly higher factor (~9.7E-04). |
| Soap (20 washes) | 0.100 | kg | Soap, at plant | {RER} | 1.66E+00 | 0.1660 | 17.0% | 5 g/wash × 20 washes = 100 g. |
| **TOTAL** | | | | | | **0.974** | **100%** | |

---

## AI Disclosure

Claude (Anthropic, claude-sonnet-4-6) was used in this assignment as a brainstorming partner and calculation aid:
- Brainstorming on dataset selection and which BAFU entries best match each material
- Checking and verifying the numerical calculations
- Suggesting structure for presenting the results

All analytical decisions — including dataset selection, geographic assumptions, system boundary choices, and interpretation of results — were made by Omri Shamgar. The written text and conclusions reflect the student's own understanding of the material.
