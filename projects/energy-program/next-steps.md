# Energy Program - Next Steps

**Priority Order**

1. [ ] Apply Daniel's model feedback (see below) - **do on work computer**
2. [ ] Complete techno-economic analysis in Excel
3. [ ] Draft supporting documentation
4. [ ] Finalize policy recommendations
5. [ ] Final ministry deliverables

---

## Daniel's Feedback - Tax Incentive Model (2026-06-01)

- [ ] **Capex** - find it in the fund data (don't estimate; pull from the source)
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

**Still unresolved after sourcing:** chiller annual operating hours (EFLH) — tried Illinois TRM, ASHRAE, DOE reference buildings, ACEEE; couldn't get a solid citation (partly because WebFetch in this session's environment is restricted to a "trusted network access" allowlist that blocks most of these). Remains an assumption for Rafi, not a sourced figure.
