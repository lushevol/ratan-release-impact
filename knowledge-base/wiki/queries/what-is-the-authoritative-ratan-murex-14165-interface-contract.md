---
type: query
title: What Is the Authoritative RATAN-Murex 14165 Interface Contract?
tags: [ratan, murex, interface-14165, interface-contract, settlement, open-question]
related: [ratan-murex-settlement-cashflow-interface, murex-ratan-batch-acknowledgement-protocol, murex-to-ratan-message-conversion, ratan, murex-g2000]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex 14165.md"]
---
# What Is the Authoritative RATAN-Murex 14165 Interface Contract?

## Known evidence

Interface 14165 provides an operational overview of Murex-to-RATAN settlement-cashflow delivery, RATAN status return, batch naming, acknowledgement gating, and inbound SWIFT MT/Payment XML conversion. Its Interface Specification section is empty, and its document-status field does not confirm publication.

## Required evidence

An authoritative contract should establish:

- MQ queue or topic names, endpoint ownership, message schemas, and security controls.
- SFTP destinations, credentials or access model, encryption, permissions, retention, and archive rules.
- CSV schemas and formal semantics for Base, Snapshot, Completion, end-of-day, ACK, and NACK files.
- Batch file ordering, atomicity, idempotency, duplicate detection, retry, replay, and recovery rules.
- ACK/NACK validity criteria, status vocabulary, correlation identifiers, and timeout escalation procedures.
- Value-date edge cases, calendar authority, holiday handling, and treatment beyond T+7.
- Supported SWIFT MT, Payment XML, and ISO 20022 mapping definitions.
- Accountable owners and the current publication or approval status.

## Current conclusion

The available source is insufficient to establish a complete, authoritative technical interface contract.