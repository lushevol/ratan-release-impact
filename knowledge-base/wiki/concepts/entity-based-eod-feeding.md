---
type: concept
title: Entity-Based EOD Feeding
created: 2026-08-23
updated: 2026-08-23
tags: [eod, accounting, feeding, entity-scheduling, cash-settlement]
related: [ebbs, aspire, bcdf, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Entity-Based EOD Feeding

## Definition

Entity-based EOD feeding is an end-of-day accounting-feed approach in which data is scheduled and transmitted according to the receiving legal or operational entity.

The source specifies:

- EOD scheduling by entity.
- Feeding data through BCDF files.

## Applied Scope

The approach is included in the planned integration scope for Aspire and EBBS accounting feeds. EBBS is explicitly described as having an “EOD approach by entity.”

The source does not define:

- Entity calendars or cut-off times.
- Batch boundaries.
- Time-zone behavior.
- File partitioning.
- Late or corrected cashflow handling.
- Acknowledgement and retry behavior.
- Reconciliation outputs.
