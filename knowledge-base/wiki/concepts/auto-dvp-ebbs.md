---
type: concept
title: Auto DVP with eBBS RTA Notifications
created: 2026-08-23
updated: 2026-08-23
tags: [auto-dvp, eBBS, RTA, settlement, DVP, Ratan]
related: [dvp-exception-lifecycle, ebbs-rta-notification-validation, cashflow-lineage-and-amendment-correlation, split-cashflow-dvp-handling, ratan, ebbs, murex, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# Auto DVP with eBBS RTA Notifications

Auto DVP is the specified Ratan behavior in which a qualifying eBBS RTA notification for a released Receive cashflow settles that cashflow and automatically closes the DVP exception on a linked Pay cashflow.

## Apparent eligibility rule

The UAT specification indicates an AND-style rule:

```text
Auto DVP =
    covered cashflows
    AND eligible booking entity
    AND eligible CCS product
    AND valid cashflow linkage
    AND Receive cashflow released
    AND qualifying EBBS RTA notification
    AND Pay cashflow has DVP exception
```

Murex eligibility is `Instrument_Common__ISDA_Taxonomy == "IRD|CS"`. Stella eligibility is one of:

```text
InterestRate:CrossCurrency:FixedFloat
InterestRate:CrossCurrency:Basis
InterestRate:CrossCurrency:FixedFixed
InterestRate:CrossCurrency:FloatFloat
```

Murex linkage uses the same `tradeid` and payment date. Stella linkage uses the same trade ID, major version, and payment date.

## Directionality

The behavior is Receive-to-Pay directional. A Receive-side RTA notification can close a linked Pay-side exception. A Pay-side RTA notification settles the Pay cashflow but does not automatically settle or close the Receive-side relationship.

## Expected outcomes

When the conditions are met:

- The Receive cashflow moves from `Waiting` to `Settled`.
- The linked Pay cashflow’s DVP exception is closed.
- The Cashflow Details UI may show a green `DVP Received` tag.

If entity scope, CCS eligibility, or RTA validation fails, the Receive cashflow may still settle while the Pay-side DVP exception remains open.

## Relationship handling

A Receive cashflow linked to split Pay children may cause the exceptions on other linked children to close after the Receive-side RTA event. A non-split one-to-many relationship does not receive the same automatic closure in the specified scenarios.

An amended cashflow appears to inherit Auto DVP treatment when its trade ID remains unchanged. A changed trade ID appears to create a new relationship that does not inherit automatic closure.

## Evidence boundary

The source defines expected UAT behavior only. It contains no completed test results and should not be treated as confirmation of production behavior.