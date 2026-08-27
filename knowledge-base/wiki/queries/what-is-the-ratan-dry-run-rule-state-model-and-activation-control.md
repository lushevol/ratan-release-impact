---
type: query
title: What Is the RATAN Dry-Run Rule State Model and Activation Control?
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, dry-run, rule-lifecycle, state-model]
related: [ratan-rule-lifecycle-management, rule-service, business-rule-maintenance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md"]
---
# What Is the RATAN Dry-Run Rule State Model and Activation Control?

The guide describes dry-run rules as rules that do not execute immediately and says that a user with operate permission can activate an existing dry-run live rule. The phrase “dry-run live rule” does not identify a clear state.

The authoritative state model should define:

- Whether dry-run is a lifecycle state, execution mode, or approval status.
- Which transitions are permitted.
- Whether activation requires Maker/Checker approval.
- Whether activation takes effect immediately in UAT, production, or both.
- How activation and disablement are recorded in history.

## Related evidence

- [[entities/rule-service]]
- [[concepts/ratan-rule-lifecycle-management]]