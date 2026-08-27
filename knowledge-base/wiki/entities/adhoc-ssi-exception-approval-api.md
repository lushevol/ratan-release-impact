---
type: entity
title: Adhoc SSI Exception Approval API
created: 2026-08-23
updated: 2026-08-23
tags: [api, adhoc-ssi, checker, approval, maker-checker]
related: [adhoc-ssi-maker-input-api, manual-swift-tag-70-and-72-flags, adhoc-ssi-api, cashflow-amendment-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# Adhoc SSI Exception Approval API

`/v2/stamping/exception/{exceptionId}/approve` approves an Adhoc SSI exception.

For `fitVostro`, `manualTag70` and `manualTag72` must match the values in the stashed `Maker_Request_Body`. On approval, the values are persisted to the cashflow's `Settlement_Instruction` as `Manual_Tag_70` and `Manual_Tag_72`.

The source requires equality but does not prescribe whether the API rejects a mismatch, ignores approval-supplied values and copies the stashed values, or uses another enforcement mechanism.