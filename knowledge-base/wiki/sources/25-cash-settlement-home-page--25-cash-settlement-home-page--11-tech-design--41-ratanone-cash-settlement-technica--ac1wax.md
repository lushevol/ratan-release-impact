---
type: source
title: Strategic SSI Stamping Design
authors: []
year: 2025
url: ""
venue: ""
tags: [cash-settlement, RATANONE, UBER, SSI-stamping, technical-design, WIP]
related: [ratan-uber-integration-technical-design, trade-level-ssi-stamping, product-agnostic-ssi-stamping, trade-ssi-stamping-idempotency-and-versioning, group-service-vs-orchestration-for-ssi-stamping, cashflow, orchestration, nstp-service, ssi-stamping-reference-data]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# Strategic SSI Stamping Design

## Status and scope

This is a work-in-progress target-state design for SSI stamping within the RATAN–UBER integration. It proposes a product-agnostic flow in which RATAN receives UBER trade messages, normalizes them into the RATAN Logic Model, stamps the trade, reuses the result for associated cashflows, and propagates SSI refreshes to downstream systems.

The design is not an approved implementation contract. Exception handling, UBER SSI structure, refresh scope, business justification, product mapping, API details, and database schemas remain incomplete.

## Objectives

- Provide a unified, product-agnostic SSI stamping API with a single responsibility.
- Reuse trade SSI stamping results for cashflows wherever the match is safe.
- Use UBER as the standard exchange format between RATAN and CDUPS.
- Support the target architecture described in the broader UBER integration design.
- Store SSI information in the RATAN cashflow model and translate it to SCBML when sending to Razor.

## Proposed flow

An inbound UBER message is decoded into the RATAN Logic Model. Product-specific currency and settlement fields are normalized into a common stamping input. RATAN or its orchestration layer invokes the SSI stamping service and stores the trade-level result.

When cashflows arrive, RATAN queries the trade result and attempts to match the result to each cashflow using currency, direction, and other yet-to-be-defined attributes. A successful match enriches the cashflow. An unsuccessful match raises an exception and routes the cashflow toward NSTP handling.

If a trade result is missing, failed, or partially failed, the design proposes ad hoc trade stamping or compensating batch stamping using cashflow information.

## Trade identity and concurrency proposal

The proposed persistence identity is `tradeId + majorVersion`. A result already stored under that key should not be restamped. A unique constraint should allow only one concurrent process to persist a result; a process that loses the key conflict should retry and then use the already-persisted result.

The source also questions whether `MajorVersion` is authoritative and considers alternatives such as `traceId` or `asOf + effectiveDate`. The query API is described as accepting only `tradeId`, creating an unresolved mismatch with versioned storage.

SSI refresh is intended to affect only the latest major version. The source does not define how “latest” is determined or how historical results are queried.

## Alternative service placements

**Option A — Group service.** Group service performs batch stamping and obtains enriched cashflows. SSI data later overrides existing lifecycle-service data. A mechanism is required to prevent concurrent access to the same cashflow.

**Option B — Orchestration.** Orchestration coordinates UBER-triggered trade stamping and reuses the result for cashflows. The SSI stamping service is invoked `1 + N` times in the described flow.

No option is selected.

## SSI refresh notifications

The design identifies deficiencies in the current SSI update notification flow, including complex queries for impacted cashflows and the lack of trade SSI support. It proposes addressing impacted trades and cashflows, refreshing both trade and cashflow SSI, and notifying downstream systems.

The SSI notification topic is described as single-partitioned to enforce sequential consumption. This addresses notification ordering only; it does not define source-message ordering, duplicate handling, out-of-order versions, or refresh reconciliation.

## Structured source data

### CDUPS request model

| Key | Data Model | Sample |  |
| --- | --- | --- | --- |
| Trade_Id | { "key": [logical model indexed term], "value": [actual value] } 1. Value + Key will be used for validation. 2. Trade_Id to be used for linkage. 3. Value will be used for stamping query. | { "key": "Trade_Id", "value": "4354367341"} | |
| Major_Version | { "key": "Trade_Lake_Trade_Major_Version", "value": "5"} | | |
| Trade_Date | { "key": "Trade_Date", "value": "2025-05-01"} | | |
| | | | |
| Booking Entity Fmid | { "key": "Entity.Booking_Entity_SCI_FMID", "value": "USD"} | | |
| Counterparty Fmid | { "key": "Entity.Counterparty_SCI_FMID", "value": "400202766"} | | |
| CFI | { "key": "Instrument_Common.CFI_Code", "value": "SRCXCX"} | | |
| --------------------------Start Loop Array [ | | | |
| Currency_X | { "key": "Swap_Instrument.IR_Leg.First_Leg.Notional_Amount_Currency", "value": "USD"} | | |
| PayReceive_Currency_X | { "key": "Swap_Instrument.IR_Leg.First_Leg.Payer_Party_Reference", "value": "party1"} | | |
| ]--------------------------End Loop Array | | | |

### UBER message mapping

| Field | UBER path | Example value | Remark |
| --- | --- | --- | --- |
| Product type | Instrument_Common.ISDA_Taxonomy | InterestRate:LoanDeposit InterestRate:IRSwap:OIS | Need a mechanism to map to existing product type (IRS, BullionSwap, etc) |
| Tracking Id | Trade_Lake_Trade_Id | | |
| Trade Id | | | |
| Party1 FMID | Entity.Booking_Entity_SCIFMID | | |
| Party2 FMID | | | |

### Proposed database tables

| TABLE | Columns | Description |
| --- | --- | --- |
| cashflow_stamping | | |
| cashflow_stamping_legacy_exception | | |
| stamped_nostro_account | | |
| stamped_vostro_account | | |
| maker_checker_request | | |
| trade_stamping_message | | |
| raw_message | | |

No SQL DDL, field definitions, constraints, foreign keys, indexes, or lifecycle states are supplied. The unique constraint on `tradeId + majorVersion` is described only in prose.

### Proposed API schema

| API | INPUT | OUTPUT | USER |
| --- | --- | --- | --- |
| batch SSI stamping | currencies | mapping of refId → stamp result | Potentially be used by RATAN services |
| trade SSI stamping | UBER | parsed currencies refId → stamp result | orchestration service |
| trade SSI stamping query | tradeId | parsed currencies refId → stamp result | group service |

The referenced attachment `strategic-ssi-stamping.yml` is unavailable in the source context.

## Open design risks

The design leaves the following contracts unresolved:

- Authoritative trade message identity and version ordering.
- Complete trade-to-cashflow matching key.
- Idempotency and repeated-request semantics.
- Partial-failure, retry, compensation, and NSTP behavior.
- Ownership between Group service and orchestration.
- Impacted-record lookup and refresh propagation.
- API error semantics and database lifecycle schema.
- Evidence for the expected reduction in stamping volume and operational cost.

## Related architecture

This design specializes the broader [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku]] and connects [[entities/cashflow]], [[entities/orchestration]], [[entities/nstp-service]], [[concepts/ssi-stamping-reference-data]], and [[concepts/cashflow-stamping-domain-ownership]].