---
type: concept
title: Stella Transaction Workflow Consistency
created: 2026-08-24
updated: 2026-08-24
tags: [stella, workflow, transaction, consistency]
related: [stella, trade-lake, stella-trade-lake-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Stella Transaction Workflow Consistency

Stella requires all actions for a transaction to use the same transaction workflow.

The source records `TRANSACTION_WORKFLOW_MISMATCH` for a `Release` submitted on workflow `Cash Settlement` where Stella held an existing `Standard Cash Settlement` workflow. It attributes the inconsistency to an earlier `Unnet` that did not synchronize to [[trade-lake]] despite a success acknowledgement.

The authoritative workflow identity and its persistence rules are unresolved.