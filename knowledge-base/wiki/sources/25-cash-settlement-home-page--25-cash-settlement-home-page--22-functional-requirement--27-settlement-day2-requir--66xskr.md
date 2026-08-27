---
type: source
title: Tranche 2 Manual-Entity Go-Live Checklist
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-day-2, manual-entities, tranche-2, go-live, static-data]
related: [manual-entity-go-live-readiness, release-cutoff-configuration, strategic-fm-list-swift-generation, ebbs-posting-configuration, what-is-the-authoritative-nigeria-ngb-ngn-rounding-configuration, what-are-the-final-qatar-release-cutoff-and-ebbs-configurations, what-is-the-approved-tranche-2-manual-entity-go-live-schedule-and-signoff-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md"]
authors: []
year: 2026
url: ""
venue: "Internal go-live checklist"
---
# Tranche 2 Manual-Entity Go-Live Checklist

This checklist records proposed configuration and readiness inputs for Bahrain, Qatar, Uganda, Ghana, and Nigeria in the Settlement Day 2 Tranche 2 manual-entity rollout. It documents values to be configured in [[ratan]], including Nostro data, SWIFT static data, release cutoffs, currency mapping, rounding, accounting timezones, and `STRATEGIC_FM_LIST`.

The checklist is not proof that the values were deployed, tested, or approved. UAT-signoff attachments are blank, CPT links contain no recorded outcome, and technical go-live dates are absent.

## Recorded go-live schedule

| Tranche2 | Technical go live date in Ratan | Business go live date |
| --- | --- | --- |
| BH | | Third week of Sepetember |
| QA | | |
| UG | | |
| GH | | |
| NG | | |

Only Bahrain has a business target, written as “Third week of Sepetember.” No year, exact date, or technical Ratan date is supplied.

## Nostro static-data register

| Country | MX2.11 Entity | FMID | FMCODE | Nostro Static |
| --- | --- | --- | --- | --- |
| Bahrain | BAHRAIN | 10036430 | SCB BAHRAI*MAN | 📎 [Nostro Static Data0729.xlsx](attachments/Nostro Static Data0729.xlsx) |
| QATAR | DOHA | 300010782 | SCB DOHA*DOH | |
| SLATE_QFC | | 401081696 | SLATE ONE LLC*DOH | |
| Uganda | UGANDA | 10041902 | SCB UGANDA*KAM | |
| Ghana | GHANA | 10037477 | SCB GHANA*ACC | |
| Nigeria | NIGERIA | 300084297 | SCB NIGERIA*LAG | |

The attachment contents are not included in the checklist, so completeness and deployed status cannot be established from this source.

## SWIFT static data

| Entity FMCODE | Country Code | Branch code | FMID | Sender Bic | Field 53 BIC(Rule1) | Field 53 CCY to be used | Field 58 BIC(Rule2) | Swift Static Data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCB BAHRAI*MAN | BH | 55 | 10036430 | SCBLBHBMXXX | SCBLBHBMGMO | BHD | SCBLBHBMGMO | 📎 [Swift Static data2026-07-21.xlsx](attachments/Swift Static data2026-07-21.xlsx) |
| SCB NIGERIA*LAG | NG | 82 | 300084297 | SCBLNGLAATSY | SCBLNGLAFMO | NGN | SCBLNGLAFMO | |
| SCB GHANA*ACC | GH | 35 | 10037477 | SCBLGHACXXX | SCBLGHACFMO | GHS | SCBLGHACFMO | |
| SCB UGANDA*KAM | UG | UG | 10041902 | SCBLUGKAXXX | SCBLUGKAFMO | UGX | SCBLUGKAFMO | |
| SCB DOHA*DOH | QA | QA | 300010782 | SCBLQAQXXXX | SCBLQAQXGMO | QAR | SCBLQAQXGMO | |

These are stated static values only. The source neither verifies loading nor provides generated-message evidence. The underlying MX eligibility logic is referenced externally and is not defined here; see [[manual-entity-swift-mx-bifurcation]].

## Release cutoff configuration

| Country | MX2.11 Entity | FMID | FMCODE | cut_off_time | cut_off_shifter | Release cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| Bahrain | BAHRAIN | 10036430 | SCB BAHRAI*MAN | 15:00 UTC | VD-1BD | |
| QATAR | DOHA | 300010782 | SCB DOHA*DOH | | Confirmed with Deepak and user, will use the Currency /Shifter/Time/Timezone from Razor | |
| SLATE_QFC | | 401081696 | SLATE ONE LLC*DOH | NA | NA | |
| Uganda | UGANDA | 10041902 | SCB UGANDA*KAM | 15:00 UTC | VD-1BD | |
| Ghana | GHANA | 10037477 | SCB GHANA*ACC | 15:00 UTC | VD-1BD | |
| Nigeria | NIGERIA | 300084297 | SCB NIGERIA*LAG | 17:00 UTC | VD-1BD | |

Qatar has no resolved cutoff values in this source and depends on [[razor]] as the specified source of currency, shifter, time, and timezone.

## Nigeria currency mapping and rounding

The checklist states that `NGB-NGN` must be added on the Ratan side for Nigeria:

| NGB | NGN | Comment |
| --- | --- | --- |
| NGB | NGN | 2026-03-25 NGB-NGN not exists in Ratan, need to add this new mapping. 2026-03-11 Confirmed with Synthia, this mapping need to added for Nigeria |

The rounding record is contradictory:

| k_currency | v_precision | v_type | Comment |
| --- | --- | --- | --- |
| ~~NGN~~ | ~~0~~ | ~~ROUNDING_OFF~~ | 2026-08-14 Deepak and Gomathy confirmed thata NGN rounding percision should be 2 |
| NGB | 2 | ROUNDING_OFF | |

A 2026-04-02 note requests NGN precision changing from `2` to `0`; a later 2026-08-14 note says NGN precision should be `2`; the active table row is instead `NGB` at precision `2`. This unresolved ambiguity is tracked in [[what-is-the-authoritative-nigeria-ngb-ngn-rounding-configuration]].

## EBBS configuration

The source identifies [[ebbs]] bridge accounts and posting values, but says Qatar and Bangladesh require double confirmation. Bangladesh is incidental context, not Tranche 2 scope evidence.

| id | closing_entity | legal_entity | fmid | ebbs_bridge_account |
| --- | --- | --- | --- | --- |
| | | SCB BAHRAI*MAN | 10036430 | 09906397050 |
| | | SCB DOHA*DOH | 300010782 | 09473025940 |
| | | SCB UGANDA*KAM | 10041902 | 0062599158900 |
| | | SCB GHANA*ACC | 10037477 | 0062599150800 |
| | | SCB NIGERIA*LAG | 300084297 | 9625047537 |

| FMID | Country | Posting Branch | Txn Type code | Dr Txn Code | Cr Txn Code |
| --- | --- | --- | --- | --- | --- |
| 10037477 | GH | 00001 | RTN | 478 | 278 |
| 300084297 | NG | 00100 | RTN | 478 | 278 |
| 10041902 | UG | 00001 | RTN | 478 | 278 |
| 10036430 | BH | 055 | RTN | 478 | 378 |
| 300010782 | QA | 042 | RTN | 478 | 378 |

A Tanzania-specific note concerning a change from `278` to `578` must not be applied to these Tranche 2 records.

## Accounting timezone configuration

The stated processing rule is to derive country from FMID using static data, then derive `zoneid` from country. New-country onboarding requires timezone configuration.

| Entity | Country | zoneid |
| --- | --- | --- |
| BAHRAIN | BH | Asia/Bahrain |
| QATAR | QA | Asia/Qatar |
| UGANDA | UG | Africa/Kampala |
| GHANA | GH | Africa/Accra |
| NIGERIA | NG | Africa/Lagos |

## SWIFT-generation exception

The checklist states that Ratan generates a SWIFT message only when the entity appears in `STRATEGIC_FM_LIST`. It identifies `SLATE_QFC` / `SLATE ONE LLC*DOH` as cashflow-suppressed and therefore not requiring `STRATEGIC_FM_LIST` configuration.

| Entity | FMID | FMCODE |
| --- | --- | --- |
| SLATE_QFC | 401081696 | SLATE ONE LLC*DOH |

This is a documented rationale for the exception, not evidence that cashflow suppression or other downstream configuration is complete. See [[strategic-fm-list-swift-generation]] and [[why-is-slate-one-not-configured-for-downstream-settlement-processing]].

## Readiness evidence gaps

- The UAT Testing Signoff table has no attachment for BH, NG, QA, UG, or GH.
- NSTP has a heading but no recorded content.
- Cashflow Suppression refers to `Business rule0811.xlsx`, whose contents are unavailable in this source.
- CPT contains links only, without recorded results, owners, defects, or approvals.
- Qatar cutoff values and EBBS confirmation remain unresolved.
- All technical go-live dates are blank.

These gaps establish incomplete checklist evidence, not that UAT, CPT, or configuration activities did not occur.