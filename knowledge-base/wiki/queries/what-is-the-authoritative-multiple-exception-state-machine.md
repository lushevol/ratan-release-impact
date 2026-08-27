---
type: query
title: What Is the Authoritative Multiple-Exception State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, exception-handling, state-machine, maker-checker, adhoc-ssi]
related: [multiple-cashflow-exception-handling, partial-success-exception-resolution, adhoc-ssi-maker-checker-workflow, cash-settlement-exception-handling, lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# What Is the Authoritative Multiple-Exception State Machine?

The design proposes the exception lifecycle:

```text
PENDING_OPERATOR → PENDING_VERIFICATION → CLOSED
                         ↓
                   PENDING_OPERATOR
```

It also shows cashflow transitions through `WAITING / Pending_Operator`, `WAITING / Pending_Verification`, `READY`, `RELEASED`, and `SETTLED`.

## Questions to resolve

- How is cashflow status derived when exceptions close at different cashflow versions?
- Does a checker reject the whole maker submission or only one exception?
- What is the exact action matrix for a closed `Adhoc SSI` dummy exception?
- How should partial success affect the Camunda task and exception summary?
- Which status spelling is canonical on APIs and in persistence?
- How are already-closed exceptions counted in `Exception_Summary`?
- Who owns the authoritative cashflow transition: Camunda, the Cashflow Lifecycle Service, or a domain service?

This query should be resolved against [[queries/what-is-the-canonical-cash-settlement-exception-state-machine]] and the existing adhoc SSI contracts before the design is marked authoritative.