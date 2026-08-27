---
type: source
title: Tranche 1 Manual-Entity Go-Live Checklist
created: 2026-08-23
updated: 2026-08-23
tags: [manual-entities, settlement-day-2, go-live, tranche-1, static-data, ebbs]
related: [go-live-readiness-for-manual-entity-settlement, ebbs, ebbs-accounting-configuration, non-iso-to-iso-currency-mapping, what-is-the-authoritative-tranche-1-manual-entity-go-live-schedule, what-is-the-authoritative-strategic-fm-list-treatment-for-slate-qfc, what-are-the-razor-derived-release-cutoff-values-for-bangladesh-and-tanzania]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
authors: []
year: 2026
url: ""
venue: "Internal operational checklist"
---
# Tranche 1 Manual-Entity Go-Live Checklist

This operational checklist records intended readiness inputs for Tranche 1 manual-entity settlement enablement across Kenya, Tanzania, Vietnam, Bangladesh, Sri Lanka, Pakistan, and Zambia. It covers RATAN and ISO dates, reference data, SWIFT data, release cutoffs, non-ISO currency mappings, EBBS accounting configuration, timezone setup, MX eligibility, business rules, UAT sign-off artefacts, and CPT links.

It is configuration and readiness evidence, not a self-contained production-approval record. Several completion columns are blank, and MX rules, cashflow-suppression rules, UAT communications, cutoff evidence, and CPT results are external resources.

## Go-live dates as recorded

The column layout and values are ambiguous. In particular, several dates omit a year, while Vietnam and Zambia contain multiple unlabelled date values. Do not treat this table as an authoritative chronological release schedule; see [[what-is-the-authoritative-tranche-1-manual-entity-go-live-schedule]].

| S.No | Tranche 1 Country | RATAN Technical Go live date | RATAN Business Go live date | ISO Go live date |
| --- | --- | --- | --- | --- |
| 1 | KE | 8-Aug-2026 | 24-Aug-2026 | 13-Jun |
| 2 | TZ | 13-Jun |
| **3** | **VN** | **10-10-2026**** 22-Aug 03-Oct** |
| 4 | BD | 05-Sep |
| 5 | LK | 05-Sep |
| 6 | PK | 05-Sep |
| **7** | **ZM** | **22-08-2026**** 17-Oct** |

## Nostro static data

| Country | MX2.11 Entity | FMID | FMCODE | Nostro static data |
| --- | --- | --- | --- | --- |
| Kenya | KENYA | 300011525 | SCB KENYA B*NBO | |
| Zambia | ZAMBIA | 10041903 | SCB ZAMBIA*LUS |
| Tanzania | TANZANIA | 10040387 | SCB TANZANI*DAR |
| Sri Lanka | SRI LANKA | 10036647 | SCB COLOMBO*CMB |
| FCBUSLANKA | 10022098 | SCB COL FCB*CMB |
| Vietnam | HANOI | 10041530 | SCB HANOI*HNI |
| Pakistan | KARACHI | 10036655 | SCB KARACHI*KHI |
| Bangladesh | DHAKA | 300011470 | SCB DHAKA*DAC |

The `FCBUSLANKA` row is structurally misaligned against the header and requires clarification before it is used as canonical reference data.

## SWIFT static data

