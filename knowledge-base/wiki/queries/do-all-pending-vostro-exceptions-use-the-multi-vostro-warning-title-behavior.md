---
type: query
title: Do All Pending Vostro Exceptions Use the Multi Vostro Warning Title Behavior?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, vostro, exceptions, ui-behavior]
related: [vostro-panel, cashflow-blotter-exception-panel-visibility, authoritative-cashflow-blotter-exception-panel-and-manual-edit-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Manual Fix Exception.md"]
---
# Do All Pending Vostro Exceptions Use the Multi Vostro Warning Title Behavior?

The requirement explicitly assigns `${exp.Exception_Code} Exception` and `COLOR_WARNING` to pending `RATAN-201000002` / Multi Vostro.

It requires exception-panel visibility for pending `RATAN-201000001` / Missing Vostro, `RATAN-201000003` / SI Mismatch, and `RATAN-201000006` / Validate Bene Info, but does not specify equivalent Vostro title or color behavior.

Confirm whether these three exception codes use the Multi Vostro presentation, distinct presentations, or only the generic exception panel highlight. Until confirmed, Multi Vostro styling must not be generalized to them.