---
type: concept
title: Grouped Cashflow Monitoring
tags: [cash-settlement, monitoring, grouped-cashflows, exception-management]
related: [group-blotter, group-pending-monitoring, group-pending-validation-monitoring, cash-settlement-home-page, trade-cashflow-reference-linkage]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Grouped Cashflow Monitoring

Grouped cashflow monitoring evaluates related payments as a set rather than treating each cashflow as an independent item.

The [[cash-settlement-home-page]] exposes group-level exception counters and routes users to the [[group-blotter]] for investigation. The principal monitoring categories are incomplete receipt and pending trade validation.

## Operational value

A group can remain unresolved even when one or more of its payments have been received. Operations must compare the expected payment set with the payments delivered to [[ratan]], identify the missing member, and investigate the source workflow.

This approach supports detection of:

- Payments missing from an expected feeding batch.
- Payments stuck in Murex processing.
- Validation-dependent cashflows.
- Trade-reference synchronization failures between Murex 2.11 and RATAN.

The source does not specify the authoritative grouping key or the formal algorithm used to derive group status.