---
type: concept
title: Murex-RATAN Batch File Triplet
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, csv, batch, reconciliation, file-interface]
related: [uk-murex-ratan-high-volume-cashflow-feeding, ratan-batch-ack-nack-gating, murex-ratan-cashflow-message-contract, murex-ratan-cashflow-reconciliation, authoritative-uk-batch-file-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# Murex-RATAN Batch File Triplet

A UK Murex-to-RATAN batch consists of three files sharing a batch date and sequence number:

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Base.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Snapshot.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Completion_ZZZZ.csv
```

The Base file contains payment records, Snapshot provides status records, and Completion carries the expected Base-file payment count. RATAN uses the count for reconciliation.

A separate daily marker completes publication:

```text
FMRP_Murex_Payments_YYYYMMDD_END.csv
```

Murex sends the daily marker even when it publishes no batches. The source does not define the formal CSV serialization contract or fully define behavior for missing, late, duplicate, or out-of-order sequences.