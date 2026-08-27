---
type: entity
title: SCBML
created: 2026-08-22
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Tech Design-Egypt.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
tags: ["xml", "message-schema", "cashflow", "integration", "scbml", "message-format", "murex", "rat an", "migration", "cashflow-migration", "ratan", "cash-settlement", "group-blotter", "settlement-method", "trade", "identifiers", "settlement", "messaging", "payment-messages", "logical-model", "settlement-instructions", "message", "schema", "CCY-Pair", "fpml", "LMS", "message-contract", "settlement-flow", "trade-processing", "SSI", "regression", "performance"]
related: ["stella", "murex-2-11", "tds3", "ratan-settlement", "cashflow-logical-model", "scbml-cashflow-ingestion-and-persistence", "murex", "ratan", "uber", "ratan-strategic-json-data-model", "murex-to-ratan-cashflow-interface", "mxml-to-scbml-conversion", "murex-ratan-migration-reconciliation", "mxml", "murex-korea", "korea-direct-comp-driven-stp", "what-is-the-authoritative-korea-comp-message-contract-and-stp-eligibility-rule", "group-blotter", "group-blotter-eco-fields", "cdu", "trade-cashflow-reference-linkage", "cashflow-reference-consistency-validation", "trade-event-id-lineage", "cashflowinfo", "ratan-scbml-template-rendering", "cashflow-materialization", "cashflow-withdrawal-and-new", "scbml-ssi-field-mapping", "cover-payment-and-mt103-serial-routing", "ssi-stamping-service", "group-management-service", "ccy-pair-based-nostro-selection", "ssi-stamping", "scbml-trade-enrichment-api", "fmrp", "lms", "scbml-cashflow-data-message", "swift-suppressed-lms-feed-contract", "cashflow-status-change-event-contract", "scbml-event-payload-storage-impact", "razor", "uber-scbml-performance-regression-testing", "25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up", "cdups", "ssi-stamping-and-best-match", "schema-evolution-for-cash-settlement", "ratanone", "uber-fxu-technical-live-and-business-go-live-2026", "release-branch-synchronization-and-deployment-gating", "cashflow-lifecycle-state-machine-restructuring"]
---

# SCBML

## Identity and role

SCBML is an XML-based message schema and message format used for cashflow data in the Stella/Murex 2.11 → TDS3 → Ratan interface. The Cashflow Logical Model & Templates functional-requirements source specifically describes SCBML 4.0 cashflow payloads.

The SCBML Template source identifies SCBML as the XML message format used for publishing Ratan cashflow data. Its supplied templates target SCBML version `4-0` and embed a `cashflowPayload`.

The template source further describes SCBML as the target serialization format for values calculated or received by Ratan services. [[ratan-scbml-template-rendering]] describes the intended separation between populating [[cashflowinfo]] and rendering the resulting message.

The template source identifies two producers:

- **Ratan Netting Service**, for resultant netted cashflows.
- **Murex → Ratan Interface**, for cashflow values extracted from inbound [[mxml]].

The RATAN–Uber Integration technical-design source describes SCBML as the legacy message format used by the existing BAU and Murex cashflow-processing flow. In its evaluated current-state option, FMRP and Murex provide SCBML to Standardization Service, and SCBML remains the outbound format.

The SSI Stamping Notification functional-requirements source describes SCBML as the payment-message and logical-model format enriched by RATAN after SSI selection or approved manual SSI remediation.

The SSI Stamping Tech Design-Egypt source describes SCBML as the XML message format used as both input and output of the [[ssi-stamping-service]].

The FX Replication Status Write Back technical-design source identifies SCBML as the XML envelope and payload format used by its sampled Razor `CashflowStatusChange` message. This is a source-specific example and does not establish that all SCBML messages have a cashflow-status payload.

Other source-specific uses are described below:

