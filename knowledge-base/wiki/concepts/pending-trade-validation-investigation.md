---
type: concept
title: Pending Trade Validation Investigation
tags: [cash-settlement, trade-validation, operational-investigation, value-date]
related: [group-pending-validation-monitoring, group-blotter, trade-confirmation-driven-cashflow-stp, stella, murex]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Pending Trade Validation Investigation

Pending trade validation investigation is the operational process for determining why a cashflow has not progressed beyond `Pending Trade Validation`.

Operations first inspect the value date and prioritize payments with imminent settlement dates. They then use the trade ID in the relevant trade-processing interface to distinguish between:

- A matching Murex and RATAN trade ID awaiting validation.
- A Murex trade-ID divergence caused by a non-economic amendment.
- A [[stella]] trade with state `TOBESENT`.

Matching-ID cases may require MO to validate the trade. Divergent-ID cases may require a [[manual-cashflow-push-from-group-blotter]]. A Stella `TOBESENT` case requires escalation to MO for validation.

The source does not define the exact event that changes the cashflow to an eligible processing state, nor does it define an investigation SLA.