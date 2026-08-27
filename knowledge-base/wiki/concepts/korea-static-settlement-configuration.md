---
type: concept
title: Korea Static Settlement Configuration
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, cash-settlement, static-data, settlement-routing, auto-netting, NSTP, SWIFT]
related: [seoul, korea, ebbs, ratan-settlement, nostro-static-management, nostro-configuration, korea-ssi-onboarding, korea-settlement-accounting, korea-swift-mx-message-generation, nds-auto-netting, netting-key-selection, cashflow-suppression, settlement-suppression, release-cutoff-configuration, high-risk-nstp-rule, is-kro-the-intended-cpt-currency-code]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Korea Static Settlement Configuration

## Overview

Korea static settlement configuration is the set of EBBS bridge-account, SWIFT, cutoff, auto-netting, NSTP, and cashflow-suppression settings associated with [[seoul]] in the RATAN operating model.

The source is an implementation summary rather than deployment evidence. Rule ownership, completion dates, production status, and Nostro Static sign-off are not populated.

## Settlement static data

SEOUL uses FMID `10036645`, legal entity `SCB SEOUL*SEL`, and branch code `70`.

The specified EBBS bridge accounts are:

- `000287(KRW)`
- `040446(ALL)`

The branch code is held in `static-data-service`. The source provides a query joining `ratanone.ratan_static__cashflow_ebbs_bridge_account` and `ratanone.ratan_static__cashflow_ebbs_txn_code` for FMID `10036645`.

The SWIFT sender BIC is `SCBLKRSEXXX`. Field 53 BIC, Field 53 currency, and Field 58 BIC are blank. No BIC-netting rule is stated as necessary for Korea in RATAN.

## Netting and cutoff

The generic `NDS Auto Netting` configuration groups cashflows by:

- ND parent trade ID.
- Booking-entity FMID.
- Counterparty FMID.
- Payment currency.
- Payment date.

Its resultant payment type is `NDS Auto Netting`, with priority `54`. Its `is_swift_suppress_when_single_cashflow` value is `false`.

All currencies use a value-date cutoff of `01:30:00 GMT`, stated as `10:30 AM KST`.

## Korea-specific controls

The configuration separates three control families:

1. **Auto-netting:** KRX/SEL IRS, SCB/London NDF, SCB/London commodity NDF, and Seoul NDS flows.
2. **NSTP:** Korea typology, financial-institution client, loan-branch, pending NDS, and large-payment controls.
3. **Cashflow suppression:** Korean bonds, netted KRX/SEL flows, non-FMRP entities, and Korean precious-metal currencies.

These families should be evaluated independently. A cashflow being eligible for one family does not establish eligibility for another.

## Important tensions

### KRO and KRW

The KRX/SEL IRS auto-netting rule requires `Cashflow__Payment_Currency == "KRO"`, while the EBBS bridge account is labelled `KRW`. The source does not define whether `KRO` is an intentional internal code, a product-specific code, or an error. See [[queries/is-kro-the-intended-cpt-currency-code]].

### Seoul NDS scope

The generic Pending NDS Netting NSTP rule excludes Seoul, while the Seoul NDS Auto Netting rule requires Seoul. This may represent an intended split between Seoul-originated flows and other booking entities, but rule precedence and lifecycle are undocumented.

### Suppression scope

The broad non-FMRP suppression rule excludes Seoul, while dedicated Seoul suppression rules cover Korean bonds, KRX/SEL netted flows, and precious-metal currencies. The source does not specify execution order or precedence.

### Inactive inter-entity rule

The UK/Korea inter-entity netting rule is crossed out in the source. It should be treated as inactive or superseded unless an authoritative configuration confirms otherwise.

## Validation priorities

1. Confirm the `KRO`/`KRW` mapping.
2. Confirm bridge-account and branch-code sign-off and production deployment.
3. Confirm whether blank SWIFT Field 53 and Field 58 values are intentional.
4. Investigate the duplicate SCB/London NDF rule in `uat-4`.
5. Establish precedence among auto-netting, NSTP, and suppression.