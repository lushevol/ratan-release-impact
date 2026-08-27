---
type: query
title: Is Auto-Netting Update Approval Atomic?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, transactions, idempotency, rule-lifecycle]
related: [auto-netting-rule-lifecycle, auto-netting-rule-version-replacement, auto-netting-rule-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Is Auto-Netting Update Approval Atomic?

Approval of a pending replacement is documented as two events:

1. `REMOVE` the old rule to `DEAD`.
2. `CONFIRM` the new rule to `LIVE`.

The source does not state whether these actions are one transaction, their required ordering, their idempotency guarantees, or recovery behavior if one succeeds and the other fails.

## Questions to Resolve

- Must the old rule be retired before the replacement is activated?
- Is there an atomic backend transaction or an event-saga/compensation process?
- Which rule version is eligible for runtime evaluation while the replacement is `UPDATE_PENDING`?
- How are duplicate deliveries, partial failures, and replay handled?
- Can a failed approval leave no LIVE rule, or can concurrent consumers observe both versions as eligible?

The answer defines the availability and correctness model for [[auto-netting-rule-version-replacement]].