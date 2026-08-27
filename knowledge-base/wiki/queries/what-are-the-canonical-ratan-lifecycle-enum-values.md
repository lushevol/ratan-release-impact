---
type: query
title: What Are the Canonical RATAN Lifecycle Enum Values?
tags: [ratan, lifecycle, enums, data-quality, integration]
related: [ratan-cashflow-lifecycle-state-machine, what-are-the-canonical-cashflow-state-and-sub-state-values, what-is-the-authoritative-ratan-lifecycle-transition-matrix, tds3, stella]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# What Are the Canonical RATAN Lifecycle Enum Values?

The lifecycle requirements use inconsistent forms that require confirmation before they are encoded in APIs, data validation, reporting, or mappings.

## Inconsistencies to resolve

- `PARTIALLY-UTILIZED` in the status definition versus `PARTIALLY_UTILIZED` in the transition matrix.
- `NOSTRO MATCHED` in the status definition versus `NOSTRO_MATCHED` in the transition matrix.
- `TDS3` versus `TDSS3` in references to the status-synchronization platform.
- `Pending Netting 4 Withdrawal`, which appears to be a malformed sub-status type in repeated matrix rows.

The canonical source should identify exact enum spellings, backward-compatibility aliases if any, and the intended correction for malformed values.