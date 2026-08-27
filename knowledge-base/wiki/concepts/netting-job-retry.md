---
type: concept
title: Netting Job Retry
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, retry, job-failure, swap-agent, operations]
related: [swap-agent, cashflow-auto-netting, pending-auto-netting-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---
# Netting Job Retry

## Definition

Netting job retry is the re-execution of a failed auto-netting job after a defined delay.

## Swap Agent requirement

The Swap Agent Day2 test case specifies that:

1. The initial auto-netting job fails.
2. A retry job starts 30 minutes after the failure.
3. Eligible cashflows are successfully netted during the retry.

The source records the expected and actual results with the same wording, but does not provide job identifiers, timestamps, failure-injection details, logs, or formal test-status values.

## Scope

The 30-minute retry behavior is evidenced for Swap Agent Day2 processing only. It should not be treated as a universal Ratan netting-job policy without additional evidence.
