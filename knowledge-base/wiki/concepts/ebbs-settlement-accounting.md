---
type: concept
title: EBBS Settlement Accounting
created: 2026-08-22
updated: 2026-08-22
tags: [ebbs, accounting, settlement, ratan, manual-entities]
related: [manual-entity-settlement-enablement, manual-entity-static-data-onboarding, ratan, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# EBBS Settlement Accounting

EBBS settlement accounting is the downstream accounting path for the manual-entity settlement scope. Ratan determines the country from the FMID, resolves the configured timezone, and submits accounting using entity-specific bridge-account and transaction configuration.

## Bridge accounts

| FMID | Legal entity / FMCODE | EBBS bridge account |
| ---: | --- | --- |
| `10036430` | `SCB BAHRAI*MAN` | `09906397050` |
| `300010782` | `SCB DOHA*DOH` | `09473025940` |
| `401081696` | `SLATE ONE LLC*DOH` | `NA` |
| `300011525` | `SCB KENYA B*NBO` | `0062599158900` |
| `10041903` | `SCB ZAMBIA*LUS` | `0062599158900` |
| `10041902` | `SCB UGANDA*KAM` | `0062599158900` |
| `10040387` | `SCB TANZANI*DAR` | `0062599158900` |
| `10037477` | `SCB GHANA*ACC` | `0062599150800` |
| `300084297` | `SCB NIGERIA*LAG` | `9625047537` |
| `10036647` | `SCB COLOMBO*CMB` | `09995954893` |
| `10022098` | `SCB COL FCB*CMB` | `09995954895` |
| `10041530` | `SCB HANOI*HNI` | `09434372001` |
| `10036655` | `SCB KARACHI*KHI` | `09900006470` |
| `300011470` | `SCB DHAKA*DAC` | `09111178468` |

`SLATE_QFC` has no bridge account because its cashflows remain suppressed.

## EBBS transaction configuration

| FMID | Country | Posting branch | Txn type code | Dr txn code | Cr txn code |
| ---: | --- | --- | --- | ---: | ---: |
| `10037477` | GH | `00001` | `RTN` | `478` | `278` |
| `10041530` | VN | `099` | `RTN` | `478` | `378` |
| `300011525` | KE | `07800` | `RTN` | `478` | `278` |
| `300084297` | NG | `00100` | `RTN` | `478` | `278` |
| `10040387` | TZ | `08700` | `RTN` | `478` | `578` |
| `10041902` | UG | `00001` | `RTN` | `478` | `278` |
| `10041903` | ZM | `01700` | `RTN` | `478` | `278` |
| `300011470` | BD | `068` | `RTN` | `478` | `378` |
| `10036655` | PK | `001` | `RTN` | `478` | `678` |
| `10036647` | LK | `093` | `RTN` | `478` | `378` |
| `10022098` | LK | `093` | `RTN` | `478` | `378` |
| `10036430` | BH | `055` | `RTN` | `478` | `378` |
| `300010782` | QA | `042` | `RTN` | `478` | `378` |

The Tanzania credit transaction code is `578`. The source records that this was changed from `278`; the correction is production-sensitive.

## Accounting timezones

| Country | Code | Zone ID |
| --- | --- | --- |
| Bahrain | `BH` | `Asia/Bahrain` |
| Qatar | `QA` | `Asia/Qatar` |
| Kenya | `KE` | `Africa/Nairobi` |
| Zambia | `ZM` | `Africa/Lusaka` |
| Uganda | `UG` | `Africa/Kampala` |
| Tanzania | `TZ` | `Africa/Dar_es_Salaam` |
| Ghana | `GH` | `Africa/Accra` |
| Nigeria | `NG` | `Africa/Lagos` |
| Sri Lanka | `LK` | `Asia/Colombo` |
| Vietnam | `VN` | `Asia/Ho_Chi_Minh` |
| Pakistan | `PK` | `Asia/Karachi` |
| Bangladesh | `BD` | `Asia/Dhaka` |

If a new country is onboarded, its country-to-zone mapping must be configured before accounting generation.

## Accounting exclusions

The source records no additional PM-currency accounting requirement for the manual entities because no applicable PM currency was planned for go-live. Existing exclusions for specified entities and PM currencies remain a separate control and must not be removed without confirmation.