| Entity FMCODE | Country Code | Branch code | FMID | Sender Bic | Field 53 BIC(Rule1) | Field 53 CCY to be used | Field 58 BIC(Rule2) | Swift Static Data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCB HANOI*HNI | VN | 29 | 10041530 | SCBLVNVXXXX | SCBLVNVXFMO | VND | SCBLVNVXFMO | |
| SCB KARACHI*KHI | PK | 97 | 10036655 | SCBLPKKXXXX | SCBLPKKXXXX | PKR | SCBLPKKXXXX |
| SCB ZAMBIA*LUS | ZM | 52 | 10041903 | SCBLZMLXXXX | SCBLZMLXFMO | ZMW | SCBLZMLXFMO |
| SCB KENYA B*NBO | KE | 39 | 300011525 | SCBLKENXXXX | SCBLKENXFMO | KES | SCBLKENXFMO |
| SCB COLOMBO*CMB | LK | 84 | 10036647 | SCBLLKLXXXX | SCBLLKLXXXX | LKR | SCBLLKLXXXX |
| SCB COL FCB*CMB | LK | 85 | 10022098 | SCBLLKLXXXX | SCBLLKLXXXX | LKR | SCBLLKLXXXX |
| SCB TANZANI*DAR | TZ | 50 | 10040387 | SCBLTZTXXXX | SCBLTZTXFMO | TZS | SCBLTZTXFMO |
| SCB DHAKA*DAC | BD | 86 | 300011470 | SCBLBDDXXXX | SCBLBDDXXXX | BDT | SCBLBDDXXXX |

The blank final column means the source does not itself demonstrate that the listed SWIFT static data was deployed.

## Branch-code reference data

| | Country | Branch Code | FMID |
| --- | --- | --- | --- |
| 1 | Vietnam | 29 | 10041530 |
| 2 | Pakistan | 97 | 10036655 |
| 3 | Zambia | 52 | 10041903 |
| 4 | Kenya | 39 | 300011525 |
| 5 | Sri Lanka | 84 | 10036647 |
| 6 | Sri Lanka | 85 | 10022098 |
| 7 | Tanzania | 50 | 10040387 |

## Release cutoff configuration

| | Country | FMID | FMCODE | cut_off_time | cut_off_shifter | Release cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Kenya | 300011525 | SCB KENYA B*NBO | 15:00 UTC | VD-1BD | 📎 [Release CutOff.xlsx](attachments/Release CutOff.xlsx) |
| 2 | Zambia | 10041903 | SCB ZAMBIA*LUS | 15:00 UTC | VD-1BD |
| 3 | Vietnam | 10041530 | SCB HANOI*HNI | 11:00 UTC | VD-1BD |
| 4 | Bangladesh | 300011470 | SCB DHAKA*DAC | | Confirmed with Deepak and user ,will use the Currency /Shifter/Time/Timezone from Razor |
| 5 | Sri Lanka | 10022098/10036647 | SCB COLOMBO*CMB/SCB COL FCB*CMB | 13:00 UTC | VD-1BD |
| 6 | Tanzania | 10040387 | SCB TANZANI*DAR | | Confirmed with Deepak and user ,will use the Currency /Shifter/Time/Timezone from Razor |
| 7 | Pakistan | 10036655 | SCB KARACHI*KHI | 13:00 UTC | VD-1BD |

Bangladesh and Tanzania are stated to inherit Currency/Shifter/Time/Timezone from Razor, but the actual inherited values and validation evidence are not included. See [[what-are-the-razor-derived-release-cutoff-values-for-bangladesh-and-tanzania]].

## Non-ISO to ISO currency mapping

`NGB-NGN,PKO-PKR need to be added on Ratan side,for the others ,keep as is`

| **PKO** | **PKR** | 2026-01-20 Confirmed with @Cordelia Sumita K Thirunavukarasu For Pakistan, Non ISO to ISO mapping is PKO -PKR, doesn't exist in current mapping list, need to be added |
| --- | --- | --- |

The source records an intended RATAN mapping change, not confirmation that either mapping was implemented. See [[non-iso-to-iso-currency-mapping]].

## EBBS bridge accounts

`2026-03-09 Yashas provided the data ,but QATAR and Bangladesh need to be double confirm`

