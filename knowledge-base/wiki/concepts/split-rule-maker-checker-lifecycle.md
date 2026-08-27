---
type: concept
title: Split Rule Maker-Checker Lifecycle
tags: [cashflow-splitting, static-data, maker-checker, audit, rules]
related: [nostro-threshold-static-data, nostro-threshold-splitting-algorithm, cashflow-auto-distribution, what-are-the-authoritative-split-rule-formula-rounding-and-child-count-limits]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Split Rule Maker-Checker Lifecycle

Split rules are static-data records used to govern automatic cashflow splitting. The documented APIs support create, update, confirmation, rejection, deletion, querying, and audit retrieval.

Rules are scoped by `entityFmId`, `nostroAgent`, and `currency`; `entityFmId` and `nostroAgent` can use the wildcard value `ALL`. Their documented numeric-text fields are `threshold`, `amount`, and `limitation`. Query results include maker/checker identities, timestamps, `referenceId`, and `dataStatus`.

Observed statuses include `SAVE_CONFIRMED`, `DELETE_PENDING`, and `DISCARDED`. The source provides no complete state machine, authorization model, or formal definition for `limitation`.

UAT demonstrated that a rule with `threshold: 1000`, `amount: 100`, and `limitation: 200` applied to a cashflow of approximately `10000000` could attempt excessive child creation and fail. This supports validation before approval and execution, but the actual child-count limit is not documented.