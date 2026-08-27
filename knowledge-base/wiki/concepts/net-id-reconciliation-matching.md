---
type: concept
title: Net ID Reconciliation Matching
tags: [cash-settlement, netting, reconciliation, tlm]
related: [ratan, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Net ID Reconciliation Matching

Ratan requires [[tlm]] to auto-match many trades to one cashflow using a common Net ID. The stated purpose is Bridge suspense reconciliation.

The source does not define Net ID generation, uniqueness, matching tolerances, exception handling, reversal behavior, or the resolution workflow for unmatched items.