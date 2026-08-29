---
type: entity
title: TLM
created: 2026-08-22
updated: 2026-08-25
tags: ["tlm", "dependency", "cash-settlement", "korea", "settlement", "accounting", "dvp", "accounting-reconciliation", "api", "reconciliation", "integration", "ola", "fx-utilization", "downstream-system", "cashflow", "trade", "murex-211", "ratan", "consumer-system"]
related: ["korea", "ratan-settlement", "dvp-payment-control", "ebbs-settlement-accounting", "korea-cash-settlement-migration", "ratan", "operational-level-agreement-for-settlement-interfaces", "korea-ratan-settlement-migration", "fxu", "ebbs", "accounting-feed-reconciliation", "partial-and-pastdue-utilization-accounting", "aspire", "oltp", "korea-accounting-reconciliation", "ratan-accounting-reconciliation-api", "irs-cashflow-aggregation", "what-are-the-tlm-lms-and-cis-impacts-of-irs-cashflow-aggregation", "manual-cashflow-rounding", "settlement-accounting", "murex-ratan-cashflow-reconciliation", "murex-211", "query-recon-records", "fmaa", "ratanone", "korea-tlm-accounting-reconciliation", "ratan-tlm-reconciliation-query", "ratan-and-tlm-20649--1ovnb8w"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---

# TLM

TLM is a downstream settlement-related system referenced in RATAN interface, reconciliation, and OLA readiness tracking. In the FX utilization accounting context, it is described as the downstream reconciliation system. TLM is also identified as potentially affected by IRS cashflow aggregation.

For the Murex 2.11–RATAN cashflow flow, the DOI designates TLM as the end-to-end reconciliation mechanism. This DOI-specific role is distinct from the Korea accounting-reconciliation, DVP, FX utilization, manual-rounding, and IRS-aggregation references described below.

## Korea accounting reconciliation

According to **Cash Settlement - Korea Accounting Recon - RATAN- TLM**, TLM is the reconciliation platform and API consumer for the Korea accounting-reconciliation process. During the interim arrangement, TLM queries [[ratan]] for accounting records sent to oltp, including acknowledged, rejected, and unanswered postings.

The same source states that the direct RATAN-to-TLM feed exists because aspire cannot meet the Korea release timeline. Feature `11898201` describes a future route from `OLTP` through `ASPIRE` to `TLM`, with decommissioning of the direct RATAN-to-TLM integration.

That source does not establish that either the direct RATAN-to-TLM route or the future OLTP-to-ASPIRE-to-TLM route has been deployed or validated in production.

In **Cash Settlement -- Korea Migration**, TLM is separately identified as the downstream system for the RATAN accounting-reconciliation API in the Korea cash-settlement migration. That source does not provide the reconciliation contract, matching rules, exception handling, ownership, or delivery status.

### Interface 20649

According to **Ratan and TLM 20649**, TLM is the consumer of RATAN interface 20649 and queries RATAN accounting information to perform reconciliation for the Korea release scope.

The documented flow is:

```text
TLM <> RESTFUL API <> RATANONE
```

The source states that TLM needs records already sent to oltp, including records described as acknowledged, NACKed, and unanswered. It associates this requirement with aspire being unable to meet the Korea release timeline.

Interface 20649 supports only the Korea entity represented by:

```text
fmidList = 10036645
```

The interface-specific query is subject to:

- A maximum three-day time span.
- GMT conversion requirements.
- An implicit `task_status = 'SENT'` filter.

These constraints are specific to interface 20649 and should not be assumed to define all TLM or RATAN behavior.

See ratan tlm reconciliation query and ratan and tlm 20649  1ovnb8w.

### Korea accounting-record retrieval API

According to **Korea Accounting - TLM Recon**, TLM is the intended reconciliation consumer of RATAN's Korea accounting-record retrieval API, query recon records. It retrieves EBBS-format accounting records within bounded release-time windows to reconcile published Korea accounting activity.

That technical-design source specifies that TLM must:

- Use fmaa-generated credentials.
- Request gzip-compressed responses.
- Split backfills into windows no longer than 72 hours.

The source does not define TLM's internal reconciliation, persistence, exception-handling, or retry behavior.

## Korea cashflow migration dependency

In the **Korea Migration Functional Analysis** source, TLM is listed as a dependency for the Korea cashflow migration. The checklist does not specify the required interfaces, functionality, owner, delivery status, or acceptance criteria.

TLM readiness therefore remains an open migration question rather than a confirmed implementation dependency with defined scope.

## OLA readiness

In **Korea OLA and other release related DOCs**, the RATAN-to-TLM OLA is pending PSS review and sign-off. That source does not state the applicable OLA version, named reviewer, review deadline, or approval outcome.

## Murex 2.11–RATAN cashflow reconciliation

According to **Settlement - Murex 2.11 DOI Document - H2 2024**, TLM is the designated end-to-end reconciliation mechanism for the Murex 2.11–RATAN cashflow flow in the DOI.

The document distinguishes TLM reconciliation from:

- The optional Murex payment-status monitor.
- Real-time ACK processing, which the document identifies as the primary data-flow control.

## DVP workflow role

In the **MX2.11 Decomm Cash Settlement Business Workflow NSTP Workflow** source, TLM is described as a settlement or accounting system referenced as a co-source of funds-receipt confirmation for DVP cashflows.

The proposed DVP workflow uses funds-receipt confirmation from EBBS or TLM before the DVP exception can be resolved. That source does not specify precedence between EBBS and TLM or the detailed message contract.

## FX utilization accounting reconciliation

In the **FXU - RATAN analysis** source, [[ratan]] publishes utilization-related bridge accounting to ebbs in real time, while utilization-accounting reconciliation is performed in TLM.

That source also describes a pending requirement for an FXU–TLM enrichment report. It does not define the report's ownership, fields, timing, or reconciliation breaks. TLM is a consumer in the intended design, not evidence of an implemented or approved reporting interface.

## Manual rounding and trade-payment cashflow breaks

In **Manual Rounding.md**, TLM is mentioned as a possible location for checking breaks between a trade and its payment cashflow after a Manual Rounding adjustment.

The question mark in that source indicates that TLM involvement is tentative. The source does not identify the TLM product, interface, matching rules, tolerance, or ownership.

## IRS cashflow aggregation impact

In **Cashflow Aggregation.md**, TLM is identified as a downstream system potentially affected by IRS cashflow aggregation. The source records the TLM impact assessment as TBC.

That source provides no interface contract, event definition, ownership confirmation, or required change. The impact remains an open item in what are the tlm lms and cis impacts of irs cashflow aggregation.