---
type: concept
title: SWIFT Status Reconciliation
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, swift, status, reconciliation, operational-controls]
related: [settlement-suppression, straight-through-processing, cash-settlement-re-platforming]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# SWIFT Status Reconciliation

SWIFT status reconciliation is the alignment of message-processing states with the corresponding cashflow status and operational dashboard presentation.

## Backlog Evidence

Several 2025 FMRP backlog items indicate recurring lifecycle-consistency concerns:

- ADO 5997797 reports a condition where the Swift status is “Released by AMH” while cashflows remain in “Released” status.
- ADO 6473019 proposes including MT103+202COV in the dashboard’s SWIFT Error criteria.
- ADO 6090337 proposes updating auto-deleted FMSGW cases to a Swift Suppressed cashflow status.
- Another item proposes warning users when net resultant cancellation requires manual Swift cancellation.
- Swift MT101 is listed as a prospective Day 2 feature under ADO 6470024.

## Interpretation

Together, these items suggest gaps between messaging-system state, cashflow-application state, and operational visibility. The source does not provide incident counts, root causes, severity, or an authoritative status mapping.

[[settlement-suppression]] is a closely related control because suppressed and auto-deleted cases must be represented consistently across systems. No assumption should be made that AMH and FMSGW perform the same role.