---
type: concept
title: NSTP Maker-Checker Processing
tags: [nstp, cash-settlement, maker-checker, camunda, workflow]
related: [nstp, camunda, ratanone-camunda-flow-starter, cashflow-user-operation-record, statusmachine, cash-settlement-exception-handling, canonical-nstp-maker-checker-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# NSTP Maker-Checker Processing

NSTP maker-checker processing is the proposed workflow for manually initiating and completing NSTP-related operations through Camunda-managed maker and checker activities.

The design scope includes:

- A maker API that starts a Camunda process through [[ratanone-camunda-flow-starter]].
- A checker API that completes a checker user task.
- Recording user-operation activity in [[cashflow-user-operation-record]].
- An NSTP sub-workflow invoked from `1_5_Nstp_Check.bpmn` in [[ratan-cash-settlement-orchestration]].
- Camunda calls to update SCBML history to `Pending_Operator` and `NSTP_Release`.
- A Camunda-callable API provided by [[statusmachine]].

The source does not define the complete state machine. In particular, it leaves maker/checker identity binding, segregation of duties, rejection, cancellation, rework, duplicate processing, task concurrency, retry, and final-state behavior unresolved.