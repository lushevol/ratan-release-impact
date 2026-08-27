---
type: concept
title: Maker-Checker Segregation
created: 2026-08-22
updated: 2026-08-22
tags: [operational-control, approval, segregation-of-duties]
related: [auto-netting, cash-settlement-2025-roadmap, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/2025 Target.md"]
---
# Maker-Checker Segregation

Maker-checker segregation separates the person who performs or initiates an operation from the person who reviews or approves it. It is one form of segregation of duties.

## Roadmap Tension

Work item `6473089` states:

> Allow user who did netting to act as Checker

This may affect maker-checker segregation, but the source does not establish that it is a control failure. The meaning and authority of the Checker role are not defined.

## Information Needed

Control assessment requires confirmation of:

- Whether Checker is an approval role
- Which products, entities, and risk levels are in scope
- Whether another independent approval remains
- Whether the same user may check their own netting result
- Whether the change is limited to exception handling
- Audit logging and monitoring requirements
- Approval by Operations, Compliance, or Operational Risk
- Compensating controls

Until those details are available, the item should be recorded as an unresolved control question rather than characterized as non-compliant.