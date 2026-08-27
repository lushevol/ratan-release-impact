---
type: stakeholder
title: FMO Ops
tags: [FMO, operations, cash-settlement, exceptions, STP, fmo-ops, authorization, operational-risk]
related: [cdu, ratan, cashflow-reference-consistency-validation, cashflow-blotter-exception-panel-visibility, fmo-users, profile-based-usd-authorization-limits, profile-limit-static-data-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# FMO Ops

## Role

The CDU Trade Confirmation Notification & Cashflow requirement identifies FMO Ops users as the proposed operational recipients of exceptions when a CDU confirmation notification cannot be reconciled with the latest cashflow available in [[ratan]].

The Profile USD Limit requirement describes FMO Ops as the operations stakeholder group requesting differentiated Ratan profiles based on operational seniority and BAU risk control.

The Profile USD Limit source does not establish whether FMO Ops is organizationally distinct from the broader [[fmo-users]] group. That relationship should be confirmed.

## Cashflow reconciliation exceptions

Under the proposed Reference ID control described in the CDU Trade Confirmation Notification & Cashflow requirement, a mismatch must prevent STP rather than release a potentially stale cashflow. Ratan should raise an exception for FMO Ops users when, for example, the confirmation Reference ID is `102` and the available cashflow Reference ID is `101`.

That source does not define the exception queue, notification channel, ownership SLA, or manual-resolution workflow.

## Profile-based operational responsibilities

The proposed operating model in the Profile USD Limit requirement assigns FMO roles progressively different capabilities:

- Maker activities for operational cash-settlement actions.
- Checker approval for exceptions within defined USD thresholds.
- High-value approval for senior profiles.
- Static-data and business-rule administration through separate maker and approver roles.

## Related control concerns

According to the Profile USD Limit requirement, FMO Ops depends on:

- A complete entitlement matrix.
- Reproducible USD conversion.
- Backend enforcement of profile limits.

The proposed controls are documented in [[profile-based-usd-authorization-limits]] and [[profile-limit-static-data-governance]].