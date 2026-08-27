---
type: source
title: RATAN and Murex 14165
authors: [Yunzhe Ta, Junying Jiang, Zhenzhen Liu]
year: 2026
url: ""
venue: Confluence
tags: [ratan, murex, settlement, cashflow, interface-14165, operational-procedure]
related: [ratan, murex-g2000, mx-2-11, ratan-murex-settlement-cashflow-interface, murex-ratan-batch-acknowledgement-protocol, murex-to-ratan-message-conversion, operational-level-agreement]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex 14165.md"]
---
# RATAN and Murex 14165

This operational interface overview describes settlement-cashflow processing and payment-message conversion between [[murex-g2000]] and [[ratan]].

The document was updated and reviewed on 2026-02-02, but its review-status field is blank. It should therefore be treated as an attributed operational reference rather than confirmed published interface specification. Its Interface Specification section is empty.

## Settlement cashflow flow

Murex sends settlement cashflow messages to RATAN for processing. After processing, RATAN returns updated cashflow status to [[mx-2-11]] for end-to-end reconciliation.

Routing depends on value date and corrective status:

- T−1 through T+1 payments are delivered in real time through MQ for immediate RATAN processing.
- T+2 through T+7 payments are delivered as Murex batch files through SFTP to the RATAN Shared NAS. The stated flow excludes weekends and public holidays.
- Fix Flag manual or corrective files are delivered through SFTP for reprocessing regardless of value date.

The document does not define cut-offs, the applicable holiday calendar, treatment of payments outside T−1 through T+7, duplicate controls, message schemas, or status vocabulary.

## Batch operations

Murex publishes batches every two hours from GMT 00:00 through 18:00. Each batch consists of Base, Snapshot, and Completion files in:

```text
/apps/ratannas/murex_ratan_transfer/payment
```

```text
Base:
FMRP_Murex_Payments_YYYYMMDD_XXX_Base.csv

Snapshot:
FMRP_Murex_Payments_YYYYMMDD_XXX_Snapshot.csv

Completion:
FMRP_Murex_Payments_YYYYMMDD_XXX_Completion_ZZZZ.csv

End-of-day marker:
FMRP_Murex_Payments_YYYYMMDD_END.csv

Acknowledgement:
FMRP_Murex_Payments_YYYYMMDD_XXX_Ack.csv

Negative acknowledgement:
FMRP_Murex_Payments_YYYYMMDD_XXX_Nack.csv
```

`YYYYMMDD` is the batch date. `XXX` is the daily sequence number (`001` through `010`). `ZZZZ` is the Base-file payment count and is intended for reconciliation.

Murex sends the end-of-day marker even if no batch was processed that day. Murex cannot automatically regenerate a batch file, so it waits for a RATAN ACK before processing the next batch. RATAN sends ACK or NACK files to a different folder, whose location is not specified. If Murex receives no RATAN response within 30 minutes, batch processing is held and Murex PSS investigates; a NACK also requires Murex PSS investigation.

The source does not define CSV layouts, the ordering or atomic-delivery requirement of the three files, ACK/NACK content, replay semantics, or recovery from delayed or duplicate acknowledgements.

## SWIFT and payment-message conversion

Murex sends SWIFT MT messages and Payment XML through MQ to RATAN. RATAN converts them to “MX (ISO 20022)” format for downstream processing and reporting.

The document says full decommission migration from Murex is pending and will centralize this logic. It does not identify the target platform, migration owner or timeline, supported MT or ISO 20022 message types, mappings, validations, error handling, or downstream consumers.

This inbound conversion is distinct from [[ratan-swift-generation-design]], which concerns RATAN SWIFT generation.

## Operational reference

The document cites the BPMS/RATAN OLA as an operational reference:

<https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA>

The linked OLA content is not reproduced in the source and its commitments cannot be inferred from this document.

## Evidence limits

Interface 14165 establishes an operational Murex-to-RATAN settlement flow, a RATAN-to-MX 2.11 status return, batch acknowledgement gating, and a high-level inbound message-conversion flow. It is not a complete technical interface contract. Open contract gaps are tracked in [[what-is-the-authoritative-ratan-murex-14165-interface-contract]].