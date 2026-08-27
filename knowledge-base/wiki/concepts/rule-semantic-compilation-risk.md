---
type: concept
title: Rule Semantic Compilation Risk
tags: [drools, rule-engine, correctness, validation, cash-settlement]
related: [ratan-rule-service, ratan-suspended-cashflow-rule-filtering, how-is-ratan-suspended-rule-conjunction-evaluated]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# Rule Semantic Compilation Risk

Rule semantic compilation risk arises when a source expression and its executable representation can produce different truth conditions.

The `RATAN_SUSPENDED` user rule `7444684846945615873333` joins its eligibility clauses with `&&`, meaning every clause must hold. Its supplied Drools representation instead defines independent rules (`...-0` through `...-14`) that add individual results to `matchedRuleSet`.

If the suspension endpoint treats any `matchedRules` entry as an overall match, cashflows satisfying only a subset of conditions could be incorrectly suspended. Correctness requires an explicit aggregation contract, such as requiring every component rule ID or evaluating the original conjunction as a whole.