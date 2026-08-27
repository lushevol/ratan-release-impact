---
type: source
title: Ingenuine Rebook Exception in Ratan
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, rebook-exception, trade-amendment, cashflow, settlement-day-2]
related: [ratan, murex, stella, rebook-exception, amendment-driven-cashflow-correlation, payment-date-proximity-matching, settlement-day-2, was-currency-validation-newly-enforced-in-the-may-30-2026-ratan-rebook-change, what-is-the-validated-precision-and-recall-of-the-five-day-ratan-rebook-rule, can-uber-trade-events-provide-authoritative-amendment-lineage-for-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Ingenuine Rebook Exception in Ratan

This functional requirement documents a [[ratan]] control for cashflows created by trade amendments. An amendment produces a withdrawal of the original cashflow and a new cashflow. If the original cashflow was already released, Operations users must validate both events before release.

The intended outcomes are:

- A reversal exception for withdrawal of the original cashflow.
- A rebook exception for the amendment-created cashflow.

Ratan has no direct original-to-replacement cashflow relationship. It therefore uses a [[payment-date-proximity-matching|proximity-based matching rule]] as a proxy rather than confirmed amendment lineage.

## Documented matching rules

The earlier workaround generated a rebook exception when another cashflow had:

- The same Trade ID; for Murex cashflows, this is the Original Trade ID.
- The same currency.
- A status of released or settled.
- A payment date within 15 days of the prospective new cashflow.

The production logic deployed on 2026-05-30 retains the same Trade ID / Murex Original Trade ID, currency, and released-or-settled comparator conditions, while narrowing the payment-date window to 5 days.

The document characterizes the change as “5-day window + CCY validation,” although currency equality is also included in its description of the earlier 15-day rule. Whether currency validation was newly introduced, newly enforced, or already active is unresolved; see [[was-currency-validation-newly-enforced-in-the-may-30-2026-ratan-rebook-change]].

## Reported exception volumes

| Date | Rebook Exception （Murex+Stella） |
| --- | --- |
| 20260504-20260508 | 656 (444+212) |
| 20260511-20260515 | 443 (329+114) |
| 20260518-20260522 | 501 (370+131) |
| 20260525-20260529 | 386 (346+40) |
| **20260530** | **change deployment** |
| 20260601-20260605 | 292 (277+15) |
| 20260608-20260612 | 134 (125+9) |
| 20260615-20260619 | 171 (146+25） |

The source expects approximately a 40% reduction in rebook-exception volume. The reported figures show lower post-deployment volumes, but volume alone does not establish false-positive reduction, coverage of genuine rebooks, or causal impact of the rule change.

## Limitations and proposed enhancement

The five-day rule remains a screening heuristic and can miss genuine amendment rebooks outside the window or raise alerts for unrelated cashflows that meet the proxy conditions.

The source proposes:

- Adding direction to the matching criteria.
- Using a trade event after Uber is enabled.

A trade-event relationship could provide more authoritative [[amendment-driven-cashflow-correlation|amendment lineage]] than payment-date proximity. The required identifiers, timing, ownership, and reconciliation contract remain open in [[can-uber-trade-events-provide-authoritative-amendment-lineage-for-ratan]].