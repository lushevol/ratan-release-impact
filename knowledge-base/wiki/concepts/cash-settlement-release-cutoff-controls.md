---
type: concept
title: Cash Settlement Release Cutoff Controls
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, operations, release-cutoff, netting, splitting]
related: [ratan, fmo-settlements, cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, were-ratan-release-time-controls-deployed-and-validated-by-their-2026-dates]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
---
# Cash Settlement Release Cutoff Controls

Cash settlement release cutoff controls restrict high-risk Operations transformations near automatic payment release. The RATAN source proposes preventing netting and splitting during the final ten minutes before the release cutoff, with a stated target date of 2026-01-17.

The control is intended to remove the period in which manual transformation of a `READY` gross cashflow can overlap with automatic release.

## Required clarification

The source gives the incident release time as 11:00:34 AM GMT but does not specify the authoritative clock, the configured cutoff timezone, exception handling, or whether netting and splitting are also prohibited after release processing begins. It also does not provide evidence that the restriction was deployed or tested.

A cutoff restriction complements, rather than replaces, [[release-time-cashflow-status-gating]] and concurrency-safe release design.