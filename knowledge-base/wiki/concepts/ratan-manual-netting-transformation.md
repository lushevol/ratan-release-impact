---
type: concept
title: RATAN Manual Netting Transformation
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, netting, lifecycle, manual-processing]
related: [ratan, cashflow-record, lien-aware-netting-and-auto-unnetting, what-is-the-authoritative-ratan-manual-netting-api-and-resultant-cashflow-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md"]
---
# RATAN Manual Netting Transformation

The Sprint 13 demo specifies that manually running the RATAN Netting API on mocked component cashflows should:

1. Move each component cashflow to `Netted`.
2. Create a resultant cashflow with state `Queued`.

This is a baseline functional expectation for manual netting, not evidence of a complete API or production behavior.

The source does not define component eligibility, grouping dimensions, amount calculation, component-to-resultant linkage, transaction atomicity, idempotency, reversals, unnetting, error handling, or retry behavior. It does not establish lien-aware rules described in [[lien-aware-netting-and-auto-unnetting]].