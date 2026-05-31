# HW3 Research Notes - Option B: Single-Use vs. Reusable Cup LCA

## Assignment Context
- Option B: 20 days of hot drink service at Karnaf store, Reichman University
- Two products: (A) disposable paper/PS cup, (B) reusable stainless steel + silicone cup
- Questions: Functional unit, system boundary type, system boundary diagram, assumptions, total GWP, biggest contributor

---

## Selected BAFU Datasets

### Materials
| Material | BAFU Dataset | Geography | GWP Factor |
|----------|-------------|-----------|------------|
| Paper (cup body) | Kraft paper, unbleached, at plant | {RER} | 7.11E-01 kgCO2eq/kg |
| LDPE (coating) | Polyethylene, LDPE, granulate, at plant | {RER} | 2.35E+00 kgCO2eq/kg |
| Polystyrene (lid) | Polystyrene, general purpose, GPPS, at plant | {RER} | 3.65E+00 kgCO2eq/kg |
| Steel (cup body) | Chromium steel 18/8, at plant | {RER} | 4.42E+00 kgCO2eq/kg |
| Silicone (lid + wrapper) | Silicone product, at plant | {RER} | 2.79E+00 kgCO2eq/kg |

### Transport
| Mode | BAFU Dataset | Geography | GWP Factor |
|------|-------------|-----------|------------|
| Lorry (land, Israel) | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 kgCO2eq/tkm |
| Lorry (land, Finland) | Transport, freight, lorry, 16t-32t gross weight, fleet average | {RER} | 2.22E-01 kgCO2eq/tkm |
| Sea freight | Transport, transoceanic container ship | {OCE} | 1.60E-02 kgCO2eq/tkm |

### Electricity
| Source | BAFU Dataset | GWP Factor |
|--------|-------------|------------|
| Israel | Given in assignment | 0.397 kgCO2eq/kWh |
| Finland | Electricity, production mix {FI} | 1.02E-01 kgCO2eq/kWh |

### Washing & Disposal
| Item | BAFU Dataset | Geography | GWP Factor |
|------|-------------|-----------|------------|
| Tap water | Tap water, at user | {RER} | 2.03E-04 kgCO2eq/kg |
| Soap | Soap, at plant | {RER} | 1.66E+00 kgCO2eq/kg |
| Paper disposal | Disposal, packaging paper, 13.7% water, to municipal incineration | {CH} | 4.33E-02 kgCO2eq/kg |
| LDPE disposal | Disposal, polyethylene, 0.4% water, to municipal incineration | {CH} | 3.03E+00 kgCO2eq/kg |
| PS disposal | Disposal, polystyrene, 0.2% water, to municipal incineration | {CH} | 3.20E+00 kgCO2eq/kg |

### Cold Impact Extrusion (steel cup forming)
| Step | BAFU Dataset | Geography | GWP Factor |
|------|-------------|-----------|------------|
| Steel forming | Deformation stroke, cold impact extrusion, steel | {RER} | 3.36E-02 kgCO2eq/kg |

---

## LDPE Coating Process Emission
- Given directly in assignment: 0.002 kgCO2eq per cup (not from BAFU)

---

## Transport Distances (estimated)
- Hedera → Natanya (paper): ~38 km (Route 4 northbound)
- Haifa → Natanya (LDPE, PS): ~63 km
- Espoo → Helsinki (truck): ~20 km
- Helsinki → Herzliya by sea: ~7,500 km (Baltic → North Sea → English Channel → Mediterranean → Israel)

---

## PRODUCT A - SINGLE-USE CUP: Full Calculation

### Raw Materials (20 cups + 20 lids)
| Component | Qty | Emission Factor | GWP |
|-----------|-----|----------------|-----|
| Paper | 0.240 kg | 0.711 | 0.1706 kgCO2eq |
| LDPE | 0.020 kg | 2.35 | 0.0470 kgCO2eq |
| Polystyrene | 0.080 kg | 3.65 | 0.2920 kgCO2eq |
| **Subtotal** | | | **0.5096 kgCO2eq** |

