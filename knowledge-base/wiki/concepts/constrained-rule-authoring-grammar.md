---
type: concept
title: Constrained Rule Authoring Grammar
created: 2026-08-24
updated: 2026-08-24
tags: [rule-authoring, grammar, drools, frontend-validation]
related: [ratan-rule-engine, drools]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# Constrained Rule Authoring Grammar

## Definition

The proposed RATAN rule-authoring grammar restricts boolean expressions to simplify front-end validation and back-end DRL generation:

1. A rule uses only `&&` when no group is present.
2. `||` is permitted only inside a group.
3. Separate rule definitions have an implicit “or” relationship.

## Examples

Permitted:

```text
Cashflow.Payment_Amount == 100
&&
Cashflow.Payment_Currency in ('USD', 'CNY')
&&
(Cashflow.Payment_Date == '2024-01-27' || Cashflow.STP_Cutoff_Date_Time == '2024-01-27 17:19:27')
```

Forbidden:

```text
Cashflow.Payment_Amount == 100
||
Cashflow.Payment_Currency in ('USD', 'CNY')
```

## Model synchronization

Rule paths are represented using logical-model fields. The proposed generator converts dot notation such as `Cashflow.Payment_Amount` into `Cashflow__Payment_Amount`. The front end and back end must therefore remain synchronized with the DM logical model.

The archived source does not provide a parser grammar, validation API, error semantics, or versioning policy.