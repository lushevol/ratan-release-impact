---
type: concept
title: UK Murex-RATAN High-Volume Cashflow Feeding
created: 2026-08-24
updated: 2026-08-24
tags: [uk, murex-211, ratan, high-volume, cashflow, integration]
related: [murex-ratan-bidirectional-cashflow-integration, murex-ratan-hybrid-batch-and-realtime-processing, murex-ratan-batch-file-triplet, payment-date-versus-value-date, uk-business-day-holiday-calendar-murex-feeding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# UK Murex-RATAN High-Volume Cashflow Feeding

The UK design uses two non-overlapping feed mechanisms because the source states that the CN/SG/IN/MY approach cannot accommodate UK payment volume.

- Real-time individual MxML files cover VD-1, VD, and VD+1 business day.
- CSV batch files cover VD T+2 through T+7 business day.
- CSV eligibility excludes weekends, 12.25, and 01.01.

The approach is specific to the UK Murex 2.11-to-RATAN migration and should not be assumed for other jurisdictions. Batch publication is proposed between GMT 00:00 and 19:00 but remains subject to confirmation.

The batch mechanism depends on [[murex-ratan-batch-file-triplet]] and [[ratan-batch-ack-nack-gating]].