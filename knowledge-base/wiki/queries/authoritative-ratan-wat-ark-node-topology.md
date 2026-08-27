---
type: query
title: What Is the Authoritative RATAN WAT-ARK Node Topology?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, topology, wat, ark, disaster-recovery, open-question]
related: [ratan, wat, ark, redis-and-vip-failover, ratan-disaster-recovery-failover]
sources: ["RATAN/RATAN -Service Restart Guide/RATAN DR Plan.md"]
---
# What Is the Authoritative RATAN WAT-ARK Node Topology?

## Question

What is the authoritative mapping among WAT, ARK, the `P`, `S`, `A`, and `B` node labels, and the named hosts referenced by the RATAN DR runbook?

## Evidence requiring clarification

The runbook says that WAT→ARK service checks should show services on the “p node only,” while ARK→WAT checks should show services on the “S node only.” It later calls for health checks on the A node and B node. The source also mentions hosts including `uklvapapp590` and `uklvasapp590` without defining their roles or relationship to the site labels.

This ambiguity affects VIP placement, Redis validation, Eureka interpretation, service-stop targets, and post-network verification.

## Needed resolution

An authoritative topology record should identify:

- The environment represented by each node label.
- The hostnames belonging to each environment and node role.
- Expected service placement during WAT→ARK and ARK→WAT.
- Expected Redis master and VIP locations at each stage.
- The authoritative dashboards or Rundeck outputs for validation.