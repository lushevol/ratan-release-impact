---
type: source
title: Manual Entities Overall Go-Live Checklist
authors: []
year: 2026
url: ""
venue: "Internal configuration checklist"
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-day-2, manual-entities, go-live, static-data, configuration]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, manual-entity-go-live-static-data-controls, non-iso-to-iso-currency-mapping, release-cutoff-configuration, ebbs-settlement-posting-configuration, fmid-country-time-zone-resolution, strategic-fm-list-swift-generation-control, ratan, razor, ebbs, swift]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md"]
---
# Manual Entities Overall Go-Live Checklist

This checklist defines required reference-data and business-rule setup for manual-entity cash settlement across Ratan, SWIFT, Razor, EBBS, and accounting time-zone configuration. It is a configuration specification, not evidence that setup was deployed, approved, tested, or reconciled.

## Nostro Static Data

| | Country | MX2.11 Entity | FMID | FMCODE | Nostro static data |
| --- | --- | --- | --- | --- | --- |
| 1 | Bahrain | BAHRAIN | 10036430 | SCB BAHRAI*MAN | 📎 [Nostro Static Data0729.xlsx](attachments/Nostro Static Data0729.xlsx) |
| 2 | QATAR | DOHA | 300010782 | SCB DOHA*DOH |
| SLATE_QFC | 401081696 | SLATE ONE LLC*DOH |
| 3 | Kenya | KENYA | 300011525 | SCB KENYA B*NBO |
| 4 | Zambia | ZAMBIA | 10041903 | SCB ZAMBIA*LUS |
| 5 | Uganda | UGANDA | 10041902 | SCB UGANDA*KAM |
| 6 | Tanzania | TANZANIA | 10040387 | SCB TANZANI*DAR |
| 7 | Ghana | GHANA | 10037477 | SCB GHANA*ACC |
| 8 | Nigeria | NIGERIA | 300084297 | SCB NIGERIA*LAG |
| 9 | Sri Lanka | SRI LANKA | 10036647 | SCB COLOMBO*CMB |
| FCBUSLANKA | 10022098 | SCB COL FCB*CMB |
| 10 | Vietnam | HANOI | 10041530 | SCB HANOI*HNI |
| 11 | Pakistan | KARACHI | 10036655 | SCB KARACHI*KHI |
| 12 | Bangladesh | DHAKA | 300011470 | SCB DHAKA*DAC |

## SWIFT Static Data

| | Entity FMCODE | Country Code | Branch code | FMID | Sender Bic | Field 53 BIC(Rule1) | Field 53 CCY to be used | Field 58 BIC(Rule2) | Swift Static Data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SCB BAHRAI*MAN | BH | 55 | 10036430 | SCBLBHBMXXX | SCBLBHBMGMO | BHD | SCBLBHBMGMO | 📎 [Swift Static data2026-07-21.xlsx](attachments/Swift Static data2026-07-21.xlsx) |
| 2 | SCB HANOI*HNI | VN | 29 | 10041530 | SCBLVNVXXXX | SCBLVNVXFMO | VND | SCBLVNVXFMO |
| 3 | SCB NIGERIA*LAG | NG | 82 | 300084297 | SCBLNGLAATSY | SCBLNGLAFMO | NGN | SCBLNGLAFMO |
| 4 | SCB KARACHI*KHI | PK | 97 | 10036655 | SCBLPKKXXXX | SCBLPKKXXXX | PKR | SCBLPKKXXXX |
| 5 | SCB GHANA*ACC | GH | 35 | 10037477 | SCBLGHACXXX | SCBLGHACFMO | GHS | SCBLGHACFMO |
| 6 | SCB UGANDA*KAM | UG | UG | 10041902 | SCBLUGKAXXX | SCBLUGKAFMO | UGX | SCBLUGKAFMO |
| 7 | SCB ZAMBIA*LUS | ZM | 52 | 10041903 | SCBLZMLXXXX | SCBLZMLXFMO | ZMW | SCBLZMLXFMO |
| 8 | SCB KENYA B*NBO | KE | 39 | 300011525 | SCBLKENXXXX | SCBLKENXFMO | KES | SCBLKENXFMO |
| 9 | SCB DOHA*DOH | QA | QA | 300010782 | SCBLQAQXXXX | SCBLQAQXGMO | QAR | SCBLQAQXGMO |
| 10 | SCB COLOMBO*CMB | LK | 84 | 10036647 | SCBLLKLXXXX | SCBLLKLXXXX | LKR | SCBLLKLXXXX |
| 11 | SCB COL FCB*CMB | LK | 85 | 10022098 | SCBLLKLXXXX | SCBLLKLXXXX | LKR | SCBLLKLXXXX |
| 12 | SCB TANZANI*DAR | TZ | 50 | 10040387 | SCBLTZTXXXX | SCBLTZTXFMO | TZS | SCBLTZTXFMO |
| 13 | SCB DHAKA*DAC | BD | 86 | 300011470 | SCBLBDDXXXX | SCBLBDDXXXX | BDT | SCBLBDDXXXX |

