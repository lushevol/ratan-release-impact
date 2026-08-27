---
type: concept
title: Accounting Feed Reconciliation
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, reconciliation, cashflow, controls, cash-settlement]
related: [ebbs, aspire, bcdf, cashflow-accounting-stamping, cashflow-accounting-eligibility, swift-message-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Accounting Feed Reconciliation

## Definition

Accounting feed reconciliation is the process of verifying that cashflows selected for accounting are represented correctly in the accounting feed and, where applicable, accepted by the receiving accounting system.

Although the source file is named `Accounting & Recon.md`, it does not define a reconciliation design.

## Missing Controls

The source does not specify:

- Reconciliation keys.
- Expected-versus-actual population checks.
- Amount or currency tolerances.
- Duplicate detection.
- Missing or rejected record handling.
- File-level and payment-level statuses.
- Replay and correction procedures.
- Ownership of reconciliation breaks.
- Reporting frequency or retention.

The reconciliation model must be defined separately for Aspire and EBBS unless a common control framework is confirmed.

## Related Pattern

[[swift-message-reconciliation]] is an adjacent wiki concept, but its lifecycle, statuses, and controls must not be assumed to apply to BCDF accounting feeds without evidence.
