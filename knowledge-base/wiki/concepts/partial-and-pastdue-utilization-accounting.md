---
type: concept
title: Partial and PastDue Utilization Accounting
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, partial-utilization, pastdue, fx-utilization]
related: [ratan, ebbs, bridge-account, utilization-remaining-amount, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# Partial and PastDue Utilization Accounting

Partial and PastDue utilization accounting is a proposed Phase 2 model for moving utilized value through FXBRREC and residual value through a Past Due Account.

The high-level design states:

- Full or partial utilization: CR Bridge Account and DR FXBRREC Account for the utilized amount.
- PastDue settlement: move remaining amount between Bridge Account and Past Due Account at the entity-configured cutoff.
- Post-PastDue utilization: reverse the Past Due position, then post the new utilization.
- Utilization reversal: reverse the original Bridge/FXBRREC entries and restore remaining amount.

RATAN is intended to send accounting to [[ebbs]] in real time, with reconciliation in [[tlm]]. Debit/credit direction differs across some examples, and sample cashflow 102 is SAR while its accounting entries use ZAR. This is design evidence, not approved accounting policy. See [[what-is-the-authoritative-pastdue-and-auto-utilization-accounting-model]].