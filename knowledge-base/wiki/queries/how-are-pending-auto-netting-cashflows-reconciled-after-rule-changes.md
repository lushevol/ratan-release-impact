---
type: query
title: How Are Pending Auto Netting Cashflows Reconciled After Rule Changes?
created: 2026-08-22
updated: 2026-08-22
tags: [query, operations, reconciliation, auto-netting, rule-changes, RATAN]
related: [auto-netting-rule-management, cashflow-auto-netting, cashflow-blotter-action-eligibility, data-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# How Are Pending Auto Netting Cashflows Reconciled After Rule Changes?

## Question

How does Ops identify, own, and process cashflows that remain in Pending Auto Netting after the rule that selected them has been updated or deleted?

## Known Requirement

The requirement explicitly excludes refresh and retroactive rule reprocessing. Changes apply only to newly received cashflows. Existing cashflows remain in Pending Auto Netting and must be manually checked by Ops.

## Missing Controls

The source does not define:

- How affected cashflows are identified.
- Whether the old rule association is retained.
- Whether the scheduled job rejects or skips an obsolete association.
- What reconciliation report, alert, or dashboard is provided.
- Which operational team owns the review.
- What SLA or escalation path applies.
- Whether the cashflow is routed to Pending Netting, Pending Exception, or another queue.

## Required Resolution

Confirm the operational workflow and control design before treating the prospective-only rule-change behavior as operationally complete.
