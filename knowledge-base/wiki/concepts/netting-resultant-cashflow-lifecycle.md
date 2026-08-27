---
type: concept
title: Netting Resultant Cashflow Lifecycle
created: 2026-08-22
updated: 2026-08-23
tags: [cashflow, netting, lifecycle, NSTP, maker-checker, cash-settlement, resultant-cashflow, state-transition]
related: [cashflow-lifecycle-state-machine, maker-checker-settlement-control, cashflow-blotter-netting-workflow, ratan, fmsre, bilateral-netting, netting-withdrawal-timing, manual-and-automatic-netting-un-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Netting Resultant Cashflow Lifecycle

A netting operation consumes one or more eligible component cashflows and creates a new resultant cashflow. Components and the resultant share a `Netting ID`, providing audit and review linkage.

## Component eligibility and validation

According to the CPN Business Scenario source, the normal netting queue contains component cashflows with:

```text
Cashflow Status: Pending
Sub Status: Pending Netting
```

Its validation key is:

```text
Booking Entity + Counterparty + Currency + Value Date
+ Status not Released or Settled
```

Cashflows with different counterparties, booking entities, or value dates cannot be combined. A cashflow that has already been released—particularly one whose SWIFT message was sent to [[fmsre]]—is ineligible.

The CPN Business Scenario source also permits ad-hoc requests to include cashflows normally following the gross path:

```text
Cashflow Status: Validated
Sub Status: Pending Release
```

This is permitted only before release and remains subject to the common-key and lifecycle checks.

The Bilateral Netting user-case source uses different state terminology for components, describing successful netting as a transition from:

```text
WAITING / Pending Netting
```

to:

```text
NETTED
```

## Resultant creation

The CPN Business Scenario source specifies that Pay and Receive directions are used as signed amounts when calculating the resultant. The resultant inherits the product type of the first component cashflow, receives a new cashflow ID, and is proposed to receive the SSI of that first component.

The Bilateral Netting user-case source repeatedly requires the resultant amount to be correct, but does not provide an amount-calculation rule.

After netting submission, the CPN Business Scenario source states that:

- Each component receives the shared `Netting ID` and is marked `Netted`.
- The resultant receives the same `Netting ID`.
- The resultant enters the NSTP review queue.
- The Checker can inspect all linked components.

The Bilateral Netting user-case source additionally requires that the resultant have:

- `Affirmation status = 'Affirmed'`
- `Payment type = 'Bilateral Netting'`

## Maker-checker review and release

The Maker submits the netting request, and a different user acts as Checker.

According to the CPN Business Scenario source, the Checker can either accept the resultant or revert the operation. On acceptance, the resultant leaves the NSTP queue and becomes:

```text
Cashflow Status: Validated
Sub Status: Pending Release
```

It then waits for the configured release cutoff.

The same source's detailed examples show the resultant initially as:

```text
Pending / Netting Review
```

although an intermediate example labels it:

```text
Gross / Queued
```

This terminology requires reconciliation with the canonical lifecycle model.

The Bilateral Netting user-case source describes NSTP as completing through `MAKER_CHECKER` and requires Operations to release the resultant from [[ratan]].

The CPN Business Scenario source does not define the exact component states or audit behavior after Checker rejection or reversion.

## Manual un-netting

The Bilateral Netting user-case source specifies that, when a user selects a resultant and chooses `Un-Net Cashflow`, the system displays a component-cashflow popup.

After the user selects `Un-Net all Cashflow`:

```text
Resultant: state = 'DEAD'
Components: state = 'WAITING'
Components: cashflow sub state type = 'Pending Netting'
```

## Automatic un-netting following component withdrawal

According to the Bilateral Netting user-case source, if a component is withdrawn while the resultant is neither `SETTLED` nor `RELEASED`, the system automatically un-nets the resultant:

```text
Resultant: state = 'DEAD'
Withdrawn component: state = 'CANCELLED'
Remaining components: WAITING / Pending Netting
```

The remaining components may subsequently generate a new resultant.

## Withdrawal after resultant release or settlement

The Bilateral Netting user-case source requires a resultant to remain in its existing state when a component is withdrawn after that resultant is `SETTLED` or `RELEASED`.

The same source states that, in this case:

- The withdrawn component is `WAITING`.
- Another component remains `NETTED`.

It does not define the accounting, reversal, or lineage consequences of this situation.