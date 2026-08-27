---
type: query
title: What Are the Withdrawal Holding-Queue and Unnetting Semantics?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, withdrawal, unnetting, holding-queue, cashflow]
related: [cashflow-unnetting, cashflow-lifecycle-stamping, withdrawal-new-cashflow-and-razor-release-check, data-persistence-node]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# What Are the Withdrawal Holding-Queue and Unnetting Semantics?

## Question

What exact workflow behavior applies when a Withdrawal targets an existing `NETTED` or `SPLIT` cashflow, or when the cashflow does not exist?

## Evidence

The source documents these rules:

- `SUSPENDED` and `SUSPENDED_MATURED` Withdrawals return `FAIL`.
- A `NETTED` or `SPLIT` cashflow whose resultant cashflow is not post released returns `FILTERED` so workflow can unnet first.
- If unnetting is not required, the holding queue is disabled.
- A nonexistent cashflow should not bypass holding disable and data persistence, although the exact control flow is unclear.

## Investigation needs

Confirm:

- The definition and authoritative source of “post released.”
- The meaning and handling of `FILTERED`.
- The owner of unnetting orchestration and retry.
- Whether persistence occurs before or after unnetting.
- Holding-queue behavior for nonexistent cashflows.
- Idempotency and ordering across event persistence, unnetting, and lifecycle execution.
- Recovery behavior after partial failure.

## Current position

The source establishes a conditional unnetting prerequisite but does not provide a complete Withdrawal state machine.
