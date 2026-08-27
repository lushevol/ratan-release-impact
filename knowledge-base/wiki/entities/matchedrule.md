---
type: entity
title: MatchedRule
created: 2026-08-23
updated: 2026-08-23
tags: [drools, rule-engine, cashflow, auto-netting]
related: [drools, enhancedfact, auto-netting-rule-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# MatchedRule

`MatchedRule` is the result model instantiated by the documented Java-dialect Drools scripts when an [[enhancedfact|EnhancedFact]] satisfies an `AUTO_NETTING` rule.

The examples set a rule identifier and the user-rule expression as the match reason before adding the result to `matchedRuleSet`:

```java
MatchedRule matchedRule = new MatchedRule();
matchedRule.setRuleId("7341393701123698688-0");
matchedRule.setReason("BCS_Trade_Id == \"1233\"");
matchedRuleSet.add(matchedRule);
```

The source does not specify downstream consumers of `matchedRuleSet` or the complete `MatchedRule` data model.