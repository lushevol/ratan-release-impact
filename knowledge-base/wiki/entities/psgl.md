---
type: entity
title: PSGL
created: 2026-08-22
updated: 2026-08-22
tags: [PSGL, accounting, cash-settlement, migration]
related: [ebbs, tlm, razor, murex-ratan-migration-reconciliation, cashflow-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# PSGL

PSGL is identified in the cashflow migration runbook as a downstream accounting system in the planned reconciliation path.

## Role in the Runbook

The planned flow was:

```text
Razor accounting -> EBBS/PSGL -> TLM EOD & reconciliation
```

The source does not define PSGL interfaces, ownership, control totals, or acceptance criteria. Its inclusion in the runbook establishes a downstream dependency, not evidence that PSGL processing was completed successfully.