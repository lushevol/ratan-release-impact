---
type: query
title: What Do operation_level, exception_code, and exception_category Mean in CN Rules?
created: 2026-08-24
updated: 2026-08-24
tags: [exceptions, data-model, nstp, rule-storage]
related: [ratan-rule-service-ratan-rule, cn-rule-service, exception-operation-level, multiple-cashflow-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# What Do operation_level, exception_code, and exception_category Mean in CN Rules?

The archived source states that matching NSTP rules generate exceptions using `operation_level`, `exception_code`, and `exception_category`. It also reports that these fields occur in both `ratan_rule_service.ratan_rule` and `ratan_rule_service.ratan_rule_exception`, while special-rule configuration also contains them.

## Questions

- Is `operation_level` determined by exception type, rule definition, processor output, or another model?
- Are the three fields rule defaults, exception-instance snapshots, or duplicated configuration?
- Which table or component is authoritative for each field?
- Under what conditions may a processor override rule-level metadata?
- How are changes to metadata versioned and audited?

## Evidence needed

Authoritative DDL, entity relationships, rule-processing code, exception creation contracts, and business definitions for each field.