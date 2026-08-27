---
type: concept
title: DRL Pattern Constraints
created: 2026-08-24
updated: 2026-08-24
tags: [drools, drl, rule-authoring, pattern-matching]
related: [drools, dynamic-drl-compilation, what-is-the-authoritative-suppression-rule-language-and-governance-model, which-drools-dialect-and-version-support-the-required-null-navigation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# DRL Pattern Constraints

DRL pattern constraints express predicates over matched facts. The archived exploration describes Java-like comparisons along with Drools-specific behavior and operators.

## Documented capabilities

- `>, >=, <, <=` support ordering; for `Date`, `<` means before, and for `String`, `<` means alphabetically before.
- `==` and `!=` provide null-safe equality and non-equality semantics analogous to `equals()` and negated equality.
- `&&` and `||` support abbreviated combined relation conditions over a common field, such as `Person (age > 30 && < 40)`.
- `matches` and `not matches` evaluate Java regular expressions.
- `contains` and `not contains` apply to Arrays, Collections, and string containment checks.
- `memberOf` and `not memberOf` evaluate membership in a variable-defined Array or Collection.
- `in` and the source's `notin` / `not in` terminology support multi-value restrictions.

The exact grammar and operator behavior must be validated against the selected Drools release and dialect. The source does not specify a Drools version and contains inconsistent spelling for the negative `in` operator.