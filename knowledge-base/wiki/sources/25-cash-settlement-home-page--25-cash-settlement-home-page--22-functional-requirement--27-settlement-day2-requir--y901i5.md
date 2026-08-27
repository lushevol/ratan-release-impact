---
type: source
title: Cashflow Auto Netting Enhancement Requirements
authors: []
year: 2026
url: ""
venue: Internal functional requirements document
tags: [cashflow-auto-netting, settlement-day2, functional-requirements, inter-entity-netting, rebook-cashflow, trade-match-status]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-eligibility-rules, pending-confirmation-affirmation, released-resultant-amendment-handling, rebook-cashflow-netting-exclusion, trade-match-status-netting-condition]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Cashflow Auto Netting Enhancement Requirements

This functional requirements document proposes four changes or assessments for [[cashflow-auto-netting]]. It distinguishes concerns that should remain separate: netting eligibility, resultant lifecycle handling, and post-netting affirmation workflow.

## Preserved requirements

```text
1. Remove auto affirmation from auto netting
2. exclude rebook cashflow from auto netting rule (TBC: if only applicable to inter entity netting or other auto netting rules)
3. for the scenario that one side netting resultant has been released, the amendment happened on the other side will not have rebook exception - solution TBC
4. for inter entity netting, need to check if possible to add trade match status as a rule condition, to be assessed if this can be applicable for other counterparty auto netting rules.
```

## Interpretation and status

- Auto affirmation is to be removed from the auto-netting process. The replacement affirmation process, affected scenarios, and release implications are not specified.
- Rebook cashflows are to be excluded from auto-netting rule matching. Whether this applies only to inter-entity netting or all auto-netting rules is explicitly TBC.
- When one side of a netting resultant is released and the opposite side is amended, a rebook exception should not be raised. The required lifecycle remediation is TBC; suppression alone does not establish how the economic or operational difference is handled.
- Trade match status is proposed as a candidate eligibility condition for inter-entity netting. Feasibility, qualifying statuses, missing-data behavior, and applicability to other counterparty rules require assessment.

## Related wiki material

The requirements extend [[auto-netting-rule-management]] and [[netting-eligibility-rules]]. The released-resultant scenario should be assessed against [[netting-resultant-cashflow-lifecycle]] and [[netting-un-net-lifecycle]]. Removal of auto affirmation is related to [[pending-confirmation-affirmation]] and [[ratan-cashflow-lifecycle-state-machine]].