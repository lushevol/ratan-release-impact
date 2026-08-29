---
type: entity
title: SWAP_AGENT
created: 2026-08-22
updated: 2026-08-22
tags: [murex, product-strategy, cash-settlement, rfr, nstp, SWAP_AGENT, cashflow-auto-netting, SAL, swap-agent, auto-netting, day2-processing]
related: [murex-2-11, ratan, rfr-payment-type-classification, auto-netting, settlement-suppression, straight-through-processing, cashflow-auto-netting, clearing-swift-suppression, auto-netting-resultant-nstp, swap-agent-mtm-coupon-netting-separation, netting-job-retry, netting-resultant-cashflow-lifecycle, trade-level-clearing-id-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---

# SWAP_AGENT

## Role and scope

`SWAP_AGENT` is a Murex product-strategy value. The source documents describe it in separate contexts:

- The RFR and Swap Agent source documents a cash-settlement scenario in which `SWAP_AGENT` drives special payment classification, suppression, and non-STP treatment in [[ratan]].
- The Auto Netting Static Go Live Process source uses `SWAP_AGENT` in SAL MTM and SAL Coupon auto-netting flows.
- The Day2 Auto Netting TestCase source covers Swap Agent as a product or processing category in [[ratan]].

The Day2 test configuration uses:

```text
Product_Strategy = "SWAP_AGENT"
Payment_Type = "Coupon"
```

## RFR cash-settlement rules

The following rules are from the RFR and Swap Agent source:

- `NSTP` is assigned when `Instrument_Common.Murex_Product_Strategy == "SWAP_AGENT"`.
- Payment types may be derived for `SWAP_AGENT` or `RECALC` using typology, `FLOW_TYPE2`, and `X_DUMMY2`; see rfr payment type classification.
- For the documented three-trade structure, dummy notional and dummy MTM flows are generally not sent to RATAN.
- Eligible interim MTM and coupon payments can be SWIFT-suppressed because settlement is handled through the clearing house.
- The source defines a `Netting` classification for `SWAP_AGENT` interim MTM and coupon payments with an empty or null `Cashflow.Netting_Id`; the intended semantics require validation.

### RFR scope boundary

These behaviors are established for the documented `SWAP_AGENT` RFR structure. The source does not establish that all swap products, all RFR trades, or all `RECALC` trades should receive the same treatment.

## Cashflow auto-netting rules

### Static go-live rule families

The following rules are from the Auto Netting Static Go Live Process source:

| Rule family | Matching condition | Additional requirements and treatment |
|---|---|---|
| SAL MTM Netting | `Cashflow__Payment_Type == "Interim MTM"` | Requires an empty or null `Cashflow__Netting_Id` and uses NSTP for Maker+Checker. |
| SAL Coupon Netting | `Cashflow__Payment_Type == "Coupon"` | Requires an empty or null `Cashflow__Netting_Id` and uses NSTP for Maker+Checker. |

The corresponding suppression logic also covers single auto-netted cashflows without a netting ID.

### Day2 tested behavior

According to the Day2 Auto Netting TestCase source, Swap Agent auto-netting groups eligible cashflows with matching attributes, including:

- Booking entity
- Counterparty
- Currency
- Value date

Cashflows with differing attributes are not netted.

The Day2 source explicitly separates `MTM` and `Coupon` cashflows. They must not be netted together; each produces its own resultant type:

- `SAL or SWAP AGENT MTM Netting`
- `SAL or SWAP AGENT Coupon Netting`

The source records a 30-minute retry after an initial netting-job failure. Netting resultants of both MTM and Coupon types are suppressed, while the original cashflows remain unaffected.

## Clearing ID traceability

For Murex cashflows, a Clearing ID contained in the trade UDF is displayed in the Cashflow Blotter. The Clearing ID field is blank for non-Murex cashflows. See [[trade-level-clearing-id-propagation]].

## Test evidence

The Day2 Auto Netting TestCase source records matching expected and actual results for the Swap Agent cases. Formal test-status fields are blank.