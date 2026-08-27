---
type: concept
title: NSTP Rule Routing
created: 2026-08-23
updated: 2026-08-23
tags: [nstp, exceptions, static-data, maker-checker, settlement]
related: [cashflow-suppression-rules, cashflow-amendment-maker-checker-control, inter-entity-cashflow-stp, cashflow-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# NSTP Rule Routing

NSTP rules are configurable conditions that route matching cashflows to operational exceptions. Each rule associates a condition with an Exception Code, Operation Level, and Exception Category.

## Routing Dimensions

- **Exception Code** identifies the business or operational exception.
- **Operation Level** identifies the required actor, including `MAKER_CHECKER`, `CHECKER_ONLY`, and `MAKER_ONLY`.
- **Exception Category** classifies the route, including `NSTP`, `HIGH_RISK_NSTP`, `AFFIRMATION`, `BACK_VALUE`, and `OTHER`.

The source covers settlement method, manual delivery, amendment errors, reinstatement, netting states, settle-as-gross, ad hoc netting, withdrawals on components, product and strategy conditions, client policies, and event reasons.

## Governance

NSTP rule creation, update, and deletion use Maker/Checker maintenance. The source does not define rule precedence, whether multiple matching rules accumulate, or how a later rule changes an earlier one.

## Ambiguous Event Routing

`Reversal` and `Rebook` appear both as `CHECKER_ONLY` / `HIGH_RISK_NSTP` rules and as `MAKER_ONLY` / `NSTP` rules. This conflict requires resolution before the inventory can be treated as an authoritative executable specification. Track it in [[what-is-the-nstp-rule-precedence-for-reversal-and-rebook]].

Blank-condition rows for Bad Business Day, High Value Payment, GSAM Client, Pending Affirmation, Corporate Client, and Back Value Date also require clarification.