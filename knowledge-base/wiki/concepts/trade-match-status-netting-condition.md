---
type: concept
title: Trade Match Status Netting Condition
tags: [cashflow-auto-netting, inter-entity-netting, trade-match-status, netting-eligibility, rule-management]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-eligibility-rules, is-inter-entity-netting-resultant-counterparty-selection-deterministic, which-trade-match-statuses-qualify-for-inter-entity-netting]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Trade Match Status Netting Condition

Trade match status netting condition is a proposed eligibility predicate for inter-entity [[cashflow-auto-netting]] rules.

## Assessment request

The source requests an assessment of whether trade match status can be included as a rule condition for inter-entity netting. It also asks whether the condition could be applied to other counterparty auto-netting rules. This is a feasibility request, not an approved universal rule condition.

## Required definition before adoption

An implementation assessment should establish:

- the canonical source and values of trade match status;
- qualifying and disqualifying statuses;
- whether both sides of an inter-entity relationship must qualify;
- availability and freshness of status during rule evaluation;
- handling of missing, stale, or contradictory values;
- behavior when status changes after a cashflow has been netted; and
- effects on rule precedence and existing rule reachability.

The condition extends [[netting-eligibility-rules]] and should be governed through [[auto-netting-rule-management]].