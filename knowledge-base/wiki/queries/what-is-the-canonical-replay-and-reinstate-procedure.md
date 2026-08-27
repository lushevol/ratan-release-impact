---
type: query
title: What Is the Canonical Replay and Reinstate Procedure?
created: 2026-08-24
updated: 2026-08-24
tags: [replay, reinstate, operations, cashflow, controls]
related: [cashflow-reinstatement-and-replay, cashflow-blotter, oscar, murex, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# What Is the Canonical Replay and Reinstate Procedure?

The source describes several recovery actions: inbound message replay, Ratan-to-Murex status replay, cashflow-blotter replay, `ReInstate`, and manual OSCAR booking.

The procedure needs to define, for each action:

- eligible lifecycle states and preconditions;
- who may initiate and approve the action;
- duplicate-processing controls, especially when Kafka redelivery is also possible;
- evidence and audit records;
- post-recovery verification; and
- reconciliation requirements for manual OSCAR booking.