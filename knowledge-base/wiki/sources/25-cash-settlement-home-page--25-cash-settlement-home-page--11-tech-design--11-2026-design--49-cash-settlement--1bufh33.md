---
type: source
title: Fixing Flag Process in Indonesia
authors: [Xinmiao Huang, Haolin Song]
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14159448"
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [draft, indonesia, ratan, murex, pending-fixing-flag, kafka, solace]
related: [indonesia-pending-fixing-flag-relay, fixing-flag-entity-based-routing, batch-service, mxg-adaptor, message-bridge, nas, kafka, solace, indonesia-ratan-data-residency-isolation, ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment, what-is-the-authoritative-indonesia-fixing-flag-event-contract, what-is-the-authoritative-indonesia-cashflow-classification-rule-for-fixing-flags, what-existing-revert-logic-is-invoked-for-indonesia-pending-fixing-flags, what-is-the-approved-gdc-indonesia-kafka-solace-topology-for-fixing-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# Fixing Flag Process in Indonesia

**Status:** DRAFT  
**Target release:** Sep. / Nov. (year not specified)  
**ADO:** [Story 14159448 — Murex Pending Fixing Flag integration via solace](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14159448)

This draft proposes a pending-fixing-flag integration for Ratan Indonesia. Ratan GDC currently processes a Murex fixing-flag batch file from NAS, but direct cross-country NAS consumption is stated to be unavailable for Indonesia. The proposed alternative is to identify Indonesia cashflows in GDC and relay fixing-flag messages through Kafka and FM Solace to Indonesia.

## Proposed flow

```text
Murex fixing-flag batch file on NAS
  → GDC batch-service
  → mxg-adaptor booking-entity FMID lookup
  → GDC Kafka topic
  → GDC message-bridge
  → FM Solace topic
  → FM Solace queue
  → Indonesia message-bridge
  → Indonesia Kafka topic
  → Indonesia batch-service
  → existing revert logic
```

The document describes this as a targeted pending-fixing-flag solution, not a general redesign of Murex cashflow integration.

## Change scope

| # | Service Name | Change Type | Description |
| --- | --- | --- | --- |
| 1 | `batch-service` | code change | 1. **[GDC take effect]** batch file processing add logic: 1. Query adaptor API to get FM entity 2. Publish to new Kafka topic if identified as an Indonesia cashflow. 2. **[ID take effect]** consume real time message from Kafka topic and follow existing revert logic |
| 2 | `mxg-adaptor` | code change | provide API to query cashflow and booking entity fmid |
| 3 | `message-bridge` | config flow change | 1. **[GDC take effect]** source Kafka topic target is FM solace topic 2. **[ID take effect]** source FM solace queue target is Kakfa |
| 4 |  |  | Solace topic & creation form |

## Architectural implications

- The asserted cross-country NAS restriction is a specific implementation constraint supporting [[indonesia-ratan-data-residency-isolation]].
- The GDC-side [[batch-service]] is intended to route only Indonesia-relevant records after an FMID lookup from [[mxg-adaptor]].
- [[message-bridge]] is proposed to implement a Kafka → FM Solace → Kafka relay using [[kafka]] and [[solace]].
- The Indonesia-side `batch-service` is expected to invoke existing revert logic, but the draft does not define that logic or its state transition.

## Incomplete design items

The draft does not specify the Indonesia cashflow-classification rule, `mxg-adaptor` API contract, event schema, keys, idempotency, ordering, retry and replay behaviour, topic and queue names, ownership, security, monitoring, reconciliation, or acceptance criteria.

The cited “revert logic” must not be assumed to be equivalent to undo/revive, cancellation, or a defined cashflow-status transition without further evidence.

## Related work

This draft extends the broader [[ratan-indonesia-onshoring-2026]] and [[ratan-indonesia-isolated-deployment]] efforts. It is a proposed application of data-locality isolation and hybrid batch-to-real-time processing, rather than an authoritative end-to-end integration specification.