---
type: query
title: Are StellaInfo Conversions and Common Event Publication Still Required?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, stellainfo, ratan-stella-message-event, event-publication, cashflow]
related: [cashflow-lifecycle-stamping, data-persistence-node, ratan-stella-message-event-source]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# Are StellaInfo Conversions and Common Event Publication Still Required?

## Question

Can the conversion and publication steps in the precheck flow be removed or simplified without changing persistence, SCBML construction, or downstream behavior?

## Evidence

The source questions:

- Whether conversion to `StellaInfo` is still required.
- Why `RatanStellaMessageEvent` is converted to `StellaInfo` again.
- Whether publication of a common Event is still required.

These questions indicate unresolved design uncertainty, not confirmed defects.

## Investigation needs

Confirm the consumers and contracts for each representation and event, including:

- Persistence schema requirements.
- SCBML construction inputs.
- Downstream event consumers.
- Duplicate-delivery and ordering behavior.
- Compatibility requirements for Withdrawal and New flows.
- Whether any common-event consumer remains active.

## Current position

Do not remove either conversion or common-event publication until active consumers and replacement contracts are verified.
