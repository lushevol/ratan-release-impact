---
type: concept
title: Netting Validation and Preview
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-netting, validation, net-preview, backend-validation, concurrency-control]
related: [settlement-netting-validation-generation, adhoc-cashflow-netting, cashflow-auto-netting, cashflow-blotter-action-eligibility, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Settlement Netting Validation Generation.md"]
---
# Netting Validation and Preview

Netting validation determines whether a selected set of cashflows can be combined. The requirement applies the validation in both the GUI and backend service.

## Eligibility key

Every selected component must match on:

```text
Booking Entity
Counterparty
Currency
Value Date
```

Every selected component must also have a status other than:

```text
Released
Settled
```

The operation must be rejected if any key differs or if any component has crossed the release or settlement boundary. Netting is not allowed after the cashflow has been sent to [[entities/razor]].

## Preview control

Before submission, Net Preview must show:

- The selected component cashflows.
- Their booking entity, counterparty, currency, value date, direction, amount, and product.
- The projected resultant.
- The signed Pay/Receive calculation.
- The product and other attributes proposed for the resultant.

The maker can discard the preview or submit the request. Preview is therefore a control point, not merely a display feature.

## Backend and concurrency controls

The backend must repeat the validation after submission and immediately before mutating component states. A cashflow that was eligible when selected must be rejected if it becomes `Released`, `Settled`, or otherwise unavailable before the transaction commits.

The implementation should make component locking or an equivalent atomic compare-and-set decision explicit, especially because `Validated` cashflows may be approaching release cutoff.

## Failure messages

The source specifies these messages:

```text
Netting have to perform on same Booking Entity, Counterparty, Currency, Value Date
Netting is not allowed on 'Released'/'Settled' cashflow.
```

The source does not define separate messages for mixed products, duplicate selection, missing components, stale previews, rounding failure, or resultant SSI failure.