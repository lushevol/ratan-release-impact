---
type: concept
title: Cross-Rule Netting Isolation
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, rule-management, aggregation, eligibility]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-eligibility-rules, netting-scenario-priority, pending-auto-netting-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Business user case testing.md"]
---
# Cross-Rule Netting Isolation

Cross-rule netting isolation is the boundary that prevents cashflows assigned to different auto-netting rules from being aggregated into one resultant.

## Test evidence

AC-Settlement-AutoNetting-008 configured two approved bilateral rules with the same booking entity and counterparty but different products:

```text
Rule1: Product A
Rule2: Product B
Netting date: VD-1
STP level: CHECKER_ONLY
Netting type: Bilateral Netting
```

The test cashflows were:

```text
C1: M00015720031
     Product: COM|SWAP
     Payment date: 2025-06-10

C2: M00015720032
     Product: IRD|IRS
     Payment date: 2025-06-10
```

Both cashflows entered `WAITING / Pending Auto Netting`, were affirmed, received the `CHECKER_ONLY` NSTP exception, and were released individually. They were not combined across rules.

## Implication

Matching common attributes such as currency, payment date, booking entity, and counterparty is insufficient for aggregation when rule membership differs. Rule identity or the selected rule assignment is therefore part of the aggregation boundary.

This finding should be distinguished from the unresolved precedence question in [[concepts/netting-scenario-priority]]: isolation describes what happens after cashflows are associated with different rules, while precedence determines which rule is selected when multiple rules match the same cashflow.