---
type: concept
title: Trade Major Version Cashflow Correlation
created: 2026-08-24
updated: 2026-08-24
tags: [trade-versioning, cashflow, correlation, Stella, Murex-2-11, RATAN, SCBML]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--34-trade-validation-cashf--mg1utu, cashflow-version-concurrency-control, fmrp-cashflow-status-synchronization, trade-validation-gated-cashflow-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process.md"]
---
# Trade Major Version Cashflow Correlation

## Definition

Trade major version cashflow correlation associates a cashflow with the exact trade version whose validation status controls its settlement visibility. It prevents validation of a later amendment from unintentionally releasing cashflows belonging to an earlier rejected or obsolete version.

## Stella correlation key

For Stella, RATAN uses:

```text
Trade_ID + Trade_Lake_Trade_Major_version
```

The version is extracted from the trade-lake `versionedTradeId` in the trade SCBML. A TDS3 validation message uses the same pair to find impacted cashflows and release only the matching version.

## Murex correlation key

For Murex 2.11, the source specifies `Source_System_Trade_Internal_Id` as the lookup identifier. Parent-trade validation is determined using the Murex-specific `Source_System_Validation_Status`, with `VALD` and `COMP` listed as accepted values.

The Murex rule must not be generalized into the Stella versioned correlation model without confirming the underlying data contract.

## Amendment implications

When major version 1 is rejected and version 2 is amended and validated, only version 2 cashflows should become visible. Economic amendments create withdrawal and replacement events; non-economic amendments additionally depend on whether the original cashflow was touched or settled.

This concept extends [[concepts/cashflow-version-concurrency-control]], while the canonical status and identifier contracts remain open.