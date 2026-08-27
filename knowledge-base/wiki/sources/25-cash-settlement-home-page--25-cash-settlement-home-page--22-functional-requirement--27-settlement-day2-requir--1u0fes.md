---
type: source
title: "UAT Testing — Enable Settlement for Manual Entities"
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [uat, manual-entities, settlement, ratan, fmsgw, swift, accounting]
related: [ratan, fmsgw, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, settlement-day2-requirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing.md"]
---
# UAT Testing — Enable Settlement for Manual Entities

This planning note defines UAT coverage for onboarding manual entities to the established settlement workflow used in other markets.

The stated testing focus is limited to onboarding-specific changes, principally SWIFT generation and accounting generation. Most covered countries are expected to be processed by existing GBS users who already operate in [[ratan]], while generic cases are included to provide confidence to country operations teams.

The document explicitly states that test scope is not intended to be uniform across countries. RATAN and [[fmsgw]] case counts are planning coverage counts only; the source contains no test execution dates, outcomes, defects, acceptance criteria, or sign-off evidence.

## Coverage matrix

|  | Country | Branch | RATAN | FMSGW | Comments |
| --- | --- | --- | --- | --- | --- |
| 1 | Bahrain |  | 19 | 9 |  |
| 2 | Qatar | Doha | 19 | 9 |  |
| 3 | Qatar | Slate One | 0 | 0 | Entity not setup to be handled in downstream |
| 4 | Kenya |  | 19 | 9 |  |
| 5 | Zambia |  | 13 | 9 |  |
| 6 | Uganda |  | 16 | 9 |  |
| 7 | Tanzani |  | 19 | 11 |  |
| 8 | Ghana |  | 16 | 9 |  |
| 9 | Nigeria |  | 29 | 9 |  |
| 10 | Sri Lanka | Colombo | 36 | 9 |  |
| 11 | Sri Lanka | Colombo FCB | ? | ? |  |
| 12 | Vietnam |  | 24 | 9 |  |
| 13 | Pakistan |  | 32 | 9 |  |
| 14 | Bangladesh |  | 32 | 11 |  |

## Scope observations

- Manual entities are expected to use the existing settlement workflow rather than a distinct workflow.
- [[manual-entity-settlement-onboarding]] therefore uses targeted change validation rather than full workflow re-certification.
- The planned coverage varies by country and branch, as described in [[country-specific-settlement-uat-coverage]].
- Slate One has no planned RATAN or FMSGW cases because it is not configured for downstream handling.
- Colombo FCB has unresolved RATAN and FMSGW coverage counts.
- `Tanzani` is retained verbatim from the source and has not been normalized to a country identifier.

## Planning totals

Excluding the unresolved Colombo FCB row, the matrix lists 255 RATAN cases and 114 FMSGW cases. These are scope-planning figures, not indicators of completed testing or operational readiness.

## Related material

This note belongs to the broader [[settlement-day2-requirement]] area. Its FMSGW reference is limited to planned UAT coverage and does not establish behavior described in [[fmsgw-deletion-driven-cashflow-settlement]].