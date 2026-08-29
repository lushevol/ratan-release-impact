---
type: concept
title: Auto-Netting Rule Version Replacement
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, versioning, maker-checker, rule-lifecycle]
related: [auto-netting-rule-lifecycle, auto-netting-rule-event-contract, is-auto-netting-update-approval-atomic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Auto-Netting Rule Version Replacement

A change to a LIVE `AUTO_NETTING` rule is represented as a replacement record rather than an in-place mutation.

The proposed rule is saved in `UPDATE_PENDING` and identifies the replaced record through `referenceRuleId`. On approval, the documented sequence removes the old record as `DEAD` and confirms the new record as `LIVE`.

## Operational Implications

- The old LIVE rule and proposed replacement may coexist as records during approval.
- Consumers need a clear selection rule so a pending replacement is not treated as operationally active.
- Update approval involves at least two events, making ordering, transactional atomicity, retry behavior, and compensation material integration concerns.
- The source does not state whether removal of the previous rule and activation of the replacement are atomic.

The unresolved execution and recovery contract is tracked in is auto netting update approval atomic.