---
type: entity
title: Cashflow
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, domain-model, workflow, settlement]
related: [manual-cashflow-holding, cashflow-status-restoration, ratan-cashflow-lifecycle-service, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Manual Holding Process Tech Design.md"]
---
# Cashflow

A cashflow is the settlement-domain object subject to lifecycle processing in RATANONE Cash Settlement. The manual-holding design treats its workflow status as the selected representation for an operator-applied hold.

A held cashflow must not continue through the specified in-progress operations. When the hold is removed, the design intends that the cashflow return to its original status rather than repeat already completed work.

The source evaluates, but does not select, adding a boolean `isHeld` attribute to the cashflow model. Therefore, `isHeld` should not be treated as an implemented or authoritative model field without further evidence.

## Related behavior

- [[manual-cashflow-holding]] describes the hold and unhold capability.
- [[cashflow-status-restoration]] describes restoration after unhold.
- [[ratan-cashflow-lifecycle-service]] is a candidate service owner in the evaluated `isHeld` alternative.
- [[query-service]] would need to expose hold-related data if a queryable hold field were implemented.