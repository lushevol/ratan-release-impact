---
type: concept
title: Cashflow Monitoring
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, monitoring, release-validation, cash-settlement]
related: [2025-cash-settlement-tranche-1, murex, nds-auto-netting, cashflow-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2025 Release Plan/2025 Cash Settlement Tranche 1 Ratan Runbook.md"]
---

# Cashflow Monitoring

## Definition

Cashflow monitoring is the post-publication validation of counts, statuses, rule behavior, flags, and product attributes during a staged cash settlement release.

## Application in the runbook

After [[Murex]] pushes the controlled CPT tranche, the runbook assigns monitoring to [[Lina Feng]]. The checklist covers:

- Cashflow numbers.
- Cashflow status.
- Rule behavior.
- The pending state of [[NDS Auto Netting]].
- Commodity flag presence.
- Pending fixing flag presence.
- `Swap Agent`/`RFR` behavior.

The runbook does not define expected values or acceptance thresholds. Monitoring should therefore be treated as a planned control rather than evidence of successful validation.
