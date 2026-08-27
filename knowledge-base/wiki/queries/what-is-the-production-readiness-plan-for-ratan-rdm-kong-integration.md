---
type: query
title: What Is the Production Readiness Plan for Ratan RDM Kong Integration?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rdm, kong, production-readiness, onboarding, indonesia]
related: [rdm, kong, rdm-reference-data-integration-via-kong, ratan-indonesia-onshoring-2026, indonesia-environment-readiness-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation/RDM Integration via Kong Gateway.md"]
---
# What Is the Production Readiness Plan for Ratan RDM Kong Integration?

## Open question

What approved plan will move the Ratanone-to-[[rdm]] integration through [[kong]] from SIT completion to production operation?

## Known evidence

The source identifies non-production PR `3141169` and pipeline run `20260804.1`, while explicitly marking production onboarding as `TBD`. It does not provide a production owner, target date, production change record, producer-grant confirmation, validation evidence, monitoring design, rollback plan, or operational support model.

## Information needed

- Named owner and approved production target date.
- Confirmation that `EDMILDAP/RATAN_EDMI_PROD` has the production RDM grant for `RDMApiService_GET`.
- Confirmation that reuse of `EDMILDAP_RATAN_EDMI_PROD_Ratanone-PCT2` has ownership, audit, and least-privilege approval.
- Production Kong configuration and deployment evidence.
- End-to-end production validation, monitoring, alerting, rollback, and credential-rotation arrangements.
- Defined handling when RDM or Kong is unavailable during compensation processing.