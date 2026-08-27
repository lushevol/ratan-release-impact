---
type: query
title: Why Is NOSTRO_MATCHED AutoFail-Eligible but Not Manual-Fail-Eligible?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, autofail, nostro-matched, lifecycle]
related: [ratan-fail-and-autofail-status-transitions, bulk-manual-fail-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail/Bulk Fail Technical Design.md"]
---
# Why Is NOSTRO_MATCHED AutoFail-Eligible but Not Manual-Fail-Eligible?

The documented transition matrix permits `AutoFail` from `NOSTRO_MATCHED` directly to `FAILED`, but does not permit manual `Fail` from `NOSTRO_MATCHED` to `WAITING / Pending Verification / Pending Manual Fail`.

The source gives no rationale. Confirmation is needed on whether this is an intentional operational restriction, a missing manual-fail matrix row, or an obsolete state assumption.