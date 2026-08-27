---
type: query
title: What Are the RATAN Workflow-Crash Detection and Recovery Procedures?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, workflow, incident-management, recovery, reconciliation]
related: [ratan, murex-ratan-cashflow-reconciliation, cn-settlement-murex-211-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# What Are the RATAN Workflow-Crash Detection and Recovery Procedures?

The exception matrix identifies two RATAN workflow-crash scenarios but leaves capture and recovery blank:

- Murex published a cashflow but RATAN does not display it because of a RATAN workflow crash.
- RATAN issued a response but Murex does not synchronize it because of a RATAN workflow crash.

MQ recovery is described separately: outbound failures are recovered by Murex status rollback and republish, while inbound failures are recovered by RATAN replay. Those procedures do not establish recovery for RATAN workflow crashes.

## Evidence needed

- RATAN error queues, alerting, and monitoring controls.
- Incident ownership, escalation target, and recovery runbook.
- Replay/idempotency rules following a RATAN workflow restart.
- Reconciliation evidence that confirms restored Murex and RATAN state.