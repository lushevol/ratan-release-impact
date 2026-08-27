---
type: source
title: Murex 2.11 CN Payment Events Affecting RATAN
authors: []
year: 2023
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cn-settlement, payment-lifecycle, market-operations, mxpayml]
related: [murex, ratan, mxpayml, murex-ratan-reversal-and-replacement-lifecycle, murex-payment-trade-lineage-identifiers, murex-payment-nstp-reason-codes, scan-and-modify-payment-impact]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Analyse murex event impacting payment to Ratan.md"]
---
# Murex 2.11 CN Payment Events Affecting RATAN

This internal functional-requirement analysis examines how Murex 2.11 market operations and cashflow events affect CN Day 1 payments sent to [[ratan]]. It uses operational evidence from 12-JUL-2022 to 11-JUL-2023 and describes expected payment behaviour after RATAN migration.

The document is design input, not evidence of approved production implementation, target-state configuration, or downstream acceptance.

## Key findings

- Payments within the seven-business-day migration horizon are expected to be represented in Murex as `SNTR`; payment-affecting amendments commonly produce a reversal and a new payment for these flows.
- Payments beyond the horizon remain `INIT`, for which Murex generally cancels the original and creates a replacement without a reversal.
- Reversal and replacement events are not reliably one-to-one or simultaneous. Re-fixing may create a new payment hours or days after the reversal.
- [[ratan]] must not correlate flows solely by amount, value date, delivery batch, timing, or `TrnRef`. The source describes `TrnRef` as mutable.
- Historical global reversal STP was 2.26%; 97.74% of reversal payments were NSTP. This is historical global evidence, not a CN target-state forecast.
- `MOD` is operationally analysed as a market-operation scenario, but the `tradeLastMKT` XML field does not treat Modify as a Murex market operation. Implementations must preserve this distinction.

## Market-operation population

The analysis covers 53,875 CN Day 1 RATAN-eligible trades with value date on or after 12-JUL-2022. Of these, 17,693 trades (33%) underwent a market operation. Operation categories overlap and must not be summed.

| Market operation | Count | Percentage of market-operation trades |
|---|---:|---:|
| `MOD` | 12,328 | 69% |
| `RPL_M` | 8,701 | 49% |
| `XIT` | 4,800 | 27% |
| `CNCL` | 1,812 | 10% |
| `RPL` | 923 | 5% |
| `EXR` | 674 | 4% |
| `RPL_DEL` | 608 | 3% |

## Lifecycle implications

`RPL_M`, `RPL`, and payment-affecting `MOD` can operate at trade or cashflow level. Trade-level changes can affect all associated payments; a cashflow customisation can affect only one payment.

For an `SNTR` payment, an amendment is expected to create a reverse/new pattern sent to [[ratan]]. For an `INIT` payment, the original may instead be cancelled (`CNCL`) and replaced. `RPL_DEL` creates a reversal for `SNTR` or `SENT` flows but cancels an `INIT` flow without a reversal.

An IRS fixed-leg replacement can be emitted before the floating leg is fixed, then later be re-netted. A documented cashflow-customisation example has two originals, two reversals, and four new payments. These behaviours are captured in [[murex-ratan-reversal-and-replacement-lifecycle]].

## Payment STP/NSTP ratios

| Population, 12-JUL-2022 to 11-JUL-2023 | Global count | Global percentage | CN count | CN percentage |
|---|---:|---:|---:|---:|
| STP | 317,188 | 11.16% | 3,183 | 7.11% |
| SUPP | 12,129 | 0.43% | 118 | 0.26% |
| SENT | 305,059 | 10.73% | 3,065 | 6.84% |
| NSTP | 2,526,235 | 88.84% | 41,611 | 92.89% |
| Total payments | 2,843,423 | 100% | 44,794 | 100% |

Excluding `SHACLHO/SHA`, CN STP was reported as 1,147 of 12,872 payments (9%), with 11,725 payments (91%) NSTP. The document identifies `SHACLHO/SHA` as the only CN counterparty blocked by the `NET` rule; this is a historical, source-specific claim.

## CN NSTP reason-code occurrences

A payment can receive multiple reason codes. Counts and percentages below are reason-tag occurrences, not distinct-payment measures.

