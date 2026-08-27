---
type: concept
title: H1-H2 Historical Cashflow Group Continuity
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, booking-model, cutover, cashflow-group, continuity]
related: [h1-booking-model, h2-booking-model, murex, cashflow-utilization-status-lifecycle, what-is-the-authoritative-h1-h2-historical-group-identity-and-cutover-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# H1-H2 Historical Cashflow Group Continuity

Historical cashflow group continuity is the requirement for [[h2-booking-model]] realtime processing to identify and update a group originally formed by [[h1-booking-model]], rather than create an unrelated H2-only group.

## Demonstrated Behavior

The source covers three non-cancellation boundaries:

- `VD` after H2 go-live.
- H1 `MxSystemDate+9` equal to the H2 date.
- `VD` equal to the H2 date.

In each scenario, H2 finds the existing three-member group. A count of 2 leaves the group `PENDING`; a count of 3 results in `COMPLETED`.

## H1 Eligibility Basis

The source uses the following inclusive H1 value-date window:

```text
MxSystemDate <= VD <= MxSystemDate+9
```

`MxSystemDate` is associated with [[murex]] in the scenario context, but the document does not establish field ownership or the business-date calculation.

## Limits

This requirement does not define the cross-model group key, a lookup-anchor rule, or handling for late, duplicate, reordered, and retried events. Repeated instructions to “Find C2” when another cashflow is received are ambiguous.

The limited statuses in these examples should not be treated as a canonical extension of [[cashflow-utilization-status-lifecycle]].