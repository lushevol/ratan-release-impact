---
type: concept
title: Trade-to-Cashflow Lien Correlation
created: 2026-08-23
updated: 2026-08-23
tags: [trade-correlation, cashflow-migration, lien, murex, ratan, event-ordering]
related: [murex, murex-211, ratan, lien-driven-cashflow-nstp, cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence, cashflow-technical-failure-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration.md"]
---
# Trade-to-Cashflow Lien Correlation

## Definition

Trade-to-cashflow Lien correlation is the process of associating a Murex cashflow with its originating Murex trade and the applicable Lien state so that RATAN can determine whether the cashflow should receive a `Lien` exception.

The source states that Murex trades and cashflows are separate business objects handled through separate data flows. Correlation is therefore an architectural prerequisite for [[concepts/lien-driven-cashflow-nstp]].

## Required Information

A complete implementation must be able to determine:

1. The originating Murex trade for each cashflow.
2. The Lien status and its effective time or sequence.
3. Whether the cashflow was created, amended, withdrawn, or migrated before or after the Lien event.
4. Whether another settlement exception remains after Lien removal.

The source does not identify the authoritative field, message, API, or correlation key for these data elements.

## Failure and Ordering Considerations

The design must define behavior when:

- A cashflow arrives before its trade or Lien status.
- A trade update arrives after the related cashflow.
- Lien placement and removal events are received out of order.
- One of the trade and cashflow feeds is delayed or missing.
- A cashflow is amended after a Lien event.
- A cashflow has both a `Lien` exception and another exception.

Possible implementation concerns include event sequencing, state reconciliation, versioned cashflow persistence, and recovery of incomplete associations. These concerns are relevant to [[concepts/business-versioned-cashflow-persistence]] and [[concepts/cashflow-technical-failure-recovery]], but the source does not prescribe a solution.

## Open Design Boundary

The phrase “cashflows post Lien update” requires a precise definition. It may refer to newly generated cashflows, amended cashflows, cashflows received after the event, or all future cashflows economically affected by the trade. This ambiguity is tracked in [[queries/what-is-the-effective-date-rule-for-lien-cashflow-nstp]].
