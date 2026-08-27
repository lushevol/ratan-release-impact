---
type: query
title: How Are Top-Level AND Conditions Preserved in Generated DRL?
created: 2026-08-24
updated: 2026-08-24
tags: [drools, drl, rule-semantics, conjunction, ratan]
related: [dynamic-drl-compilation, drools-rule-language, ratan-rule, ratan-drools-rule, what-is-the-authoritative-ratan-rule-service-api-and-schema-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# How Are Top-Level AND Conditions Preserved in Generated DRL?

The archived design shows a user rule with a top-level conjunction:

```text
Cashflow__Payment_Amount > 2.01 && (Cashflow__Status_Event_Type == "123123" || Cashflow__Status_Event_Type == "aaaabbbb")
```

Its response example emits two independently firing DRL rules: one for the payment amount condition and one for the status-event condition. On its face, that representation permits either component to generate a `MatchedRule`.

The v2 response model also includes `unMatchedRules.matchedSubRules`, suggesting an aggregation or partial-match layer may exist, but the source does not define its truth table or output contract.

## Evidence needed

- Generated DRL and evaluation results for all combinations of the two top-level conditions.
- The implementation that aggregates subrule matches into business-rule matches.
- The authoritative semantics for `matchedRules`, `unMatchedRules`, and `matchedSubRules`.
- Regression tests demonstrating that conjunction and disjunction semantics are retained after compilation.