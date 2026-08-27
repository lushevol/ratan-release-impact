---
type: query
title: What Is the Authoritative HOLD/UNHOLD Status Restoration and Eligibility Matrix?
tags: [cashflow, hold, unhold, status-machine, lifecycle]
related: [cashflow-hold-and-unhold, ratan, failed-cashflow-status, what-is-the-authoritative-failed-cashflow-state-machine]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# What Is the Authoritative HOLD/UNHOLD Status Restoration and Eligibility Matrix?

The requirement establishes that UNHOLD should restore the state that existed immediately before HOLD, but its matrix inconsistently represents `Pending Exception`, `Pending Netting`, and `Reversal_Rebook` as either main statuses or values under `WAITING`.

## Questions to resolve

- Is the canonical main-status literal `HOLD` or `ON HOLD`?
- Which values are main statuses, sub-status types, and sub-statuses?
- What complete source-state set is eligible for HOLD?
- Are `FAILED`, `CANCELLED`, `DEAD`, `SWIFT SUPPRESSED`, and `CASHFLOW SUPPRESSED` ineligible?
- What prior-state snapshot must be persisted to guarantee exact restoration?
- Does the cited Confluence Status Machine supersede any matrix entry in this requirement?

The requirement is partial evidence for [[what-is-the-authoritative-failed-cashflow-state-machine]], not a definitive lifecycle specification.