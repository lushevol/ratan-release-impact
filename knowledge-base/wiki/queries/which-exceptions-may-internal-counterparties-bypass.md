---
type: query
title: Which Exceptions May Internal Counterparties Bypass?
tags: [cash-settlement, exception-handling, internal-counterparty, controls]
related: [internal-counterparty-exception-bypass, hard-blocker-exception, swap-agent-coupon-release-block, inter-entity-cashflow-stp]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# Which Exceptions May Internal Counterparties Bypass?

The Inter-Entity STP requirement says that an internal-counterparty identifier can be used to bypass exceptions, but it does not define the permitted exception taxonomy.

## Questions

1. Are hard blockers eligible for bypass, or are they categorically non-bypassable?
2. Are compliance, sanctions, settlement-risk, SSI, static-data, accounting, message-generation, and release exceptions treated differently?
3. Is bypass automatic, approval-based, or limited to specific operational states?
4. What audit event, authorization, monitoring, reconciliation, and fallback behavior is required?
5. What happens when the internal-counterparty identifier is missing, stale, ambiguous, or inconsistent?

Until these questions are answered, the requirement must not be interpreted as authorizing bypass of [[hard-blocker-exception]] or [[swap-agent-coupon-release-block]].