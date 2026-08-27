---
type: concept
title: Standard Settlement Instructions
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, settlement, reference-data]
related: [cash-settlement-2025-roadmap, ratan, cashflow-migration, ssi-selection-hierarchy, ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# Standard Settlement Instructions

Standard Settlement Instructions, abbreviated SSI, are standing instructions used to determine how settlement should occur.

## Role in the Roadmap

SSI behavior is a significant dependency in the migration to [[ratan]]. The source records work involving:

- A Tranche 1 SSI selection hierarchy that should follow the UK model
- A revised SI hierarchy for Stella Prime payments
- Vostro SI Settlement Means values
- UK Prime trade SSI stamping aligned with cashflow best-match behavior
- Strategic One Stop SSI stamping

## Related Concerns

[[ssi-selection-hierarchy]] governs how a candidate instruction is selected. [[ssi-stamping]] concerns applying the selected instruction to a trade or cashflow.

The source does not provide the actual hierarchy, best-match algorithm, data fields, exception handling, or acceptance criteria.