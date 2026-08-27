---
type: source
title: Cashflow Events Control Draft2
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow-events, stella, ratan, deprecated, netting, amendment, withdrawal]
related: [stella, ratan, murex-2-11, cashflow-blotter, cashflow-status-lifecycle, cashflow-amendment-supersession, cashflow-netting-and-un-netting-state-transitions, reversal-and-correction-cashflow-processing, cashflow-expiry-event-filtering, what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule, what-is-the-authoritative-post-split-withdrawal-amendment-and-netting-model, what-is-the-authoritative-ratan-expiry-filtering-key-and-version-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft2.md"]
authors: []
year: 2022
url: ""
venue: ""
---
# Cashflow Events Control Draft2

> **Deprecated draft:** This document records historical proposed behavior. It is not an authoritative current functional specification and must be validated against later requirements, implementation evidence, and decisions.

The draft describes how [[stella]] trade-market events should affect cashflows in [[ratan]]. It distinguishes `New`, `Withdrawal`, `Amendment`, `Withdrawal & New`, and expiry events, with processing dependent on the operational state of the original cashflow.

## Historical proposed model

- A withdrawal before release or settlement closes the cashflow lifecycle.
- A withdrawal after release, settlement, or netting creates a visible reversal cashflow (`Reversal = Y`) for further operational processing.
- An amendment before `NETTED`, `RELEASED`, or `SETTLED` is represented as an updated business version.
- An amendment at or after those states is proposed to create a reversal plus a correction/new cashflow.
- For a netted component, an unsettled resultant is proposed to require manual un-netting; a settled resultant remains settled and the reversal is processed separately.
- Separate withdrawal and new messages can allow the new cashflow to proceed first, creating a duplicate-payment risk.
- Stella expiry processing on VD+1 is proposed to create a later physical version marked `Dead`, which Ratan should filter while retaining the prior operational record.

The draft leaves post-split withdrawal, amendment, and netting behavior unresolved.

## Source state transitions

| Scenario | Source transition |
| --- | --- |
| Standard processing | `PROJECTED->QUEUED->WAITING->READY->RELEASED->SETTLED` |
| Pre-settlement withdrawal | `PROJECTED → CANCELLED` |
| Released/settled withdrawal/reversal | `SETTLED → WAITING->READY->RELEASED->SETTLED` |
| Netted component withdrawal | `NETTED->WAITING` |
| Manual un-net, impacted component | `PROJECTED->NETTED->CANCELLD` / `PROJECTED->NETTED->CANCELLED` |
| Manual un-net, resultant | `QUEUED->WAITING->DEAD` |
| Manual un-net, unaffected components | `PROJECTED->NETTED->QUEUED->WAITING` |
| Netting reversals/corrections | `NETTED->WAITING->NETTED` and `PROJECTED->QUEUED->WAITING->NETTED` |
| Split original | `PROJECTED->QUEUED->WAITING->SPLIT` |
| Failed cashflow | `PROJECTED->QUEUED->WAITING->FAILED` |

Source spelling, including inconsistent status labels, is retained where it appears in the tables below.

## Pre-settlement withdrawal

| Cashflow ID | Cashflow Event | Business Version | Pay/Receive | Amount | Currency | Stella Status | Ratan Status Moving | Visible in Blotter | Reversal | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->QUEUED->WAITING | N | N | |
| C101 | Withdrawal | 1 | Pay | 100 | USD | PROJECTECD | PROJECTED → CANCELLED | N | N | Cancelled update back to Stella/TDS3 |

## Released or settled withdrawal

| Cashflow ID | Cashflow Event | Business Version | Pay/Receive | Amount | Currency | Stella Status | Ratan Status Moving | Visible in Blotter | Reversal | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->QUEUED->WAITING->READY->RELASED->SETTLED | N | N | MT103/MT202 generated |
| C101 | Withdrawal | 1 | Pay | 100 | USD | SETTLED | SETTLED → WAITING->READY->RELEASED->SETTLED | Y | Y | MT192/MT292 generated |

The SWIFT-message assertions are draft examples rather than an established message-generation contract.

## Unsettled netting resultant and withdrawal

| Cashflow Type | Cashflow ID | Cashflow Event | Business Version | Pay/Receive | Amount | Currency | Stella Status | Ratan Status Moving | Visible in Blotter | Reversal | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | C101 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->NETTED->CANCELLD | N | N | |
| Component | C102 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED→NETTED->QUEUED->WAITING | N | N | |
| Component | C103 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->NETTED->QUEUED->WAITING | N | N | |
| Resultant | N101 | New | 0 | Pay | 300 | USD | | QUEUED->WAITING->DEAD | N | N | |
| Reversal | C101 | Withdrawal | 1 | Pay | 100 | USD | NETTED | NETTED->WAITING->CANCELLED | N | Y | |

This is the draft's proposed manual un-net outcome. It does not define the operator permissions, approval controls, API, retry model, or audit contract.

## Settled netting resultant and withdrawal

| Cashflow Type | Cashflow ID | Cashflow Event | Business Version | Pay/Receive | Amount | Currency | Stella Status | Ratan Status Moving | Visible in Blotter | Reversal | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | C101 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->NETTED | N | N | |
| Component | C102 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->NETTED | N | N | |
| Component | C103 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->NETTED | N | N | |
| Resultant | N101 | New | 0 | Pay | 300 | USD | | QUEUED->WAITING->READY->RELEASED->SETTLED | Y | N | |
| Reversal | C101 | Withdrawal | 1 | Pay | 100 | USD | NETTED | NETTED->WAITING->READY->RELEASED->SETTLED | Y | Y | |

## Pre-netting amendment

| Cashflow ID | Cashflow Event | Business Version | Cashflow Version | Amount | Stella Status | Ratan Version Change | Ratan Status Moving |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | 0 | 100 | PROJECTECD | 0->1->2->3 | PROJECTED->QUEUED->WAITING->READY |
| C101 | Amendment | 1 | 1 | 150 | PROJECTECD | 0->1->2->3 | PROJECTED->QUEUED->WAITING->READY |

The draft does not establish whether the prior record is overwritten, superseded, hidden, cancelled, or retained for audit.

## Packed withdrawal and new events

| Cashflow ID | Cashflow Event | Business Version | Pay/Receive | Amount | Currency | Stella Status | Ratan Status Moving | Visible in Blotter | Reversal | Correction | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | Pay | 100 | USD | PROJECTECD | PROJECTED->QUEUED->WAITING->READY->RELASED->SETTLED | N | | | MT103/MT202 generated |
| C101 | Withdrawal | 1 | Pay | 100 | USD | SETTLED | SETTLED → WAITING | Y | Y | | |
| C102 | New | 0 | Pay | 150 | USD | PROJECTED | PROEJCTED->QUEUED->WAITING | | | Y | |

The draft proposes a “full NSTP” rule for a withdrawal-and-new pair in one Stella message, intended to prevent the correction from being sent before the withdrawal is complete. See [[what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule]].

## Separate withdrawal and new messages

| Description | Cashflow ID | Cashflow Event | Business Version | Cashflow Version | Ratan Version | Currency | Pay/Receive | Amount | Cashflow Stauts | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New trade | C101 | New | 0 | 0 | 2 | USD | Pay | 100 | PROJECTED->QUEUED->WAITING->READY->RELEAESD | |
| Trade Amendment | C101 | Withdrawal | 1 | 1 | 1 | USD | Pay | 100 | PROJECTED->QUEUED->WAITING->READY->RELEASED | Withdrawal of C101 must be proceed before new cashflow C102 |
|  | C102 | New | 0 | 0 | 0 | USD | Receive | 100 | PROJECTED->QUEUED->WAITING->READY->RELEASED | Duplicate payment risk as C102 can be STP |

The source identifies separate delivery as applicable when Stella matching fails and for Murex amendments after payment workflow status `SNTR`. It does not define a final sequencing, correlation, failure, or retry contract.

## Expiry processing

| Cashflow ID | Cashflow Event | Business Version | Cashflow Version | Stella Status | Physical Status |
| --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | 0 | PROJECTECD | Live |
| C101 | New | 0 | 1 | PROJECTECD | Dead |

| Cashflow ID | Cashflow Event | Business Version | Cashflow Version | Ratan Version Change | Ratan Status Moving |
| --- | --- | --- | --- | --- | --- |
| C101 | New | 0 | 0 | 0->1->2->3 | PROJECTED->QUEUED->WAITING->FAILED |

For this VD+1 expiry example, the draft says Ratan should filter the new expiry cashflow and continue working the previous record. It presents equivalent intended filtering for released/settled, netted, and split cashflows. The predicate and version-correlation model are unspecified; see [[cashflow-expiry-event-filtering]] and [[what-is-the-authoritative-ratan-expiry-filtering-key-and-version-model]].

## Related pages

This source is historical input for [[cashflow-status-lifecycle]], [[cashflow-amendment-supersession]], [[cashflow-netting-and-un-netting]], [[cashflow-netting-and-un-netting-state-transitions]], [[cashflow-blotter-functional-scope]], and [[cashflow-lifecycle-supersession-and-audit-history]].