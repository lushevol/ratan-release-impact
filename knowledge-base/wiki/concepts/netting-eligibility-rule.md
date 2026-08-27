---
type: concept
title: Netting Eligibility Rule
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, eligibility, business-rule, settlement]
related: [client-level-cashflow-netting, fmrp-china-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Netting Eligibility Rule

## Documented predicate

The source defines eligibility using the following exact attributes and operators:

| Attribute | Operator | Value |
| --- | --- | --- |
| Entity.Booking_Entity_SCI_FMID | IN | 10036642,400899993 |
| Cashflow.Payment_Currency | IN | CNO,USD |
| Entity.Counterparty_SCI_FMID | IN | 10032025,400054708 |
| Instrument_Common.CFI_Code | == | SESXXX |
| Cashflow.Netting_Id | == | 10036642,300068459 |

## Interpretation

A cashflow is in the documented netting population only when its booking entity, payment currency, counterparty, instrument CFI code, and netting identifier satisfy the stated predicates.

## Validation issue

The rule uses `CNO`, while the test scenarios use `CNY` and `USD`; an expected-result description also mentions `JPY`. The source does not establish whether `CNO` is a valid system code or a documentation error. See [[which-currency-code-is-valid-for-netting-eligibility]].
