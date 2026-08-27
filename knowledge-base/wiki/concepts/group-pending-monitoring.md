---
type: concept
title: Group Pending Monitoring
tags: [cash-settlement, group-pending, exception-monitoring, payment-receipt]
related: [group-blotter, grouped-cashflow-monitoring, grouped-cashflow-completeness, ratan, murex-2-11]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Group Pending Monitoring

**Group Pending** is a group-level monitoring state indicating that the expected set of related payments has not been fully received.

A non-zero Group Pending dashboard count opens the [[group-blotter]] filtered to `Status = PENDING`.

## Investigation

Operations should:

1. Query all underlying payments with the original trade ID.
2. Review the `Pending Reason`.
3. Identify the missing payment ID.
4. Check the payment status in [[murex-2-11]].
5. Ask the Murex 2.11 PSS team to investigate an undelivered payment.
6. Follow the applicable Murex DOI to deliver the payment to [[ratan]].

The source expects the pending exception to clear automatically after the missing payment is delivered, but it does not define the formal closure rule.

## Example

Payments `108185597` and `108185598` were generated from the same market event. The first reached RATAN and the second did not. The first payment remained `PENDING` because the group was incomplete.