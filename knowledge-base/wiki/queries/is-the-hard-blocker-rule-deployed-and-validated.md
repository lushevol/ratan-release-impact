---
type: query
title: Is the Hard Blocker Rule Deployed and Validated?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, go-live, hard-blocker, deployment-validation, ratan]
related: [hard-blocker-go-live-checklist, hard-blocker-exception, ratan-rule-service, ratanone-rule-service, ratan-cash-settlement-netting-service, ratanone-db-repository]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# Is the Hard Blocker Rule Deployed and Validated?

The source specifies required service versions and database checks but does not record execution results or sign-off.

## Evidence required

- Confirmation that `ratan-cash-settlement-netting-service` is version `1.5.7`.
- Confirmation that `ratanone-rule-service` is version `2.3.11`.
- Confirmation that `ratan-rule-service` is version `2.2.4.5`.
- Validation of the specified suppression-field records and activated versions.
- Query results showing the expected `hardBlockerComponentType` data.
- Front-end evidence that configuration and maker, checker, and bulk-submit controls behave as specified.
- Named FE and BE sign-off owners and completion dates.