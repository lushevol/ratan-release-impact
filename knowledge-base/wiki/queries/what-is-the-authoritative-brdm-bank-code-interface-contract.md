---
type: query
title: What Is the Authoritative BRDM Bank-Code Interface Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, brdm, bank-code, interface-contract, fileit, operations]
related: [brdm, fileit, ratan, brdm-bank-code-ingestion, operational-level-agreement, 5-ratan--17-ratan-interfaces--20-ratan-and-brdm-51330--1bpyud7]
sources: ["RATAN/RATAN -Interfaces/Ratan and BRDM 51330.md"]
---
# What Is the Authoritative BRDM Bank-Code Interface Contract?

## Question

Which approved document or system record defines the technical and operational contract for global bank-code data moving from [[brdm]] through [[fileit]] into [[ratan]]?

## Known information

The available source documents only this high-level route:

```text
BRDM → FileIT → Ratan
```

It also links to a RATAN OLA location, but does not demonstrate that the OLA covers this feed or provide any applicable terms.

## Missing contract elements

An authoritative contract should identify:

- the producer, transfer-layer, consumer, data-quality, and incident owners;
- the delivery initiation model and FileIT responsibilities;
- transport configuration, security controls, and environment-specific endpoints;
- file or message schema, encoding, naming, data dictionary, and versioning;
- cadence, cut-offs, service-level targets, acknowledgement, retry, and replay;
- validation, deduplication, reconciliation, correction, and retention rules;
- monitoring, alerting, exception handling, escalation, and support procedures.

## Resolution path

Locate an approved interface specification, FileIT configuration record, service catalogue entry, or OLA explicitly covering the BRDM bank-code feed. Validate the discovered record against the identifier ambiguity tracked in [[is-ratan-brdm-51330-or-51358-the-canonical-interface-identifier]].