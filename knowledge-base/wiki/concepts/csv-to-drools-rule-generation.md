---
type: concept
title: CSV-to-Drools Rule Generation
created: 2026-08-24
updated: 2026-08-24
tags: [csv, drools, rule-generation, rule-onboarding, governance]
related: [drools, drools-rule-language, rule-service, rule-service-migration, rule-governance-and-auditability, what-rule-auditability-and-approval-controls-does-cash-settlement-require]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]
---
# CSV-to-Drools Rule Generation

CSV-to-Drools rule generation is a planned onboarding workflow recorded in an archived 2023 delivery plan: the BAU team would provide existing rules in CSV format, @Lin Liang would generate corresponding [[drools]] rules, and BAU testing would start after all rules were imported.

The source establishes this as a planned workflow only. It does not provide a CSV schema, transformation implementation, DRL templates, equivalence tests, approval process, versioning model, or evidence that rule import and testing completed.

A production-grade conversion process requires traceability from source CSV rows to generated rules, business review of generated behavior, test evidence, controlled releases, and rollback capability. The delivery plan does not specify these controls; they remain relevant to [[rule-governance-and-auditability]].