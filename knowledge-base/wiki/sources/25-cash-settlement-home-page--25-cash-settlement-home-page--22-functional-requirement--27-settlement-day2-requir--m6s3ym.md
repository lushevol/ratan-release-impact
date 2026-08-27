---
type: source
title: "Cash Settlement Home Page — Settlement Day 2 Swap Agent Requirement"
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6962983"
venue: "Azure DevOps"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, settlement-day-2, swap-agent, auto-netting, functional-requirement]
related: [swap-agent, murex, ratan, ratan-cash-settlement-netting-service, lms, tds3-api, sal-mtm-and-coupon-auto-netting, swap-agent-mtm-coupon-netting-separation, netting-job-retry, clearing-resultant-swift-suppression, trade-level-clearing-id-propagation, pending-auto-netting-state, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Swap Agent Day2.md"]
---
# Cash Settlement Home Page — Settlement Day 2 Swap Agent Requirement

## Scope

This functional requirement defines Settlement Day 2 auto-netting for `SWAP_AGENT` coupon and interim MTM cashflows. It also specifies SWIFT suppression for netting resultants and the display and refresh of trade identifiers in the Ratan Cashflow Blotter.

The requirement is recorded as Azure DevOps story [6962983 Swap Agent Day2](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6962983). It specifies intended behavior and does not provide evidence that the feature was implemented, UAT-passed, or enabled in production.

## Auto-netting rules

Two separate rules are required:

```text
SAL MTM Netting:
Product_Strategy = "SWAP_AGENT"
&& Payment_Type = "Interim MTM"
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

SAL Coupon Netting:
Product_Strategy = "SWAP_AGENT"
&& Payment_Type = "Coupon"
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

Eligible cashflows are grouped by booking entity, counterparty, currency (`ccy`), value date (`VD`), and payment type. Consequently, `Interim MTM` cashflows cannot net with `Coupon` cashflows. `Initial Notional` and `Final Notional` cashflows are outside the stated rule scope.

The source cashflow category is preserved in the resultant payment type:

| Source payment type | Resultant payment type |
| --- | --- |
| `Interim MTM` | `SAL MTM Netting` |
| `Coupon` | `SAL Coupon Netting` |

## Scheduling and retry

The auto-netting start time must be configurable. If the scheduled job fails, the source requires a subsequent job to retry the netting 30 minutes later. The document does not specify the scheduler, retry scope, maximum retry count, idempotency mechanism, or behavior after repeated failures.

Eligible cashflows are expected to enter `WAITING` state with sub-state `Pending Auto Netting` before processing. Successful processing changes source cashflows to `Netted` and creates a netting resultant.

## Resultant suppression and accounting

The suppression rule is:

```text
Payment_Type in ("SAL MTM Netting", "SAL Coupon Netting")
&& (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")
```

For both MTM and coupon scenarios, the resultant is expected to have:

```text
Cashflow State = SWIFT_SUPPRESSED
```

The resultant must not be sent to LMS because of its SWIFT-suppressed status. The business cases also expect an accounting entry to be generated and sent as expected. The source does not identify the accounting destination or establish whether accounting publication is independent of LMS and SWIFT delivery.

## Trade identifiers in Ratan

The Ratan Cashflow Blotter view builder must expose:

- `Clearing_Organization_Trade_Id`
- `Trade_External_Id`

Users may add these fields to a custom view. The fields are not added to the customized cashflow filter.

After a cashflow is received in Ratan, the system calls the [[tds3-api]] to retrieve the field values. If a trade event indicates that a source trade value changed, the value is refreshed for active cashflows in the following states:

```text
PROJECTED
QUEUED
WAITING
READY
```

The refresh is not notification-driven. When a user manually queries the cashflow, the latest available value is displayed. The expected values are the corresponding identifiers on the parent trade.

## Identifier mappings

### `Clearing_Organization_Trade_Id`

```text
(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href=(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeInformation/conf:relatedParty[conf:role="ClearingOrganization"]/conf:partyReference/@href]/conf:tradeId[@tradeIdScheme=[http://www.sc.com/coding-scheme/tradeId](http://www.sc.com/coding-scheme/tradeId)]
```

### `Trade_External_Id`

```text
(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))(:[@xsi:type=fn:QName('','scbextn:Trade')]:)/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href='party1']/conf:tradeId[@tradeIdScheme='http://www.sc.com/coding-scheme/tradeId/sourceSystem/tradeExternalId']
```

The mappings cover original trade structures and novation or cancel-reissue new-trade structures. The requirement does not define behavior for missing identifiers, multiple matches, inactive amended trades, or discrepancies between TDS3 and the source trade payload.

## Business scenarios

### Swap Agent MTM

Two `SWAP_AGENT` cashflows with payment type `Interim MTM` should enter `WAITING` with sub-state `Pending Auto Netting`. After the scheduled job, they should become `Netted`, and a resultant should be created with payment type `SAL MTM Netting` and state `SWIFT_SUPPRESSED`.

### Swap Agent Coupon

Two `SWAP_AGENT` cashflows with payment type `Coupon` should follow the same lifecycle, with a resultant payment type of `SAL Coupon Netting` and state `SWIFT_SUPPRESSED`.

### Initial and final exchanges

`Initial Notional` and `Final Notional` cashflows should not match the auto-netting rules.

### Clearing ID display

When a user adds the clearing organization trade identifier and external trade identifier to a customized cashflow view, the values should be displayed and should match the parent trade.

## Dependency and inactive requirement

The stated dependency is for [[murex]] to consume a new `Clearing ID` field from Murex.

The requirement to send Clearing ID downstream to TLM and RATAN EOD is struck through in the source and is therefore not treated as an active requirement. The relationship between the generic term `Clearing ID` and the two active fields remains unresolved.

## Related wiki topics

- [[sal-mtm-and-coupon-auto-netting]]
- [[swap-agent-mtm-coupon-netting-separation]]
- [[netting-job-retry]]
- [[clearing-resultant-swift-suppression]]
- [[trade-level-clearing-id-propagation]]
- [[active-cashflow-trade-identifier-refresh]]
- [[pending-auto-netting-state]]
- [[netting-resultant-cashflow]]
- [[ratan-cash-settlement-netting-service]]
- [[lms]]
- [[murex]]