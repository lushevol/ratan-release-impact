---
type: concept
title: Past-Due Accounting Reversal
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, past-due, accounting, reversal, settlement-method]
related: [utilization-service, gross-util-settlement-method-transition, cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# Past-Due Accounting Reversal

The draft requires an immediate past-due accounting reversal when a manual settlement-method change moves a cashflow from `UTIL` to `GROSS` and past-due accounting exists.

Utilization Service is identified as the component responsible for handling this reversal. The document does not specify the reversal event schema, accounting owner, duplicate-prevention mechanism, ordering relative to settlement-method updates, or rollback behavior if either the update or reversal fails.

This is a conditional side effect of the transition described in [[gross-util-settlement-method-transition]], rather than a general rule for all cashflow changes.