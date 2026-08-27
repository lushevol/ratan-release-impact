---
type: query
title: What Controls Govern Force-STP for Incomplete Cashflow Groups?
created: 2026-08-22
updated: 2026-08-22
tags: [force-stp, cashflow, group-management, controls, workflow]
related: [cashflow-group-completeness-gating, ratan-cash-settlement-group-management-service, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# What Controls Govern Force-STP for Incomplete Cashflow Groups?

The design permits rare manual force-STP where a group is incomplete because a message is lost or a leg is missing.

## Evidence needed

- The required-leg model and completeness algorithm
- Timeout and missing-message detection rules
- Authorized users and any maker/checker approval
- Idempotency and duplicate-message controls
- Audit records, compensating actions, and reconciliation procedures

Without these controls, force-STP remains an incompletely specified exception path.