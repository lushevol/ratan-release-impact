---
type: query
title: What Does a RATAN Batch Acknowledgement Confirm?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, acknowledgement, batch-processing, operational-control]
related: [ratan-batch-ack-nack-gating, murex-ratan-batch-file-triplet, fmrp-cashflow-publication-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# What Does a RATAN Batch Acknowledgement Confirm?

Murex gates publication of the next batch on a RATAN ACK, but the source does not define ACK semantics.

Clarify whether an ACK means all three files were received, validated, reconciled, persisted, fully processed, or processed with permitted payment-level exceptions. The contract should also define response correlation, timeout handling, replay, duplicate delivery, and duplicate ACK/NACK behavior.