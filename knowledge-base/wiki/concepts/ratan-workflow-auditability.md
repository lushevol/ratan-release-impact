---
type: concept
title: RATAN Workflow Auditability
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, workflow, auditability, cashflow, maker-queue, operations]
related: [ratan-ktlo-tracker, ratan-accounting-status-lifecycle]
sources: ["RATAN/RATAN -KTLO Tracker/RATAN -KTLO Tracker.md"]
---
# RATAN Workflow Auditability

RATAN workflow auditability is the ability for authorised users to determine which business or system event caused a cashflow to change state or return to an operational queue.

## `RevertToQueued`

GENERIC TASK 10062646 states that a cashflow can be pushed back to the Maker queue through the action `RevertToQueued`. The source lists Nostro refresh, Vostro refresh, and netting-rule updates as triggers. It requests an audit comment that gives users an easy reference and reduces support queries.

The tracker reports three to four requests since August and states that Ops cannot easily retrieve the required information from the UI. This indicates an operator self-service and causal-history gap.

## Expected Audit Information

For each `RevertToQueued` event, the history should make the causal trigger, timestamp, initiating component or user, affected cashflow, prior and resulting workflow states, and any required remediation visible to authorised operators. The exact comment format and trigger taxonomy remain unspecified.

The source does not establish whether `RevertToQueued` is a formal accounting status transition or a workflow action recorded in audit history. Its relationship to [[concepts/ratan-accounting-status-lifecycle]] should be validated before updating that lifecycle as a formal state machine.