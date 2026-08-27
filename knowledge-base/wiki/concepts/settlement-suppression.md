---
type: concept
title: Settlement Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, suppression, controls, exceptions, swift]
related: [maker-checker-segregation, swift-status-reconciliation, standard-settlement-instructions, netting-on-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# Settlement Suppression

Settlement suppression prevents or halts settlement processing or associated payment-message transmission for a cashflow.

## Backlog Scope

The 2025 FMRP backlog includes requirements to:

- Permit suppression and other actions while an item is on HOLD.
- Display exceptions to the Checker when suppression is performed.
- Automatically suppress zero-amount cashflows.
- Update auto-deleted FMSGW cases to a Swift Suppressed cashflow status.
- Warn users when a net resultant cancellation requires manual Swift cancellation.

## Control Implications

Suppression intersects with [[maker-checker-segregation]] because the backlog calls for Checker visibility into exceptions. It also intersects with [[swift-status-reconciliation]] because an internal suppression state must remain consistent with message-generation and gateway behavior.

The source does not define whether every suppression action blocks message creation, message release, settlement booking, or all three. These effects require flow-specific confirmation.