- The Korea-migration functional-requirements source identifies SCBML as the target message format for the Korea direct Murex-to-RATAN `COMP` status path.
- The deprecated CDU Trade Confirmation Notification & Cashflow source identifies SCBML as the format carrying trade and cashflow metadata for a proposed Reference ID design.
- The deprecated Cashflow Events Control Draft 1 identifies SCBML as the message format used for the draft's event-level processing discussion.
- The LMS Settlement Day2 requirement identifies SCBML as the proposed XML message format for the LMS `CashflowData` feed.
- The Strategic SSI Stamping Design source identifies SCBML as the message format at the documented trade SSI-stamping integration boundary.
- The Uber & FXU Technical Live Plan includes SCBML as a processing and message-format domain within its UBER and FXU live-plan scope.

## Namespaces and payload identity

The SCBML Template source lists these core namespaces:

- `http://www.sc.com/SCBML-1`
- `http://www.fpml.org/FpML-5/confirmation`
- `http://www.fpml.org/FpML-5/ext`
- `http://www.sc.com/scbml/extension-2-0`
- `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.03`

The templates identify the message as:

```xml
<scb:typeName>CashflowData</scb:typeName>
<scb:payloadFormat>XML</scb:payloadFormat>
<scb:payloadType>cashflowPayload</scb:payloadType>
<scb:payloadVersion>4-0</scb:payloadVersion>
```

According to the template source, the payload includes:

- Cashflow header data
- Payment details
- Trade-reference information
- Product and portfolio information
- STP indicators
- Workflow controls
- Parties

The SSI Stamping Tech Design-Egypt source also shows SCBML version `4-0`, with FpML confirmation content embedded in `scb:FPMLPayload`. Its messages include trade parties, product identifiers, exchanged currencies, settlement instructions, process state, and confirmation data.

The LMS requirement likewise uses SCBML version `4-0`, an XML `cashflowPayload`, and FpML confirmation elements. In that requirement, the template is proposed rather than finalized.

The sampled Razor `CashflowStatusChange` message in the FX Replication Status Write Back source declares `scbmlVersion="4-0"` and uses `cashflowPayload` version `4-0`. It contains header metadata, process metadata, and a cashflow-status business payload. Referenced XSD locations appear in the XML, but that source does not confirm that they resolve or that the sample validates against them.

The Strategic SSI Stamping Design source does not provide a complete SCBML schema, namespace contract, versioning policy, or canonical XPath catalog for the trade SSI-stamping boundary.

## Message structure and cashflow content

A message can contain one or more `<scb:cashflow>` elements, and each cashflow can itself contain one or more `<scb:payment>` elements. These cardinality levels have distinct Ratan processing requirements described in [[scbml-cashflow-ingestion-and-persistence]] and [[intent-to-settle-payment-selection]].

SCBML carries inbound lineage, lifecycle, payment economics, trade context, party information, SSI data, and STP/NSTP indicators. Some values are mapped directly from SCBML; others require enrichment or are managed internally by Ratan. See [[cashflow-logical-model]].

The LMS `CashflowData` requirement states that its proposed message contains:

- Cashflow identifiers
- Business-event data
- Payment details
- Trade references
- Party identifiers
- Settlement instructions

This statement describes the proposed LMS feed and does not by itself establish that every listed element is mandatory for all SCBML messages.

SCBML payload structure should not be conflated with persistence behavior; see [[scbml-event-payload-storage-impact]].

## SSI stamping and settlement-instruction enrichment

According to the SSI Stamping Notification functional-requirements source, RATAN enriches SCBML after SSI selection or approved manual SSI remediation.

That source maps settlement-instruction data into SCBML for:

- Account details
- Beneficiary details
- Ordering-customer details
- Remittance information
- Sender-to-receiver information
- POP Dubai
- Bank-routing fields including `54A`, `56A`, and `57A`

The SSI Stamping source's documented paths contain typographical and incomplete expressions. They require technical validation before becoming an implementation contract. See [[scbml-ssi-field-mapping]] and [[cover-payment-and-mt103-serial-routing]].

