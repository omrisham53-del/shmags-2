# Energy Program - Next Steps

**Priority Order**

1. [ ] Apply Daniel's model feedback (see below) - **do on work computer**
2. [ ] Complete techno-economic analysis in Excel
3. [ ] Draft supporting documentation
4. [ ] Finalize policy recommendations
5. [ ] Final ministry deliverables

---

## Daniel's Feedback - Tax Incentive Model (2026-06-01)

- [x] **Capex** - find it in the fund data (don't estimate; pull from the source) — Omri has this pulled from the grant program rounds extraction; being used directly for all 4 technologies
- [ ] **Electricity price** - use average across תעו"ז time bands (peak / off-peak / shoulder)
- [ ] **Interest rate** - use 6%

**Notes:**
- Add specific tasks as they become clearer
- Link to meeting notes in `notes/` folder

## Daniel's Unblocking Suggestion - Baseline Data Points (2026-07-06)

Omri was stuck making progress on the model; Daniel suggested a 3-step process:

1. [x] Find average data points from open sources for a first baseline reference → done, see `baseline-technology-data.md`. Revised once already to use real technology-specific standards (AHRI 550/590 IPLV, EN 14511, CAGI specific power, ASME PTC 4) and real manufacturer sourcing (Carrier/Trane/York) instead of generic COP/blog sourcing, after review caught the gaps.
2. [ ] Review with Daniel — confirm popular-spectrum picks and efficiency indicators
3. [ ] Talk with Rafi for verification — see the "Open Flags for Rafi" section in `baseline-technology-data.md`

Per-technology data points gathered: 2 capacity points on the popular spectrum (for linear interpolation), efficiency indicator, annual operating hours, and power.

**Open decision:** whether to drop electric steam systems (מערכות קיטור חשמליות) from the model entirely. Rafi's ~50% grid-efficiency factor means its primary-energy "savings" story doesn't clearly hold up against the fuel-oil baseline — see the 2026-07-06 decision log entries for the full reasoning. Not yet finalized.

**Resolved (2026-07-08):** Chiller annual operating hours locked at 3,000 as a working number (Omri, above the ~2,080-8,760 range an EcoTraders engineer gave verbally) — flagged for a later sensitivity analysis rather than further sourcing. Chiller kW/ton also reworked into a real baseline-vs-efficient split (ASHRAE 90.1 code minimum vs. DOE FEMP efficient tier). Heat pump baseline corrected from electric resistance to mazut/diesel-fired ovens/boilers per Rafi's notes, with a point-of-use + well-to-heat efficiency comparison added.

**Pending — engineer consult needed:** Heat pump annual operating hours (currently unsourced 3,000-4,000 estimate) — deliberately left open rather than locked to a placeholder, since Omri is consulting the EcoTraders engineer directly on this one. Blocks the annual fuel-consumption (tons/year) calc for the heat pump baseline until resolved. Omri is separately pulling real grant program data to sanity-check the range.

**Also needed:** ₪/ton fuel prices for diesel and mazut, to turn the heat pump efficiency comparison into actual OPEX cost savings. Omri has this in his Excel model already — needs pulling in alongside the caloric value data already used.

**Resolved (2026-07-12):** CapEx for all 4 technologies will use Omri's grant-program-rounds extraction directly (not open-source data). A same-day open-source CapEx attempt in `baseline-technology-data.md` was reversed and removed once this was clarified — see `decisions/log.md`. Also fixed real errors in the heat pump data: capacity points corrected to 40kW/70kW (the cited source didn't actually support 150kW), COP made capacity-specific and sourced (4.13 at 40kW, 3.23-3.24 at 70kW) instead of a flat estimated band, and heat pump vs. mazut/diesel oven data split into separate tables.
