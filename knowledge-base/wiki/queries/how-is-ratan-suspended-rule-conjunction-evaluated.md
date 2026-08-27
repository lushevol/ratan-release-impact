---
type: query
title: How Is Ratan SUSPENDED Rule Conjunction Evaluated?
tags: [open-question, ratan, drools, rule-engine, correctness]
related: [ratan-rule-service, ratan-suspended-cashflow-rule-filtering, rule-semantic-compilation-risk]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# How Is Ratan SUSPENDED Rule Conjunction Evaluated?

Rule `7444684846945615873333` is written as a conjunction, while its supplied Drools `running_rule` has separately firing component rules that populate `matchedRuleSet`.

Determine whether `/v1/ratanSuspendedRule/check`:

- Requires all component rule IDs to match.
- Evaluates `user_rule` as a complete expression.
- Uses an omitted grouping or aggregation mechanism.
- Treats any `MatchedRule` as a successful suspension match.

Also validate whether `§Entity__Counterparty_SCI_FMID` is an intentional parser construct or a transcription error.

A test matrix should include cases matching only one clause, all but one clause, every clause, and each exclusion branch.