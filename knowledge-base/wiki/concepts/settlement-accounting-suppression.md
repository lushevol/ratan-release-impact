---
type: concept
title: Settlement Accounting Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-accounting, accounting-suppression, swift, uk, cash-settlement]
related: [cash-settlement, ukde, uk-specific-swift-logic, settlement-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis.md"]
---
# Settlement Accounting Suppression

Settlement accounting suppression is the processing pattern in which a settlement message is generated while specified settlement-accounting entries are not created.

For UKDE PM processing, ticket **4038613** describes generating SWIFT while suppressing settlement accounting and UK accounting. The tracker records test-case readiness, development readiness, and UAT running as of the Q3 2024 snapshot.

The source does not identify the exact accounting entries, suppression conditions, reconciliation behavior, or UAT result. The requirement should not be treated as equivalent to the broader [[concepts/settlement-suppression]] concept without confirming the applicable accounting scope.

---