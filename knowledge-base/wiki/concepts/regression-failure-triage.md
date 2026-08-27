---
type: concept
title: Regression Failure Triage
created: 2026-08-22
updated: 2026-08-22
tags: [regression-testing, defect-triage, test-maintenance, qa]
related: [uber-regression-testing, uber-integration, sfmrp, ratan-one, murex-cashflow-status-lifecycle, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md"]
---
# Regression Failure Triage

## Definition

Regression failure triage is the classification of failed automated tests according to the cause and evidentiary status of the failure. In the UBER regression record, a failed assertion is not automatically treated as a RATANONE product defect.

## Classification

### Product or implementation defect

Use this category when repeated evidence indicates that the implementation violates the intended contract. The source links examples to ADO work items `11224366`, `11236167`, and `11222354`.

### Test-script or assertion defect

Use this category when the system contract has changed but the test still expects obsolete behavior, such as `Fail` instead of `AutoFail`, `QUEUED` instead of the intended UI state, database-persisted cutoff data, an obsolete minor version, or an outdated response count.

### Test-data or mock defect

Use this category when missing, duplicate, or inconsistent SSI, Vostro, Nostro, counterparty, or cashflow data prevents the scenario from representing its intended state.

### Environment or dependency limitation

Use this category when a required external responder or environment is unavailable, as with IMS cases requiring a Razor response.

## Required disposition

Each failure should receive:

- A reproducible case identifier
- The observed and expected behavior
- The environment and data version
- A rerun result after correction
- An owner and defect reference where applicable
- A final disposition: product defect, script defect, data defect, environment blocker, accepted limitation, or passed

This classification is needed before using regression results as a release decision.