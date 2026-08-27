---
type: concept
title: Cashflow Blotter Exception Panel Visibility
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, exceptions, ui-logic, cashflow-status]
related: [cashflow-blotter, cashflow-status-lifecycle, vostro-panel, nostro-panel, authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
---
# Cashflow Blotter Exception Panel Visibility

[[cashflow-blotter]] exception visibility is status-gated rather than based solely on an exception's existence.

## Display Rule

For the listed Vostro and generic exception types, the UI displays an exception highlight only when the effective exception status—identified by the source as `Cashflow Sub Status`—is one of:

- `Pending Operator`
- `Pending Verification`

The generic types are `affirmation`, `back_value`, `nstp`, `high_risk_nstp`, `hard_blocker`, `other`, and `comment`.

The Vostro category has code-specific variants: `RATAN-201000002` Multi Vostro, `RATAN-201000001` Missing Vostro, `RATAN-201000003` SI Mismatch, `RATAN-201000006` Validate Bene Info, and `RATAN-201000005` Missing Nostro.

## Code-Specific Boundary

The broad `vostro` type does not imply identical UI treatment for every code. The source explicitly gives title and warning-color behavior for Multi Vostro and edit behavior for Missing Nostro only. It does not establish that these specialized behaviors apply to Missing Vostro, SI Mismatch, or Validate Bene Info.

`RATAN-201000010` / `Per SSI Adhoc` is an explicit exception: it is described as `INACTIVE` SSI Good Stamping data and is not shown in the exception panel.

## Unresolved Contract

The source implies equivalence between Exception Status and Cashflow Sub Status but does not define which system field is authoritative or how conflicts are resolved. See [[authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract]].