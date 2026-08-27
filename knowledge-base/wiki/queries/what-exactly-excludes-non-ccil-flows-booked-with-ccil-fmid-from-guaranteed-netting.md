---
type: query
title: What Exactly Excludes Non-CCIL Flows Booked with CCIL FMID from Guaranteed Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, netting, eligibility, FMID, IRS, open-question]
related: [ccil-guaranteed-and-non-guaranteed-netting, ccil, cashflow-logical-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# What Exactly Excludes Non-CCIL Flows Booked with CCIL FMID from Guaranteed Netting?

## Question

What formal eligibility predicate prevents Cash and Bond flows booked with counterparty FMID `400021949` from being included in guaranteed CCIL IRS netting?

## Evidence

The guaranteed matrix uses:

```text
Settlement Method == CCIL
Cashflow Status in (WAITING)
Cashflow_Sub_State_Type == 'Pending Netting'
Counterparty FMID == 400021949
```

However, the source explicitly states that Cash and Bond flows booked with FMID `400021949` must not be netted with guaranteed IRS cashflows. The examples distinguish the in-scope product as `Family = IRD`, `Group = IRS`, and `Typology = Vanilla IR Swap`, but the formal matrix does not include those fields.

## Required Resolution

Confirm whether the authoritative rule also requires product family, product group, typology, booking entity, currency, payment type, or another classification. The result should be documented in the GUI and backend validation rules so that FMID-only classification cannot create an incorrect netting population.