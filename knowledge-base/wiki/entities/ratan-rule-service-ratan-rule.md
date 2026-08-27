---
type: entity
title: ratan_rule_service.ratan_rule
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, rule-storage, cn-rule-service, schema]
related: [cn-rule-service, cached-rule-loading, drools-based-nstp-rule-evaluation, what-do-operation-level-exception-code-and-exception-category-mean-in-cn-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# ratan_rule_service.ratan_rule

`ratan_rule_service.ratan_rule` is described as the consolidated rule repository for CN Rule Service. The archived source states that it replaced `ratanone.ratan_suppression_rule` and stores IRS, suppression, SWIFT suppression, netting, and NSTP rules.

## Reported schema changes

Relative to `ratanone.ratan_suppression_rule`, the source reports these additions:

```text
created_by
updated_by
operation_level
exception_code
exception_category
```

It reports these removals:

```text
creator
last_modifier
approver
approve_time
hierarchy
value_date
```

No DDL, types, keys, constraints, indexes, or nullability definitions were provided.

## Exception metadata ambiguity

The source reports that `operation_level`, `exception_code`, and `exception_category` also exist in `ratan_rule_service.ratan_rule_exception`. It does not establish whether these values are rule defaults, generated exception snapshots, shared configuration, or duplicated data with separate ownership.

`ratan_rule_service.ratan_special_rule_config` is said to contain `business_workflow`, `rule_type`, `exception_code`, `exception_category`, `operation_level`, and `processor`, adding another potential source of exception metadata.

See [[what-do-operation-level-exception-code-and-exception-category-mean-in-cn-rules]] for the unresolved ownership model.