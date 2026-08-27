---
type: concept
title: Cashflow Detail Field Projection
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, cashflow-blotter, field-mapping, ui-projection, logical-model]
related: [cashflow-blotter, cashflow-record, trade-record, cashflow-status-lifecycle, what-are-the-authoritative-mappings-for-cashflow-details-page-unmapped-fields, what-are-the-valid-values-for-payment-payer-party-reference]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Cashflow Details page.md"]
---
# Cashflow Detail Field Projection

A cashflow detail field projection presents related trade-level and cashflow-level data in a single details view without defining a new underlying data model.

For the Cashflow Blotter details page, the projection has two primary groups:

- **Trade Details:** `Trade.Trade_Id`, `Trade.Trade_Version`, `Trade.Trade_State`, booking entity and counterparty codes, portfolio, ISDA taxonomy, and CFI code.
- **Cashflow Details:** `Cashflow.Cashflow_Id`, `Cashflow.Netting_Id`, business version, event type, affirmation status, payment date, currency, amount, payer-party reference-derived direction, and `Cashflow.Cashflow_State`.

The projection is documented in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-cashflow-blotter--21-c--obh2w3]] and applies to [[cashflow-blotter]], [[trade-record]], and [[cashflow-record]].

## Direction Derivation

The specified display rule is:

```text
If Cashflow.Payment_Payer_Party_Reference=='party1' then 'Pay' Else 'Receive'.
```

This rule does not define handling for null, malformed, or otherwise unknown payer-party references. Its correctness therefore depends on an authoritative constrained domain for `Cashflow.Payment_Payer_Party_Reference`.

## Unmapped Display Areas

The requirement includes Confirmation Status, Payment Cutoff, Sub Status, Action History, and Exceptions without authoritative paths, data sources, or display semantics. Cashflow Status is mapped to `Cashflow.Cashflow_State`, but Sub Status is not defined as part of [[cashflow-status-lifecycle]] by this source.

See [[what-are-the-authoritative-mappings-for-cashflow-details-page-unmapped-fields]] for the unresolved mappings and [[what-are-the-valid-values-for-payment-payer-party-reference]] for the direction-rule domain.