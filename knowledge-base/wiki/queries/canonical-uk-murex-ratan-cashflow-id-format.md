---
type: query
title: What Is the Canonical UK Murex-RATAN Cashflow ID Format?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, cashflow-id, identifier, data-contract]
related: [uk-murex-ratan-high-volume-cashflow-feeding, murex-ratan-cashflow-message-contract, is-razorid-the-legacy-or-canonical-identifier-for-ratan-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# What Is the Canonical UK Murex-RATAN Cashflow ID Format?

The source lists `FLOW_ID` as `numeric(10,0)` but specifies `Formula_CashflowID`, which produces an alphanumeric value such as `M00087755146`.

Confirmation is required for:

- Target data type and maximum length.
- Whether the `M0` prefix includes a leading space.
- The required left-padding length and algorithm.
- Whether the formula is applied to both MxML and CSV inputs.
- The relationship to existing RATAN and RAZOR identifiers.