---
type: source
title: "Enabling Settlement for Manual Entities"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, settlement-day-2, manual-entities, cash-settlement, functional-requirement]
related: [ratan, cash-settlement-home-page, settlement-day-2, manual-entity-settlement-enablement, manual-entity-static-data-onboarding, settlement-suppression-exceptions, ebbs-settlement-accounting, manual-entity-lms-feed, tranche-1-vs-tranche-2-manual-entities, business-rule-maintenance, nostro-static, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# Enabling Settlement for Manual Entities

## Summary

This functional requirement records the implementation and operational-readiness work required to enable settlement in [[entities/ratan]] for manual entities whose cashflows originated in Murex 2.11 but were previously suppressed in Ratan. The objective is to replace manual payment processing with Ratan-managed settlement while preserving required controls for accounting, Swift generation, business rules, suppression, LMS delivery, UAT, and CPT.

The document is an evolving implementation tracker rather than a single final specification. It contains historical proposals, corrected values, signoffs, open points, and implementation updates through August 2026. Production go-live status and a consolidated completion matrix are not established by the source.

## Scope

Botswana was removed because its branch was closing and was replaced by Qatar. The active scope contains 14 entity rows, including two distinct Qatar entities and two Sri Lankan entities. The source also refers to 12 countries, so country count and entity count should not be treated as interchangeable.

| Country or scope | Murex 2.11 entity | FMID | FMCODE | Settlement treatment |
| --- | --- | ---: | --- | --- |
| Bahrain | BAHRAIN | `10036430` | `SCB BAHRAI*MAN` | Enabled |
| Qatar | DOHA | `300010782` | `SCB DOHA*DOH` | Enabled |
| Qatar | SLATE_QFC | `401081696` | `SLATE ONE LLC*DOH` | Cashflow suppressed |
| Kenya | KENYA | `300011525` | `SCB KENYA B*NBO` | Enabled |
| Zambia | ZAMBIA | `10041903` | `SCB ZAMBIA*LUS` | Enabled |
| Uganda | UGANDA | `10041902` | `SCB UGANDA*KAM` | Enabled |
| Tanzania | TANZANIA | `10040387` | `SCB TANZANI*DAR` | Enabled |
| Ghana | GHANA | `10037477` | `SCB GHANA*ACC` | Enabled |
| Nigeria | NIGERIA | `300084297` | `SCB NIGERIA*LAG` | Enabled |
| Sri Lanka | SRI LANKA | `10036647` | `SCB COLOMBO*CMB` | Enabled |
| Sri Lanka | FCBUSLANKA | `10022098` | `SCB COL FCB*CMB` | Enabled |
| Vietnam | HANOI | `10041530` | `SCB HANOI*HNI` | Enabled |
| Pakistan | KARACHI | `10036655` | `SCB KARACHI*KHI` | Enabled |
| Bangladesh | DHAKA | `300011470` | `SCB DHAKA*DAC` | Enabled |

Historical scope entry:

```text
BOTSWANA / FMID 10036775 / SCB BOTSWAN*GBE
```

## Required implementation domains

- Nostro static data, including correspondent and account fields.
- Swift sender, Field 53, Field 58, and branch-code configuration.
- Release-cutoff time, shifter, currency, and timezone configuration.
- Non-ISO-to-ISO currency mappings.
- Currency-specific rounding.
- EBBS bridge accounts, posting branches, transaction codes, and timezones.
- NSTP and cashflow-suppression rules.
- `STRATEGIC_FM_LIST` membership.
- Cashflow Blotter currency dropdown values.
- LMS feed delivery.
- UAT and CPT readiness.

Manual entities follow the UK SSI stamping model and should not be added to `NON_UK_ENTITY_LIST`. No new CFI code or PM currency was required for the manual-entity scope.

## Canonical decisions and corrections

- `SLATE_QFC` remains cashflow-suppressed. It requires suppression configuration rather than the full settlement static-data set.
- `SLATE_QFC` is excluded from `STRATEGIC_FM_LIST` because its cashflows remain suppressed.
- All 14 active entity rows are marked for LMS feed, including `SLATE_QFC`.
- New currency mappings required on the Ratan side are `NGB -> NGN` and `PKO -> PKR`.
- Existing relevant mappings include `VNO -> VND`, `LKO -> LKR`, `BDO -> BDT`, and `NGX -> NGN`.
- The authoritative latest rounding values are `NGN`, precision `2`, `ROUNDING_OFF`, and `NGB`, precision `2`, `ROUNDING_OFF`. The earlier proposal for NGN precision `0` is obsolete.
- Tanzania uses credit transaction code `578`, corrected from `278`.
- The proposed new Tanzania settlement means `DFCC` was superseded. For DFCC, settlement means is `NOS`.
- The earlier hardcoded receiver BIC proposal for metal currencies was superseded by confirmation that applicable PM cashflows remain suppressed and no hardcoded receiver BIC is required.
- Release-cutoff values are entity- and currency-dependent. Where no configured value exists for Qatar, Tanzania, or Bangladesh, the Ratan fallback is `VD-1 business day 18:00 GMT`.

## ADO work items

The source links the following ADO stories:

`11759091`, `12529837`, `12529867`, `12529900`, `12529902`, `12529903`, `12529904`, `12529905`, `12529907`, `12529910`, `12529912`, `12529914`, `12529916`, and `12529918`.

## Related operational context

The work is part of [[concepts/settlement-day-2]] and affects the [[entities/cash-settlement-home-page]]. It extends existing concerns around [[concepts/nostro-static]], [[concepts/nostro-static-validation]], [[concepts/business-rule-maintenance]], [[concepts/clearing-swift-suppression]], and [[concepts/ratan-cashflow-lifecycle-state-machine]].

The source references Confluence material for Swift analysis, UAT, CPT, and LMS verification, as well as attached spreadsheets and message samples. These artifacts remain the detailed evidence for deployment and signoff status.