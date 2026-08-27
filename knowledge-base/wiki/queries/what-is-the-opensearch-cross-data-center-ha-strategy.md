---
type: query
title: What Is the OpenSearch Cross-Data-Center HA Strategy?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, high-availability, cross-cluster-replication, disaster-recovery]
related: [opensearch, ratan-opensearch-rollout, db-to-opensearch-data-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# What Is the OpenSearch Cross-Data-Center HA Strategy?

The source identifies an HA issue: CCR does not work for synchronization between two data centers. It does not provide an alternative replication design, failover model, recovery objective, consistency requirement, or operational runbook.

This must be resolved before OpenSearch can be considered ready for broad production reliance.