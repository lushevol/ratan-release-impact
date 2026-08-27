---
type: source
title: Auto Un-Net - Trade market event
authors: []
year: 0
url: ""
venue: Functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, ratan, trade-market-event, auto-un-netting]
related: [ratan, stella, murex, automatic-un-netting-on-trade-market-events, cashflow-event-versioning, does-auto-un-netting-place-cashflows-in-nstp-or-queued, what-market-event-correlation-key-triggers-ratan-auto-un-netting, what-is-the-ratan-auto-un-netting-contract-for-cancellation-and-termination, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Auto Un-Net - Trade market event.md"]
---
# Auto Un-Net - Trade market event

## Summary

This functional requirement specifies an automatic Ratan un-netting scenario for FMRP strategy netting. Netting components can originate in Stella, Murex 2.11, or MXCash. When Ratan identifies a subsequent trade-market event for a netted cashflow, it must automatically un-net the affected group.

The document demonstrates this behavior only for a Stella Amendment to component `C103`. The event releases all components in netting group `N101` and retires the Ratan-generated resultant. It does not define the event-correlation key, ordering, idempotency behavior, or the equivalent processing for Cancellation and Termination events.

## Stated background

FMRP strategy netting is handled in [[ratan]]. Cashflows may be sourced from Stella, Murex 2.11, and MXCash. Subsequent trade-market events, including Amendment, Cancellation, and Termination, can produce new cashflow events for a previously netted component.

The narrative says that un-netted cashflows are held as `NSTP` for user review and further action. This conflicts with the detailed worked example, where all released components have status `Queued`. See [[does-auto-un-netting-place-cashflows-in-nstp-or-queued]].

## Worked amendment scenario

### Netting completed in Ratan

| Cashflow Type | Cashflow ID | Cashflow Event | Cashflow Version | Netting ID | Source System | Booking Entity | Counterpart | Currency | Pay/Receive | Amount | Product | Value Date | Cashflow Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Netting Component | C101 | New | 1 | N101 | Murex 2.11 | Shanghai | JP Morgan | USD | Pay | 100 | IRS | 10/20/2022 | Netted |
| Netting Component | C102 | New | 1 | N101 | Murex 2.11 | Shanghai | JP Morgan | USD | Receive | 150 | IRS | 10/20/2022 | Netted |
| Netting Component | C103 | New | 1 | N101 | Stella | Shanghai | JP Morgan | USD | Pay | 200 | Loan | 10/20/2022 | Netted |
| Netting Resultant | C104 | New | 0 | N101 | Ratan | Shanghai | JP Morgan | USD | Pay | 150 | IRS | 10/20/2022 | Queued |

### Amendment received from Stella

| Cashflow Type | Cashflow ID | Cashflow Event | Cashflow Version | Netting ID | Source System | Booking Entity | Counterpart | Currency | Pay/Receive | Amount | Product | Value Date | Cashflow Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Netting Component | C103 | Amendment | 2 | N101 | Stella | Shanghai | JP Morgan | USD | Pay | 300 | Loan | 10/20/2022 | Projected |

### Auto un-net performed in Ratan

| Cashflow Type | Cashflow ID | Cashflow Event | Cashflow Version | Netting ID | Source System | Booking Entity | Counterpart | Currency | Pay/Receive | Amount | Product | Value Date | Cashflow Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | C101 | New | 1 | N101 | Murex 2.11 | Shanghai | JP Morgan | USD | Pay | 100 | IRS | 10/20/2022 | Queued |
|  | C102 | New | 1 | N101 | Murex 2.11 | Shanghai | JP Morgan | USD | Receive | 150 | IRS | 10/20/2022 | Queued |
|  | C103 | Amendment | 2 | N101 | Stella | Shanghai | JP Morgan | USD | Pay | 300 | Loan | 10/20/2022 | Queued |
|  | C104 | New | 0 | N101 | Ratan | Shanghai | JP Morgan | USD | Pay | 150 | IRS | 10/20/2022 | Dead |

## Demonstrated behavior

For the illustrated `N101` group:

- A Stella Amendment changes `C103` from version `1`, amount `200`, to version `2`, amount `300`.
- Ratan automatically un-nets the entire group, including Murex 2.11 components unaffected by the incoming amendment.
- `C101` and `C102` transition from `Netted` to `Queued`.
- Amended `C103` transitions from `Projected` to `Queued`.
- Ratan resultant `C104` transitions from `Queued` to `Dead`.

These transitions are evidence for the illustrated Amendment scenario only; they are not specified as universal rules for other event types or lifecycle states.

## Unresolved requirements

- Whether `NSTP` is a status, hold flag, exception workflow, or an outdated narrative term relative to `Queued`.
- The correlation fields used to associate an incoming event with a prior netting component and netting group.
- Version ordering, duplicate-event handling, concurrency behavior, and stale-event handling.
- Cancellation and Termination outcomes.
- Whether `Netting ID` remains persisted after un-netting or is retained only as audit lineage.
- Whether released components are re-netted automatically, netted manually, or kept out of the prior cycle.

Related pages: [[automatic-un-netting-on-trade-market-events]], [[cashflow-event-versioning]], [[what-market-event-correlation-key-triggers-ratan-auto-un-netting]], and [[what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]].