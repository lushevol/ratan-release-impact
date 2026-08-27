---
type: query
title: What Is the Canonical NSTP Maker-Checker State Machine?
tags: [nstp, maker-checker, state-machine, cash-settlement, camunda]
related: [nstp, nstp-maker-checker-processing, cash-settlement-exception-handling, scbml, statusmachine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Canonical NSTP Maker-Checker State Machine?

The proposal references SCBML history updates to `Pending_Operator` and `NSTP_Release`, but it does not define a complete NSTP maker-checker state machine.

Open points include:

- Valid initial statuses and transition preconditions.
- Maker submission and checker completion outcomes.
- Approval, rejection, cancellation, rework, and release behavior.
- Terminal states and permitted re-entry.
- Duplicate requests, retries, concurrent checker tasks, and compensation.
- Which service is authoritative for transition validation and persistence.

The source is a proposed design and cannot establish these semantics.