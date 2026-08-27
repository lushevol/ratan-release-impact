---
type: query
title: Was the SFX Migration-Weekend NSTP Hold Approved, Deployed, and Removed?
created: 2026-08-23
updated: 2026-08-23
tags: [sfx, nstp, migration-weekend, partial-stp, control-validation]
related: [sfx, ratan, migration-weekend-lifecycle-event-control, fmrp-trade-attribute-cashflow-nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md"]
---
# Was the SFX Migration-Weekend NSTP Hold Approved, Deployed, and Removed?

The SFX support notes proposed an NSTP rule to hold all unaffirmed cashflows during the migration weekend because partial STP was enabled in the BCS flow. The rule was intended to be removed after migration.

The source does not show whether the control was approved, deployed, tested against partial-STP behavior, monitored during the migration window, or removed afterward.

## Evidence needed

- Approval of the control scope and migration-window duration.
- Configuration or deployment evidence for the NSTP rule.
- Test evidence showing partial STP did not bypass the hold.
- Operations monitoring and exception-handling evidence.
- Confirmation that the rule was removed and that normal processing resumed.