### SSI Stamping service API use

According to the SSI Stamping Tech Design-Egypt source, SSI Stamping receives SCBML encoded as Base64 in the API `message` field and returns a Base64-encoded enriched SCBML message.

That source states that the service parses:

- Legal-entity FMID
- Counterparty FMID
- Payment currencies
- Product classification and CFI-related attributes
- Settlement method and settlement type
- Payer and receiver information used to derive debit/credit behavior

### Trade SSI-stamping integration boundary

According to the Strategic SSI Stamping Design source:

1. CDUPS sends SCBML to RATANONE.
2. The trade SSI-stamping flow extracts the required inputs from the message.
3. The flow applies SSI matching.
4. The flow returns enriched SCBML.

The Strategic SSI Stamping Design source states that SCBML parsing is not uniform across trade types. XPath locations differ, limiting reuse between the trade and cashflow API implementations even though their matching logic is shared. This source-specific observation concerns the trade SSI-stamping integration and should not be generalized to all SCBML consumers.

### Multi-entity compatibility design

According to the SSI Stamping Flow's *Compatibility design for multiple entities* source, SCBML is the message source for the booking-entity FM ID, product taxonomy, and a proposed new `CCY Pair` attribute.

The source identifies these existing paths:

```text
Entity FM ID:
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']

Product taxonomy:
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productId[@productIdScheme="http://www.fpml.org/coding-scheme/product-taxonomy"]
```

That source marks the `CCY Pair` XPath as `TBD`. The final schema definition must be confirmed before the value can be treated as an authoritative message contract. See [[ccy-pair-based-nostro-selection]].

### XPath and sample-data concerns

The SSI Stamping Tech Design-Egypt source states that SCBML XPath expressions were upgraded to XPath 2.0 while the legacy implementation uses XPath 1.0. XPath expressions and namespace bindings in that source contain apparent inconsistencies and require validation before implementation.

The concrete confirmation sample in the SSI Stamping Tech Design-Egypt source uses country code `KE` and `SCBLKEN*NBO`, despite the source filename referring to Egypt.

## LMS `CashflowData` feed and Swift Suppressed status

The Settlement Day2 LMS requirement concerns including `Swift Suppressed` status in the LMS feed, but only for receipts.

That requirement does not define a dedicated SCBML field for `Swift Suppressed` status. It leaves open whether the status should be encoded through `businessEvent`, another existing SCBML element, or a contract extension.

Final agreement is required before the representation of `Swift Suppressed` status can be treated as part of the LMS SCBML contract. The LMS requirement's template remains proposed rather than finalized.

## Withdrawal and new events

The deprecated Cashflow Events Control Draft 1 states that, for Stella messages containing both withdrawal and new events, the events are represented as separate events with individual SCBML records.

According to that draft, separating the events supports event-level processing and is relevant to the proposed ordering control requiring withdrawal processing to complete before a replacement cashflow can proceed.

The draft does not define the SCBML schema, message envelope, correlation fields, delivery guarantees, or authoritative event-ordering contract. Its event-sequencing statements therefore remain specific to that draft and do not establish a general SCBML implementation contract.

## Trade and cashflow Reference ID proposal

According to the deprecated CDU Trade Confirmation Notification & Cashflow source, the proposed solution would persist a Reference ID in both trade SCBML and cashflow SCBML.

The source identifies the following candidate paths for associated trade and process metadata:

```text
Trade ID:
/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/*/(*:originalTrade|*:trade))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:tradeId[@tradeIdScheme="http://www.sc.com/coding-scheme/tradeId"]

Tracking Version:
/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:trackingVersion

Event ID:
/scb:SCBML/scb:payload/scb:FPMLPayload/scb:header/scb:process/scb:eventId[@eventIdScheme="http://www.sc.com/coding-scheme/eventId"]
```

