---
type: query
title: What Is the Approved Indonesia GDC-ID Message Processing Topology?
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, gdc, topology, messaging, data-residency, disaster-recovery]
related: [indonesia-hybrid-gdc-id-message-flow, ratanone-message-bridge, ratan-cash-settlement-batch-service, cash-settlement-dc-failover-strategy, what-data-residency-controls-apply-to-ratan-indonesia-session-and-disaster-recovery-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# What Is the Approved Indonesia GDC-ID Message Processing Topology?

## Question

What is the approved steady-state topology for the GDC-only batch and MXG paths, ID-driven Netting, and Message Bridge consumption in the Indonesia deployment?

## Evidence

The implementation plan states that Batch and the MXG cashflow adaptor are GDC-only, the batch service publishes to `Cash_Settlement_Mxg_Inbound_Batch_All`, and [[ratanone-message-bridge]] has a mandatory GDC deployment dependency. It also raises possible GDC Kafka data synchronization and a pending DR solution.

## Decisions needed

- Whether GDC-only dependencies are transitional or permanent.
- Whether data is replicated, remotely consumed, or transferred through another path.
- Event ownership, ordering, deduplication, replay, and recovery responsibilities.
- Data-residency, NAS/FileIT, and disaster-recovery controls.
- The active/passive and fencing model for cross-environment processing.

The source is a tracker and does not answer these questions.