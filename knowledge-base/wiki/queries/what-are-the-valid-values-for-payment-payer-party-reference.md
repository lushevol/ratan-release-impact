---
type: query
title: What Are the Valid Values for Payment Payer Party Reference?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, pay-receive, data-quality, field-validation, open-question]
related: [cashflow-detail-field-projection, cashflow-record, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Cashflow Details page.md"]
---
# What Are the Valid Values for Payment Payer Party Reference?

The Cashflow Details page specifies the following Pay/Receive display logic:

```text
If Cashflow.Payment_Payer_Party_Reference=='party1' then 'Pay' Else 'Receive'.
```

This makes `party1` the only explicit Pay value and classifies every other value as Receive.

## Open Questions

- Is `Cashflow.Payment_Payer_Party_Reference` constrained to exactly `party1` and one opposing party value?
- Can the field be null, blank, malformed, or unavailable?
- If unknown values are possible, should they display as Receive, Unknown, blank, or an error state?
- Is the reference interpreted relative to the booking entity, the selected user context, or another party identity?
- Is this derivation performed by the source service or by the [[cashflow-blotter]] UI?

## Impact

Without a validated domain contract, the fallback behavior can misrepresent unknown or invalid payer references as Receive. The requirement supports the documented rule for the [[cashflow-detail-field-projection]], but does not provide validation, error handling, or alternative display semantics.