For an economic trade update that affects cashflows, the Reference ID would change in the trade SCBML and be copied into the generated cashflow SCBML. For status transitions and non-economic changes, it would remain unchanged. Cashflows generated by fixing events would inherit the Reference ID from the parent trade.

The CDU source does not specify the XML location, datatype, ownership, uniqueness scope, or mandatory presence of the proposed Reference ID.

## Korea direct Murex-to-RATAN `COMP` path

According to the Korea-migration functional-requirements source, the documented SCBML contract for this path:

- Sets the originating-system sender to `Murex`.
- Maps `COMP` into `process/subState`.
- Maps `validation` into `process/transactionType`.
- Maps the party entity and the Murex internal trade ID.
- Derives a product taxonomy identifier from Murex trade-category components.

The paths preserved in that source contain potentially malformed or incomplete XPath attribute expressions and Markdown-rendered URI values. They must not be treated as schema-valid implementation specifications without comparison to canonical SCBML definitions and actual payloads.

## Uber coexistence, migration, and live-plan regression

According to the RATAN–Uber Integration technical-design source, the proposed Uber migration does not immediately eliminate SCBML. Historical data and Murex data must remain compatible, and some cashflows in Uber entity scope may continue to carry SCBML because they are historical.

That source identifies a strategic tension between removing SCBML from RATAN processing and retaining it to reduce migration risk. This creates either a dual-workflow, dual-format operating model or a longer incremental migration.

Routing mechanisms must distinguish entity scope from message format. A cashflow being in Uber scope is not sufficient evidence that it can be handled as JSON.

The authoritative handling rule for historical SCBML cashflows in Uber scope remains open.

The *PT result for UBER* technical-design source describes the existing Cash Settlement SCBML flow as the performance-regression baseline for Uber adoption. That source records a requirement that Uber adoption must have no performance impact on the SCBML flow.

The source's single mixed-workload Round 1 result was run without Message Bridge. It does not provide a same-environment SCBML-only baseline and therefore cannot establish that the no-performance-impact requirement has been met. [[uber-scbml-performance-regression-testing]] defines the controls needed to evaluate that claim.

The Uber & FXU Technical Live Plan states that its release scope includes SCBML processing for other entities. Its readiness expectations include SCBML-focused regression covering BAU cases and performance testing intended to demonstrate no downside relative to current production behavior.

The live-plan source records a delayed Case Enrichment / settlement-method regression and a stated need to rerun full performance testing at prior volume. It does not establish final regression completion or production performance acceptance.

## Relationship to Group Blotter Eco Fields

The 2026 Group Blotter field inventory identifies `Settlement_Method` as a logical-model field with release-specific sourcing. For the SCBML version, the Group Blotter source states that the value is taken from the production `Cashflow Record`.

This statement is specific to `Settlement_Method`. It does not establish the sourcing, availability, or release behavior of the other Group Blotter fields.

The Group Blotter source does not define whether `Settlement_Method` is stored or derived. It also does not provide the field's data type, permitted values, update behavior, or validation rules. The authoritative SCBML implementation contract remains open.

## Template and implementation limitations

The SCBML Template source does not provide:

- An Amendment template, despite claiming coverage of Amendment events.
- XML schema-validation results.
- A deployed implementation version.
- Consumer acceptance criteria.
- Authoritative definitions for `cashflowVersion`, `businessVersion`, and `cashflowMinorVersion`.

The New and Withdrawal examples also differ structurally and contain inconsistent template-expression capitalization. These issues should not be treated as resolved SCBML behavior without implementation evidence.

The deprecated Cashflow Events Control Draft 1 likewise does not establish authoritative envelope, correlation, delivery, or ordering semantics.

The Strategic SSI Stamping Design source separately states that it does not provide a complete SCBML schema, namespace contract, versioning policy, or canonical XPath catalog. This limitation applies specifically to the trade SSI-stamping integration boundary and reinforces the need to validate XPath and schema assumptions against canonical definitions and actual payloads.