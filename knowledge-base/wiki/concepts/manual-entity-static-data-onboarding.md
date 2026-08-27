---
type: concept
title: Manual-Entity Static-Data Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [static-data, settlement, nostro, swift, release-cutoff, currency, rounding]
related: [manual-entity-settlement-enablement, nostro-static, nostro-static-validation, ebbs-settlement-accounting, cash-settlement-home-page, business-calendar-relative-netting-time]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# Manual-Entity Static-Data Onboarding

Manual-entity settlement requires coordinated onboarding across settlement instructions, messaging, timing, currency, accounting, and user-interface configuration. The source records repeated reconciliation with country users and downstream teams rather than a one-time static-data load.

## Scope of static data

Required domains include:

- Nostro accounts, settlement means, notice-to-receive values, and correspondent fields.
- Swift sender, Field 53, Field 58, and branch codes.
- Currency-specific release cutoff and shifter values.
- Non-ISO-to-ISO mappings.
- Currency precision and rounding type.
- EBBS bridge accounts and transaction codes.
- Country-to-timezone mappings.
- Cashflow Blotter currency dropdown values.

`SLATE_QFC` is an exception. Because its cashflows remain suppressed, only cashflow-suppression configuration is required for that entity.

## Release cutoff

| Entity or group | FMID | Cutoff | Shifter |
| --- | ---: | --- | --- |
| Bahrain | `10036430` | `15:00 UTC` | `VD-1BD` |
| Kenya | `300011525` | `15:00 UTC` | `VD-1BD` |
| Zambia | `10041903` | `15:00 UTC` | `VD-1BD` |
| Uganda | `10041902` | `15:00 UTC` | `VD-1BD` |
| Ghana | `10037477` | `15:00 UTC` | `VD-1BD` |
| Nigeria | `300084297` | `17:00 UTC` | `VD-1BD` |
| Sri Lanka | `10036647`, `10022098` | `13:00 UTC` | `VD-1BD` |
| Vietnam | `10041530` | `11:00 UTC` | `VD-1BD` |
| Pakistan | `10036655` | `13:00 UTC` | `VD-1BD` |
| Qatar, Tanzania, Bangladesh | `300010782`, `10040387`, `300011470` | Razor currency/entity value; otherwise `18:00 GMT` on VD-1 business day | Ratan fallback |

For Qatar, Tanzania, and Bangladesh, configured Razor values are used for non-blank currencies. A blank or unconfigured currency uses the Ratan default.

## Currency mappings

```text
NGB -> NGN
PKO -> PKR
VNO -> VND
LKO -> LKR
BDO -> BDT
NGX -> NGN
```

The first two mappings were identified as additions. The remaining listed mappings were already present or confirmed as existing.

The Cashflow Blotter currency dropdown must expose the relevant ISO and non-ISO values:

| ISO | Non-ISO |
| --- | --- |
| BHD | |
| VND | `VNO` |
| NGN | `NGO/NGY/NGH/NGX/NGA/NGB` |
| PKR | `PKH/PKO` |
| GHS | `GHH` |
| UGX | `UGH` |
| ZMW | `ZMH` |
| KES | `KEH` |
| QAR | |
| LKR | `LKO/LKH` |
| TZS | `TZH` |
| BDT | `BDO` |

## Rounding

The latest source decision is:

| Currency | Precision | Type |
| --- | ---: | --- |
| `NGN` | `2` | `ROUNDING_OFF` |
| `NGB` | `2` | `ROUNDING_OFF` |

The earlier proposal to change NGN precision from `2` to `0` is superseded.

## SSI and settlement means

Manual entities follow the UK SSI stamping model:

```text
'BranchId_Murex3Id' -> 'CFI Code' -> 'Is_Default_SSI'
```

They should not be added to `NON_UK_ENTITY_LIST`.

For Tanzania DFCC flows, the confirmed settlement means is `NOS`; no new settlement means is required on the Ratan UI. The earlier proposal to create a new `DFCC` settlement means is obsolete.