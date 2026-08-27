---
type: concept
title: RFI Portfolio Economic Amendment
tags: [RFI, portfolio, economic-amendment, cashflow, lifecycle, versioning]
related: [ratan, portfolio-based-rfi-nostro-stamping, cashflow-versioning, amendment-driven-cashflow-correlation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# RFI Portfolio Economic Amendment

An RFI portfolio economic amendment is the lifecycle treatment applied when a cashflow changes between RFI and non-RFI portfolio classifications.

## Required transitions

- Non-RFI to RFI: economic amendment.
- RFI to non-RFI: economic amendment.
- Non-RFI to non-RFI: not an economic amendment; the withdrawal and new event offset in the group blotter.

For an RFI/non-RFI transition, RATAN must process the latest cashflow version. The withdrawal and new cashflow are expected to enter waiting status and then be released after maker/checker processing.

If a technical failure prevents RATAN from retrieving the indicator needed to determine RFI status, the requirement mandates conservative default treatment as an economic change.

The source does not formally define “economic change,” the RFI indicator, or the complete correlation and status contract for withdrawal and replacement events.
