---
type: query
title: How Are Past-Value-Date Murex Reversals Reconciled in RATAN?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, reversal, settlement-risk, reconciliation]
related: [murex-cashflow-status-lifecycle, murex-cashflow-migration-to-ratan, murex-to-ratan-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# How Are Past-Value-Date Murex Reversals Reconciled in RATAN?

For a post-migration `SNTR/RLSR` cashflow, a Murex trade event can create a reversal with a value date in the past. The source states that Murex will not send such a reversal to RATAN and that Operations will handle it manually under BAU.

This can leave RATAN showing the original cashflow as settled even though Murex has cancelled it. The source identifies the issue but does not define a reconciliation, status-correction, or settlement-prevention control.

Needed confirmation:

- Whether RATAN receives a status-only cancellation or another corrective event.
- Which system is authoritative for historical settlement state.
- How Operations evidence manual resolution and reconcile it to RATAN.
- Whether the control also covers a future-dated replacement that can otherwise create duplicate-payment risk.