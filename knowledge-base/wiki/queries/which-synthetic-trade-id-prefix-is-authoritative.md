---
type: query
title: Which Synthetic Trade-ID Prefix Is Authoritative?
created: 2026-08-22
updated: 2026-08-22
tags: [trade-id, data-enrichment, ratan, downstream-integration]
related: [blank-flows-enrichment, dummy-trade-id-management, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# Which Synthetic Trade-ID Prefix Is Authoritative?

The requirement is internally inconsistent about the synthetic trade ID created when Murex sends trade ID `0`.

## Conflicting evidence

- The narrative says RATAN should create `R` plus the Murex flow ID, for example `R112517395`.
- The snapshot-file example uses `R112517395`.
- The real-time MxML and batch enrichment examples populate `TRN_ORGID` / original transaction ID with `MTR112517395`.

## Decision needed

Confirm one identifier convention for real-time, batch, snapshot, RATAN internal processing, and downstream removal logic. Also confirm the target output value for downstream systems once the synthetic identifier is removed.