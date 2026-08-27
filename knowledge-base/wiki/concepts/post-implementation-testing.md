---
type: concept
title: Post-Implementation Testing
created: 2026-08-22
updated: 2026-08-22
tags: [pit, production-validation, release-management]
related: [production-release-management, release-rollback-readiness, chg1016055, ratan-settlement-korea]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Post-Implementation Testing

Post-implementation testing, or PIT, verifies that a production change has reached the intended state and that critical behavior remains operational.

## Recommended Evidence

Each PIT check should record:

- A unique check identifier.
- Preconditions.
- Exact command, query, or user action.
- Expected result.
- Actual result.
- Pass/fail status.
- Executor.
- Execution timestamp.
- Evidence location.
- Follow-up action for failures or deviations.

## CHG1016055 Coverage

The [[chg1016055]] PIT plan covers application properties, static data, Nostro data, EBBS records, SWIFT data, auto-netting, rule records, accounting schema metadata, routing, trade attributes, frontend entities and currencies, dashboard filtering, warning behavior, and rule versions.

## Evidence Limitation

Many actual-result cells are blank, while screenshots carry the evidence. This weakens searchability, comparison, and auditability. The unresolved completion status is tracked by [[did-all-chg1016055-pit-checks-pass]].