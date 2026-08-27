---
type: source
title: RATAN - Uber Integration Technical Design
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page Tech Design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, uber, cash-settlement, scbml, tdsx, technical-design]
related: [cash-settlement-home-page-tech-design, uber, tdsx, ratanone-data-model, ratanone-anti-corruption-layer, uber-snapshot-comparison, uber-partial-success-and-completeness, bi-temporal-trade-lake-querying, proto-defined-json-data-model, scbml-decommissioning, historical-scbml-compatibility, ratan-cashflow-lifecycle-service, message-bridge, tdsx-uber-message-listener, uber-inbound-message-idempotency-and-error-state, kafka-persistent-retry-and-dlt-recovery, message-bridge-deduplication-key-lifecycle, strategic-cashflow, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---

# RATAN - Uber Integration Technical Design

## Summary

This document is a feasibility and high-level technical design proposal for integrating `UBER` messages into the RATANONE strategic cash settlement flow. Its primary objective is to reduce pervasive `SCBML` parsing and move RATANONE services toward a shared `RatanCashSettlementData` model transmitted as JSON and defined from protobuf schemas.

The proposal is not an authoritative final API or schema contract. It leaves message completeness, sequencing, duplicate detection, historical migration, field ownership, topic configuration, and downstream compatibility unresolved.

## Architectural direction

The proposed flow is:

1. TDSX publishes or exposes an aggregated UBER snapshot.
2. RATANONE receives UBER bytes through an EDMI topic.
3. A shared data-model component converts UBER into `RatanCashSettlementData`.
4. Internal RATANONE services use the common model rather than parsing SCBML independently.
5. JSON is used for inter-service transmission.
6. Protobuf remains the schema-definition and code-generation mechanism.
7. SCBML remains available for historical compatibility and any downstream conversion still required.

The central architectural pattern is an [[ratanone-anti-corruption-layer]] that isolates RATANONE domain services from external representations such as UBER and legacy SCBML.

## UBER message shape

The source describes UBER as an aggregated snapshot containing trade, cashflow, and fixing information:

```text
tradeRecord: Object
cashFlowData: Object[]
FixingNotice: Object[]
Has_Changed: {
  Cashflows: true,
  Trade: false,
  FixingNotice: true
}
```

UBER is intended to provide a complete trade-level view, but it is not necessarily an ordered event stream. The document states that there is no sequence indicator, messages may be lost or delivered out of order, and intermediate versions may not be recoverable from the consumer alone.

## TDSX query construction

The source provides this query construction:

```java
private TDSXQuery queryUberMessageData(String tradeId, Instant effective, Instant asOf) {
    return TDSXQueryBuilderWrapper.builder()
        .fields("*")
        .asOf(asOf)
        .effective(effective)
        .includeCashflowFields("*")
        .includeFixingNoticeFields("*")
        .includeDuplicateBooking()
        .includeComputedData(TDSXComputedDataTypes.FixingInformationComputed)
        .filter(f -> f.eq(TradeFields.TradeId, tradeId))
        .build();
}
```

The query uses bi-temporal parameters:

| Field name | Mandatory | Condition |
| --- | --- | --- |
| `asOf=<iso8601 date>` | No; defaults to `NOW()` | `Trade_Lake_Transaction_To_Date_Time > asOf` AND `Trade_Lake_Transaction_From_Date_Time <= asOf` |
| `effective=<iso8601 date>` | No; defaults to `NOW()` | `Trade_Lake_Valid_To_Date_Time > effective` AND `Trade_Lake_Valid_From_Date_Time <= effective` |

The source models version closure as:

```text
v1, from t1 -> to tMax

when v2 coming at t2 time

v1, from t1 -> to t2
v2, from t2 -> to tMax
```

## TDSX result versus client-generated UBER

The TDSX API result does not exactly match the UBER message schema. The client constructs a `TDSXUberMessage` and may add or derive fields:

- `TDS3Data`;
- the first trade ID from `tradeIdList`;
- the first tracking version from `trackingVersionList`;
- a `hasChanged` map converted to protobuf `BoolValue` values.

This creates three distinct representations that require explicit contract ownership:

1. TDSX query response;
2. client-generated UBER message;
3. RATANONE internal JSON representation.

## Expected benefits

The proposal identifies several potential benefits for RATANONE:

- aggregated trade, cashflow, and fixing snapshots;
- reduced reliance on cashflow grouping and blotter waits;
- centralized typed serialization and validation;
- fewer repeated upstream queries;
- trade-level enrichment and stamping;
- common data-model usage across lifecycle, orchestration, NSTP, query, netting, LMS, Swift, and accounting services;
- incremental migration from SCBML rather than a single cutover.

These are design expectations rather than measured production results.

## Migration scope

The delivery plan identifies changes in:

- `ratanone-data-model`;
- `ratanone-message-bridge`;
- `ratan-cash-settlement-standardization-service`;
- `ratan-cash-settlement-orchestration`;
- `ratan-cash-settlement-ssi-stamping-service`;
- [[ratan-cashflow-lifecycle-service]];
- NSTP and rule-engine services;
- query service;
- netting and unnetting;
- LMS;
- Swift;
- accounting;
- automation tests.

The lifecycle service is specifically described as requiring restructuring because its state machine, domain events, workflow variables, and historical data handling are tightly coupled to SCBML.

## Main risks and unresolved contracts

The source leaves these issues open:

- the authoritative completeness or exception indicator;
- whether partial-success snapshots are eligible for processing;
- the authoritative duplicate-detection and version key;
- recovery after a lost or out-of-order UBER message;
- whether `Has_Changed` can identify all payment-relevant changes;
- compatibility requirements for `Murex`;
- ownership of RATAN-specific supplemental fields;
- EDMI topic retention, partitioning, ordering, replay, and access control;
- whether downstream interfaces remain unchanged or require JSON and ACK/NACK changes;
- migration and reconciliation of historical SCBML records;
- governance of upstream field filtering.

The proposal explicitly warns that `Has_Changed` alone is insufficient. RATANONE should compare a received snapshot with the latest known version to identify impacted cashflows.

## Evidence boundaries

The document contains a concrete TDSX query signature, representative UBER state examples, and a service-by-service migration scope. It does not contain a complete UBER schema, a complete `RatanCashSettlementData` schema, delivery guarantees, performance benchmarks, formal replay semantics, or historical migration test results.

It should therefore be used as a design proposal and source of open questions, not as evidence that the migration was completed or that the proposed interfaces were accepted.

---FILE: wiki/entities/uber.md---
---
type: entity
title: UBER
created: 2026-08-24
updated: 2026-08-24
tags: [uber, tdsx, event-message, cash-settlement]
related: [tdsx, tdsx-uber-message-listener, uber-snapshot-comparison, uber-partial-success-and-completeness, uber-inbound-message-idempotency-and-error-state, ratanone-anti-corruption-layer]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# UBER

`UBER` is an aggregated message format proposed as the principal upstream input for RATANONE strategic cash settlement.

## Contents

A UBER snapshot contains:

- `tradeRecord`;
- `cashFlowData`, an array of cashflow records;
- `FixingNotice`, an array of fixing records;
- a `Has_Changed` map describing reported changes.

The message is generated from the Logic Model and uses protobuf-defined structures and SDKs for consumers.

## Processing implications

UBER provides a trade-level snapshot rather than separate trade and cashflow messages. This may reduce grouping and repeated upstream queries, but aggregation does not guarantee ordering or completeness. The source states that UBER has no sequence indicator and may be lost or delivered out of order.

RATANONE should therefore use [[uber-snapshot-comparison]] and an explicit completeness contract rather than treating `Has_Changed` as the sole processing trigger.

## Contract boundary

The TDSX query result, client-generated UBER message, and RATANONE JSON model are distinct representations. Their mappings, version identifiers, and failure semantics require separate documentation.

---FILE: wiki/entities/tdsx.md---
---
type: entity
title: TDSX
created: 2026-08-24
updated: 2026-08-24
tags: [tdsx, trade-lake, uber, query-api]
related: [uber, bi-temporal-trade-lake-querying, tdsx-uber-message-listener, ratanone-data-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# TDSX

`TDSX` is the upstream data platform and query interface described as the source of UBER trade, cashflow, and fixing snapshots for RATANONE.

## Query model

The source shows that TDSX queries can select trade fields, cashflow fields, fixing notice fields, duplicate bookings, and computed fixing information. Queries can be restricted by `tradeId` and by the `asOf` and `effective` temporal parameters.

The temporal semantics are described in [[bi-temporal-trade-lake-querying]].

## UBER construction

A TDSX API response is not necessarily an UBER message directly. A client constructs `TDSXUberMessage`, derives the first trade ID and tracking version, and converts `hasChanged` values to protobuf wrapper values.

This distinction matters when defining the authoritative boundary between TDSX data, UBER delivery, and the RATANONE common model.

## Open integration concerns

The source does not establish delivery ordering, replay guarantees, a complete versioning contract, or the semantics of partial UBER publication. Those concerns remain relevant to [[uber-inbound-message-idempotency-and-error-state]] and [[uber-partial-success-and-completeness]].

---FILE: wiki/entities/ratanone-data-model.md---
---
type: entity
title: ratanone-data-model
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, data-model, protobuf, json, sdk]
related: [ratanone-anti-corruption-layer, proto-defined-json-data-model, uber, scbml-decommissioning, historical-scbml-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# ratanone-data-model

`ratanone-data-model` is the proposed shared foundation component for RATANONE cash settlement data.

## Responsibilities

The delivery plan assigns it responsibility for:

- integrating TDSX schema and SDK dependencies;
- defining and maintaining `RatanCashSettlementData`;
- converting UBER messages into the common model;
- providing JSON serialization and deserialization;
- providing Kafka serializers and deserializers;
- converting historical SCBML data into the common JSON representation.

The model combines Logic Model fields with RATAN-specific settlement fields, including settlement-instruction data required for internal processing and downstream interactions.

## Schema and transmission choices

The proposal selects protobuf as the schema-definition and code-generation mechanism, while selecting JSON as the inter-service transmission format for readability. No complete `.proto` definition or canonical JSON schema is included in the source.

The model is intended to implement the [[ratanone-anti-corruption-layer]] and support [[historical-scbml-compatibility]].

## Governance risk

The source states that RATAN defines 122 supplemental fields, but most field ownership and status information remains incomplete. The common model should not be treated as final until field source, requiredness, consumer, and lifecycle ownership are documented.

---FILE: wiki/concepts/ratanone-anti-corruption-layer.md---
---
type: concept
title: RATANONE Anti-Corruption Layer
created: 2026-08-24
updated: 2026-08-24
tags: [architecture, anti-corruption-layer, ratanone, data-model, migration]
related: [ratanone-data-model, uber, scbml-decommissioning, historical-scbml-compatibility, message-bridge, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# RATANONE Anti-Corruption Layer

The RATANONE Anti-Corruption Layer is the proposed translation boundary between external message formats and the internal cash settlement domain model.

## Purpose

The layer would translate UBER and legacy SCBML into `RatanCashSettlementData`, centralize serialization and terminology, and prevent individual services from embedding format-specific parsing logic.

This addresses the current pattern in which multiple services parse SCBML independently through XML/XPath extraction and maintain duplicated factories, constants, and mapping code.

## Migration role

The layer supports incremental migration:

- UBER can become the live upstream representation;
- historical SCBML records can continue to be read;
- internal services can migrate to the common model independently;
- downstream systems can continue using SCBML where reverse conversion is required.

The approach is particularly important for [[ratan-cashflow-lifecycle-service]], whose state machine and domain events are described as strongly coupled to SCBML.

## Limitation

An Anti-Corruption Layer does not resolve upstream ordering, completeness, duplicate detection, or schema-governance problems. Those contracts must be defined at the UBER ingestion and common-model boundaries.

---FILE: wiki/concepts/uber-snapshot-comparison.md---
---
type: concept
title: UBER Snapshot Comparison
created: 2026-08-24
updated: 2026-08-24
tags: [uber, snapshots, idempotency, cashflow-identification, versioning]
related: [uber, uber-inbound-message-idempotency-and-error-state, message-bridge-deduplication-key-lifecycle, tdsx, ratanone-anti-corruption-layer]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# UBER Snapshot Comparison

UBER snapshot comparison is the proposed RATANONE technique for identifying changed and eligible cashflows by comparing a received trade-level snapshot with the latest known snapshot.

## Rationale

The source states that UBER has no guaranteed sequence and that `Has_Changed.Cashflows` can be `false` for a trade validation or confirmation change that nevertheless drives payment straight-through processing. A consumer that relies only on the change map could therefore miss a business-significant transition.

Comparison with the latest stored version is proposed as a safer trigger for cashflow identification.

## Required information

A workable implementation needs:

- a stable trade and cashflow identity;
- a version, timestamp, or tracking identifier;
- a defined ordering or freshness rule;
- storage for the latest accepted snapshot;
- handling for duplicate, stale, partial, and out-of-order snapshots;
- a recovery path when an intermediate message is missing.

## Boundary

Snapshot comparison can identify differences between received data and stored data, but it cannot prove that a snapshot is complete unless the upstream completeness contract is explicit.

---FILE: wiki/concepts/uber-partial-success-and-completeness.md---
---
type: concept
title: UBER Partial Success and Completeness
created: 2026-08-24
updated: 2026-08-24
tags: [uber, completeness, partial-failure, cashflow, error-handling]
related: [uber, uber-snapshot-comparison, uber-inbound-message-idempotency-and-error-state, kafka-persistent-retry-and-dlt-recovery, tdsx]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# UBER Partial Success and Completeness

UBER partial success and completeness describe the unresolved behavior when an upstream UBER snapshot is generated while one or more cashflows fail or are omitted.

## Proposed behavior

The source discusses publishing successful cashflows while excluding exceptional cashflows, and introducing an exception indicator that allows RATANONE to filter an unsafe UBER message.

This creates two separate contracts:

- upstream publication may contain only successfully produced cashflows;
- RATANONE eligibility may require rejecting or withholding the entire snapshot when the exception indicator signals incompleteness.

## Unresolved semantics

The source does not define:

- the exception field name or value set;
- whether the indicator is trade-level or cashflow-level;
- whether rejected snapshots are persisted;
- how omitted cashflows are recovered;
- whether a later complete snapshot supersedes a partial snapshot;
- whether partial snapshots can be used for non-payment processing.

Until these semantics are agreed, UBER aggregation cannot be treated as proof of transaction completeness.

---FILE: wiki/concepts/bi-temporal-trade-lake-querying.md---
---
type: concept
title: Bi-Temporal Trade Lake Querying
created: 2026-08-24
updated: 2026-08-24
tags: [bi-temporal, tdsx, trade-lake, historical-data, querying]
related: [tdsx, uber, historical-scbml-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# Bi-Temporal Trade Lake Querying

Bi-temporal querying selects data using both transaction time and business-validity time.

## Parameters

The source defines:

- `asOf`: the transaction-time point at which the Trade Lake record is viewed;
- `effective`: the business-validity point for which the record is requested.

Both parameters are optional and default to `NOW()`.

## Conditions

```text
asOf:
Trade_Lake_Transaction_To_Date_Time > asOf
AND Trade_Lake_Transaction_From_Date_Time <= asOf

effective:
Trade_Lake_Valid_To_Date_Time > effective
AND Trade_Lake_Valid_From_Date_Time <= effective
```

When a new version arrives, the previous version's transaction or validity interval is closed at the new version's timestamp, and the new version remains open to `tMax`.

## RATANONE relevance

These semantics support point-in-time UBER retrieval, historical compatibility, and reconciliation. They do not by themselves define event delivery order or guarantee that every intermediate UBER message was published or consumed.

---FILE: wiki/concepts/proto-defined-json-data-model.md---
---
type: concept
title: Proto-Defined JSON Data Model
created: 2026-08-24
updated: 2026-08-24
tags: [protobuf, json, schema, serialization, ratanone]
related: [ratanone-data-model, ratanone-anti-corruption-layer, uber]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# Proto-Defined JSON Data Model

A proto-defined JSON data model uses protobuf definitions and generated code as the schema authority while transmitting inter-service payloads as JSON.

## Design choice

The source selects:

- protobuf for schema definition, generated classes, cross-language support, and schema evolution;
- JSON for service-to-service transmission because human readability is considered important to the current application.

This is a design trade-off, not a measured performance conclusion. The source provides no RATANONE payload benchmarks comparing JSON and binary protobuf.

## RATANONE application

The pattern is intended for `RatanCashSettlementData`, allowing services to share a governed model while retaining readable payloads for operations and debugging.

The boundary between protobuf-generated UBER structures and RATANONE JSON must specify field naming, null and default values, repeated fields, unknown fields, compatibility rules, and conversion errors.

---FILE: wiki/concepts/scbml-decommissioning.md---
---
type: concept
title: SCBML Decommissioning
created: 2026-08-24
updated: 2026-08-24
tags: [scbml, migration, ratanone, uber, legacy-compatibility]
related: [uber, ratanone-anti-corruption-layer, ratanone-data-model, historical-scbml-compatibility, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# SCBML Decommissioning

SCBML decommissioning is the proposed removal of direct SCBML/XML/XPath dependencies from the RATANONE strategic cash settlement flow.

## Motivation

The source describes SCBML parsing as distributed across grouping, orchestration, lifecycle, SSI stamping, query, LMS, netting, and other services. This creates duplicated extraction logic and makes changes to upstream data representations expensive.

The target state is for services to consume `RatanCashSettlementData`, with UBER serving as the preferred live input.

## Compatibility constraint

Decommissioning does not mean that SCBML can immediately disappear. Existing stored records and live historical data require conversion or an adapter. Downstream systems such as Razor and LMS may also require reverse conversion if their interfaces remain SCBML-compatible.

The migration must therefore distinguish live-input migration from historical and downstream compatibility.

---FILE: wiki/concepts/historical-scbml-compatibility.md---
---
type: concept
title: Historical SCBML Compatibility
created: 2026-08-24
updated: 2026-08-24
tags: [scbml, historical-data, migration, compatibility, ratanone]
related: [scbml-decommissioning, ratanone-anti-corruption-layer, ratanone-data-model, ratan-cashflow-lifecycle-service, cashflow-status-restoration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# Historical SCBML Compatibility

Historical SCBML compatibility is the requirement to continue processing existing SCBML-backed messages and stored records during and after UBER adoption.

## Proposed approach

The source proposes:

- converting SCBML to Logical Model JSON through a converter;
- storing UBER JSON with a message type such as `UBER`;
- selecting the appropriate parser according to the stored raw-message type;
- converting historical data to the common RATANONE model when services are migrated;
- generating SCBML again when an unchanged downstream interface requires it.

## Risks

The source does not provide migration test results or a reconciliation procedure. The implementation must preserve state-machine behavior, domain-event meaning, cashflow identity, status transitions, and downstream output equivalence.

Historical compatibility is therefore a first-class migration workstream rather than a parser convenience.

---FILE: wiki/concepts/trade-level-cashflow-stamping.md---
---
type: concept
title: Trade-Level Cashflow Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, stamping, enrichment, sci-api, uber, performance]
related: [uber, ratanone-data-model, ratan-cash-settlement-ssi-stamping-service, strategic-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# Trade-Level Cashflow Stamping

Trade-level cashflow stamping moves enrichment and settlement-instruction lookup from individual cashflows to an aggregated UBER trade event where the data can be reused.

## Proposed benefit

The source gives an example in which 40 payments under one trade could cause 40 cashflow-level SCI API calls. With an aggregated UBER snapshot, RATANONE may be able to query once at trade level and apply the result to affected cashflows.

This is an expected optimization, not a measured performance result.

## Preconditions

The approach requires confirmation that:

- the enrichment criteria are shared by all affected cashflows;
- the SCI API supports trade-level lookup;
- heterogeneous cashflows can be safely handled;
- partial or exceptional cashflows are excluded or treated explicitly;
- settlement-instruction ownership between TDSX, RATANONE, and CDUPS is defined.

The concept is part of the proposed [[ratanone-anti-corruption-layer]] migration.

---FILE: wiki/queries/what-is-the-authoritative-uber-version-and-deduplication-key.md---
---
type: query
title: What Is the Authoritative UBER Version and Deduplication Key?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, versioning, deduplication, open-question]
related: [uber, tdsx, uber-snapshot-comparison, uber-inbound-message-idempotency-and-error-state, message-bridge-deduplication-key-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# What Is the Authoritative UBER Version and Deduplication Key?

The source states that UBER has no technical version and no guaranteed sequence indicator. It discusses using a timestamp or tracking ID for duplicate and overdue checks, while also noting that a lost intermediate message may remain undetectable.

The authoritative identifier must be confirmed across TDSX, the client-generated UBER message, EDMI delivery, and RATANONE persistence. The answer should define freshness, duplicate, stale, out-of-order, and missing-message behavior.

---FILE: wiki/queries/what-is-the-authoritative-uber-message-completeness-contract.md---
---
type: query
title: What Is the Authoritative UBER Message Completeness Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, completeness, partial-failure, tdsx, open-question]
related: [uber, tdsx, uber-partial-success-and-completeness, uber-snapshot-comparison]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration.md"]
---
# What Is the Authoritative UBER Message Completeness Contract?

The source contains two competing behaviors: UBER may publish successful cashflows while omitting exceptional cashflows, but RATANONE may need to filter the entire message when an exception indicator is present.

The contract must define the exception field, its scope, whether partial snapshots are persisted or processed, and how omitted cashflows are recovered and reconciled with later snapshots.

---FILE: wiki/log.md---
## 2026-08-24 ingest | RATAN - Uber Integration Technical Design

- Ingested the RATANONE UBER integration proposal, including its common-model migration, Anti-Corruption Layer, bi-temporal TDSX query semantics, snapshot-comparison approach, completeness risks, and historical SCBML compatibility requirements.