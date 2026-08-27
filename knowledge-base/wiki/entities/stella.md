---
type: entity
title: Stella
created: 2026-08-23
updated: 2026-08-24
tags: ["integration-system", "cashflow-delivery", "upstream-system", "Stella", "settlement", "cashflows", "migration", "cashflow-source", "netting", "trade-processing", "integration", "cashflow-id", "cash-settlement", "settlement-system", "cashflow-splitting", "booking", "cashflow-events", "trade-amendment", "cashflow", "expiry", "inbound-events", "messaging", "ratan", "message-producer", "test-input", "cn-settlement", "system", "trade-source", "scbml", "fmrp", "rebook-exception", "cashflow-source-system", "cfi-code", "downstream-system", "settlement-status", "external-platform", "transaction-workflow", "status-synchronisation", "trade-status", "trade-xml"]
related: ["fmrp-china-cash-settlement", "blade", "ratan", "fmo-post-trade-portal", "fxo-mini-trade-migration-ratan-cash-settlement", "ratan-settlement", "high-risk-nstp-rule", "cashflow-suppression", "trade-cashflow-reconciliation", "ad-hoc-cashflow-netting", "cashflow-failure-and-reinstatement", "ratan-cashflow-blotter", "murex-2-11", "scbml", "tds3", "scbml-cashflow-ingestion-and-persistence", "ratan-cashflow-id-management", "murex-stella-rule-parity", "what-is-the-authoritative-bcs-swift-field-20-format", "cashflow-splitting", "split-cashflow-downstream-integration", "murex-reversal-and-new-cashflow-matching", "cashflow-migration-readiness", "non-trade-event-cashflow-updates", "cashflow-event-withdrawal-reconciliation", "how-should-stella-expiry-and-withdrawal-events-reconcile-in-ratan", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tec--1uz12d6", "cashflow-record", "stella-cashflow-amendment-supersession", "cashflow-materialization", "cashflow-blotter", "cashflow-amendment-supersession", "value-date-based-cashflow-materialization", "failed-cashflow-status", "cashflow-event-versioning", "cashflow-partial-update", "cashflow-lifecycle-supersession-and-audit-history", "fmrp", "trade-lake", "cdups", "trade-ssi-stamping", "rebook-exception", "payment-date-proximity-matching", "automated-cashflow-rounding", "what-is-the-authoritative-cashflow-rounding-contract", "ssi-plus", "ssi-stamping-behavior-differences", "murex-211", "cashflow-status-write-back", "backward-workflow-design", "cash-settlement-platform", "ratanone-stella-ambassador", "sabre-booking-api", "stella-transaction-workflow-consistency", "group-management-service", "cashflow", "non-economic-cashflow-amendment", "cashflow-replacement-mapping", "ratan-cdups-trade-confirmation-flow", "strategic-fm-re-platforming-sfmrp"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md", "Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Cashflow & Payment cashflow id management.md", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Settlement Day2 Requirement -- Cashflow Splitting -- Cash Settlement Home Page -- Functional Requirement -- Settlement Day2 Requirement -- Cashflow Splitting -- Cashflow Splitting UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Stella Inbond cashflow filter.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md", "RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---

# Stella

Stella, also rendered as `STELLA` in source documentation, is documented in several distinct source contexts. These include upstream cashflow and trade-data roles, test and demonstration inputs, cashflow-mapping records, status-update integrations, and an API role in an FMRP trade-confirmation route.

## FMRP trade-confirmation flow

The **Ratan and CDUPS 51512** source describes Stella as an API service in an FMRP trade-confirmation route.

For trades booked in [[blade]] and confirmed in [[cdups]]:

1. CDUPS calls the Stella API.
2. Stella updates the trade status.
3. Stella sends trade XML to RATAN through [[tds3]].

That source does not explicitly establish whether “FMRP” is equivalent to [[strategic-fm-re-platforming-sfmrp]], so that relationship requires verification. It also does not state whether the instruction to send to Stella after an ACK is limited to FMRP trades.

These trade-confirmation details are specific to the **Ratan and CDUPS 51512** source. They do not, by themselves, establish that the cashflow, status-update, trade-data-template, demonstration, or other Stella roles use the same API, trade-status model, XML format, routing path, or acknowledgement behavior.

## Strategic cashflow status-update integration

The **Strategic Cashflow Stella Ambassandor** source describes Stella as the external transaction and workflow platform that receives Ratan strategic-cashflow status updates through [[ratanone-stella-ambassador]] and `sabre-booking-api`.

For a transaction, Stella requires successive actions to remain on the same workflow. The same source records `TRANSACTION_WORKFLOW_MISMATCH` when an action on `Cash Settlement` conflicts with an existing `Standard Cash Settlement` workflow.

Stella exposes the `RATANCASH_V2("ratancash-v2")` channel for strategic cashflows. Its API responses may report success before synchronization with [[trade-lake]] is durably complete.

These strategic-cashflow integration details are specific to the Strategic Cashflow Stella Ambassandor source. They do not, by themselves, establish that the demonstration, upstream cashflow, trade-data, mapping-record, FMRP trade-confirmation, or other Stella roles use the same channel, API, workflow, or durability behavior.

## Cashflow and trade-data roles

CN Settlement demonstration sources describe Stella as an upstream source of mocked cashflow messages for functional demonstrations and demo cases processed by [[ratan]]. In those flows, Stella-originated messages are manually pushed into the RATAN workflow and may be verified through the [[cashflow-blotter]].

The H1 2024 cashflow-migration rounding source describes Stella as an upstream system that books cashflows and supplies them to [[ratan]] in SCBML format. This source-specific description should not be taken as establishing the production responsibilities, interface, ownership, or message contract of the Stella cashflow flows in the CN Settlement demonstration sources.

Separately, the trade SSI stamping product-template source identifies STELLA as the originating trade-data system in SCBML templates. This trade-data role is distinct from both the cashflow demonstration and cashflow-rounding contexts.

The failed-cashflow requirement separately describes Stella as an upstream or event-producing system. The Vostro SSI requirement identifies STELLA as the upstream system responsible for stamping CFI codes on specified cashflows.

The rebook-exception requirement identifies Stella as a named source population included in reported Ratan rebook-exception volumes.

### Cashflow-mapping records

The **Group Management Service – Non-Eco Amendment Technical Design** identifies Stella as the source system for cashflows in proposed `ratan_cashflow_mapping` and `ratan_cashflow_mapping_history` records, where `source_system` is exemplified as `STELLA`.

This proposed-record usage does not, by itself, define Stella's production message contract, technical interface, or the identifier and matching rules used by other Stella-related sources.

## CFI-code stamping responsibility

The Vostro SSI requirement assigns the following CFI-code stamping responsibilities:

- STELLA stamps CFI codes on BLADE, CFETS, and S2BX cashflows.
- [[ratan]] stamps CFI codes on Murex 2.11 cashflows.

The source does not define precedence or reconciliation when an upstream CFI code is missing, malformed, or inconsistent with the SSI+ mapping. This responsibility split is an example of [[ssi-stamping-behavior-differences]].

## Cashflow rounding for H1 2024 migration

The H1 2024 cashflow-migration rounding source states that the strategic intent is for Stella to round its cashflows before sending them to Ratan. Stella was not ready to deliver that capability before the H1 2024 cashflow migration.

As a tactical measure, [[ratan]] must round Stella-booked cashflows using [[murex-2-11]] BAU behavior as a reference. This reference to Murex 2.11 describes the required tactical Ratan behavior; it does not establish that Stella has the same rounding behavior as Murex 2.11.

The source identifies the Stella input amount path as:

```text
/scb:SCBML/scb:payload/scb:cashflowPayload/ scb:cashflow/scb:payment/conf:paymentAmount/conf:amount
```

The source-to-target mapping is incomplete for Stella. See [[what-is-the-authoritative-cashflow-rounding-contract]].

## Trade SSI stamping templates

In the SCBML templates used by the trade SSI stamping flow, STELLA messages provide:

- trade identifiers;
- event metadata;
- temporal information;
- product structure;
- party references;
- currencies;
- settlement method; and
- product-specific fields supporting [[ratan]] lookup.

Example tracking IDs use the `STELLA` prefix.

The same source includes a historical Fixing Notice example whose sender is `MDS`. That historical example should not be generalized as the normal sender for STELLA trade-data messages.

## CN Settlement demonstration context

### Sprint 13

The Sprint 13 RATAN demo scenarios use mocked Stella `New` and `Amendment` messages that are manually pushed into the RATAN workflow.

For the Sprint 13 flow:

- A Stella `New` message is expected to create a stored cashflow.
- The initial state of that cashflow depends on the payment-date VD position.
- A Stella `Amendment` for the same cashflow is intended to replace the `New` cashflow in [[ratan-cashflow-blotter]] display.
- The documented retention and correlation rules for the replacement are unspecified.

### Sprint 14

The Sprint 14 CN Settlement functional demo documents Stella as the source of mocked `New` and `Amendment` cashflow messages. Its test flow also manually pushes Stella messages to the RATAN workflow.

### Sprint 17

The Sprint 17 specification uses Stella to provide:

- CCS initial- and final-exchange cashflows;
- forward-trade cashflows at T+5, T+6, and T+7;
- spot-trade cashflows for amendment, withdrawal, and netting scenarios.

Stella-originated messages in these scenarios are manually pushed into the RATAN workflow and verified through the [[cashflow-blotter]].

## Failed-cashflow behavior

The failed-cashflow requirement states that new cashflow events from Stella can overwrite cashflows while they are in `FAILED` status.

That source does not define:

- whether the overwrite affects the status, the entire cashflow, or selected fields;
- event ordering;
- duplicate handling;
- stale-event protection; or
- the relationship between Stella events and Ratan reinstatement.

This behavior should be reconciled with [[cashflow-event-versioning]], [[cashflow-partial-update]], and [[cashflow-lifecycle-supersession-and-audit-history]] before being treated as a general lifecycle rule.

## Rebook-exception reporting

The Ingenuine Rebook Exception requirement reports Murex and Stella rebook-exception volumes as an aggregate, with parenthetical component counts.

That source does not define Stella's platform role, its identifiers, or whether Stella matching behavior is identical to the Murex-specific Original Trade ID rule. The Murex correlation rule should not be assumed to apply unchanged to Stella without further evidence.

## Status synchronization

### Generic backward workflow

The [[backward-workflow-design]] source names STELLA as one possible downstream synchronization target for updated cashflow status from [[ratan]].

That source does not provide a STELLA endpoint, payload, transport, acknowledgement model, retry policy, or error contract. It also does not state whether STELLA receives the same payload that Ratan sends to the Adaptor.

The precise STELLA integration path remains open and should not be inferred from the documented Ratan-to-Adaptor payload. This backward-workflow role is separate from the upstream cashflow, trade-data, CFI-stamping, FMRP trade-confirmation, and demonstration roles described above.

The Strategic Cashflow Stella Ambassandor source provides a more specific strategic-cashflow status-update path through [[ratanone-stella-ambassador]] and `sabre-booking-api`. That source-specific path does not resolve the broader endpoint, payload, transport, acknowledgement, retry, or error-contract gaps in the generic backward-workflow requirement.

### Netting and unnetting acknowledgements

The **Group Management Service – Non-Eco Amendment Technical Design** describes Stella status synchronisation for Netting and Unnetting. Under that design:

- a failed acknowledgement received from “Stella ambassador” is expected to mark a blocking-queue record as `FAILED` and generate an exception;
- a later successful Netting acknowledgement is expected to mark that record `SUCCESS`; and
- that successful Netting acknowledgement is expected to trigger Unnet status synchronisation.

This source does not define Stella's API contract, the technical identity or deployment boundary of Stella ambassador, acknowledgement correlation, retry policy, or ownership of blocking-queue processing.

These Netting and Unnetting expectations are specific to the Group Management Service design. They do not establish that the generic backward-workflow target, the strategic-cashflow status-update route, the FMRP trade-confirmation route, or all other Stella integrations use the same acknowledgement handling, queue processing, or synchronization sequence.

## Scope and limitations

The available CN Settlement demonstration documentation identifies Stella in a test and demonstration context only. The Sprint 14 source does not establish Stella's production responsibilities, message contract, or operational ownership.

The documented cashflow sources do not identify Stella's technical interface, production message schema, or production scope. The Sprint 17 source also does not establish whether its documented materialization behavior applies to all Stella products.

The H1 2024 rounding source identifies Stella as supplying SCBML-format cashflows to Ratan and specifies an input amount path, but its Stella source-to-target mapping is incomplete. It does not by itself establish a complete Stella message contract.

The trade SSI stamping template source establishes STELLA's role within its SCBML trade-data templates, but does not by itself establish the production scope, operational ownership, or message contract of the Stella cashflow flows described in the demonstration sources.

The Vostro SSI requirement establishes the stated STELLA/RATAN CFI-code stamping split, but does not define handling or precedence for missing, malformed, or inconsistent upstream CFI codes.

The rebook-exception source likewise does not establish Stella's platform role, identifier model, or matching rules.

The backward-workflow source establishes only that STELLA is a possible downstream target for updated cashflow status; it does not establish a deployed integration or a complete status-write-back contract.

The Strategic Cashflow Stella Ambassandor source establishes the strategic-cashflow channel, workflow-consistency behavior, and status-update route described above, but does not establish that those details apply to every Stella integration or product. It also records that an API success response may precede durable Trade Lake synchronization, so API success should not by itself be treated as proof of completed downstream synchronization.

The Group Management Service – Non-Eco Amendment Technical Design establishes proposed mapping-record and Netting/Unnetting synchronization behavior only. It does not define Stella's API contract, Stella ambassador's technical identity or deployment boundary, acknowledgement correlation, retry policy, or blocking-queue-processing ownership.

The **Ratan and CDUPS 51512** source establishes only the FMRP trade-confirmation route in which CDUPS calls Stella, Stella updates trade status, and Stella sends trade XML to RATAN through [[tds3]]. It does not establish that this route applies to all trades, all FMRP interpretations, cashflow delivery, or other Stella integrations.