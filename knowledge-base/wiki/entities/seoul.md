---
type: entity
title: SEOUL
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-entity, Korea, RATAN, EBBS, SWIFT]
related: [korea, ebbs, ratan-settlement, korea-static-settlement-configuration, korea-ssi-onboarding, korea-settlement-accounting, korea-swift-mx-message-generation, krx]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# SEOUL

## Identity

- Entity: `SEOUL`
- FMID: `10036645`
- Legal entity and FM code: `SCB SEOUL*SEL`
- Branch code: `70`

SEOUL is the central Korea booking and settlement entity described in the Korea cash settlement migration. It is associated with [[entities/korea]] and processes the Korea-specific settlement rules in [[entities/ratan-settlement]].

## EBBS bridge accounts

The source specifies two EBBS bridge accounts:

| Currency label | Account | Branch code |
| --- | --- | --- |
| KRW | `000287` | `70` |
| ALL | `040446` | `70` |

The branch code is sourced from a `static-data-service` file. The source does not provide sign-off or deployment confirmation for these values.

## SWIFT static data

The sender BIC is `SCBLKRSEXXX`.

Field 53 BIC, Field 53 currency, and Field 58 BIC are blank in the source. The source also states that no BIC-netting rule is needed in RATAN for Korea.

## Rule participation

SEOUL is explicitly selected by FMID `10036645` in rules for:

- Structured Swap, `Red Trades-StrucSwap`, and `SLT-Cust` NSTP.
- Financial-institution client NSTP.
- `LN_BR` NSTP.
- Payments of at least USD 500 million NSTP.
- Korean bond suppression.
- KRX/SEL netted-cashflow suppression.
- Korean precious-metal suppression.
- KRX/SEL IRS auto-netting.
- SCB/London NDF and commodity NDF auto-netting.
- Seoul NDS Auto Netting.

The generic Pending NDS Netting NSTP rule explicitly excludes SEOUL through `Entity__Booking_Entity_SCI_FMID != "10036645"`.

## Open validation points

The `KRO` currency condition in the KRX/SEL IRS auto-netting rule conflicts with the `KRW` label on the KRW bridge account. This is tracked in [[queries/is-kro-the-intended-cpt-currency-code]].