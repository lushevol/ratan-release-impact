---
type: source
title: FXU - RATAN Analysis
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/DSP/FXU+Tech+Detail+Design"
venue: Internal functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [fx-utilization, cash-settlement, functional-requirement, ratan, fto]
related: [fxu, ratan, blade, stella, scpay, s2bx, tlm, fx-utilization, utilization-remaining-amount, utilization-status-lifecycle, partial-and-pastdue-utilization-accounting, utilization-request-idempotency, utilization-settlement-method-conversion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md"]
---
# FXU - RATAN Analysis

This internal functional-requirement and solution-design document defines proposed FX Utilization behaviour across [[fxu]], [[ratan]], [[blade]], [[stella]], [[scpay]], and associated accounting and reconciliation systems. It is a mixed-maturity source: it distinguishes MVP scope from Phase 2 proposals and records open questions, TBC configuration, and pending ADO priorities.

## Scope and system roles

FX Utilization applies client payment instructions to eligible FX settlement amounts before settlement/value date. Transaction Banking Operations retrieve deals in SCPAY/FX Util, apply payment instructions linked with an AA code, and submit utilization details to RATAN.

RATAN is intended to validate requests, retain and expose remaining amounts, control utilization statuses, prevent gross settlement for `UTIL` cashflows, publish accounting to [[ebbs]], and distribute utilization information to downstream consumers including TLM, RATAN EOD, SSDR, and FMMIS.

The MVP is limited to full utilization on value date. Partial utilization, PastDue utilization, reversal, and early utilization are described as Phase 2 capabilities.

## Intended MVP controls

- Eligible products are FX Spot, Forward, and Swap.
- Eligible and auto-utilization-eligible clients require static-data setup.
- S2BX-originated trades may be stamped `UTIL` based on utilization-client static data; BLADE users may select `UTIL` when booking manually.
- BLADE should expose a client ID (`SCI LEID`) and remaining amount retrieved from RATAN.
- RATAN should reject FXU utilization requests for cancelled or already-utilized trades.
- Utilized trades must be hard-blocked from market events in BLADE for every profile, including MO. Financial amendments require utilization reversal first.
- RATAN should record whether a utilization was initiated by FXU, auto utilization, or manual utilization.
- `FXBRREC-M` is proposed as the default settlement means for manually booked `UTIL` trades whose client is absent from utilization static.

The authoritative location of Util Client Static—S2BX, BLADE, or STELLA—is unresolved. See [[where-is-the-authoritative-util-client-static-maintained]].

## Proposed utilization flow

For manual full utilization, FXU queries RATAN for the remaining amount and required details, submits a utilization request through Solace, and receives an asynchronous ACK/NACK response from RATAN. Auto utilization is proposed to occur on value date based on a trade-level indicator, a counterparty flag, and settlement means `FXBRREC`.

The source requires retry handling using the same utilization ID, processing of late ACK/NACK responses after a timeout, and safe handling of multiple responses for one request. The API schema, error catalogue, correlation key, and idempotency contract are not supplied. See [[what-is-the-fxu-ratan-utilization-api-and-idempotency-contract]].

## Proposed status and lifecycle model

The document uses the following terms:

- `UTILIZED`: full original amount utilized and remaining amount is zero.
- `PARTIALLY-UTILIZED`, `PARTIALUTILIZED`, and `PARTIALUTIL`: variants describing a non-zero remaining amount.
- `PASTDUE`: no utilization by value-date EOD, with `Pastdue` also described as a sub-status.

Partial and PastDue statuses are explicitly marked outside MVP scope, despite being referenced in solution-design controls. Canonical naming and release applicability remain open. See [[what-is-the-canonical-fx-utilization-status-and-sub-status-model]].

## Phase 2 proposals

Phase 2 proposes contract-level partial utilization, PastDue utilization, reversal, and early utilization:

- Partial utilization retains a remaining amount and uses `PARTIALLY-UTILIZED`.
- At the configured cutoff, the remaining amount may be settled through a Past Due Account and marked `Pastdue`.
- A subsequent post-value-date utilization first reverses the Past Due position, then posts the utilization amount.
- Reversal restores the remaining amount through opposite Bridge/FXBRREC postings.
- Early utilization may begin from VD-10; RATAN updates the balance upon request but sends accounting to EBBS at SOD on value date.

The MVP text instead says requests after value date should be rejected and unutilized cashflows should be auto-utilized to FXBRREC at EOD. The effective post-value-date behaviour and accounting model are unresolved. See [[what-is-the-authoritative-pastdue-and-auto-utilization-accounting-model]].

## Configured timing proposal

| Entity | Auto Util (GMT) | Auto Util (Local Timing) |
| --- | --- | --- |
| EG | 16:30 | 18:30 |
| SA | 16:30 | 19:30 |
| NP | 15:15 | 21:00 |

The source states that PastDue timing is the same as auto-utilization timing but runs after auto utilization. Timing was also marked TBC in the design notes.

## Pending priorities ADOs

| | Priority | Impacted Application | Requirement | Comment |
| --- | --- | --- | --- | --- |
| 1 | Must to Have | FXU | FXU should show the Auto Utilized trades in FXU GUI when Department query the trade in FXU. | MVP Leftover requirement |
| 2 | Must to Have | FXU, Ratan | Identify Client Leg for S2BX trade id. | MVP Leftover requirement |
| 3 | Must to Have | Ratan | **Push Util to Gross** - For hybrid customer (customer who can settle both as Gross/Util) in this case we should be able to settle as gross for util cashflows. Currently this is achieved by doing CnR in Razor and changing the settlement method. | ideally blade should amend settlement method on trade level? |
| 4 | Must to Have | Ratan | **Push Gross to Util** - Some client may be available for both gross and util, so if trade is booked as gross, but need to settle as Util ~~not for EG/NP/SA, ~~set FXBRREC-M as default settlement means | ideally blade should amend settlement method on trade level? |
| 5 | Must to Have | Ratan | Support **utilization window** beyond VD-10 for SA, VD-5 EG, directly materalize UTIL cashflow once received ** ** | @Chongxuan Li |
| 6 | Medium | Ratan, FXU | EOD report to FXU, which contains auto-utilization ~~and pastdue ~~trade info. | duplicate with No. 1 |
| 7 | Must to Have | Ratan, FXU | New API to provide utilization currency 2 and amount to FXU. | @Fengke Wu |
| 8 | Must to Have | Ratan, FXU | Utilization response API fields enrichment for FXU. Including utilization request and remaining amount | @Fengke Wu |
| 9 | | Ratan | Non-financial amendment, RATAN will not reject util request Validation for trade is amended, to be identified from 6 elements instead of trade major version. | |
| 10 | | Ratan | Consider cancellation fee/amendment fee in utilization trade, to be supported in FMRP. | |
| 11 | | Ratan | If post utilization, amendment happens, withdrawal and new need to be supported to process further utilization request. 1. 1. 1. Dependency on Rajesh to confirm no concern from FXU ops. | |
| 12 | Must to Have | FXU | FXU would validate any cashflow in ERROR status, FXU would block the util. (for scenario: If post utilization, amendment/ withdrawal happens) | |
| 13 | | Ratan | Static - Bulk uploader | |
| 14 | | Ratan | Static - Additional comments column to update source ref before approving | |
| 15 | | Ratan | Static - Differentiate the addition / deletion / amendment requests in colors under the verification queue | |
| 16 | | FXU | FXU-TLM Enrichment report, to check with Karthick/Gopi | |
| 17 | Must to Have | FXU | 1. Retry mechanize for util request with same util id? if timeout 2. Process late ACK/NACK message from Ratan post timeout. 3. Handle multi response from Ratan for the same util id, only process the ACK message no matter the sequence. | |
| 18 | Must to have | Ratan, FXU | IMS header to be added | |
| 19 | Medium | Ratan, FXU | Decimal tolerance handling in Ratan for ScPay -> FXU -> Ratan Maker ID will be ScPay, Checker ID will be empty. | identify SC Pay All full utilization? |
| 20 | | Ratan | Pastdue Dashboard for financial GRU team. | |
| 21 | | Ratan | Remaining amount API (In post trade portal, already done by a demo) in Blade. | |
| 22 | Medium | Ratan | Functionality to reverse of pastdue would be required in Ratan, as the action can be performed by FMO. Post reverse of pastdue, pastdue amount would be reversed and move to FXBRREC account. | |
| 23 | | FXU | Trade ID should be Blade trade id in utilization request | |

## Static data

| Entity | Branch Code | FMID | Sender's BIC (SCB Booking Entity BIC) | Field 53 BIC (Rule1) | Field 53 CCY to be Used | Field 58 BIC (Rule 2) |
| --- | --- | --- | --- | --- | --- | --- |
| Egypt | 34 | 401036553 | SCBLEGCAXXX | SCBLEGCAXXX | EGP | SCBLEGCAXXX |
| Nepal | 47 | 400007847 | SCBLNPKAXXX | SCBLNPKAXXX | NPR | SCBLNPKAXXX |
| Saudi | 16 | 400991880 | SCBLSAR2XXX | SCBLSAR2FMO | SAR | SCBLSAR2FMO |
| | | | | | | |

## User-case accounting data

The source provides example entries for cashflows 101 (USD) and 102 (identified as SAR). The accounting currency for cashflow 102 is repeatedly `ZAR`; the source does not explain this difference.

```text
#1 Partial Util of 400K USD on Value Date
101 | USD | Remaining 600,000 | PARTIALLY-UTILIZED | FXBR Account 101.1 USD Dr 400,000 | Bridge Account 101.1 USD Cr 400,000 | SCPAY001 | 10001
102 | SAR | Remaining 2,250,000 | PARTIALLY-UTILIZED | FXBR Account 102.1 ZAR Cr 1,500,000 | Bridge Account 102.1 ZAR Dr 1,500,000 | SCPAY001 | 10001

#2 Partial Util of 200K USD on Value Date
101 | USD | Remaining 400,000 | PARTIALLY-UTILIZED | FXBR Account 101.2 USD Dr 200,000 | Bridge Account 101.2 USD Cr 200,000 | SCPAY002 | 10002
102 | SAR | Remaining 1,500,000 | PARTIALLY-UTILIZED | FXBR Account 102.2 ZAR Cr 750,000 | Bridge Account 102.2 ZAR Dr 750,000 | SCPAY002 | 10002

#3 Partial Util of 100 K USD on Value Date
101 | USD | Remaining 300,000 | PARTIALLY-UTILIZED | FXBR Account 101.3 USD Dr 100,000 | Bridge Account 101.3 USD Cr 100,000 | SCPAY003 | 10003
102 | SAR | Remaining 1,125,000 | PARTIALLY-UTILIZED | FXBR Account 102.3 ZAR Cr 375,000 | Bridge Account 102.3 ZAR Dr 375,000 | SCPAY003 | 10003

#4 Util Reversal of 200K USD on Value Date
101 | USD | Remaining 500,000 | PARTIALLY-UTILIZED | FXBR Account 101.4 USD Cr 200,000 | Bridge Account 101.4 USD Dr 200,000 | SCPAY002 | 10002
102 | SAR | Remaining 1,875,000 | PARTIALLY-UTILIZED | FXBR Account 102.4 ZAR Dr 750,000 | Bridge Account 102.4 ZAR Cr 750,000 | SCPAY002 | 10002

#5 Past Due Settlement at EOD
101 | USD | Remaining 500,000 | PARTIALLY-UTILIZED + Pastdue | Past Due Account 101.5 USD Dr 500,000 | Bridge Account 101.5 USD Cr 500,000
102 | SAR | Remaining 1,875,000 | PARTIALLY-UTILIZED + Pastdue | Past Due Account 102.5 ZAR Cr 1,875,000 | Bridge Account 102.5 ZAR Dr 1,875,000

#6 Partial Util of 100 K USD from Past Due post value date
101 | USD | Remaining 400,000 | PARTIALLY-UTILIZED + Pastdue | Past Due reversal: 500,000 USD | New utilization: 100,000 USD | SCPAY004 | 10004
102 | SAR | Remaining 1,500,000 | PARTIALLY-UTILIZED + Pastdue | Past Due reversal: 1,875,000 ZAR | New utilization: 375,000 ZAR | SCPAY004 | 10004

#7 Past Due Settlement at EOD
101 | USD | Remaining 400,000 | PARTIALLY-UTILIZED + Pastdue | Past Due Account 101.8 USD Dr 400,000 | Bridge Account 101.8 USD Cr 400,000
102 | SAR | Remaining 1,500,000 | PARTIALLY-UTILIZED + Pastdue | Past Due Account 102.8 ZAR Cr 1,500,000 | Bridge Account 102.8 ZAR Dr 1,500,000

#8 Full Util of 400 K USD from Past Due post value date
101 | USD | Remaining 400,000 | UTILIZED | Past Due reversal: 400,000 USD | FXBR/Bridge utilization: 400,000 USD | SCPAY004 | 10005
102 | SAR | Remaining 1,500,000 | UTILIZED | Past Due reversal: 1,500,000 ZAR | FXBR/Bridge utilization: 1,500,000 ZAR | SCPAY004 | 10005
```

The examples are design input, not approved accounting policy. See [[is-sar-to-zar-in-the-fxu-ratan-user-case-table-an-intended-fx-conversion-or-a-data-error]].