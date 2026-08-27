---
type: query
title: What Is the Authoritative Ratan Batch Completeness Timeout and Recovery Policy?
tags: [ratan, batch-control, timeout, recovery, operations]
related: [ratan, cashflow-batch-control, murex-ratan-cashflow-ringfencing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# What Is the Authoritative Ratan Batch Completeness Timeout and Recovery Policy?

Ratan must hold incomplete batches and later batches that arrive out of order, but the functional requirement provides no operational recovery contract.

## Questions to resolve

- What timeout applies when a declared batch member never arrives?
- Which team receives alerts and has authority to override, replay, or discard a batch?
- How are duplicate members, late arrivals, and source resends identified and audited?
- Does release of a blocked batch require all predecessors to be dispatched, terminally processed, or manually approved?

The answer is required to turn [[cashflow-batch-control]] into an operable production control.