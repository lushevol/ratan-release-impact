---
type: entity
title: Adhoc SI
created: 2026-08-23
updated: 2026-08-23
tags: [Adhoc-SI, SSI, exception, cash-settlement]
related: [ssi, adhoc-ssi-workflow, ssi-exception-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# Adhoc SI

Adhoc SI is the exceptional or manually supplied standing instruction classification used in the SSI workflow.

The source represents this classification through `SSI Exception Type = Adhoc SI`. A maker action can create or advance the classification, while a checker can approve or reject the associated input.

For a `WAITING` cashflow, checker approval changes the primary status to `READY` and changes the SSI exception type to `NA`. Checker rejection preserves `Adhoc SI` in the explicitly specified `WAITING` rejection paths and returns the sub-status to `Pending Operator`.

The source does not define whether `Adhoc SI` is persisted as a literal value, whether it represents a specific SSI payload, or what notification is sent when the classification changes.