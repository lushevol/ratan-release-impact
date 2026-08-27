---
type: entity
title: ratanone-db-repository
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, database, repository, suppression-fields, cash-settlement]
related: [ratan, ratan-rule-service, cashflow-suppression-rule, hard-blocker-go-live-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# ratanone-db-repository

`ratanone-db-repository` is the repository component listed in the hard-blocker back-end deployment checklist. No required version is specified.

The associated validation checks the presence and activated versions of suppression-field configuration records in the `ratan_rule_service` schema:

- `ratan_suppression_fields_config`: `a770a624-b4dd-4dfd-bf41-d889cf78222f`
- `ratan_suppression_fields`: `069b1939-577f-47d4-8253-901e89d40777`
- `ratan_suppression_fields_xpath`: `5bfa098c-1142-4764-9ee8-996cf3f0b61f`

The source provides validation SQL but no results or repository deployment evidence.