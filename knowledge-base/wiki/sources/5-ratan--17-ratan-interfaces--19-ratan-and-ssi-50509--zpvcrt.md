---
type: source
title: Ratan and SSI+ 50509
authors: [Yunzhe Ta, Junying Jiang, Zhenzhen Liu, Pengpeng Li]
year: 2026
url: ""
venue: "RATAN Interfaces"
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ssi-plus, interface-50509, settlement, vostro, solace]
related: [ssi-plus, ratan-ssi-stamping, ssi-best-matching, ssi-change-notification, solace, fmrp, ratan-settlement, ratan-service-governance, what-is-the-authoritative-ratan-ssi-plus-50509-interface-contract, how-does-ratan-handle-ssi-change-notifications, what-is-the-ratan-ssi-best-matching-algorithm, what-happens-to-processed-cashflows-after-ssi-changes]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# Ratan and SSI+ 50509

This interface document describes interface **50509** between RATAN and [[ssi-plus]] for Standard Settlement Instruction (SSI) data used in Vostro processing and [[ratan-ssi-stamping]].

The source was updated and reviewed on 2026-03-12. It does not state a formal status.

## Summary

[[ssi-plus]] centrally maintains SSI information. When RATAN receives a cashflow, it uses the booking-entity FMID, counterparty FM code, currency, and CFI code to call the SSI+ ES cluster in real time and identify a matching SSI record. RATAN attaches relevant SSI-record data to the cashflow.

SSI+ also proactively publishes notifications through [[solace]] when SSI records are updated, added, or deleted. The source cautions that such changes may affect previously processed cashflows and could require re-evaluation or adjustment; it does not confirm an implemented reprocessing mechanism.

## Documented Flow

```text
SSI+ → Solace → RATAN
Real-time SSI+ publish for any update

RATAN → SSI+ ES cluster
Real-time API call
```

The document therefore identifies two distinct integration paths:

- A synchronous RATAN-to-SSI+ API lookup for cashflow matching.
- An asynchronous SSI+-to-RATAN notification flow through Solace.

## Matching Inputs

The source identifies the following cashflow attributes as inputs to SSI matching:

- Booking entity FMID
- Counterparty FM code
- Currency
- CFI code

It does not define field mandatoryness, matching precedence, tie-breaking rules, no-match handling, or the SSI fields stamped onto the cashflow. See [[ssi-best-matching]] and [[what-is-the-ratan-ssi-best-matching-algorithm]].

## Interface Contacts

| Service | Contact Name | Email Address | Phone Number |
|---|---|---|---|
| RATAN (RATAN ONE) | RATAN ONE PSS | FM_BPMS.SUPPORT@sc.com | N/A |
| SSI+ | 50509 (SSI+) | FMProdMgt - SharedServices <FMProdMgt-SharedServices@[exchange.standardchartered.com](http://exchange.standardchartered.com)> | +91 9686785999 |

## Operational Responsibilities

- SSI+ PSS monitors SSI notifications, API availability, and agreed response time.
- SSI+ PSS informs RATAN PSS of planned downtime outside the greenzone and unexpected outages.
- RATAN PSS monitors the SSI subscription through Solace and contacts SSI+ PSS when the committed API response time is breached.

The source references the RATAN FM Settlement OLA but does not provide response-time thresholds, greenzone definition, monitoring tooling, or an escalation workflow.

## Referenced Documentation

- [Vostro SSI Best Matching - UK Cashflow Migration - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Vostro+SSI+Best+Matching+-+UK+Cashflow+Migration)
- [FMRP - SSI Stamping Flow - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/FMRP+-+SSI+Stamping+Flow)
- [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

## Limitations

Connection details are empty. The source provides neither an API contract nor a Solace messaging contract, including endpoints, schemas, authentication, timeout values, topics, delivery guarantees, replay handling, or error handling.