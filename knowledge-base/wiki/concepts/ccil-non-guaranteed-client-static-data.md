---
type: concept
title: CCIL Non-Guaranteed Client Static Data
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, static-data, Ratan, Murex-2-11, data-quality, onboarding]
related: [ccil-guaranteed-and-non-guaranteed-netting, ccil-settlement-method-stamping, ratan, murex-2-11, configuration-driven-onboarding, maker-checker-settlement-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# CCIL Non-Guaranteed Client Static Data

## Current Problem

The source identifies three BAU weaknesses:

- no golden source for non-guaranteed CCIL client data;
- no clear ownership for Murex 2.11 CCIL static data;
- data-quality issues in the CCIL client static data.

## Tactical Model

Ratan receives a copy of Murex 2.11 CCIL client static data as local logical static data. It uses the FMIDs in that list to classify eligible non-guaranteed IRS cashflows with `Settlement Method = CCIL`.

This is explicitly tactical. The copied data and associated classification logic are expected to be discarded after Murex 2.11 decommissioning. The source does not define the owner, approval process, quality controls, retirement date, or migration plan.

## Sample Population

The source provides a sample list including CANARA BANK, HDFC BANK LIMITED, ICICI BANK LIMITED, IDBI BANK LTD, STATE BANK OF INDIA, THE FEDERAL BANK LIMITED, THE RATNAKAR BANK LTD., UNION BANK OF INDIA, and AXIS BANK LTD. It is not confirmed to be complete or authoritative. User-case examples contain additional FMIDs not present in the sample.

## New-Client Workaround

When a newly onboarding client's FMID is not yet in the list:

1. Add an NSTP rule to hold the cashflows.
2. Manually verify the Nostro account number.
3. Manually suppress SWIFT.
4. Request a permanent Ratan static-data update.
5. Remove the temporary NSTP rule after the update.

The static-data change is described as a CR that can take weeks through change, UAT, and release. Additional FMIDs may be added to a pre-tested NSTP rule in BAU without new UAT, based on the agreement cited in the source. The governance, approval, rollback, evidence-retention, expiry, and monitoring controls are not specified.

## Strategic Target

The strategic model requires a golden source for the non-guaranteed CCIL client list. stella identifies the client category and stamps the settlement method, while [[ratan]] provides operational filtering and netting.