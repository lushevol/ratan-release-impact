---
type: concept
title: BRDM Bank-Code Ingestion
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, brdm, bank-code, reference-data, fileit, ingestion]
related: [brdm, fileit, ratan, ratan-interface-architecture, fileit-file-arrival-notification, 5-ratan--17-ratan-interfaces--20-ratan-and-brdm-51330--1bpyud7, is-ratan-brdm-51330-or-51358-the-canonical-interface-identifier, what-is-the-authoritative-brdm-bank-code-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and BRDM 51330.md"]
---
# BRDM Bank-Code Ingestion

BRDM Bank-Code Ingestion is the documented high-level flow by which [[ratan]] is intended to receive global bank-code reference data from [[brdm]] through [[fileit]].

```text
BRDM → FileIT → Ratan
```

## Scope

The source identifies the data feed as **Bank Code** and its country scope as **Global**.

## Evidence boundary

The flow is explicitly stated in the source but is not an implementable specification. In particular, it does not define:

- whether BRDM pushes data, FileIT publishes or notifies, or RATAN extracts data;
- transport, authentication, encryption, endpoint, or directory configuration;
- file name, encoding, schema, data dictionary, and versioning;
- delivery schedule, cut-off, latency target, acknowledgement, retry, or replay;
- validation, duplicate handling, reconciliation, correction, and data-quality processes;
- monitoring, alerting, support ownership, escalation, or incident recovery.

This flow is an instance of [[ratan-interface-architecture]], but it must not be assumed to follow the mechanics of [[fileit-file-arrival-notification]] or other RATAN reference-data ingestion paths.

## Identifier ambiguity

The source filename uses 51330, while its body calls the target “RATAN - 51358.” The canonical identity is unresolved in [[is-ratan-brdm-51330-or-51358-the-canonical-interface-identifier]].