### Transport
| Route | Qty | Factor | GWP |
|-------|-----|--------|-----|
| Paper: Hedera→Natanya | 0.000240t × 38km = 0.00912 tkm | 0.222 | 0.00202 kgCO2eq |
| LDPE: Haifa→Natanya | 0.000020t × 63km = 0.00126 tkm | 0.222 | 0.00028 kgCO2eq |
| PS: Haifa→Natanya | 0.000080t × 63km = 0.00504 tkm | 0.222 | 0.00112 kgCO2eq |
| **Subtotal** | | | **0.00342 kgCO2eq** |

### Processing
| Step | Qty | Factor | GWP |
|------|-----|--------|-----|
| Cup forming (Israel elec.) | 0.8 kWh | 0.397 | 0.3176 kgCO2eq |
| LDPE coating | 20 cups | 0.002/cup | 0.0400 kgCO2eq |
| **Subtotal** | | | **0.3576 kgCO2eq** |

### Disposal (incineration, 20 cups + 20 lids)
| Material | Qty | Factor | GWP |
|----------|-----|--------|-----|
| Paper | 0.240 kg | 0.0433 | 0.01039 kgCO2eq |
| LDPE | 0.020 kg | 3.03 | 0.06060 kgCO2eq |
| PS | 0.080 kg | 3.20 | 0.25600 kgCO2eq |
| **Subtotal** | | | **0.32699 kgCO2eq** |

### TOTAL PRODUCT A = 0.5096 + 0.0034 + 0.3576 + 0.3270 = **1.197 kgCO2eq**

### Contributions (A)
- Raw materials: 42.6%
- Transport: 0.3%
- Processing: 29.9%
- Disposal: 27.3%
- **Biggest single contributor: PS (polystyrene raw material) = 24.4%**

---

## PRODUCT B - REUSABLE STEEL CUP: Full Calculation

### Raw Materials
| Component | Qty | Emission Factor | GWP |
|-----------|-----|----------------|-----|
| Steel (18/8) | 0.150 kg | 4.42 | 0.6630 kgCO2eq |
| Silicone (lid) | 0.025 kg | 2.79 | 0.06975 kgCO2eq |
| Silicone (wrapper) | 0.015 kg | 2.79 | 0.04185 kgCO2eq |
| **Subtotal** | | | **0.7746 kgCO2eq** |

### Transport
| Route | Qty | Factor | GWP |
|-------|-----|--------|-----|
| Espoo→Helsinki (truck) | 0.000190t × 20km = 0.00380 tkm | 0.222 | 0.000844 kgCO2eq |
| Helsinki→Herzliya (sea) | 0.000190t × 7500km = 1.425 tkm | 0.0160 | 0.02280 kgCO2eq |
| **Subtotal** | | | **0.02364 kgCO2eq** |

### Processing
| Step | Qty | Factor | GWP |
|------|-----|--------|-----|
| Lid conversion (FI elec.) | 0.4 × 0.025 = 0.010 kWh | 0.102 | 0.001020 kgCO2eq |
| Wrapper conversion (FI elec.) | 0.4 × 0.015 = 0.006 kWh | 0.102 | 0.000612 kgCO2eq |
| Cold impact extrusion (steel) | 0.150 kg | 0.0336/kg | 0.005040 kgCO2eq |
| **Subtotal** | | | **0.006672 kgCO2eq** |

### Use Phase (20 washes)
| Input | Qty | Factor | GWP |
|-------|-----|--------|-----|
| Water | 14 kg | 0.000203 | 0.002842 kgCO2eq |
| Soap | 0.100 kg | 1.66 | 0.166000 kgCO2eq |
| **Subtotal** | | | **0.168842 kgCO2eq** |

### TOTAL PRODUCT B = 0.7746 + 0.0236 + 0.0067 + 0.1688 = **0.974 kgCO2eq**

### Contributions (B)
- Raw materials: 79.6%
- Transport: 2.4%
- Processing: 0.7%
- Use phase (washing): 17.3%
- **Biggest single contributor: Steel = 68.1%**

---

## Summary
| Product | Total GWP | Winner |
|---------|-----------|--------|
| A - Single-use (20 cups) | 1.197 kgCO2eq | |
| B - Reusable (1 cup, 20 uses) | 0.974 kgCO2eq | Yes |

Reusable cup is ~19% lower GWP over 20 days. Break-even would occur well before 20 uses.
