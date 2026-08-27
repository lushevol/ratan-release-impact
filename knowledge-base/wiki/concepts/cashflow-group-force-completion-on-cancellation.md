---
type: concept
title: Cashflow Group Force Completion on Cancellation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-group, cancellation, force-completion, h2]
related: [h2-booking-model, h1-h2-historical-cashflow-group-continuity, cashflow-reinstatement-and-replay, cash-settlement-exception-handling, what-are-the-force-completion-semantics-for-cancelled-historical-cashflow-groups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# Cashflow Group Force Completion on Cancellation

The supplied H1-to-H2 cutover scenarios specify a narrow exceptional rule: when `C3` is found in a historical four-cashflow group and arrives with status `CNCL` after H2 go-live, the adaptor must send force complete to the group.

In the illustrated case, the group is reported as `COMPLETED` with a cashflow count of 4, while the member statuses include `C1 SNTR`, `C2 SNTR`, `C4 SNTR`, and `C3 CNCL`.

## Scope and Limits

This is not a general cancellation lifecycle definition. The source does not establish:

- Whether `CNCL` counts as an arrived member for cardinality purposes.
- Whether force completion updates every group member.
- What event, audit record, or downstream notification is emitted.
- Whether later events are accepted after force completion.
- Retry, deduplication, ordering, and idempotency rules.

The concept is related to [[cashflow-reinstatement-and-replay]] and [[cash-settlement-exception-handling]], but the source concerns cancellation-triggered completion rather than replay, reinstatement, or a complete exception state machine.