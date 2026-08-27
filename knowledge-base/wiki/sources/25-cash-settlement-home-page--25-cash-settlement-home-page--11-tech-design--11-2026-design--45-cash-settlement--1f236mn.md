---
type: source
title: Cash Settlement Platform Architecture - Korea
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/FMRP/KR%3A+Trade+Settlement"
venue: Confluence
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, korea, ratan, architecture, payments, accounting]
related: [cash-settlement-platform, murex-korea, oltp, enisis, fmsgw, saa, korea-cash-settlement-payment-routing-and-accounting, korea-trade-confirmation-stp-control, real-time-ratan-oltp-accounting-integration, korea-swift-fmsgw-saa-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Cash Settlement Platform Architecture - Korea

## Scope and status

This design source outlines a proposed 2026 Korea cash-settlement architecture spanning RATAN, Murex Korea, OLTP, Solace/EDMI, FMSGW, SAA, Enisis, and TLM. It documents intended flows and open design points rather than an approved target architecture.

The material does not provide finalized interface contracts, selected transport protocols, delivery dates, acceptance criteria, or formal approvals. Korea-specific claims in this source must not be generalized to Indonesia or other RATAN deployments.

## Data flow allocation

| | Sett Means | Sett Account | Cashflow Status Post Cutoff | Payment Type | Currency | Payment Process | Accounting | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NOS | CCY MAIN | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP | |
| 2 | NOS | CCY KEBSEO | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP | |
| 3 | NOS | CCY WRBSEO | Released/Settled | External Client | FCY | SWIFT into ENISIS | Accounting entry into OLTP | |
| 4 | NOX | CCY UISUS | Released | Internal Movement, 1. credit funds to another branch account hold in SCBK 2. credit funds to client account hold in SCBK 3. Interbank Remittance Network | KRW & FCY | Ratan->TIS->UI(OLTP) | Accounting entry will not flow into OLTP | |
| 5 | NOX | CCY UIBOK | Released | BOK-Wire | KRW | Ratan->TIS->UI(OLTP) | Accounting entry into OLTP | BOK related payment can't directly debit on suspend account. It will directly debit on nostro account, so accounting entry will be required. |
| 6 | NOX | CCY UIDD | Released | Internal Movement, 1. debit funds to another branch account hold in SCBK 2. debit funds to client account hold in SCBK | KRW & FCY | Ratan->TIS->UI(OLTP) | Accounting entry will not flow into OLTP | |
| 7 | NOX | KRO BOKSEO | Released | Client is Bank, through BOK wire | KRW | User will manually query in SSDR, then manually upload into OLTP | Accounting entry into OLTP | Daily volume around 20-30, so user prefer bulk upload directly into OLTP. Accounting behavior same with UIBOK |

The allocation establishes distinct accounting outcomes: NOS external-client FCY flows post accounting to OLTP through Enisis; UISUS and UIDD do not; and UIBOK plus KRO BOKSEO require OLTP accounting because of BOK-related nostro debit treatment. See [[korea-cash-settlement-payment-routing-and-accounting]].

## Architecture open points

|  | Current State | Expectation |
| --- | --- | --- |
| Trade Confirmation Flow | 1. MXG KR will only sync trade VALD to MXG GDC 2. UDF field update for Affirmation: MO manual upload to MXG KR via a spreadsheet 3. COMP status: MO manually change one by one 4. Payments in MXG KR post the upload would be STP, ~ 70% | 1. Trade confirmation need to be synced from MXG KR to MXG GDC/TDS3, otherwise no payment will be STP, they will be pending affirmation 2. Current situation: 1. 90% are internal, which can bypass the trade confirmation check 2. 5% are MW 2 sided trade, which confirmed already by broker, can also bypass the confirmation check. However Murex should provide the flag 3. 5% are CORP and FI, which should be NSTP based on the existing rule 3. Potential solution: 1. CDUPS integration might be required for auto confirmation & MXG KR sync the confirmation status to TDS, although now it is manual 2. Give up the confirmation control, perhaps only CORP and FI clients to be NSTP, as Ji Hoon mentioned as the above current situation |
| OLTP integration | 1. MXG -> IFOS -> OLTP via batch 2. Manually key in | Ratan <-> KR Solace <-> KR EDMI <-> OLTP Risk: 1. Eventually Yeon Su found that Vendor process to cover the development. Expectation would be below for OLTP: 1. Ratan publish accounting in real time 2. OLTP process accounting and process to FX DB 3. OLTP respond ACK/NACK in real time 4. OLTP follow existing processes for downstream, including PSGL/IFOS 5. OLTP to handle the KRW payments: 1. Build the STP process 2. Or suppress in Ratan, and manually key in OLTP |
| Murex KR Integration | NA | Assume Murex KR will replicate the global model, Ratan to process 2 Murex stream Trade id & cashflow id overlap? |
| SWIFT integration/customization | MXG -> RATAN -> Enisis -> SAA(SOAP) -> Swift network | MXG -> RATAN -> FMSGW -> SAA, If any customization required: 1. MT210 2. Portfolio level nostro stamping |
| Tech Integration | NA | 1. New Korea MQ pair: RATAN ↔ Murex KR 2. New Korea Solace Topic/queue pair 1. RATAN ↔ OLTP 2. RATAN ↔ FMSGW 3. FMSGW ↔ SAA, Expected protocol is SOAP, which may will be a potential risk, IBMMQ might be an alternative solution. |
| Tactical API for TLM | NA | Propose an API for tactical solution |

## Key findings

- Trade-confirmation synchronization from MXG KR to MXG GDC/TDS3 is presented as the principal dependency for broad payment STP. The proposed bypass population and CDUPS option are not approved decisions.
- The desired accounting path is `Ratan <-> KR Solace <-> KR EDMI <-> OLTP`, with real-time accounting publication and OLTP ACK/NACK responses. Event, idempotency, retry, timeout, and reconciliation contracts are absent.
- The proposed SWIFT route replaces Enisis with FMSGW, but SOAP versus IBM MQ remains unresolved. MT210 and portfolio-level nostro stamping may require customization.
- KRO BOKSEO remains a manual SSDR-query and OLTP bulk-upload process at approximately 20–30 daily items.
- The delivery timeline is unpopulated despite material architecture dependencies and unresolved choices.

## Timeline

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Analysis | | | | | | | | | | | | |
| Development | | | | | | | | | | | | |
| SIT | | | | | | | | | | | | |
| UAT | | | | | | | | | | | | |
| CPT | | | | | | | | | | | | |
| Go Live | | | | | | | | | | | | |
| Post Care & BAU | | | | | | | | | | | | |

## Related pages

- [[korea-trade-confirmation-stp-control]]
- [[real-time-ratan-oltp-accounting-integration]]
- [[korea-swift-fmsgw-saa-integration]]
- [[what-is-the-approved-korea-trade-confirmation-control-model]]
- [[what-is-the-approved-korea-oltp-accounting-ack-nack-contract]]
- [[which-korea-krw-payment-handling-model-is-approved]]
---

---FILE: wiki/entities/murex-korea.md---
type: entity
title: Murex Korea
created: 2026-08-24
updated: 2026-08-24
tags: [murex, korea, trade-processing, cash-settlement]
related: [cash-settlement-platform, korea-trade-confirmation-stp-control, how-will-murex-korea-prevent-trade-and-cashflow-id-collisions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Murex Korea

Murex Korea, also referenced as MXG KR, is the Korea trade-processing deployment in the proposed RATAN cash-settlement design.

## Documented role

MXG KR currently synchronizes only trade `VALD` to MXG GDC. Affirmation UDF updates are manually uploaded by spreadsheet, and `COMP` status changes are performed manually.

The source expects trade-confirmation state to be synchronized from MXG KR to MXG GDC/TDS3 to support payment STP. A new Korea MQ pair between RATAN and Murex Korea is proposed.

## Unresolved integration risks

The design assumes Murex Korea will replicate the global model while RATAN processes two Murex streams. It explicitly leaves open whether trade IDs and cashflow IDs can overlap. See [[how-will-murex-korea-prevent-trade-and-cashflow-id-collisions]].

The source does not establish an approved integration contract, source-of-truth model for confirmation state, or identifier namespace.
---

---FILE: wiki/entities/oltp.md---
type: entity
title: OLTP
created: 2026-08-24
updated: 2026-08-24
tags: [accounting, korea, payment-processing, integration]
related: [real-time-ratan-oltp-accounting-integration, korea-cash-settlement-payment-routing-and-accounting, what-is-the-approved-korea-oltp-accounting-ack-nack-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# OLTP

OLTP is the Korea accounting and downstream processing system named in the proposed RATAN cash-settlement architecture.

## Current and proposed paths

The documented current path is `MXG -> IFOS -> OLTP via batch`, supplemented by manual keying.

The proposed target path is `Ratan <-> KR Solace <-> KR EDMI <-> OLTP`. In that model, OLTP is expected to process RATAN accounting events, pass processing to FX DB, return real-time ACK/NACK responses, and retain downstream PSGL/IFOS processes.

## KRW handling

The source leaves two alternatives unresolved:

1. Build an OLTP STP process for KRW payments.
2. Suppress corresponding postings in RATAN and manually key them into OLTP.

Neither alternative is identified as approved. See [[which-korea-krw-payment-handling-model-is-approved]].
---

---FILE: wiki/entities/enisis.md---
type: entity
title: Enisis
created: 2026-08-24
updated: 2026-08-24
tags: [swift, payments, korea, legacy-integration]
related: [korea-swift-fmsgw-saa-integration, saa, fmsgw]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Enisis

Enisis is the existing Korea payment/SWIFT integration component in the documented route:

```text
MXG -> RATAN -> Enisis -> SAA(SOAP) -> Swift network
```

NOS external-client FCY settlement flows for CCY MAIN, CCY KEBSEO, and CCY WRBSEO are documented as using “SWIFT into ENISIS” and generating accounting entries in OLTP.

The source proposes FMSGW as a successor route component but does not establish that Enisis is retired or that a migration has been approved.
---

---FILE: wiki/entities/saa.md---
type: entity
title: SAA
created: 2026-08-24
updated: 2026-08-24
tags: [swift, payment-messaging, korea, integration]
related: [enisis, fmsgw, korea-swift-fmsgw-saa-integration, is-soap-or-ibm-mq-approved-for-korea-fmsgw-to-saa-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# SAA

SAA is the SWIFT connectivity component in the Korea cash-settlement design.

The current documented route sends messages from Enisis to `SAA(SOAP)` and then to the SWIFT network. The proposed route is `MXG -> RATAN -> FMSGW -> SAA`.

New Korea messaging integration between FMSGW and SAA is proposed. SOAP is the expected protocol, but the source identifies it as a risk and records IBM MQ as an alternative. No selected transport, interface contract, or rollback plan is provided.
---

---FILE: wiki/entities/fmsgw.md---
type: entity
title: FMSGW
created: 2026-08-24
updated: 2026-08-24
tags: [gateway, swift, korea, payments]
related: [saa, enisis, korea-swift-fmsgw-saa-integration, is-soap-or-ibm-mq-approved-for-korea-fmsgw-to-saa-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# FMSGW

FMSGW is the proposed financial-markets gateway component for the Korea SWIFT route.

## Proposed role

The source proposes changing the existing route:

```text
MXG -> RATAN -> Enisis -> SAA(SOAP) -> Swift network
```

to:

```text
MXG -> RATAN -> FMSGW -> SAA
```

The proposed design requires Korea topic/queue pairs for RATAN ↔ FMSGW and FMSGW ↔ SAA.

## Open design matters

Potential FMSGW/SAA customization includes `MT210` and portfolio-level nostro stamping. SOAP is expected but explicitly identified as risky; IBM MQ is recorded only as an alternative. The source does not evidence an approved migration, transport selection, or replacement of Enisis.
---

---FILE: wiki/concepts/korea-cash-settlement-payment-routing-and-accounting.md---
type: concept
title: Korea Cash-Settlement Payment Routing and Accounting
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, korea, payment-routing, accounting, bok-wire]
related: [cash-settlement-platform, oltp, enisis, ssdr, which-korea-krw-payment-handling-model-is-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Korea Cash-Settlement Payment Routing and Accounting

Korea cash-settlement routing is differentiated by settlement means, settlement account, payment type, currency, and accounting treatment.

## Routing model

- NOS external-client FCY flows for CCY MAIN, CCY KEBSEO, and CCY WRBSEO route through SWIFT into [[enisis]] and post accounting entries to [[oltp]].
- NOX UISUS and UIDD internal-movement flows route `Ratan->TIS->UI(OLTP)` but do not send accounting entries to OLTP.
- NOX UIBOK BOK-Wire payments route through `Ratan->TIS->UI(OLTP)` and require OLTP accounting because BOK-related payments debit a nostro account rather than a suspend account.
- NOX KRO BOKSEO payments have equivalent accounting behavior to UIBOK but remain manual: users query [[ssdr]] and bulk-upload into OLTP. The stated volume is approximately 20–30 items daily.

## Boundary

This is a Korea-specific model documented as a design allocation. It does not establish identical routing or accounting behavior for other RATAN regions.

## Unresolved treatment

The wider design leaves KRW handling unresolved between an OLTP STP implementation and RATAN suppression followed by manual OLTP keying. See [[which-korea-krw-payment-handling-model-is-approved]].
---

---FILE: wiki/concepts/korea-trade-confirmation-stp-control.md---
type: concept
title: Korea Trade-Confirmation STP Control
created: 2026-08-24
updated: 2026-08-24
tags: [korea, trade-confirmation, stp, nstp, murex]
related: [murex-korea, what-is-the-approved-korea-trade-confirmation-control-model, how-will-murex-korea-prevent-trade-and-cashflow-id-collisions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Korea Trade-Confirmation STP Control

The Korea design treats synchronization of trade-confirmation state from [[murex-korea]] to MXG GDC/TDS3 as a prerequisite for broad payment straight-through processing.

## Current state

MXG KR synchronizes trade `VALD` only. Affirmation UDF updates are manually uploaded through spreadsheets, and `COMP` status changes are manually performed one by one. The source estimates that approximately 70% of payments are STP after the upload process.

## Proposed control directions

The source records, but does not select, these approaches:

1. Use CDUPS for auto-confirmation and synchronize confirmation status from MXG KR to TDS.
2. Relax broad confirmation control, potentially retaining NSTP only for CORP and FI.

It estimates that internal trades constitute approximately 90% and may bypass confirmation checks, MW two-sided trades constitute approximately 5% and may bypass if Murex provides a flag, and CORP/FI trades constitute approximately 5% and remain NSTP.

These proportions, bypass controls, flag semantics, and governance approval are not validated in the source.
---

---FILE: wiki/concepts/real-time-ratan-oltp-accounting-integration.md---
type: concept
title: Real-Time RATAN-OLTP Accounting Integration
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, oltp, accounting, solace, ack-nack, korea]
related: [oltp, fm-solace, conditional-integration-only-accounting-testing, what-is-the-approved-korea-oltp-accounting-ack-nack-contract, which-korea-krw-payment-handling-model-is-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Real-Time RATAN-OLTP Accounting Integration

The proposed Korea target topology is:

```text
Ratan <-> KR Solace <-> KR EDMI <-> OLTP
```

It is intended to replace the current `MXG -> IFOS -> OLTP via batch` path and manual accounting keying.

## Expected responsibilities

- RATAN publishes accounting events in real time.
- [[oltp]] processes accounting and passes processing to FX DB.
- OLTP returns ACK/NACK in real time.
- OLTP continues existing downstream processing, including PSGL/IFOS.
- KRW payments are either handled by a new STP process or suppressed in RATAN and keyed manually in OLTP.

## Contract gap

The source does not define event schemas, correlation identifiers, ordering, idempotency, retry handling, timeout behavior, error taxonomy, replay, reconciliation, or audit requirements. Real-time ACK/NACK is an expectation, not evidence of an implemented contract.
---

---FILE: wiki/concepts/korea-swift-fmsgw-saa-integration.md---
type: concept
title: Korea SWIFT FMSGW-SAA Integration
created: 2026-08-24
updated: 2026-08-24
tags: [swift, fmsgw, saa, soap, ibm-mq, korea]
related: [fmsgw, saa, enisis, is-soap-or-ibm-mq-approved-for-korea-fmsgw-to-saa-integration, what-are-the-mt210-and-portfolio-nostro-stamping-requirements-for-korea]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Korea SWIFT FMSGW-SAA Integration

The Korea design proposes moving the SWIFT route from Enisis to [[fmsgw]].

## Documented routes

Current:

```text
MXG -> RATAN -> Enisis -> SAA(SOAP) -> Swift network
```

Proposed:

```text
MXG -> RATAN -> FMSGW -> SAA
```

The proposal includes Korea topic/queue pairs for RATAN ↔ FMSGW and FMSGW ↔ [[saa]].

## Open matters

The source identifies potential requirements for `MT210` and portfolio-level nostro stamping. SOAP is the expected FMSGW-to-SAA protocol but is identified as a risk; IBM MQ is an alternative rather than a selected decision.

The document provides no interface mapping, security model, throughput target, resiliency design, test strategy, migration plan, or rollback plan.
---

---FILE: wiki/queries/what-is-the-approved-korea-trade-confirmation-control-model.md---
type: query
title: What Is the Approved Korea Trade-Confirmation Control Model?
created: 2026-08-24
updated: 2026-08-24
tags: [korea, trade-confirmation, stp, controls]
related: [korea-trade-confirmation-stp-control, murex-korea]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# What Is the Approved Korea Trade-Confirmation Control Model?

The design records competing directions: CDUPS-based auto-confirmation plus synchronization to TDS, or broad relaxation of confirmation control with CORP and FI retained as NSTP.

## Information needed

- The authoritative confirmation-state system among MXG KR, MXG GDC, TDS3, and CDUPS.
- Approval for bypassing controls on internal and MW two-sided trades.
- The Murex flag definition, source, reliability, and exception handling for broker-confirmed MW trades.
- Compliance, operational-risk, audit, and exception-management requirements.
- Evidence that the estimated 90% / 5% / 5% trade distribution is current and representative.

Until resolved, the claimed STP outcome remains a design assumption.
---

---FILE: wiki/queries/how-will-murex-korea-prevent-trade-and-cashflow-id-collisions.md---
type: query
title: How Will Murex Korea Prevent Trade and Cashflow ID Collisions?
created: 2026-08-24
updated: 2026-08-24
tags: [murex, korea, identifiers, data-integrity, reconciliation]
related: [murex-korea, korea-trade-confirmation-stp-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# How Will Murex Korea Prevent Trade and Cashflow ID Collisions?

The design assumes that RATAN will process two Murex streams while leaving open whether trade IDs and cashflow IDs overlap.

## Information needed

- Identifier uniqueness scope and canonical namespace.
- Source-system or region discriminator requirements.
- Effects on message correlation, accounting, confirmation synchronization, and reconciliation.
- Collision detection and remediation procedures.
- Migration and historical-data compatibility implications.

A direct replication of the global model cannot be treated as validated until this risk is resolved.
---

---FILE: wiki/queries/what-is-the-approved-korea-oltp-accounting-ack-nack-contract.md---
type: query
title: What Is the Approved Korea OLTP Accounting ACK/NACK Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [oltp, accounting, ack-nack, integration, korea]
related: [real-time-ratan-oltp-accounting-integration, oltp, conditional-integration-only-accounting-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# What Is the Approved Korea OLTP Accounting ACK/NACK Contract?

The proposed RATAN-to-OLTP topology expects real-time accounting publication and ACK/NACK responses, but no contract is defined.

## Information needed

- Accounting event and ACK/NACK payload schemas.
- Correlation ID, event ID, and idempotency requirements.
- Ordering, duplicate, late-response, retry, timeout, and replay behavior.
- NACK error taxonomy and ownership of remediation.
- Reconciliation, audit retention, observability, and operational support requirements.
- Test acceptance criteria for positive, negative, and manual-fallback scenarios.

The stated ACK/NACK requirement is not sufficient to establish reliable end-to-end processing.
---

---FILE: wiki/queries/which-korea-krw-payment-handling-model-is-approved.md---
type: query
title: Which Korea KRW Payment Handling Model Is Approved?
created: 2026-08-24
updated: 2026-08-24
tags: [korea, krw, oltp, stp, accounting, bok-wire]
related: [korea-cash-settlement-payment-routing-and-accounting, real-time-ratan-oltp-accounting-integration, oltp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Which Korea KRW Payment Handling Model Is Approved?

The source leaves KRW payment treatment open between building OLTP STP and suppressing RATAN postings for manual OLTP keying.

## Information needed

- The approved processing model by KRW payment type and settlement account.
- Whether UIBOK and KRO BOKSEO require different control or accounting treatment.
- Ownership, maker-checker controls, reconciliation, and audit evidence for any manual process.
- Operational volume thresholds and service targets that would trigger automation.
- Acceptance criteria for accounting completeness and error remediation.

KRO BOKSEO is documented as manual at approximately 20–30 daily items; this does not itself approve manual processing as the target model.
---

---FILE: wiki/queries/is-soap-or-ibm-mq-approved-for-korea-fmsgw-to-saa-integration.md---
type: query
title: Is SOAP or IBM MQ Approved for Korea FMSGW-to-SAA Integration?
created: 2026-08-24
updated: 2026-08-24
tags: [soap, ibm-mq, fmsgw, saa, swift, korea]
related: [korea-swift-fmsgw-saa-integration, fmsgw, saa]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# Is SOAP or IBM MQ Approved for Korea FMSGW-to-SAA Integration?

The source expects SOAP for FMSGW-to-SAA communication, identifies it as a potential risk, and records IBM MQ as an alternative. It does not identify a selected transport.

## Information needed

- SAA capabilities and constraints for SOAP and IBM MQ.
- Security, authentication, certificate, and network requirements.
- Delivery guarantees, ordering, retry, duplicate handling, and recovery behavior.
- Throughput, latency, availability, and support ownership targets.
- Test strategy, migration sequencing, fallback, and rollback plan.

No transport decision should be inferred from the expected SOAP wording.
---

---FILE: wiki/queries/what-are-the-mt210-and-portfolio-nostro-stamping-requirements-for-korea.md---
type: query
title: What Are the MT210 and Portfolio Nostro Stamping Requirements for Korea?
created: 2026-08-24
updated: 2026-08-24
tags: [mt210, nostro, swift, fmsgw, saa, korea]
related: [korea-swift-fmsgw-saa-integration, fmsgw, saa]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# What Are the MT210 and Portfolio Nostro Stamping Requirements for Korea?

The proposed FMSGW-to-SAA route identifies `MT210` and portfolio-level nostro stamping as possible customization requirements, without defining their scope.

## Information needed

- Payment scenarios that require MT210 generation or transformation.
- SWIFT field mappings, validation rules, and triggering conditions.
- Definition and source of the portfolio-level nostro value.
- Ownership across RATAN, FMSGW, SAA, and operations.
- Required test cases, exception handling, and production reconciliation controls.

The source does not confirm whether either customization is required.
---

---FILE: wiki/queries/what-is-the-scope-and-retirement-plan-for-the-tactical-tlm-api.md---
type: query
title: What Is the Scope and Retirement Plan for the Tactical TLM API?
created: 2026-08-24
updated: 2026-08-24
tags: [tlm, api, tactical-integration, korea]
related: [cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Korea.md"]
---
# What Is the Scope and Retirement Plan for the Tactical TLM API?

The source proposes an API as a tactical solution for TLM but provides no further design information.

## Information needed

- Consumer, business purpose, and functional scope.
- API owner, data ownership, and authoritative source systems.
- Interface contract, authentication, authorization, and audit requirements.
- Availability, support model, monitoring, and error handling.
- End-state replacement and decommissioning criteria.

Without these details, the tactical API cannot be assessed for operational or architecture risk.
---

---FILE: wiki/log.md---
## 2026-08-24 ingest | Cash Settlement Platform Architecture - Korea

- Ingested Korea cash-settlement architecture design, including payment-routing allocation, confirmation-STP dependencies, proposed OLTP accounting integration, and proposed FMSGW/SAA SWIFT route.