## Release Cutoff

| | Country | MX2.11 Entity | FMID | FMCODE | cut_off_time | cut_off_shifter | Release cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bahrain | BAHRAIN | 10036430 | SCB BAHRAI*MAN | 15:00 UTC | VD-1BD | 📎 [Release CutOff.xlsx](attachments/Release CutOff.xlsx) |
| 2 | QATAR | DOHA | 300010782 | SCB DOHA*DOH | | Confirmed with Deepak and user ,will use the Currency /Shifter/Time/Timezone from Razor |
| SLATE_QFC | 401081696 | SLATE ONE LLC*DOH | NA | NA |
| 3 | Kenya | KENYA | 300011525 | SCB KENYA B*NBO | 15:00 UTC | VD-1BD |
| 4 | Zambia | ZAMBIA | 10041903 | SCB ZAMBIA*LUS | 15:00 UTC | VD-1BD |
| 5 | Uganda | UGANDA | 10041902 | SCB UGANDA*KAM | 15:00 UTC | VD-1BD |
| 6 | Tanzania | TANZANIA | 10040387 | SCB TANZANI*DAR | | Confirmed with Deepak and user ,will use the Currency /Shifter/Time/Timezone from Razor |
| 7 | Ghana | GHANA | 10037477 | SCB GHANA*ACC | 15:00 UTC | VD-1BD |
| 8 | Nigeria | NIGERIA | 300084297 | SCB NIGERIA*LAG | 17:00 UTC | VD-1BD |
| 9 | Sri Lanka | SRI LANKA | 10036647 | SCB COLOMBO*CMB | 13:00 UTC | VD-1BD |
| FCBUSLANKA | 10022098 | SCB COL FCB*CMB | 13:00 UTC | VD-1BD |
| 10 | Vietnam | HANOI | 10041530 | SCB HANOI*HNI | 11:00 UTC | VD-1BD |
| 11 | Pakistan | KARACHI | 10036655 | SCB KARACHI*KHI | 13:00 UTC | VD-1BD |
| 12 | Bangladesh | DHAKA | 300011470 | SCB DHAKA*DAC | | Confirmed with Deepak and user ,will use the Currency /Shifter/Time/Timezone from Razor |

## Non-ISO to ISO Currency Mapping

| Non ISO Currency | ISO Currency | Comment |
| --- | --- | --- |
| NGB | NGN | 2026-03-25 NGB-NGN not exists in Ratan, need to add this new mapping. 2026-03-11 Confirmed with Synthia, this mapping need to added for Nigeria. |
| PKO | PKR | 2026-01-20 Confirmed with @Cordelia Sumita K Thirunavukarasu. For Pakistan, Non ISO to ISO mapping is PKO -PKR, doesn't exist in current mapping list, need to be added. |

## Rounding Logic

| k_currency | v_precision | v_type |
| --- | --- | --- |
| ~~NGN~~ | ~~0~~ | ~~ROUNDING_OFF~~ |
| NGB | 2 | ROUNDING_OFF |

