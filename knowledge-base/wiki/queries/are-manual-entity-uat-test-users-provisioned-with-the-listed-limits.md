---
type: query
title: Are Manual-Entity UAT Test Users Provisioned with the Listed Limits?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, access-provisioning, authorization-limits, manual-entities, open-question]
related: [settlement-test-user-profiles, manual-entity-settlement-enablement, manual-entity-settlement-onboarding, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/User Profile for testing env.md"]
---
# Are Manual-Entity UAT Test Users Provisioned with the Listed Limits?

## Question

Were the listed test users actually created in the testing environment, assigned the requested `FMO_OPS_*` profiles, configured with the stated settlement authorization limits, and validated for UAT?

## Evidence Available

The source lists numeric test-user IDs, names, requesters, dates, six operational profiles, and authorization limits. It does not provide provisioning records, role-assignment evidence, access-test results, approval references, or UAT execution outcomes.

Every `Status` field is blank. The table also contains continuation rows with omitted fields, an ambiguously formatted row beginning with `2023656`, and dates such as `8/5/2026` whose intended format is unclear.

## Validation Required

For each listed account, obtain evidence confirming:

1. Account creation in the correct testing environment.
2. Assignment of the intended role code.
3. Configuration of the stated monetary limit.
4. Effective permissions for the assigned role.
5. Maker-checker or other segregation-of-duties controls.
6. Successful access and authorization-limit tests.
7. UAT execution, approval, or remediation status.
8. Canonical identity, requester, and date mapping for continuation rows.

The validation should specifically confirm that `FMO_OPS_MKR` cannot authorize settlement above its USD 0 limit and that the higher `FMO_OPS_BOM` limit relative to `FMO_OPS_BOL` and `FMO_OPS_BOS` is intentional.

## Current Assessment

The source supports the existence of a requested access roster only. Provisioning and UAT readiness remain unconfirmed until environment evidence and nonblank status records are supplied.