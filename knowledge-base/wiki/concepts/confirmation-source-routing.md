---
type: concept
title: Confirmation Source Routing
created: 2026-08-23
updated: 2026-08-23
tags: [confirmation, source-of-truth, routing, stella, cdu-lake, deprecated-evidence]
related: [trade-confirmation-driven-cashflow-stp, cdu-lake, fmrp, cfets, stella, what-is-the-current-fmrp-and-cfets-confirmation-status-source-and-eligibility-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# Confirmation Source Routing

Confirmation-source routing determines which system supplies the confirmation status used for cashflow STP for a given trade population.

A deprecated requirement presents [[cdu-lake]] as the normal consolidation path for Murex 2.11 and Stella confirmations, but identifies historical exceptions:

- [[fmrp]]: source confirmation status directly from [[stella]] rather than CDU Lake, with `AFFIRMED` and `CONFIRMED`.
- [[cfets]]: source confirmation status directly from Stella rather than CDU Lake, including `COMP`.

The source does not state when these exceptions took effect, whether they remain active, their complete scope, or fallback behavior. They should not be treated as current routing rules until validated.