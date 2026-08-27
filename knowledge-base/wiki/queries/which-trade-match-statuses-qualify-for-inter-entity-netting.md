---
type: query
title: Which Trade Match Statuses Qualify for Inter-Entity Netting?
tags: [trade-match-status, inter-entity-netting, cashflow-auto-netting, netting-eligibility]
related: [trade-match-status-netting-condition, netting-eligibility-rules, auto-netting-rule-management, is-inter-entity-netting-resultant-counterparty-selection-deterministic]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Which Trade Match Statuses Qualify for Inter-Entity Netting?

Trade match status is proposed as a possible condition for inter-entity netting, but qualifying values and operational semantics are not specified.

## Questions to resolve

- What system is authoritative for trade match status?
- Which status values permit, block, or defer netting?
- Must both sides satisfy the same condition?
- How should missing, stale, contradictory, or later-amended statuses be treated?
- Can the condition be safely extended to other counterparty auto-netting rules?

The resulting rule semantics should be recorded in [[trade-match-status-netting-condition]] and governed through [[auto-netting-rule-management]].