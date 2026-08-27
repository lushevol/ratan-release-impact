---
type: concept
title: Cashflow Status Change Event Contract
tags: [cashflow, status-change, scbml, xml, event-contract]
related: [scbml, razor, fx-cashflow-status-write-back, scbml-event-payload-storage-impact, cashflow-version-tuple-comparison]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md"]
---
# Cashflow Status Change Event Contract

The observed contract is an SCBML XML message with type `CashflowStatusChange`, message version `1.0`, payload type `cashflowPayload`, and payload version `4-0`.

Its header includes sender provenance, initiation time, tracking ID, and `Insert` event metadata. Its business payload contains:

- a Razor-scheme `cashflowId`;
- a Razor-scheme trade `linkId`;
- a scalar `id` using a Razor version scheme;
- workflow `state`;
- `isPaymentReversal`;
- `paymentDate`; and
- `settledCashCurrency`.

## Identity and Version Boundaries

The sample contains several potential correlation values: `cashflowId`, `linkId`, `trackingId`, and `id`. It does not state which is authoritative for recipient matching or deduplication.

Likewise, the scalar Razor `id` has a version-oriented scheme but does not establish its business meaning or prove compatibility with [[cashflow-version-tuple-comparison]]. Consumers must not assume that it maps to a Cash Settlement version tuple without corroborating contract evidence.

## Format Note

Although the source calls the artifact “Sample Json,” the supplied payload is XML and declares `payloadFormat` as `XML`. XML is therefore the authoritative observed format for this sample.