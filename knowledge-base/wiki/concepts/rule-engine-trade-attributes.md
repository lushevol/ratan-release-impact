---
type: concept
title: Rule-Engine Trade Attributes
created: 2026-08-22
updated: 2026-08-22
tags: [rule-engine, trade-attributes, fmrp-uber]
related: [fmrp-uber, ratan-rule-service, ratan-cash-settlement-netting, 51358-ratan-cash-settlement-query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# Rule-Engine Trade Attributes

Rule-engine trade attributes are trade-level data fields exposed to configuration and runtime evaluation so that settlement and netting behavior can be selected by business rules.

## FMRP UBER Expansion

[[chg1016055]] adds ten [[fmrp-uber]] fields across:

- [[51358-ratan-cash-settlement-query-service]] for field retrieval.
- [[ratan-cash-settlement-netting]] for rule inputs.
- [[ratan-rule-service]] for rule configuration and evaluation.
- `51358-mfe-rules` for frontend hierarchy.
- Filter and view builders for operational configuration.

## Validation Limitation

The source confirms the number of added fields but does not enumerate all ten names in text. PIT provides screenshots showing the new attributes, without a machine-readable field inventory or an end-to-end rule-evaluation result.