---
type: concept
title: Cashflow Accounting Release
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, accounting, operations, SWIFT_SUPP, READY]
related: [2025-cash-settlement-tranche-1, cashflow-status-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2025 Release Plan/2025 Cash Settlement Tranche 1 Ratan Runbook.md"]
---

# Cashflow Accounting Release

## Definition

Cashflow accounting release is the operational step that makes eligible cashflows available for accounting treatment.

## Procedure specified by the runbook

For May 17, the source lists:

- Release `SWIFT_SUPP`/`READY` cashflows for accounting.
- Bulk unsuppress and then reject `SWIFT_SUPP` cashflows.
- Manually early-release `READY` cashflows.
- Update CPT configuration.

The source does not establish the order, dependencies, approvals, or rollback path for these actions. It also does not clarify whether unsuppress-to-reject is a prerequisite for accounting release or a separate remediation flow.
