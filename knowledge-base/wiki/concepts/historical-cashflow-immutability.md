---
type: concept
title: Historical Cashflow Immutability
tags: [cashflow, historical-data, immutability, corrections, controls]
related: [cashflow-data-retention-lifecycle, hot-warm-cashflow-retrieval, cash-settlement-home-page]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Archival & Retrieval.md"]
---
# Historical Cashflow Immutability

The source asks whether updates should be prevented when a cashflow's value date is more than six months in the past. This indicates a possible immutability control for historical records, but no decision is recorded.

A six-month value-date rule could apply to records retrieved from warm storage, records still physically held in the Production Database, or both. Those interpretations have different operational consequences.

## Required Policy Decisions

The implementation needs to define:

- Which fields become immutable.
- Whether the restriction applies to all users, roles, or workflows.
- Whether privileged correction or remediation flows are permitted.
- How late settlement corrections, cancellations, reversals, and regulatory adjustments are handled.
- Whether updates are rejected, versioned, or recorded as compensating events.
- Which audit evidence is retained.
- Whether the rule is based on value date, physical storage tier, or another lifecycle event.

Immutability should not be implemented solely from the blank question in the source. It requires an approved exception model that remains compatible with the [[cashflow-data-retention-lifecycle]].
