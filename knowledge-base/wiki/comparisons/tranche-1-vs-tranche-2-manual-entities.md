---
type: comparison
title: Tranche 1 versus Tranche 2 Manual Entities
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-day-2, rollout, manual-entities, ratan, operational-readiness]
related: [manual-entity-settlement-enablement, manual-entity-static-data-onboarding, settlement-suppression-exceptions, ebbs-settlement-accounting, manual-entity-lms-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# Tranche 1 versus Tranche 2 Manual Entities

The source organizes manual-entity settlement migration into two rollout groups. The groups are operational planning categories, not a replacement for the entity-level settlement and suppression decisions.

## Scope comparison

| Tranche 1 | Tranche 2 |
| --- | --- |
| Bangladesh — `300011470` | Nigeria — `300084297` |
| Tanzania — `10040387` | Ghana — `10037477` |
| Sri Lanka — `10036647` and `10022098` | Qatar DOHA — `300010782` |
| Pakistan — `10036655` | Bahrain — `10036430` |
| Kenya — `300011525` | Uganda — `10041902` |
| Vietnam — `10041530` | |
| Zambia — `10041903` | |

`SLATE_QFC` — `401081696` — is associated with the Qatar scope but remains cashflow-suppressed and is not treated as a normal settlement-enabled entity.

## Configuration differences

| Area | Tranche 1 | Tranche 2 |
| --- | --- | --- |
| Release cutoff | Mostly explicit entity values; Bangladesh and Tanzania use Razor values with Ratan fallback | Bahrain, Ghana, Uganda, and Qatar-related rules use entity-specific or Razor-derived configuration; Nigeria has `17:00 UTC` |
| Currency additions | `PKO -> PKR`, `VNO -> VND`, `LKO -> LKR`, `BDO -> BDT` | `NGB -> NGN`, `NGX -> NGN`, plus Nigeria-specific rounding and static data |
| EBBS accounting | Includes country-specific posting branches and credit codes | Includes Bahrain, Ghana, Nigeria, Qatar, and Uganda configurations |
| Suppression work | Tranche 1 non-FMRP additions, Vietnam `LN_BR`, Sri Lanka internal deals, Tanzania/XVA Omnibus | Tranche 2 entity list, metals, internal counterparties, and PM-trade suppression |
| LMS | Feed required for all tranche entities | Feed required for all tranche entities, including `SLATE_QFC` |
| Readiness evidence | UAT and CPT tracking recorded, with uneven signoff status | Business-rule and static-data work continued through August 2026 |

## Important distinctions

- The source does not establish a single production go-live date for either tranche.
- The source uses both country and entity counts; the two tranche lists include 12 countries but 14 active entity rows when duplicate-country entities are counted separately.
- Qatar contains two entities with different outcomes: DOHA is settlement-enabled, while `SLATE_QFC` remains suppressed.
- Tranche membership does not override entity-specific business rules, accounting configuration, or downstream-feed requirements.