---
type: concept
title: Partial-Success Exception Resolution
created: 2026-08-24
updated: 2026-08-24
tags: [exception-handling, resilience, retry, cash-settlement, NSTP]
related: [multiple-cashflow-exception-handling, cashflow-versioned-exception-orchestration, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# Partial-Success Exception Resolution

Partial-success exception resolution is the requirement that independently successful exception fixes remain applied when another fix in the same maker or checker task fails.

## Required behavior

For a cashflow with ten exceptions:

1. Nine fixes succeed.
2. One fix fails, for example because of a network or downstream error.
3. The nine successful fixes are not repeated.
4. The cashflow remains `WAITING / Pending_Operator`.
5. The next maker session exposes only the unresolved exception.
6. The unresolved exception can be retried independently.

## Why it matters

The behavior prevents operators from re-entering already successful fixes and reduces the risk of duplicate side effects such as repeated SSI stamping or payment-related operations.

## Unspecified implementation contract

The design does not define:

- Whether actions execute sequentially or in parallel.
- Whether each action has an independent transaction.
- The idempotency key for an action.
- How a timeout is distinguished from a confirmed failure.
- How an unknown downstream outcome is reconciled.
- How partial results are persisted and returned.
- How retries interact with cashflow version checks.

These omissions should be resolved before the behavior is treated as an implementation contract.