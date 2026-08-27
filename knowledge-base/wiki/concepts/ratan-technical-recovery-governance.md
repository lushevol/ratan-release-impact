---
type: concept
title: RATAN Technical Recovery Governance
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, governance, risk-acceptance, auditability, KTLO]
related: [ratan, ratan-temporary-technical-recovery, pss, development-team, ops-team, azure-devops, ratan-operational-observability, ratan-workflow-auditability]
sources: ["RATAN/RATAN -Projects/Temporary tech recovery process for Handling Technical Failure Exceptions v1.0.md"]
---

# RATAN Technical Recovery Governance

RATAN Technical Recovery Governance controls the use of temporary PSS recovery through approval, risk acceptance, ownership, tracking, review, and escalation.

## Approval and risk acceptance

Temporary recovery steps must be documented in Confluence and approved by the relevant Product Owner before execution.

The relevant Business Owner and/or Product Owner must acknowledge that the workaround is temporary and risk-bearing. The source distinguishes these controls conceptually but does not clarify whether both approvals are always required.

## Tracking and accountability

Every exception requires an ADO ticket, a named Development owner, and a committed permanent-fix ETA. These requirements support [[ratan-workflow-auditability]] and [[ratan-operational-observability]].

## Recurrence thresholds

The source requires accelerated remediation when:

- A P4 or higher incident occurs.
- The same issue occurs twice within one week.
- Manual replay or recovery occurs more than three times within one month.

Other repeated recoveries are classified as [[ratan-resilience-control-debt]] and prioritized above normal enhancement work.

The source does not define the severity convention, counting method, time-window boundaries, or issue-identity rules.

## Review and escalation

Tracked exceptions and permanent-fix items are reviewed every two weeks at the KTLO prioritization call. Slippage against the agreed target date is escalated to the Development Head, PSS Head, and CPO.
