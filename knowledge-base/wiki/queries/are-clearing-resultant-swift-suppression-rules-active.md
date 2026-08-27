---
type: query
title: Are Clearing Resultant SWIFT Suppression Rules Active?
created: 2026-08-22
updated: 2026-08-22
tags: [swift-suppression, clearing, static-data, deployment]
related: [clearing-resultant-swift-suppression, swift-versus-cashflow-suppression, cashflow-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# Are Clearing Resultant SWIFT Suppression Rules Active?

## Question

Were the documented clearing and SAL SWIFT-suppression rule changes approved and activated in the intended environment?

## Evidence

The source records new, updated, and disabled suppression rules, including IDs `7351885393248022528`, `7351891133699129344`, `7356611640855298048`, `7356241418356981760`, and `7356241729352040448`. It also identifies a correction from a comma-delimited equality predicate to an FMID `in (...)` predicate for CME, EUREX, JSCC, and ICE.

All relevant `Rule Status` fields are blank. Therefore, the source does not demonstrate that the rules are active.

## Needed evidence

- Approved static-data change records.
- Effective rule versions and activation timestamps.
- Runtime samples showing suppression for each named scope.
- Confirmation that superseded or disabled rules no longer apply.