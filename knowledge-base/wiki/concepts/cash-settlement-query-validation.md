---
type: concept
title: Cash Settlement Query Validation
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, query-validation, quick-search, custom-filter, frontend]
related: [cash-settlement-home-page, cash-settlement-filter-operator-allowlists, reversible-cashflow-query-ui-state, lms-cashflow-lifecycle-message-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Cash Settlement Query Validation

Cash Settlement Query Validation is the set of front-end rules governing quick-search combinations and custom-filter definitions on the [[cash-settlement-home-page]].

## Quick Search Rules

The requirement identifies the following as passing or intended behaviors:

- `Cashflowid / trade id`
- `trade original id`
- `Value date + booking entity fmid`
- `Value date + booking entity fmcode`
- `Value date + counterparty fmid`
- `Value date + counterparty fmcode`
- Multiple-value Cashflow State search without a stated validation rule

Value date is described as mandatory, while searches with neither booking entity nor counterparty must be refused. The source does not clarify whether those restrictions apply to direct identifier searches.

Cashflow Sub State may be added only after user confirmation.

## Custom-Filter Rules

Payment date, booking entity FMID, and cashflow state may be combined in a passing filter. Operator restrictions are defined in [[cash-settlement-filter-operator-allowlists]]. Fields ending in `_id` are described as bypassing validation, but the meaning of that bypass is unresolved.

## Invalid Filter Lifecycle

When a user selects or opens a custom filter, validation runs and a failure message is shown if validation fails. The failed filter remains visible and may be deleted. It cannot be saved, created, or searched.

This separates filter visibility and deletion from filter persistence and execution.

## Scope Boundary

These are UI query-validation rules. They should not be treated as definitions of cashflow lifecycle eligibility, STP authorization, settlement posting, or downstream LMS behavior.