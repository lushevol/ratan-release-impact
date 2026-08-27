---
type: query
title: Does Value Date Apply to ID-Based Quick Searches?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, quick-search, value-date, requirements-ambiguity]
related: [cash-settlement-query-validation, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Quick Search & Custom Filter FE Query Validation.md"]
---

# Does Value Date Apply to ID-Based Quick Searches?

Does the requirement that value date “must be mandatory” apply to direct `Cashflowid`, trade ID, and trade original ID searches?

## Evidence

The source separately lists cashflow/trade identifier searches as passing or bypassing, while also requiring value date and refusing searches with neither booking entity nor counterparty. It does not state whether identifier lookups are exempt from the value-date and party-context rules.

## Decision Needed

Confirm the validation matrix for:

- `Cashflowid` or trade ID alone
- Trade original ID alone
- Identifier plus value date
- Identifier plus booking entity or counterparty
- Value date without either booking entity or counterparty

Until clarified, the implementation should not infer that direct identifier searches either require or exclude party context.