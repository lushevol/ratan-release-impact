---
type: concept
title: Group Pending Validation Monitoring
tags: [cash-settlement, group-pending-validation, trade-validation, exception-monitoring]
related: [group-blotter, pending-trade-validation-investigation, trade-confirmation-driven-cashflow-stp, murex, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Group Pending Validation Monitoring

**Group Pending Validation** identifies grouped cashflows that await trade or market-event validation.

A non-zero dashboard count opens the [[group-blotter]] with cashflows in `Pending Trade Validation`. Operations should prioritize cases with an imminent value date, such as the following day, although the source defines no exact cutoff or SLA.

## Processing cases

- **Murex with matching trade ID:** The RATAN and Murex trade IDs match, but validation is incomplete. Settlement Ops may approach MO, especially when a client requests payment affirmation.
- **Murex with divergent trade ID:** A non-economic amendment creates a new validated Murex trade ID that is not synchronized to RATAN. Manual cashflow pushing is required.
- **Stella with unvalidated trade:** The cashflow remains in `Pending Trade Validation`. The user checks the same trade ID and major version in the trade blotter; `TOBESENT` indicates that MO should validate the trade.

The Murex and Stella cases are separate processing paths and should not be treated as one shared validation state model.