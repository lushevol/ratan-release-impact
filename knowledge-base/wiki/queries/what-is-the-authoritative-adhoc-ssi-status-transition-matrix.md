---
type: query
title: What Is the Authoritative Adhoc SSI Status Transition Matrix?
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, Adhoc-SI, status-transition, open-question]
related: [adhoc-ssi-workflow, ssi-exception-state-model, maker-checker-ssi-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# What Is the Authoritative Adhoc SSI Status Transition Matrix?

The source provides status/action rows for Adhoc SSI processing, but several field semantics and transition details require confirmation.

## Questions to resolve

1. Are `READY` and `Ready` the same status enumeration?
2. Does `NA` mean a persisted literal value, null, empty string, or display placeholder?
3. What precisely distinguishes `Maker Adhoc SSI` from `Maker Input Adhoc SSI`?
4. Should checker rejection from `READY` restore `SSI Exception Type` to `Adhoc SI`?
5. Can a cashflow remain operationally `READY` while carrying `Pending Exception`?
6. Which blank target fields mean cleared values, unchanged values, or unspecified behavior?
7. What are the server-side permissions and validation rules for maker and checker actions?

The explicit `WAITING` approval path is comparatively clear: `Checker Approve` changes the cashflow to `READY` and clears the pending exception fields. The `READY` paths are less complete and should not be normalized without confirmation.