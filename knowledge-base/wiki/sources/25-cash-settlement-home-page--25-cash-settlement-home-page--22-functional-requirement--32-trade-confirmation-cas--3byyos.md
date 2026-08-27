---
type: source
title: "Trade Confirmation & Cashflow STP"
created: 2026-08-24
updated: 2026-08-24
tags: [functional-requirement, cashflow-stp, trade-confirmation, ratan, tds3, murex-211, stella]
related: [ratan, tds3, murex-211, stella, cdu, solace, trade-confirmation-driven-cashflow-stp, trade-cashflow-correlation-by-trade-version, murex-comp-confirmation-exception-resolution]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Trade Confirmation & Cashflow STP

## Summary

This functional requirement defines a target-state control in which trade affirmation or confirmation status drives cashflow STP/NSTP processing in [[ratan]].

[[tds3]] is proposed as Ratan's universal golden source for trade updates. It receives Murex 2.11 MxML and Stella trade SCBML, persists normalized trade data using a DM-defined logical and physical model, and publishes generic trade SCBML for Ratan consumption.

The requirement distinguishes two correlation approaches:

- Stella trade and cashflow data are linked by `Trade_ID` and `Trade_Lake_Trade_Major_version`.
- Murex 2.11 trade status is linked to cashflows by matching `Source_System_Trade_Internal_Id` from trade SCBML to cashflow `Trade_Id`.

For Murex, `Source_System_Validation_Status = COMP` permits Ratan to close `Pending Confirmation/Affirmation`. Ratan moves the cashflow to STP only when that exception is the only remaining exception.

## Target Integration Flow

1. Murex 2.11 generates MxML when a trade market event or trade-status movement occurs and sends it to TDS3.
2. TDS3 converts Murex MxML into SCBML and persists it according to the logical-model pattern.
3. Stella sends DM-defined trade SCBML to TDS3 when a trade market event or trade-status movement occurs.
4. TDS3 persists Stella trade records using the DM logical-model schema.
5. Ratan consumes generic trade SCBML from TDS3 as the universal golden source of trade updates.

This is a functional requirement, not implementation evidence. It provides neither delivery status nor an authoritative deployed-interface specification.

## Stella Trade and Cashflow Correlation

The source identifies the following Stella logical-model attributes but does not provide their SCBML paths.

| Logical Model Name | SCBML Path |
|---|---|
| `Trade_ID` |  |
| `Trade_Lake_Trade_Major_version` |  |

Ratan is expected to use the pair `Trade_ID` and `Trade_Lake_Trade_Major_version`, present in both trade and cashflow data, as the correlation identifier.

A Stella trade status of `AFFIRMED`, `CONFIRMED`, or `NONCONFIRMED` permits closure of the `Pending Confirmation/Affirmation` cashflow exception. The source does not state whether closure under the Stella rule promotes a cashflow to STP.

## Stella Business-Case Matrix

| Stella Trade Business Event | Stella Trade Action | Trade ID/Major Version | Cashflow Event/ID | Cashflow Major Version | CDU Confirmation Status | Cashflow STP With CDU Confirmation Status |
|---|---|---|---|---|---|---|
| Trade | Book | T1 + V1 | New + C1 | V1 | T1 + V1 | Y |
| Trade | Cancel | T1 + V2 | Withdrawal + C1 | V2 | NA | 1. No confirmation status for trade withdrawal 2. Cashflow withdrawal event from trade cancellation is special STP case, wont' go to any settlement exception handling( SSI checking/NSTP checking/Suppression checking etc). |
| Withdrawal | Book | T1 + V2 | Withdrawal + C1 | V2 | NA | Same as above |
| Trade | Update | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| Amendment | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| PartialTermination | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| Termination | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y |  |
| Fixing |  |  | New |  | NA |  |
| Novation | Book | T1 + V2 | Withdrawal + C1 New +C2 | V2 | Y | 1. CDU will do the confirmation on latest major version |
| CloseOut | Book | T1 + V1 | New + C1 | V1 | T1 + V1 | Y |
| PortfolioReassignment | Book |  | Withdrawal(Old trade) |  | Y |  |
| Trade | Revive | T1 + V3 | Withdrawal + C2 New +C1 | V3 | Y | Y |
| Trade | Expiry | T1 + V1 | New +C1 | V1 | NA | 1. Cashflow would be filtered out from trade expiry |

The matrix is explicitly limited to common cases. `Fixing` and `PortfolioReassignment` are incomplete, and the `Trade | Revive` row warrants validation because it pairs trade version `V3` with `Withdrawal + C2 New +C1`.

## Cancellation and Withdrawal Handling

Cashflow withdrawal events caused by Stella trade cancellation are described as “special STP” cases. They bypass SSI checking, NSTP checking, suppression checking, and other settlement exception processing.

The source does not define “special STP” or reconcile this bypass with the matrix's `NA` CDU confirmation status.

## Murex 2.11 Solace Topics

The source specifies product-specific `pub` and `pub/replay` topic strings for Ratan's consumption of Murex 2.11 trade SCBML from TDS3.

| Product | Publication topic | Replay topic |
|---|---|---|
| Commodity | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/com/pub` | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/com/pub/replay` |
| Credit | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/cre/pub` | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/cre/pub/replay` |
| ForeignExchange | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/fx-oth/pub`<br>`v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/fx-spot/pub` | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/fx-oth/pub/replay`<br>`v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/fx-spot/pub/replay` |
| InterestRate | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/irs/pub` | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/irs/pub/replay` |
| Cash | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/cash/pub` | `v1/post-trade/42970-fmedmi/tradelake/murex/scbml-4.0/-/cash/pub/replay` |

The original table has inconsistent header and row cardinalities. This presentation retains every supplied topic string but is not a production-ready subscription specification.

## Murex 2.11 Trade-SCBML Field Mappings

| Field Name | Logical Model Name | SCBML Path |
|---|---|---|
| Trade ID | `Source_System_Trade_Internal_Id` | `(/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade\|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade\|*:trade))\|((*:novation\|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:tradeId[@tradeIdScheme=http://www.sc.com/coding-scheme/tradeId/Murex/tradeInternalId]` |
| Trade Status | `Source_System_Validation_Status` | `/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:subState[@stateScheme=http://www.sc.com/coding-scheme/state/Murex]` |

## Murex `COMP` Exception Resolution

For a Murex trade:

1. Extract `Source_System_Trade_Internal_Id` from trade SCBML, for example `T1`.
2. Find cashflows where `Trade_Id` equals that value.
3. When `Source_System_Validation_Status` equals `COMP`, identify matching cashflows carrying `Pending Confirmation/Affirmation`.
4. Close that exception.
5. Move a cashflow to STP only if the closed exception was its only exception.

The requirement does not define the meaning of `COMP`, idempotency for replay messages, handling of duplicate or out-of-order statuses, version regressions, missing cashflows, or multiple matching cashflows.

## Related Pages

- [[trade-confirmation-driven-cashflow-stp]]
- [[trade-cashflow-correlation-by-trade-version]]
- [[murex-comp-confirmation-exception-resolution]]
- [[what-is-the-authoritative-cdu-confirmation-status-contract]]
- [[what-does-nonconfirmed-mean-for-cashflow-stp]]
- [[what-is-the-authoritative-tds3-to-ratan-solace-topic-contract]]