---
type: query
title: When Does is_trade_validated Propagate Bulk Manual STP to Related Group Versions?
tags: [open-question, trade-validation, group-blotter, manual-stp]
related: [trade-validation-gated-group-processing, bulk-manual-stp-for-group-blotter, group-major-version-completion-rules, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2025-changes--38-bulk--4160up]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# When Does is_trade_validated Propagate Bulk Manual STP to Related Group Versions?

Cases 4.1–4.3 imply that an action on `T1_G2_V2` can affect `T1_G3_V3`, with outcomes varying by `is_trade_validated` and the latter record's parent status.

The source does not identify:

- The business or technical relationship between `T1_G2_V2` and `T1_G3_V3`.
- Whether propagation is automatic or selection-driven.
- Why `is_trade_validated=true` advances a child while `PENDING_TRADE_VALIDATION` remains unchanged in case 4.2.
- Why the same flag together with `PENDING_PRE_GROUP` permits parent completion in case 4.3.

Resolve this with the group dependency model, validation-rule definition, and execution evidence for cases 4.1–4.3.