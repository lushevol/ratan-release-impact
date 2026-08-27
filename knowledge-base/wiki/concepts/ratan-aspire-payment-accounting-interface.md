---
type: concept
title: Ratan-Aspire Payment Accounting Interface
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, aspire, payment-accounting, batch-interface, fileit]
related: [ratan, aspire, fileit-file-arrival-notification, settlement-accounting, operational-level-agreement, what-is-the-authoritative-ratan-to-aspire-payment-accounting-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Aspire 51282.md"]
---
# Ratan-Aspire Payment Accounting Interface

The Ratan-Aspire Payment Accounting Interface is a documented high-level batch flow:

```text
Ratan --(FileIT)-->Aspire
```

The source directly states that a Payment Accounting message travels from [[ratan]] to [[aspire]] via FileIT in batch mode.

## Confirmed scope

- Ratan is the sender.
- Aspire is the receiver.
- FileIT is the named intermediary transport mechanism.
- The payload is described as a Payment Accounting message.
- Processing is described as batch rather than real-time.

## Unconfirmed details

The source does not provide a file or message schema, a FileIT route or job identifier, transfer protocol, security controls, batch schedule, calendar policy, delivery acknowledgement, reconciliation, duplicate handling, retry process, replay procedure, support contacts, or troubleshooting runbook.

The Payment Accounting label suggests a possible relationship to [[settlement-accounting]], but the source does not establish that this flow is produced by Ratan Settlement or any particular accounting stage.

An OLA location is referenced, but interface-specific commitments are not reproduced or confirmed. See [[operational-level-agreement]].

## Authority status

The interface page records review activity dated 2026-01-09, while its Status field is blank despite template guidance that reviewed articles should be marked Published. The document therefore cannot be treated as a complete or confirmed operational contract.