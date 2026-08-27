---
type: concept
title: Settlement Test-User Profiles
created: 2026-08-23
updated: 2026-08-23
tags: [uat, test-environment, user-profiles, role-based-access-control, settlement]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, settlement-day-2, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/User Profile for testing env.md"]
---
# Settlement Test-User Profiles

## Definition

A settlement test-user profile is the combination of a test-environment account, an application role, a settlement authorization limit, a requester, and provisioning or validation status used to support UAT.

For manual-entity settlement, these profiles provide the access-control layer needed to test operational workflows without treating a user roster as proof of completed UAT.

## Profiles in the Source

The source identifies six profiles:

- `FMO_OPS_MKR` — Operations Maker, USD 0 authorization limit.
- `FMO_OPS_BOC` — Operations Back Office Clerk, up to USD 29,999,999.
- `FMO_OPS_BO` — Operations Back Office Officer, up to USD 99,999,998.
- `FMO_OPS_BOM` — Operations Back Office Manager, up to USD 3,999,999,999.
- `FMO_OPS_BOL` — Operations Back Office Lead, up to USD 999,999,999.
- `FMO_OPS_BOS` — Operations Back Office Supervisor, up to USD 299,999,999.

The source does not define the general permissions associated with these roles. Authorization limits must therefore be kept separate from assumptions about viewing, editing, submitting, releasing, cancelling, or approving settlement activity.

## Control Significance

The USD 0 limit for `FMO_OPS_MKR` is consistent with a possible maker-versus-approver separation, but the source does not explicitly define a maker-checker workflow.

The limits are not ordered strictly by role title. `FMO_OPS_BOM` has a higher stated limit than `FMO_OPS_BOL` and `FMO_OPS_BOS`; title-based approval precedence should not be inferred without an authoritative authorization model.

A complete profile record should preserve:

- Numeric test-user ID.
- Canonical user identity.
- Assigned application role.
- Configured authorization limit and currency.
- Requester and request date.
- Provisioning status.
- Environment-validation evidence.
- UAT execution and approval evidence.

## Provisioning Status

The source has blank `Status` values for all listed users. It consequently establishes a request or intended roster, but not account creation, role assignment, limit configuration, access validation, or UAT completion.

A status model should distinguish at least:

- Requested.
- Provisioned.
- Role and limit validated.
- UAT-ready.
- UAT executed.
- Approved.
- Rejected or requiring remediation.

The project should also define whether authorization limits are inclusive and whether they apply per transaction, per settlement batch, or cumulatively.

## Data Governance

User names should be normalized without losing the original source representation. For example, `Fonseka, Shalini` and `Shalini Fonseka` should be reconciled only after identity confirmation.

Continuation rows in the source do not repeat all fields, so profile membership, requester, and date assignments require validation before being used as audit evidence. Dates such as `8/5/2026` must be converted to an unambiguous format.

This concept extends [[concepts/manual-entity-settlement-onboarding]] by identifying user access and authorization as a prerequisite for UAT. It should not be used to infer [[concepts/country-specific-settlement-uat-coverage]] because the source does not identify a country or execution result.