---
type: concept
title: FXU-RATAN Utilization Exception Routing
created: 2026-08-23
updated: 2026-08-23
tags: [fxu, ratan, utilization, exception-management, operations]
related: [fxu, ratan, fmo-ops, tb-ops, oscar, fxu-ratan-utilization-response-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Util Response ACK NACK.md"]
---
# FXU-RATAN Utilization Exception Routing

The documented default handling for a RATAN `NACK` is for [[fxu]] to place the request in the FMO Exception queue for [[fmo-ops]] investigation.

## Assigned Follow-Up Paths

- For out-of-scope, amended, or cancelled trades, [[tb-ops]] is expected to coordinate with FMO and obtain a replacement Contract ID or Contract Number from the client or Sales.
- For RATAN internal errors, FMO escalates to RATAN PSS.
- For invalid cashflow count or error-cashflow cases, FMO monitors RATAN errors and may manually process through [[oscar]].
- For `MISSING_INFO`, marked Phase 2, the FMO Investigation team is directed to correct the item in the RATAN Exception Queue.

## Gaps

The source does not identify queue names, terminal statuses, service-level targets, ownership of retries, or acknowledgement and reconciliation rules. It therefore documents intended operating routing rather than a complete operational runbook.