The source contains earlier guidance to change NGN precision from `2` to `0`, but later notes state that NGN rounding precision should be `2` and retain the `NGB` row. The authoritative mapping-and-rounding sequence remains unresolved.

## EBBS Bridge Accounts

| id | closing_entity | legal_entity | fmid | ebbs_bridge_account |
| --- | --- | --- | --- | --- |
| | | SCB BAHRAI*MAN | 10036430 | 09906397050 |
| | | SCB DOHA*DOH | 300010782 | 09473025940 |
| | | SCB KENYA B*NBO | 300011525 | 0062599158900 |
| | | SCB ZAMBIA*LUS | 10041903 | 0062599158900 |
| | | SCB UGANDA*KAM | 10041902 | 0062599158900 |
| | | SCB TANZANI*DAR | 10040387 | 0062599158900 |
| | | SCB GHANA*ACC | 10037477 | 0062599150800 |
| | | SCB NIGERIA*LAG | 300084297 | 9625047537 |
| | | SCB COLOMBO*CMB | 10036647 | 09995954893 |
| | | SCB COL FCB*CMB | 10022098 | 09995954895 |
| | | SCB HANOI*HNI | 10041530 | 09434372001 |
| | | SCB KARACHI*KHI | 10036655 | 09900006470 |
| | | SCB DHAKA*DAC | 300011470 | 09111178468 |

The source records that Qatar and Bangladesh bridge-account data require double confirmation.

## EBBS Posting and Transaction Codes

| FMID | Country | Posting Branch | Txn Type code | Dr Txn Code | Cr Txn Code |
| --- | --- | --- | --- | --- | --- |
| 10037477 | GH | 00001 | RTN | 478 | 278 |
| 10041530 | VN | 099 | RTN | 478 | 378 |
| 300011525 | KE | 07800 | RTN | 478 | 278 |
| 300084297 | NG | 00100 | RTN | 478 | 278 |
| 10040387 | TZ | 08700 | RTN | 478 | 578 |
| 10041902 | UG | 00001 | RTN | 478 | 278 |
| 10041903 | ZM | 01700 | RTN | 478 | 278 |
| 300011470 | BD | 068 | RTN | 478 | 378 |
| 10036655 | PK | 001 | RTN | 478 | 678 |
| 10036647 | LK | 093 | RTN | 478 | 378 |
| 10022098 | LK | 093 | RTN | 478 | 378 |
| 10036430 | BH | 055 | RTN | 478 | 378 |
| 300010782 | QA | 042 | RTN | 478 | 378 |

On 2026-06-15, EBBS advised that Tanzania's credit transaction code should change from `278` to `578`.

## FMID-to-Time-Zone Configuration

| Country full name | Country | zoneId |
| --- | --- | --- |
| BAHRAIN | BH | Asia/Bahrain |
| QATAR | QA | Asia/Qatar |
| KENYA | KE | Africa/Nairobi |
| ZAMBIA | ZM | Africa/Lusaka |
| UGANDA | UG | Africa/Kampala |
| TANZANIA | TZ | Africa/Dar_es_Salaam |
| GHANA | GH | Africa/Accra |
| NIGERIA | NG | Africa/Lagos |
| SRI LANKA | LK | Asia/Colombo |
| Vietnam | VN | Asia/Ho_Chi_Minh |
| Pakistan | PK | Asia/Karachi |
| Bangladesh | BD | Asia/Dhaka |

Accounting generation is described as resolving country from FMID and then resolving `zoneId` from country. New-country onboarding requires a corresponding configuration entry.

## Business Rules

`STRATEGIC_FM_LIST` is checked during SWIFT-message generation. All non-suppressed manual-entity FMIDs must be added. `SLATE_QFC` (FMID `401081696`, `SLATE ONE LLC*DOH`) must not be added because it is cashflow-suppressed.

The source links to an MX eligibility rule but does not reproduce its decision criteria or provide validation evidence.

## Assurance Limits

The checklist provides required values and reported confirmations, but no environment-specific deployment evidence, maker-checker approval, UAT execution, reconciliation result, rollback procedure, or go-live sign-off.