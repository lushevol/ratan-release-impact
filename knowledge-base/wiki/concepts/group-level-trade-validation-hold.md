---
type: concept
title: Group-Level Trade Validation Hold
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-holding, trade-validation, cashflow-groups, RatanOne]
related: [trade-validation-gating, manual-cashflow-holding, ratanone, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# Group-Level Trade Validation Hold

A group-level trade validation hold temporarily retains cashflow messages when the cashflow group is complete but one or more associated trades have not reached an accepted validation status.

## Role in the preferred design

Option 1 proposes that the Group service:

1. Detect whether all expected cashflows have arrived.
2. Check the associated trade validation status.
3. Hold messages when validation is incomplete.
4. Publish to workflow only after both group completion and trade validation.
5. Disable `Manual STP` for affected items.

This is an automated control in the Group service. It is distinct from [[manual-cashflow-holding]], which represents an operator-driven hold.

## State and event considerations

The source identifies `PENDING`, `PENDING_TRADE_VALIDATION`, and `OFFSET` but does not define a complete state machine. In particular, it does not specify:

- How a held group is released after late validation.
- How validation failures, reversals, or corrections are handled.
- Whether the hold is persisted at group, cashflow, or trade-link level.
- How new and withdrawal events are correlated when a group is held.
- What audit record demonstrates that release occurred only after validation.

The amendment scenario in the source indicates that different trade versions may create unnecessary or delayed payments, so release and version semantics require explicit design.
