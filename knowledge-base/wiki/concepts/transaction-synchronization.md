---
type: concept
title: FXU Transaction Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [transaction-synchronization, fxu, ratan, tds3, cash-settlement, architecture]
related: [fxu, ratan, tds3, razor, cash-settlement-service-landscape, which-system-owns-fxu-transaction-coordination]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# FXU Transaction Synchronization

FXU transaction synchronization is the coordination of state and data changes across FXU, RATAN, and TDS3 during utilization processing. The design treats synchronization ownership as an architectural choice rather than a fixed platform property.

## Ownership alternatives

- **FXU-coordinated model:** FXU handles transactions among TDS3, RATAN, and FXU.
- **RATAN-coordinated model:** RATAN handles transactions among TDS3, RATAN, and FXU.
- **RATAN-centered model:** RATAN owns accounting and persistence, with an existing cashflow-status hard block. TDS3 is involved when synchronization of the remaining amount needs transactional control.

The first two models persist FXU details in RATAN, TDS3, and FXU. The third lists persistence only in RATAN.

## Consequences

The selected coordinator determines where synchronization failures, exception workflows, and consistency controls are handled. The source does not describe transaction boundaries, compensation, retry, ordering, or recovery semantics. The ownership decision remains open in [[which-system-owns-fxu-transaction-coordination]].