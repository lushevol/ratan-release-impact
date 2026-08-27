---
type: concept
title: Cashflow Auto-Split Failure
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-split, failure-handling, techfail, autosplitfail, recovery]
related: [cashflow-auto-distribution, nostro-threshold-static-data, ratan-fail-and-autofail-status-transitions, cashflow-pre-fail-state-restoration, held-cashflow-reinstatement, cashflow-withdrawal-during-split-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Cashflow Auto-Split Failure

Cashflow auto-split failure is the proposed handling for an unrecoverable threshold-splitting condition, particularly when `deductAmount` becomes less than `1`.

## Original proposal

The original design proposed:

```text
exception -> READY+NA+Pending_Exception
action = AutoSplitFail
```

The expected operational recovery was:

1. Correct the Nostro threshold static configuration.
2. Perform manual fail.
3. Reinstate the cashflow.

## Recommended workflow

The design recommends reusing the existing `TechFail` action rather than creating or extending `AutoSplitFail`. The reasons are production maturity, user familiarity, and reduced cross-system change.

The proposed enhancement is to add the required comment and result information to the existing `TechFail` flow. The source does not specify the exact status transition, result schema, audit record, or downstream notification contract.

## Risks

Reusing `TechFail` may obscure the distinction between a technical processing failure and invalid or pathological static configuration. The workflow must also preserve the original cashflow, support correction and reinstatement, and remain compatible with withdrawal processing.

See [[cashflow-withdrawal-during-split-failure]] for the unresolved withdrawal lifecycle issue.