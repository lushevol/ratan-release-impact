---
type: query
title: What Are the Force-Completion Semantics for Cancelled Historical Cashflow Groups?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cancellation, force-completion, cashflow-group, h2]
related: [cashflow-group-force-completion-on-cancellation, h1-h2-historical-cashflow-group-continuity, cash-settlement-exception-handling, cashflow-reinstatement-and-replay, what-is-the-canonical-cash-settlement-exception-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
---
# What Are the Force-Completion Semantics for Cancelled Historical Cashflow Groups?

The Case 4 scenario states that an adaptor should send force complete when a `CNCL` cashflow is found in a historical H1 group after H2 go-live. It does not define the resulting system contract.

## Questions to Resolve

- Does a `CNCL` member count toward the group’s expected cashflow cardinality?
- Does force completion set group status only, or also change member statuses?
- What events, audit records, and downstream notifications are required?
- What happens when a late or corrected event arrives after force completion?
- How are duplicate messages, retries, and out-of-order events made idempotent?
- Is force completion an exception flow in the canonical state machine, or a normal terminal group transition?

The source supports only the scenario-specific rule documented in [[cashflow-group-force-completion-on-cancellation]]; it does not resolve the broader [[what-is-the-canonical-cash-settlement-exception-state-machine]].