---
type: query
title: Should Trade Validation Gating Belong to the Group or Lifecycle Service?
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, service-ownership, trade-validation, cash-settlement]
related: [trade-validation-gating, group-level-trade-validation-hold, ratan-cashflow-standardization-service, ratan-cashflow-lifecycle-service, cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# Should Trade Validation Gating Belong to the Group or Lifecycle Service?

The design leaves unresolved whether trade-validation gating belongs in the Group service or the Lifecycle service.

## Option 1: Group-service gate

The preferred Option 1 adds a hold control to the Group service and publishes to workflow only after group completion and trade validation. It avoids changing the main lifecycle workflow but expands the Group service into progression control.

## Option 2: Lifecycle-service gate

Option 2 adds `TOBEVALIDATED` before `PROJECTED` and makes the Lifecycle service query the Group service. It offers clearer cashflow status visibility and a more explicit lifecycle ownership boundary, but changes the main workflow and increases regression effort.

## Decision criteria

Resolution should address:

- Which service owns the authoritative transition guard.
- Whether validation is represented at group level, cashflow level, or both.
- Who releases a group after late validation.
- How `Manual STP`, LIEN STP, withdrawals, and amendments are controlled.
- Which service owns audit records and operational dashboards.
- How duplicate, delayed, corrected, or regressed TDS3 statuses are handled.

The source records Option 1 as preferred on 2024-05-29, but does not constitute a final architectural decision.
