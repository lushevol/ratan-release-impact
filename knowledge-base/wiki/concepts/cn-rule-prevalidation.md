---
type: concept
title: CN Rule Prevalidation
created: 2026-08-24
updated: 2026-08-24
tags: [cn-rules, validation, nstp, netting, suppression]
related: [ratan-rule-service, ratanone-rule-service, nstp-maker-checker-processing, cashflow-netting, where-are-rule-to-exception-relations-and-nstp-exception-metadata-owned]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# CN Rule Prevalidation

CN Rule Prevalidation describes category-specific guards and enrichment steps recorded for the legacy CN rule path.

- Suppression checks `Cashflow.Is_Cashflow_Unsuppress`.
- Special Rule fetches third-party data.
- IRS and Netting Rules require additional checks before validation.
- NSTP validation does not start if exceptions exist.
- Swift Suppression follows Suppression behavior.

These statements apply to CN-rule processing only. The archived source does not provide conditions, ordering, data contracts, exception-state definitions, or the equivalent target implementation after consolidation.