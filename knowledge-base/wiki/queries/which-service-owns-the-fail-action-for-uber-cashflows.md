---
type: query
title: Which Service Owns the Fail Action for Uber Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, fail-action, orchestration, lifecycle, action-ownership]
related: [uber-restructured-workflow-integration, orchestration, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# Which Service Owns the Fail Action for Uber Cashflows?

The action inventory assigns `Fail` to the UI but lists both its API provider and comments as `??`. A separate case note says the orchestration status-update API needs change for Manual Fail/Reinstate.

## Why this matters

Without a named owner and endpoint, the action cannot be reliably tested for authorization, state-transition validity, event emission, processing-message publication, idempotency, or recovery.

## Resolution criteria

Assign one accountable service and publish the canonical API, permitted source states, target state, maker-checker requirements, event and message publication behaviour, audit fields, and failure/retry semantics for Uber cashflows.