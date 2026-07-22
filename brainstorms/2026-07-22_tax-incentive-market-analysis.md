# Tax Incentive Chapter -- Market Analysis Methodology

**Date:** 2026-07-22
**Context:** EcoTraders national energy program. The tax incentive chapter (accelerated depreciation for energy-efficient equipment) mirrors the grant chapter's structure. The Excel model is the MICRO view (per-unit economics); the market analysis is the MACRO view that produces the chapter's results. Daniel scoped a chiller method and asked Omri to brainstorm the rest with Claude, then bring solutions back.

---

## The core reframe

Market analysis = **micro model per-unit results x adoption count per technology.**

The model already produces, per representative unit: NPV, energy saved (MWh), CO2 saved (tCO2), and (once added) the fiscal cost of the incentive. Scaling to the whole market is one multiplication: how many units adopt. So the entire chapter hinges on one hard question per technology:

> How many installations realistically adopt under this incentive?

Everything else is arithmetic off the model that already exists.

## Adoption: binary, driven by the model (Daniel's call)

Not a soft adoption percentage. **100% if the incentive convinces the firm, 0% if not.** The model's invest-or-not switch (the A-C row Daniel asked to add, with conditional formatting) decides it: if the incentive flips the representative unit's NPV positive, the whole addressable segment for that unit adopts; if not, none of it does. The switch can differ by size segment (on for 500 RT, off for 100 RT). Defensible to the Ministry in a way a hand-picked adoption % is not.

## Grant data dropped for sizing

Grant-program rounds are budget-capped and selection-biased. They show what the program funded, not what the market is. Wrong denominator. Omri's call, agreed. Each technology is sized from its own real demand driver instead.

---

## Sizing engine per technology

### Chillers (strongest, Daniel's method)
- CBS non-residential construction starts over the last 5 years -> growth parameter (trend the series forward over the policy horizon).
- RT/m2 assumption -> converts new floor area to installed cooling capacity -> chillers.
- Non-residential categories only (offices, commercial, hotels, institutional, industry). Residential uses split units, excluded.
- New construction = conservative base case. Replacement handled as a **sensitivity**: replacement/year ~= existing stock RT / lifetime, using the model's own lifetime (rows 42-43, ~15-17 yrs). Needs an estimate of existing installed stock (from cumulative historical construction).
- OPEN: RT/m2 needs a real per-building-type source (cooling-load density varies hugely by type). Candidates: ASHRAE rule-of-thumb, or an Israeli source (SI 5282 / local HVAC reference). Pull a real citation, do not pick a number.

### Heat pumps (bounded hard by a technical ceiling)
- Size off the **national energy balance** (CBS "אספקה וצריכה של אנרגיה" / Ministry of Energy tables): industrial mazut/diesel burned for heat = the addressable pool.
- NOT the MRV. The MRV gave Omri conversion/emission factors only (the 0.085 / 0.088 ton/MWh caloric values), not facility fuel consumption. The MRV registry (Ministry of Environmental Protection) could hold facility-level fuel use IF Omri has access to that dataset -- open question.
- HARD CONSTRAINT: heat pumps only reach low-to-medium temperature heat (~80-90C common, ~150C for rare high-temp models). Much industrial fuel goes to high-temp process/steam a heat pump cannot serve, so the addressable pool is only the low-temp share, not all industrial fuel oil. That fraction is itself an assumption (source it or get it from Rafi) and it is what most shrinks this market. Flag to Daniel: heat pumps have a ceiling the other two techs do not.

### VSD compressors (roughest, leans on borrowed benchmarks)
- Size off **national industrial electricity** (CBS electricity-by-sector / Electricity Authority annual report / Noga) x compressed-air share.
- Compressed-air share ~10% of industrial electricity: an INTERNATIONAL rule of thumb (US DOE compressed-air sourcebook; Radgen & Blaustein 2001 EU study), not an Israeli measurement. Cite it as a borrowed benchmark, do not dress it as local data.
- Narrow further: only variable-load compressors benefit from VSD (base-load running flat-out do not), and VSD savings are ~15-35% on that variable-load portion.
- Be upfront with Daniel: chillers is the rigorous one, VSD is the roughest.

---

## Fiscal cost (highest-leverage, likely the headline)

Compute the state's cost as the **NPV of the deferred tax (a timing cost), NOT the full deduction.**

A grant is a cash outlay: cost = full grant. Accelerated depreciation is never cash: the firm deducts the same 100% of the equipment over its life either way (the 2x multiplier only front-loads it), so the state loses only the time value of collecting that tax later. Much smaller than a grant of the same headline size.

Why it matters: report ₪/tCO2 for both instruments on one ruler, and if the tax side is the small timing cost while the grant side is full outlay, the tax incentive looks far cheaper per tCO2. That is probably the chapter's punchline -- but only if measured consistently.

NEXT ACTION: open the model's ניתוח (analysis) sheet and check whether fiscal cost is computed at all, and if so whether it is timing-based or wrongly counting the full deduction. This gates the whole cost-effectiveness story.

## Parked for a future Daniel discussion

Additionality / deadweight: for segments where the efficient tech is already profitable WITHOUT the incentive, the firm adopts anyway, so the incentive is pure deadweight cost with no behavior change. "100% if convinced" handles the flip cases; decide later whether already-profitable segments count as incentive impact or get netted out. Same question the grant chapter took a position on. Revisit after the model fixes and Rafi's data land.

---

## Immediate next actions
1. Check the analysis sheet for the fiscal-cost calc (timing vs full deduction). Add it if missing.
2. Build the chiller engine: pull the real CBS non-residential construction series + a sourced RT/m2.
3. Confirm whether Omri has MRV registry access (facility fuel use) or only the factors.
4. Then heat pump and VSD engines from the energy balance.
