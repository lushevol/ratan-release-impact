---
type: entity
title: EnhancedFact
created: 2026-08-23
updated: 2026-08-23
tags: [drools, fact-model, cashflow, auto-netting]
related: [drools, matchedrule, auto-netting-rule-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# EnhancedFact

`EnhancedFact` is the Drools fact model matched by the documented `AUTO_NETTING` rule scripts.

The examples evaluate the `BCS_Trade_Id` field, such as:

```java
EnhancedFact( BCS_Trade_Id == "1233" )
```

A successful match causes the script to create and add a [[matchedrule|MatchedRule]] to the global `matchedRuleSet`. The source does not define the full `EnhancedFact` schema or the permitted set of user-rule fields and operators.