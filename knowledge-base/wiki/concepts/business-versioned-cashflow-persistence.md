---
type: concept
title: Business-Versioned Cashflow Persistence
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, business-version, persistence, SCBML, history, performance]
related: [cashflow-lifecycle-state-machine, cashflow-message-event-source, murex-to-ratan-cashflow-interface, confirmation-match-based-payment-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---
# Business-Versioned Cashflow Persistence

Business-versioned cashflow persistence chooses insert, update, and conditional-write behavior by comparing the incoming cashflow ID and business version with the current stored record.

## Scenario rules

| Scenario | Event-source record | SCBML history | Current SCBML message | Cutoff information | Holding message | Affirmation status |
| --- | --- | --- | --- | --- | --- | --- |
| New cashflow ID | Insert | Insert | Insert | Insert | NA | Insert if affirmed in SCBML |
| Business version downgrade | Insert | Insert new and update current | Update | Insert | NA | Insert if affirmed in SCBML |
| Business version upgrade | Insert | Insert new and update current | Update | Insert | Update current on demand | Insert if affirmed in SCBML |
| Business version unchanged | Update | Insert new and update current | Update | Insert if not exists | Insert on demand | Insert if affirmed from request |

A downgrade is described as a “late start, early arrival” in which an older incoming version arrives after a newer version is already present. The design preserves the incoming historical event while updating the current representation.

## Persistence principles

- `ratan_stella_message_event_source` is insert-oriented for new or versioned events and update-oriented when the business version is unchanged.
- `ratan_cashflow_scbml_history` preserves lineage while maintaining the current version.
- `ratan_cashflow_scbml_message` is updated for existing cashflows.
- Cutoff information is inserted, with an explicit no-duplicate condition for unchanged versions.
- Holding-message writes are demand-driven.
- Affirmation status is conditional and has different stated sources depending on the scenario.

The design optimizes writes without discarding historical version information. It does not specify version-ordering rules, uniqueness constraints, transaction boundaries, or field-level immutability.