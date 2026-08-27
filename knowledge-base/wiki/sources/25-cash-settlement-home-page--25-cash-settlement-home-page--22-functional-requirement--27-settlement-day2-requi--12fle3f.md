---
type: source
title: User Profile for Testing Environment
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [uat, test-environment, manual-entities, settlement, access-control]
related: [cash-settlement-home-page, manual-entity-settlement-enablement, manual-entity-settlement-onboarding, settlement-day-2, settlement-test-user-profiles, are-manual-entity-uat-test-users-provisioned-with-the-listed-limits]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/User Profile for testing env.md"]
---
# User Profile for Testing Environment

## Summary

This document records requested test-environment user profiles for [[concepts/manual-entity-settlement-enablement]] within the [[entities/cash-settlement-home-page]] functional area and [[concepts/settlement-day-2]] requirement grouping.

The roster identifies six operational profiles, their stated settlement authorization limits, test-user accounts, requesters, dates, and status fields. Every `Status` field is blank. The document therefore records requested or intended access but does not prove that accounts were provisioned, assigned the listed limits, validated, or used successfully during UAT.

## Operational Profiles

| Role | Profile | Authorization limit |
| --- | --- | ---: |
| Operations Maker | `FMO_OPS_MKR` | USD 0 |
| Operations Back Office Clerk | `FMO_OPS_BOC` | Up to USD 29,999,999 |
| Operations Back Office Officer | `FMO_OPS_BO` | Up to USD 99,999,998 |
| Operations Back Office Manager | `FMO_OPS_BOM` | Up to USD 3,999,999,999 |
| Operations Back Office Lead | `FMO_OPS_BOL` | Up to USD 999,999,999 |
| Operations Back Office Supervisor | `FMO_OPS_BOS` | Up to USD 299,999,999 |

The source uses `Upto` in the original table. The normalized summary uses `Up to`, while the original wording is preserved below.

`FMO_OPS_MKR` has a USD 0 authorization limit. This may support segregation between transaction preparation and monetary settlement approval, but the source does not specify the Maker's general functional permissions.

The authorization limits are not monotonically ordered by role title. In particular, `FMO_OPS_BOM` has a higher stated limit than `FMO_OPS_BOL` and `FMO_OPS_BOS`. The source does not define approval precedence or explain whether the limits are per transaction, settlement batch, or cumulative.

## Source Data

The following table is reproduced as provided, including continuation-row structure and blank statuses.

```markdown
| Request Sub-Group | Role | Authorization Limit for Settlement Profiles | Test User | Test User name | Requested by | Date | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operations Maker | FMO_OPS_MKR | USD 0 | 1473304 | Ranasinghe, Jehan | Fonseka, Shalini | 4/16/2026 | |
| 2023656 | Khensa Zainab | Ali, Shaukat | 4/16/2026 | |
| 1594253 | Nasir Hussain |
| Operations Back Office Clerk | FMO_OPS_BOC | Upto USD 29,999,999 | 1633783 | V, Hari | Joseph, Synthia | 4/16/2026 | |
| 2030438 | D, Charanya | 5/8/2026 | |
| 1520516 | Mahela, Simon Godfrey | Mahela, Simon Godfrey | 4/14/2026 | |
| 2015859 | Kalinga, Nancy Richard |
| Operations Back Office Officer | FMO_OPS_BO | Upto USD 99,999,998 | 1508350 | Udara, Thilina | Fonseka, Shalini | 4/16/2026 | |
| 1177353 | Fonseka, Shalini |
| 1216485 | Arifuzzaman, Abu Mohammad | Morshed, Golam | 4/21/2026 | |
| 1648931 | Niloy, Nehabul Haque |
| 1567048 | Muhammad Ahsan Khan | Ali, Shaukat | 4/21/2026 | |
| Operations Back Office Manager | FMO_OPS_BOM | Upto USD 3,999,999,999 | 1226803 | Joseph, Synthia | Joseph, Synthia | 4/16/2026 | |
| 1166836 | Narasimhanparthasarathy, Lakshmi |
| 1262588 | Raghu, Lavanya | 5/8/2026 | |
| 1254467 | Raju Gokulakrishnan | K Thirunavukarasu, Cordelia Sumita | 4/16/2026 | |
| 1337744 | Abdul Kadir, Abdullah |
| 1129381 | K Thirunavukarasu, Cordelia Sumita |
| 1405593 | Vignesh D52 | Vignesh D52 | 8/5/2026 | |
| 1462616 | Shaukat Ali | Ali, Shaukat | 4/21/2026 | |
| 1590763 | Florian Muhochi | Florian Muhochi | 7/15/2026 | |
| Operations Back Office Lead | FMO_OPS_BOL | Upto USD 999,999,999 | 1448370 | N1, Gomathy | Joseph, Synthia | 4/16/2026 | |
| 1226798 | Sridharan, Sathyanarayanan |
| 1465419 | DeviM, Renuka |
| 1279615 | Mathew, Morris |
| 1668747 | Rawat, Rohit Singh |
| 1404876 | M, Logeashwari | 5/8/2026 | |
| 1657151 | Subramani1, Dhinesh |
| 1668926 | Vimalraj, Preethi |
| Operations Back Office Supervisor | FMO_OPS_BOS | Upto USD 299,999,999 | 1458672 | Hadi Zaidi | Ali, Shaukat | 4/16/2026 | |
| 1141942 | Alam, Mohammad Maksud | Morshed, Golam | 4/21/2026 | |
| 1213850 | Morshed, Golam |
```

## Data-Quality and Interpretation Notes

- Continuation rows omit repeated profile, role, authorization limit, and sometimes requester or date fields.
- The row beginning `2023656 | Khensa Zainab` does not align with the eight-column header and requires validation.
- Several continuation rows have no visible date or requester.
- `8/5/2026` is ambiguous between August 5, 2026 and May 8, 2026.
- Name ordering is inconsistent. `Fonseka, Shalini` and `Shalini Fonseka` appear to refer to the same person, [[stakeholders/shalini-fonseka]].
- Some requester and test-user names are identical, which may be valid but should be confirmed.
- No request identifier, approval reference, provisioning evidence, or nonblank status is provided.
- The source does not identify a country, settlement entity, test case, execution result, or UAT approval outcome.

## Evidence Boundary

This document should be used as evidence of intended UAT access provisioning, not as evidence of completed provisioning or successful UAT. Validation should confirm, for each numeric test-user ID:

1. The account exists in the testing environment.
2. The intended `FMO_OPS_*` role is assigned.
3. The stated settlement authorization limit is configured.
4. Functional permissions are consistent with the role.
5. Segregation-of-duties controls are effective.
6. UAT execution and approval evidence is available.
7. The requester, date, and status are unambiguous.

See [[concepts/settlement-test-user-profiles]] and [[queries/are-manual-entity-uat-test-users-provisioned-with-the-listed-limits]] for the resulting control and validation questions.