---
type: query
title: What Are the Authoritative Accounting-Feed Task State Transitions?
created: 2026-08-24
updated: 2026-08-24
tags: [state-machine, accounting, task-lifecycle, open-question]
related: [cashflow-group-and-message-state-machines, cashflow-lifecycle-state-machine-restructuring, accounting-feed-file-generation-idempotency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# What Are the Authoritative Accounting-Feed Task State Transitions?

The examples associate actions including `Fail`, `SwiftSuppress`, `Reinstate`, `UnSwiftSuppress`, `Release`, and `NostroStamped` with task statuses `HOLD`, `MISSING_INFO`, `MISS_INFO`, `DISABLED`, and `SUCCESS`. The document has a “Status Machine” heading but supplies no transition model.

A formal accounting-feed task state machine is needed, including whether `MISSING_INFO` and `MISS_INFO` are distinct, action preconditions, terminal states, retry behavior, and the relationship between task state, file generation, FileIT delivery, and cashflow lifecycle updates. This must remain separate from the cashflow state models in [[cashflow-group-and-message-state-machines]] and [[cashflow-lifecycle-state-machine-restructuring]].