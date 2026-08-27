---
type: concept
title: SSI Refresh Propagation
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, refresh, notifications, cashflow, consistency]
related: [ssi-stamping-reference-data, static-reference-data-synchronization, trade-level-ssi-stamping, what-is-the-authoritative-ssi-refresh-impact-and-reconciliation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# SSI Refresh Propagation

SSI refresh propagation is the proposed process for updating trade-level and cashflow-level SSI results after SSI data changes and notifying downstream systems.

## Proposed scope

The design intends to:

- Identify impacted trade stamping results.
- Identify impacted cashflows.
- Refresh the latest applicable trade SSI result.
- Refresh SSI stored on affected cashflows.
- Notify downstream consumers through an SSI notification topic.

The source says refresh should affect only the current latest major version of a trade.

## Ordering and consistency

The notification topic is described as single-partitioned so consumers process notifications sequentially. This does not by itself guarantee ordered UBER input, correct version selection, duplicate suppression, or reconciliation between trade results and cashflows.

The source does not specify the event payload, impacted-record query, refresh transaction, retry policy, replay behavior, or downstream delivery guarantee.

## Status

SSI refresh propagation is an architectural goal with incomplete implementation details. It should be coordinated with [[concepts/static-reference-data-synchronization]] and the open refresh contract query.