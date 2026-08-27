---
type: source
title: Feed Manual Entities to LMS
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, manual-entities, LMS, UAT, reference-data]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, manual-entity-lms-reference-data-feed, country-specific-settlement-uat-coverage, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/019 Feed Manual Entities to LMS.md"]
---
# Feed Manual Entities to LMS

## Scope

This source is a reference-data roster in the Settlement Day 2 → Enable Settlement for Manual Entities → UAT testing context. Its title indicates that the listed manual entities are intended to be fed to [[lms]], but the document does not provide evidence that a feed was executed or accepted.

The roster contains 13 manual entities across 12 country codes. Sri Lanka appears twice, represented by `SCB COLOMBO*CMB` and `SCB COL FCB*CMB`.

## Source Data

| FMID | COUNTRY CODE | FMCODE | BRANCH CODE | |
| --- | --- | --- | --- | --- |
| 10036430 | BH | SCB BAHRAI*MAN | 55 | Manual entity |
| 10041530 | VN | SCB HANOI*HNI | 29 | Manual entity |
| 300011525 | KE | SCB KENYA B*NBO | 39 | Manual entity |
| 300084297 | NG | SCB NIGERIA*LAG | 82 | Manual entity |
| 10040387 | TZ | SCB TANZANI*DAR | 50 | Manual entity |
| 10037477 | GH | SCB GHANA*ACC | 35 | Manual entity |
| 10041902 | UG | SCB UGANDA*KAM | UG | Manual entity |
| 10041903 | ZM | SCB ZAMBIA*LUS | 52 | Manual entity |
| 300011470 | BD | SCB DHAKA*DAC | 86 | Manual entity |
| 300010782 | QA | SCB DOHA*DOH | QA | Manual entity |
| 10036655 | PK | SCB KARACHI*KHI | 97 | Manual entity |
| 10036647 | LK | SCB COLOMBO*CMB | 84 | Manual entity |
| 10022098 | LK | SCB COL FCB*CMB | 85 | Manual entity |

## Observations

All 13 FMIDs are distinct. Branch codes are heterogeneous: most are numeric, while the Uganda and Qatar records use alphabetic values (`UG` and `QA`). The source does not state whether these formats are intentional, mandatory, or accepted by LMS.

The source uses abbreviated FMCODE values. Some appear related to canonical wiki entities, including [[bahrain-scb-bahrai-man-gbs]], [[scb-kenya-b]], [[scb-nigeria-lag-gbs]], [[tanzania-scb-dar]], [[ghana-scb-ghana-acc-gbs]], [[uganda-scb-uganda-kam-gbs]], [[zambia-scb-zambia-lus-gbs]], [[qatar-scb-doha]], [[sri-lanka-scb-colombo-cmb]], and [[sri-lanka-scb-col-fcb-cmb]]. Exact identity should be verified before attaching these identifiers to existing entity records.

## Evidence Boundary

This document establishes an intended LMS-oriented roster, not a completed integration. It contains no payload or file specification, interface details, field mapping, transport mechanism, schedule, response codes, test cases, expected or actual results, reconciliation output, or approval evidence.

The relationship to [[cross-border-debit-lms-feed-contract]] is conceptual only. This source does not establish that manual-entity onboarding uses the same LMS interface, mapping, or processing rules as cross-border debit.

## Related Concepts

The roster provides concrete scope evidence for [[manual-entity-settlement-onboarding]] and [[manual-entity-settlement-enablement]]. It may also inform [[country-specific-settlement-uat-coverage]], while remaining separate from evidence that UAT was completed successfully.