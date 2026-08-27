---
type: concept
title: Murex-RATAN Batch Acknowledgement Protocol
tags: [murex, ratan, batch-processing, acknowledgement, nack, reconciliation, sftp]
related: [murex-g2000, ratan, ratan-murex-settlement-cashflow-interface, what-is-the-authoritative-ratan-murex-14165-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex 14165.md"]
---
# Murex-RATAN Batch Acknowledgement Protocol

The Murex-to-RATAN batch flow is an ordered, acknowledgement-gated operational protocol. Murex publishes a batch every two hours from GMT 00:00 through 18:00 and must wait for a RATAN ACK before proceeding with the next batch.

## File convention

Batch files are delivered to the stated RATAN Shared NAS location:

```text
/apps/ratannas/murex_ratan_transfer/payment
```

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Base.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Snapshot.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Completion_ZZZZ.csv
```

`YYYYMMDD` is the batch date, `XXX` is the daily sequence number from `001` through `010`, and `ZZZZ` is the count of payments in the Base file for reconciliation.

Daily completion is indicated by:

```text
FMRP_Murex_Payments_YYYYMMDD_END.csv
```

Murex sends this marker even when no batch was processed that day.

## Response control

RATAN responds in a different, unspecified folder using:

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Ack.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Nack.csv
```

If Murex receives no RATAN response within 30 minutes, the batch process is held. A RATAN NACK also causes Murex PSS to investigate. This control is important because the source states that Murex cannot automatically regenerate the batch files.

## Undocumented semantics

The source does not define Base, Snapshot, or Completion-file contents or their delivery order; it also omits ACK/NACK payload rules, archive and retention procedures, idempotency, delayed-response handling, and replay or recovery controls. These gaps prevent this procedure from serving as a complete protocol specification.