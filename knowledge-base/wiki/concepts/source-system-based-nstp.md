---
type: concept
title: Source-System-Based NSTP
created: 2026-08-23
updated: 2026-08-23
tags: [NSTP, source-system, clearing, payment-controls, RATAN]
related: [ratan, clearing-trade-payment-risk, clearing-status-propagation, ratan-netting-rule-check]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md"]
---
# Source-System-Based NSTP

Source-system-based NSTP is a fallback payment control that places payments into NSTP according to `SRC_SYSTEM` when a reliable trade-level clearing indicator is unavailable.

## Intended use

For a system such as [[entities/swapswire]], RATAN could hold the original bilateral payment C1 rather than allowing STP and VD-1 auto-release. If novation occurs, C1 can be cancelled and replacement payment C2 can be held for clearing-counterparty netting.

## Benefits

- Does not require the clearing indicator to be included in the payment message.
- Can use a field already available in RATAN.
- Provides a conservative control for source systems whose initial messages lack clearing status.

## Limitations

The rule may hold normal non-clearing payments unnecessarily if the same source system produces both clearing and non-clearing trades. This can increase NSTP volume, manual workload, and operational delay. It also does not resolve the underlying synchronization gap between Murex and RATAN.

## Required validation

Before deployment, analysis should measure the proportion of clearing and non-clearing flows by source system, product, entity, and payment type. The rule should define exceptions and precedence when an explicit clearing status is later available. A source-system rule should not be treated as proof that every payment from that system requires clearing treatment.