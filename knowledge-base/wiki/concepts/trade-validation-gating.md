---
type: concept
title: Trade Validation Gating
created: 2026-08-24
updated: 2026-08-24
tags: [trade-validation, cash-settlement, workflow-control, settlement-operations]
related: [group-level-trade-validation-hold, fmrp-major-version-backward-validation, ratanone, tds3, cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# Trade Validation Gating

Trade validation gating is the control that prevents a cashflow group from entering settlement workflow until the group is complete and every associated trade satisfies the validation rule for its source system.

## Proposed behavior

A group remains `PENDING` while expected cashflows are still arriving. Once the group is complete:

- A group with validated associated trades may be published to workflow.
- A group with any unvalidated associated trade enters `PENDING_TRADE_VALIDATION`.
- `Manual STP` is disabled for items associated with an unvalidated trade under the preferred design.

The gate is proposed at the Group-service boundary in Option 1. Option 2 would instead add `TOBEVALIDATED` to the lifecycle and make the Lifecycle service query the Group service.

## Source-specific rules

The gate must preserve the distinction between systems:

- FMRP uses trade ID, major version, and an accepted validation status.
- Murex uses trade ID and an accepted validation status.
- FMRP validation at a higher major version applies backward to earlier major versions.
- The FMRP version rule must not be generalized to Murex.

## Architectural tension

The preferred option avoids changing the main lifecycle workflow but gives the Group service responsibility for a progression control. This creates an unresolved boundary between group management and lifecycle management. The source also does not specify whether validation is represented at group level, cashflow level, or both.

Related lifecycle ownership questions are tracked in [[cashflow-stamping-domain-ownership]] and [[what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract]].
