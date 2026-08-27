---
type: concept
title: Cashflow Version Tuple Comparison
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, versioning, consistency, ui-refresh]
related: [cashflow-notification-and-auto-refresh, cashflow-blotter, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md"]
---

# Cashflow Version Tuple Comparison

Cashflow version tuple comparison is the proposed freshness check for determining whether a notification changes the cashflow currently displayed in an open detail dialog.

## Tuple

The comparison uses:

```text
(cashflowVersion, cashflowBusinessVersion, cashflowMinorVersion)
```

The same logical version information also appears in nested fields in the example payload, including `cashflow_Version`, `cashflow_Business_Version`, and `cashflow_Minor_Version`.

## Intended Use

For a Level 2 notification:

1. Identify whether the notification concerns the cashflow currently open.
2. Compare the incoming version tuple with the displayed tuple.
3. If the versions differ, block normal actions and request or require refresh.
4. Reopen the latest cashflow after refresh.
5. Recalculate allowable actions from the latest status and exceptions.

A notification for a different cashflow should not affect the open detail dialog.

## Undefined Ordering Semantics

The source does not establish whether freshness means:

- Any component of the tuple differs.
- The incoming tuple is lexicographically greater.
- All components must differ.
- A domain-specific ordering rule determines which tuple is newer.

It also does not define handling for an older or out-of-order notification. This is an implementation-critical open question, tracked in [[queries/what-is-the-authoritative-cashflow-notification-and-auto-refresh-contract]].