| id | closing_entity | legal_entity | fmid | ebbs_bridge_account |
| --- | --- | --- | --- | --- |
| | | SCB KENYA B*NBO | 300011525 | 0062599158900 |
| | | SCB ZAMBIA*LUS | 10041903 | 0062599158900 |
| | | SCB TANZANI*DAR | 10040387 | 0062599158900 |
| | | SCB COLOMBO*CMB | 10036647 | 09995954893 |
| | | SCB COL FCB*CMB | 10022098 | 09995954895 |
| | | SCB HANOI*HNI | 10041530 | 09434372001 |
| | | SCB KARACHI*KHI | 10036655 | 09900006470 |
| | | SCB DHAKA*DAC | 300011470 | 09111178468 |

The source flags Bangladesh and Qatar for double confirmation, but Qatar has no row in this table.

## EBBS posting branches and transaction codes

`2026-06-15 Got update from ebbs that Cr Txn Code should be update to 578 from 278 for TZ`

| FMID | Country | Posting Branch | Txn Type code | Dr Txn Code | Cr Txn Code |
| --- | --- | --- | --- | --- | --- |
| 10041530 | VN | 099 | RTN | 478 | 378 |
| 300011525 | KE | 07800 | RTN | 478 | 278 |
| 10040387 | TZ | 08700 | RTN | 478 | 578 |
| 10041903 | ZM | 01700 | RTN | 478 | 278 |
| 300011470 | BD | 068 | RTN | 478 | 378 |
| 10036655 | PK | 001 | RTN | 478 | 678 |
| 10036647 | LK | 093 | RTN | 478 | 378 |
| 10022098 | LK | 093 | RTN | 478 | 378 |

The latest stated Tanzania credit transaction code is `578`. See [[ebbs-accounting-configuration]].

## Timezone configuration

`When generate accounting ,system will get country by fmid from above static table ,then get zoneid via country, if there is new country on boarding ,we need to config this`

`2026-03-13`

`Provided by J, Madhankumar and Yashas`

| KENYA | KE | Africa/Nairobi |
| --- | --- |
| ZAMBIA | ZM | Africa/Lusaka |
| TANZANIA | TZ | Africa/Dar_es_Salaam |
| SRI LANKA | LK | Asia/Colombo |
| Vietnam | VN | Asia/Ho_Chi_Minh |
| Pakistan | PK | Asia/Karachi |
| Bangladesh | BD | Asia/Dhaka |

## MX bifurcation and business rules

The checklist identifies MX bifurcation as a go-live dependency but does not reproduce the rule. It links to the [MX Eligibility Rule](https://confluence.global.standardchartered.com/display/DSP/02+Swift+Message+Analysing+for+manual+entities#id-02SwiftMessageAnalysingformanualentities-MXEligibilityRule).

Cashflow suppression is referenced through `Business rule0811.xlsx`, which is not included. The source should therefore not be used to infer the full rule content. See [[manual-entity-swift-mx-bifurcation]] and [[cashflow-suppression-rule]].

## UAT and CPT evidence

The source groups KE/TZ/BD/LK/PK/ZM/VN under one UAT sign-off row and provides links to `.msg` communications, including country training-UAT correspondence, manual-entity functional-test sign-off, and LMS approval requests. It does not establish a dated, independently auditable approval result for every country.

CPT and LMS verification are referenced through external Confluence pages:

- [Tranche 1 operational readiness and post-go-live issue tracker](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3790204945)
- [CPT - Tranche1 - LMS verification](https://confluence.global.standardchartered.com/display/DSP/01+CPT+-Tranche1-LMS+verification)

## `STRATEGIC_FM_LIST` exception

The checklist states that SWIFT generation checks whether an entity is in `STRATEGIC_FM_LIST`. It further states that cashflow-suppressed `SLATE_QFC` does not require configuration in that list, while other manual entities require FMID addition.

| SLATE_QFC | 401081696 | SLATE ONE LLC*DOH |
| --- | --- | --- |

The displayed row and accompanying prose are in tension. The row may represent an existing configuration, exception record, or stale entry. See [[what-is-the-authoritative-strategic-fm-list-treatment-for-slate-qfc]] and [[why-is-slate-one-not-configured-for-downstream-settlement-processing]].