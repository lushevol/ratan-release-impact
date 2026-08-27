---
type: query
title: What Is the Approved Idempotent Replay Procedure for Missing UBER Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, uber, cashflow-replay, idempotency, recovery]
related: [upstream-cashflow-replay-for-group-completion, uber-inbound-message-idempotency-and-error-state, message-bridge-deduplication-key-lifecycle, cashflow, sabre-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# What Is the Approved Idempotent Replay Procedure for Missing UBER Cashflows?

The release runbook proposes replaying a specific upstream cashflow when a RATAN group is incomplete, but it does not define a complete or approved replay procedure.

The investigation should establish:

1. Which team authorizes and performs the replay.
2. Which identifier distinguishes the missing cashflow and prevents duplicate processing.
3. How replay interacts with Uber inbound idempotency, Message Bridge deduplication, and RATAN group management.
4. Whether replay must preserve the original ordering, version, and business date.
5. Which SQL or operational checks confirm successful group completion.
6. How failed, duplicated, or partially applied replays are reconciled.

Until these points are documented, the runbook should be treated as a proposed contingency rather than a safe operational contract.
