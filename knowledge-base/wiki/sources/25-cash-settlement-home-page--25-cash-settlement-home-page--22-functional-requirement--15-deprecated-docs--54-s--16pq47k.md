---
type: source
title: "SFMRP - Cash Settlement Platform Integration (Deprecated)"
authors: []
year: 0
url: ""
venue: "Deprecated functional requirement"
tags: [deprecated, cash-settlement, payment-integration, stella, swift, netting, splitting]
related: [cash-settlement-platform, stella, fmsre, amh, murex-2-11, fmo-ops, cashflow-status-lifecycle, cashflow-materialization, payment-date-override, cashflow-withdrawal-and-new, cashflow-netting-and-un-netting-state-transitions, cashflow-split-and-unsplit]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md"]
---
# SFMRP - Cash Settlement Platform Integration (Deprecated)

> **Deprecated historical evidence.** This document describes a proposed or historical integration model. It must not be used as the current authoritative contract without corroboration from non-deprecated requirements.

## Historical integration model

The document describes [[stella]] as a producer of New, Amendment, and Withdrawal cashflow events. The [[cash-settlement-platform]] persists and enriches inbound cashflows in a “payment lake,” then owns lifecycle processing, materialization, NSTP handling, SWIFT generation, netting, and splitting. Stella and Blade are described as querying the latest status and versions from the payment lake rather than receiving synchronous lifecycle callbacks.

The source states that a status change is complete once it has been persisted to the payment lake, with no need to call the Stella API or write to TDS3. The relationship between this payment lake and [[cdu-lake]] is not established.

## Status and event matrix

| Owner | Event | Status | Comment |
| --- | --- | --- | --- |
| STELLA | New Amend Withdrawal | PROJECTED: New cashflow created by Stella out of VD-5 window; QUEUED: New cashflow created by Stella within VD-5 window; CANCELLED: Cashflow cancelled by Stella | Stella can get the latest cashflow status from payment lake when handling these business events. |
| Cash Settlement Platform | Data Persistence | PROJECTED/QUEUED | Cash Settlement Platform would store the new inbound cashflows into payment lake. |
| Materialization | PROJECTED → QUEUED | PROJECTED → QUEUED | Scheduled job to materialize the cashflow falling into the V-5 window. |
| NSTP process | QUEUED → PENDING → VALIDATED | QUEUED → PENDING → VALIDATED | Post-trade NSTP activities manually progressed by Settlement Ops: SSI Exception, NSTP review, and CPN. |
| Swift Generation | VALIDATED → RELEASED | VALIDATED → RELEASED | SWIFT message generated and sent to routing application [[fmsre]]. |
| Settle in Swift Network | RELEASED → SETTELED | RELEASED → SETTELED | SWIFT message routed to the SWIFT network for final settlement. |
| Netting | PENDING → NETTING | PENDING → NETTING | Component cashflows after netting. |

## Gross-settlement lifecycle example

| Stage | Trade ID | Cashflow ID | Source System | Cashflow Event | Cashflow Status | Business Version | Cashflow Version | Sub Status Type | Sub Status | Payment Lake Version | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | --- | ---: | --- | ---: | --- |
| New Trade | D101 | C101 | Stella | New | Projected | 0 | 0 | NA | NA | 0 | USD | 100 | 10/20/2022 |
| Materialization | D101 | C101 | Stella | New | Queued | 0 | 1 | NA | NA | 1 | USD | 100 | 10/20/2022 |
| Manual Process | D101 | C101 | Stella | New | Pending | 0 | 2 | NSTP Release | Pending Maker | 2 | USD | 100 | 10/20/2022 |
| Maker complete | D101 | C101 | Stella | New | Pending | 0 | 2 | NSTP Release | Pending Checker | 3 | USD | 100 | 10/20/2022 |
| Checker complete | D101 | C101 | Stella | New | Validated | 0 | 3 | NA | NA | 4 | USD | 100 | 10/20/2022 |
| Swift Generation | D101 | C101 | Stella | New | Released | 0 | 4 | NA | NA | 5 | USD | 100 | 10/20/2022 |
| Final Settlement | D101 | C101 | Stella | New | Settled | 0 | 5 | NA | NA | 6 | USD | 100 | 10/20/2022 |

The document associates `MT202/MT103` generation with `VALIDATED → RELEASED`, delivery to [[fmsre]], and an [[amh]] ACK after routing with `SETTLED`. It does not establish that this ACK represents irrevocable financial settlement rather than network acceptance or instruction delivery.

## Payment-date override example

The document states that FMO Settlement Ops may find the source value date invalid and manually add a distinct `Payment Date`, leaving `Value Date` unchanged. It describes `Payment Date` as transparent for Blade/Stella.