| Reason code | CN occurrences | CN percentage | Source interpretation |
|---|---:|---:|---|
| `CORP` | 26,448 | 28.97% | Counterparty is non-bank and non-internal. |
| `NET` | 21,377 | 23.41% | Counterparty-netting exclusion. |
| `FIXING` | 13,808 | 15.12% | Fixed leg waits for estimated floating leg before netting. |
| `SI(MUL)` | 10,542 | 11.55% | Multiple SSI records meet selection criteria. |
| `STRAT` | 7,002 | 7.67% | STP strategy static eligibility. |
| `SI` | 3,631 | 3.98% | Missing nostro or vostro settlement instruction. |
| `MOP` | 2,442 | 2.67% | Recent or unvalidated market operation. |
| `ENTITY` | 1,858 | 2.03% | Internal-entity payment-module eligibility. |
| `CP_EXCL` | 1,660 | 1.82% | Precious-metal counterparty exclusion. |
| `PROD` | 1,173 | 1.28% | Product or typology static exclusion. |

## Global reversal-payment STP ratio

| Measure | Count | Percentage |
|---|---:|---:|
| STP reversal payments | 343 | 2.26% |
| NSTP reversal payments | 14,827 | 97.74% |
| Total reversal payments | 15,170 | 100% |

| NSTP reversal reason | Count | Percentage of NSTP reversals |
|---|---:|---:|
| `REV` | 13,386 | 90.28% |
| `REV;FIXING;` | 1,154 | 7.78% |
| `NO ERROR` | 232 | 1.56% |
| `FIXING` | 55 | 0.37% |
| Total | 14,827 | 100% |

The source states that `REV` applies when the original payment is not `SENT` or the market operation has not been validated.

## MxPayML integration attributes

The following table preserves the source's integration fields and XPaths verbatim, including apparent XPath and spelling inconsistencies that require payload validation.

| Label | Description | XPath |
|---|---|---|
| Flow id | murex flow id | `/MxPayML/flowID` |
| Action | `FIX_DEF` means payment is fixing related. Fixing related payment may also have this field as `INS`. `Action` value on reverse should be same as original payment, but new might differ from original. A new payment generated from Modify has `Action=MOD`. | `/MxPayML/scbExtraInfoBlock/action` |
| Trade Last Operation | Belonging trade comes from which market operation. Modify (`MOD`) is not defined as market operation in Murex, so this field does not change for `MOD`. Removal of Mktops (`CNCL`) is not defined as market operation, so this field does not change for `RPL_DEL`. | `k/MxPayML/scbExtraInfoBlock/tradeLastMKT` |
| TrnRef | Most recent trade number associated with the payment; it can change following the latest trade number. | `/MxPayML/transactionID` |
| TrnID | Trade number from which the payment was originally created. | `/MxPayML/transactionOriginID` |
| TrnParentID | Creator trade number of current trade. If no creator exists, value is `0`. | `/MxPayML/scbExtraInfoBlock/TrnParentID` |
| TrnOriginalID | RPL original trade number of current trade. If no RPL occurred, value is `0`. | `/MxPayML/scbExtraInfoBlock/TrnOrginalID` |
| Comment | `Reverse of flow` for a reverse flow; blank for a new flow. | `/MxPayML/comment` |
| CpuDate | System date when the cashflow persisted to the Murex database. | `/MxPayML/computerDate` |
| CpuTime | System time when the cashflow persisted to the Murex database. | `/MxPayML/computerTime` |
| Mx payment snapshot | Payment snapshot under the belonging trade when enriched into Murex XML. Array includes `Flowid`, `status`, and `value_date`; `SNTR` and `RLSR` indicate cashflow expected to be sent to RATAN. | `/MxPayML/scbExtraInfoBlock/Flows/flow` |

## Caveats and unresolved matters

- The `tradeLastMKT` XPath begins with `k/`, and `TrnOrginalID` differs from the label spelling. Both require validation against actual MxPayML messages.
- `CNCL` is used both in discussion of removing market operations and in payment-cancellation descriptions; `RPL_DEL` is separately called Cancellation. Canonical terminology is needed.
- The source names “Messge lost” as an exception scenario but does not provide detection, recovery, ownership, or reconciliation behaviour.
- Readiness markings and percentage totals in the source are assessments with undefined blanks and `TBC` entries; they are not confirmed implementation evidence.

See [[murex-payment-trade-lineage-identifiers]], [[murex-payment-nstp-reason-codes]], and [[scan-and-modify-payment-impact]] for derived operational concepts.