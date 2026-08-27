---
type: source
title: RFR and SWAP_AGENT Functional Requirement
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, rfr, swap-agent, murex, ratan]
related: [swap-agent, rfr-payment-type-classification, blank-flows-enrichment, dummy-trade-id-management, accounting-extended-narrative-format, which-synthetic-trade-id-prefix-is-authoritative, does-an-empty-netting-id-indicate-netting, where-should-ratan-remove-dummy-trade-ids, what-is-the-authoritative-rfr-payment-type-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# RFR and SWAP_AGENT Functional Requirement

This functional requirement documents RFR cashflow handling across [[murex-2-11]] and [[ratan]], using a three-trade example with shared `LTI_ID = 5560580`. It combines 2024 payment-lifecycle examples with a payment-type mapping revision identified during UAT on 2025-01-07.

## Scope and trade-specific behavior

The example comprises three related trades:

| Trade | Typology | Documented settlement behavior |
|---|---|---|
| Trade1 | `Vanilla X-ccy swap` | Dummy notionals and MTM flows are generally not sent to RATAN; qualifying coupon flows are subject to SWIFT suppression. |
| Trade2 | `RFR CCS MTM Fixing` | Initial notional, interim MTM, and final notional are eligible for RATAN processing and shown as bilateral settlement flows. |
| Trade3 | `RFR CCS MTM Fixing` | Dummy notionals and MTM flows are generally not sent to RATAN. |

A shared `LTI_ID` does not determine settlement treatment. Processing must evaluate the individual trade, strategy, typology, flow type, dummy flag, Murex status, and payment activity.

## Latest payment-type mapping

The source supersedes an earlier coupon rule following UAT findings on 2025-01-07.

```text
Initial Notional(Trade 2): Strategy in (‘SWAP_AGENT,'RECALC') && Typology=‘RFR CCS MTM Fixing’ && FLOW_TYPE2==’INIT’

Interim MTM(Trade 2): Strategy in (‘SWAP_AGENT,'RECALC') && Typology=‘RFR CCS MTM Fixing’ && FLOW_TYPE2!=’INIT’ && X_DUMMY2==’0’

Coupon(Trade 1): Strategy in (‘SWAP_AGENT,'RECALC') && Typology=’Vanilla X-ccy swap’

Final Notional(Trade 2): Strategy in (‘SWAP_AGENT,'RECALC') && Typology=‘RFR CCS MTM Fixing’ && X_DUMMY2==’1’
```

| Mapping target | Model / path |
|---|---|
| Payment Type logic model | `Cashflow.Payment_Type` |
| Payment Type physical model | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:payment/conf:paymentType` |
| NSTP | `Instrument_Common.Murex_Product_Strategy == "SWAP_AGENT"` |
| Netting | `Cashflow.Payment_Type in ("Interim MTM", "Coupon") AND Instrument_Common.Murex_Product_Strategy == "SWAP_AGENT" AND (Cashflow.Netting_Id == "" OR Cashflow.Netting_Id == null)` |

The documented `Netting` condition is counterintuitive because it tests for a blank or null `Cashflow.Netting_Id`; its intended meaning remains unresolved.

## Settlement eligibility is not message release

For the documented `SWAP_AGENT` case, Trade2 initial and final notionals are bilateral settlement flows. Trade2 interim MTM and qualifying Trade1 coupon flows can be marked eligible for RATAN while also carrying `Swift Suppression`. Dummy flows and certain related Trade1 and Trade3 flows are not sent to RATAN.

Therefore, settlement eligibility, bilateral settlement, netting, and SWIFT suppression are separate controls. See [[settlement-suppression]] and [[cashflow-suppression]].

## Accounting narrative requirement

The clearing team requires strategy and payment-type information for TLM reconciliation and for the [[ebbs]] accounting feed.

| Target | Value |
|---|---|
| eBBS path | `data/attributes/request/transaction entry/extended-narratives` |
| eBBS field | `EXTENDEDNARRATIVE1` |
| Format | `Instrument_Common.Murex_Product_Strategy#Cashflow.Payment_Type#Cashflow.Netting_Id` |
| Missing values | Blank, with no spaces; retain separators |
| Maximum length | 65 characters, truncated from the trailing side |

```text
Swap_Agent#Bilateral netting#3297d3a6-b122-11ef-ac77-005056ac4ab7
#Bilateral Netting#3297d3a6-b122-11ef-ac77-005056ac4ab7
Swap_Agent#Interim MTM#
Swap_Agent##
#CouponFloat#
##
```

The length restriction means this narrative must not be treated as an authoritative, lossless netting identifier.

## Blank `<Flows>` enrichment

A special RFR and swap-agent auto-netting scenario between Trade1 and Trade3 can have blank `<Flows>` data. The scenario is described as coupon netting from Trade1 during MTM re-fixing, with monthly re-fixing below 10. RATAN must pre-process the payment, enrich trade and flow data, and set `VAL_STATUS` to `VALD`.

| Identifier | MxML path | Batch header |
|---|---|---|
| Strategy | `/MxPayML/strategy` | `STRATEGY` |
| Trade reference | `/MxPayML/transactionID` | `TRN_REF` |
| Typology | `/MxPayML/transactionTypology` | `TYPOLOGY` |

The qualifying indicators are strategy in `RECALC` or `SWAP_AGENT`, trade reference `0`, and blank typology.

```xml
<flow>Flowid:112517395, status:SNTR, value_date:20241211</flow>
```

The requirement describes a synthetic trade identifier derived from flow ID `112517395`, but contradicts itself: prose and snapshot data use `R112517395`, whereas real-time and batch enrichment tables show `MTR112517395`.

## Dummy-ID downstream handling options

The synthetic trade ID is not intended for downstream delivery to [[lms]], [[ebbs]], or FMSWG.

| Option | Advantage | Disadvantage |
|---|---|---|
| Remove the dummy trade ID in the first workflow task | Centralized data cleanup | Potential lock-control risk involving the trade ID |
| Retain the dummy ID in RATAN and remove it dynamically in LMS/accounting services | Avoids RATAN lock-control changes | Requires customized logic in several downstream services |

No final architecture decision is recorded.

## Source limitations

The documented lifecycle is a worked example rather than evidence that all RFR or `RECALC` trades behave identically. In particular, the source does not establish how `RECALC` payments with typologies other than `Vanilla X-ccy swap` should be classified, nor whether enrichment applies to every blank-`<Flows>` event.