| Description | Trade ID | Cashflow ID | Cashflow Status | Business Version | Cashflow Version | Payment Lake Version | Currency | Amount | Value Date | Payment Date |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- | --- |
| Manual Process | D101 | C101 | Pending | 0 | 2 | 2 | USD | 100 | 10/20/2022 | 10/21/2022 |
| Manual Process | D101 | C101 | Pending | 0 | 2 | 2 | USD | 100 | 10/20/2022 | 10/21/2022 |

The duplicate rows are not explained.

## Amendment scenarios

### Amendment while Validated

The historical model permits a Stella amendment while cashflow `C101` is `Validated`. Stella emits an `Amendment`, retains `C101`, increments Business Version from `0` to `1`, and the platform records a new Cashflow Version and Payment Lake Version.

| Description | Trade ID | Cashflow ID | Source System | Cashflow Event | Cashflow Status | Business Version | Cashflow Version | Payment Lake Version | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| Validated | D101 | C101 | Stella | New | Validated | 0 | 3 | 3 | USD | 100 | 10/20/2022 |
| Trade Amendment | D101 | C101 | Stella | Amendment | Queued | 1 | 4 | 4 | USD | 110 | 10/20/2022 |

### Amendment while Released

For a released payment, the source specifies a combined `Withdrawal & New` message. The original cashflow is withdrawn and recalled using `MT292/MT192`; only after successful recall may the replacement be validated, released, and settled using `MT202/MT103`.

| Description | Trade ID | Cashflow ID | Source System | Cashflow Event | Cashflow Status | Business Version | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- |
| Withdrawal & New | D101 | C101 | Stella | Withdrawal | Cancelled | 1 | USD | 100 | 10/20/2022 |
| Withdrawal & New | D101 | C102 | Stella | New | Queued | 0 | USD | 110 | 10/20/2022 |

The later replacement-processing tables identify the new payment as `C101` rather than `C102`; this is an internal documentation defect and the replacement identity rule is not safe to adopt as authoritative.

## Netting and automatic un-netting

The source describes manual netting in [[cashflow-blotter]] across Stella and [[murex-2-11]] cashflows.

| Description | Trade ID | Cashflow ID | Netting ID | Source System | Cashflow Event | Cashflow Status | Business Version | Cashflow Version | Payment Lake Version | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| Netted | D101 | C101 | N001 | Stella | New | Netted | 0 | 3 | 3 | USD | 100 | 10/20/2022 |
| Netted | D101 | C102 | N001 | Stella | New | Netted | 0 | 3 | 3 | USD | 200 | 10/20/2022 |
| Netted | D103 | C103 | N001 | Murex 2.11 | New | Netted | 0 | 3 | 3 | USD | 100 | 10/20/2022 |
| Netted | D104 | C104 | N001 | Murex 2.11 | New | Netted | 0 | 3 | 3 | USD | 100 | 10/20/2022 |
| Netting Resultant | NA | C105 | N001 | Cash Settlement | New | Queued | 0 | 0 | 0 | USD | 500 | 10/20/2022 |

A Stella amendment to a netted component is stated to trigger automatic un-netting. Components return to `Queued`, and the resultant is marked `Dead`. The un-netting table identifies the resultant as `C103`, conflicting with the earlier resultant identifier `C105`; `C103` is already a Murex component. It also clears Netting ID for Stella components but retains `N001` for Murex components without explanation.

## Payment split model

The source describes FMO Ops splitting Stella parent `C101` into Cash Settlement-owned child cashflows `C102` and `C103`. It states that child payments are transparent to Stella, while the parent status is updated as children proceed.

| Description | Trade ID | Parent Cashflow Id | Cashflow ID | Source System | Cashflow Event | Cashflow Status | Business Version | Cashflow Version | Payment Lake Version | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | --- |
| Splitting | D101 | NA | C101 | Stella | New | Queued | 0 | 4 | 4 | USD | 100 | 10/20/2022 |
| Splitting | D101 | C101 | C102 | Cash Settlement | New | Queued | 0 | 0 | 0 | USD | 50 | 10/20/2022 |
| Splitting | D101 | C101 | C103 | Cash Settlement | New | Queued | 0 | 0 | 0 | USD | 50 | 10/20/2022 |

A subsequent parent `Withdrawal & New` is said to cause child payments to be marked as reversals and recalled through `MT192/MT292`. The source does not define parent-status aggregation, partial-child handling, or failure semantics. Its released-state example also shows child `C103` as `Validated` while describing both children as released.

## Open validation points

- The exact relationship between payment lake and [[cdu-lake]] is unknown.
- The meanings and ownership of Business Version, Cashflow Version, and Payment Lake Version remain undefined.
- The terms `NETTING` and `Netted` are used inconsistently.
- AMH acknowledgement must not be assumed to mean final interbank settlement.
- The document contains inconsistent identifiers and amounts in its released-amendment and un-netting examples.
---