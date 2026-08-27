---
type: source
title: RATAN and CDUPS Interface 51512
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, cdups, interfaces, trade-confirmation, affirmation, settlement]
related: [ratan, cdups, ratan-cdups-trade-confirmation-flow, ratan-cdups-econaffirm-acknowledgement, ratan-interface-architecture, ratan-interface-inventory, ratan-ssi-stamping, operational-level-agreement]
sources: ["RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---
# RATAN and CDUPS Interface 51512

## Scope

This document describes the interface and end-to-end flow between [[entities/ratan]]/RATANONE and [[entities/cdups]] for trade SSI stamping, trade confirmation, trade-information exchange, and affirmation-status exchange.

The source was generalized to use BPMS APP and Interface APP naming conventions, with “RATAN and TDS3” given as an example. Its content is nevertheless specifically about RATAN and CDUPS. The document status field is blank despite a review date of 2026-03-19, so it should be treated as a preliminary flow inventory rather than confirmed as Published.

## Document maintenance

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Junying Jiang @Yunzhe Ta | 2026-01-19 | @Daiqi Wang @Yunzhe Ta | 2026-03-19 | |

## Business functions

The source identifies three high-level interactions:

1. CDUPS calls a RATAN API for trade SSI stamping. The API is noted as missing from the RATAN-CDUPS OLA.
2. CDUPS sends trade-confirmation information to RATAN.
3. RATAN sends trade information to CDUPS for confirmation-related processing.

The summarized end-to-end flow is:

```text
1. Stamping: CDUPS call Ratan API for trade SSI stamping
2. CDUPS →Solace →Ratan (trade confirmation)
3. Ratan →Solace →CDUPS (trade info)
```

## Trade-confirmation routes

The route depends on the originating booking system and must not be generalized into one universal path.

- **Murex trades:** Trades are booked in Murex and confirmed in CDUPS. CDUPS sends a trade-confirmation event to [[entities/tds3]], and RATAN synchronizes trade state, including the cashflow STP condition, from TDS3.
- **BCS trades:** Trades are booked in [[entities/edrisque]] and confirmed in CDUPS. CDUPS sends the trade-confirmation event directly to RATAN, described as inbound and outbound. TDS3 does not contain this data.
- **FMRP trades:** Trades are booked in [[entities/blade]] and confirmed in CDUPS. CDUPS calls the [[entities/stella]] API; Stella updates the trade status and sends trade XML to RATAN through TDS3.

The source also states that [[entities/cdu-is]] subscribes to trade messages from RATAN for confirmation.

## RATAN-to-CDUPS affirmation flow

[[stakeholders/mo]] performs affirmation in RATAN to facilitate settlement.

When a trade is affirmed directly in RATAN without an update in CDUPS, RATAN sends the affirmation status to CDUPS. CDUPS returns an ACK after receiving the status. When CDUPS receives `EconAffirm`, it marks the affirmation status as “Under Investigation” in the described business condition.

RATANONE is explicitly stated not to send duplicate `EconAffirm` messages to CDUPS. The source does not define the deduplication key, persistence model, retry behavior, or receiver-side handling of an unexpected duplicate.

## Interface identifiers

### Flow 1: RATANONE to CDUPS

```text
RATANONE -> FM-EDMi(JMS-Json) -> CDU PS

v1/post-trade/51358-ratanone/cdups/json-1.0/ecoaffirm/pub
```

### Flow 2: CDUPS to RATANONE

```text
CDUPS->FM-EDMi(JMS-Json)->RATANONE (ACK message)

q-51358-cdups-ratanone-ack

[CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub
```

The source also summarizes the transport as Solace. It does not explain whether Solace is the underlying transport for FM-EDMi, an alternative description, or a separate layer.

## Affirmation-status mapping

The following table is preserved from the source:

| **CDUPS Affirmation Status** | **RATAN Affirmation status to CDUPS** | **CDUPS Affirmation Status** | **Action on CDUPS** |
| --- | --- | --- | --- |
| 1. Awaiting Affirmation 2. “Affirmation : Pending approval” (with Checker) 3. Under Investigation (SSI affirmed, Economic not affirmed) | Econaffirm | Under Investigation (Economics Affirmed as True) | 1. CDUPS to consume Affirmation Status from RATAN and send ACK to RATAN 2. CDUPS should update Econaffirm Status in CDUPS. 3. Send to Stella if Acked. (econaffirm) |
| 1. Phone affirmed 2. Email affirmed 3. Confirmation Match 4. Under Investigation (SSI not affirmed, Economic affirmed) 5. Affirmation Suppressed | Econaffirm | Affirmation Status to CDUPS | 1. CDUPS to send Nack with appropriate reason- |

The table is structurally ambiguous. It does not clearly distinguish source state, transmitted state, resulting state, and action. “Under Investigation” appears in more than one business context, and the source does not define the NACK reason taxonomy.

## Operational relationship

The source references the [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA). It states that the trade-stamping API is missing from the OLA and provides no connection details, interface-team contact, troubleshooting steps, known issues, or complete message schemas.

This source therefore contributes a routing and interface inventory to [[concepts/ratan-interface-architecture]] and [[concepts/ratan-interface-inventory]], but it is not a complete production API contract.

## Evidence limitations

The source does not specify:

- The stamping API endpoint, request, response, authentication, retry, or error contract.
- The schemas, headers, correlation identifiers, or versioning rules for `EconAffirm`, ACK, and NACK messages.
- The relationship between Solace and FM-EDMi.
- The exact meaning of “inbound, outbound” for the BCS route.
- The deduplication key or persistence requirements for `EconAffirm`.
- Whether “Send to Stella if Acked” applies only to FMRP trades.
- Whether the ACK queue and publication path are both required.
- Whether the referenced OLA is current or should be amended.
