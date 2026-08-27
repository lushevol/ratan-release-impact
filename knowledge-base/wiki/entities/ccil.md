---
type: entity
title: CCIL
created: 2026-08-22
updated: 2026-08-23
tags: [CCIL, clearing, manual-netting, settlement-method, cash-settlement, bilateral-netting, settlement, netting, payment-type, settlement-infrastructure, scope-exclusion, organisation]
related: [f2b, fmrp, murex, stella, auto-netting, bilateral-netting, bilateral-netting-eligibility, ccil-manual-netting, ccil-netting-eligibility-key, manual-un-netting, ratan, nstp, affirmation-email-scope-configuration, settlement-affirmation-email-automation, ccil-cashflow-identification, ccil-netting, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# CCIL

## Scope and terminology

CCIL is the central named organisation and settlement-workflow subject in the [[ccil-netting]] design. The design distinguishes the organisation or settlement arrangement from the technical settlement-method value `CCIL` attached to qualifying cashflows.

CCIL is also referenced in the functional requirements in connection with manual netting and the CCIL settlement method.

The [[ccil-netting]] design does not provide organisational details, legal requirements, approval status, or implementation evidence for CCIL processing.

## Onboarding implications

The onboarding checklist describes existing CCIL logic as using Murex products. New onboarding requires those rules to be reviewed and updated with STELLA attributes.

The checklist also states that settlement-method stamping occurs in RATAN and asks whether STELLA should stamp the method.

The onboarding source does not establish the target FMRP/STELLA design or implementation status.

## Proposed technical processing path

According to the CCIL Netting Design, the design proposes a dedicated processing path for CCIL cashflows. The proposed path includes:

- Classification in the Murex adaptor
- NSTP treatment in the rule service
- Cross-counterparty netting review
- Conversion of the resultant cashflow to settlement method `CASH`

These are design proposals from the CCIL Netting Design and are not implementation evidence.

## CCIL Netting workflow

According to the CCIL Netting source, a successful CCIL netting operation produces a resultant cashflow with payment type `CCIL Netting`.

The specified flow requires:

- Affirmation submission
- Completed NSTP `MAKER_CHECKER` processing
- Release of the resultant from [[ratan]]

CCIL-specific acceptance cases in the CCIL Netting source require the component counterparty FMID to be different from `400021949`.

The source does not establish whether `400021949` is a permanent production exclusion or a test-data condition.

## Bilateral-netting coverage

According to the bilateral-netting requirement, the acceptance criterion covers cashflows satisfying:

```text
Settlement Method = CCIL
Counterparty FMID = 400021949
```

These cashflows are expected to transition from `WAITING / Pending Netting` to `NETTED` and produce a resultant with:

- `Affirmation status = 'Affirmed'`
- Correct amount
- `Payment type = 'Bilateral Netting'`
- `NSTP process complete (MAKER_CHECKER)`

This bilateral-netting requirement describes a different resultant payment type from the `CCIL Netting` workflow source. The bilateral-netting requirement does not establish whether `Counterparty FMID=400021949` is mandatory for every CCIL netting operation.

## Settlement-affirmation email scope

According to the Derivative Settlement Affirmation - Email Automation requirement, CCIL deals are explicitly excluded from the settlement-affirmation email trigger.

That requirement also identifies CCIL Settlement Method as a configurable scope criterion. The implementation must therefore clarify whether the exclusion is global or configurable by Booking Entity, client, product, or date.