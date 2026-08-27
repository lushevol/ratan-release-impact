---
type: query
title: Why Do Round 1 Uber Performance-Test Record Counts Not Reconcile?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, performance-testing, data-reconciliation, cashflow]
related: [uber, scbml, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md"]
---
# Why Do Round 1 Uber Performance-Test Record Counts Not Reconcile?

## Status

Open.

## Reconciliation gaps

The stated workload was 7,000 Murex records, 7,000 Stella records, and 100 Uber messages producing 200 cashflows. Recorded query output reports 6,773 Murex cashflows, 6,967 Stella cashflows, and 200 `uber_message` records.

The reported Settlement STP total is 13,737, while the displayed query counts sum to 13,940.

## Questions to resolve

- Why did Murex and Stella active-record counts fall below stated input volumes?
- Does `uber_message = 200` count messages, cashflows, or joined message-history rows?
- What population and deduplication rule produces the 13,737 STP total?
- Is `tr` in the recorded SQL a transcription error, and what executable query produced the output?
- What timezone and execution context apply to `2025-11-21 04:50:00`?